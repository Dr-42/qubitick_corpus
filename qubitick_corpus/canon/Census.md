# $\langle qu(b(i(t|t))ick)\rangle$ — **Census** — The Computed Cells (Category B) and Their Consumption

**Role.** The census annex of the era canon: the tags whose primary deliverable is a computed table, card, ladder, orbit set, multiplet family, or count over a named configuration space, and whose tabulated values are cited by downstream consumers. The structural tags (identities, mechanisms, covariance laws, no-gos, uniqueness and scope theorems — Category A) live in Parts 1–4; the two categories are disjoint and complete over the FT series.
**Charter (the separation rule).** A tag is **Category B (census)** $\iff$ its primary deliverable is a computed data cell over a named configuration space and downstream consumers cite the tabulated values; **Category A (structural)** $\iff$ its primary deliverable is an identity, mechanism, covariance law, no-go, uniqueness, or scope theorem about the corpus's algebra, geometry, or dynamics — even when proved by exhaustive enumeration. Mixed tags are classified by primary deliverable; the census sides of Category-A tags (the cover-polynomial tables of FT.68, the frame catalogue of FT.93, the susceptibility census of FT.103) are consumed through those tags' own rows in Parts 3 — no B-classification is implied.
**Dep.** Parts 1–3 (cited by tag at use in each cell's **Req**). Nothing in Parts 1–2 cites this file; Part 3 and Part 4 cite its cells row-wise. The tag-level citation graph is acyclic (every **Req** resolves to an earlier tag or a marked forward pointer); `checks/verify_era_structure.py` machine-verifies ownership, closure, and acyclicity.
**Inventory.** 25 cells: FT.28, FT.32, FT.35, FT.42, FT.43, FT.44, FT.45, FT.49, FT.50, FT.51, FT.63, FT.64, FT.65, FT.69, FT.76, FT.78, FT.81, FT.83, FT.84, FT.96, FT.98, FT.99, FT.105, FT.114, FT.120. Format: Part 1 §0.4 (**Thm** · **Req** · **Pf** · **Phys**).
**External-data quarantine.** The [EXT] audit rows (FT.114, FT.120; and the audit clauses of FT.77, FT.79, FT.87, FT.104 in Part 3) are quarantined comparison data: tested, never trusted; they enter no derivation [P1, P5; FT.73(5) pattern].

---

## The cells

### FT.28 — First computation: the floor-fermion particle card

**Thm.** ($\Sigma_{\min}$ card.) Let $\Sigma_{\min}=\{p,q\}$ with the materialized 2-cycle $c=(e_1,e_2)$, $e_1=(p,q)$, $e_2=(q,p)$, as its interior [Def-H.4 floor; FT.24: $\kappa:=\widehat{ds}^{\,2}(e_1)=\widehat{ds}^{\,2}(e_2)\in\mathbb Z\setminus\{0\}$], observed by a single external neighbour $o$ through one real edge ($E_{\mathrm{bd}}=1$, $\delta\tau\ge1$; FT.17 hypotheses, Def-H.35). Then:
$$(1)\quad I_{\mathrm{hid}}=E_{\mathrm{int}}\ln2=2\ln2,\qquad m_{\mathrm{hid}}=\frac{2\ln2}{\mathfrak h}\qquad[\mathrm{FT.17},\ \mathrm{Def\text{-}H.9}(2)];$$
$$(2)\quad\Theta_{\mathrm{int}}=\Theta(c)=2\kappa\in2\mathbb Z,\qquad k=\kappa,\qquad\mathrm{Hol}_{\mathrm{int}}=+1\qquad[\mathrm{FT.22},\ \mathrm{FT.24},\ \mathrm{FT.25}];$$
$$(3)\quad\mathcal A(\Sigma_{\min};C)\supseteq\{G,H,W\};\qquad\mathrm{EM}\in\mathcal A\iff f_p\ne0\ \vee\ f_q\ne0\ [\mathrm{D3.3}];$$
$$\text{strong}\notin\mathcal A\ \text{necessarily}:\ n(q)=2\implies q\ \text{carries no slot index}\ [\mathrm{D3.1},\ \mathrm{CT3.11}(1):\ \text{colour slots at}\ n{=}3\ \text{only}];\quad\mathrm{Colour}(\Sigma_{\min})=\{p\};\quad\pi_C(p)\subseteq\Sigma_{\min}\ \text{impossible}\ [\mathrm{A1}:\ \text{partners distinct}]\implies\mathcal C=0\implies\text{block}\equiv0\ [\mathrm{FT.19}]:\ \textbf{the single-contact floor fermion is structurally colourless}\ (\text{colour-visible variant}:\ \mathrm{Rmk}\ \text{below});$$
$$(4)\quad\dim\mathcal K_{\Sigma_{\min}}=9\ (G{+}W{+}H\ \text{core})\ +\ 1\cdot[\mathrm{EM}\ \text{active}]\ \le\ 10;\qquad\text{general bound}\ \le18\ [\mathrm{FT.26}(3),\ \mathrm{CT0.14}];\quad18\ \text{is attained only in the inside-sealed variant}\ [\mathrm{Rmk}\ \text{below}:\ 9{+}1{+}8];$$
$$(5)\quad n(p)=3\ [e_1\ \text{out},\ e_2\ \text{in},\ \text{observer edge in}],\quad n(q)=2\ [e_1\ \text{in},\ e_2\ \text{out}]\qquad[\mathrm{D0.8}];\quad D_{\mathrm{tick}}(3)=2^{4}=16=C_{\mathrm{cap}},\quad O(2)=O(3)=0\ [\mathrm{CT0.5},\ \mathrm{CT0.6}]:\ \text{no oversubscription anywhere at the floor}\ [\mathrm{CT0.11}];$$
$$(6)\quad q:\ \text{boundary-channel read; the closed core}\ (\partial c=0\ [\mathrm{D1.4}])\ \text{carries basepoint sign data}\ q_{\mathrm{core}}(c;v)=\tfrac12(\sigma_{e_1}-\sigma_{e_k})\in\{-1,0,+1\}\ [\mathrm{FT.40}:\ \text{ternary},\ \omega\text{-covariant}\ [\mathrm{D2.6}]];$$
$$(7)\quad Z(\mathcal R,\Sigma_{\min})\ \text{poles}\iff1\in\operatorname{spec}\mathbf F_M^{(\Sigma_{\min})}\ [\mathrm{FT.26}];\qquad c\ \text{materializes}\implies\Theta(c)=2\kappa\ [\mathrm{FT.22},\ \mathrm{Def\text{-}H.16}].$$

**Req.** FT.17 (Def-H.35), FT.19, FT.20, FT.22, FT.24, FT.25, FT.26, FT.27; A1; Def-H.4, Def-H.9, Def-H.10, Def-H.15, Def-H.16; D0.8, D1.4, D3.1, D3.3, D3.4, D3.8, D3.9; CT0.5, CT0.6, CT0.11, CT0.14 (Part 1); CT3.11, CT3.17 (Part 2); CT4.9 (Part 2).

**Pf.**
$$
(1):\ E_{\mathrm{int}}=2\ (\text{both cycle edges have both endpoints in}\ \Sigma_{\min}\ [\mathrm{Def\text{-}H.12}]);\quad E_{\mathrm{bd}}=1\le4\cdot1\ \checkmark\ [\mathrm{FT.17}\ \text{hyp}]
$$
$$
\mathrm{CT4.9}(1):\ S(p)\le3\ln2\ \text{at}\ n{=}3,\ \text{channel-visible}\ 1\ \text{bit}\ <3\ \checkmark\ [\mathrm{FT.17}\ \text{Def-H.35}]\implies I_{\mathrm{hid}}=E_{\mathrm{int}}\ln2=2\ln2;\qquad m_{\mathrm{hid}}=I_{\mathrm{hid}}/\mathfrak h\ [\mathrm{Def\text{-}H.9}(2)]
$$
$$
(2):\ \Sigma_{\min}\setminus\partial\Sigma_{\min}=\{e_1,e_2\}=E(c)\ (\text{single chain, edge-disjoint trivially}):\ \Theta_{\mathrm{int}}=\Theta(c)=2\kappa\ [\mathrm{FT.24}(1)];\qquad\mathrm{Hol}_{\mathrm{int}}=(-1)^{2\kappa}=+1,\ k=\Theta/2=\kappa\ [\mathrm{FT.25}(1),(3)]
$$
$$
(3):\ \text{FT.20 rows}:\ G:\ I_{\mathrm{hid}}=2\ln2\ne0\ \checkmark;\quad H:\ \text{folded into}\ G\ [\mathrm{Def-H.36}]\ \checkmark;\quad W:\ \Theta_{\mathrm{int}}=2\kappa\ne0\ (\kappa\ne0)\ \checkmark\ [\text{criterion fires in the sound direction}];\quad\mathrm{EM}:\ \exists v:\ f_v\ne0\ [\mathrm{D3.3}]
$$
$$
\text{strong}:\ n(q)=2\implies q\in V_2:\ \neg\exists\ \text{slot index at}\ q\ [\mathrm{D3.1}:\ n{=}3\ \text{slots}=\text{colour};\ \mathrm{CT3.11}(1)]\implies\mathrm{Colour}(\Sigma_{\min})\subseteq\{p\}
$$
$$
p\ \text{slot-carrying}\ (n(p)=3):\ \pi_C(p)\ne\varnothing\ \text{requires a distinct partner}\ [\mathrm{A1}];\ \text{the only candidate inside}\ \Sigma_{\min}\ \text{is}\ q,\ \text{slot-less}\implies\pi_C(p)\not\subseteq\Sigma_{\min}\ \forall C\implies\mathcal C(\Sigma_{\min};C)=0\ [\mathrm{Def\text{-}H.10}]\implies\text{block}\equiv0\ [\mathrm{FT.19}]\quad(\text{if}\ p\text{'s slot is colour-inert in}\ C:\ \mathrm{Colour}(\Sigma_{\min})=\varnothing\ 	ext{and the block vanishes on the no-content side — FT.27's case split})
$$
$$
(4):\ \text{block dims}\ [\mathrm{CT0.12},\ \mathrm{CT0.14}]:\ 5(G)+3(W)+1(H)=9;\quad\mathrm{EM}\ \text{active}:\ +1\ [\dim\mathcal K^{(\mathrm{EM})}=1]\implies\le10;\quad\text{general bound}\ 18\ [\mathrm{FT.26}(3)];\quad+8\ [\dim\mathcal K^{(\mathrm{strong})}=8,\ \mathrm{CT3.8}]\ \text{only in the inside-sealed variant}\ [\mathrm{Rmk}]
$$
$$
(5):\ n(p)=\partial^\leftarrow(p)+\partial^\rightarrow(p)=2{+}1=3,\quad n(q)=1{+}1=2\ [\mathrm{D0.8}:\ e_1,e_2\ \text{plus the observer edge at}\ p];\qquad\mathrm{CT0.5}:\ D_{\mathrm{tick}}(3)=2^{4}=16,\ D_{\mathrm{tick}}(2)=2^{3}=8;\quad\mathrm{CT0.6}:\ O(2)=O(3)=0;\quad\mathrm{CT0.11}:\ n\le3\ \checkmark
$$
$$
(6):\ \partial c=t(c)-s(c)=0\ [\mathrm{D1.4}:\ \text{closed}];\quad\text{core read}=\text{first/last edge registers at the basepoint}:\ q_{\mathrm{core}}=(\sigma_{e_1}-\sigma_{e_k})/2\ [\mathrm{D3.4}\ \text{on the ordered tuple},\ \mathrm{CT0.9}:\ \text{independent registers};\ \mathrm{EM.9}:\ \text{ternary, attained}];\quad\text{observer-facing read via transit channels}\ [\mathrm{Def\text{-}H.4},\ \mathrm{EM.9}]
$$
$$
(7):\ \mathrm{Def\text{-}H.16}+\mathrm{FT.26};\qquad\mathrm{FT.22}\ \text{at materialized}\ c.\ \blacksquare
$$

**Rmk (the dark floor).** With no observer edge ($E_{\mathrm{bd}}=0$): $\partial\Sigma_{\min}=\varnothing\implies\gamma(o,\Sigma_{\min})=\varnothing$ [Def-H.1] — the floor fermion is dark by construction: $I_{\mathrm{hid}}=E_{\mathrm{tot}}=2\ln2$, no read channel [FT.3's indistinguishability]. The observer edge is what lifts the floor into the spectrum bookkeeping — consistent with Def-H.4's external characterization.

**Rmk (the colour-visible variant).** Give $q$ its own single-contact observer edge ($E_{\mathrm{bd}}=2\le4\,\delta\tau$, $\delta\tau\ge1$): then $n(p)=n(q)=3$, both vertices slot-carrying [D3.1], and two sealing phases exist [FT.20 strong row]: **(i) inside-sealed** — $p$ triplet, $q$ antitriplet contracted by $\delta^i{}_j$ inside $\Sigma_{\min}$ (meson-type [D3.9, CT3.17]): $\mathcal C=1$, strong block active, $\dim\mathcal K_{\Sigma_{\min}}=9+1+8=18$ — the maximal observable mask [FT.26]; **(ii) outside-sealed or dangling** — $\mathcal C=0$, strong block $\equiv0$ [FT.19]. Bookkeeping: with two contacts FT.17's single-observer hypothesis no longer applies; $I_{\mathrm{hid}}$ becomes observer-relative [Def-H.9(2), FT.20 $G$ row]: $E_{\mathrm{tot}}=(2{+}2)\ln2$, $E_{\mathrm{vis}}(o_1)=\ln2\implies I_{\mathrm{hid}}(o_1)=3\ln2$ (the other observer's boundary bit is hidden from $o_1$), $m_{\mathrm{hid}}(o_1)=3\ln2/\mathfrak h$. The smallest colour-observable fermion floor is this variant — the sealed meson-type pair [FT.27 strong row].

**Phys.** The first particle card of the program, every entry derived: the floor fermion carries informational mass $m_{\mathrm{hid}}=2\ln2/\mathfrak h$ — two bits of hidden connectivity — an even interior winding $2\kappa$ with trivial interior parity, the integer label $k=\kappa$ as its spin candidate, charge readable only at its boundary, no colour at all in the single-contact case — structurally, not contingently: its one slot-carrying vertex has no possible partner inside — and no oversubscription anywhere ($O(2)=O(3)=0$). What remains open on the card is open by name, not by hand-waving: the charge read for closed cores (Gaps 14), the $k\to j$ rule (Gaps 11), and the pole-mass/$I_{\mathrm{hid}}$ relation (Gaps 7).

---

---

### FT.32 — The cycle floor family (single-contact $\Sigma_L$)

**Thm.** Let $\Sigma_L$ be a simple oriented $L$-cycle, $L\ge2$ [A1 excludes self-loops; D1.4], with materialized interior chain $c$ and a single observer contact at $v_1$ ($E_{\mathrm{bd}}=1\le4\,\delta\tau$, $\delta\tau\ge1$; FT.17 hypotheses, Def-H.35). Write $\kappa_e:=\widehat{ds}^{\,2}(e)$ for $e\in c$. Then:
$$(1)\quad E_{\mathrm{int}}=L,\qquad I_{\mathrm{hid}}=L\ln2,\qquad m_{\mathrm{hid}}=\frac{L\ln2}{\mathfrak h}\qquad[\mathrm{FT.17},\ \mathrm{Def\text{-}H.9}(2)];$$
$$(2)\quad n(v_1)=3,\ \ n(v_i)=2\ (i\ge2)\ [\mathrm{D0.8}];\qquad O(2)=O(3)=0,\ \ D_{\mathrm{tick}}(3)=16=C_{\mathrm{cap}}\ [\mathrm{CT0.5},\ \mathrm{CT0.6}];$$
$$(3)\quad\Theta_{\mathrm{int}}=\Theta(c)\in2\mathbb Z\ \text{if}\ c\ \text{materialized}\ [\mathrm{FT.22}];\qquad\mathrm{Hol}_{\mathrm{int}}=+1\ [\mathrm{FT.25}(1)];\qquad k=\Theta/2\in\mathbb Z;\qquad W\ \text{row fires}\iff\Theta\ne0;$$
$$(4)\quad\textbf{structural colourlessness}:\ \mathrm{Colour}(\Sigma_L)\subseteq\{v_1\}\ [\mathrm{D3.1}:\ \text{colour slots at}\ n{=}3\ \text{only};\ \mathrm{CT3.11}(1)];\ \ \pi_C(v_1)\subseteq\Sigma_L\ \text{impossible}\ [\mathrm{A1}:\ \text{partners distinct}]\implies\mathcal C=0\ \vee\ \mathrm{Colour}=\varnothing\implies\text{strong}\notin\mathcal A(\Sigma_L;C)\ \ \forall C;$$
$$(5)\quad\mathcal A(\Sigma_L;C)\supseteq\{G,H\}\ [G:\ I_{\mathrm{hid}}\ne0;\ H:\ \mathrm{Def-H.36}];\quad\mathrm{EM}\in\mathcal A\iff\exists i:\ f_{v_i}\ne0\ [\mathrm{D3.3}];\quad\dim\mathcal K_{\Sigma_L}=9\ (+1\ \mathrm{EM})\le10<18\ [\mathrm{FT.26},\ \mathrm{CT0.14}];$$
$$(6)\quad\text{minimality ladder for}\ \Theta(c)\ [\mathrm{FT.22}'\text{s constraint}\ \Theta\in2\mathbb Z]:\qquad\text{uniform-}\kappa:\ L\ \text{odd}\Rightarrow\kappa_{\min}=2,\ \Theta_{\min}=2L;\quad L\ \text{even}\Rightarrow\kappa_{\min}=1,\ \Theta_{\min}=L;$$
$$\text{all-nonnull per-edge-integral}\ [\text{scope}:\ \mathrm{FT.24}]:\ \Theta_{\min}=L+(L\ \mathrm{mod}\ 2);\qquad\text{null-permitting}:\ \Theta_{\min}=2\ (\kappa\ \text{profile}\ (1,1,0,\dots,0)\ [\mathrm{CT1.19a}:\ \kappa=0\iff\text{null}]);$$
$$\text{scope}:\ \text{uniform/all-nonnull regimes presuppose per-edge}\ \kappa\in\mathbb Z\ —\ \text{derived at}\ L{=}2\ [\mathrm{FT.24}]\ \text{and on round-trip-closed edges}\ [\mathrm{FT.34}(4),\ \text{forward}],\ \text{conditional for bare}\ L\ge3\ \text{cycles}\ [\text{Open Gaps 13 class (iii)}:\ \mathrm{FT.22}\ \text{alone permits}\ \kappa\in(2/L)\mathbb Z];\qquad\text{unconditional floor}:\ \Theta_{\min}=2\ \ \forall L\ (\text{rational uniform witness}\ \kappa\equiv2/L);$$
$$(7)\quad\Pi(\Sigma_L)=L^2\,\Theta\,(\ln2)^2\;\qquad L=2\ \text{reproduces FT.28's card verbatim (consistency)}.$$

**Req.** FT.17 (Def-H.35), FT.20, FT.22, FT.24, FT.25, FT.26, FT.27, FT.28; A1; Def-H.4, Def-H.9, Def-H.10, Def-H.15; D0.8, D1.4, D3.1, D3.3, D3.8, D3.9; CT0.5, CT0.6, CT0.11, CT0.13, CT0.14 (Part 1); CT1.19a (Part 2); CT3.11, CT3.17 (Part 2); CT4.9 (Part 2).

**Pf.**
$$
(1):\ E_{\mathrm{int}}=L\ (\text{cycle edges have both endpoints in}\ \Sigma_L\ [\mathrm{Def\text{-}H.12}]);\quad E_{\mathrm{bd}}=1\le4\cdot1\ \checkmark;\quad\mathrm{CT4.9}(1):\ S(v_1)\le3\ln2,\ \text{channel-visible}\ 1\ \text{bit}<3\ \checkmark\ [\text{as in FT.28}(1)]\implies I_{\mathrm{hid}}=L\ln2\ [\mathrm{FT.17}]
$$
$$
(2):\ \text{edge counts at vertices}\ [\mathrm{D0.8}]:\ v_1:\ 2\ \text{cycle}+1\ \text{observer}=3;\quad v_{i\ge2}:\ 1\ \text{in}+1\ \text{out}=2;\qquad\mathrm{CT0.5}/\mathrm{CT0.6}:\ D_{\mathrm{tick}}(n)=2^{n+1}:\ 8,\ 16;\quad O(2)=O(3)=0;\quad\mathrm{CT0.11}:\ n\le3\ \checkmark
$$
$$
(3):\ \Sigma_L\setminus\partial\Sigma_L=E(c)\ (\text{single chain}):\ \Theta_{\mathrm{int}}=\Theta(c)\in2\mathbb Z\ [\mathrm{FT.22}];\quad\mathrm{Hol}_{\mathrm{int}}=(-1)^{2\mathbb Z}=+1,\ k=\Theta/2\ [\mathrm{FT.25}(1),(3)];\quad W\ \text{criterion}:\ \Theta\ne0\ [\mathrm{FT.20}\ \text{row},\ \text{sound direction}]
$$
$$
(4):\ n(v_i)=2\ (i\ge2)\implies v_i\in V_2:\ \neg\exists\ \text{colour slot}\ [\mathrm{D3.1},\ \mathrm{CT0.13}:\ \text{strong strictly new only at}\ n{=}3]\implies\mathrm{Colour}(\Sigma_L)\subseteq\{v_1\};\qquad\text{FT.27's case split applies at}\ v_1:\ \text{block}\equiv0\ \forall C
$$
$$
(5):\ \text{FT.20 rows evaluated as in FT.28}(3);\qquad\dim:\ 5(G)+3(W)+1(H)=9\ [\mathrm{CT0.12}],\ +1\ [\mathrm{CT0.14}]
$$
$$
(6):\ \text{uniform}:\ \Theta=L\kappa\in2\mathbb Z:\ L\ \text{odd}\Rightarrow\kappa\ \text{even}\Rightarrow\kappa_{\min}=2;\quad L\ \text{even}\Rightarrow\kappa_{\min}=1;\qquad\text{all-nonnull}:\ \min\{\textstyle\sum\kappa_e:\ \kappa_e\ge1,\ \sum\in2\mathbb Z\}=L+(L\ \mathrm{mod}\ 2);\qquad\text{null-permitting}:\ (1,1,0,\dots,0):\ \Theta=2
$$
$$
(7):\ \Pi=E_{\mathrm{int}}^2\Theta(\ln2)^2\ =L^2\Theta(\ln2)^2;\qquad L=2:\ (1)\text{--}(5)\ \text{reduce to FT.28}(1)\text{--}(5)\ \text{line by line}.\ \blacksquare
$$

**Rmk (the mass ladder).** $m_{\mathrm{hid}}(\Sigma_L)=L\ln2/\mathfrak h$ is linear in the cycle length at single contact — the first ladder structure of the fermion hunt.

**Phys.** The whole single-contact cycle family is one card: mass proportional to hidden edge count, interior winding even and parity-trivial, colour structurally absent at every rung of the ladder (one slot-carrying vertex can never seal inside), and the observable mask never exceeds ten dimensions. The floors differ not by which forces act — they all carry $G,H,W$ — but by their integer labels $(L,\Theta,k)$: the fermion hunt, at floor level, is integer bookkeeping.

---

---

### FT.35 — The composite floor $\Sigma_{12}$: first colour-active, first $D^-$-carrying

**Thm.** Let $\Sigma_{12}=\{p_1,q_1\}\cup\{p_2,q_2\}$ with materialized 2-cycles $c_1=(p_1{\to}q_1{\to}p_1)$, $c_2=(p_2{\to}q_2{\to}p_2)$ [FT.24: quanta $\kappa_1,\kappa_2$], joined by the bidirectional connector $e_{12}=(q_1,p_2)$, $\bar e_{12}=(p_2,q_1)$ [both $\in\mathcal R$], single observer contact at $p_1$ ($E_{\mathrm{bd}}=1$; FT.17 hypotheses, Def-H.35). Let $\Gamma=c_1\cup e_{12}\cup c_2\cup\bar e_{12}$ [valid closed chain, D1.4]. If $\Gamma$ materializes:
$$(1)\quad\kappa_{12}\in\mathbb Z\qquad[\mathrm{FT.34}(4):\ \Gamma\setminus\{e_{12},\bar e_{12}\}=c_1\sqcup c_2\ \text{decomposes into materialized closed chains}];$$
$$(2)\quad E_{\mathrm{int}}=6\ (c_1{:}\,2,\ c_2{:}\,2,\ \text{connector}{:}\,2),\quad I_{\mathrm{hid}}=6\ln2,\quad m_{\mathrm{hid}}=\frac{6\ln2}{\mathfrak h}\qquad[\mathrm{FT.17};\ \mathrm{CT4.3}\ \text{retention, as below}];$$
$$(3)\quad\Theta_{\mathrm{int}}(\Sigma_{12})=2\kappa_1+2\kappa_2+2\kappa_{12}=2\,k(\Gamma)\in2\mathbb Z\ [\mathrm{FT.34}(3)];\qquad\mathrm{Hol}_{\mathrm{int}}=+1\ [\mathrm{FT.25}];\qquad\Pi=72\,k(\Gamma)\,(\ln2)^2;$$
$$(4)\quad\text{rungs}:\ n(p_1)=3,\ n(q_2)=2,\ n(q_1)=n(p_2)=4:\quad O(4)=2^5-16=16>0\ [\mathrm{CT0.6}]:\ \text{the junction vertices are}\ D^-\text{-configured}\ [\mathrm{CT4.1}]:\ \text{excess locked, ledger-retained}\ [\mathrm{D4.2},\ \mathrm{CT4.3}];$$
$$(5)\quad\textbf{colour phases}:\ \mathrm{Colour}(\Sigma_{12})\subseteq\{p_1,q_1,p_2\}\ [\mathrm{D3.1};\ \mathrm{CT0.13}:\ \text{strong persists at}\ n\ge4];\quad\mathcal C(\Sigma_{12};C)=1\iff\text{all three seal inside as one}\ \varepsilon\text{-type (baryon-like) triple}\ [\mathrm{D3.9},\ \mathrm{CT3.17},\ \mathrm{FT.34}(5):\ 3\ \text{admits no}\ \{2,3\}\text{-partition with an external remainder}];$$
$$\text{strong-active phase}:\ \dim\mathcal K_{\Sigma_{12}}=9+1+8=18\ —\ \text{the maximal observable mask is attained}\ [\mathrm{FT.26}(3)];\qquad\text{any external/unsealed attachment}:\ \mathcal C=0\implies\text{block}\equiv0\ [\mathrm{FT.19}].$$

**Req.** FT.17 (Def-H.35), FT.19, FT.22–FT.28, FT.32, FT.34; D0.8, D1.4, D3.1, D3.9, D4.1, D4.2; CT0.6, CT0.11, CT0.13, CT0.14 (Part 1); CT3.11, CT3.17 (Part 2); CT4.1, CT4.3 (Part 2); Def-H.9, Def-H.10, Def-H.12, Def-H.15.

**Pf.**
$$
(1):\ \Gamma\setminus\{e_{12},\bar e_{12}\}=c_1\sqcup c_2:\ \text{edge-disjoint materialized closed chains}\implies\mathrm{FT.34}(4)\ \text{applies}:\ \kappa_{12}\in\mathbb Z
$$
$$
(2):\ \text{all six cycle/connector edges have both endpoints in}\ \Sigma_{12}\ [\mathrm{Def\text{-}H.12}];\quad E_{\mathrm{bd}}=1\le4\cdot1\ \checkmark;\quad q_1,p_2\ \text{oversubscribed}\ (n{=}4):\ \text{excess locked but retained and counted}\ [\mathrm{CT4.3},\ \mathrm{D4.2};\ \mathrm{FT.17}\ \text{cross-check 2 precedent}]\implies I_{\mathrm{hid}}=E_{\mathrm{int}}\ln2=6\ln2
$$
$$
(3):\ \Theta_{\mathrm{int}}=\Theta(c_1)+\Theta(c_2)+\kappa_{12}+\kappa_{\bar e_{12}}=2\kappa_1+2\kappa_2+2\kappa_{12}\ [\mathrm{FT.23},\ \mathrm{FT.24}];\quad\mathrm{FT.34}(3):\ =2k(\Gamma);\quad\mathrm{Hol}_{\mathrm{int}}=(-1)^{2\mathbb Z}=+1;\quad\Pi=E_{\mathrm{int}}^2\Theta_{\mathrm{int}}(\ln2)^2=36\cdot2k(\Gamma)(\ln2)^2
$$
$$
(4):\ n(q_1)=2\ (c_1)+2\ (\text{connector})=4;\quad n(p_2)=2+2=4;\quad n(p_1)=2+1=3;\quad n(q_2)=2\ [\mathrm{D0.8}];\qquad\mathrm{CT0.5}/\mathrm{CT0.6}:\ D_{\mathrm{tick}}(4)=2^5=32>16\implies O(4)=16;\quad\mathrm{CT4.1}:\ n\ge4\implies D^-\text{-configured};\quad\text{locked}=\text{retained}\ \neg\text{accessible}\ [\mathrm{D4.2}]
$$
$$
(5):\ \text{slots at}\ n\ge3:\ p_1\ (n{=}3),\ q_1,p_2\ (n{=}4:\ \text{rung-3 structure persists}\ [\mathrm{CT0.13}]);\quad q_2\ (n{=}2):\ \text{slot-less}
$$
$$
\mathcal C=1\iff\forall v\in\mathrm{Colour}:\ \pi_C(v)\subseteq\Sigma_{12}\ [\mathrm{Def\text{-}H.10}];\qquad\text{partition of}\ 3\ \text{into}\ \{2,3\}\text{-parts}:\ \text{only}\ 3=3\implies\varepsilon\text{-type triple}\ [\mathrm{FT.34}(5)];\quad\delta\text{-pair}+\text{remainder}:\ \text{remainder external}\implies\mathcal C=0\ [\mathrm{FT.19}]
$$
$$
\text{strong-active}:\ \dim=5{+}3{+}1{+}1{+}8=18\ [\mathrm{CT0.12},\ \mathrm{CT0.14},\ \mathrm{CT3.8}]=\mathrm{FT.26}(3)\text{'s bound}.\ \blacksquare
$$

**Rmk (composition creates saturation).** The first composite floor necessarily carries dark content: joining two floors by a bidirectional channel pushes both junction vertices to rung 4, where $D^-$ locks 16 registers' worth of excess [CT0.6, D4.1, D4.2] — retained in the ledger, inaccessible to any observer [D1.11, FT.3]. Composite fermion structure and saturation content are born together; $m_{\mathrm{hid}}$ counts the locked content as retained exactly as FT.17's cross-check 2 already established.

**Phys.** Two floor fermions wired into one object produce the program's first colour-active floor — sealed as a baryon-type triple, the smallest sealing the partition rule allows at three slots — its first dark junction content, its maximal eighteen-dimensional observable mask, and a composite winding that is the sum of the parts plus the integer distance between them. Meson-type pairs (two slots) and baryon-type triples (three slots) are not conventions: they are the only parts the sealing grammar has.

---

---

### FT.42 — The Platonic card template

**Thm.** Under Def-H.20's setup, with (M2) [hence $\kappa_e\in\mathbb Z$ on every channel, FT.24] and (M1) [hence $\Theta_f\in2\mathbb Z$ per face, FT.22]:
$$(1)\quad E_{\mathrm{int}}=2E,\qquad I_{\mathrm{hid}}=2E\ln2,\qquad m_{\mathrm{hid}}=\frac{2E\ln2}{\mathfrak h}\qquad[\text{observed: FT.17},\ \text{Def-H.35};\ \text{dark: Def-H.9(2) with}\ E_{\mathrm{vis}}=0];$$
$$(2)\quad\text{rungs (rung correction, FT.62)}:\ \text{dark}\ n(v)=2d\ \forall v;\ \ \text{observed (1 directed edge)}\ n(v_1)=2d+1;\ \ \text{bidirectional contact}\ 2d+2;\ \text{others}\ 2d\ [\mathrm{D0.8}:\ \text{directed real-edge count};\ \mathrm{CT0.5}:\ \phi_e\ \text{per incident real edge}];\qquad O(2d)=112\ (d{=}3),\ 496\ (d{=}4),\ 2032\ (d{=}5);\ \ O(2d{+}1)=240,1008,4080\ [\mathrm{CT0.6}];$$
$$\text{saturation universality (the "accessibility trichotomy" epithet does not stand, FT.62(3))}:\ \text{every vertex of every bidirectional floor}\ (d\ge2\ \text{channels}:\ n\ge4)\ \text{is}\ D^-\text{-configured}\ [\mathrm{CT4.1}],\ \text{content locked, retained, counted}\ [\mathrm{CT4.3},\ \mathrm{D4.2}];\ \text{grade by degree}:\ O(2d);\ \ \text{the lock-free family is the unidirectional one}\ [\mathrm{FT.28}(5),\ \mathrm{FT.32}(2);\ \mathrm{FT.62}(3)];$$
$$(3)\quad\Theta_{\mathrm{int}}=2K_S,\qquad K_S:=\!\!\sum_{\text{channels}}\!\!\kappa_{\mathrm{ch}}\in\mathbb Z\qquad[\mathrm{FT.23}:\ \kappa_{\bar e}=\kappa_e;\ \mathrm{D1.7}:\ \text{additivity}];\qquad\mathrm{Hol}_{\mathrm{int}}=+1\ [\mathrm{FT.25}(2)];\qquad W\ \text{row fires}\iff K_S\ne0;$$
$$(4)\quad\mathcal A(\Sigma_S;C)\supseteq\{G,H\}\ [G:\ I_{\mathrm{hid}}\ne0;\ H:\ \mathrm{Def-H.36}];\qquad\mathrm{EM}\in\mathcal A\iff\exists v:\ f_v\ne0\ [\mathrm{D3.3}];\qquad(\text{scope}\ [\mathrm{FT.62}(5)]:\ \text{type-}(d,d)\ \text{vertices leave D3.3's literal type-}(1,1)\ \text{domain empty on dark bidirectional floors};\ \text{the row evaluates on observed variants via chain-local pass-through reads}\ [\mathrm{FT.21}(i)]);$$
$$\text{strong}\in\mathcal A\iff\text{inside-sealed phase}\ (\mathcal C=1):\ \text{exists for every}\ S\ (V\ge4\ \text{partitions into 2s and 3s}\ [\mathrm{FT.34}(5)]),\ \text{in}\ g(V)\ \text{groupings}\ [\mathrm{FT.41}(b)];\qquad\dim\mathcal K_{\Sigma_S}=9\ (+1)\ (+8)\le18\ [\mathrm{FT.26}];$$
$$(5)\quad\textbf{the card table}:\ \Pi=E_{\mathrm{int}}^2\,\Theta_{\mathrm{int}}(\ln2)^2=8E^2K_S(\ln2)^2\.$$
$$
\begin{array}{c|c|c|c|c|c|c|c|c}
S & (V,E,F,d) & m_{\mathrm{hid}}\cdot\mathfrak h/\ln2 & O(2d)\ \text{dark}\ & O(2d{+}1)\ \text{contact} & \text{face}\ (L,\kappa_{\min},\Theta_{f,\min},k_{f,\min}) & \text{indep. windings} & g(V)\ \text{groupings} & \Pi/(\ln2)^2\\ \hline
\text{tetrahedron} & (4,6,4,3) & 12 & 112 & 240 & (3,2,6,3) & 3 & 3 & 288\,K_S\\
\text{cube} & (8,12,6,3) & 24 & 112 & 240 & (4,1,4,2) & 5 & 385 & 1152\,K_S\\
\text{octahedron} & (6,12,8,4) & 24 & 496 & 1008 & (3,2,6,3) & 7 & 25 & 1152\,K_S\\
\text{dodecahedron} & (20,30,12,3) & 60 & 112 & 240 & (5,2,10,5) & 11 & 292938721075 & 7200\,K_S\\
\text{icosahedron} & (12,30,20,5) & 60 & 2032 & 4080 & (3,2,6,3) & 19 & 164395 & 7200\,K_S
\end{array}
$$
$$(6)\quad\textbf{consistency anchors}:\ \text{tetrahedron observed with a bidirectional contact reproduces FT.17 cross-check 3 verbatim}\ (E_{\mathrm{int}}=12,\ E_{\mathrm{bd}}=2\le4\cdot1,\ I_{\mathrm{hid}}=12\ln2);\ \ \text{the tetrahedron face}\ \{A,B,C\}\ \text{observed by}\ D\ \text{is cross-check 2}\ (E_{\mathrm{int}}=6,\ E_{\mathrm{bd}}=6,\ \delta\tau\ge2);$$
$$\Sigma_{\min}=E{=}1\ \text{cell}\ [\mathrm{FT.28}];\qquad\Sigma_{12}=E{=}3\ \text{cell}\ [\mathrm{FT.35}].$$

**Req.** Def-H.20; FT.17 (Def-H.35), FT.22, FT.23, FT.24, FT.25, FT.26, FT.32(6), FT.34(5), FT.41(b); Def-H.1, Def-H.8, Def-H.9, Def-H.15; D0.8, D1.7, D3.1, D3.3; CT0.5, CT0.6, CT0.11, CT0.13, CT0.14 (Part 1); CT3.11 (Part 2); CT4.1, CT4.3, CT4.9 (Part 2); D4.2; solid cardinalities, Euler $V-E+F=2$ [math].

**Pf.**
$$
(1):\ \text{every channel bidirectional}\implies E_{\mathrm{int}}=2E\ [\mathrm{Def\text{-}H.12}:\ \text{both endpoints in}\ \Sigma_S];\qquad\text{observed}:\ E_{\mathrm{bd}}=1\le4\cdot1\ \checkmark\implies I_{\mathrm{hid}}=E_{\mathrm{int}}\ln2\ [\mathrm{FT.17}];\qquad(\text{re-scope}\ [\mathrm{FT.62}(4)]:\ \text{at corrected contact rung}\ 2d{+}1\ge7\ \text{the vertex is locked};\ \text{the}\ \mathrm{CT4.9}(1)\ \text{"visible}<3\text{" check passes to Def-H.35}+\mathrm{CT4.3}\ \text{retention};\ \text{value unchanged})
$$
$$
\text{dark}:\ \partial\Sigma_S=\varnothing\implies E_{\mathrm{vis}}=0\implies I_{\mathrm{hid}}=E_{\mathrm{tot}}=2E\ln2\ [\mathrm{Def\text{-}H.9}(2);\ \mathrm{FT.28}\ \text{dark-floor pattern}];\qquad m_{\mathrm{hid}}=I_{\mathrm{hid}}/\mathfrak h
$$
$$
(2)\ (\mathrm{FT.62}(1)):\ \mathrm{D0.8}\ \text{directed counts}:\ n=2d:\ D_{\mathrm{tick}}(2d)=2^{2d+1}:\ 128,512,2048\ (d=3,4,5);\quad\mathrm{CT0.6}:\ O(2d)=112,496,2032;\quad\text{contact}:\ O(2d{+}1)=240,1008,4080
$$
$$
\mathrm{CT4.1}:\ n\ge4\implies D^-\text{-configured};\quad\text{locked}=\text{retained}\ [\mathrm{D4.2},\ \mathrm{CT4.3};\ \mathrm{FT.17}\ \text{cross-check 2 precedent}]\implies E_{\mathrm{tot}}\ \text{accounting intact}
$$
$$
(3):\ \Theta_{\mathrm{int}}=\!\!\sum_{\text{directed edges}}\!\!\kappa_e=\!\!\sum_{\text{channels}}\!\!(\kappa_e+\kappa_{\bar e})=2\!\!\sum_{\text{channels}}\!\!\kappa_{\mathrm{ch}}\ [\mathrm{FT.23}];\qquad\mathrm{M2}+\mathrm{FT.24}:\ \kappa_{\mathrm{ch}}\in\mathbb Z\implies K_S\in\mathbb Z;\qquad\mathrm{Hol}_{\mathrm{int}}=(-1)^{2K_S}=+1\ [\mathrm{FT.25}(2)]
$$
$$
(4):\ \text{FT.20 rows as in FT.28}(3)/\mathrm{FT.32}(5);\qquad\text{slots at every vertex}\ (d\ge3\ \text{for all five solids}\ [\mathrm{D3.1},\ \mathrm{CT3.11}(1)];\ n\ge4:\ \text{rung-3 structure persists}\ [\mathrm{CT0.13}])
$$
$$
V\ge4\implies\{2,3\}\text{-partition exists}\ [\mathrm{FT.34}(5)];\qquad g(V)\ [\mathrm{FT.41}(b)];\qquad\dim\ [\mathrm{FT.26}(3),\ \mathrm{CT0.14}]
$$
$$
(5):\ \text{face regimes from FT.32}(6)\ \text{uniform-}\kappa\ \text{minimality}\ (L\ \text{odd}:\ \kappa_{\min}=2,\ \Theta_{f,\min}=2L,\ k_{f,\min}=L;\ \ L\ \text{even}:\ 1,\ L,\ L/2);\qquad\Pi=(2E)^2\cdot2K_S(\ln2)^2=8E^2K_S(\ln2)^2
$$
$$
(6):\ \text{FT.17 cross-check 3}:\ \text{whole bidirectional}\ K_4,\ E_{\mathrm{int}}=\binom42\times2=12=2E\ (E{=}6)\ \checkmark;\quad\text{cross-check 2}:\ \text{face}\ \{A,B,C\}:\ E_{\mathrm{int}}=6=2\cdot3\ \checkmark,\ E_{\mathrm{bd}}=6\le4\cdot2\ \checkmark
$$
$$
\mathrm{FT.28}:\ E{=}1\implies E_{\mathrm{int}}=2\ \checkmark;\qquad\mathrm{FT.35}:\ E{=}3\implies E_{\mathrm{int}}=6\ \checkmark.\ \blacksquare
$$

**Rmk (what the card does not say).** $g(V)$ counts grouping *patterns*; attachment types (triplet/antitriplet per vertex [D3.8]) and the $\kappa$-profile are configuration data on top. The dodecahedron's sealing count ($292938721075$) and the icosahedron's ($164395$) are grammar sizes, not state counts. Materialization (M1/M2) is hypothesized, not derived — which faces and which 2-cycles are on-spectrum is the corpus's to decide [D2.4, CT2.5].

**Phys.** Every Platonic solid is a fermion floor with the same five-line card: mass $=2E$ hidden bits over $\mathfrak h$, trivial total parity with an integer winding ledger $K_S$, gravity and Higgs always active, electromagnetism state-dependent, colour available in as many sealing patterns as the vertex count's $\{2,3\}$-grammar allows — and a lock profile fixed by the degree — every bidirectional vertex saturated (rung correction, FT.62: dark rungs are $2d$), graded $O(2d)\in\{112,496,2032\}$, excess absorbed and retained by $D^-$. The solids differ where the integers differ: edges, faces, vertices, degree.

---

---

### FT.43 — The winding ledger and Euler consistency

**Thm.** Under FT.42's hypotheses:
$$(1)\quad\textbf{sum rule}:\ \ \sum_{f}\Theta_f=2\!\!\sum_{\text{channels}}\!\!\kappa_{\mathrm{ch}}=\Theta_{\mathrm{int}}\quad\Longleftrightarrow\quad\sum_f k_f=K_S\qquad[\text{each channel lies in exactly two faces}:\ FL=2E;\ \mathrm{D1.7}];$$
$$(2)\quad\textbf{independent face reads}:\ F-1=E-V+1=\beta_1(\Gamma_S)\qquad[\text{one sum rule};\ \text{Euler}\ V-E+F=2;\ \text{math}:\ \text{cycle rank of a connected graph}];$$
$$(3)\quad\textbf{parity lattice}:\ \text{the on-shell}\ \kappa\text{-profiles}\ \{\kappa\in\mathbb Z^E:\ \Theta_f\in2\mathbb Z\ \forall f\}\ \text{form the kernel of the face-incidence map}\ \varphi:\mathbb Z^E\to\mathbb Z_2^F,\ \text{of index}\ 2^{F-1}\ \ [\text{math}:\ \operatorname{rk}_{\mathbb Z_2}\varphi=F-1\ \text{for spherical embeddings};\ \text{machine}:\ \text{explicit GF(2) elimination, tetrahedron and cube}];$$
$$(4)\quad\text{sector counts}:\ 2^{F-1}=2^{\beta_1}:\ \ \text{tetrahedron}\ 8,\ \text{cube}\ 32,\ \text{octahedron}\ 128,\ \text{dodecahedron}\ 2048,\ \text{icosahedron}\ 2^{19}=524288;$$
$$(5)\quad\textbf{Euler as card consistency}:\ \beta_1=E-V+1=F-1\ \text{ties the three ledgers}:\ \text{mass}\ (E\ \text{via FT.42}(1)),\ \text{colour}\ (V\ \text{via}\ g(V)),\ \text{winding}\ (F{-}1\ \text{reads})\ —\ \text{the sphere's Euler number is an identity among card entries, not an extra assumption}.$$

**Req.** FT.22, FT.23, FT.24, FT.42; Def-H.20; D1.7; FT.25(2); Euler's formula, cycle-rank and GF(2)-rank facts for connected planar graphs [math]; solid face incidences [math].

**Pf.**
$$
(1):\ \text{each channel}\ \{e,\bar e\}\ \text{lies in exactly two faces}\ [\text{solid geometry};\ FL=2E\ \text{double-count}]:\quad\sum_f\Theta_f=\sum_f\sum_{e\in f}\kappa_e=\sum_{\text{channels}}2\kappa_{\mathrm{ch}}=\Theta_{\mathrm{int}}\ [\mathrm{D1.7}\ \text{additivity};\ \mathrm{FT.42}(3)]
$$
$$
\Theta_f=2k_f\ [\mathrm{M1}+\mathrm{FT.22}],\ \Theta_{\mathrm{int}}=2K_S\ [\mathrm{FT.42}(3)]\implies\sum_fk_f=K_S
$$
$$
(2):\ \text{one linear relation among}\ F\ \text{reads}\implies F-1\ \text{independent};\qquad\text{Euler}:\ V-E+F=2\implies F-1=E-V+1=\beta_1\ \ [\text{math}]
$$
$$
(3):\ \varphi(\kappa)_f:=\sum_{e\in f}\kappa_e\ \mathrm{mod}\ 2:\ \ \text{on-shell locus}=\ker\varphi\ [\mathrm{M1}+\mathrm{FT.22}];\qquad\operatorname{rk}_{\mathbb Z_2}\varphi=F-1\ [\text{math}:\ \text{faces generate the cycle space with the single spherical relation}]\implies[\mathbb Z^E:\ker\varphi]=2^{F-1}
$$
$$
(4):\ 2^{F-1}\ \text{evaluated at}\ F=4,6,8,12,20;\qquad(5):\ \text{substitution of}\ (2)\ \text{into FT.42}(1)/(4).\ \blacksquare
$$

**Rmk (what the lattice index means).** Materialization prunes the integer $\kappa$-lattice by exactly the solid's $\mathbb Z_2$ cycle space: an off-lattice profile (some face with odd $\Theta_f$) is a profile no face-materialized configuration can carry [FT.22]. The pruned cosets are not physical sectors — they are the excluded parity classes; the physical ledger is $\ker\varphi$ with its $F-1$ integer face reads.

**Phys.** A Platonic fermion's geometric memory is the solid's combinatorics turned into integers: one winding read per face, one relation among them, and the number of independent reads is the skeleton's first Betti number — the same number Euler's formula builds from vertices and edges. Mass counts edges, colour counts vertices, winding counts faces, and $V-E+F=2$ is the statement that the three ledgers are not independent. The solids with more independent cycles remember more windings: tetrahedron 3, cube 5, octahedron 7, dodecahedron 11, icosahedron 19.

---

---

### FT.44 — Duality signature and the floor taxonomy

**Thm.** $(1)$ **Duality mass-degeneracy.** Dual solids exchange $(V,F)$ at fixed $E$ [math]: cube$\leftrightarrow$octahedron $(8,12,6)\leftrightarrow(6,12,8)$, dodecahedron$\leftrightarrow$icosahedron $(20,30,12)\leftrightarrow(12,30,20)$, tetrahedron self-dual $(4,6,4)$. Since $m_{\mathrm{hid}}=2E\ln2/\mathfrak h$ [FT.42(1)] and $\Pi=8E^2K_S(\ln2)^2$ [FT.42(5)] depend on $E$ only: **dual pairs are mass-degenerate and $\Pi$-degenerate at matched $K_S$** — cube/octahedron: $24\ln2/\mathfrak h$; dodecahedron/icosahedron: $60\ln2/\mathfrak h$; three mass values across the five solids.
$(2)$ **Ledger splitting.** The degeneracy is split by every finer ledger: independent windings $F-1$ (cube 5 vs octahedron 7; dodecahedron 11 vs icosahedron 19); lattice index $2^{F-1}$ ($32$ vs $128$; $2048$ vs $2^{19}$); sealing grammar $g(V)$ ($385$ vs $25$; $292938721075$ vs $164395$); lock profile $O(2d)$ (correction, FT.62(3): cube $112$ vs octahedron $496$; dodecahedron $112$ vs icosahedron $2032$ — saturation grade splits both dual pairs).
$(3)$ **Self-dual floor.** The tetrahedron is the unique self-paired cell ($V=F=4$): its winding and colour ledgers coincide in cardinality ($F-1=3$ independent reads; $g(4)=3$ groupings) — the smallest floor on which the full card, including a $\delta$-pair sealing grammar and a nontrivial winding ledger, is simultaneously active.
$(4)$ **Taxonomy (all computed floors).** Every fermion floor computed in this document obeys $m_{\mathrm{hid}}=E_{\mathrm{int}}\ln2/\mathfrak h$ with $E_{\mathrm{int}}=2E_{\mathrm{bidir}}+E_{\mathrm{uni}}$: $\Sigma_{\min}$: $E_{\mathrm{int}}=2$ [FT.28]; cycle ladder $\Sigma_L$: $E_{\mathrm{int}}=L$ (unidirectional) [FT.32]; $\Sigma_{12}$: $E_{\mathrm{int}}=6$ [FT.35]; Platonic family: $E_{\mathrm{int}}=2E$ [FT.42]. The informational mass is the directed-edge count, universally, across every computed cell.

**Req.** FT.42, FT.43; FT.28, FT.32, FT.35; FT.41(b); duality cardinals, Euler [math]; Def-H.20.

**Pf.**
$$
(1):\ \text{duality exchanges}\ V\leftrightarrow F,\ \text{fixes}\ E\ [\text{math};\ \text{cardinals above}];\qquad m_{\mathrm{hid}},\ \Pi\ \text{are}\ E\text{-functions}\ [\mathrm{FT.42}(1),(5)]\implies\text{degenerate on dual pairs}
$$
$$
(2):\ F\text{-dependence}:\ \mathrm{FT.43}(2),(4);\qquad V\text{-dependence}:\ g(V)\ [\mathrm{FT.41}(b)];\qquad d\text{-dependence}:\ O(d)\ [\mathrm{FT.42}(2)]:\ \text{cube}\ d{=}3\ (O{=}0\ \text{dark})\ \text{vs octahedron}\ d{=}4\ (O{=}16)
$$
$$
(3):\ V=F=4:\ F-1=3=g(4)\ [\mathrm{FT.41}(b):\ g(4)=3];\qquad\text{both ledgers active}:\ \text{winding}\ [\mathrm{FT.43}(2)],\ \delta\text{-pair sealing}\ (4=2{+}2)\ [\mathrm{FT.34}(5)]
$$
$$
(4):\ \text{direct count per cell}:\ \mathrm{FT.28}(1)\text{--}(2),\ \mathrm{FT.32}(1),\ \mathrm{FT.35}(2),\ \mathrm{FT.42}(1).\ \blacksquare
$$

**Rmk (candidate reading, recorded not claimed).** Dual mass-degeneracy split by finer integer ledgers is a derived degeneracy-splitting *template* for families sharing a mass-like read, distinguished by winding/colour/lock data (an application-layer reading). No physical identification — of duals with generations, or of any card entry with a named particle — is made or implied here.

**Phys.** Duality, in the floor ledger, is exact mass-degeneracy with everything else distinct: the cube and octahedron weigh the same and remember differently — five winding reads against seven, three-hundred-eighty-five sealing patterns against twenty-five, one hundred twelve locked registers per vertex against four hundred ninety-six (rung correction, FT.62(3)). The tetrahedron, self-dual, is the smallest floor whose card exercises every ledger at once. And across the whole computed taxonomy — digon, cycles, composite pair, all five solids — one law has never broken: the informational mass is the count of directed internal edges, in bits over $\mathfrak h$.

---

---

### FT.45 — The bidirectional polygon floors $P_n$: cards, minima, and the null-carrying sector

**Thm.** Let $\Sigma_{P_n}$ ($n\ge3$) be the fully bidirectional 1-skeleton of the regular $n$-gon [Def-H.20's setup class], $n\ge3$: $n$ vertices, $n$ bidirectional channels, $2n$ directed edges; sphere compactification with two length-$n$ faces (interior, exterior): $FL=2n=2E$, $V-E+F=n-n+2=2\ \checkmark$ [math]. (The digon-walk floor $\Sigma_{\min}$ [FT.28] is the taxonomy's $E{=}1$ cell, $\neg$a polygon member — clause (5).) Under **(M2$_n$)** all $n$ channels materialize as 2-cycles [FT.24: $\kappa_i\in\mathbb Z$] and **(M1$_n$)** the interior face materializes [FT.22: $\Theta_f\in2\mathbb Z$]:
$$(1)\quad E_{\mathrm{int}}=2n,\qquad I_{\mathrm{hid}}=2n\ln2,\qquad m_{\mathrm{hid}}=\frac{2n\ln2}{\mathfrak h},\qquad\Pi=8n^2K_P(\ln2)^2,\qquad K_P:=\Theta_{\mathrm{int}}/2=\textstyle\sum_{i=1}^n\kappa_i\ [\mathrm{FT.42}\ \text{template}];$$
$$(2)\quad\text{rungs (rung correction, FT.62)}: \text{dark}\ n(v)=4\ \forall v\ (2\ \text{channels each},\ \mathrm{D0.8}\ \text{directed count};\ \text{type}\ (2,2));\ \ \text{single-contact observed}\ n(v_1)=5,\ \text{others}\ 4;\qquad O(4)=16=C_{\mathrm{cap}},\ O(5)=48\ [\mathrm{CT0.5},\ \mathrm{CT0.6}]:\ \textbf{uniform minimal saturation at every vertex of every member}\ [\mathrm{CT4.1}];\ \text{locked content retained and counted}\ [\mathrm{CT4.3},\ \mathrm{D4.2}];\ \text{the lock-free family is the unidirectional one}\ [\mathrm{FT.32}(2),\ \mathrm{FT.62}(3)];$$
$$(3)\quad\textbf{walk space and the single parity constraint}:\ \beta_1(\text{directed multigraph})=2n-n+1=n+1\ [\text{math}];\qquad\text{closed-walk structure}:\ \text{flow balance at every vertex}\implies\text{per-channel net flow constant}=w\ (\text{the walk's winding});$$
$$\Theta(w)=w\,\textstyle\sum_i\kappa_i+2\sum_i\kappa_i b_i\ \ (b_i:\ \text{reverse traversals})\implies\Theta(w)\in2\mathbb Z\ \forall w\iff\textstyle\sum_i\kappa_i\in2\mathbb Z\ \ (w{=}1:\ \text{the face},\ \mathrm{M1}_n):$$
$$\textbf{exactly one independent parity constraint};\qquad\text{on-shell}\ \kappa\text{-lattice}=\{\kappa\in\mathbb Z^n:\ \textstyle\sum\kappa_i\in2\mathbb Z\}:\ \text{index}\ 2=2^{F-1}\ [\mathrm{FT.43}(3)\ \text{pattern at}\ F{=}2];\qquad\text{digons}\ (w{=}0):\ \Theta=2\sum\kappa_ib_i\in2\mathbb Z\ \text{automatic}\ [\mathrm{M2}_n,\ \mathrm{FT.24}];$$
$$(4)\quad\textbf{four minimality regimes}\ (\Theta_{\min}>0,\ \text{face materialized};\ \text{machine-enumerated for}\ n\le7):$$
$$\text{spacelike-or-null}\ [\kappa\ge0]:\ \Theta_{\min}=2\ \forall n\ge3\ (\text{profile}\ (1,1,0,\dots,0));\qquad\textbf{null-carrying dimension}=|\{i:\kappa_i=0\}|\ge n-2\ \text{in every such minimizer};$$
$$\text{strictly-spacelike}\ [\kappa\ge1]:\ \Theta_{\min}=n+(n\ \mathrm{mod}\ 2)\ (n\ \text{even}:\ \text{unique all-1 profile};\ n\ \text{odd}:\ \text{one}\ 2,\ \text{rest}\ 1);\qquad\text{uniform}\ [\kappa_i\equiv\kappa]:\ \Theta_{\min}=n\ (n\ \text{even},\ \kappa{=}1)\ /\ 2n\ (n\ \text{odd},\ \kappa{=}2)\ [\mathrm{FT.32}(6)];$$
$$\text{signature-mixed}\ [\kappa\in\mathbb Z,\ \text{timelike}\ \kappa<0\ \text{admissible}\ [\mathrm{CT1.12}]]:\ \Theta_{\min}=2\ \forall n\ge3\ (\text{witnesses}:\ n\ge4\ \text{even}:\ (1^{(n+2)/2},(-1)^{(n-2)/2});\ n\ge5\ \text{odd}:\ (1^{n-1},-(n-3));\ n{=}3:\ (2,1,-1));$$
$$(5)\quad\textbf{the digon distinction}:\ \text{the null-carrying sector has dimension}\ n-2:\ \text{at}\ n=2\ (\Sigma_{\min})\ \text{it is}\ \{-1\}\text{-dimensional}=\text{empty}:\ \Theta_{\min}=2\ \text{there forces}\ \kappa_1=\kappa_2=1\ \text{(all-nonnull, purely spacelike)}\ [\mathrm{FT.24}(4)];\ \text{for every}\ n\ge3\ \text{the minimum is null-carrying}.\ \textbf{The fermion floor is derived to be a digon, not a polygon};$$
$$(6)\quad\textbf{sealing}:\ \text{dark}\ P_n:\ \mathrm{Colour}=\varnothing\ (n(v)=2<3\ [\mathrm{D3.1}])\implies\text{strong}\ \neg\in\mathcal A\ \text{always}\ [\mathrm{FT.20}];\ \ \text{observed}:\ \mathrm{Colour}=\{v_1\}:\ \neg\exists\ \text{inside partner}\ [\mathrm{A1}]\implies\text{structurally colourless}\ [\mathrm{FT.27}\ \text{case split}];\quad\mathcal A\supseteq\{G,H\},\ W\iff K_P\ne0,\ \mathrm{EM}\iff\exists v:\ f_v\ne0;\quad\dim\mathcal K\le10<18;$$
$$(7)\quad\textbf{anchors}:\ \Sigma_{\min}\ (\text{digon walk},\ E{=}1)\ \text{is adjacent to but}\ \neg\text{a member of this family}\ [\mathrm{FT.28}/\mathrm{FT.44}(4)\ \text{taxonomy}]:\ \text{clauses}\ (3)\text{--}(5)\ \text{degenerate there}\ (\neg\exists\ \text{proper face};\ \text{its minimum forces}\ \kappa{=}1\ [\mathrm{FT.24}(4)]);\quad\text{the unidirectional}\ 3\text{-cycle}\ =\ \mathrm{FT.17}\ \text{cross-check 1}\ [\mathrm{FT.32}];\quad\text{the observed tetrahedron face is NOT}\ P_3\text{: in bidirectional}\ K_4\ \text{the face vertices carry the third (external) channel each}\ (n(v)=4,\ E_{\mathrm{bd}}=6)\ [\mathrm{FT.17}\ \text{cross-check 2}].$$

**Req.** FT.17 (Def-H.35), FT.20, FT.22, FT.23, FT.24, FT.25, FT.26, FT.27, FT.28, FT.32(6), FT.42; Def-H.20; A1; D0.8, D1.7, D3.1, D3.3; CT0.5, CT0.6, CT0.14 (Part 1); CT1.12 (**C**, signature classes); CT4.9 (Part 2); cycle-rank and partition facts [math].

**Pf.**
$$
(1),(2):\ \mathrm{FT.42}(1)\text{--}(2)\ \text{template at}\ E=n,\ V=n,\ d_{\text{dark}}=2,\ d_{\text{contact}}=3;\qquad\mathrm{CT0.6}:\ O(2)=O(3)=0;\qquad\mathrm{CT4.9}(1):\ \text{visible}\ 1\ \text{bit}<3\ \checkmark
$$
$$
(3):\ \beta_1=2n-n+1=n+1\ [\text{math}:\ \text{connected multigraph}];\qquad\text{closed walk}:\ \text{in-degree}=\text{out-degree at every vertex}\implies a_i-b_i=\text{const}=w\ [\text{flow balance around the cycle};\ a_i,b_i:\ \text{forward/reverse traversals of channel}\ i]
$$
$$
\Theta(w)=\sum_i\kappa_i(a_i+b_i)=\sum_i\kappa_i(2b_i+w)=w\sum_i\kappa_i+2\sum_i\kappa_ib_i\ [\mathrm{D1.7}\ \text{additivity};\ \mathrm{FT.23}:\ \kappa_{\bar e}=\kappa_e]\implies\text{parity}(\Theta(w))=\text{parity}\bigl(w\textstyle\sum_i\kappa_i\bigr)
$$
$$
\text{face walk}:\ w=1:\ \text{constraint}\ \textstyle\sum\kappa_i\in2\mathbb Z\ [\mathrm{M1}_n+\mathrm{FT.22}];\quad\text{digons}:\ w=0:\ \text{automatic};\quad w\ge2:\ \text{automatic once the face is constrained}\implies\textbf{exactly one independent parity constraint};\quad\text{index}\ 2\ [\text{math}]
$$
$$
(4):\ \text{spacelike-or-null}:\ (1,1,0^{n-2}):\ \Theta=2\in2\mathbb Z\ \checkmark;\quad\Theta>0\ \text{even}\Rightarrow\Theta\ge2:\ \text{minimal};\qquad\Theta=2\ \text{with}\ \kappa\ge0\implies\le2\ \text{positive units}\implies\ge n{-}2\ \text{zeros}
$$
$$
\text{strictly-spacelike}:\ \min\{\textstyle\sum\kappa_i:\ \kappa_i\ge1,\ \sum\in2\mathbb Z\}=n+(n\ \mathrm{mod}\ 2);\qquad\text{uniform}:\ n\kappa\in2\mathbb Z\Rightarrow\kappa_{\min}=1\ (n\ \text{even}),\ 2\ (n\ \text{odd})\ [\mathrm{FT.32}(6)]
$$
$$
\text{signature-mixed witnesses}:\ n\ge4\ \text{even}:\ \tfrac{n+2}{2}\ \text{entries}\ {+}1,\ \tfrac{n-2}{2}\ \text{entries}\ {-}1:\ \Theta=2\ \checkmark;\quad n\ge5\ \text{odd}:\ (1^{n-1},-(n-3)):\ \Theta=(n-1)-(n-3)=2\ \checkmark;\quad n=3:\ (2,1,-1):\ \Theta=2\ \checkmark
$$
$$
(5):\ n=2:\ \Theta=2\kappa\ [\mathrm{FT.23}];\quad\Theta=2\Rightarrow\kappa=1:\ \neg\exists\ \text{null slot};\qquad n\ge3:\ (1,1,0^{n-2})\ \text{admissible}\ [\mathrm{CT1.19a}:\ \kappa=0\iff\text{null edge permitted}]
$$
$$
(6):\ \text{dark}:\ n(v)=2\implies\neg\exists\ \text{colour slots}\ [\mathrm{D3.1}:\ \text{slots}=colour\ \text{at}\ n{=}3;\ \mathrm{CT0.13}:\ \text{strong strictly new at}\ n{=}3]\implies\mathrm{Colour}=\varnothing;\qquad\text{observed}:\ \mathrm{Colour}\subseteq\{v_1\}:\ \mathrm{FT.27}\ \text{case split}
$$
$$
(7):\ \text{direct comparison of}\ (1)\text{--}(6)\ \text{against FT.28}\ (n{=}2),\ \mathrm{FT.17}\ \text{cross-checks 1--2}.\ \blacksquare
$$

**Rmk (regime precedence; withdrawn draft claim).** The four regimes are nested constraint classes, not alternatives: strictly-spacelike $\subseteq$ spacelike-or-null; signature-mixed relaxes both. Physically primary for a *spatial* polygon floor are the two spacelike regimes; the mixed regime is kinematically admissible [CT1.12: $\operatorname{sig}=(-,+,+,+)$ permits $\kappa<0$] but describes floors with timelike interior edges — a different physical situation, recorded for completeness. An earlier draft's "$n\equiv2\ (\mathrm{mod}\ 4)$ anomaly" is **withdrawn as an arithmetic error** (its witness summed to $8$, not $6$): no residue-class anomaly exists — the strictly-spacelike floor is $n+(n\ \mathrm{mod}\ 2)$ for every $n$, with the unique all-1 profile at even $n$.

**Rmk (accessibility contrast, corrected [FT.62(3)]).** $P_n$ dark has $n(v)=4$ everywhere [D0.8 directed count]: exactly one channel quantum over budget — $O(4)=16=C_{\mathrm{cap}}$, uniform in $n$: the polygon family is the *uniform minimal-saturation* family (the "unlimited-accessibility" epithet does not stand). The Platonic family saturates graded by degree, $O(2d)\ge112$; the lock-free cells are the unidirectional floors ($n\le3$) [FT.28(5), FT.32(2)]. First structural difference between the two polygon-derived families — uniform vs graded saturation — derived from D0.8/CT0.5/CT0.6 alone.

**Phys.** Bidirectional polygons are the fermion program's cleanest infinite family: one uniform minimal lock per vertex ($O(4)=16$, correction), no colour ever, exactly one parity constraint from the face (an index-2 on-shell lattice), and a null-carrying minimal sector of dimension $n-2$ — one that has no analogue at the digon, whose minimum forces $\kappa=1$: the fermion floor's ledger is qualitatively polygon-external.

---

---

### FT.49 — The tetrahedron-face floor: full card

**Thm.** Let $\Sigma_{\triangle}=\{A,B,C\}$ be the bidirectional 3-face of the bidirectional $K_4$ [FT.17 cross-check 2's setup], observed by the fourth vertex $D$ (six boundary edges). Under M2 (face-channel digons materialize [FT.24]) and M1 (both directed face triangles materialize [FT.22]):
$$(1)\quad E_{\mathrm{int}}=6,\quad E_{\mathrm{bd}}=6\le4\,\delta\tau\Rightarrow\delta\tau\ge2\ [\mathrm{FT.17}\ \text{hypotheses},\ \text{Def-H.35}];\qquad I_{\mathrm{hid}}=6\ln2,\qquad m_{\mathrm{hid}}=\frac{6\ln2}{\mathfrak h}\ \ [\text{the multi-tick observation cell of the taxonomy}];$$
$$(2)\quad\text{interior channel structure}=\Sigma_{P_3}'s\ [\mathrm{FT.45}\ \text{at}\ n{=}3]:\ \kappa\text{-lattice}\ \{\kappa\in\mathbb Z^3:\ \kappa_{AB}{+}\kappa_{BC}{+}\kappa_{CA}\in2\mathbb Z\}\ \text{of index}\ 2;\ \ \text{both directed triangles give the same constraint}\ [\mathrm{FT.23}:\ \text{orientation-even}];$$
$$(3)\quad\Theta_{\mathrm{int}}=2\,\Theta_{\triangle}=4\,k_{\triangle}\in4\mathbb Z,\qquad k_{\triangle}:=\Theta_{\triangle}/2\in\mathbb Z\ [\mathrm{FT.22}];\qquad\mathrm{Hol}_{\mathrm{int}}=+1\ [\mathrm{FT.25}(2)];\qquad W\ \text{row fires}\iff\Theta_{\triangle}\ne0;$$
$$(4)\quad\text{minimality regimes}\ [\mathrm{FT.45}(4)\ \text{at}\ n{=}3]:\quad\Theta_{\triangle,\min}=2\ (\text{null-carrying}\ (1,1,0)\text{-class}),\ 4\ (\text{strictly-spacelike}\ (1,1,2)\text{-class}),\ 6\ (\text{uniform}\ \kappa{=}2);\qquad\Pi=36\,\Theta_{\mathrm{int}}(\ln2)^2\in\{144,288,432\}(\ln2)^2;$$
$$(5)\quad\text{rungs and locks}:\ n(A)=n(B)=n(C)=6\ [\mathrm{D0.8}:\ 3\ \text{channels each in the}\ K_4];\qquad O(6)=2^7-16=112\ [\mathrm{CT0.5},\ \mathrm{CT0.6}]:\ \text{every vertex}\ D^-\text{-configured}\ [\mathrm{CT4.1}],\ \text{locked content retained and counted}\ [\mathrm{CT4.3},\ \mathrm{D4.2}];$$
$$(6)\quad\textbf{baryon-type sealing phase}:\ \text{all three vertices slot-carrying}\ (n\ge3\ [\mathrm{D3.1},\ \mathrm{CT0.13}:\ \text{rung-3 structure persists}]);\quad\mathcal C(\Sigma_{\triangle};C)=1\iff\text{the three attachments seal as one}\ \varepsilon\text{-type triple}\ [3=3\ \text{is the only}\ \{2,3\}\text{-partition}:\ \mathrm{FT.34}(5),\ g(3)=1\ \mathrm{FT.41}(b)]:\ \text{the first computed cell whose strong phase is exactly D3.9's baryon structure}\ B=\varepsilon_{ijk}q^iq^jq^k\ (\text{structural correspondence,}\ \neg\text{particle identification});$$
$$(7)\quad\mathcal A(\Sigma_{\triangle};C)\supseteq\{G,H\}\ [G:\ I_{\mathrm{hid}}\ne0;\ H:\ \mathrm{Def-H.36}];\quad\mathrm{EM}\iff\exists v:\ f_v\ne0;\quad\text{strong}\iff\varepsilon\text{-sealed};\qquad\dim\mathcal K=9\ (+1)\ (+8)\le18\ [\mathrm{FT.26}];$$
$$(8)\quad\text{boundary algebra}:\ N(\Sigma_{\triangle})=6\implies\mathcal H_{\mathrm{slot}}=\mathbb C^6,\ \iota_\Sigma:\ \mathfrak u(6)\ \text{of dimension}\ 36;\qquad\text{strictly new at}\ \Sigma:\ 36-6=30\ \text{real dimensions}\ [\mathrm{FT.41}(d)]\ —\ \text{the largest exchange sector computed}.$$

**Req.** FT.17 (Def-H.35), FT.22, FT.23, FT.24, FT.25, FT.26, FT.34(5), FT.41(b),(d), FT.45; Def-H.9, Def-H.10, Def-H.12, Def-H.15; D0.8, D3.1, D3.3, D3.9; CT0.5, CT0.6, CT0.13, CT0.14 (Part 1); CT3.11, CT3.17 (Part 2); CT4.1, CT4.3 (Part 2); D4.2.

**Pf.**
$$
(1):\ \mathrm{FT.17}\ \text{cross-check 2 verbatim}:\ E_{\mathrm{int}}=6,\ E_{\mathrm{bd}}=6,\ \delta\tau\ge2;\qquad I_{\mathrm{hid}}=E_{\mathrm{int}}\ln2=6\ln2\ [\mathrm{FT.17},\ \text{Def-H.35}];\quad m_{\mathrm{hid}}=I_{\mathrm{hid}}/\mathfrak h\ [\mathrm{Def\text{-}H.9}(2)]
$$
$$
(2):\ \text{interior channels}=\{AB,BC,CA\}\ \text{bidirectional}=\Sigma_{P_3}\ \text{interior}\ [\mathrm{FT.45}\ \text{setup}];\quad\text{digons}:\ \kappa\in\mathbb Z\ [\mathrm{M2}+\mathrm{FT.24}];\quad\text{triangles}:\ \Theta_{\triangle}=\kappa_{AB}{+}\kappa_{BC}{+}\kappa_{CA}\ [\mathrm{FT.23}:\ \text{same both directions}]\in2\mathbb Z\ [\mathrm{M1}+\mathrm{FT.22}]
$$
$$
(3):\ \Theta_{\mathrm{int}}=\!\!\sum_{\text{6 directed}}\!\!\kappa=2\Theta_{\triangle};\qquad\Theta_{\triangle}=2k_{\triangle}\ [\mathrm{FT.22}]\implies\Theta_{\mathrm{int}}=4k_{\triangle};\qquad\mathrm{Hol}_{\mathrm{int}}=(-1)^{4k_{\triangle}}=+1\ [\mathrm{FT.25}(2)]
$$
$$
(4):\ \mathrm{FT.45}(4)\ \text{regimes at}\ n{=}3;\qquad\Pi=E_{\mathrm{int}}^2\Theta_{\mathrm{int}}(\ln2)^2=36\cdot(2\Theta_{\triangle})(\ln2)^2:\ \Theta_{\triangle}\in\{2,4,6\}\Rightarrow\{144,288,432\}(\ln2)^2
$$
$$
(5):\ \mathrm{D0.8}:\ n=3\ \text{channels}\times2=6;\quad\mathrm{CT0.5}/\mathrm{CT0.6}:\ D_{\mathrm{tick}}(6)=2^7=128,\ O(6)=112;\quad\mathrm{CT4.1}:\ n\ge4\Rightarrow D^-\text{-configured};\quad\text{retained}\ [\mathrm{CT4.3}]
$$
$$
(6):\ n\ge3\Rightarrow\text{slots}\ [\mathrm{D3.1},\ \mathrm{CT3.11}(1)];\quad\text{partitions of}\ 3\ \text{into}\ \{2,3\}\text{-parts}:\ \text{only}\ 3\ [\mathrm{FT.34}(5)];\quad g(3)=1\ [\mathrm{FT.41}(b)];\quad\varepsilon\text{-triple}=B\ \text{structure}\ [\mathrm{D3.9},\ \mathrm{CT3.17}]
$$
$$
(7):\ \mathrm{FT.20}\ \text{rows};\quad(8):\ N(\Sigma)=E_{\mathrm{bd}}=6\ [\mathrm{Def\text{-}H.12}];\quad\dim\mathfrak u(6)=36;\quad\text{factored diagonal}=6\implies\text{strictly new}=30\ [\mathrm{FT.41}(d)].\ \blacksquare
$$

**Rmk (relation to the polygon and Platonic cells).** $\Sigma_{\triangle}$ is neither $\Sigma_{P_3}$ nor a Platonic floor: its interior ledger is the polygon's (index-2 lattice, $n{-}2{=}1$ null freedom at the minimum), while its rung/lock ledger is the ambient $K_4$'s ($n{=}6$, $O{=}112$) — the first computed cell where interior and ambient ledgers visibly decouple. Its sealing phase is the baryon type; $\Sigma_{12}$'s was also $\varepsilon$-type [FT.35(5)] but at three slots from two floors plus a junction — the grammar [FT.34(5)] is the same, the wiring differs.

**Phys.** The tetrahedron face is the program's densest small cell: six hidden bits, a winding ledger even in both directions ($\Theta_{\mathrm{int}}\in4\mathbb Z$), every vertex deep in the saturation regime with 112 registers' absorption rate each, one baryon-type colour phase, and thirty dimensions of strictly-new boundary exchange structure — all of it derived from cards already in the ledger, assembled without a single new premise beyond the declared materialization hypotheses.

---

---

### FT.50 — Composition and gluing laws

**Thm.** $(1)$ **Bridged union.** Let $\Sigma^{(1)},\Sigma^{(2)}$ be floors with bidirectional interiors [$E_{\mathrm{int}}^{(i)}=2E_i$], joined by a bidirectional connector path $P=(f_1,\dots,f_m)$ (disjoint from both interiors), single external contact; all digons materializing [M2-type]. Then
$$E_{\mathrm{int}}(\Sigma)=2E_1+2E_2+2m,\qquad m_{\mathrm{hid}}(\Sigma)=m_{\mathrm{hid}}^{(1)}+m_{\mathrm{hid}}^{(2)}+\frac{2m\ln2}{\mathfrak h}\qquad[\mathrm{FT.17},\ \text{Def-H.35}]:\ \textbf{informational mass is additive under bridged composition}.$$
$(2)$ **Generalized round-trip.** If $\Gamma=c_1\cdot P\cdot c_2\cdot\bar P$ materializes [$c_i$ materialized closed chains at the attachments; D1.4 concatenation]: $d_{12}:=\Theta(P)\in\mathbb Z$ and $k(\Gamma)=k_1+k_2+d_{12}$ [FT.34(2)–(3) generalized to $m$-channel connectors]; per-edge integrality $\kappa_{f_j}\in\mathbb Z$ requires each connector digon to materialize [FT.24] — the sum $d_{12}$ is integral without that strengthening.
$(3)$ **Junction saturation.** A bidirectional bridge into a vertex of interior degree $d\ge2$ gives $n_{\mathrm{junction}}=d+2\ge4\implies O(d{+}2)=2^{d+3}-16>0$: **composition creates darkness at every junction** [CT0.5, CT0.6, CT4.1, D4.2; FT.35's Rmk generalized]; content retained [CT4.3]. For $s$ triangular floors sharing one junction vertex: $2s$ channels meet there, $n=4s$ [D0.8], $O(4s)=2^{4s+1}-16$ — absorption rate grows exponentially in the sharing multiplicity [D4.2: rate $\propto O(n)$]: high-multiplicity junctions are maximally dark.
$(4)$ **Gluing law.** For $\Sigma=\Sigma_1\cup_G\Sigma_2$ glued along a shared subgraph $G$: $E_{\mathrm{int}}=E_{\mathrm{int}}^{(1)}+E_{\mathrm{int}}^{(2)}-|E_{\mathrm{dir}}(G)|$; the on-shell parity lattice is $\{\kappa:\ \Theta_c\in2\mathbb Z\ \forall\ \text{materialized closed chains}\ c\}$ — its index is $2^{\operatorname{rk}_{\mathbb Z_2}(\text{materialized cycle system})}$, dependencies automatic: a cycle homologous to a sum of materialized cycles inherits evenness [D1.7 additivity; FT.23 orientation-blindness].
$(5)$ **Computed cells.** **Bowtie** (two bidirectional triangles sharing one vertex $X$): $E_{\mathrm{int}}=12$, $m_{\mathrm{hid}}=12\ln2/\mathfrak h$; both faces materialized $\Rightarrow\Theta_{\mathrm{int}}=2(K_1{+}K_2)\in4\mathbb Z$; constraint rank 2 (index 4); rungs: $n(X)=8$ [$O(8)=496$], other four vertices $n=4$ [$O(4)=16$] — every vertex locked; five slots $\Rightarrow g(5)=10$ sealing groupings (one $\delta$-pair $+$ one $\varepsilon$-triple) [FT.41(b)]. **Double-triangle patch** (two tetrahedron faces glued along channel $AB$; $\Sigma=\{A,B,C,D\}$): $E_{\mathrm{int}}=10$; constraints $\Theta_{ABC},\Theta_{ABD}\in2\mathbb Z$: $\operatorname{rk}_{\mathbb Z_2}=2$ (index 4), and the boundary 4-cycle constraint is *derived*: $\Theta_{ACBD}=\Theta_{ABC}+\Theta_{ABD}-2\kappa_{AB}\in2\mathbb Z$; rungs $n(A)=n(B)=6$ [$O=112$], $n(C)=n(D)=4$ [$O=16$]; four slots $\Rightarrow g(4)=3$ groupings, all $\delta{+}\delta$ (meson–meson phases — the only $\{2,3\}$-partition of 4).

**Req.** FT.17 (Def-H.35), FT.22, FT.23, FT.24, FT.27, FT.34, FT.35, FT.41(b), FT.45; Def-H.9, Def-H.10, Def-H.12; D0.8, D1.4, D1.7, D3.1, D3.9; CT0.5, CT0.6 (Part 1); CT3.17 (Part 2); CT4.1, CT4.3 (Part 2); D4.2; $\mathbb Z_2$-rank facts [math].

**Pf.**
$$
(1):\ E_{\mathrm{int}}:\ \text{interiors disjoint}\ \sqcup\ 2m\ \text{connector directed edges};\quad E_{\mathrm{bd}}=1\le4\delta\tau\ \checkmark;\quad I_{\mathrm{hid}}=E_{\mathrm{int}}\ln2\ [\mathrm{FT.17}]\implies m_{\mathrm{hid}}=\tfrac{E_{\mathrm{int}}\ln2}{\mathfrak h}=\text{sum of parts}
$$
$$
(2):\ \mathrm{FT.34}(1):\ \Theta(P)+\Theta(\bar P)=\Theta(\Gamma)-\Theta(c_1)-\Theta(c_2)\in2\mathbb Z;\quad\Theta(\bar P)=\Theta(P)\ [\mathrm{FT.23}\ \text{per edge}]\implies\Theta(P)=d_{12}\in\mathbb Z;\quad k(\Gamma)=\tfrac{\Theta(\Gamma)}{2}=k_1+k_2+d_{12}
$$
$$
\text{per-edge}:\ \text{each}\ f_j\ \text{needs its own round-trip or digon materialization}\ [\mathrm{FT.34}(4)/\mathrm{FT.24}]:\ \text{sum integrality does not imply edge integrality}\ [\text{scope stated}]
$$
$$
(3):\ n_{\mathrm{junction}}=d+2\ [\mathrm{D0.8}:\ \text{bridge adds 1 in}+1\ \text{out}];\quad d\ge2\implies n\ge4:\ O(n)=2^{n+1}-16>0\ [\mathrm{CT0.6}];\quad\mathrm{CT4.1}:\ D^-\text{-configured};\qquad s\ \text{triangles at one junction}:\ 2s\ \text{channels}\implies n=4s,\ O(4s)=2^{4s+1}-16\ [\mathrm{D0.8},\ \mathrm{CT0.6}];\quad\text{rate}\ \propto O(n)\ [\mathrm{D4.2}]
$$
$$
(4):\ E_{\mathrm{int}}:\ \text{inclusion–exclusion on directed edges};\qquad\text{constraints}:\ \text{each materialized}\ c:\ \Theta_c=\sum_{e\in c}\kappa_{\mathrm{ch}(e)}\ (\mathrm{mod}\ 2)=0\ [\mathrm{FT.22}/\mathrm{FT.23}];\quad\text{rank over}\ \mathbb Z_2\ \text{of the system}=\text{independent constraint count};\ \text{index}=2^{\operatorname{rk}}
$$
$$
\text{dependency witness}:\ \Theta_{ACBD}=\Theta_{ABC}+\Theta_{ABD}-2\kappa_{AB}\ [\mathrm{D1.7}\ \text{additivity on shared channel}]\implies\text{boundary-cycle constraint derived}
$$
$$
(5):\ \text{bowtie}:\ E_{\mathrm{int}}=2\cdot6=12;\ n(X)=8\ [\text{4 channels}];\ O(8)=2^9-16=496;\quad\text{constraints}:\ \Theta_{XAB},\Theta_{XCD}\in2\mathbb Z:\ \text{disjoint channel sets}\implies\operatorname{rk}=2;\quad g(5)=10\ [\mathrm{FT.41}(b)]
$$
$$
\text{patch}:\ E_{\mathrm{int}}=2\cdot5=10;\quad\text{constraint vectors on}\ (AB,AC,BC,AD,BD):\ (1,1,1,0,0),\ (1,0,0,1,1):\ \text{independent over}\ \mathbb Z_2\implies\operatorname{rk}=2,\ \text{index}\ 4;\quad n(A)=n(B)=6,\ n(C)=n(D)=4;\quad g(4)=3\ [\text{all}\ 2{+}2].\ \blacksquare
$$

**Phys.** Floors compose like ledger objects should: masses add across bridges, winding numbers add across round-trips, and every junction pays for the composition in darkness — the absorption rate doubling with each shared channel, exponentially with multiplicity. Gluing identifies shared channels and adds parity constraints by rank, with homological dependencies automatic. The bowtie and the patch are the first wired cells: one a five-vertex all-locked object with ten sealing patterns, the other a four-vertex meson–meson floor whose boundary-cycle constraint the ledger already implies.

---

---

### FT.51 — Enumeration of the winding ledger

**Thm.** For the polygon floor $\Sigma_{P_n}$ under M1/M2 [FT.45], at winding level $k$ (face constraint $\sum_i\kappa_i=2k$ [FT.45(3)]):
$$(1)\quad\#\{\text{on-shell profiles},\ \kappa\in\mathbb Z_{\ge0}^n,\ \textstyle\sum\kappa_i=2k\}=\binom{2k+n-1}{n-1}\qquad[\text{stars-and-bars};\ \text{math}];$$
$$(2)\quad\#\{\text{strictly-spacelike profiles},\ \kappa\ge1\}=\binom{2k-1}{n-1}\quad(2k\ge n;\ =0\ \text{otherwise});$$
$$(3)\quad\textbf{coarse-grained degeneracy}:\ \text{configurations related by mask-preserving relabeling are identified [CT2.6's}\ \sim\ \text{; CT2.7: weights are vertex-name independent], so the distinct ledger states at level}\ k\ \text{are the dihedral necklaces}$$
$$M(n,k)=\frac{1}{2n}\Bigl(\sum_{j=0}^{n-1}\mathrm{fix}(r^j)+\sum_{\text{reflections}}\mathrm{fix}\Bigr)\qquad[\text{Burnside};\ \text{math}],$$
with $\mathrm{fix}(r^j)=\binom{2k\,c/n+c-1}{c-1}$ if $(n/c)\mid 2k$, else $0$, where $c=\gcd(n,j)$ [rotation fixed points: $\kappa$ constant on the $c$ orbits]; machine values: $M(3,1)=2,\ M(3,2)=4,\ M(3,3)=7;\quad M(4,1)=3,\ M(4,2)=8$;
$$(4)\quad\textbf{growth}: \#\text{profiles}\sim(2k)^{n-1}/(n-1)!\ \text{as}\ k\to\infty\ [\text{math}]:\ \text{the winding ledger's state count grows polynomially in the winding at fixed}\ n,\ \text{degree}\ n{-}1\ —\ \text{a derived density of states for the floor family};$$
$$(5)\quad\text{sign registers factor}: \sigma\text{-assignments are independent of}\ \kappa\ [\mathrm{CT0.10}]:\ \text{total floor states at level}\ k=2^{2n}\cdot M(n,k)\cdot(\text{sealing/attachment data})\ —\ \text{the three registers multiply, none converts into another}.$$

**Req.** FT.45; CT2.6, CT2.7 (Part 2); CT0.9, CT0.10 (Part 1); stars-and-bars, Burnside, asymptotics of binomials [math].

**Pf.**
$$
(1),(2):\ \text{compositions of}\ 2k\ \text{into}\ n\ \text{non-negative (resp. positive) parts}\ [\text{math}];\qquad\text{parity automatic: the constraint fixes}\ \textstyle\sum\kappa=2k\ \text{even}\ [\mathrm{FT.45}(3)]
$$
$$
(3):\ \text{relabeling quotient}:\ \mathrm{CT2.6}'\text{s}\ \sim\ \text{on coarse-grained ledger entries};\ \mathrm{CT2.7}\ \text{Pf}:\ \text{weights}\ \neg\text{vertex-name dependent}\implies D_n\text{-orbits are the distinct states};\qquad\text{Burnside with rotation/reflection fixed-point counts}\ [\text{math};\ \text{machine cross-check by orbit enumeration}]
$$
$$
(4):\ \binom{2k+n-1}{n-1}=\frac{(2k+n-1)\cdots(2k+1)}{(n-1)!}\sim\frac{(2k)^{n-1}}{(n-1)!}
$$
$$
(5):\ \mathrm{CT0.10}:\ P(C)\ \text{and}\ \pi(C)\ \text{independent sign structures};\ \ \mathrm{CT0.9}:\ 2^{2n}\ \text{sign assignments on}\ 2n\ \text{directed edges};\qquad\kappa\text{-ledger}\ [\text{clauses}(1)\text{--}(3)]\ \text{and sealing data}\ [\mathrm{FT.41}(b)]\ \text{factor as independent registers}.\ \blacksquare
$$

**Phys.** The winding ledger is countable in closed form: at winding $k$ a polygon floor carries $\binom{2k+n-1}{n-1}$ integer profiles, collapsing to dihedral necklaces under the corpus's own relabeling equivalence — two, four, seven distinct states for the triangle at $k=1,2,3$. The count grows like $(2k)^{n-1}$: bigger polygons remember more, higher windings remember denser — a derived density of states, with signs and sealings multiplying as independent registers. This is the combinatorial substrate any generation/flavour reading  would have to select from.

---

---

### FT.63 — The Platonic physical cards: spin, charge, parity, holonomy, entropy, mass ratios, binding

**Thm.** For each Platonic floor $\Sigma_S$ [Def-H.20] under M1/M2 (interface clause), FT.62's corrected rungs, and — for the spin and defect-ladder rows — Def-H.38/Def-H.37(2) (interface clause): all seven requested computations close, per solid and universally. Write $(V,E,F,L,d)$ for the cardinals, $\kappa_{0,\min}=1$ (cube) / $2$ (all others) [FT.42(5)], $K_{S,\min}=E\kappa_{0,\min}$, $\delta_v=2\pi-d\,\frac{(L-2)\pi}{L}$ the vertex angle defect, and $k_{f,\min}=L$ ($L$ odd) / $L/2$ ($L$ even) the uniform-minimal face winding.
$(1)$ **Spin** [Def-H.38; Def-H.23, FT.60]: every materialized face chain carries winding $k_f$ with carrier $\mathrm{Sym}^{k_f}$ and label $j_f=|k_f|/2$; every channel digon carries $k=\kappa_{\mathrm{ch}}$, $j=\kappa_{\mathrm{ch}}/2$ [FT.24(1), FT.25(3)]. At the uniform minima:
$$
\begin{array}{c|c|c|c|c|c}
S & k_{f,\min} & j_f & K_{S,\min} & j_{\max}=K_S/2 & \dim:\ \text{face basis}\ /\ \text{digon basis}\\ \hline
\text{tetrahedron} & 3 & \tfrac32 & 12 & 6 & 4^4=256\ /\ 3^6=729\\
\text{cube} & 2 & 1 & 12 & 6 & 3^6=729\ /\ 2^{12}=4096\\
\text{octahedron} & 3 & \tfrac32 & 24 & 12 & 4^8=65536\ /\ 3^{12}=531441\\
\text{dodecahedron} & 5 & \tfrac52 & 60 & 30 & 6^{12}=2176782336\ /\ 3^{30}\\
\text{icosahedron} & 3 & \tfrac32 & 60 & 30 & 4^{20}=2^{40}\ /\ 3^{30}
\end{array}
$$
with the digon-basis check $\sum_{\mathrm{ch}}\kappa_{0,\min}/2=K_{S,\min}/2=j_{\max}$ [machine]. **Derived laws**: (a) $j_{\max}=K_S/2$ and the total winding sum $\sum_fk_f=K_S$ are decomposition-invariant [FT.43(1), FT.60(7a)]; the full tensor carrier is basis-relative (digon basis is the edge-disjoint one [FT.25(1)]). (b) $V,F$ even for all five solids $\Rightarrow$ at uniform minima every face $j_f$ composes to an **integer** stretched total ($F$ half-integer-or-integer summands, $F$ even) — Platonic floors are integer-spin objects in the stretched read at their minima, with half-integer face reads for the four odd-$L$ solids: fermion-like faces, boson-like stretched totals (structural observation, $\neg$particle identification). (c) Dual splitting, new column: $j_{\max}$ splits cube ($6$) from octahedron ($12$) but is *degenerate* for dodecahedron/icosahedron ($30$) — where the per-face structure splits instead ($5/2\times12$ vs $3/2\times20$) and the face-basis carrier dimensions split ($6^{12}$ vs $4^{20}$) while the digon-basis dimensions are degenerate ($3^{30}$ both).
$(2)$ **Charge** [FT.40, EM.9, D3.4]: the closed-core read $q_{\mathrm{core}}(c;v)=\tfrac12(\sigma_{e_1}-\sigma_{e_k})\in\{-1,0,+1\}$ is defined on every materialized closed core — faces, digons, and homology sums: $\beta_1=F-1$ independent core reads per solid $(3,5,7,11,19)$, ternary alphabet, all three values attained per solid [machine: explicit $\sigma$-assignments on the encoded skeletons]; $\omega$-rebase flips the sign [D2.6, FT.40]. Channel-facing charge: dark floors — no read channel [FT.3; FT.62(5)]; observed variants — EM.9 end-reads of transit chains through the contact, telescoping to boundary signs [FT.21(i)]; EM activity criterion $\exists v:\ f_v\ne0$ on chain-local reads [FT.42(4), FT.62(5) scope]. No independent weak or strong charge exists [FT.11, FT.12, CT3.22].
$(3)$ **Parity**: the on-shell $\kappa$-lattice is $\ker\varphi_S$, $\varphi_S:\mathbb Z^E\to\mathbb Z_2^F$ the face-incidence map — index $2^{F-1}=(8,32,128,2048,2^{19})$ [FT.43(3); machine: GF(2) elimination for **all five**, extending the earlier tetra/cube]; equivalently $\kappa\bmod2$ ranges over the **cut space** of $\Gamma_S$ (dimension $V-1=E-F+1$ — Euler again) [math: planar duality of the face-even lattice; machine: dimension identity + star-cut witnesses]. Consequences [machine]: $A_S(1)=0$ for all five (no bridges: single-channel $\kappa{=}1$ leaves two faces odd); $A_S(3)=V$ for $d{=}3$ solids (the vertex stars), $0$ for octahedron/icosahedron-at-$K{=}3$ (odd $K$ needs an odd cut; $|\delta S|\equiv d|S|\bmod2$); **octahedron: every face $2$-coloring balances $\sum_{\mathrm{black}}k_f=\sum_{\mathrm{white}}k_f=K_S/2$, hence $K_S\in2\mathbb Z$ and $A_{\mathrm{octa}}(\text{odd}\,K)=0$** [machine; the unique Platonic with even $d$]. On materialized loops: $\Theta\in2\mathbb Z$, $\mathrm{Hol}_{\mathrm{int}}=+1$ [FT.22, FT.25(1), FT.42(3)]; partial internal sets retain free parity [FT.25(3)]; on-shell weight phases are registration-only, $(-1)^{\aleph+n_-}$ [FT.61(1)–(2)].
$(4)$ **Holonomy**: $\mathrm{Hol}_{\mathrm{spiral}}=+1$ on every materialized loop [FT.22]; $\mathrm{Hol}_{\mathrm{int}}=+1$ [FT.25(2)]. Frame/spin-connection side [Def-H.21, FT.54]: the skeleton metric is piecewise-flat with conical defects $\delta_v$ at vertices — exact table $\delta_v/\pi=(1,\tfrac12,\tfrac23,\tfrac15,\tfrac13)$, and **Descartes/Gauss–Bonnet closes the ledger**: $V\delta_v=4\pi$ for all five [machine in exact $\pi$-units]. Hence the global spinor transport around any full sweep is $\exp(i\,\tfrac{4\pi}{2}\,\hat n\cdot\vec\sigma)=+\mathbb I$ — $4\pi$ is the SU(2) period [machine over $\mathbb Q(i)$]: spherical materialization is spinor-single-valued, a consistency anchor for M1. Loops cleanly enclosing one vertex (transverse to the singular locus — vertex-figure loops in the derived geometry) carry $\Theta_R=\delta_v$ [FT.47(1)/GB; Def-H.21(6)] and defect values $D_S=2-2\cos(\delta_v/2)=4\sin^2(\delta_v/4)$ — exact radicals, clause (6). 1-skeleton face loops sit *on* the singular locus (vertices on the loop): the smooth-enclosure defect read does not apply to them without a corner convention, undeclared — recorded, not guessed [Rmk below]. Under Def-H.38 the defect read becomes the multiplet ladder $m^2_{\mathrm{pole}}(m)=4\hat\mu'^2\sin^2(m\,\Theta_R/4)$, $m\in\{k,k{-}2,\dots,-k\}$ [FT.60(5)] — per-solid weight tables in (6). Weak-transport side: kernel coherence — charge-aligned profiles give $G(c)=0$, defect-massless, at every floor [FT.33(6), EW.22, EM.6].
$(5)$ **Entropy**: $S_{\mathrm{hid}}=I_{\mathrm{hid}}=2E\ln2=(12,24,24,60,60)\ln2$ nats [FT.42(1); FT.62(4): unchanged]; loop relating rate $S_{\mathrm{reg}}/A_{\mathrm{loop}}=(\ln2/\mathfrak h^2)/\bar\kappa$ [FT.37]: at the uniform minima $\bar\kappa=\kappa_{0,\min}$ — **the cube is the unique Platonic floor whose uniform-minimal loops saturate the CT1.29 Bekenstein rate $\ln2/\mathfrak h^2$ exactly**; the other four run at half rate ($\kappa_0=2$). Diagnostic minima $\Pi_{\min}=8E^2K_{S,\min}(\ln2)^2=(3456,13824,27648,432000,432000)(\ln2)^2$ — dual-degenerate at matched $K_S$ [FT.42(5), FT.44(1)]. Lock ledgers (corrected): $\sum_vO$ per variant from FT.62(2)'s table — the retained-but-inaccessible register rate, e.g. dark icosahedron $24384$/tick vs dark tetrahedron $448$/tick. Boundary entropy: dark floors $\partial\Sigma_S=\varnothing$; observed $E_{\mathrm{bd}}\in\{1,2\}$ [FT.42; CT1.29 applies to locked-interior separating surfaces — the Platonic lock ledger is vertex-absorption, not surface area; no identification].
$(6)$ **Mass ratios** [Def-H.37(2); FT.54(4)]: $m_{\mathrm{hid}}=2E\ln2/\mathfrak h$; the vertex-defect pole datum and the dimensionless ratio:
$$
\frac{m^2_{\mathrm{pole}}(\delta_v)}{m_{\mathrm{hid}}^2}=\frac{4\hat\mu'^2\,\mathfrak h^2\sin^2(\delta_v/4)}{4E^2(\ln2)^2}=\frac{\hat\mu'^2\mathfrak h^2}{(\ln2)^2}\cdot\frac{D_S}{4E^2}\in\mathfrak q^0\qquad[[\hat\mu'^2]=\mathfrak q,\ [\mathfrak h^2]=\mathfrak q^{-1}:\ \mathrm{D2.9}],
$$
$$
\begin{array}{c|c|c|c|c}
S & D_S=4\sin^2(\delta_v/4) & \text{exact field} & \text{min. polynomial of}\ D_S & D_S/4E^2\\ \hline
\text{tetrahedron} & 2 & \mathbb Q & x-2 & 1/72\\
\text{cube} & 2-\sqrt2 & \mathbb Q(\sqrt2) & x^2-4x+2 & (2-\sqrt2)/576\\
\text{octahedron} & 1 & \mathbb Q & x-1 & 1/576\\
\text{dodecahedron} & 2-2\cos\tfrac\pi{10} & \mathbb Q(\cos\tfrac\pi{10}) & x^4-8x^3+19x^2-12x+1 & D_S/3600\\
\text{icosahedron} & 2-\sqrt3 & \mathbb Q(\sqrt3) & x^2-4x+1 & (2-\sqrt3)/3600
\end{array}
$$
[machine: the dodecahedron quartic verified by exact substitution $x=2-2c$ into $\mathbb Z[c]/(16c^4-20c^2+5)$ — itself verified from $\cos5t=16c^5-20c^3+5c$ by de Moivre binomials at $t=\pi/10$; the cube/icosahedron quadratics from $(x-2)^2\in\{2,3\}$]. Weight-ladder values $D_S(m)=2-2\cos(m\,\delta_v/2)$, $m\le4$ [FT.60(5); machine]: tetrahedron $(2,4,2,0)$ — rational, with an exact zero at $m{=}4$; cube $(2{-}\sqrt2,2,2{+}\sqrt2,4)$; octahedron $(1,3,4,3)$ — rational; icosahedron $(2{-}\sqrt3,1,2,3)$; dodecahedron $D(2)=\tfrac{3-\sqrt5}2$, $D(4)=\tfrac{5-\sqrt5}2$ [machine in $\mathbb Q(\sqrt5)$ via $4c^2\mp2c-1$ at $c=\cos\tfrac\pi5,\cos\tfrac{2\pi}5$], $D(1),D(3)$ the two **smallest** of its four positive roots. **[precision correction [FT.76(10)]: the quartic $x^4-8x^3+19x^2-12x+1$ has four positive roots — $0.097886967410$, $0.824429495415$, $3.175570504585$, $3.902113032590$ (machine-isolated to width $2^{-60}$; $q(0..4)=(1,1,5,1,1)>0$, so no integer bracket separates them) — realized by the weights $m\in\{1,19\},\{3,17\},\{7,13\},\{9,11\}$ respectively; $D(1),D(3)$ are the two smallest.]** Def-H.37(1) form at stationarity: ratio $=\hat\mu^2\mathfrak h^4G(c)\,\kappa_{0,\min}/(\ln2)^2$ [FT.53(3)] with $\kappa_{0,\min}\in\{2,1,2,2,2\}$. **Derived law (dual splitting, pole side)**: both dual pairs share $m_{\mathrm{hid}}$ and $\Pi$ [FT.44(1)] but split on every defect datum — $\delta_v$: $\tfrac\pi2$ vs $\tfrac23\pi$; $\tfrac\pi5$ vs $\tfrac\pi3$; $D_S$: $2-\sqrt2$ vs $1$; $2-2\cos\tfrac\pi{10}$ vs $2-\sqrt3$ — FT.44(2)'s splitting template gains its first *irrational* column. Face loops carry $\Theta_R=0$ on the flat-face side (defect-massless), corner convention undeclared [Rmk].
$(7)$ **Binding-force contributions**: per-aspect ledger, all five solids:
$$
\begin{array}{c|c|c|c}
\text{aspect} & \text{criterion on}\ \Sigma_S & \dim\mathcal K^{(A)} & \text{binding read}\\ \hline
G & \text{always}\ (I_{\mathrm{hid}}=2E\ln2\ne0) & 5 & \kappa\text{-profile modulo loop constraint}\ [\mathrm{FT.41}(c)]\\
H & \text{always}\ (\mathrm{Def-H.36}\ \text{fold}) & 1 & m_{\mathrm{hid}}\ \text{read}\ [\mathrm{FT.20}]\\
W & \iff K_S\ne0\ (\text{at minima: always}) & 3 & \text{spin content of}\ (1)\ [\mathrm{FT.42}(3),\ \mathrm{Def-H.38}]\\
\mathrm{EM} & \text{observed/charged states}\ [\mathrm{FT.62}(5)] & 1 & q_{\mathrm{core}}\ \text{ternary per core}\ [(2)]\\
\text{strong} & \iff\ \text{inside-sealed phase}\ (\mathcal C=1) & 8 & g(V)\ \text{groupings; singlet-diagonal reads vanish}\ [\mathrm{FT.39}(2)]
\end{array}
$$
$\dim\mathcal K_{\Sigma_S}=9\ (+1)\ (+8)\le18$ [FT.26(3), FT.42(4)]. Sealing grammar: $g(V)=(3,385,25,292938721075,164395)$ [FT.41(b); machine: closed form vs enumeration for $V\le8$], with the **even-$\varepsilon$ theorem**: $V$ even for all five solids $\Rightarrow$ every grouping has an even number $b$ of $\varepsilon$-triples ($2a+3b=V$, $b$ even) [machine] — Platonic sealing phases are baryon-number-even by structure; the tetrahedron is meson-only ($b=0$: three $\delta\delta$-pairings), the octahedron admits $2\varepsilon$ phases ($15\,\delta^3+10\,\varepsilon^2$), the icosahedron $b\in\{0,2,4\}$, the dodecahedron $b\in\{0,2,4,6\}$, the cube $b\in\{0,2,4\}$ [machine: term breakdown]. Confinement is all-or-nothing [FT.19] with generic nonvanishing at $\mathcal C=1$ [FT.39(1)]; no per-edge strong phase exists [FT.29(2)]; strong binding contributes *admissibility structure and gluon modes*, never singlet expectation values [FT.39(2), CT3.13]. Boundary/exchange algebra: dark $N(\Sigma_S)=0$ (no boundary algebra); single-directed-edge contact $N=1$: nothing strictly new [FT.41(d)]; bidirectional contact $N=2$ corolla at $n(w)=2$: exchange doublet $W$-hosted literally [FT.58(1)]; the face-floor variant $N=6$, $n(D)=6$: exchange sector wholly kernel/$D^-$-absorbed [FT.59(4a)]. $D^-$: never observable, absorption-only [FT.20, CT4.4] — its binding contribution is the lock ledger of FT.62(2), by rate not by force.

**Req.** Def-H.20, Def-H.23; Def-H.38, Def-H.37(2), Def-H.36, Def-H.35; M1/M2 (interface clause); FT.9, FT.11, FT.12, FT.19, FT.20, FT.21, FT.22, FT.24, FT.25, FT.26, FT.29, FT.31, FT.33, FT.37, FT.39, FT.40, FT.41, FT.42, FT.43, FT.44, FT.47, FT.49, FT.53, FT.54, FT.58, FT.59, FT.60, FT.61, FT.62; A4; D2.6, D2.9, D3.3, D3.4; CT0.6, CT0.7, CT0.9, CT0.10, CT0.12, CT0.13, CT0.14 (Part 1); CT1.29, CT2.5, CT2.9 (Part 2); CT3.13, CT3.17, CT3.22 (Part 2); CT4.3, CT4.4, CT4.9 (Part 2); EW.22, EW.32 (Part 2); EM.2, EM.6, EM.9 (Part 2); Descartes/Gauss–Bonnet, planar cut-space duality, $\cos(5t)$ de Moivre identity, SU(2) $4\pi$-periodicity [math].

**Pf.**
$$
(1):\ \text{faces materialize}\ [\mathrm{M1}]:\ \text{each face}=\text{materialized closed chain}\implies\Psi=\mathrm{Sym}^{k_f}\ [\mathrm{Def\text{-}H.23}];\quad\text{digons}\ [\mathrm{M2}]:\ k=\kappa\ [\mathrm{FT.24}(1),\mathrm{FT.25}(3)]
$$
$$
\text{uniform minima}:\ k_{f,\min}=\Theta_{f,\min}/2:\ L\ \text{odd}:\ \tfrac{2L}2=L;\ L\ \text{even}:\ \tfrac L2\ [\mathrm{FT.42}(5)];\qquad K_{S,\min}=E\kappa_{0,\min}\ [\mathrm{FT.42}(3)];\quad j_{\max}=K_S/2\ [\mathrm{FT.60}(2),(7a)]
$$
$$
\dim\mathrm{Sym}^k=k+1:\ \text{table arithmetic}\ [\text{machine}];\qquad(b):\ F\in\{4,6,8,12,20\}\ \text{even};\ j_f\in\tfrac12\mathbb Z:\ \text{stretched total}=\textstyle\sum_fk_{f,\min}/2=K_{S,\min}/2\in\mathbb Z\ [\text{machine}:\ 6,6,12,30,30]
$$
$$
(c):\ E\ \text{invariance}\ [\mathrm{FT.44}(1)];\quad j_{\max}:\ 6\ne12\ (\text{cube/octa});\quad30=30\ (\text{dodeca/icosa}):\ k_{f,\min}\times F:\ 5\times12\ne3\times20\ \text{as multisets};\ 6^{12}\ne4^{20};\ 3^{30}=3^{30}
$$
$$
(2):\ \mathrm{FT.40}\ \text{verbatim per core};\qquad\beta_1=F-1\ \text{independent reads}\ [\mathrm{FT.43}(2)];\qquad\text{attainment witnesses}\ [\text{machine}];\qquad\omega\text{-flip}\ [\mathrm{D2.6}]
$$
$$
(3):\ \mathrm{FT.43}(3)+\text{machine elimination (all five)};\qquad\ker\varphi_S\ \text{mod}\ 2:\ \dim_{\mathbb Z_2}=E-(F-1)=V-1\ [\text{Euler}]=\dim\text{cut space}\ [\text{math}];\ \text{stars}=\delta\{v\}:\ \text{admissible}\ [\text{machine}]
$$
$$
A_S(1)=0:\ \text{single channel}\ \kappa{=}1:\ \text{its two faces odd};\ \neg\exists\ \text{bridges}\ [\text{solid 2-connectivity};\ \text{machine}];\qquad A_S(3)=V\ (d{=}3):\ \text{stars};\ \text{odd}\ K\iff\text{odd cut}:\ |\delta S|\equiv d|S|\ (2)\ \text{via}\ \textstyle\sum_{v\in S}\deg v=|\delta S|+2|E(S)|
$$
$$
\text{octahedron}:\ \text{dual bipartite}\iff d\ \text{even}\ [\text{machine}: 2\text{-coloring exists iff octahedron}];\quad\text{each channel in one black} + \text{one white face}\implies\textstyle\sum_{\mathrm{bl}}\Theta_f=\sum_{\mathrm{wh}}\Theta_f=\sum_e\kappa_e
$$
$$
\implies\textstyle\sum_{\mathrm{bl}}k_f=\sum_{\mathrm{wh}}k_f=K_S/2\in\mathbb Z;\qquad\text{on-shell phases}:\ \mathrm{FT.61}(1)\text{--}(2)
$$
$$
(4):\ \delta_v=2\pi-d\alpha,\ \alpha=\tfrac{(L-2)\pi}L\ [\text{regular}\ L\text{-gon angle};\ \text{math}]:\ \delta_v/\pi=2-\tfrac{d(L-2)}L=(1,\tfrac12,\tfrac23,\tfrac15,\tfrac13);\qquad V\delta_v=4\pi\ [\text{machine}:\ \text{Descartes}]
$$
$$
\exp(i\tfrac{4\pi}2\hat n\cdot\vec\sigma)=\cos(2\pi)+i\sin(2\pi)\hat n\cdot\vec\sigma=\mathbb I\ [\text{machine over}\ \mathbb Q(i)];\qquad\Theta_R=\delta_v\ \text{for clean enclosure}\ [\mathrm{FT.47}(1)/\mathrm{GB};\ \mathrm{Def\text{-}H.21}(6)]
$$
$$
(5):\ \mathrm{FT.42}(1)+\mathrm{FT.62}(4);\qquad\bar\kappa=\kappa_{0,\min}\ [\text{uniform}]:\ \text{rate}=(\ln2/\mathfrak h^2)/\kappa_{0,\min}\ [\mathrm{FT.37}];\quad\kappa_0=1\iff\text{cube}\iff\text{CT1.29 saturation}\ [\mathrm{FT.37}\ \text{iff-clause}]
$$
$$
\Pi_{\min}=8E^2K_{S,\min}\ [\mathrm{FT.42}(5)];\qquad\text{lock sums}:\ \mathrm{FT.62}(2)\ [\text{machine}]
$$
$$
(6):\ \mathrm{FT.54}(4)\ \text{at}\ \Theta_R=\delta_v;\quad m^2_{\mathrm{hid}}=4E^2(\ln2)^2/\mathfrak h^2\ [\mathrm{FT.42}(1)];\qquad D_S=2-2\cos(\delta_v/2)\ [\text{half-angle}];\ \text{table values}\ [\text{machine: radicals},\ \text{min. polys}]
$$
$$
\text{quartic}:\ c=\cos\tfrac\pi{10}:\ \cos5t=16c^5-20c^3+5c\ [\text{de Moivre};\ \text{machine}];\ t=\tfrac\pi{10}:\ \cos\tfrac\pi2=0\implies16c^4-20c^2+5=0;\quad x=2-2c\implies x^4-8x^3+19x^2-12x+1=0\ [\text{machine: exact substitution}]
$$
$$
\text{ladder}:\ D_S(m)=2-2\cos(m\delta_v/2)\ [\mathrm{FT.60}(5)];\qquad\text{table per solid}\ [\text{machine}:\ \mathbb Q,\ \mathbb Q(\sqrt2),\ \mathbb Q(\sqrt3),\ \mathbb Q(\sqrt5)\ \text{exact}]
$$
$$
(7):\ \mathrm{FT.20}\ \text{rows}+\mathrm{FT.42}(4);\qquad g(V)=\!\!\sum_{2a+3b=V}\!\!\tfrac{V!}{a!\,b!\,2^a6^b}\ [\mathrm{FT.41}(b)];\quad V\ \text{even}\implies3b\ \text{even}\implies b\ \text{even};\qquad\text{term breakdowns}\ [\text{machine}]
$$
$$
N(\Sigma_S):\ \text{dark}\ 0;\ \text{obs}\ 1\ \text{or}\ 2\ [\mathrm{Def\text{-}H.12}];\quad N{=}2\ \text{corolla at}\ n(w){=}2:\ \mathrm{FT.58}(1);\quad\text{face-floor variant}:\ \mathrm{FT.59}(4a).\ \blacksquare
$$

**Rmk (corner convention, undeclared).** Skeleton face-loops pass through conical vertices: their $\Theta_R$ requires a corner-distribution convention for defects on the loop (or the two-region read $0$ vs $4\pi-\delta$: the defect values differ by side, though the total $4\pi$ and the SU(2) global triviality are side-independent). This is the single place where the requested "mass ratio" computation meets an undeclared convention, and it is marked rather than papered over.

**Rmk (no identifications).** As everywhere in this document: no card entry is identified with a named particle; the dual-degeneracy/splitting pattern (mass and $\Pi$ degenerate; winding, sealing, locks, pole defects, and spin structure split) extends FT.44(2)'s template with two new columns and remains a template, not a generation claim .

**Phys.** Computed in full, the five solids read: spins — half-integer faces composing to integer stretched totals, six for the tetrahedron and cube, twelve for the octahedron, thirty for the last dual pair; charges — ternary core registers on every closed loop, three to nineteen independent reads, flipping under the corpus's own conjugation; parities — an index-$2^{F-1}$ lattice whose mod-2 classes are exactly the cuts of the skeleton, with the octahedron alone forced even-wound by its two-colored faces; holonomies — trivial spirals, trivial global spinor transport, and conical vertex defects summing to one sphere; entropies — twelve to sixty hidden bits, the cube alone running its minimal loops at the exact Bekenstein rate; mass ratios — the pole side written in $\sqrt2$, $\sqrt3$, and $\cos\frac\pi{10}$, splitting every dual pair that the hidden-bit mass degenerates; binding — gravity and Higgs always, weak whenever the ledger is wound, colour in three to two-hundred-ninety-three-billion sealing patterns, always baryon-even, never as a number a sealed floor carries.

---

---

### FT.64 — The filter chain and the per-solid loop lattices

**Thm.** $(1)$ **Filter chain (definition of ledger-admissible).** A loop datum on a floor $\Sigma$ is **ledger-admissible** iff it passes, in order: **(F0)** configuration validity — closed real-edge content, Janus balance, mask image, no dangling ledger boundary [D2.11, D1.3, D0.10]; **(F1)** registration — $\sigma_e\in\{\pm1\}$ per directed real edge, independent of $\kappa$ [CT0.9, CT0.10]; **(F2)** integrality — $\kappa_e\in\mathbb Z$ on edges of materialized digons and round-trip-closed channels (classes (i)/(ii) [FT.24, FT.34(4)]; Platonic/polygon floors: under declared M2 [Def-H.20]); **(F3)** loop quantization — $\Theta(c)\in2\mathbb Z$ per materialized closed chain [FT.22; M1 on faces]: for the Platonic floors exactly $\kappa\in\ker\varphi_S$, $\varphi_S=\,$face-incidence mod $2$ [FT.43(3)]; **(F4)** stationarity (semiclassical survivors) — $\kappa\equiv\kappa_0$ constant along each connected materialized chain, geodesic support [FT.53(1)–(2), FT.48(1)]; **(F5)** regime — null-permitting ($\kappa\ge0$), strictly-spacelike ($\kappa\ge1$), uniform, or signature-mixed ($\kappa\in\mathbb Z$; fibers infinite at fixed $K$ — witness $(K{+}n,-n)$ — so enumeration is scoped to $\kappa\ge0$ [FT.45(4) pattern]); **(F6)** relabeling quotient — identification under mask-preserving relabeling [CT2.6's $\sim$, CT2.7; FT.51(3)]: $\operatorname{Aut}(\Gamma_S)$-orbits (FT.65); **(F7)** register product — signs $\times$ $\kappa$-orbits $\times$ sealing groupings, independent registers [FT.51(5), FT.65(2)]; **(F8)** spectral filter — materialization (M1/M2 declared; which admissible loops are on-spectrum is the corpus's [D2.4, CT2.5, Def-H.16]); no ledger-side criterion can further select by stability index [FT.61(4)]: **(F8) is the honest boundary of this list**.
$(2)$ **Per-solid lattice, all five by machine.** $\ker\varphi_S\subseteq\mathbb Z^E$ has index $2^{F-1}$ — GF(2) rank $F-1$ verified by explicit elimination for **all five** solids (the earlier tetra/cube checks extended): $(8,32,128,2048,2^{19})$. Equivalent formulation: $\kappa\bmod2$ lies in the **cut space** of $\Gamma_S$ — $\dim_{\mathbb Z_2}\ker\varphi_S=E-(F-1)=V-1=\dim\operatorname{Cut}(\Gamma_S)$ [Euler; math: planar duality; machine: dimensions + vertex-star cut witnesses].
$(3)$ **Face-read realizability (SNF).** For the face-read map $B:\mathbb Z^E\to\mathbb Z^F$, $\kappa\mapsto(\Theta_f)_f$: Smith invariant factors are $(1,1,1,2)$ tetrahedron, $(1^5,2)$ cube, $(1^7)$ octahedron (rank $7=F{-}1$), $(1^{11},2)$ dodecahedron, $(1^{19},2)$ icosahedron [machine]. Consequences: **(a)** tetrahedron/cube/dodecahedron/icosahedron: $(2\mathbb Z)^F\subseteq\operatorname{im}B$ — *every* integer face-winding vector $k=(k_f)\in\mathbb Z^F$ is realized by some signed $\kappa$ [machine witness: all four unit vectors $k=e_f$ realized on the tetrahedron with $\kappa\in[-2,2]^6$]; **(b)** octahedron: $\operatorname{im}B=\ker\psi$, $\psi=$ black$-$white face-sum (dual bipartite, $d$ even — the unique such Platonic): $k$ realizable $\iff\sum_{\mathrm{bl}}k_f=\sum_{\mathrm{wh}}k_f\iff K_S\in2\mathbb Z$ [machine: $\psi(\operatorname{im}B)=0$ on samples; $\psi(2e_f)=\pm2\ne0$: $k=e_f$ unrealizable]; each channel lies in exactly one black and one white face [machine].
$(4)$ **Level-set counts.** $A_S(K):=\#\{\kappa\in\mathbb Z_{\ge0}^E:\ \sum_e\kappa_e=K,\ \varphi_S(\kappa)=0\}$ (level $K=K_S=\Theta_{\mathrm{int}}/2$) [machine, DFS with face-parity pruning; cross-checked against orbit enumeration and the Burnside identity element]:
$$
\begin{array}{c|ccccccccc}
S & K{=}0 & 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8\\ \hline
\text{tetrahedron} & 1 & 0 & 6 & 4 & 24 & 24 & 74 & 84 & 189\\
\text{cube} & 1 & 0 & 12 & 8 & 93 & 120 & 576 & — & —\\
\text{octahedron} & 1 & 0 & 12 & 0 & 84 & 0 & 452 & — & —\\
\text{dodecahedron} & 1 & 0 & 30 & 20 & 495 & 672 & — & — & —\\
\text{icosahedron} & 1 & 0 & 30 & 0 & 465 & 12 & — & — & —
\end{array}
$$
with the exact character-sum closed form [math: GF(2) orthogonality; machine-verified against the DFS for tetrahedron/cube/octahedron, $K\le6$]:
$$
A_S(K)=\frac{1}{2^{F-1}}\sum_{s\in\mathbb Z_2^F/\langle\mathbf1\rangle}[z^K]\prod_{e\in E}\frac{1}{1-(-1)^{s\cdot b_e}\,z}\qquad(b_e=\text{face-incidence column of}\ e),
$$
and asymptotics $A_S(K)\sim\binom{K+E-1}{E-1}/2^{F-1}\sim K^{E-1}/((E-1)!\,2^{F-1})$ [equidistribution of the $F-1$ parity conditions; machine trend: tetrahedron $A(16)=2673$ vs $20349/8$]. Structural reads [machine]: $A_S(1)=0$ for every solid (no bridges — a lone $\kappa{=}1$ channel leaves its two faces odd); $A_S(3)=V$ for the $d{=}3$ solids (the vertex stars), $0$ for the $d\ge4$ solids (octahedron: even-$d$ parity; icosahedron: its stars carry $K{=}5$); the octahedron has $A(\text{odd}\,K)=0$ [(3)(b)]; the icosahedron's $A(5)=12$ is exactly its star family — the index-$2^{19}$ lattice is sparse enough that at low levels only the symmetric families survive. The $K{=}0$ entry is the all-null bound configuration (trivial-chain content [D1.7, D3.7]; $W$-row silent [FT.42(3)]).
$(5)$ **Minimality regimes, all five** [FT.45(4)/FT.32(6) pattern; machine]:
$$
\begin{array}{c|c|c|c|c}
S & \text{R0 null-perm.}: (K_{\min},\Theta_{\mathrm{int}},\text{orbits}) & \text{R1 strict}: (\varepsilon_{\min},K_{\min},\Theta_{\mathrm{int}},\text{orbits}) & \text{R2 uniform}: \kappa_0\ \text{ladder} & \text{R1 witness type}\\ \hline
\text{tetrahedron} & (2,4,1) & (2,8,16,1) & 2,4,6,\dots & \text{opposite-edge pair at}\ 2\\
\text{cube} & (2,4,1) & (0,12,24,1) & 1,2,3,\dots & \text{all-1 profile (unique)}\\
\text{octahedron} & (2,4,1) & (4,16,32,3) & 2,4,6,\dots & \text{coset leaders, 3 orbits}\\
\text{dodecahedron} & (2,4,1) & (6,36,72,25) & 2,4,6,\dots & \text{coset leaders, 25 orbits}\\
\text{icosahedron} & (2,4,1) & (10,40,80,14) & 2,4,6,\dots & \text{coset leaders, 14 orbits}
\end{array}
$$
R0: single channel at $\kappa{=}2$ (one orbit — $\operatorname{Aut}$ edge-transitive [machine]). R1: $\kappa=1+x$, $x\ge0$: parity demands $Bx\equiv(L\bmod2)\cdot\mathbf1$; $\varepsilon_{\min}=$ minimum weight in the GF(2) coset [machine: coset enumeration, $\le2^{19}$ for the dodecahedron]. **Derived laws**: (a) $\Theta_{\mathrm{int},\min}^{\mathrm{R0}}=4$ for every solid vs $2$ for $\Sigma_{\min}$ and $2$ (face-winding) for polygons — a solid's faces are too many to be fooled by one channel [$F\ge4$ separated faces; FT.45(5)'s digon distinction extended]; (b) the **cube is the unique Platonic whose uniform-minimal profile is also its strictly-spacelike minimum** ($\varepsilon_{\min}=0$; all-1, unique up to symmetry) — for the four odd-$L$ solids R1 beats R2 strictly ($16{<}24$, $32{<}48$, $72{<}120$, $80{<}120$): their uniform minima are *not* their cheapest spacelike configurations, and the minimizers form nontrivial orbit families (up to $25$); (c) R2's stationary ladder is the semiclassical survivor list [FT.53]: one orbit per rung $\kappa_0$, $K=E\kappa_0$.
$(6)$ **Completeness, ledger side.** (F0)–(F7) are decidable and decided above (or cited closed-form: polygons [FT.51], cycles [FT.32(6)]); (F8) is declared. The list is complete as a ledger enumeration: every admissible loop datum on every computed floor is an element of $\ker\varphi$ (lattice) $\times$ sign registers $\times$ sealing groupings, modulo $\operatorname{Aut}$, within one of the four regimes, surviving semiclassically exactly on the R2 ladder.

**Req.** FT.22, FT.24, FT.32, FT.34, FT.42, FT.43, FT.45, FT.48, FT.51, FT.53, FT.61, FT.62; Def-H.20; M1/M2 (interface clause); D0.10, D1.3, D1.7, D2.4, D2.11, D3.7; CT0.9, CT0.10 (Part 1); CT2.5, CT2.6, CT2.7 (Part 2); Def-H.16; GF(2) elimination, Smith normal form, planar cut-space duality, character orthogonality, stars-and-bars asymptotics [math].

**Pf.**
$$
(1):\ \text{each step one citation as listed};\qquad\text{order}:\ \mathrm{F2/F3}\ \text{before}\ \mathrm{F4}\ [\text{integrality classes gate rigidity},\ \mathrm{FT.38}(2)/\mathrm{FT.53}];\ \mathrm{F8}\ \text{last}\ [\text{spectral},\ \text{declared}]
$$
$$
(2):\ \mathrm{FT.43}(3)\ \text{method extended}:\ \text{explicit GF(2) elimination per solid}\ [\text{machine}];\qquad\dim\ker=E-\operatorname{rk}\varphi=E-(F-1)=V-1\ [\text{Euler}];\quad\operatorname{Cut}:\ \dim=V-1\ [\text{math}];\ \text{stars}\ \delta\{v\}\in\ker\varphi\ [\text{machine}]
$$
$$
(3):\ \mathrm{SNF}\ [\text{machine}:\ \text{integer row/column reduction}];\qquad(a):\ \text{divisors}\in\{1,2\}\iff(2\mathbb Z)^F\subseteq\operatorname{im}B\ [\text{math}];\ \text{witnesses}\ [\text{machine}]
$$
$$
(b):\ \text{dual bipartite}\iff d\ \text{even}\ [\text{machine}:\ 2\text{-coloring}];\quad\psi(B\kappa)=\sum_e\kappa_e(1-1)=0;\quad\psi(2e_f)=\pm2;\qquad K_S=\textstyle\sum_fk_f=2\sum_{\mathrm{bl}}k_f
$$
$$
(4):\ \text{DFS with completed-face parity pruning}\ [\text{machine}];\qquad\text{character sum}:\ \tfrac1{2^{F-1}}\sum_s(-1)^{s\cdot B\kappa}\ \text{projection}\ [\text{math};\ \text{machine vs DFS}];\qquad\text{asymptotics}:\ s=0\ \text{term dominates}\ [\text{math};\ \text{machine trend}]
$$
$$
A(1)=0:\ \text{single channel}:\ \text{its}\ 2\ \text{faces odd};\ \neg\exists\ \text{bridge}\ [\text{solid}\ 2\text{-edge-connectivity};\ \text{machine}];\qquad A(3)=V\ (d{=}3):\ \text{stars}\ \delta\{v\}:\ \text{each face at}\ v\ \text{meets}\ 2\ \text{star edges}
$$
$$
(5):\ \text{R0 witness}\ \kappa=2e:\ B(2e)\equiv0;\ \text{orbit}=\text{point}\ [\text{edge-transitivity};\ \text{machine}];\qquad\text{R1}:\ \kappa=1+x:\ \Theta_f=L+\sum_{e\in f}x_e\in2\mathbb Z\iff Bx\equiv(L\bmod2)\mathbf1;\ \varepsilon_{\min}=\text{coset leader weight}\ [\text{machine}]
$$
$$
\text{cube}:\ L\ \text{even}:\ x=0\ \text{admissible}:\ \varepsilon_{\min}=0,\ \kappa\equiv1\ \text{unique at}\ K=E;\qquad\text{odd}\ L:\ \varepsilon_{\min}\ge2\ (B x\equiv\mathbf1\ \text{needs}\ x\ne0);\ \text{witnesses as tabled}\ [\text{machine}]
$$
$$
(6):\ \text{decidability}:\ \text{each filter arithmetic or cited-closed}.\ \blacksquare
$$

**Rmk (what the sparse low levels mean).** The icosahedron's lattice is so fine (index $2^{19}$) that below its star level $K{=}5$ only the symmetric families fit: $A(3)=0$, $A(5)=12$. Low-level admissibility on a solid is therefore *highly non-generic* — most low profiles are excluded not by energy but by parity — a derived selection pressure of purely combinatorial origin that any spectral mechanism (F8) inherits for free. Recorded as structure; no physical reading claimed.

**Phys.** Run the machine and the five solids answer with one grammar: a lattice of index a power of two, whose odd classes are exactly the cuts of the skeleton; winding vectors free as integers on four of the five, balanced black-against-white on the octahedron; a cheapest null-tolerant loop of four quanta everywhere, cheapest honest loops that beat uniformity on every odd-faced solid; and a semiclassical list of survivors that is nothing but the uniform ladder — one orbit per rung. The list is complete up to exactly one door: which of these loops the spectrum keeps. That door was always the corpus's, and the ledger now proves it cannot be opened from this side.

---

---

### FT.65 — Coarse-grained degeneracies, register product, and the master loop list

**Thm.** $(1)$ **Degeneracy under the relabeling quotient.** $\operatorname{Aut}(\Gamma_S)$ acts on admissible profiles by channel permutation [CT2.6's $\sim$ on coarse-grained ledger entries; CT2.7: weights are vertex-name independent; FT.51(3) pattern]; orders $|\operatorname{Aut}|=(24,48,48,120,120)$, rotation subgroups $(12,24,24,60,60)$ [machine: enumeration + determinant filter on exact coordinates, $\mathbb Q$ and $\mathbb Q(\sqrt5)$]. The coarse-grained degeneracies $M_S(K)=\frac1{|\operatorname{Aut}|}\sum_g\operatorname{fix}(g,K)$ [Burnside; math] — with $\operatorname{fix}(g,K)$ the orbit-constant profile count [machine: orbit-DP with face-parity masks; identity element cross-asserted against $A_S(K)$; small-$K$ values cross-checked by direct orbit enumeration]:
$$
\begin{array}{c|ccccccccc}
S & K{=}0 & 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8\\ \hline
M\ \text{tetrahedron} & 1 & 0 & 1 & 1 & 4 & 2 & 8 & 6 & 17\\
M\ \text{cube} & 1 & 0 & 1 & 1 & 7 & 4 & 25 & — & —\\
M\ \text{octahedron} & 1 & 0 & 1 & 0 & 6 & 0 & 19 & — & —\\
M\ \text{dodecahedron} & 1 & 0 & 1 & 1 & 10 & 9 & — & — & —\\
M\ \text{icosahedron} & 1 & 0 & 1 & 0 & 9 & 1 & — & — & —\\ \hline
M^+\ \text{tetrahedron} & 1 & 0 & 1 & 1 & 4 & 2 & 11 & 7 & 23\\
M^+\ \text{cube} & 1 & 0 & 1 & 1 & 8 & 5 & 34 & — & —\\
M^+\ \text{octahedron} & 1 & 0 & 1 & 0 & 7 & 0 & 25 & — & —\\
M^+\ \text{dodecahedron} & 1 & 0 & 1 & 1 & 13 & 12 & — & — & —\\
M^+\ \text{icosahedron} & 1 & 0 & 1 & 0 & 12 & 1 & — & — & —
\end{array}
$$
$M^+$ (rotation-only quotient) is reported alongside $M$ (full automorphism quotient, the FT.51 convention for polygons): whether orientation-reversing relabelings identify states is the $\omega$/charge-conjugation read [D2.6] — both counts are derived data; no choice is imposed. Growth: $M_S(K)\sim A_S(K)/|\operatorname{Aut}|$ generically (free orbits dominate) [math; the fixed-point terms are lower-order].
$(2)$ **Register product (generalized).** Distinct ledger states of $\Sigma_S$ at level $K$:
$$
\#\text{states}(K)=2^{2E}\cdot M_S(K)\cdot g(V)\cdot(\text{attachment-type data})\qquad[\mathrm{FT.51}(5)\ \text{pattern};\ \mathrm{CT0.9}/\mathrm{CT0.10}:\ \text{signs independent of}\ \kappa;\ \mathrm{FT.41}(b):\ \text{sealing register}],
$$
with $g(V)=(3,385,25,292938721075,164395)$ [FT.63(7)] — the three registers multiply, none converts into another; e.g. dark tetrahedron at $K{=}2$: $2^{12}\cdot1\cdot3=12288$ states before attachment data.
$(3)$ **Density of states.** $\#\text{states}(K)\sim2^{2E}\,g(V)\,K^{E-1}/((E-1)!\,2^{F-1}\,|\operatorname{Aut}|)$ [from FT.64(4)'s asymptotics]: polynomial in the winding at fixed solid — degrees $E-1=(5,11,11,29,29)$ — with the Platonic prefactors spanning twelve orders of magnitude (tetrahedron $2^{12}\cdot3/24$ vs dodecahedron $2^{60}\cdot g(20)/120$): the derived state-count substrate any selection mechanism (Open Gaps 5/12, filter F8) would act on.
$(4)$ **Master generalized loop list** (every cell computed in this document; $K=\Theta_{\mathrm{int}}/2$ levels; lattice index within $\mathbb Z^{E_{\mathrm{ch}}}$; all entries machine-verified or cited-closed):
$$
\begin{array}{l|c|c|c|c|c|c|c}
\text{cell} & E_{\mathrm{int}} & m_{\mathrm{hid}}\cdot\tfrac{\mathfrak h}{\ln2} & \text{lattice index} & K_{\min}\ (\Theta_{\mathrm{int},\min}) & \Theta_{\min}^{\mathrm{strict}} & \kappa_0\ \text{ladder}\ (\mathrm{F4}) & \text{quotient}\ \to\ M\\ \hline
\Sigma_{\min}\ [\mathrm{FT.28}] & 2 & 2 & 1\ (\kappa\in\mathbb Z) & 1\ (2) & 2\ (\kappa{=}1) & 1,2,3,\dots & \text{trivial}\to1\\
\Sigma_L\ \text{uni.}\ [\mathrm{FT.32}] & L & L & 2\ (\textstyle\sum\kappa\in2\mathbb Z) & 1\ (2) & L{+}(L\bmod2) & \text{even}\ (L\ \text{odd})\ /\ \text{any}\ (L\ \text{even}) & \mathbb Z_L\to\text{necklaces}\\
\Sigma_{P_n}\ \text{bidir.}\ [\mathrm{FT.45}] & 2n & 2n & 2 & 2\ (4) & 2n{+}2(n\bmod2) & 1,2,\dots\ (n\ \text{ev})\ /\ 2,4,\dots\ (n\ \text{odd}) & D_n\to M(n,k)\ [\mathrm{FT.51}]\\
\Sigma_{12}\ [\mathrm{FT.35}] & 6 & 6 & 1\ (\mathbb Z^3) & 1\ (2) & 3\ (6) & \text{free}\ \mathbb Z^3\ (\text{digon quanta}) & \mathbb Z_2\to\text{swap-orbits}\\
\Sigma_\triangle\ [\mathrm{FT.49}] & 6 & 6 & 2 & 2\ (4) & 4\ (8) & 2,4,\dots & D_3\to M(3,\cdot)=(2,4,7)\\
\text{bowtie}\ [\mathrm{FT.50}] & 12 & 12 & 4 & 2\ (4) & 8\ (16) & (2a,2b)\ \text{per face} & |\operatorname{Aut}|=8\ (\text{not tabulated})\\
\text{double-triangle}\ [\mathrm{FT.50}] & 10 & 10 & 4 & 2\ (4) & 6\ (12) & 2,4,\dots & \mathbb Z_2\times\mathbb Z_2\ (|\operatorname{Aut}|=4,\ \text{not tabulated})\\ \hline
\text{tetrahedron} & 12 & 12 & 8 & 2\ (4) & 8\ (16) & 2,4,6,\dots & S_4\to\text{table}\ (1)\\
\text{cube} & 24 & 24 & 32 & 2\ (4) & 12\ (24) & 1,2,3,\dots & S_4\times\mathbb Z_2\to\text{table}\\
\text{octahedron} & 24 & 24 & 128\ (K\ \text{even}) & 2\ (4) & 16\ (32) & 2,4,6,\dots & S_4\times\mathbb Z_2\to\text{table}\\
\text{dodecahedron} & 60 & 60 & 2048 & 2\ (4) & 36\ (72) & 2,4,6,\dots & A_5\times\mathbb Z_2\to\text{table}\\
\text{icosahedron} & 60 & 60 & 2^{19} & 2\ (4) & 40\ (80) & 2,4,6,\dots & A_5\times\mathbb Z_2\to\text{table}
\end{array}
$$
(Columns: $E_{\mathrm{int}}=$ directed internal edges; index $=$ of the on-shell $\kappa$-lattice in the channel lattice; $K_{\min}$ null-permitting with $\Theta_{\mathrm{int},\min}=2K_{\min}$; strict $=$ minimal $\Theta_{\mathrm{int}}$ at $\kappa\ge1$ with its $K$; $\kappa_0$-ladder $=$ the stationary (F4) survivors; quotient group with degeneracy source. For the solids, $\Theta_{\mathrm{int},\min}^{\mathrm{R0}}=4$ universally and the strict minima are the FT.64(5) coset-leader values.)
$(5)$ **Taxonomy law, re-anchored.** Across every computed cell and family (the twelve master-table rows below plus the $\Sigma_L$/$\Sigma_{P_n}$ members): $m_{\mathrm{hid}}=E_{\mathrm{int}}\ln2/\mathfrak h$ with $E_{\mathrm{int}}=2E_{\mathrm{bidir}}+E_{\mathrm{uni}}$ [FT.44(4) — extended from eleven cells to sixteen, zero exceptions], and the list is closed under the program's composition operations: bridged unions add masses and windings [FT.50(1)–(2)], gluings compose lattices by constraint rank [FT.50(4)], round-trips add connector distance [FT.34(3)] — every composite of listed cells is itself a listed-type cell with computable invariants.

**Req.** FT.28, FT.32, FT.34, FT.35, FT.41(b), FT.42–FT.45, FT.49–FT.51, FT.63, FT.64; CT0.9, CT0.10 (Part 1); CT2.6, CT2.7 (Part 2); D2.6; Burnside, orbit-stabilizer, asymptotics [math]; Def-H.20; M1/M2 (declared, solids/polygon rows).

**Pf.**
$$
(1):\ \operatorname{Aut}\ \text{by adjacency backtracking}\ [\text{machine}:\ \text{orders}\ 24,48,48,120,120];\quad\text{rotations}:\ \det=+1\ \text{on exact coordinate realization}\ [\text{machine}:\ \mathbb Q\ \text{and}\ \mathbb Q(\sqrt5)\ \text{linear algebra}]
$$
$$
\text{Burnside}:\ \operatorname{fix}(g,K)=\#\{\text{orbit-constant}\ \kappa\ge0:\ \textstyle\sum=K,\ \varphi=0\}\ [\text{orbit-DP with parity masks};\ \text{machine}];\qquad\operatorname{fix}(\mathrm{id},K)=A_S(K)\ [\text{cross-asserted}];\quad M\in\mathbb Z\ [\text{asserted}]
$$
$$
\text{cross-checks}:\ \text{direct orbit enumeration}\ K\le3\ (\text{tetra/cube/octa}),\ K\le2\ (\text{dodeca/icosa})\ [\text{machine}];\qquad M^+\ge M\ [\text{smaller group}]
$$
$$
(2):\ \mathrm{CT0.9}:\ 2^{2E}\ \text{sign registers};\ \mathrm{CT0.10}/\mathrm{FT.51}(5):\ \text{independence};\ \mathrm{FT.41}(b):\ g(V);\ \mathrm{D3.8}:\ \text{attachments};\qquad\text{example}:\ 2^{12}\cdot1\cdot3=12288\ [\text{machine}]
$$
$$
(3):\ \text{substitution of FT.64}(4)\ \text{asymptotics};\qquad(4):\ \text{rows}:\ \mathrm{FT.28}(2),\mathrm{FT.32}(1),(6),\mathrm{FT.45}(1),(3),(4),\mathrm{FT.35}(1)\text{--}(3),\mathrm{FT.49}(2),(4),\mathrm{FT.50}(5),\mathrm{FT.62}\text{--}\mathrm{FT.64}
$$
$$
\Sigma_{\min}\ \text{index}\ 1:\ \Theta=2\kappa\in2\mathbb Z\ \text{automatic}\ [\mathrm{FT.24}];\quad\Sigma_L:\ \{\textstyle\sum\kappa\in2\mathbb Z\}\ \text{index}\ 2\ [\mathrm{FT.32}(6)\ \text{scope}];\quad\Sigma_{12}:\ \mathbb Z^3\ [\mathrm{FT.35}(1),(3)]
$$
$$
\text{bowtie/patch}:\ \text{index}\ 4\ [\mathrm{FT.50}(5):\ \mathbb Z_2\text{-rank}\ 2];\qquad(5):\ \text{per-cell counts cited};\ \text{composition laws}\ [\mathrm{FT.34}(3),\mathrm{FT.50}(1),(2),(4)].\ \blacksquare
$$

**Rmk (the two untabulated quotients).** Bowtie ($|\operatorname{Aut}|=8$: the degree-4 junction is fixed; the two pairs of leaf vertices swap freely, and the two triangles exchange) and double-triangle patch ($\mathbb Z_2\times\mathbb Z_2$: $C\leftrightarrow D$, $A\leftrightarrow B$) degeneracy tables are computable by the same machine and are deferred only for space; their lattice indices, minima, and group orders are in the table. Quotient convention throughout: automorphisms of the floor's internal skeleton (CT2.7's vertex-name independence; external contacts are configuration data, not relabeled). No structural claim rests on the omission.

**Phys.** The generalized list, read aloud: every fermion floor the program has computed admits loops on one lattice per topology — index one for the digon and the wired pair, index two for cycles and polygons and the tetrahedron face, index four for the glued pairs, eight to half a million for the solids — and on each lattice the admissible loops come in four regimes, collapse to orbits under the skeleton's own symmetries, and multiply by two independent sign-and-sealing registers. Twelve rows, one mass law, closed under composition. What the list does not contain is its own last filter: which loops the spectrum keeps. The ledger side is finished; the door is the corpus's.

---

---

### FT.69 — Platonic amplitude census completed; the cycle-alternation lemma; one census correction

**Thm.** Under Def-H.25's scopes (S1)–(S4):
$(1)$ **Cap census, completed.** Bypass-configuration counts by $K$ (cap-DP, exact): octahedron $318\,523$ ($K\le9$; row $(1,24,276,2024,10206,35448,81344,110736,69504,8960)$; $K\le5$ exhaustively validated); dodecahedron $3\,067\,633\,654\,196\,912$ ($K\le30=3V/2$ forced); icosahedron $2\,483\,119\,531\,360$ ($K\le18=3V/2$ forced). Low-order universality: the rows of the two $60$-edge skeletons agree through $K=3$ ($(1,60,1770,34220)$: caps bind only from $K=4$: $487335$ vs $485115$, the difference $20\binom64$ vs $12\binom{10}4$ exactly the single-vertex lock counts) and diverge from $K=4$ on. Orbits: not attempted (bounded rule: cube's $33\,564$ already exceeded $10^4$ [FT.68(3)]).
$(2)$ **Coverings.** Octahedron complete (two independent enumerators agree): $\mathcal Z_{\mathrm{byp}}(y)=1+72y+852y^2+1152y^3$, $\mathcal Z_{\mathrm{lock}}(y)=36y^2+1008y^3+840y^4$; $Z^{\pm}_{\mathrm{byp}}=87\,649$, $Z^{\pm}_{\mathrm{lock}}=280\,128$, $Z^{\pm}_{\mathrm{all}}=367\,777$. Dodecahedron/icosahedron exact to $|\mathcal C|\le3$: dodecahedron $\{0{:}1,\,1{:}120,\,2{:}5880{+}60_{\mathrm{lock}},\,3{:}153\,960{+}6140_{\mathrm{lock}}\}$ ($166\,161$ covers, $Z^{\pm}\ge9\,948\,001$ byp / $393\,920$ lock from the counted range); icosahedron $\{0{:}1,\,1{:}240,\,2{:}17\,520{+}120_{\mathrm{lock}},\,3{:}478\,360{+}27\,600_{\mathrm{lock}}\}$ ($523\,841$ covers, $Z^{\pm}\ge30\,896\,321/1\,768\,320$ counted). Single-centre closed form on every skeleton: $\#\{|\mathcal C|=1\}=V\,d_{\mathrm{in}}d_{\mathrm{out}}$ minus closed-thread exclusions $=V\,d(d{-}1)$ bidirectional $=(24,48,72,120,240)$ for the five solids [machine]. Full dodeca/icosa counts deferred: the vertex-DP state width (cut-arcs $\le11$ at degree $5$; memo exhaustion) and the branch enumerator ($\sim(1+d^2)^V$ raw) both exceed the bounded rule — recorded, not guessed. Fully crystallized floors cancel: types $(3,3)^{20}$, $(5,5)^{12}$, no centres, value $0$ [FT.67(3a)].
$(3)$ **Cycle-alternation lemma.** Let $R$ be a literal-domain cover and $\gamma\subseteq R$ a directed cycle. Then along $\gamma$ the vertices **strictly alternate centre / non-centre**; consequently: (i) $|\gamma|$ is even; (ii) every non-centre vertex of $\gamma$ carries at least one further real edge outside $\gamma$ (else its type on $\gamma$ alone is $(1,1)$, forcing a centre — contradiction); (iii) a pure directed cycle is never a cover [FT.67(3a), now with its structural reason]; (iv) **no odd directed cycle — in particular no triangle — lies inside any cover**: the amplitude layer's bound content is exactly even-cycle content, dissolved into threading **[scope: clauses (i)–(v) are literal-domain theorems. Both chain-local extensions dissolve odd cycles into open threads — on the tetrahedron, of $2397$ patterns containing a directed $3$-cycle, $833$ (E2) and $1025$ (E1) have nonzero amplitude against $0$ literal [FT.75(4)]]**; (v) census (distinct cycles, canonicalized; machine): covers containing directed cycles — tetrahedron $64/101$ ($84$ digon instances; $48$ bypass $+16$ locked), cube $9060/11205$ ($14\,328$ digons, $504$ four-cycles), octahedron $3054/3961$ ($4704$ digons, $672$ four-cycles), $P_3$–$P_7$ digons only; the $P_4$ face $4$-cycle lies in *none* of its $33$ covers (clause (ii): its non-centre cycle vertices have no extra edges to carry); zero odd cycles in any enumerated cover.
$(4)$ **FT.68(1) census correction (self-audit).** The tetrahedron census numbers stand ($501/252/90$ bypass configurations containing digons/$3$-cycles/$4$-cycles, re-derived). The clause "all of it cancels in amplitude" is **false for the digon row**: $48$ of the $501$ are covers. Witness (machine, brute-force sign sum $=$ cover value $=16$): $R=\{(0{\to}1),(1{\to}0),(2{\to}1),(3{\to}2)\}$, types $\bigl((1,1),(2,1),(1,1),(0,1)\bigr)$ — the digon $\{0,1\}$ dissolved: centre $0$ reads both digon edges, vertex $1$ is a $(2,1)$ non-centre supported by centre $2$'s thread. The $3$-cycle and $4$-cycle rows cancel completely [(iii)+(i) of clause (3); machine: $0$ nonzero of $252/90$]. **[addition: these $48$ survivors are killed by *both* chain-local extensions ($N_{E2}=N_{E1}=0$ on all $48$, exhaustive), while the $16$ *locked* digon-covers of clause (5) are killed by E2 and kept by E1 at the derangement values $(!a)4^a$ [FT.75(1),(4)]. The triangle rows revive in the extensions: $833$ (E2) / $1025$ (E1) of the $2397$ tetrahedron patterns containing a directed $3$-cycle.]** Corrected statement: **bound cells cancel standalone; bound substructures survive inside covers only dissolved — even cycles threaded through supported non-centres.** FT.68(1) patched in place (marker).
$(5)$ **Minimal dissolution family.** The smallest dissolved-digon covers are double-digon hubs: two digons $\{h,c_1\},\{h,c_2\}$ sharing a locked $(2,2)$ hub $h$, centres $c_1,c_2$ ($|\mathcal C|=2$, $|R|=4$, value $16$): the tetrahedron's $12$ locked two-centre covers are exactly this family ($4$ hub choices $\times\binom32$); exhibited on cube and octahedron. The four $K_{1,3}$ stars [FT.68(1)] are the triple-digon hubs. Locked hubs are the only lock content visible in covers [FT.67 Rmk], and digons are the only bound cells they can host at $|\mathcal C|=2$.

**Req.** Def-H.25; FT.17, FT.22, FT.28, FT.32, FT.42, FT.45, FT.62, FT.63, FT.67, FT.68; A4, A8; D0.1, D0.8, D0.10, D1.4, D1.5, D3.3; CT0.11 (Part 1); CT4.1 (Part 2); cap-DP / cover-DP / branch enumeration, cycle census [math; machine].

**Pf.**
$$
(1):\ \text{cap-DP over vertex-introduction order (state: active degrees $\le3$, by-$K$ accumulation)}\ [\text{machine exact}];\quad K\le\lfloor 3V/2\rfloor:\ \textstyle\sum_vk_v=2K\le3V
$$
$$
\text{low-order rows}:\ K\le3:\ \text{no vertex can reach}\ k_v\ge4:\ c_K=\binom{2E}K;\qquad K=4:\ \binom{60}4-\#\{\text{4 edges at one vertex}\}:\ 20\binom64=300,\ 12\binom{10}4=2520\ \checkmark
$$
$$
(2):\ \text{two enumerators: vertex-introduction DP (centre pre-claim masks, completion checks)}\ =\ \text{branch enumeration over centre sets with claim conflicts pruned};\quad |\mathcal C|=1:\ \text{in-pick}\times\text{out-pick},\ \text{closed thread}\ (s{=}t)\ \text{excluded}\ \implies Vd(d{-}1)
$$
$$
\text{floors}:\ \text{type}(d,d),\ d\ge2:\ \mathcal C=\varnothing,\ R\ne\varnothing:\ \text{cov}\equiv0:\ \text{value}\ 0\ [\mathrm{FT.67}(2)]
$$
$$
(3):\ e_i=(v_i\to v_{i+1})\ \text{along}\ \gamma:\ \operatorname{cov}(e_i)=1:\ v_i\ \text{centre}\iff e_i\ \text{read at tail},\ e_{i-1}\ \text{read at head};\quad v_i\ \text{centre}\implies v_i\ \text{reads both}\ e_{i-1},e_i\implies v_{i\pm1}\ \text{read neither}\implies v_{i\pm1}\ \text{non-centre}
$$
$$
v_i\ \text{non-centre}\implies e_{i-1}\ \text{read at}\ v_{i-1}\ (\text{centre}),\ e_i\ \text{read at}\ v_{i+1}\ (\text{centre}):\ \text{strict alternation};\quad\text{(i)}:\ \text{alternation on a cycle}\implies|\gamma|\ \text{even}
$$
$$
\text{(ii)}:\ v\ \text{non-centre on}\ \gamma:\ \text{type on}\ \gamma\ \text{alone}=(1,1):\ \text{forced centre}\ [\mathrm{D3.3}\ \text{type-based}]\ \implies\ \exists\ \text{extra edge};\qquad\text{(iii)}:\ \text{pure cycle}:\ \text{all vertices on}\ \gamma,\ \text{alternation} + \text{(ii)}\ \text{impossible}
$$
$$
\text{(iv)}:\ \text{odd}\ |\gamma|\ \text{cannot alternate};\qquad\text{(v)}:\ \text{machine census, canonical min-rotation cycles}
$$
$$
(4):\ \text{witness types verified};\ \text{reads}:\ (0{\to}1),(1{\to}0)\ \text{at centre}\ 0;\ (2{\to}1)\ \text{at centre}\ 2;\ (3{\to}2):\ \text{centre}\ 2\ \text{in-pick}:\ \text{cov}\equiv1\ \checkmark;\quad\text{brute force}=16\ [\text{machine}]
$$
$$
(5):\ |\mathcal C|=2\ \text{with a digon}:\ \text{digon edges both read by one centre}\ c\ (\text{type}(1,1)\ \text{forces its only edges});\ \text{partner}\ h:\ \text{second digon's centre}\ c'\ \text{reads it};\ h\ (2,2)\ \text{locked};\ \text{tetrahedron count}\ 4\times\binom32\cdot\ldots=12\ [\text{machine}].\ \blacksquare
$$

**Rmk (what the lemma settles for the two-layer picture).** The amplitude layer does not merely cancel bound *cells* — it cancels every odd cycle and every undissolved even cycle. Bound content inside survivors is always *threaded*: read exactly once per edge, which a closed chain read at both ends can never be. The spectral layer's bound floors (M1/M2) are therefore not in tension with the cover grammar — they are disjoint reads, and the tension is precisely the inter-family bridge.

**Phys.** Ask which flickering patterns carry nonzero ledger amplitude, and the answer now has a grammar: edges tile into open two-step threads, and any loop that hides inside the tiling must be even, must be read alternately, and must be propped open at every other vertex by extra threading. Triangles cannot hide at all. The smallest hiding place is a pair of digons on a locked hub — darkness threaded by transit, exactly the picture the locked-hub remark promised.

---

---

### FT.76 — The Platonic pole-mass multiplets; the bounded-hierarchy ceiling

**Thm.** Under Def-H.37(2) and Def-H.38, with $\Theta_R=\delta_v$ [FT.63(4)'s vertex-figure read; the corner convention is *not* declared in this part], $D_S(m):=m^2_{\mathrm{pole}}(m)/\hat\mu'^2=2-2\cos(m\,\delta_v/2)=4\sin^2(m\,\delta_v/4)$ [FT.60(5)], and $k$ the carrier winding [Def-H.38]:
$(1)$ **Conventions and the two trivial readings.** $k_f=K_S/F=(3,2,3,5,3)$ (face winding; $K_S=(12,12,24,60,60)$ [FT.63(1), FT.43(1)], reproduced from the minimality rule $\kappa_{\min}=2$ odd-$L$ / $1$ even-$L$, $k=L\kappa_{\min}/2$ [FT.32(6), FT.45]); $k_{vf}=(3,3,2,3,5)$ (vertex-figure winding, same rule on the vertex-figure $L_{vf}=(3,3,4,3,5)$). **Variant (A)** $:=$ $(\delta_v,k_f)$ — the directive's reading; **variant (B)** $:=$ $(\delta_v,k_{vf})$ — the loop-consistent reading. Both other readings named by FT.63(4)/(6) are identically massless: $\Theta_R=0$ (flat-face side) and $\Theta_R=V\delta_v=4\pi$ (global sweep: $D(m)=2-2\cos(2m\pi)=0$ for every weight — FT.63(4)'s trivial global spinor transport).
$(2)$ **Exact multiplets.** With $c=\cos\tfrac\pi{10}$ ($16c^4-20c^2+5=0$):
$$
\begin{array}{c|c|c|c}
S & \text{(A)}\ k_f & m^2_{\mathrm{pole}}/\hat\mu'^2\ \text{on}\ \{k,k{-}2,\dots,-k\} & \text{field}\\
\hline
\text{tetra} & 3 & 2,\ 2,\ 2,\ 2\ (m=\pm1,\pm3) & \mathbb Q\\
\text{cube} & 2 & 2\ (m=\pm2),\ \mathbf 0\ (m=0) & \mathbb Q\\
\text{octa} & 3 & 4\ (m=\pm3),\ 1\ (m=\pm1) & \mathbb Q\\
\text{dodeca} & 5 & 2\ (m=\pm5),\ 2{-}2\cos\tfrac{3\pi}{10}\ (m=\pm3),\ 2{-}2c\ (m=\pm1) & \mathbb Q(c)\\
\text{icosa} & 3 & 2\ (m=\pm3),\ 2{-}\sqrt3\ (m=\pm1) & \mathbb Q(\sqrt3)
\end{array}
$$
$$
\begin{array}{c|c|c|c}
S & \text{(B)}\ k_{vf} & m^2_{\mathrm{pole}}/\hat\mu'^2 & \text{field}\\
\hline
\text{tetra} & 3 & 2,\ 2,\ 2,\ 2 & \mathbb Q\\
\text{cube} & 3 & 2{+}\sqrt2\ (m=\pm3),\ 2{-}\sqrt2\ (m=\pm1) & \mathbb Q(\sqrt2)\\
\text{octa} & 2 & 3\ (m=\pm2),\ \mathbf 0\ (m=0) & \mathbb Q\\
\text{dodeca} & 3 & 2{-}2\cos\tfrac{3\pi}{10},\ 2{-}2c & \mathbb Q(c)\\
\text{icosa} & 5 & 2{+}\sqrt3\ (m=\pm5),\ 2\ (m=\pm3),\ 2{-}\sqrt3\ (m=\pm1) & \mathbb Q(\sqrt3)
\end{array}
$$
Decimals ($m^2/\hat\mu'^2$): dodeca $(0.097886967410,\ 0.824429495415,\ 2)$; icosa $(0.267949192431,\ 2)$, (B) adds $3.732050807569$; cube (B) $(0.585786437627,\ 3.414213562373)$. Every value is exact in the stated field and was cross-checked against an exact rational Taylor series for $\cos$ to $45$ digits ($125$ values, $m=0..24$, all five solids).
$(3)$ **Periodicity, monotonicity, and the hard ceiling.** The ladder is periodic in the weight with period $P_S=4\pi/\delta_v=(4,8,6,20,12)$ and takes exactly $P_S/2+1=(3,5,4,11,7)$ distinct values, monotone increasing in $m$ on $[0,P_S/2]$; the maximum is $4\hat\mu'^2$ (attained at $m=P_S/2$; $P_S$ even for all five) and the minimum nonzero value is $D_S$ itself. Hence **every Platonic pole mass lies in $[0,4\hat\mu'^2]$** and the widest ratio attainable *within* a solid is
$$
\frac{4}{D_S}=\Bigl(2,\ \tfrac{4}{2-\sqrt2},\ 4,\ \tfrac{4}{2-2\cos\frac\pi{10}},\ \tfrac{4}{2-\sqrt3}\Bigr)=(2,\ 6.828427,\ 4,\ 40.863458,\ 14.928203)\ \ \text{in}\ m^2,
$$
maximal for the dodecahedron, whose value has minimal polynomial $x^4-48x^3+304x^2-512x+256$; in **mass** the ceiling is $\sqrt{4/D_S}=(1.414214,\ 2.613126,\ 2,\ 6.392453,\ 3.863703)$, maximal at $6.392453\ldots$ No choice of winding — $k_f$, $k_{vf}$, $K_S$, or any iterate — and no admissible $\Theta_R$ convention can exceed it: the value set is finite and bounded.
$(4)$ **Top-weight near-universality.** In variant (A) the heaviest weight of *four of the five* solids is exactly $2\hat\mu'^2$ ($k_f\delta_v\equiv\pi\bmod 2\pi$: tetra $3\pi$, cube $\pi$, dodeca $\pi$, icosa $\pi$), the octahedron's being $4\hat\mu'^2$ ($k_f\delta_v=2\pi$). The inter-solid hierarchy therefore lives **entirely at the light end**; the heavy ends are degenerate across solids.
$(5)$ **Two structural obstructions.** (a) **Tetrahedral degeneracy**: $\delta_v=\pi\Rightarrow D(m)=2-2\cos(m\pi/2)\in\{0,2,4\}$, and the $k=3$ multiplet is *fully degenerate* at $2\hat\mu'^2$ (both variants) — the tetrahedron carries no multiplet splitting at all. (b) **Even-$k$ zero modes** [FT.60(5)'s standing zero]: the cube in (A) ($k_f=2$) and the octahedron in (B) ($k_{vf}=2$) each carry an exactly massless weight $m=0$, so their literal "lightest pole mass" is $0$ and only lightest-*nonzero* reads are well defined.
$(6)$ **Inter-solid ratios (lightest nonzero, relative to the tetrahedron).**
$$
\begin{array}{c|cc|cc}
& \multicolumn2{c|}{\text{(A)}} & \multicolumn2{c}{\text{(B)}}\\
S & m^2\ \text{ratio} & m\ \text{ratio} & m^2\ \text{ratio} & m\ \text{ratio}\\
\hline
\text{tetra} & 1 & 1 & 1 & 1\\
\text{cube} & 1\ (0\ \text{with the zero mode}) & 1\ (0) & 0.292893218813 & 0.541196100146\\
\text{octa} & 0.5 & 0.707106781187 & 1.5 & 1.224744871392\\
\text{dodeca} & 0.048943483705 & 0.221231742082 & 0.048943483705 & 0.221231742082\\
\text{icosa} & 0.133974596216 & 0.366025403784 & 0.133974596216 & 0.366025403784
\end{array}
$$
Normalized to the lightest solid, in mass: (A) dodeca $1$, icosa $1.654488638651$, octa $3.196226610750$, cube $=$ tetra $4.520147021340=\sqrt{2/(2-2c)}$; (B) dodeca $1$, icosa $1.654488638651$, cube $2.446285940037$, tetra $4.520147021340$, octa $5.536026882322$.
$(7)$ **Intra-solid splittings (heaviest/lightest nonzero).**
$$
\begin{array}{c|cc|cc}
S & \text{(A)}\ m^2 & \text{(A)}\ m & \text{(B)}\ m^2 & \text{(B)}\ m\\
\hline
\text{tetra} & 1 & 1 & 1 & 1\\
\text{cube} & 1\ (+1\ \text{zero mode}) & 1 & 3{+}2\sqrt2=5.828427124746 & 1{+}\sqrt2=2.414213562373\\
\text{octa} & 4 & 2 & 1\ (+1\ \text{zero mode}) & 1\\
\text{dodeca} & \tfrac{2}{2-2c}=20.431729094531 & 4.520147021340 & \tfrac{2-2\cos(3\pi/10)}{2-2c}=8.422260053931 & 2.902113032590\\
\text{icosa} & 4{+}2\sqrt3=7.464101615138 & 1{+}\sqrt3=2.732050807569 & 7{+}4\sqrt3=13.928203230276 & 2{+}\sqrt3=3.732050807569
\end{array}
$$
Minimal polynomials of the $m^2$ splittings: dodeca (A) $x^4-24x^3+76x^2-64x+16$, dodeca (B) $x^4-14x^3+51x^2-34x+1$, icosa (A) $x^2-8x+4$, icosa (B) $x^2-14x+1$, cube (B) $x^2-6x+1$; the mass splittings $1{+}\sqrt3$, $2{+}\sqrt3$, $1{+}\sqrt2$ have $x^2-2x-2$, $x^2-4x+1$, $x^2-2x-1$ (machine; certified dyadic isolations).
$(8)$ **Dual splitting, sharpened.** The dual pairs remain degenerate in $m_{\mathrm{hid}}$ and $\Pi$ [FT.44(1)] and split on the pole side as multisets in *both* variants — cube $\{0,2\}$ vs octa $\{1,4\}$ in (A), cube $\{2{-}\sqrt2,2{+}\sqrt2\}$ vs octa $\{0,3\}$ in (B); dodeca vs icosa share only the top value $2\hat\mu'^2$ in (A) and nothing in (B). FT.44(2)'s splitting template acquires its multiplet form.
$(9)$ **Field-degree ledger.** Tetra/octa: $\mathbb Q$; cube: $\mathbb Q(\sqrt2)$; icosa: $\mathbb Q(\sqrt3)$; dodeca: $\mathbb Q(\cos\tfrac\pi{10})$, degree $4$, with $\sqrt5=8c^2-5$ its unique quadratic subfield (machine) — the requested four-field list $\{\mathbb Q,\mathbb Q(\sqrt2),\mathbb Q(\sqrt3),\mathbb Q(\sqrt5)\}$ is **insufficient for the dodecahedron**, exactly as FT.73(2)'s degree-$16$ compositum requires.
$(10)$ **FT.63(6) precision correction.** The dodecahedral quartic $x^4-8x^3+19x^2-12x+1$ has **four positive roots** (machine-isolated to width $2^{-60}$): $0.097886967410$, $0.824429495415$, $3.175570504585$, $3.902113032590$, realized by the weights $m\in\{1,19\},\{3,17\},\{7,13\},\{9,11\}$ respectively. FT.63(6)'s "$D(1),D(3)$ the two positive roots of the quartic" corrects to **the two smallest of its four positive roots**; patched in place (marker).

**Req.** Def-H.37(2), Def-H.38; Def-H.21, Def-H.23; FT.22, FT.32, FT.43, FT.44, FT.45, FT.47, FT.52, FT.54, FT.55, FT.60, FT.63; D2.9; CT2.5 (Part 2); CT0.7a (Part 1); Chebyshev recursion, de Moivre $\cos5t$, exact root isolation by bisection, minimal polynomials via the multiplication map [math; machine].

**Pf.**
$$
(1):\ k_f=K_S/F:\ (12,12,24,60,60)/(4,6,8,12,20)=(3,2,3,5,3)\ \checkmark;\qquad k=L\kappa_{\min}/2:\ \text{odd}\ L\to L,\ \text{even}\ L\to L/2
$$
$$
\Theta_R=4\pi:\ D(m)=2-2\cos(2m\pi)=0\ \forall m;\qquad\Theta_R=0:\ D\equiv0\ [\mathrm{FT.63}(4),(6)]
$$
$$
(2):\ D(m)=2-2T_m(\cos(\delta_v/2))\ [\text{Chebyshev recursion}\ T_{n+1}=2xT_n-T_{n-1},\ \text{integer coefficients}];\quad\cos(\delta_v/2)=(0,\tfrac{\sqrt2}2,\tfrac12,c,\tfrac{\sqrt3}2)
$$
$$
\text{base elements exact}:\ 16c^4-20c^2+5=0\ [\cos5t\ \text{at}\ t=\tfrac\pi{10}];\quad(\tfrac{\sqrt2}2)^2=\tfrac12;\quad(\tfrac{\sqrt3}2)^2=\tfrac34;\quad\text{root branch by sign/order}
$$
$$
\text{values}:\ \text{exact field arithmetic};\qquad\text{cross-check}:\ |D(m)-[2-2\sum_j(-1)^j(m\delta_v/2)^{2j}/(2j)!]|<10^{-45}\ \text{at 120 terms}\ [\text{machine}]
$$
$$
(3):\ D(m+P)=D(m)\iff\cos((m+P)\delta_v/2)=\cos(m\delta_v/2):\ P\delta_v/2=2\pi:\ P=4\pi/\delta_v;\qquad D(P-m)=D(m),\ D(-m)=D(m)
$$
$$
m\in[0,P/2]:\ m\delta_v/2\in[0,\pi]:\ \cos\ \text{strictly decreasing}\implies D\ \text{strictly increasing}:\ \min_{\ne0}=D(1)=D_S,\ \max=D(P/2)=4
$$
$$
\text{distinct count}=P/2+1;\qquad 4/D_{\mathrm{dodeca}}:\ \text{minpoly by the multiplication map on}\ \mathbb Q(c)\ [\text{machine}]
$$
$$
(4):\ k_f\delta_v=(3\pi,\pi,2\pi,\pi,\pi):\ \cos(k_f\delta_v/2)=(0,0,-1,0,0)\implies D(k_f)=(2,2,4,2,2)
$$
$$
(5a):\ \delta_v=\pi:\ D(m)=2-2\cos(m\pi/2):\ m\ \text{odd}\to2,\ m\equiv0(4)\to0,\ m\equiv2(4)\to4:\ k_f=3\ \text{odd weights only}\implies\text{constant}\ 2
$$
$$
(5b):\ k\ \text{even}\implies m=0\in\{k,k{-}2,\dots,-k\}:\ D(0)=0\ [\mathrm{FT.60}(5)]
$$
$$
(6),(7):\ \text{exact division in the solid's field};\quad\text{mass ratios}:\ r=\sqrt{q}:\ q\ \text{isolated exactly}\implies r\in(\sqrt a,\sqrt b)\ [\sqrt{}\ \text{monotone}];
$$
$$
\text{icosa (A)}:\ q=\tfrac{2}{2-\sqrt3}=2(2{+}\sqrt3)=4{+}2\sqrt3:\ \sqrt q=1{+}\sqrt3\ [(1{+}\sqrt3)^2=4{+}2\sqrt3\ \checkmark]
$$
$$
\text{icosa (B)}:\ q=\tfrac{2+\sqrt3}{2-\sqrt3}=(2{+}\sqrt3)^2=7{+}4\sqrt3:\ \sqrt q=2{+}\sqrt3\ \checkmark
$$
$$
\text{cube (B)}:\ \tfrac{2+\sqrt2}{2-\sqrt2}=3{+}2\sqrt2=(1{+}\sqrt2)^2\ \checkmark;\qquad(8),(9):\ \text{multiset comparison; field membership by construction}
$$
$$
(10):\ \text{sign-change scan on}\ \mathbb Q\ \text{at step}\ 1/500\ \text{over}\ [-1,6]\ \text{then bisection to}\ 2^{-60}:\ 4\ \text{brackets, all in}\ (0,\infty);\quad q(0..4)=(1,1,5,1,1)>0
$$
$$
\text{weight attribution}:\ D(m)=\text{root}\iff m\ \text{in the stated residue classes mod}\ 20\ [\text{machine}].\ \blacksquare
$$

**Phys.** Ask the five solids for their pole masses under the declared defect transfer, and the answer is a small, closed, exactly computable set of numbers — three values for the tetrahedron, five for the cube, eleven for the dodecahedron — all of them between zero and four times one unknown scale. Nothing in that set is large. The tetrahedron's multiplet does not split at all; the cube's even winding leaves one weight exactly massless; and the heaviest state of four of the five solids is the same number. So the Platonic defects do not generate hierarchy — they generate a bounded, near-degenerate spectrum, and the bound is a theorem about cones, not a limitation of the search.

---

---

### FT.78 — The orbit decompositions: tetrahedron exhaustive, cube symmetry-reduced

**Thm.** Under Def-H.28, at (S1)–(S4):
$(1)$ **Tetrahedron, exhaustive.** The $1230$ admissible configurations [FT.68(1)] form **$70$ orbits** under $\operatorname{Aut}=S_4$ ($|\operatorname{Aut}|=24$), with $\sum_{\mathcal O}\Omega_{\mathcal O}=1230$; orbits by $K$: $(1,1,5,13,23,21,6)$ for $K=0..6$; configuration counts by $K$ reproduce the cap row $(1,12,66,220,435,408,88)$ [FT.68(1)] exactly; $\Omega\in\{1,3,4,6,8,12,24\}$, every value dividing $24$.
$(2)$ **Tetrahedron cover sector: seven orbits total.** The $85$ bypass covers form $5$ orbits and the $16$ locked covers $2$ orbits:
$$
\begin{array}{c|cccccc}
\text{sector} & K & |\mathcal C| & \Omega & 4^{|\mathcal C|} & \text{signature (cycles shadowed)} & \text{type multiset}\\
\hline
\text{byp} & 0 & 0 & 1 & 1 & () & (0,0)^4\ \text{(vacuum)}\\
\text{byp} & 2 & 1 & 24 & 4 & () & (0,0),(0,1),(1,0),(1,1)\ \text{single thread}\\
\text{byp} & 4 & 2 & 24 & 16 & (2) & (1,0),(1,1)^2,(1,2)\\
\text{byp} & 4 & 2 & 24 & 16 & (2) & (0,1),(1,1)^2,(2,1)\\
\text{byp} & 4 & 2 & 12 & 16 & () & (0,2),(1,1)^2,(2,0)\ \text{double thread}\\
\hline
\text{lock} & 4 & 2 & 12 & 16 & (2,2) & \text{double-digon }(2,2)\text{ hub}\\
\text{lock} & 6 & 3 & 4 & 64 & (2,2,2) & K_{1,3}\ \text{star hub}
\end{array}
$$
—the two locked rows being exactly FT.69(5)'s minimal dissolution family ($12$) and the four $K_{1,3}$ triple-digon stars [FT.68(1)]. The single-centre orbit's size $24=Vd(d{-}1)$ is FT.69(2)'s closed form.
$(3)$ **Orbit-level amplitude identity (new).** The amplitude sum decomposes exactly over classes:
$$
\sum_{\mathcal O}\Omega_{\mathcal O}\,4^{|\mathcal C(\mathcal O)|}=Z^{\pm},
$$
machine-verified on both skeletons: tetrahedron $1057$ (bypass) and $448$ (locked) [FT.68(1)]; cube $1\,109\,313$ and $1\,150\,848$ [FT.68(3)]. Consequently the covering-polynomial coefficients are the $|\mathcal C|$-level *configuration* counts, and the orbit counts refine them: cube bypass $|\mathcal C|=0..4\Rightarrow(1,1,19,57,88)$ orbits over $(1,48,648,2672,3624)$ configurations; locked $|\mathcal C|=2..6\Rightarrow(1,18,71,7,1)$ over $(24,728,3192,264,4)$.
$(4)$ **Cube, symmetry-reduced.** Cap row $(1,24,276,2024,10506,40296,115796,247704,383913,408464,270096,91392,9600)$, total $1\,580\,092$ configurations with $K\le12$ forced [FT.68(3)]; cap-aware Burnside over $|\operatorname{Aut}|=48$ gives orbits by $K$ $(1,1,11,49,250,863,2509,5211,8163,8571,5768,1922,245)$, total $33\,564>10^4$ — the bounded rule is observed, so full configuration enumeration is *not* attempted. The **cover sector is enumerated explicitly** (it is small): the $11\,205$ covers ($6993$ bypass $+\,4212$ locked, two independent enumerators agreeing [FT.69(2)]) form **$264$ orbits** ($166$ bypass, $98$ locked), $\sum\Omega=11\,205$, $\Omega\mid48$ throughout, with $\Omega$-histogram $\{1{:}1,\ 4{:}1,\ 8{:}1,\ 12{:}4,\ 16{:}2,\ 24{:}47,\ 48{:}208\}$ — the $208$ free orbits are the generic case, so the twenty most populated classes are all free orbits ($\Omega=48$) and are distinguished only by signature: one at $|\mathcal C|=1$ (the single thread), eight at $|\mathcal C|=2$ (four cycle-free, four shadowing one digon), eleven at $|\mathcal C|=3$. **Independent cross-validation:** explicit canonical-form enumeration of every admissible configuration with $K\le5$ ($53\,127$ of them) reproduces the Burnside row $(1,1,11,49,250,863)$ exactly — two methods, same numbers.
$(5)$ **Signatures.** Covers shadow only **even** cycles, orbit by orbit [FT.69(3)(i) recovered at class level]: tetrahedron covers contain digons only ($84$ instances, $\delta h=2$ [D0.6]); cube covers contain digons and directed $4$-cycles ($14\,832$ instances, $\delta h\in\{2,4\}$), with $10$ distinct cycle contents $\{(),(2),(2,2),(4),(2,2,2),(2,4),(2,2,2,2),(2,2,4),(2,2,2,2,2),(2,2,2,2,2,2)\}$ and no odd cycle anywhere. The signature $(K,\text{cycles},|\mathcal C|)$ is **not a complete class invariant**: $7$ tetrahedron cover orbits carry only $6$ signatures, $264$ cube cover orbits only $21$ — the completing datum is the vertex-type multiset (clause (2)'s last column).
$(6)$ **Charge-conjugation chirality of the cover sector (new).** Global orientation reversal $R\mapsto R^{\mathrm T}=\{(b,a):(a,b)\in R\}$ is an involution of the pattern space that is **not** in $\operatorname{Aut}(\Gamma)$ (it is induced by no vertex permutation). It pairs cover classes: the $48$ bypass dissolved-digon covers of FT.69(4) split into **two $\Omega=24$ orbits exchanged by reversal** (representatives with type multisets $(1,0),(1,1)^2,(1,2)$ and $(0,1),(1,1)^2,(2,1)$ — transposes of each other; machine: the reversal of one representative is canonical in the other orbit). This is the pattern-level form of charge conjugation [D2.6]. **Both mass ansätze are reversal-invariant** ($K$, $\Omega$ and $4^{|\mathcal C|}$ are), so the chirality is invisible to the mass spectrum; reading it requires a C-odd ledger of FT.40's $q_{\mathrm{core}}$ species.

**Req.** Def-H.25, Def-H.26, Def-H.28; FT.67, FT.68, FT.69, FT.70, FT.71; FT.27, FT.40; A4, A8; D0.6, D0.8, D2.6; CT0.11, CT0.13, CT0.14 (Part 1); CT1.20 (Part 2); orbit–stabilizer, Burnside's lemma, canonical-form enumeration [math; machine].

**Pf.**
$$
(1):\ \text{canonical form}=\min\ \text{over the}\ 24\ \text{edge-permutations};\quad\text{admissibility and}\ K\ \text{are invariant}\implies\text{orbits lie inside the set}
$$
$$
\sum_{\mathcal O}\Omega_{\mathcal O}=1230\ [\text{machine}];\qquad\Omega\cdot|\operatorname{Stab}|=24\implies\Omega\mid24;\qquad\text{cap row}:\ \text{CT0.11 counting per}\ K
$$
$$
(2):\ \text{explicit enumeration of the}\ 101\ \text{covers}\ (85+16);\quad|\mathcal C|=1:\ \Omega=24=Vd(d{-}1)=4\cdot3\cdot2\ [\mathrm{FT.69}(2)]
$$
$$
\text{locked rows}:\ \text{double-digon}(2,2)\ \text{hub}\ (12=4\binom32),\ K_{1,3}\ \text{star}\ (4,\ \operatorname{Stab}=S_3)\ [\mathrm{FT.69}(5)]
$$
$$
(3):\ Z^{\pm}=\sum_{R\ \mathrm{cover}}4^{|\mathcal C(R)|}\ [\mathrm{FT.67}(2)\ \text{at (S1)}]=\sum_{\mathcal O}\ \sum_{R\in\mathcal O}4^{|\mathcal C|}=\sum_{\mathcal O}\Omega_{\mathcal O}4^{|\mathcal C(\mathcal O)|}\quad[|\mathcal C|\ \text{class-constant}]
$$
$$
(4):\ \text{Burnside}:\ \#\text{orbits}_K=\tfrac1{48}\sum_{p}\operatorname{fix}_K(p),\ \operatorname{fix}_K\ \text{by orbit-subset enumeration under the cap};\quad\text{covering polys}:\ \text{DP}=\text{backtracking}\ [\mathrm{FT.69}(2)]
$$
$$
\text{cross-validation}:\ K\le5\ \text{explicit canonical forms}=(1,1,11,49,250,863)=\text{Burnside row}\ [\text{machine}]
$$
$$
(5):\ \text{canonical cycle enumeration per representative};\ \text{evenness}:\ \mathrm{FT.69}(3)(i);\qquad\text{incompleteness}:\ \text{two classes share}(4,(2),2)\ \text{and differ in type multiset}
$$
$$
(6):\ R^{\mathrm T}\ \text{preserves}\ K,\ \text{types}^{\mathrm T},\ |\mathcal C|,\ \text{cover status};\quad R^{\mathrm T}=p(R)\ \forall p\in\operatorname{Aut}\ \text{would force}\ \Omega\ \text{to merge}:\ \text{the two orbits are distinct}\implies\notin\operatorname{Aut}
$$
$$
\text{reversal maps one}\ \Omega{=}24\ \text{orbit onto the other}\ [\text{machine: canonical forms agree}].\ \blacksquare
$$

**Phys.** Ask the flickering gas how many distinct shapes it takes, and the answer is startlingly small: the tetrahedron's $1230$ configurations are $70$ shapes, and the whole of its amplitude-carrying cover content is *seven* — one vacuum, one single thread, three two-centre networks, and the two locked hub families. The cube's eleven thousand covers are $264$ shapes over seven mass levels. Nothing here is random; the shapes come in chirality pairs related by reversing every arrow, a distinction the mass reads cannot see. The degeneracies are where the complexity lives, and degeneracy is not hierarchy.

---

---

### FT.81 — Particle-content census (audit pass A)

**Thm.** Under Def-H.29, with the SM field content external and marked:
$(1)$ **The census.** $24$ entries, classified with their supplying tags or no-goes:
$$
\begin{array}{lll}
\textbf{PRESENT}\ (10) & \textbf{PARTIAL}\ (6) & \textbf{ABSENT}\ (8)\\
\hline
\text{gluons }(8) & \text{Higgs doublet} & \text{neutrino}\\
W^\pm & \text{quark triplet} & \text{generations/flavour}\\
Z\ (\text{mixture}) & \text{lepton doublet} & \text{CKM/PMNS, CP phase}\\
\text{photon} & \text{charged-lepton singlet} & \text{Yukawa sector}\\
\text{confinement/singlet} & \text{observable charge} & \text{chirality/Weyl}\\
\theta_W,\ e\ (\text{relations}) & \text{EW VEV} & \text{gauge anomalies}\\
G_N\ (\text{beyond SM}) & & \Lambda_{\mathrm{QCD}}\\
\text{spin ladder} & & \text{spin-statistics}\\
\text{fermion/boson content} & & \\
D^\pm\ \text{dark (beyond SM)} & &
\end{array}
$$
**Completeness fraction $=\dfrac{10+\frac12\cdot6}{24}=\dfrac{13}{24}=0.5416\overline6$.** Sub-censuses: **gauge species $4/4$ PRESENT** (as aspect blocks and reads, *not* as gauged chiral couplings); **fermion sector $8$ entries $\to0$ present, $3$ partial, $5$ absent $=0.1875$**.
$(2)$ **The SM side, machine-verified in exact rationals** (external data): one generation $=15$ left-handed Weyl fields $=6+3+3+2+1$ ($(3,2)_{1/6}$, $(\bar3,1)_{-2/3}$, $(\bar3,1)_{1/3}$, $(1,2)_{-1/2}$, $(1,1)_{1}$), $45$ over three generations; $12$ gauge bosons ($8+3+1$) and $4$ real Higgs dof; every anomaly sum vanishes exactly — $\sum Y=0$, $\sum Y^3=0$, $[\mathrm{SU}(3)]^2\mathrm U(1):\ \sum Y\,d(\mathrm{SU}(2))\,T(3)=0$, $[\mathrm{SU}(2)]^2\mathrm U(1):\ \sum Y\,d(\mathrm{SU}(3))\,T(2)=0$, $[\mathrm{SU}(3)]^3:\ 2A(3)+2A(\bar3)=0$, $[\mathrm{SU}(2)]^3\equiv0$.
$(3)$ **The charge lattice, exactly.** The SM field charges $Q=T_3+Y$ span $\{0,\pm\tfrac13,\pm\tfrac23,\pm1\}$; the corpus read is ternary, $q_{\mathrm{EM}}\in\{-1,0,+1\}$ with all three attained [D3.4, EM.9, P2]. The two sets are related by **confinement projection, machine-verified**: the CT3.17/D3.9 singlets of $u,d$ — $\varepsilon_{ijk}$ baryons and $\delta^i{}_j$ mesons — carry *integer* charge, and the meson charge set is **exactly** $\{-1,0,+1\}$, the corpus read; the baryon set is $\{-1,0,1,2\}$, so the $|q|=2$ state exceeds a single chain's ternary read, and the confined thirds are unreadable by construction [CT3.22: colour is $\neg$observable as end-charge]. Verdict: **charge quantization to integers is reproduced for the observable sector; the per-chain read is $3$-valued where the SM's observable lattice is $\mathbb Z$** (a multi-chain additive read would be needed for $|q|\ge2$; FT.41(a) counts $N_{\mathrm{charge}}=2$ end registers).
$(4)$ **Anomalies are not poseable.** Every anomaly above is a constraint on *chiral* hypercharge assignments. The corpus has no chiral projector, no Weyl symbol and no hypercharge-assignment read ($Y$ appears only as the abstract generator with three realizations [EW.8] and in the mixing [D3.10/EW.24]), so the cancellation question cannot be posed — a structural absence downstream of chirality, not a numerical failure.
$(5)$ **Inventory facts (machine-checked over the frozen Parts 1–2).** Count $0$ for: Yukawa, neutrino, Weyl, CKM, PMNS, left-handed, right-handed, $\gamma_5$, flavour, flavor, black hole, spin-statistics, $P_L$, $P_R$, $\bar\psi$, generation structure, quark mixing, lepton number. Present: $\theta_W$ ($71$), $T_a$ ($51$), $h_0$ ($38$), gluon ($22$), $f_{abc}$ ($14$), $\varepsilon_{ijk}$ ($12$), $m_H$ ($11$), baryon ($11$), $W^\pm$ ($10$), meson ($6$), hypercharge ($4$), chirality ($2$). The two "chirality" occurrences are both inside D2.6's orientation-reversal clause ($\omega$: chirality $\mapsto-$chirality) — vocabulary without a projector. The four "generation" occurrences in D/F are the algebraic sense ("mass generation", "$\delta$/$\varepsilon$ generation"), machine-checked to be non-flavour.

**Req.** Def-H.29; D1.5, D2.6, D3.4, D3.7, D3.8, D3.9, D3.10, D4.1–D4.3; CT0.9, CT0.12, CT0.13, CT0.14 (Part 1); CT2.9, CT1.25 (Part 2); CT3.15, CT3.17, CT3.18, CT3.20, CT3.21, CT3.22 (Part 2); CT4.1, CT4.4, CT4.5 (Part 2); EM.9, EM.20 (Part 2); EW.8, EW.13, EW.20, EW.24, EW.27, EW.32, EW.33, EW.35 (Part 2); FT.19, FT.20, FT.26, FT.27, FT.30, FT.34, FT.41, FT.52, FT.55, FT.57, FT.60, FT.71, FT.76, FT.79, FT.80; P1–P5; A §0.2, §0.3; external SM field content (marked); exact rational arithmetic, integer inventory scan [machine].

**Pf.**
$$
(1):\ \text{per-entry citation table}\ [\text{machine-checked: every PRESENT row resolves to the cited tag; every ABSENT row to a scan count or a no-go}]
$$
$$
\text{fraction}:\ (10+3)/24=13/24;\qquad\text{gauge sub-census}\ 4/4;\qquad\text{fermion sub-census}\ (0+\tfrac32)/8=3/16
$$
$$
(2):\ 6+3+3+2+1=15;\quad15\cdot3=45;\quad8+3+1=12;\quad2\cdot2=4;\qquad\text{anomaly sums}:\ \text{exact Fractions}
$$
$$
\textstyle\sum Y=6\cdot\tfrac16+3(-\tfrac23)+3\cdot\tfrac13+2(-\tfrac12)+1=1-2+1-1+1=0;\qquad\sum Y^3=\tfrac1{36}-\tfrac89+\tfrac19-\tfrac14+1=0
$$
$$
[\mathrm{SU}(3)]^2\mathrm U(1):\ \tfrac12\bigl(2\cdot\tfrac16-\tfrac23+\tfrac13\bigr)=0;\qquad[\mathrm{SU}(2)]^2\mathrm U(1):\ \tfrac12\bigl(3\cdot\tfrac16-\tfrac12\bigr)=0;\qquad[\mathrm{SU}(3)]^3:\ 2\cdot\tfrac12-2\cdot\tfrac12=0
$$
$$
(3):\ Q=T_3+Y\ \text{over the five multiplets}\implies\{0,\pm\tfrac13,\pm\tfrac23,\pm1\};\qquad q_{\mathrm{EM}}=\tfrac12(\sigma_s-\sigma_t)\in\{-1,0,1\}\ [\mathrm{EM.9}]
$$
$$
\text{mesons}:\ \{u\bar u,u\bar d,d\bar u,d\bar d\}\to\{0,1,-1,0\}=\{-1,0,1\}\ \checkmark;\qquad\text{baryons}:\ \{uuu,uud,udd,ddd\}\to\{2,1,0,-1\}
$$
$$
\text{integrality}:\ \tfrac23-\tfrac13=\tfrac13\notin\mathbb Z\ \text{per quark},\ \text{but}\ \varepsilon/\delta\ \text{singlets sum to}\ \mathbb Z\ [\mathrm{CT3.17},\mathrm{D3.9};\ \text{exhaustive}]
$$
$$
(4):\ \text{anomaly}\equiv\text{chiral constraint};\quad\neg\exists\ \text{projector/Weyl symbol in Parts 1–2}\ [\text{scan}]\implies\neg\exists\ \text{the question}
$$
$$
(5):\ \text{exact substring counts over the seven frozen documents}\ [\text{machine}].\ \blacksquare
$$

**Phys.** Line up the Standard Model's inventory against what this corpus can read, and the pattern is not random. Everything about *forces* is there: eight gluons with a closing eight-dimensional algebra, three weak directions that mix into a massive $Z$ and an exactly massless photon, a scalar with a background and a mass formula, a confinement rule that makes colour unreadable and thereby makes observable charge integral — the meson charges come out as precisely the three values the ledger can register. Everything about *matter* is missing: no handedness, no Weyl spinor, no neutrino, no flavours, no mixing, no Yukawa couplings, and no second scale for any of them to live on. The corpus is a theory of the gauge skeleton with the chiral flesh left undeclared — and the anomalies that make the SM's flesh consistent cannot even be written down here.

---

---

### FT.83 — The rung emergence ledger (audit pass C): derived, declared, open

**Thm.** Under Def-H.29, per rung $n$:
$(1)$ **The ladder is a theorem, not a picture.** $\mathcal A(0)=\{J\}$; $\mathcal A(1)=\{J,G,W,H,D^+\}$; $\mathcal A(2)=\mathcal A(1)\cup\{\mathrm{EM}\}$; $\mathcal A(3)=\mathcal A(2)\cup\{\mathrm{strong}\}$; $\mathcal A(n\ge4)=\mathcal A(3)\cup\{D^-\}$, with a strict mask flag $\dim\mathcal K_n=(6,16,17,25)$ [CT0.13, CT0.14 — both with Pfs]. The admissibility ceiling is derived: $D_{\mathrm{tick}}(n)=2^{n+1}\le C_{\mathrm{cap}}=16\iff n\le3$, with saturation at $n=3$ [CT0.5, CT0.11, P2's $n_{\max}=3$].
$(2)$ **Rung-by-rung status.**
$$
\begin{array}{c|l|l}
n & \text{what becomes active/trackable} & \text{status}\\
\hline
0 & J^\pm\ \text{seals only};\ \dim\mathcal K_0=6 & \textbf{derived}\ [\mathrm{CT0.13}/\mathrm{CT0.7}]\\
1 & G(5)\ \text{spin-2 shear},\ W(3),\ H(1),\ D^+(1);\ \dim\mathcal K_1=16 & \textbf{derived}\ [\mathrm{CT0.12}/\mathrm{CT0.13}];\ \text{the "pretime force set"}\\
2 & +\ \mathrm{EM};\ \alpha_{\mathrm{EM}}=\pi;\ q_{\mathrm{EM}}\ \text{readable on open chains} & \textbf{derived}\ [\mathrm{CT0.13},\mathrm{EM.9},\mathrm{EM.20}]\ \text{under Comm-min}+\text{Eff (declared premises)}\\
3 & +\ \text{strong};\ N_{\text{colour}}=3,\ N_{\mathrm{gluon}}=8;\ \text{sealing}=\text{confinement};\ \text{mass reads} & \textbf{derived}\ [\mathrm{CT3.20},\mathrm{CT3.13},\mathrm{CT3.22},\mathrm{EW.20}/\mathrm{EW.33}]\\
\ge4 & D^-\ \text{absorption}\ O(n)=2^{n+1}{-}16,\ w=0\ \text{dust},\ \text{locking};\ \neg\exists\ \text{gauge structure} & \textbf{derived as a no-go}\ [\mathrm{CT0.11},\mathrm{CT4.1},\mathrm{CT4.4},\mathrm{CT4.5},\mathrm{FT.59}]
\end{array}
$$
$(3)$ **What is *not* derived at any rung.** (a) The proposal's "$n=1$: gravity, weak, Higgs, Dark$^+$, Janus" is exactly $\mathcal A(1)$ and is derived — but the *Higgs* entry is the scalar aspect $F_H$ with a P4-free background $h_0$ [EW.13, EW.20, P4], and its mass is "configuration data" [EW.27]: the mechanism is derived, the scale is not. (b) The proposal's "$n=2$: EM $+$ lepton structure" is **half derived**: EM is a theorem; "lepton structure" has no read at any rung (no lepton species, no chirality [FT.81(5)]). (c) "$n=3$: colour $+$ quarks $+$ the baryon edge budget" is derived — $\varepsilon_{ijk}$ sealing of three fundamentals [CT3.15/CT3.17/D3.9], the $2$s-and-$3$s partition rule [FT.34(5)], and $N=1$ impossibility [FT.27] — but "quark" in the corpus is D3.8's *bound fermionic loop with a triplet attachment*, i.e. a topological definition with no flavour and no chirality. (d) "$n\ge4$: lock / black-hole-matter cascade": the locking and absorption side is derived (CT4.1/CT4.2/CT4.5, $w=0$ dust, retained-and-inaccessible [D1.11]); **"black hole" has no corpus referent at all** (inventory count $0$), so the cascade reading is an external gloss, recorded and not adopted.
$(4)$ **Parameter census.** P4 declares $8$ independent internal configuration parameters $(g,g',h_0,c_W,\Lambda,\varkappa,\beta,\alpha_\Omega)$ with $6$ functionally dependent members $(\theta_W,e,\mu_\star^2,m_W,m_Z,m_H)$; P1/A §0.3 admit exactly **one** free dimensionful scale $\mathfrak h$; P3 names $G_N=\mathfrak h^2/(4\ln2)$, $\kappa^2=8\pi G_N$ for external comparison only; P5 forbids identifying any quantity with a measured constant. The SM's $19$ parameters (external count: $3$ gauge $+\,1$ VEV $+\,9$ Yukawa $+\,4$ CKM $+\,1$ $\theta_{\mathrm{QCD}}+\,1$ Higgs self-coupling) contain **$13$ flavour parameters, which alone exceed the corpus's $8$** — and the corpus's $8$ are declared *configuration* data, not constants, so no parameter-by-parameter map exists even in principle without extending P4.

**Req.** Def-H.29; D0.8, D0.9, D1.2, D1.11, D3.1, D3.2, D4.1–D4.3; CT0.5–CT0.14 (Part 1); CT1.20, CT1.25, CT2.9 (Part 2); CT3.15, CT3.17, CT3.20, CT3.22 (Part 2); CT4.1–CT4.5 (Part 2); EM.9, EM.20 (Part 2); EW.13, EW.20, EW.24, EW.27, EW.33, EW.35 (Part 2); FT.20, FT.27, FT.30, FT.34, FT.59; A §0.3, P1–P5; external SM parameter count (marked) [machine].

**Pf.**
$$
(1):\ \mathrm{CT0.13}\ \text{Pf by rung induction on}\ \vee^2/\wedge^2\ \text{population and}\ \mathrm{CT0.7}'\text{s}\ S\text{-grading};\qquad\mathrm{CT0.14}:\ \mathcal K_n=\bigoplus_{A\in\mathcal A(n)}\mathcal K^{(A)}
$$
$$
2^{n+1}\le16\iff n\le3\ [\mathrm{CT0.5},\mathrm{CT0.11}];\qquad O(n)=2^{n+1}-16\implies(16,48)\ \text{at}\ n=4,5\ [\mathrm{CT4.1}]
$$
$$
(2):\ \text{each row's citations are theorems with Pfs in B–G};\qquad n\ge4:\ \mathrm{CT4.4}\ \text{is a non-existence theorem}
$$
$$
(3):\ \text{inventory scans}\ [\mathrm{FT.81}(5)];\qquad\text{EW.27}:\ m_H^2=\text{configuration data}\ [\mathrm{P4}]
$$
$$
(4):\ |P4_{\mathrm{core}}|=8;\quad19=3+1+9+4+1+1;\quad9+4=13>8;\qquad\text{one scale}\ [\mathrm{P1},\text{A}\ \S0.3].\ \blacksquare
$$

**Phys.** The rung ladder is the part of this corpus that behaves most like a generative spine, and it is derived rather than asserted: at one crystallized edge per vertex only seals exist; add a second and geometry, the weak block, a scalar and uniform dark come online; at three the electromagnetic read becomes available with a phase coefficient of exactly $\pi$; at four edges the vertex oversubscribes, the information is absorbed and locked, and — provably — no gauge structure of any kind survives there. What the ladder never generates is matter's handedness or its flavours: those are not at any rung, and no rung's activation set contains them.

---

---

### FT.84 — The deficit table and the two-ceiling synthesis (audit pass D)

**Thm.** Under Def-H.29 and FT.81–FT.83:
$(1)$ **The ranked deficit list** (load-bearing order; class: (i) missing declaration, (ii) structural no-go already proven, (iii) genuinely open):
$$
\begin{array}{c|l|l|l}
\# & \text{deficit} & \text{corpus status} & \text{class}\\
\hline
1 & \text{chirality (Weyl/projector)} & \text{no read; }\omega\text{-vocabulary only [D2.6]} & \text{(iii) open — root deficit}\\
2 & \text{Yukawa sector / fermion masses} & \text{no read; no P4 parameter} & \text{(iii) open, constrained by P1/P4}\\
3 & \text{three generations / flavour} & \text{no read } & \text{(iii) open}\\
4 & \text{CKM/PMNS mixing, CP phase} & \text{no read} & \text{(iii) open; needs 1 and 3}\\
5 & \text{gauge-anomaly structure} & \text{not poseable} & \text{(ii) blocked by 1}\\
6 & \text{neutrino species/mass/mixing} & \text{no read} & \text{(iii) open; needs 1 and 3}\\
7 & \Lambda_{\mathrm{QCD}}\ \text{/ any second scale} & \text{no read} & \text{(ii) no-go [A §0.3, P1, P5]}\\
8 & \text{Higgs as }4\text{ real dof} & \dim F_H=1 & \text{(ii) no-go [CT0.12 allocation]}\\
9 & \text{fractional confined charges} & \text{ternary read} & \text{(ii) partial no-go [EM.9, CT3.22]}\\
10 & |q|=2\ \text{observable states} & \text{single-chain read} & \text{(iii) open; needs a multi-chain read}\\
11 & \text{spin-statistics} & \text{external} & \text{(iii) open [FT.80(5)]}\\
12 & \text{SM masses (any species)} & \text{two ceilings proven} & \text{(ii) no-go [FT.76(3), FT.79(2)]}
\end{array}
$$
$5$ structural no-goes or blocked items (each with a cited no-go), $7$ open. Deficit $1$ is the root of $4,5,6$ and $11$; deficits $7$–$9$ and $12$ are derived impossibilities within the current inventory.
$(2)$ **The two-ceiling synthesis.** Both mass audits failed for the *same* structural reason at different loci: the pole side is bounded because a cone defect is an angle ($m^2_{\mathrm{pole}}\in[0,4\hat\mu'^2]$, widest ratio $6.39$ [FT.76(3)]), and the cover side is bounded because a mass counted in crystallized edges is bounded by the cap census ($K\le3V/2$, $|\mathcal C|\le3V/4$, widest ratio $6$ on the cube [FT.79(2)]). Deficit $2$ names the deeper cause: **there is no Yukawa sector**, so no mechanism in the inventory generates fermion mass at all — the two ceilings bound the *reads that exist*, and the SM's masses live in a sector the corpus does not contain. The mass negatives of FT.77/FT.79 are consequences of deficit $2$, not evidence against the reads themselves.
$(3)$ **What is reproduced, stated positively** (each with its citation): the gauge block dimensions and their sum $8+3+1=12$ [CT0.14, CT0.12, CT1.1]; $\mathfrak{su}(2)$ and $\mathfrak{su}(3)$ closure with correct roots, normalizations and no ninth gluon [FT.82(2)–(3); CT3.8, CT3.13]; the derived colour count $3$ [CT3.20]; the full electroweak mixing structure with an exactly massless photon and $m_W=m_Z\cos\theta_W$, $1/e^2=1/g^2+1/g'^2$ [EW.20/23/24/35]; the vev's doublet-and-singlet quantum numbers [EW.20, EW.32]; confinement as a theorem with norm-zero isolated triplets [CT3.22, CT3.18, FT.19]; the baryon/meson sealing grammar [D3.9, CT3.15, CT3.17, FT.34(5)]; integer observable charge with the meson set exactly equal to the ternary read [EM.9, D3.4, FT.81(3)]; the spin ladder $j=|k|/2$ with $\mathrm{Sym}^k$ carriers [CT0.7a, EW.32, FT.52–FT.60, Def-H.38]; a derived Newton constant from the single scale [P3, CT2.9]; the fermion/boson *content-type* split [D1.5, Def-H.4]; and, beyond the SM, a dark sector with exact equations of state [D4.1–D4.3, CT1.25, CT4.1, CT4.5, FT.71].
$(4)$ **Verdict.** The corpus is **not** a Standard Model completion and does not claim to be: it is a derivation of the gauge-and-geometry skeleton from one scale and sixteen registers, with the chiral matter sector, the flavour sector and every dimensionful mass scale left outside the inventory. Its completeness fraction on the audited entry list is $13/24$, concentrated as $4/4$ on gauge species and $0.19$ on the fermion sector. No identification is made; Open Gaps 5/12 are unchanged and now carry a sharper form: *the mass question is not open but blocked from two sides (deficit $2$ above, ceilings below), while the gauge question is substantially answered.*
$(5)$ **Consequences.** (a) Any further mass-read search must first extend P4 with a flavour/Yukawa sector or accept that fermion masses have no read — searching for the SM hierarchy inside the existing reads is exhausted by FT.77/FT.79 and this clause. (b) The large-$V$ route of FT.79(2) is now demoted: even at $V\ge1200$ the resulting ladder would be an *even-integer* spectrum with no chirality and no flavour, so it could match a hierarchy's *range* and still not its *structure*. (c) The highest-value open direction is deficit $1$: a chirality read would unblock $4,5,6,11$ at once, and D2.6's $\omega$-action is the only existing hook — whether $\omega$ (or the FT.78(6) cover chirality) can be promoted from vocabulary to a projector is a well-posed question with no answer in the current inventory.

**Req.** Def-H.29; FT.11, FT.12, FT.19, FT.20, FT.26, FT.27, FT.30, FT.34, FT.41, FT.52–FT.60, FT.71, FT.76–FT.83; A §0.2, §0.3; D1.5, D2.6, D3.4, D3.9, D4.1–D4.3; CT0.11–CT0.14 (Part 1); CT2.9, CT3.15, CT3.17, CT3.18, CT3.20, CT3.22 (**C/F**); CT4.1, CT4.4, CT4.5 (Part 2); EM.9, EM.20 (Part 2); EW.8, EW.13, EW.20, EW.23, EW.24, EW.27, EW.32, EW.33, EW.35 (Part 2); P1–P5, Def-H.38; Open Gaps 5/7/12/13/16; external SM parameter and hierarchy data (marked) [machine].

**Pf.**
$$
(1):\ \text{each row's class follows from its cited tag}:\ \text{(ii) rows cite a theorem of non-existence or an allocation argument}
$$
$$
\text{(iii) rows cite an inventory scan}\ [\mathrm{FT.81}(5)]\ \text{plus the absence of any blocking theorem};\qquad1\Rightarrow4,5,6,11:\ \text{each requires a chiral read}
$$
$$
(2):\ \mathrm{FT.76}(3):\ m^2_{\mathrm{pole}}\le4\hat\mu'^2,\ \max\ \text{ratio}\ \sqrt{4/D_{\mathrm{dodeca}}}=6.3925;\qquad\mathrm{FT.79}(2):\ K=2|\mathcal C|\le3V/2\implies\max\ \text{ratio}\ 6\ (V=8)
$$
$$
\text{deficit}\ 2:\ \text{Yukawa count}\ 0\ [\text{scan}]\implies\neg\exists\ \text{fermion-mass mechanism};\qquad\text{the ceilings bound existing reads, not the SM's sector}
$$
$$
(3):\ \text{conjunction of the cited tags, each machine-verified in FT.81–FT.83};\qquad(4):\ (1)+(3)\ \text{with}\ 13/24
$$
$$
(5a):\ \mathrm{FT.77}(2),\ \mathrm{FT.79}(4)\ \text{exhaustive audits};\qquad(5b):\ \text{even-integer ladder}\ [\mathrm{FT.79}(1)];\qquad(5c):\ \mathrm{D2.6},\ \mathrm{FT.78}(6).\ \blacksquare
$$

**Phys.** Asked whether it contains the Standard Model, the corpus answers with a clean split that no amount of mass-fitting would have revealed. The forces are there: eight gluons in an algebra that closes with the right roots, three weak generators whose mixture leaves one combination exactly massless, a mixing angle and an electric coupling tied together by identities rather than fits, a confinement rule that turns fractional quarks into integer-charge mesons and baryons, and gravity's constant fixed by the single scale. The matter is not: nothing is left- or right-handed, nothing comes in flavours, nothing mixes, and no second scale exists for any of it. That is why the two mass audits failed the way they did — they were reading masses out of registers that hold geometry and combinatorics, in a document with no Yukawa sector at all. The honest summary is not "the corpus fails the Standard Model" but "it derives the gauge skeleton and leaves the chiral matter sector undeclared", with one hook — the orientation-reversal involution — where a chirality read might someday be hung.

---

---

---

### FT.96 — The reversal-chirality census of the cover sector

**Thm.** Under Def-H.28, at (S1)–(S4):
$(1)$ **Rename (premise correction).** "$S$-parity of a cover class" is undefined: CT1.1's $S$ acts on the pair register $\mathfrak H(\mathbb C^4)$ (force blocks), not on crystallization patterns. The native class-level chirality is FT.78(6)'s **reversal involution** $R\mapsto R^{\mathrm T}$ — the pattern-level charge conjugation [D2.6], induced by no vertex permutation ($\notin\operatorname{Aut}\Gamma$). E1–E3 are executed for this invariant; the word "bias" has no numeric referent and is dropped.
$(2)$ **Tetrahedron (re-derived, two enumerators).** The $101$ covers form $7$ $\operatorname{Aut}$-classes ($5$ bypass $+2$ locked; fresh enumeration matching the stored census orbit-by-orbit); under reversal: **$5$ self-conjugate $+1$ exchanged pair $\to6$ reversal classes**. The exchanged pair is exactly FT.78(6)'s: the two $\Omega=24$ dissolved-digon classes with component-transposed type multisets $\bigl((1,0),(1,1)^2,(1,2)\bigr)\leftrightarrow\bigl((0,1),(1,1)^2,(2,1)\bigr)$.
$(3)$ **Cube (new, exhaustive on the cover sector).** The $11\,205$ covers form $264$ classes ($166$ bypass $+98$ locked; $Z$-anchors $1\,109\,313/1\,150\,848$ and $\sum\Omega=11\,205$ re-verified); under reversal:
$$
264\ \text{classes}\ =\ 42\ \text{self-conjugate}\ +\ 111\ \text{exchanged pairs}\ \longrightarrow\ 153\ \text{reversal classes},
$$
by sector: bypass $26+2\cdot70=166$, locked $16+2\cdot41=98$; the per-$(\mathrm{sector},K,|\mathcal C|)$ distribution is recorded in the suite output. Every exchanged pair is chirality-blind on all nine stored fields ($K,|\mathcal C|,\Omega,\mathrm{amp},\mathrm{locked},\mathrm{norm\ weight},k_{\max},\mathrm{maskdim},\mathrm{cycles}$) — FT.78(6)'s ansatz-invariance at full census scale.
$(4)$ **E3: no dominant handedness is labelable.** Pair members are indistinguishable by every declared read (clause (3)); a label would require a $C$-odd ledger — FT.78(6)'s own conclusion — and FT.87(8)'s $\operatorname{sign}(k)$ applies to materialized chains, which covers do not carry [FT.80(6)]. Classes are exactly: self-conjugate ($C$-even by construction) or members of an *unordered* pair. "Left-handed dominant / right-handed dominant" has no referent.
$(5)$ **E4: negative.** The reversal invariant takes exactly **two** values (self / paired) on both skeletons — not three; the exact counts are $6$ (tetra) and $153$ (cube) reversal classes. "Three generations $=$ three distinct $S$-parity bias classes" fails at the invariant level ($2\ne3$), and any generation reading is barred regardless [F2; FT.90(6): generations are a missing label, not a capacity limit].

**Req.** Def-H.25, Def-H.28; FT.67, FT.68, FT.69, FT.78(6), FT.79, FT.80, FT.87(8), FT.90(6), FT.95(3); D2.6; two enumerators (fresh backtracking vs stored census), exact canonical forms under $\operatorname{Aut}$ [math; machine].

**Pf.**
$$
(2):\ \text{fresh enumeration}=101\to7\ \text{classes};\qquad\text{stored rows matched field-by-field}\ [\text{machine}]
$$
$$
(3):\ \text{canonical form}=\min_{p\in\operatorname{Aut}}\ \text{sorted edge list of}\ p(R^{\mathrm T}):\ 42\ \text{fixed},\ 111\ \text{2-cycles};\qquad 42+2\cdot111=264\ \checkmark
$$
$$
(4),(5):\ \text{clause}\ (3)\text{'s field identities};\qquad\#\{\text{invariant values}\}=2\ \blacksquare
$$

**Phys.** Turn every arrow in the gas around and ask what changed. On the tetrahedron, one pair of shapes trades places and five look at themselves in the mirror; on the cube, a hundred eleven pairs dance and forty-two stand still — a hundred fifty-three reversal classes under the two hundred sixty-four. Nothing that feeds a mass moved anywhere: the mirror pairs are identical in every count the corpus can read. The covers come in handed pairs, and the hands are unnamed — not because the census is incomplete, but because no declared read has ever told left from right. That is the shape of the chirality absence at the census level, and it is now counted exactly.

---

---

### FT.98 — The polygon form factors: exact census, saturating growth, fifth negative

**Thm.** On the bidirectional cycles $C_n$, $n=3..10$ (literal domain, (S1)–(S4)):
$(1)$ **Census (two enumerators per $n$; anchors exact).** Backtracking vs covering-polynomial DP agree everywhere; the sign-summed amplitudes reproduce FT.68(2)'s documented pairs $(Z_{\mathrm{byp}},Z_{\mathrm{lock}})$ **exactly for all eight $n$**: $(25,48),(353,64),(1161,80),(3121,1632),(11929,10864),(53825,43136),(229417,159888),(844881,775840)$; cover counts $(10,33,56,118,281,649,1423,3166)$ with sector splits $(7{+}3,\ 29{+}4,\ 51{+}5,\ 97{+}21,\ 211{+}70,\ 485{+}164,\ 1051{+}372,\ 2241{+}925)$; $|\mathcal C|_{\max}\le\lfloor3n/4\rfloor$ (bypass) verified per $n$: $(1,2,3,3,4,4,5,6)$.
$(2)$ **Form factors (tail convention, all-sector, exact Fractions, units $\ln2$).**
$$
\begin{array}{c|cccc}
n & M^{(w_U)}=M^{(w_C)}\cdot2 & M^{(w_K)} & M^{(w_E)} & M^{(w_H)}\\
\hline
3 & \tfrac{3264}{865} & \tfrac{9504}{865} & \tfrac{96}{865} & \tfrac{3072}{865}\\
4 & \tfrac{24832}{6273} & \tfrac{1408}{153} & \tfrac{1408}{2091} & \tfrac{10240}{6273}\\
5 & \tfrac{281920}{50081} & \tfrac{694240}{50081} & \tfrac{7840}{50081} & \tfrac{135680}{50081}\\
6 & \tfrac{2808192}{407233} & \tfrac{7585344}{407233} & \tfrac{212160}{407233} & \tfrac{2079744}{407233}\\
7 & \tfrac{29210048}{3804641} & \tfrac{74587296}{3804641} & \tfrac{2663136}{3804641} & \tfrac{17679872}{3804641}\\
8 & \tfrac{300392960}{33646849} & \tfrac{767038208}{33646849} & \tfrac{19632384}{33646849} & \tfrac{178147328}{33646849}\\
9 & \tfrac{2833063488}{282265633} & \tfrac{7303749984}{282265633} & \tfrac{16677792}{21712741} & \tfrac{1757108736}{282265633}\\
10 & \tfrac{27649976960}{2481810241} & \tfrac{71155288000}{2481810241} & \tfrac{2115650880}{2481810241} & \tfrac{17046103040}{2481810241}
\end{array}
$$
with $M^{(w_C)}=M^{(w_U)}/2$ exactly at every $n$ [FT.97(3)]. Per-sector values are tabulated in the suite output.
$(3)$ **Growth: linear-to-sublinear, saturating.** $M^{(w_U)}(C_n)$ rises $3.77\to11.14$ over $n=3..10$ (ratios to $P_3$: $1.049,1.492,1.827,2.035,2.366,2.660,2.953$) — approximately $\approx1.1n$, never exponential in $n$; $M^{(w_K)}$: max ratio $2.609$; $M^{(w_H)}$: max $1.934$; $M^{(w_E)}$: non-monotone (parity oscillation), max $7.681$.
$(4)$ **B4/D1 verdict: the fifth clean negative.** The widest form-factor ratio in the entire computed family is $7.681$ ($w_E$, $n{=}10/3$) against [EXT] targets $207$ (shortfall $\times27.0$) and $3477$ ($\times453.9$); for the primary weight $w_U$ the widest is $2.953$ (shortfalls $\times70.1$ / $\times1177.6$). No aligned triple exists within any factor of $10$ (the widest family ratio over all weights and all $n$ is $7.681$). The "lepton sector" label is declined [F2]; the [EXT] hierarchies enter only this comparison.
$(5)$ **D2 answered exactly.** The $16^{|\mathcal C|}$ weighting *does* concentrate inside each skeleton — exact weight fractions at $|\mathcal C|_{\max}$: $\tfrac{768}{865},\tfrac{2048}{2091},\tfrac{40960}{50081},\tfrac{196608}{407233},\tfrac{3211264}{3804641},\tfrac{16777216}{33646849},\tfrac{50331648}{282265633},\tfrac{1509949440}{2481810241}$ ($0.888,0.979,0.818,0.483,0.844,0.499,0.178,0.608$ — parity-oscillating) — but $|\mathcal C|_{\max}$ itself grows only linearly ($\le3n/4$), so the enhancement **saturates at the cap**: exponential within, linear across [FT.97(5)]. "Suppress low-node, exponentially enhance high-node" is true intra-skeleton and false as a hierarchy mechanism.

**Req.** Def-H.25, Def-H.26; FT.67, FT.68(2), FT.69, FT.75, FT.79(2), FT.97; CT0.11 (Part 1); two enumerators (backtracking vs DP), exact Fractions [math; machine]. External targets marked at (4).

**Pf.**
$$
(1):\ \text{enum\_covers\_bt}=\text{cover\_dp coefficients per level};\qquad Z=\sum_{\text{level}}c_k4^k=\mathrm{FT.68}(2)\ \text{row verbatim}\ [\text{machine}]
$$
$$
(2),(3):\ \text{exact Fraction averages over the enumerated covers};\qquad M^{(w_C)}=M^{(w_U)}/2:\ \mathrm{FT.97}(3)\ \text{identity}
$$
$$
(4):\ \max_{w,n}\tfrac{M^{(w)}(C_n)}{M^{(w)}(C_3)}=7.681\ldots;\qquad 207/7.681=26.95\ldots;\qquad(5):\ \text{exact fractions as tabulated}\ \blacksquare
$$

**Phys.** Run the new mass idea along the polygon ladder and the ladder answers in the same voice as every read before it: the averages climb, but they climb like counting, not like cascading — three and a half units at the triangle, eleven at the decagon, and the steepest weighting scheme in the whole family buys a factor of seven and change. The exponential the proposal hoped for is real, but it lives in the *weights*, and the weights are capped by the crystallization budget: three units of $|\mathcal C|$ per four vertices, forever. Ten-sided polygons are not two hundred times heavier than triangles, and no reweighting of the same finite gas will make them so.

---

---

### FT.99 — The Platonic form factors, the dominance census, and the reduced-denominator record

**Thm.** At (S1)–(S4):
$(1)$ **Tetrahedron (two enumerators: power-set filter of all $4096$ patterns vs backtracking — identical $101$ covers; $7$-class table re-verified [FT.78(2)]; $Z=(1057,448)$ [FT.68(1)]).** Exact form factors (tail, units $\ln2$):
$$
\begin{array}{c|ccccc}
\text{sector} & w_U & w_K & w_C & w_E & w_H\\
\hline
\text{all} & \tfrac{172800}{35201} & \tfrac{566400}{35201} & \tfrac{86400}{35201} & \tfrac{12672}{35201} & \tfrac{227328}{35201}\\
\text{byp} & \tfrac{62208}{15745}\ [\mathrm{FT.68}(1)(ii)\ \text{anchor}] & \tfrac{27264}{3149} & \tfrac{31104}{15745} & \tfrac{12672}{15745} & \tfrac{18432}{15745}\\
\text{lock} & \tfrac{108}{19} & \tfrac{420}{19} & \tfrac{54}{19} & 0 & \tfrac{204}{19}
\end{array}
$$
(the locked $w_E=0$ is structural: locked tetra covers — double-digon hubs and $K_{1,3}$ stars — have no endpoints at all). Concentration at $|\mathcal C|_{\max}=3$: $16384/35201=0.4654$ (the four $K_{1,3}$ stars).
$(2)$ **Cube (fresh enumeration: $11\,205$ covers, all distinct; cross-checked against the stored class census: $\sum\Omega=11\,205$, $\Omega$-histogram identical, $Z=(1\,109\,313,\ 1\,150\,848)$).** Exact form factors:
$$
\begin{array}{c|ccccc}
\text{sector} & w_U & w_K & w_C & w_E & w_H\\
\hline
\text{all} & \tfrac{482089472}{53648367}\ (8.986) & \tfrac{2241319168}{89413945}\ (25.07) & \tfrac{241044736}{53648367} & \tfrac{256135424}{268241835} & \tfrac{2021359616}{268241835}\\
\text{byp} & \tfrac{655450624}{82871211}\ (7.909) & \tfrac{485339392}{27623737} & \tfrac{327725312}{82871211} & \tfrac{144068864}{82871211} & \tfrac{202792960}{82871211}\\
\text{lock} & \tfrac{285644}{30171}\ (9.468) & \tfrac{285804}{10057} & \tfrac{142822}{30171} & \tfrac{6080}{10057} & \tfrac{887972}{90513}
\end{array}
$$
Concentration at $|\mathcal C|_{\max}=6$: $67108864/804725505=0.0834$ (four covers).
$(3)$ **C3 comparison against the existing reads.** The directive's "single-node aspect-blind masses" are whole-subnetwork reads: $m_{\mathrm{hid}}(\mathrm{tetra\ floor})=12\ln2/\mathfrak h$, $m_{\mathrm{hid}}(\mathrm{cube\ floor})=24\ln2/\mathfrak h$ [FT.42: $2E$]; Ansatz-A ladder extremes $\{0..6\}$, $\{0..12\}$ [FT.79(1)]. The form factors sit **inside the same $O(V)$ band**: $M^{(w_U)}\mathfrak h/\ln2=4.909$ (tetra), $8.986$ (cube) — cube/tetra $=1.831$ against the $m_{\mathrm{hid}}$ ratio $2$; the widest cube-vs-tetra form-factor ratio over the five weights is $2.652$ ($w_E$, all-sector: $\tfrac{256135424/268241835}{12672/35201}$ exact; the locked sector is degenerate at $w_E$ — tetra locked $=0$ by clause (1)) and the primary-weight ratio is $1.831$. No new range; no hierarchy.
$(4)$ **Dominance census (the directive's flag, exact).** "Intermediate dominates base" := centre$+$hub role bits $>$ endpoint role bits (convention-free half-split). Counts: tetrahedron $64/100$ non-vacuum covers ($|A|^2$-weighted fraction $248/275=0.902$); cube $10\,052/11\,204$ (weighted $3115352/3143459=0.9911$); polygons rising $3/9\ (C_3)\to2725/3165\ (C_{10})$. **The amplitude-weighted ensemble is generically centre-dominated** — mechanism: an isolated $2$-edge thread splits its bits evenly (one centre bit vs two endpoint half-bits), and dominance arises exactly where vertices *share* roles (types $(1,2),(2,2),\dots$): multi-role vertices accrue centre/hub bits while their partner endpoints accrue fewer. The flag is therefore not an anomaly to hunt but the generic structure of covers at scale.
$(5)$ **D1 verdict: fifth clean negative, with the exact obstruction.** No weight, sector or skeleton in the computed inventory produces ratios within $\times27$ of the [EXT] $207$ or $\times454$ of $3477$; the a priori bound is FT.97(5)'s required-$V$ table ($V\ge65\ldots6561$ by weight, against $V=4/8$); "baryon sector" declined [F2]. The verdicts of FT.77/FT.79(4)/FT.84(5)/FT.87(9) stand unmodified and now cover the form-factor species as well.
$(6)$ **Integrity ledger (this pass's catches, recorded pre-ship).** **(a)** The first run double-counted registration bits ($i_v=a{+}b$: $\sum_v\deg=2K$), producing $124416/15745=2\times$ the FT.68(1)(ii) anchor — **caught by the anchor**, corrected to the tail convention, and promoted to FT.97(2a)'s convention clause (the factor-$2$ freedom is real and now documented, not silently fixed). **(b)** the previously published $\langle m_A^2\rangle_{\mathrm{cube}}=22146188288/268241835$ is in **lowest terms**: the unreduced census sums are $66438564864/804725505$ (common factor $3$) — the values are identical, **no erratum needed**; the trap (comparing unreduced sums to reduced Fractions) is recorded so it is not re-hit. **(c)** Dodeca/icosa/octa form factors deferred (bounded rule — cover enumeration scale; recorded, as in FT.78's Status).

**Req.** Def-H.25, Def-H.28; FT.16, FT.41, FT.42, FT.67, FT.68(1), FT.78, FT.79, FT.80, FT.94(3), FT.97; two enumerators per skeleton; stored cross-checks; exact Fractions [math; machine]. External data marked at (5).

**Pf.**
$$
(1):\ 2^{12}\ \text{power-set filter}=\text{backtracking}\ (101=101,\ \text{set-identical});\qquad M^{(w_U)}_{\mathrm{byp}}=\tfrac{\sum16^{|\mathcal C|}K}{\sum16^{|\mathcal C|}}=\tfrac{62208}{15745}\ [\text{machine}=\mathrm{FT.68}(1)(ii)]
$$
$$
(2):\ \text{fresh }11205\ \text{distinct covers};\qquad \sum\Omega\cdot16^{|\mathcal C|}=804725505=3\cdot268241835\ [\text{reduction recorded at}\ (6b)]
$$
$$
(3):\ \tfrac{482089472/53648367}{172800/35201}=\tfrac{482089472\cdot35201}{53648367\cdot172800}\ [\text{machine, exact}];\qquad(4):\ \text{per-cover role decomposition census}
$$
$$
(5):\ \mathrm{FT.97}(5)\ \text{table};\qquad(6):\ \text{anchor catch}+\gcd(66438564864,804725505)=3\ [\text{machine}]\ \blacksquare
$$

**Phys.** Weighed node by node under five honest conventions, the tetrahedron's gas comes out at about five bits and the cube's at about nine — the same band every previous read occupied, the same factor-of-two step between four vertices and eight. The one genuinely new picture the census paints is of *who* carries the weight: in the cube's amplitude-weighted ensemble, ninety-nine percent of the mass of the average sits in configurations where the threading junctions and hubs outweigh the thread ends — the gas, weighed by its own amplitudes, is almost pure junction. That is a real structural fact about covers at scale. It is not a hierarchy, and the theorem says no amount of reweighing can turn it into one: the average is hostage to its largest summand, and every summand is hostage to the cap.

---

---

### FT.105 — Well-definedness: the topology census from first principles, finiteness, the regularization

**Thm.** Under Def-H.32:
$(1)$ **Polya census.** The all-graph counts derived by exact Burnside over $S_n$ acting on edge pairs, $g(n)=\tfrac1{n!}\sum_\pi2^{\,\mathrm{cycles}(\pi|_{\text{pairs}})}$:
$$
g(1..8)\ =\ (1,\ 2,\ 4,\ 11,\ 34,\ 156,\ 1044,\ 12346)\qquad[\text{exact integers; machine}].
$$
$(2)$ **Connected counts by Euler inversion.** From $\prod_k(1-x^k)^{-c(k)}=\sum_ng(n)x^n$ [math: the component decomposition of the ordinary generating function], solved exactly over $\mathbb Z$:
$$
c(1..8)\ =\ (1,\ 1,\ 2,\ 6,\ 21,\ 112,\ 853,\ 11117)\qquad[\text{every }c(n)\text{ integral; machine}].
$$
$(3)$ **Explicit enumeration (independent path).** Canonical-form enumeration over all $2^{\binom n2}$ labelled edge sets, minimum over $S_n$, agrees with $(1)$–$(2)$ at every $n\le5$ (all-graph totals $1,2,4,11,34$; connected $1,1,2,6,21$). $|\mathcal G_4|=10$; the cells by edge count: $E=(0,1,2,3,3,3,4,4,5,6)$.
$(4)$ **Finiteness and regularization.** Per budget cell the configuration space is finite and its size exact: $\sum_{\Gamma\in\mathcal G_4}2^{2E(\Gamma)}=5845$; every $Z^{\bullet}_B(q,S)$ is a finite sum of terms in $\mathbb Z[t,u]$ — well-defined with no convergence question [FT.68(7) pattern]; the declared regularization is the budget filtration $(B,B_K)$ of Def-H.32(1); the unfiltered limit is not constructed. Growth bookkeeping: $g$ doubles-exponentially in $n^2$ [$(1)$'s closed form], $c$ with it — per-budget finiteness is the exact statement, asymptotics are per-family data, not limits.
$(5)$ **New-cell covering census (exact; two enumerators where affordable).** Covering polynomials $(\mathcal Z_{\mathrm{byp}},\mathcal Z_{\mathrm{lock}})$ by cover counts per $|\mathcal C|$:
$$
\begin{array}{c|cc|c}
\text{cell}&\#\text{byp covers}&\#\text{lock covers}&\text{note}\\ \hline
\text{digon}&1&0&\text{vacuum only — the digon itself cancels [FT.74(3)]}\\
P_3&3&1&\\
C_3&7&3&\text{triangle threads; no closed triangle is a cover [FT.69(3)(iv)]}\\
P_4&7&4&\\
\mathrm{star}_4\ (K_{1,3})&9&2&\\
C_4&19&6&\text{the face 4-cycle lies in none of its covers [FT.69(3)(v)]}\\
\mathrm{paw}&29&4&\\
\mathrm{diamond}&45&10&\\
\text{tetra}&85\ (=1{+}24{+}60)&16\ (=12{+}4)&\text{re-derived live}=\text{frozen FT.68(1) rows}
\end{array}
$$

**Req.** A1, A7; D0.1, D0.8, D0.10; CT0.11 (Part 1); CT1.29 (Part 2); CT4.1 (Part 2); Def-H.25; FT.67, FT.68(7), FT.69(3), FT.74(3); Burnside/Polya enumeration, ordinary-generating-function Euler inversion, canonical forms [math; machine: `checks/verify_H_topology_blind.py` §A–§B].

**Pf.**
$$
(1):\ \text{cycle index of }S_n\text{ on }\binom n2\text{ pairs, computed per permutation (exact orbit walk)};\qquad n!\mid\sum_\pi2^{\mathrm{cyc}}\ [\text{machine: integrality asserted}]
$$
$$
(2):\ n\,g(n)=\sum_{k\le n}b(k)g(n-k),\ b(k)=\sum_{d\mid k}d\,c(d):\ \text{exact integer recursion solved upward};\qquad c(n)\in\mathbb Z\ \forall n\le8\ [\text{machine}]
$$
$$
(3):\ \text{adjacency-bitmask canonical minimum over }S_n;\qquad \text{counts}=(1,1,2,6,21)/(1,2,4,11,34)\ [\text{machine}]
$$
$$
(4):\ |\mathfrak C(\Gamma)|=2^{2E(\Gamma)};\qquad \textstyle\sum_{\Gamma\in\mathcal G_4}2^{2E}=2^0+2^2+2^4+2^6+2^6+2^6+2^8+2^8+2^{10}+2^{12}=5845\ [\text{machine}]
$$
$$
(5):\ \text{cover-DP}=\text{branch enumeration on every cell with }2E\le8\ [\text{machine, two enumerators}];\qquad \text{tetra rows}=\mathrm{FT.68}(1)\ \text{verbatim}.\ \blacksquare
$$

**Phys.** The integration variable "topology" is now an exactly enumerated space with a stated cutoff: ten connected cells at four nodes, thirty-one at five, one hundred twenty-five at six — counts derived from Burnside and Euler, not quoted. Nothing converges because nothing needs to: every budget cell is a finite exact sum, and the filtration by the ledger's own nat content is the regularization. No particle identification; topology names are bookkeeping.

---

---

### FT.114 — The [EXT] audit clause (FT.73(5) pattern)

**Thm.** External-data clause. The hierarchy
$$1:206.768:3477.2\qquad[\text{EXT: supplied measured charged-lepton mass ratios}]$$
is supplied measured data. It enters no derivation, no definition, and no coefficient of this document; every number in FT.109–FT.113 is fixed without it. This document identifies no particles. The exact shortfalls of the supplied hierarchy against the derived ratios [FT.113] are
$$\text{shortfall}_{\mathrm{mid}}=\frac{206.768}{r_{\mathrm{mid}}^2/r_{\min}^2}=\frac{25846/125}{r_2^2/r_1^2}=0.999988799297817\ldots,$$
$$\text{shortfall}_{\mathrm{out}}=\frac{3477.2}{r_{\max}^2/r_{\min}^2}=\frac{17386/5}{r_0^2/r_1^2}=0.999921541556935\ldots\qquad[\text{exact rational division of enclosed ratios; widths}<2^{-50};\ \text{machine}],$$
and the recorded verdicts are:
$$(1)\ \ \text{The computed ratios do NOT match [EXT] to [EXT]'s stated precision (mid: }6\text{ significant figures; out: }5\text{): the gaps are enclosure-provably nonzero — }r_2^2/r_1^2-206.768>\tfrac1{1000},\quad r_0^2/r_1^2-3477.2>\tfrac1{10};$$
$$(2)\ \ \text{both shortfalls are strictly below }1\text{ and above }1-2\times10^{-4}:\ \text{the derived ratios exceed the supplied values by relative margins below }2\times10^{-4}\ (1-\text{shortfall}_{\mathrm{mid}}\in(10^{-5},2\times10^{-5}),\ 1-\text{shortfall}_{\mathrm{out}}\in(7\times10^{-5},9\times10^{-5}));$$
$$(3)\ \ \text{the numerical coincidence and the structural origin are reported separately: the coincidence is the proximity recorded in (2); the structural origin of the ratios is the normalization data of FT.111–FT.113 — the diagonal coefficient }2\text{, the seal dimension }3\text{, the transfer trace }3\text{ — which contain no [EXT] input. No claim is made that the derivation reproduces the observed hierarchy. No identification of the three eigenvalues with any particle species is made or implied.}$$

**Req.** FT.113; FT.73(5) (Tiers F.23–F.25, the audit pattern); P1, P5 (**A**: no quantity identified with a measured external constant; comparison is a test, never an input); exact rational interval division [math; machine: `checks/verify_H_koide_channel.py` §G]. [EXT] data clause: the supplied values enter this block and no other block of this document (machine-scanned, §H).

**Pf.**
$$
206.768=\tfrac{206768}{1000}=\tfrac{25846}{125},\qquad 3477.2=\tfrac{34772}{10}=\tfrac{17386}5\ [\text{exact Fractions in lowest terms}]
$$
$$
\text{shortfall}=\tfrac{[\mathrm{EXT}]}{q},\ q\ \text{the enclosed ratio of FT.113}:\ \text{monotone exact interval division by positive enclosures}\ \bigl[\tfrac{[\mathrm{EXT}]}{q_{\mathrm{hi}}},\tfrac{[\mathrm{EXT}]}{q_{\mathrm{lo}}}\bigr];\qquad\text{widths}<2^{-50}\ [\text{machine §G}]
$$
$$
(1):\ 206.768<\operatorname{lo}\bigl(r_2^2/r_1^2\bigr),\quad 3477.2<\operatorname{lo}\bigl(r_0^2/r_1^2\bigr)\ [\text{exact rational comparison against disjoint enclosures}]
$$
$$
(2):\ \operatorname{hi}(\text{shortfall})<1;\qquad 1-\text{shortfall}\in\bigl(10^{-5},2\times10^{-5}\bigl)\cup\bigl(7\times10^{-5},9\times10^{-5}\bigl)\ [\text{enclosure-proven, machine}]
$$
$$
(3):\ \text{the tokens }206.768,\ 3477.2\ \text{occur only inside this block, and [EXT]-marked content enters no Req, Pf, or coefficient of FT.109–FT.113}\ [\text{machine scan §H};\ \mathrm{FT.73}(5)\ \text{discipline: recorded, not adopted}].\ \blacksquare
$$

**Phys.** The audit states exactly what is on record and nothing more: a three-line dimensionless hierarchy built from seal integers lands within two parts in $10^4$ of a supplied three-line measured hierarchy, misses it at the measurement's own stated precision, carries no overall scale, and identifies nothing. The near-agreement is a numerical fact about rationals and cosines; the construction remains data-free by its own rules.

---

---

### FT.120 — The [EXT] audit ledger: scheme columns, exact shortfalls, and the two exclusions

**Thm.** External-data clause (FT.73(5)/FT.114 pattern). The heavy triplet of the up-type and down-type sectors, in three renormalization-scheme columns,
$$\text{S1 (own-scale}\ \overline{\mathrm{MS}}\text{)}:\ (1.273,\ 4.183,\ 162.5)\ \mathrm{GeV};\qquad\text{S2}\ (\overline{\mathrm{MS}}\ \text{plus pole top}):\ (1.273,\ 4.183,\ 172.4)\ \mathrm{GeV};\qquad\text{S3 (pole-type)}:\ (1.67,\ 4.78,\ 172.4)\ \mathrm{GeV},$$
$$\text{with ratio box}\quad m_u/m_d=0.462\pm0.020,\qquad m_s/m_d\in[17,22],\qquad m^0_{\pi}=134.9768\ \mathrm{MeV}\qquad[\text{EXT}]\ \text{supplied measured data},$$
is supplied measured data [EXT]. It enters no derivation, no definition, and no coefficient of this document; every number in FT.116–FT.119 is fixed without it. This document identifies no particles; the correspondence audited below is a test, never an input [P1, P5]. The exact shortfall factors of the supplied hierarchies [EXT] against the derived ratios [FT.119(5)], by monotone rational interval division at widths $<2^{-50}$, are
$$(1)\quad\text{S1}:\ \ \frac{m_2}{m_1}=3.285938\ldots,\ \frac{m_3}{m_1}=127.6512\ldots\implies\text{shortfall}_{\mathrm{mid}}=0.922058\ldots,\quad\text{shortfall}_{\mathrm{out}}=0.916122\ldots;$$
$$\text{S2}:\ \ \frac{m_3}{m_1}=135.4281\ldots\implies\text{shortfall}_{\mathrm{mid}}=0.922058\ldots,\quad\text{shortfall}_{\mathrm{out}}=0.971934\ldots;\qquad\text{S3}:\ \ (2.862275\ldots,\ 103.2335\ldots)\implies(0.803176\ldots,\ 0.740881\ldots);$$
$$(2)\quad\text{all six shortfalls are strictly below}\ 1\ \text{and enclosure-provably nonzero: the derived ratios exceed the supplied ones in every scheme column};$$
$$(3)\quad\textbf{the channel invariant:}\qquad Q=\frac{\sum_im_i}{\bigl(\sum_i\sqrt{m_i}\bigr)^2}:\quad\text{S1}\ 0.662600\ldots,\quad\text{S2}\ 0.669113\ldots,\quad\text{S3}\ 0.648359\ldots,$$
$$\text{equivalently}\quad\frac{B^2}{A^2}=6Q-2:\quad\text{S1}\ 1.97560\ldots,\quad\text{S2}\ 2.01468\ldots,\quad\text{S3}\ 1.89015\ldots\qquad\text{against the derived normalization value}\ 2\ [\mathrm{FT.111}(3)];$$
$$|\,Q-\tfrac23\,|<0.01\ \text{in S1 and S2}\ (\text{and}\ 0.01<|\,Q-\tfrac23\,|<0.03\ \text{in S3}):\ \text{the heavy triplet sits on the channel's normalization surface at the}\ 1\%\ \text{level in the}\ \overline{\mathrm{MS}}\ \text{columns};$$
$$(4)\quad\textbf{anchored rows}\ [\mathrm{FT.119}(6)]:\qquad\frac{m_2}{m_3}\bigg|_{\text{derived}}=0.025575776\ldots\ \text{vs}\ \frac{4.183}{162.5}=0.025741\ldots\ [\text{EXT}]\ \text{S1}:\ \text{relative margin}\ 0.0065<0.01\ (\text{agreement within}\ 1\%);$$
$$\frac{m_1}{m_3}\bigg|_{\text{derived}}=0.007176757\ldots\ \text{vs}\ \frac{1.273}{162.5}=0.007833\ldots\ [\text{EXT}]\ \text{S1}:\ \text{relative margin}\ 0.0838>0.05\ (\text{the inner member is the outlier});$$
$$(5)\quad\textbf{no scheme column reproduces both derived ratios at the}\ 1\%\ \textbf{level}\ [\text{machine: exhaustive over the three columns}];$$
$$(6)\quad\textbf{obstruction O3 (light triplet, excluded):}\ \ \text{over the whole supplied ratio box}\ m_u/m_d\in[0.442,0.482],\ m_s/m_d\in[17,22],$$
$$Q_{\mathrm{light}}\in(0.5461\ldots,\ 0.5804\ldots)\subset(0.54,0.59),\qquad Q_{\mathrm{light}}<\frac35<\frac23,\qquad\frac{B^2}{A^2}=6Q_{\mathrm{light}}-2\in(1.25,1.5)\ \text{versus the derived}\ 2;$$
$$\text{extrema attained at box corners}\ [\partial Q/\partial\sqrt{r_s}>0,\ \partial Q/\partial\sqrt{r_u}<0\ \text{on the box};\ \text{machine-guarded}]:\ \text{the}\ (A,B)=(1,\sqrt2)\ \text{normalization is EXCLUDED for the light triplet at every phase}\ \delta\ [\mathrm{FT.119}(4):\ Q\ \text{is phase-free}];$$
$$(7)\quad\textbf{obstruction O4 (hadron range, excluded):}\ \ \text{the established hadron mass span}\ \le\frac{11000}{134.9768}=81.495\ldots<82\ [\text{EXT}]\ \text{is below the derived colour-channel outer ratio}\ 139.3386880284\ldots\ [\mathrm{FT.119}(5)]\ \text{and far below}\ \mathrm{FT.113}\text{'s}\ 3477.472837104\ldots;$$
$$\text{hence no baryon or meson triplet spans the channel's dynamic range}\ —\ \text{the second, independent exclusion of the hadron-level read, the first being FT.117}(7)\text{'s blindness theorem};$$
$$(8)\quad\textbf{the dimension trap, disclosed and rejected}\ [\mathrm{FT.77}(3)\ \text{pattern}]:\ \ \text{the literal label}\ m\propto r\ (\text{unsquared})\ \text{gives}\ 1:14.3795\ldots:58.9701\ldots\ \text{on the}\ \delta_\ell=\tfrac29\ \text{spectrum — missing the supplied mid ratio}\ 206.768\ [\text{EXT}]\ \text{by}\ >14\times,$$
$$\text{while the}\ r^2\ \text{read reproduces it within}\ 1\%\ (206.770315972\ldots)\ [\text{EXT}];\qquad\text{the same literal label on the colour channel gives}\ r^{(q)}_2/r^{(q)}_1=1.887775\ldots\ \text{against}\ 3.285938\ldots\ (1.74\times\ \text{off}):\ \text{the squared read is the only one that survives either audit};$$
$$(9)\quad\textbf{provenance:}\ \ \text{the structural origin of the derived ratios is the normalization data of FT.116–FT.119 — the diagonal coefficient}\ 2,\ \text{the seal dimension}\ 3,\ \text{the transfer trace}\ 3,\ \text{the colour count}\ 3\ —\ \text{which contain no [EXT] input. The numerical proximity recorded in}\ (1)\text{–}(4)\ \text{and the structural origin are reported separately. No claim is made that the derivation reproduces the observed hierarchy; no identification of the three eigenvalues with any particle species is made or implied.}$$

**Req.** FT.119; FT.113, FT.114 (**Tier F.37**, the audit pattern and the lepton-side decimals); FT.73(5) (Tiers F.23–F.25), FT.77(3) (Tiers F.26–F.28), FT.107 (Tier F.36) for the audit-pattern and read-vocabulary precedents; P1, P5 (**A**: no quantity identified with a measured external constant; comparison is a test, never an input); exact rational interval division, exact rational square-root enclosures, corner-monotonicity guards [math; machine: `checks/verify_H_colour_channel.py` §E]; floating-point cross-check of the same ledger: `checks/audit_heavy_quark_scheme.py`. [EXT] data clause: the supplied values enter this block and no other block of this document (machine-scanned, §F).

**Pf.**
$$
(1):\ \text{S1 mid}=\tfrac{4.183}{1.273}=\tfrac{4183}{1273},\ \text{S1 out}=\tfrac{162.5}{1.273}=\tfrac{16250}{1273};\ \text{S2 out}=\tfrac{172.4}{1.273};\ \text{S3}=\tfrac{4.78}{1.67},\ \tfrac{172.4}{1.67}\ [\text{exact Fractions in lowest terms}]
$$
$$
\text{shortfall}=\tfrac{[\mathrm{EXT}]}{q},\ q\ \text{the enclosed ratio of FT.119(5)}:\ \text{monotone exact interval division}\ \bigl[\tfrac{[\mathrm{EXT}]}{q_{\mathrm{hi}}},\tfrac{[\mathrm{EXT}]}{q_{\mathrm{lo}}}\bigr];\ \text{widths}<2^{-50}\ [\text{machine}]
$$
$$
(2):\ \operatorname{hi}(\text{shortfall})<1\ \text{in all six cases};\qquad\text{nonzero gaps: }\ q_{\mathrm{lo}}>[\mathrm{EXT}]\ [\text{disjoint rational comparison};\ \text{machine}]
$$
$$
(3):\ Q=\tfrac{\sum m}{(\sum\sqrt m)^2}\ \text{with}\ \sqrt m\ \text{enclosed by integer Newton certificates at}\ 2^{-60};\ \text{widths}<2^{-40};\qquad\tfrac{B^2}{A^2}=6Q-2\ [\text{exact affine read of}\ \mathrm{FT.111}(3)\text{'s}\ \textstyle\sum(\lambda-A)^2=\tfrac32B^2\ \text{and}\ \sum\lambda=3A]
$$
$$
\text{windows}: \text{S1},\text{S2}\in(\tfrac23-\tfrac1{100},\tfrac23+\tfrac1{100});\qquad\text{S3}\in(\tfrac23+\tfrac1{100},\tfrac23+\tfrac3{100})\cup(\tfrac23-\tfrac3{100},\tfrac23-\tfrac1{100})\ [\text{machine}]
$$
$$
(4):\ \tfrac{4.183}{162.5}=\tfrac{4183}{162500};\quad\bigl|\tfrac{4183}{162500}-\tfrac{(r^{(q)}_2)^2}{(r^{(q)}_0)^2}\bigr|/\tfrac{4183}{162500}<\tfrac1{100};\qquad\tfrac{1.273}{162.5}=\tfrac{1273}{162500};\quad\text{relative margin}>\tfrac5{100}\ [\text{machine}]
$$
$$
(5):\ \neg\bigl(\operatorname{lo}(\text{shortfall}_{\mathrm{mid}})>\tfrac{99}{100}\wedge\operatorname{lo}(\text{shortfall}_{\mathrm{out}})>\tfrac{99}{100}\bigr)\ \text{in each column}\ [\text{machine, exhaustive}]
$$
$$
(6):\ Q(r_u,r_s)=\tfrac{r_u+1+r_s}{(\sqrt{r_u}+1+\sqrt{r_s})^2}\ \text{with}\ r_u=m_u/m_d,\ r_s=m_s/m_d;\quad\partial_{\sqrt{r_s}}Q>0\iff\sqrt{r_s}(1+\sqrt{r_u})>1+r_u\ (\text{true on the box});\quad\partial_{\sqrt{r_u}}Q<0\iff\sqrt{r_u}(1+\sqrt{r_s})<1+r_s\ (\text{true on the box})
$$
$$
\implies\text{extrema at corners}:\ Q_{\min}=Q(\tfrac{482}{1000},17),\ Q_{\max}=Q(\tfrac{442}{1000},22);\qquad\tfrac{54}{100}<Q_{\min}\le Q_{\mathrm{light}}\le Q_{\max}<\tfrac{59}{100}<\tfrac35<\tfrac23\ [\text{exact enclosures};\ \text{machine}]
$$
$$
(7):\ \tfrac{11000}{134.9768}=\tfrac{110000000}{1349768}=81.495\ldots<82<139.3386880284\ldots\ [\text{exact rational comparison against FT.119(5)'s enclosure};\ \text{machine}]
$$
$$
(8):\ \tfrac{l_2}{l_1}=14.3795\ldots,\ \tfrac{l_0}{l_1}=58.9701\ldots\ \text{on the}\ \delta_\ell\ \text{spectrum}\ [\mathrm{FT.113}\ \text{enclosures re-derived};\ \text{machine}];\qquad\tfrac{206.768}{14.3795\ldots}>14;\qquad0.99<\tfrac{206.768}{206.770315972\ldots}<1.01;\qquad\tfrac{r^{(q)}_2}{r^{(q)}_1}=1.887775\ldots<2<3.285938\ldots
$$
$$
(9):\ \text{the tokens}\ 1.273,\ 4.183,\ 162.5,\ 172.4,\ 1.67,\ 4.78,\ 0.462,\ 134.9768\ \text{occur only inside this block, and no [EXT]-marked content enters any Req, Pf, or coefficient of FT.116–FT.119}\ [\text{machine scan}\ \S\mathrm{F}].\ \blacksquare
$$

**Phys.** The ledger states what is on record and nothing further. A three-line dimensionless hierarchy built from four integers of the frozen algebra — the seal coefficient $2$ and the three factors $3,3,3$ of the dressed arena — has its invariant reading $Q$ landing within one percent of the supplied [EXT] heavy-triplet value in the two running-mass columns, and its top-anchored inner ratio landing within seven parts in a thousand of the supplied own-scale column. It misses both supplied ratios at their own precision, in every column, by an enclosure-provably nonzero margin; the pole column misses by twenty to twenty-six percent. Two branches of the docket are closed by theorem rather than by taste: the light triplet cannot sit on this channel at any phase, because its $Q$ is bounded below $\tfrac35$ across the entire supplied ratio box while the channel's normalization forces exactly $\tfrac23$; and no hadron triplet can reach the channel's range, because the established hadron spectrum spans less than a factor $82$ against the channel's $139$ — the same verdict FT.117 reached structurally. The squared-mass label is the only one that survives either side of the dimension audit. The near-agreement is a numerical fact about rationals and cosines; the construction remains data-free by its own rules.

---

---

---

## §Consumption — the cell-consumption block

*Preamble (census supply from Category-A tags): the cover-polynomial tables of FT.68, the frame catalogue of FT.93, and the susceptibility census of FT.103 are census sides of structural tags; Part 4 consumes them through those tags' own rows — no B-classification is implied. No census entry is dismissed: each is a load-bearing cell supply (separation charter).*

**FT.28.** Space: the two-vertex digon floor $\Sigma_{\min}$ with a single observer contact; registration data $(\sigma_e,\kappa)$). Counts: the complete floor card: $I_{\mathrm{hid}}=2\ln2$, $\Theta_{\mathrm{int}}=2\kappa$, winding, holonomy, aspect rows, mask dimension $\le10$, rung counts, the ternary core read. Baryonic: the minimal fermion cell and its card grammar — every sealed composite card (baryon-type junctions included) refines this row template; the digon is the junction kernel of the composition laws.

**FT.32.** Space: the single-contact cycle floors $\Sigma_L$ (unidirectional $L$-cycles). Counts: the ladder $m_{\mathrm{hid}}(L)=L\ln2/\mathfrak h$, the minimality regimes, structural colourlessness per $L$. Baryonic: the winding ladder baryonic chains compose over; additive winding composition [FT.34(3)] consumes these cells as summands.

**FT.35.** Space: the composite floor $\Sigma_{12}$ (first colour-active, first lock-carrying). Counts: the junction lock content, the baryon-type sealing phase, the maximal $18$-dimensional mask. Baryonic: the first computed colour-active cell — the junction grammar baryon seals run, and the $D^-$-carrying cell for the $n\ge4$ lock side.

**FT.42.** Space: the five Platonic skeletons under the uniform-minimal materialization scope (M1/M2). Counts: the card template per solid: $E_{\mathrm{int}}=2E$, $m_{\mathrm{hid}}$, $\Pi$, winding and lock profiles. Baryonic: the symmetric-skeleton cell pool; the tetrahedron's trivalent vertices are the native baryon-junction site.

**FT.43.** Space: per-solid winding-ledger states with Euler consistency. Counts: $F-1$ independent winding reads, degeneracies, per-face winding assignments. Baryonic: the winding bookkeeping sealed baryonic chains inherit; composition adds windings cell-wise.

**FT.44.** Space: the computed floors under solid duality. Counts: dual pairs sharing $m_{\mathrm{hid}}/\Pi$, split by winding/sealing/lock profiles; the taxonomy rows across every computed floor. Baryonic: the degeneracy-splitting grammar — how baryonic multiplets sharing a skeleton are told apart by ledger data.

**FT.45.** Space: the full regular-polygon floor family $\Sigma_{P_n}$, $n\ge3$. Counts: walk-space rank $n+1$, the single parity constraint, four minimality regimes, injective mass/rank/null reads per $n$. Baryonic: the unbounded cell family for chain composition and the polygon-limit anchor of the flicker boundaries [FT.70(3)].

**FT.49.** Space: the tetrahedron-face floor with baryon-type sealing. Counts: the full card: $\Theta_{\mathrm{int}}\in4\mathbb Z$, the $30$-dimensional exchange sector, the sealing grammar. Baryonic: the reference baryon-type sealing-phase cell — its junction structure is the template for $\varepsilon$-sealed triplet reads.

**FT.50.** Space: patch cells (bowtie, double-triangle) and floor pairs under gluing. Counts: junction-saturation data, the constraint-rank gluing law, glued-card rows. Baryonic: the composition laws by which multi-face baryonic skeletons are assembled from computed cells.

**FT.51.** Space: closed-walk winding ledgers per skeleton under dihedral symmetry. Counts: closed-form enumerations with degeneracy counts. Baryonic: the degeneracy pool for the sector labels $(q,S)$ of conditioned baryonic path integrals [Def-H.32(c) grammar].

**FT.63.** Space: the five Platonic floors with all physical read columns. Counts: spin (under Def-H.38), charge, parity, holonomy, entropy, mass ratios, binding — per solid; $j_{\max}\in\{6,6,12,30,30\}$. Baryonic: the per-solid read table baryonic multiplets consume as constituent data on symmetric skeletons.

**FT.64.** Space: admissible-loop lattices per solid under the filter chain. Counts: the generalized loop lists $A_S(K)$ with the exact character-sum closed form. Baryonic: the loop pool over which baryonic cover cells are built; the filter chain is the admissibility grammar.

**FT.65.** Space: coarse-grained loop classes under the full automorphism groups. Counts: the degeneracies $M_S(K)/M^+_S(K)$ and the register product $2^{2E}M_S(K)g(V)$. Baryonic: the register-counting side of sealed-object enumeration — multiplicity bookkeeping for baryonic state counts.

**FT.69.** Space: Platonic cover patterns with amplitude weights. Counts: the completed amplitude census (cover polynomials; the $62208/15745$ anchor), the cycle-alternation rows. Baryonic: the amplitude-layer data for flicker ensembles on symmetric skeletons; the norm/amplitude dichotomy [FT.68(3)] consumes these values.

**FT.76.** Space: Platonic defect-angle pole reads under both winding-pairing variants (A/B). Counts: the multiplet tables, the ceiling $[0,4\hat\mu'^2]$, the four $\Theta_R$ readings priced. Baryonic: the pole-side mass cells and their range taxonomy — the hard ceiling every baryonic pole read inherits.

**FT.78.** Space: tetrahedron and cube cover configurations under $\operatorname{Aut}$. Counts: tetrahedron: $70$ admissible / $7$ cover classes; cube: $33\,564$ admissible by $K$ / $264$ cover classes with $|\mathcal C|$-levels, signatures, chirality pairs. Baryonic: the cover-class pool baryonic sector-conditioning runs over; the exact enumeration substrate for cube-era cells.

**FT.81.** Space: the corpus read classes against the external-reference content rows. Counts: presence/absence per read class (charge, spin, winding, sealing, chirality, flavour) — the internal read-class inventory (external scoring columns excluded). Baryonic: the read-class grammar every baryonic card fills, and the audit template for P1/P5-compliant external comparison.

**FT.83.** Space: the rungs $n=0,1,2,3,\ge4$ with their activation sets. Counts: derived/declared/open status per rung; the $n\ge4$ derived no-go row. Baryonic: the activation map Part 4 extends at $n=3$ (colour, derived) and $n\ge4$ (the lock side).

**FT.84.** Space: the five mass-read species with their ranges. Counts: the ceiling taxonomy: two hard ceilings, two size-scaling species, one undeclared-fugacity direction (external scoring excluded). Baryonic: the range constraints any baryonic mass read inherits, and the species taxonomy new reads must join.

**FT.96.** Space: tetra/cube cover orbits under the orientation reversal. Counts: the chiral cover pairs (the two $\Omega=24$ orbits exchanged), reversal signatures per orbit. Baryonic: the chirality-tagged cover cells parity reads [FT.137] consume for sealed objects.

**FT.98.** Space: polygon skeletons under the multi-node form-factor species. Counts: exact $M$-tables, saturating growth rows, reduction-identity anchors. Baryonic: form-factor range data for extended baryonic skeletons (the linear size-bound species).

**FT.99.** Space: Platonic skeletons under the form-factor reads. Counts: the dominance census, reduced-denominator record, concentration fractions. Baryonic: the symmetric-skeleton form-factor cells for baryonic multiplet range checks.

**FT.105.** Space: connected graphs and canonical skeletons to $V\le8$ (canonical enumeration to $V\le5$). Counts: exact Burnside/Polya counts $g(n)$, Euler inversion $c(n)$, finiteness and regularization cells per budget. Baryonic: the first-principles topology pool over which the topology-blind baryonic integral is regulated (budget filtration).

**FT.114.** Space: the supplied external hierarchy against the derived $\ell$-channel ratios. Counts: exact shortfall arithmetic on the quarantined rows. Baryonic: the audit-discipline template for Part-4 external tests (P1/P5-compliant comparison grammar).

**FT.120.** Space: renormalization-scheme columns against the derived $q$-channel ratios; the light-triplet $Q$-box. Counts: the scheme ledger, exact shortfalls, the two derived exclusions. Baryonic: the scheme-dependence record Part-4 comparisons inherit — no canonical renormalization point is derivable in the corpus.

---
