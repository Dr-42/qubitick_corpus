# $\langle qu(b(i(t|t))ick)\rangle$ — **Part 5 · Atomic era** — Tier AT.4

**Level.** 5. **Era.** 2 (the Atomic era). **Tier.** AT.4 — the CP-assimilated tensor: scaffolding
for the Janus/CP merger channel, and the location of the structural obstruction.
**Tags.** AT.21–AT.28. **Status.** discovery-phase working tier. **No declaration issues;
§Cal-AT stays empty; no clause of Parts 1–4 is modified or retracted.**
**Machine.** `canon/era2/cp_tensor.py` → **28/28 exact**; `canon/era2/obs_equiv.py` → **18/18 exact** (AT.28). Exit 0. Arithmetic: `Fraction`,
$\mathbb Z[x_+,x_-]$, $\mathbb Q[\varepsilon_q]$, exact $2\times2$ and $4\times4$ matrices over
`Fraction`, exact integer dimension counts. **No floating point; no smooth-manifold analogy.**
**Charter.** Part 5 cites Parts 1–4 and earlier AT-tags only.

> **Directive compliance.** Steps 1–5 executed. **Step 5's premise is stale and is corrected**
> (AT.25): the no-annihilation row is *re-scoped, ¬retracted* [BM.123(8)], and residues
> (R9), (R9′), (R9″) are **closed** [BM.123(6); BM.142(5),(8)]. Step 5's dichotomy therefore has
> a **third answer**. The real obstruction to the directive's stated object is the **mask**, not
> the bar (AT.25(4)–(6)). Steps 1–2 are also corrected: the corpus has no history-kets, and the
> two histories are move-classes inside one configuration sum (AT.24).

---

## Tier AT.4 — the CP-assimilated tensor

### AT.21 — The Janus register, its two moves, and the nilpotence of the supply vertex

**Thm.**
$$(1)\quad\mathcal J:=\operatorname{span}_{\mathbb C}\{|\mathcal V\rangle,|\mathcal R\rangle\}\cong\mathbb C^2\ \ \text{in the (virtual, real) order}\qquad[\mathrm{Def\text{-}BM.18}(1)];$$
$$(2)\quad \hat J_+:=|\mathcal R\rangle\langle\mathcal V|\ (\text{crystallization},\ n_{\mathcal R}:0\to1),\qquad \hat J_-:=|\mathcal V\rangle\langle\mathcal R|\ (\text{dissolution},\ n_{\mathcal R}:1\to0);$$
$$\boxed{\ \hat J_+^2=0=\hat J_-^2\ }\qquad P_{\mathcal V}+P_{\mathcal R}=\mathrm{id},\quad P_{\mathcal V}P_{\mathcal R}=0\qquad[\text{machine: exact }2\times2\ \text{identities over }\mathbb Z];$$
$$(3)\quad\textbf{the master generator and its decomposition:}\qquad Q=\begin{pmatrix}-x_+&x_+\\ x_-&-x_-\end{pmatrix}\ \ \text{over}\ \mathbb Z[x_+,x_-],\qquad Q=x_+(\hat J_+-P_{\mathcal V})+x_-(\hat J_--P_{\mathcal R})\qquad[\mathrm{Def\text{-}BM.18}(3);\ \text{machine: entrywise}];$$
$$(4)\quad\textbf{the stationary measure:}\qquad (x_-,\ x_+)\,Q=(0,0)\ \ \text{exactly over }\mathbb Z[x_+,x_-],\qquad \dim\ker Q=1,\qquad p=\frac{x_+}{x_++x_-}=1-4\varepsilon_q\qquad[\mathrm{BM.19}(1)\text{--}(3);\ \mathrm{FT.108}(4)];$$
$$(5)\quad\textbf{the supply vertex is nilpotent:}\qquad \widehat{\mathcal V}_{\mathrm{sup}}:=e(k,E)^2\,(\hat J_+\otimes\hat J_+),\qquad \boxed{\ (\hat J_+\otimes\hat J_+)^2=0\ }\qquad[\mathrm{BM.142}(2);\ \text{machine: the exact }4\times4\ \text{identity over }\mathbb Z];$$
$$\textbf{the register cannot supply a pair twice};\qquad (\hat J_-\otimes\hat J_-)^2=0\ \ \text{likewise}\qquad[\text{machine}];$$
$$(6)\quad\textbf{the composition is a PAIR of nilpotent moves, }\neg\textbf{one operator:}\qquad \varnothing\xrightarrow{\ \hat J_+\otimes\hat J_+\ }\{c,c^{\mathrm{CP}}\}\xrightarrow{\ \hat J_-\otimes\hat J_-\ }\varnothing\qquad[\mathrm{BM.123}(5)];$$
$$(7)\quad\textbf{status: derived.}$$

**Req.** A4, A6, D0.4, D1.1, D1.2, CT0.1, CT0.8 (Part 1); Def-H.33, Def-H.38, FT.108(4) (Part 3); Def-BM.15(2),(3), Def-BM.18(1),(2),(3),(4),(5), BM.19(1),(2),(3), BM.109(1),(2), BM.113(2), BM.120(1),(5), BM.122, BM.123(1),(5), BM.142(2) (Part 4); exact $2\times2$/$4\times4$ matrix arithmetic over `Fraction`, exact polynomial identity over $\mathbb Z[x_+,x_-]$ [math; machine: `cp_tensor.py` §A].

**Pf.** $(2)$: $|\mathcal R\rangle\langle\mathcal V|\cdot|\mathcal R\rangle\langle\mathcal V|=|\mathcal R\rangle\langle\mathcal V|\mathcal R\rangle\langle\mathcal V|=0$ since $\langle\mathcal V|\mathcal R\rangle=0$; likewise for $\hat J_-$ [machine: entrywise]. $(3)$: entrywise over $\mathbb Z[x_+,x_-]$. $(4)$: $(x_-,x_+)Q=(x_-(-x_+)+x_+x_-,\ x_-x_++x_+(-x_-))=(0,0)$ identically. $(5)$: $(\hat J_+\otimes\hat J_+)^2=\hat J_+^2\otimes\hat J_+^2=0$. $\blacksquare$

**Phys.** The Janus register is a two-state object and its two moves are nilpotent, so no move can
repeat: the register crystallizes or dissolves *once*. That is the algebraic root of the arrow —
the reversibility lives in the move set and the stationary measure, never in a repeatable
operation. The supply vertex inherits the nilpotence, which is why the corpus can say the
register cannot supply a pair twice without invoking any dynamics.

---

### AT.22 — The exact weights of the two histories and the detailed-balance point

**Thm.**
$$(1)\quad\textbf{the four monomials:}\qquad\begin{array}{l|l|l}
\text{the move} & \text{the weight} & \text{the locus}\\ \hline
\text{pair creation (two one-way)} & \mathcal W_{\text{channel}}=x_+^2\,\chi_{\{NE\ge\mathcal T_0\}}=(1-4\varepsilon_q)^2\chi & [\mathrm{BM.122}(3)]\\
\text{annihilation (the reverse)} & \mathcal W_{\text{ann}}=x_-^2\,\chi_{\{NE\ge\mathcal T_0\}}=16\varepsilon_q^2\chi & [\mathrm{BM.123}(1)]\\
\text{one round trip} & \mathcal W_{\text{round}}=x_+x_-=4\varepsilon_q(1-4\varepsilon_q)\le\tfrac14 & [\mathrm{BM.122}(3);\ \mathrm{BM.123}(3)]\\
\text{the full out-and-back} & \mathcal W_{\text{out-back}}=x_+^2x_-^2 & [\mathrm{BM.123}(5)]\end{array}$$
$$(2)\quad\textbf{the round trip is }\neg\textbf{the product:}\qquad \mathcal W_{\text{channel}}\cdot\mathcal W_{\text{ann}}=x_+^2x_-^2=\mathcal W_{\text{round}}^2\ \ \neg\text{is}\ \mathcal W_{\text{round}};\qquad\textbf{the round trip is ONE creation and ONE annihilation}\qquad[\mathrm{BM.123}(3)];$$
$$(3)\quad\textbf{the exact extremum:}\qquad x_+x_-=\tfrac14-16\bigl(\varepsilon_q-\tfrac18\bigr)^2\qquad[\mathrm{BM.44}(7);\ \text{machine: an identity in }\mathbb Q[\varepsilon_q]];$$
$$\boxed{\ \max_{\varepsilon_q\in[0,1/4)}x_+x_-=\tfrac14\ \ \text{at}\ \ \varepsilon_q=\tfrac18\ }\qquad \Gamma_{\mathrm{tr}}(\varepsilon_q)=\frac{x_+x_-}{1-x_+x_-}\in\bigl[0,\tfrac13\bigr];$$
$$(4)\quad\textbf{the detailed-balance indicator:}\qquad \boxed{\ \frac{\mathcal W_{\text{ann}}}{\mathcal W_{\text{channel}}}=\Bigl(\frac{x_-}{x_+}\Bigr)^2=\Bigl(\frac{4\varepsilon_q}{1-4\varepsilon_q}\Bigr)^2\ =1\iff\varepsilon_q=\tfrac18\ }\qquad[\mathrm{BM.123}(2)];$$
$$<1\iff\varepsilon_q<\tfrac18;\qquad >1\iff\varepsilon_q>\tfrac18;\qquad \varepsilon_q=0:\ \text{ratio }0\ (\textbf{nothing annihilates});\qquad \varepsilon_q\to\tfrac14^-:\ \text{diverges};$$
$$(5)\quad\textbf{the amplitudes and cross-sections (formed, symbolic):}\qquad \mathcal M_{\mathrm{pair}}=e_0^2q^2x_+^2\chi\cdot\frac{N(k,E)f(k)}{1+G(E)},\qquad \mathcal M_{\mathrm{ann}}=e(k,E)^2q^2x_-^2\chi\qquad[\mathrm{BM.142}(3),(5)];$$
$$\sigma_{\mathrm{pair}}=\frac{e_0^4q^4x_+^4\chi Nf^2}{16\pi z^3(1+G)^2}\sqrt{z^2-4N^2(2m_{\mathrm{hid}})^2},\qquad \sigma_{\mathrm{ann}}=\frac{e_0^4q^4x_-^4\chi Nf^2}{16\pi z(1+G)^2\sqrt{z^2-4N^2(2m_{\mathrm{hid}})^2}};$$
$$[\sigma_{\mathrm{pair}}]=[\sigma_{\mathrm{ann}}]=\mathfrak q^{-1}=\text{the area species of }(\Delta x_{\mathrm B})^2;\qquad \boxed{\ \frac{\sigma_{\mathrm{ann}}}{\sigma_{\mathrm{pair}}}=\Bigl(\frac{x_-}{x_+}\Bigr)^4\frac{z^2}{z^2-4N^2(2m_{\mathrm{hid}})^2}\ }\qquad[\mathrm{BM.142}(4),(5),(6)];$$
$$|\mathcal M_{\mathrm{ann}}|=|\mathcal M_{\mathrm{pair}}|\iff\varepsilon_q=\tfrac18\qquad[\mathrm{BM.142}(6):\ \text{detailed balance elevated to the amplitude}];$$
$$(6)\quad\textbf{the threshold:}\qquad \mathcal T_0(\text{pair})=\frac{E^{\text{pair}}_{\mathrm{int}}\mathfrak h}{\ln2}=\frac{2E_{\mathrm{int}}(c)\mathfrak h}{\ln2};\qquad \text{at the minimal floor }E_{\mathrm{int}}(c)=2:\ \ \mathcal T_0=\frac{4\mathfrak h}{\ln2};$$
$$\text{materialization}\iff NE\ge\mathcal T_0;\qquad \mathcal T(\text{pair};N)=\frac{4\mathfrak h}{N\ln2};\qquad \text{the ladder spans }\Bigl\{\tfrac{4\mathfrak h}{\ln2},\dots,\tfrac{120\mathfrak h}{\ln2}\Bigr\},\ \text{span ratio exactly }30;$$
$$(7)\quad\textbf{the exact zeros of the pair amplitude:}\qquad \mathcal M=0\iff e_0=0\ \vee\ q=0\ \vee\ \varepsilon_q=\tfrac14\ \vee\ \chi=0\ \vee\ N=0\ \vee\ f=0\qquad[\mathrm{BM.142}(3)];$$
$$(8)\quad\textbf{the entropy destination:}\qquad n_{\mathcal R}=0\implies\rho_{pq}=\rho_\circ=\tfrac14I,\qquad S_{\mathrm{raw}}(\rho_\circ)=\ln4=\max,\qquad \arg\max=\{\tfrac14I\}\qquad[\mathrm{BM.123}(4);\ \mathrm{A5}];$$
$$(9)\quad\textbf{status: derived.}\qquad\neg\text{a numerical cross-section, rate or branching fraction is evaluated}\ [\mathrm{P5};\ \mathrm{BM.44}(5)];\ \neg\text{external seconds}\ [\mathrm{BM.44}(3)].$$

**Req.** D0.4, CT0.8, A5 (Part 1); EM.25(7), CT2.1 (Part 2); AT.16, AT.21 (this tier); Def-BM.17(3),(4), Def-BM.18(5), Def-BM.20(4),(5), BM.13(3), BM.44(4),(5),(7), BM.88(2),(3), BM.109(1),(2), BM.111(1),(5), BM.115(1),(2)(i),(4), BM.116(1), BM.120(5), BM.121(2),(4),(5), BM.122(1),(2),(3), BM.123(1),(2),(3),(4),(5), BM.132(2), BM.133(4),(6), BM.134(4), BM.142(2)–(9), BM.143(4), Census FT.28, FT.79(5) (Part 4); exact rational-function division, exact polynomial identities in $\mathbb Q[\varepsilon_q]$, exact extremum on a 251-point rational grid, Laurent-monomial exponent censuses [math; machine: `cp_tensor.py` §§B–C].

**Pf.** $(2)$: $x_+^2\cdot x_-^2=(x_+x_-)^2$ and $x_+x_-\ne(x_+x_-)^2$ on the admissible range. $(3)$: $\tfrac14-16(\varepsilon_q-\tfrac18)^2=\tfrac14-16\varepsilon_q^2+4\varepsilon_q-\tfrac14=4\varepsilon_q-16\varepsilon_q^2=(1-4\varepsilon_q)(4\varepsilon_q)=x_+x_-$ [machine: coefficient-wise in $\mathbb Q[\varepsilon_q]$]. $(4)$: $x_-^2/x_+^2=1\iff x_-=x_+\iff4\varepsilon_q=1-4\varepsilon_q\iff\varepsilon_q=\tfrac18$; monotone in $\varepsilon_q$ on $[0,\tfrac14)$ [machine: eight exact thresholds]. $\blacksquare$

**Phys.** The two histories are weighted by monomials in one parameter, and their ratio is a pure
function of the crystallization threshold: creation dominates below $\varepsilon_q=\tfrac18$,
annihilation above it, and at exactly $\tfrac18$ the two amplitudes are equal in modulus — the
corpus's own detailed-balance point, which is also where the round-trip weight and the transit
rate attain their maxima. Nothing annihilates at $\varepsilon_q=0$, which is the no-flicker limit;
the channel diverges as $\varepsilon_q\to\tfrac14^-$. The threshold gate $\chi_{\{NE\ge\mathcal T_0\}}$
carries $E_{\mathrm{int}}$ into every weight, and the metric profile carries it again through
$N$, $f$ and $G$.

---

### AT.23 — The state space of the CP-assimilated tensor: $\mathcal T_{\mathcal J}^2$, not $\mathcal H_{\text{meson}}$

**Thm.**
$$(1)\quad\textbf{the two spaces, and they are different:}\qquad \mathcal T_{\mathcal J}(c)=\mathcal J\otimes\mathcal H_\omega(c)\otimes\Psi(c),\qquad \dim\mathcal T_{\mathcal J}(c)=4\,(|k(c)|+1)\qquad[\mathrm{Def\text{-}BM.18}(4)];$$
$$\mathcal T_{\mathcal J}^{\,2}(c):=\mathcal T_{\mathcal J}(c)\otimes\mathcal T_{\mathcal J}(c^{\mathrm{CP}}),\qquad \boxed{\ \dim\mathcal T_{\mathcal J}^{\,2}=16\,(|k|+1)^2\ };$$
$$\mathcal H_2(c_1,c_2)=\mathcal H_\omega(c_1)\otimes\Psi(c_1)\otimes\mathcal H_\omega(c_2)\otimes\Psi(c_2),\qquad \dim\mathcal H_2=4(|k_1|+1)(|k_2|+1)\qquad[\mathrm{Def\text{-}BM.16}(2)];$$
$$\mathcal H_{\text{meson}}(c)=\mathcal H_2(c,c^{\mathrm{CP}}),\qquad \dim\mathcal H_{\text{meson}}=4(|k|+1)^2\qquad[\mathrm{BM.110}(2)];$$
$$(2)\quad\textbf{the exact relation:}\qquad \boxed{\ \mathcal T_{\mathcal J}^{\,2}(c)\ =\ (\mathcal J\otimes\mathcal J)\ \otimes\ \mathcal H_{\text{meson}}(c),\qquad \dim(\mathcal J\otimes\mathcal J)=4,\qquad 16(|k|+1)^2=4\cdot4(|k|+1)^2\ }$$
$$(3)\quad\textbf{the consequence, and it decides the directive's step 1:}\qquad\textbf{the two histories are separated by the JANUS factor }\mathcal J\otimes\mathcal J,\ \neg\text{by }\mathcal H_{\text{meson}};$$
$$\mathcal H_{\text{meson}}(c)\ \textbf{cannot distinguish History A from History B},\ \text{because both carry the same orientation and winding data};$$
$$\textbf{the CP-assimilated tensor must be built on }\mathcal T_{\mathcal J}^{\,2}(c),\ \textbf{and }\mathcal H_{\text{meson}}(c)\ \textbf{is its quotient by the register};$$
$$(4)\quad\textbf{the register factor's four basis states, mapped to the histories:}\qquad\begin{array}{l|l|l}
\text{state of }\mathcal J\otimes\mathcal J & \text{the register content} & \text{the history}\\ \hline
|\mathcal R\rangle|\mathcal R\rangle & \text{both crystallized} & \textbf{A}:\ \text{retained, no boundary dissolution}\\
|\mathcal R\rangle|\mathcal V\rangle,\ |\mathcal V\rangle|\mathcal R\rangle & \text{one dissolved} & \text{partial: the flicker window}\\
|\mathcal V\rangle|\mathcal V\rangle & \text{both dissolved} & \textbf{B}:\ \text{the annihilation move }\hat J_-\otimes\hat J_-\ \text{has fired}\end{array}$$
$$(5)\quad\textbf{the exchange structure on }\mathcal T_{\mathcal J}^{\,2}:\qquad \hat P_{12}=\hat\mu_{\mathrm{CP}}\circ\hat S_{12},\quad \hat P_{12}^2=\mathrm{id},\quad \varepsilon(c)=\mu_{\mathrm{CP}}(c)|_{\vee^2}=i^{\Theta(c)}=(-1)^{|k(c)|}\qquad[\mathrm{Def\text{-}BM.16}(4),(5)];$$
$$\Theta(c^{\mathrm{CP}})=\Theta(c)\ \ \text{on the materialized locus}\qquad[\mathrm{BM.113}(2)(\mathrm{ii})]\implies \varepsilon(c^{\mathrm{CP}})=\varepsilon(c);$$
$$(6)\quad\textbf{the meson is a boson, unconditionally:}\qquad k_M=2k\implies \varepsilon_M=(-1)^{|2k|}=+1,\qquad j_M=k\in\mathbb Z\qquad[\mathrm{BM.129}(1)];$$
$$\textbf{robust:}\ k(c^{\mathrm{CP}})=-k(c)\ \text{gives}\ k_M=0,\ \varepsilon_M=+1\ \text{-- the STATISTICS is robust, the total spin is not}\qquad[\mathrm{BM.129}(2)];$$
$$(7)\quad\textbf{status: derived.}$$

**Req.** A3, A4 (Part 1); Def-H.33, Def-H.38, EW.32 (Parts 2–3); AT.21 (this tier); Def-BM.15(2),(3), Def-BM.16(1),(2),(3),(4),(5), Def-BM.18(4), BM.108(3), BM.110(2), BM.113(2), BM.127, BM.128(1),(2),(7), BM.129(1),(2),(3), BM.136(3) (Part 4); exact integer dimension arithmetic [math; machine: `cp_tensor.py` §C].

**Pf.** $(2)$: $\mathcal T_{\mathcal J}^{\,2}=(\mathcal J\otimes\mathcal H_\omega\otimes\Psi)\otimes(\mathcal J\otimes\mathcal H_\omega\otimes\Psi)$ rearranges as $(\mathcal J\otimes\mathcal J)\otimes(\mathcal H_\omega\otimes\Psi\otimes\mathcal H_\omega\otimes\Psi)=(\mathcal J\otimes\mathcal J)\otimes\mathcal H_2$; at $c_2=c^{\mathrm{CP}}$, $|k(c^{\mathrm{CP}})|=|k(c)|$, giving $16(|k|+1)^2=4\cdot4(|k|+1)^2$ [machine: exact integers at $k=0..6$]. $(3)$: the register factor is exactly what $\mathcal H_{\text{meson}}$ omits. $(5),(6)$: re-cited. $\blacksquare$

**Phys.** The directive's step 1 asks how to write the CP-assimilated tensor as a superposition.
The answer is that the tensor product already exists and already separates the two histories —
but not in the space one would first reach for. $\mathcal H_{\text{meson}}$ carries orientation and
winding; both histories share those, so it cannot tell them apart. The distinction lives in the
Janus factor $\mathcal J\otimes\mathcal J$, whose four basis states are: both crystallized
(History A), one dissolved (the flicker window), and both dissolved (History B, the annihilation
move having fired). So the CP-assimilated tensor is $\mathcal T_{\mathcal J}^{\,2}(c)$, and
$\mathcal H_{\text{meson}}(c)$ is what remains after the register is forgotten. Since the meson is
unconditionally a boson and its statistics is robust under the unresolved orientation-sign row,
both histories carry $\varepsilon_M=+1$ — the statistics does not discriminate them either.

---

### AT.24 — The path integral is ONE configuration sum, and $E_{\mathrm{int}}$ enters four ways

**Thm.**
$$(1)\quad\textbf{the corpus has no history-kets.}\ \text{Its objects are:}$$
$$Z(\mathcal R)=\!\!\sum_{C\in\mathfrak C(\mathcal R)}\sum_\sigma\!\! w(C),\quad w(C)=\mathcal J(C)\!\!\prod_{e\in E(C)}\!\!G(e)\cdot(-1)^{\aleph(\sigma,C)}\qquad[\mathrm{A8};\ \mathrm{C12};\ \mathrm{D0.10}];$$
$$Z(\mathcal X)=\sum_{R\in\mathcal E(\mathcal X)}\sum_\sigma w(R,\sigma)\qquad[\mathrm{Def\text{-}H.32}(2),\ \text{topology-blind}];\qquad Z(\mathcal R,\Sigma)=\Bigl\langle\mathrm{out}\Bigl|\bigl(1-\mathbf F_M^{(\Sigma)}\bigr)^{-1}\Bigr|\mathrm{in}\Bigr\rangle\qquad[\mathrm{Def\text{-}H.16}];$$
$$(2)\quad\textbf{so the ``superposition of two histories'' is a decomposition of the sum by move-class:}$$
$$\boxed{\ Z=Z_A+Z_B,\qquad Z_A:\ \text{configurations with no boundary dissolution},\qquad Z_B:\ \text{configurations carrying }\hat J_-\otimes\hat J_-\ }$$
$$\textbf{and both are already inside ONE Def-H.32 sum, because}\qquad |\mathcal E(\mathcal X)|>1\iff x_->0\iff \varepsilon_q>0\qquad[\mathrm{BM.19}(6)];$$
$$\textbf{History A and History B are two REGIONS of one sum, }\neg\textbf{two sums and }\neg\textbf{two kets};$$
$$(3)\quad\textbf{the relative weight is a ratio of monomials, }\neg\textbf{amplitudes }\alpha,\beta:\qquad \frac{Z_B}{Z_A}\ \text{carries}\ \frac{x_-^2}{x_+^2}=\Bigl(\frac{4\varepsilon_q}{1-4\varepsilon_q}\Bigr)^2\ \text{times the kinematic factor}\qquad[\mathrm{AT.22}(4);\ \mathrm{BM.142}(6)];$$
$$(4)\quad\textbf{how }E_{\mathrm{int}}\textbf{ enters the weighting — through FOUR derived channels, }\neg\textbf{as a bare node count:}$$
$$\begin{array}{l|l|l}
\text{(i)}\ \text{the threshold gate} & \chi_{\{NE\ge\mathcal T_0\}},\quad \mathcal T_0=E_{\mathrm{int}}\mathfrak h/\ln2 & [\mathrm{BM.115}(1);\ \mathrm{BM.122}(2)]\\
\text{(ii)}\ \text{the curvature lock} & G=2\pi E_{\mathrm{int}}^2\ln2 & [\mathrm{BM.88}(3)]\\
\text{(iii)}\ \text{the lapse} & N^2=1-\dfrac{G}{4\pi k}=1-\dfrac{\mathfrak hE_{\mathrm{int}}}{2r} & [\mathrm{BM.132};\ \mathrm{BM.146}(3);\ \mathrm{AT.1}(3)]\\
\text{(iv)}\ \text{the profile} & \mathsf g=\dfrac1{1+G},\quad f=1-\dfrac1k,\quad e^2=e_0^2\dfrac{Nf}{1+G} & [\mathrm{BM.133}(4),(6);\ \mathrm{BM.88}(2)]\end{array}$$
$$\boxed{\ \mathcal M_{\mathrm{ann}}=e_0^2q^2x_-^2\chi\cdot\frac{Nf}{1+G}\ }:\qquad E_{\mathrm{int}}\ \textbf{is inside }\chi,\ N,\ f\ \textbf{and }G\ \textbf{simultaneously};$$
$$(5)\quad\textbf{the flicker measure itself:}\qquad P_{\mathrm{mat}}(E{=}2j)=\binom njp^ju^{n-j}/(1-u^n),\quad j\ge1,\qquad p=1-4\varepsilon_q,\ u=4\varepsilon_q\qquad[\mathrm{BM.137}(1);\ \mathrm{AT.6}(3)];$$
$$\textbf{the normalizer is }1-u^n=pD_n,\ \neg D_n;\qquad w_{\mathrm{mat}}^{(n)}=\tfrac1{D_n}\ \textbf{is the crystallization weight};$$
$$(6)\quad\textbf{status: derived, with (2)'s reframing of the directive's step 2.}$$

**Req.** A8, C12, D0.10, D2.4, D2.5, CT2.5 (Parts 1–2); Def-H.15(3), Def-H.16, Def-H.32(1),(2),(4) (Part 3); AT.1(3), AT.6(3), AT.21, AT.22, AT.23 (this tier); BM.19(6), BM.88(2),(3), BM.115(1), BM.122(2), BM.132, BM.133(4),(6), BM.137(1), BM.142(3),(5),(6), BM.146(3), Def-BM.5(4) (Part 4); exact monomial censuses, exact rational-function ratios [math; machine: `cp_tensor.py` §E].

**Pf.** $(2)$: Def-H.32(1)'s ensemble is a set of edge subsets $R$ preserving the boundary data; a configuration whose boundary registers end in $\mathcal V$ is exactly one on which $\hat J_-$ has fired, so the two move-classes partition $\mathcal E(\mathcal X)$; BM.19(6) gives $|\mathcal E|>1\iff\varepsilon_q>0$. $(4)$: substitute AT.22(5)'s $\mathcal M_{\mathrm{ann}}=e(k,E)^2q^2x_-^2\chi$ with BM.133(6)'s $e^2=e_0^2Nf/(1+G)$. $\blacksquare$

**Phys.** The directive's $|\Psi\rangle=\alpha|D^-_{\text{merged}}\rangle+\beta|\text{Radiation Flash}\rangle$
is not an object the corpus can host: there are no history-kets, and there is no need of them.
What exists is one configuration sum whose terms sort into two move-classes, and whose relative
weight is a ratio of monomials in the crystallization threshold rather than a pair of complex
amplitudes. That is a weaker-looking statement and a stronger one: the ratio is exact and depends
on a single derived parameter, whereas $\alpha,\beta$ would have to be supplied. And $E_{\mathrm{int}}$
does not weight the histories as a bare count — it enters four times over, through the threshold
gate, the curvature lock, the lapse and the coupling profile, all at once.

---

### AT.25 — The obstruction check: the bar is re-scoped, and the real obstruction is the mask

**Thm.**
$$(1)\quad\textbf{what stands frozen (re-scoped at its own locus, }\neg\textbf{retracted):}\qquad \neg\exists\ \textbf{a DIRECT}\ \mathrm{EM}^+\to\mathrm{EM}^-\ \textbf{operator};\qquad\text{the two sectors remain amplitude-equal configuration orbits of one involution},\ |w(c^{\mathrm{CP}})|^2=|w(c)|^2\qquad[\mathrm{BM.123}(5),(8);\ \mathrm{BM.25}(4);\ \mathrm{BM.27}(6),(7);\ \mathrm{BM.29}(5);\ \mathrm{Def\text{-}BM.7}(5);\ \mathrm{Def\text{-}BM.15}(5);\ \mathrm{BM.108}(7);\ \mathrm{BM.109}(5)];$$
$$(2)\quad\textbf{what is constructed:}\qquad \boxed{\ \textbf{a MEDIATED channel}\ —\ \mathcal J\text{'s two moves composed with }\mathrm{Def\text{-}BM.15}(2)\text{'s CP identification}\ —\ \textbf{connects the two sectors THROUGH the }\mathcal V\textbf{ sector, }\neg\textbf{through a direct operator}\ }$$
$$\varnothing\xrightarrow{\ \hat J_+\otimes\hat J_+\ }\{c,c^{\mathrm{CP}}\}\xrightarrow{\ \hat J_-\otimes\hat J_-\ }\varnothing,\qquad \text{weight}\ x_+^2x_-^2;\qquad \neg\text{a cross-section is attached to THAT row}\ [\mathrm{Def\text{-}BM.18}(6);\ \mathrm{BM.6}(6)];$$
$$(3)\quad\textbf{the residues are closed:}\qquad \begin{array}{l|l}
(\mathrm{R9})\ \text{the annihilation channel} & \textbf{CLOSED at the channel level}:\ \text{exact weight }x_-^2\chi,\ \text{exact threshold }\mathcal T_0,\ \text{exact charge balance, exact entropy destination}\ [\mathrm{BM.123}(6)]\\
(\mathrm{R9}')\ \text{the annihilation cross-section} & \textbf{CLOSED}:\ \sigma_{\mathrm{ann}}\ \text{constructed as an exact symbolic chart-side read on the formed domain}\ [\mathrm{BM.142}(5),(8)]\\
(\mathrm{R9}'')\ \text{the radiation legs} & \textbf{CLOSED at the vertex level}:\ \text{the two-transit-quantum supply vertex, nilpotent, charge-balanced, threshold-gated}\ [\mathrm{BM.142}(2),(8)]\end{array}$$
$$(4)\quad\textbf{so step 5's dichotomy has a THIRD answer:}\qquad\textbf{neither.}\ \ \text{The bar does }\neg\text{block History B, and it is }\neg\text{merely a cross-section bar: the channel AND the cross-section are both constructed. What remains barred is a DATA bar:}$$
$$\neg\text{a numerical cross-section, rate or branching fraction}\ [\mathrm{P5};\ \mathrm{BM.44}(5)];\quad \neg\text{an S-matrix unitarity claim}\ [\mathrm{Def\text{-}BM.20}(5)];\quad \neg\text{external seconds}\ [\mathrm{BM.44}(3)];\quad e_0\ \text{remains calibration};\quad \text{amplitude}\ne\text{mass}\ [\mathrm{FT.79}(5)];$$
$$(5)\quad\textbf{THE ACTUAL OBSTRUCTION to the directive's stated object is the MASK, and it is harder:}$$
$$\mathrm{Def\text{-}BM.18}(1):\ \mathcal J\ \textbf{is the two-state register of ONE PAIR};\qquad \mathrm{Def\text{-}BM.18}(4):\ \mathcal T_{\mathcal J}(c)\ \textbf{is built on a CHAIN }c;$$
$$D^-\ \textbf{is neither}: it is the vertex oversubscription excess\ O(n)=\max(0,2^{n+1}-16),\ \text{absorbed at rate}\propto O(n)\qquad[\mathrm{CT0.6};\ \mathrm{CT4.1};\ \mathrm{D4.1};\ \mathrm{D4.2};\ \mathrm{BM.149}(2);\ \mathrm{AT.16}];$$
$$(6)\quad\textbf{and the mask annihilates it at every accessible rung:}\qquad \forall n\le3:\ \ \mathcal P_M^{(n)}F_{D^-}\mathcal P_M^{(n)}=0,\qquad \neg\exists\ \text{a pole of }Z(\mathcal R,n)\ \text{carrying locked content}\qquad[\mathrm{CT4.2};\ \mathrm{BM.149}(3);\ \mathrm{AT.17}(4)];$$
$$\text{locked content: physical norm }0\ \text{at accessible rungs},\quad w(C)\ne0\ \text{in the unmasked A8 sum},\quad \neg\exists\ \text{a deleted entry}\qquad[\mathrm{CT4.3};\ \mathrm{CT2.8}];$$
$$(7)\quad\textbf{the two consequences, exactly:}\qquad(\mathrm i)\ \ \text{the masked resolvent}\ Z(\mathcal R,\Sigma)=\langle\mathrm{out}|(1-\mathbf F_M^{(\Sigma)})^{-1}|\mathrm{in}\rangle\ [\mathrm{Def\text{-}H.16}]\ \textbf{has }\neg\textbf{a }D^-\textbf{ pole};$$
$$(\mathrm{ii})\ \ \mathcal T_{\mathcal J}(D^-)\ \textbf{is not defined by any clause},\ \text{since }\mathcal J\ \text{is a pair register and }D^-\ \text{content is vertex excess};$$
$$\boxed{\ \textbf{History A (the smooth merger of two }D^-\textbf{ sectors) is }\neg\textbf{formed}\ —\ \neg\textbf{because a bar forbids it, but because }D^-\textbf{ has no accessible state space to merge in}\ }$$
$$(8)\quad\textbf{what IS well-formed, and is adjacent:}\qquad\textbf{the meson-floor CP-pair channel on }\mathcal T_{\mathcal J}^{\,2}(c)\ \textbf{for a chain }c\ \textbf{and its CP conjugate}. Every element the directive asks for exists there, completely: the state space (AT.23), the two moves and their nilpotence (AT.21), the four weights and the detailed-balance point (AT.22), the threshold gate, the amplitudes, the cross-sections, the charge balance }Q_{\mathrm{in}}=Q_{\mathrm{out}}=0\ \text{with}\ Q_{\mathrm{EM}}=\sum q=0\ \text{surviving in every valid universe}\ [\mathrm{BM.122}(1);\ \mathrm{EM.11};\ \mathrm{D2.11}],\ \text{and the entropy destination}\ S_{\mathrm{raw}}=\ln4\ [\mathrm{BM.123}(4)];$$
$$(9)\quad\textbf{status:}\qquad\textbf{derived:}\ (1)\text{--}(8);\qquad\textbf{the directive's step-5 premise is stale and is corrected here};\qquad\textbf{nothing is adopted}. $$

**Req.** A8, A9, D2.11, D4.1, D4.2 (Part 1); CT0.6, CT2.8, CT4.1, CT4.2, CT4.3, CT4.5, EM.11 (Part 2); Def-H.15(3), Def-H.16, Def-H.32, FT.79(5) (Part 3); AT.16, AT.17(4), AT.21–AT.24 (this tier); Def-BM.7(5), Def-BM.15(2),(5), Def-BM.18(1),(4),(6), Def-BM.20(5), BM.6(5),(6), BM.25(4), BM.27(6),(7), BM.29(5), BM.44(3),(5), BM.108(3),(7), BM.109(5), BM.118(7), BM.122(1),(6), BM.123(5),(6),(8), BM.130(3),(7), BM.142(2),(5),(8),(9), BM.143(4), BM.149(1),(2),(3) (Part 4) [math; machine: `cp_tensor.py` §D].

**Pf.** $(1)$–$(3)$: re-citation of the frozen, constructed and closed rows at their own loci, with BM.123(8)'s disposition list read in full. $(6)$–$(7)$: $\mathbf F_M^{(\Sigma)}=\mathcal P_M^{(\Sigma)}\mathbf F\mathcal P_M^{(\Sigma)}$ [Def-H.15(3)], and $\mathcal P_M^{(n)}F_{D^-}\mathcal P_M^{(n)}=0$ for every accessible $n$ [CT4.2], so the $D^-$ block contributes nothing to $(1-\mathbf F_M^{(\Sigma)})^{-1}$; a resolvent pole requires $1\in\operatorname{spec}\mathbf F_M^{(\Sigma)}$ [Def-H.16; CT2.5], which the annihilated block cannot supply. $\blacksquare$

**Phys.** The directive anticipated a bar and asked the right question about it, but the bar had
already moved. What stands frozen is narrow and structural: there is no *direct* operator taking
one sector to the other. What exists is a *mediated* channel running through the virtual sector —
out by $\hat J_+\otimes\hat J_+$, back by $\hat J_-\otimes\hat J_-$ — with an exact weight, an exact
threshold, exact charge balance, an exact entropy destination, and now an exact cross-section.
Residues (R9), (R9′) and (R9″) are all closed.

The obstruction that *does* bite is a different one and it is not a prohibition but an absence of
footing. $D^-$ is vertex oversubscription excess, not a pair and not a chain; the Janus register
is defined on pairs and its crossing space on chains; and the mask annihilates the $D^-$ block at
every accessible rung, so the resolvent has no $D^-$ pole to sum over. A path integral over $D^-$
histories therefore has nothing to integrate. This is the same shape as AT.17's finding: the
locked sector is retained in full and exposed not at all.

The good news is that the object the directive is reaching for exists one level down, complete and
exact: the CP-pair channel on the meson floor. It is a chain-and-its-conjugate merger, not a
$D^-$-merger, and everything asked for — state space, two histories, weights, threshold,
amplitudes, cross-sections, entropy destination — is already constructed.

---

### AT.26 — Locus discipline on the CP premise

**Thm.**
$$(1)\quad\textbf{the two reversals, at two loci:}\qquad\begin{array}{l|l|l}
\text{the reversal} & \text{the action} & \text{the locus}\\ \hline
\text{the metric time-reversal pullback} & (a_{00},q,w)\mapsto(a_{00},q,-w)\iff g_{00},g_{ij}\ \text{fixed},\ g_{0i}\mapsto-g_{0i} & [\mathrm{FT.156}(3);\ \text{machine}]\\
\text{the record reversal} & \Theta_{\mathfrak L},\qquad w(\Theta_{\mathfrak L}C)=w(C)^* & [\mathrm{D2.7};\ \mathrm{CT2.8}(1),(2)]\end{array}$$
$$(2)\quad\textbf{the locus bar:}\qquad \boxed{\ \text{the register grading [A3] and the record reversal [D2.7] act on DIFFERENT SPACES}\ —\ \textbf{the identity is of the TIME ENTITY (the order parameter), }\neg\textbf{an operator equality}\ }\qquad[\mathrm{FT.159}(3);\ \mathrm{FT.134}(1)\ \text{pattern}];$$
$$(3)\quad\textbf{so the directive's premise is admissible as a paired reading and barred as an equation:}\qquad\text{``the antimatter sector is the CP conjugate, with }w_i\to-w_i\text{, charges flipped, identical }E_{\mathrm{int}}\ \text{and spatial geometry''}$$
$$\textbf{is CORRECT as a reading}:\quad (N,\gamma_{ij})\ \text{are fixed under}\ w\mapsto-w\ [\mathrm{BM.34}(3)];\qquad m(c^{\mathrm{CP}})=m(c)\ [\mathrm{BM.27};\ \mathrm{BM.108}(3)];$$
$$\Theta(c^{\mathrm{CP}})=\Theta(c)\ \ \text{on the materialized locus}\ [\mathrm{BM.113}(2)(\mathrm{ii})];\qquad |w(c^{\mathrm{CP}})|^2=|w(c)|^2\ [\mathrm{BM.27}(6)];$$
$$\textbf{and BARRED as an operator identity}\ \Theta_{\mathfrak L}=(w\mapsto-w)\ \ \text{by}\ (2);$$
$$(4)\quad\textbf{what is exact instead:}\qquad\text{one order parameter, four tags}\ [\mathrm{D0.7}\ \text{ticks};\ \mathrm{D1.8}\ x^0;\ \mathrm{CT2.6}\ \text{charts};\ \mathrm{D2.7}\ \Theta_{\mathfrak L}]\ —\ \textbf{no second time entity exists}\ [\mathrm{FT.159}(3);\ \text{scan}];$$
$$(5)\quad\textbf{the arrow rows stand:}\qquad \neg\exists\,\tau^{-1}\ [\mathrm{A6}];\qquad\text{the channel is forward-only};\qquad\textbf{the reversibility is in the move set and the stationary measure, }\neg\textbf{in the tick}\qquad[\mathrm{BM.123}(7);\ \mathrm{BM.120}(3),(7);\ \mathrm{FT.144}(2)\text{--}(4)];$$
$$(6)\quad\textbf{status: derived; (3)'s first row is a scope clause, not a new claim.}$$

**Req.** A3, A6, D0.7, D1.8, D2.6, D2.7 (Part 1); CT2.6, CT2.8(1),(2) (Part 2); FT.134(1), FT.156(3), FT.159(1)–(3), FT.159(5) (Part 3); AT.21, AT.25 (this tier); BM.27(6), BM.34(3), BM.108(3), BM.113(2), BM.120(3),(7), BM.123(7), BM.149(5), Def-BM.15(2), FT.144(2)–(4) (Part 4) [math; machine: `cp_tensor.py` §E].

**Pf.** Re-citation with the locus rows kept apart; FT.159(3)'s discipline clause is the
governing row. $\blacksquare$

**Phys.** The premise that an antimatter sector is the CP conjugate with a flipped shift and
identical geometry is *right as physics reading* — the lapse and the spatial metric are invariant
under $w\mapsto-w$, the mass and the winding are CP-invariant, and the amplitudes are equal. But
the corpus keeps two reversals at two loci and refuses to equate them as operators, because the
metric pullback acts on coefficient fields and the record reversal acts on configuration records.
Writing $\Theta_{\mathfrak L}=(w\mapsto-w)$ would collapse that discipline and is barred. The
usable statement is that both are the same *order parameter* read at two loci — one time entity,
four tags, no second time.

---

### AT.27 — Tier AT.4 status, and what is missing from the canon

**Thm.**
$$(1)\quad\textbf{STRUCTURALLY VALID, on the meson floor:}\qquad\textbf{the CP-assimilated tensor is well-formed as }\mathcal T_{\mathcal J}^{\,2}(c)=(\mathcal J\otimes\mathcal J)\otimes\mathcal H_{\text{meson}}(c),\ \dim=16(|k|+1)^2;$$
$$\text{the two histories are its register classes; the path integral is one Def-H.32 sum decomposed by move-class; the weights are exact monomials in }(x_+,x_-);\ \text{the relative weight is their ratio, peaking at }\varepsilon_q=\tfrac18;$$
$$(2)\quad\textbf{NOT FORMED, on the }D^-\textbf{ sector:}\qquad\neg\exists\ \mathcal T_{\mathcal J}(D^-),\ \text{and the masked resolvent has }\neg\text{a }D^-\ \text{pole};\ \text{so a }D^-\text{--}D^-\ \text{merger path integral is }\neg\text{constructible from the present inventory};$$
$$(3)\quad\textbf{what is missing from the canon, named precisely — four rows, in ascending cost:}$$
$$\begin{array}{l|l|l}
(\mathrm{M1}) & \textbf{a }D^-\textbf{ state space} & \text{the Janus register is defined on ONE PAIR [Def-BM.18(1)] and }\mathcal T_{\mathcal J}\ \text{on a CHAIN [Def-BM.18(4)]; }D^-\ \text{is vertex excess }O(n).\ \textbf{A new definition is required.}\\
(\mathrm{M2}) & \textbf{an unmasked read of the locked sector} & \mathcal P_M^{(n)}F_{D^-}\mathcal P_M^{(n)}=0\ \forall n\le3\ [\mathrm{CT4.2}].\ \text{Any }D^-\ \text{path integral needs a rung }n\ge4\ \text{mask, and CT0.13 gives }\mathcal A(n\ge4)=\mathcal A(3)\cup\{D^-\}\ \text{with }\dim\mathcal K_{n\ge4}\ \text{beyond }25.\ \textbf{Unexplored in the frozen canon.}\\
(\mathrm{M3}) & \textbf{a superposition law for the shift across two subnetworks} & \text{the directive's ``the shifts cancel, }+w_i-w_i=0\text{'' assumes linearity of }w\ \text{across subnetworks.}\ w_i\ \text{is a per-edge metric coordinate [Def-H.14], and AT.5 determines only its LONGITUDINAL projection }w\!\cdot\!\Delta x\ \text{per edge.}\ \neg\exists\ \text{a derived additivity law for }w.\ \textbf{A new theorem or a declared composition is required.}\\
(\mathrm{M4}) & \textbf{the connector contribution} & \text{the directive's }E_{\mathrm{int}}\to E_{\mathrm{int}}^{(1)}+E_{\mathrm{int}}^{(2)}\ \text{is exact for DISJOINT edge sets, but a junction carries a connector:}\ k(\Gamma)=k_1+k_2+d_{12}\ [\mathrm{FT.34}(3);\ \mathrm{BM.2}(2)].\ \textbf{The merged }E_{\mathrm{int}}\ \text{needs the connector term.}\end{array}$$
$$(4)\quad\textbf{the bars that stand, unchanged:}\qquad\neg\text{a numerical cross-section, rate or branching fraction}\ [\mathrm{P5};\ \mathrm{BM.44}(5)];\quad\neg\text{external seconds}\ [\mathrm{BM.44}(3)];\quad\neg\text{an S-matrix unitarity claim}\ [\mathrm{Def\text{-}BM.20}(5)];\quad e_0\ \text{remains calibration}\ [\mathrm{EM.25}(7);\ \mathrm{BM.143}(4)];\quad\text{amplitude}\ne\text{mass}\ [\mathrm{FT.79}(5)];\quad\neg\text{a species identification}\ [\mathrm{Def\text{-}BM.3}(7)];$$
$$\textbf{in particular: ``black hole'', ``matter/antimatter black hole'', ``fuzzball'' and ``radiation flash'' are all species names and are }\neg\textbf{issued.}\ \text{The corpus's own vocabulary is: the locked sector, the CP-conjugate chain, the annihilation move, the transit quanta.}$$
$$(5)\quad\textbf{the declarations this tier adds: none.}\qquad\neg\text{a P4 addition (§Cal-AT empty)},\ \neg\text{a new dimensionful scale},\ \neg\text{a measured value or an [EXT] datum},\ \neg\text{an isolated aspect applied},\ \neg\text{a smooth-manifold analogy used};$$
$$(6)\quad\textbf{the recommended route, and it is constructive:}\qquad\text{build the merger on the MESON FLOOR first, where every ingredient exists, and treat the }D^-\ \text{version as requiring (M1)+(M2):}$$
$$(\mathrm{P1})\ \text{assemble }Z=Z_A+Z_B\ \text{on }\mathcal T_{\mathcal J}^{\,2}(c)\ \text{as a decomposition of one Def-H.32 sum, with the exact monomial ratio }x_-^2/x_+^2;$$
$$(\mathrm{P2})\ \text{attach the threshold gate }\chi_{\{NE\ge\mathcal T_0\}}\ \text{with }\mathcal T_0=4\mathfrak h/\ln2\ \text{at the minimal floor, and the metric profile }Nf/(1+G);$$
$$(\mathrm{P3})\ \text{verify the detailed-balance point }\varepsilon_q=\tfrac18\ \text{as the locus where }|\mathcal M_{\mathrm{ann}}|=|\mathcal M_{\mathrm{pair}}\ \text{and }\Gamma_{\mathrm{tr}}\ \text{maximizes};$$
$$(\mathrm{P4})\ \textbf{only then}\ \text{attempt (M1)/(M2): a }D^-\ \text{state space at a rung }n\ge4\ \text{mask. This is the genuinely new construction and it is where the directive's real content lies.}$$
$$(7)\quad\textbf{machine:}\qquad\texttt{canon/era2/cp\_tensor.py}\to28/28\ \text{exact};\ \texttt{run\_all\_era2.py}\to\text{all green}. $$

**Req.** AT.16–AT.26 (this tier); P1, P5 (Parts 1–2); A8, CT0.13, CT0.14, CT4.2, CT4.3, D4.1, D4.2, EM.25(7), FT.34(3), FT.79(5) (Parts 1–3); Def-BM.3(7), Def-BM.14, Def-BM.18(1),(4),(6), Def-BM.20(5), BM.2(2), BM.6(5),(6), BM.44(3),(5), BM.142(9), BM.143(4), BM.149(1),(3) (Part 4) [math; machine: `cp_tensor.py`].

**Pf.** Assembly of AT.21–AT.26; each missing row is justified by the absence of a defining
clause, checked by citation census. $\blacksquare$

**Phys.** The scaffolding stands, and it stands on the meson floor: a four-dimensional Janus
factor times the meson's orientation-and-winding space, two histories as register classes, one
configuration sum, exact monomial weights, a single detailed-balance point at
$\varepsilon_q=\tfrac18$, and a mediated channel through the virtual sector in place of the
forbidden direct operator. What does not stand is the $D^-$ version — and the reason is not a
prohibition but a missing floor: there is no Janus register for vertex excess, and the mask
annihilates the locked block at every accessible rung, so the resolvent has no pole to weight.
Four rows name exactly what a construction would have to add, and the cheapest path is to build
the merger where the corpus already has everything, then climb to a rung-$n\ge4$ mask for the
locked sector. That climb is the real content of the directive, and it is genuinely new work
rather than assembly.

---

### AT.28 — Subnetwork observational equivalence: a locked interior and an internal Janus network are the same accessible read

**Thm.** *(This clause corrects AT.27(3)'s rows (M1) and (M2), which were framed as
constructions on the $D^-$ representative. They are not needed.)*
$$(1)\quad\textbf{three independent invisibility rows:}\qquad\begin{array}{l|l|l|l}
\text{the block} & \text{the sector} & \text{metric coords} & \text{the accessible read}\\ \hline
D^- & \text{stack aspect},\ \oplus_{n\ge4}F_n & 0 & \textbf{MASKED}:\ \mathcal P_M^{(n)}F_{D^-}\mathcal P_M^{(n)}=0\ \forall n\le3\\
J^+ & \mathcal E_{-+},\ S\text{-odd} & 0 & \textbf{not observable}\\
J^- & \mathcal E_{--},\ S\text{-odd} & 0 & \textbf{not observable}\end{array}$$
$$[\mathrm{CT4.2};\ \mathrm{BM.149}(3);\ \mathrm{FT.20};\ \mathrm{FT.30}\ \text{audit table};\ \mathrm{CT1.12a}(2);\ \mathrm{AT.2}(4)];$$
$$(2)\quad\textbf{and both are RETAINED:}\qquad w(C)\ne0\ \text{in the unmasked A8 sum},\quad \neg\exists\ \text{a deleted entry},\quad S_{\mathfrak L}=n_{\mathcal R}\ln2\ \text{retained in full on absorption}\qquad[\mathrm{CT4.3};\ \mathrm{CT2.8}];$$
$$\text{the zig-zag records ``every step in the ledger order''}\qquad[\mathrm{A6};\ \mathrm{Def\text{-}BM.18}(5)];$$
$$(3)\quad\textbf{THE DECISIVE ARITHMETIC — the locked density IS a Janus statistic:}\qquad f_{\mathrm{adm}}(n,p)=\sum_{k\le3}\binom nkp^k(1-p)^{n-k}\qquad[\mathrm{CT4.5a}(1)];$$
$$\boxed{\ 1-f_{\mathrm{adm}}(n,p)\ =\ \sum_{k\ge4}\binom nk p^k(1-p)^{n-k}\ =\ P\bigl(\mathrm{Binomial}(n,p)\ge4\bigr)\ }\qquad[\text{machine: an exact identity in }\mathbb Q[p]\ \text{at }n=4,5,6,7,8,10,12];$$
$$p=\frac{x_+}{x_++x_-}=1-4\varepsilon_q\ \ \textbf{is the Janus RETENTION probability, derived not declared}\qquad[\mathrm{BM.19}(1)\text{--}(3);\ \mathrm{Def\text{-}BM.5}(3)];$$
$$\therefore\qquad \bigl\langle\rho_{D^-}\bigr\rangle_\Gamma(p)=\sum_v O(n_v)\,P\bigl(\mathrm{Binomial}(n_v,p)\ge4\bigr)\qquad\textbf{contains }\neg\textbf{a }D^-\textbf{-specific datum};$$
$$(4)\quad\textbf{the valence-8 case (4 in, 4 out), exact:}\qquad D_{\mathrm{tick}}(8)=2^9=512,\quad C_{\mathrm{cap}}=16,\quad O(8)=496;$$
$$\begin{array}{c|cccccc}\varepsilon_q&0&\tfrac1{64}&\tfrac1{32}&\tfrac1{16}&\tfrac18&\tfrac3{16}\\ \hline p&1&\tfrac{15}{16}&\tfrac78&\tfrac34&\tfrac12&\tfrac14\\ 1-f_{\mathrm{adm}}(8,p)&1&\tfrac{4294771875}{4294967296}&\tfrac{16756579}{16777216}&\tfrac{63747}{65536}&\tfrac{163}{256}&\tfrac{7459}{65536}\\ O(8)\,(1-f_{\mathrm{adm}})&496&\tfrac{133137928125}{268435456}&\tfrac{519453949}{1048576}&\tfrac{1976157}{4096}&\tfrac{5053}{16}&\tfrac{231229}{4096}\end{array}$$
$$\textbf{strictly decreasing in }\varepsilon_q:\ \textbf{the flicker itself relieves the oversubscription},\ \text{because dissolution removes retained edges};$$
$$(5)\quad\textbf{the equivalence, with its exact scope:}\qquad\text{two configurations with the SAME boundary data}\ \bigl(\text{charge class},\ \Theta_{\mathrm{int}}\ \text{class},\ S\ \text{winding class}\bigr)\ [\mathrm{Def\text{-}BM.5}(1)]\ \text{and the same retained content }|R|$$
$$\textbf{are indistinguishable by every accessible read},\ \text{whether their interiors are}$$
$$(\mathrm a)\ \ \text{one oversubscribed vertex whose excess falls to }D^-,\qquad\text{or}\qquad(\mathrm b)\ \ \text{a refined network of admissible}(\le3)\text{-valent vertices with internal }\hat J_\pm\ \text{zig-zags};$$
$$(6)\quad\textbf{what is NOT claimed — locus discipline:}\qquad\text{the equivalence is OBSERVATIONAL,}\ \neg\text{ontological. In the UNMASKED A8 sum the two are distinct:}\ D^-=\oplus_{n\ge4}F_n\ \text{is a STACK aspect}\ [\mathrm{A8};\ \mathrm{D4.3}],\ \text{while}\ J^\pm\ \text{are }S\text{-odd aspects of the 16-dimensional PAIR ARENA}\ [\mathrm{CT0.12}];$$
$$w(C)\ne0\ \text{for locked content}\implies\textbf{the unmasked weights differ};$$
$$\boxed{\ \textbf{one accessible read, two unmasked representatives}\ —\ \textbf{a SUBNETWORK-LEVEL GAUGE REDUNDANCY},\ \neg\text{an identity of objects}\ }$$
$$(7)\quad\textbf{the mechanism already exists in the canon:}\qquad\mathrm{Def\text{-}H.32}\ \text{sums over TOPOLOGIES}\ \bigl(\mathcal G_B=\{\Gamma:\ V(\Gamma)\le B\},\ \text{isomorphism classes}\bigr)\ \text{and over edge subsets}\ \mathfrak C_B(\Gamma)=\{R\subseteq E_{\mathrm{dir}}:|R|\le B_K\};$$
$$\mathrm{Def\text{-}BM.5}(1)\ \text{indexes the ensemble by boundary data ALONE};\qquad\mathrm{BM.94}\ \text{adjudicates}\ \textbf{``the composite is an ensemble and}\neg\textbf{a topology''};$$
$$(8)\quad\textbf{AT.27(3)'s rows, re-graded:}\qquad\begin{array}{l|l|l}
\text{row} & \text{AT.27's grading} & \textbf{re-graded}\\ \hline
(\mathrm{M1})\ \text{a }D^-\ \text{state space} & \text{a new definition required} & \textbf{DISSOLVED}:\ \text{use the REPRESENTATIVE's }\mathcal T_{\mathcal J}^{\,2}(c)\ [\mathrm{AT.23}],\ \text{which exists}\\
(\mathrm{M2})\ \text{an unmasked locked read} & \text{needs a rung-}n\ge4\ \text{mask} & \textbf{DISSOLVED}:\ \text{it would be a GAUGE-FIXING act,}\ \neg\text{a derivation; CT4.2 forbids it}\\
(\mathrm{M3})\ \text{a superposition law for }w & \text{a new theorem or declaration} & \textbf{SURVIVES, SHARPENED}:\ \text{observational equivalence forces }w\ \textbf{invariant across representatives} — \text{a CONSTRAINT, and testable}\\
(\mathrm{M4})\ \text{the connector term }d_{12} & \text{survives} & \textbf{SURVIVES unchanged}\ [\mathrm{FT.34}(3);\ \mathrm{BM.2}(2)]\end{array}$$
$$(9)\quad\textbf{the payoff for the CP-assimilated tensor:}\qquad\textbf{History A and History B are }\neg\textbf{two topologies. They are two REPRESENTATIVES of one boundary-data class, separated only by the Janus register factor }\mathcal J\otimes\mathcal J\ \textbf{inside }\mathcal T_{\mathcal J}^{\,2};$$
$$\text{the ``fuzzball'' reading acquires an exact corpus form with no species name:}\ \textbf{the interior structure the mask hides IS the Janus zig-zag content},\ \text{and the path integral over it is Def-H.32's sum restricted to that class};$$
$$(10)\quad\textbf{status:}\qquad\textbf{derived:}\ (1),(3),(4),(5),(7);\qquad\textbf{scope:}\ (6);\qquad\textbf{corrected:}\ \mathrm{AT.27}(3)\text{'s (M1),(M2)},\ \text{re-graded at (8)};\qquad\textbf{the declarations this clause adds: none.}$$

**Req.** A6, A8, D4.3 (Part 1); CT0.6, CT0.12, CT1.12a(2), CT2.8, CT4.2, CT4.3, CT4.5a(1), FT.20, FT.30 (Part 2); Def-H.32(1),(4), FT.34(3), FT.134(1), FT.159(3) (Part 3); AT.2(4), AT.5, AT.16, AT.17(4), AT.21, AT.23(3), AT.27(3) (this tier); Def-BM.5(1),(3), Def-BM.18(5), BM.2(2), BM.19(1),(2),(3), BM.94, BM.149(2),(3) (Part 4); exact polynomial identities in $\mathbb Q[p]$ by binomial expansion, exact integer binomials, exact rational evaluation [math; machine: `obs_equiv.py` 18/18].

**Pf.**
$$(3):\ (1-p)^{n-k}=\sum_j\binom{n-k}{j}(-1)^jp^j;\ \text{expanding }\sum_{k\le3}\ \text{and }\sum_{k\ge4}\ \text{separately and adding gives }(p+(1-p))^n=1,\ \text{so }1-f_{\mathrm{adm}}=\sum_{k\ge4}\ \text{coefficient-wise}\ [\text{machine: exact comparison of all coefficients at }n=4,5,6,7,8,10,12];$$
$$(4):\ O(8)=2^9-16=496\ [\mathrm{CT0.6}];\ \text{monotonicity from }\partial_p(1-f_{\mathrm{adm}})>0\ \text{on the exact rational values tabulated};$$
$$(5):\ \text{by (1) both interiors contribute }0\ \text{to }\mathcal P_M^{(n)}\mathbf F\mathcal P_M^{(n)}\ \text{for every accessible }n,\ \text{hence }0\ \text{to }(1-\mathbf F_M^{(\Sigma)})^{-1}\ [\mathrm{Def\text{-}H.15}(3);\ \mathrm{Def\text{-}H.16}];\ \text{the retained content is }S_{\mathfrak L}=|R|\ln2\ \text{on both sides}\ [\mathrm{CT1.29};\ \mathrm{CT4.3}];\ \text{the boundary data are equal by hypothesis}\ [\mathrm{Def\text{-}BM.5}(1)]. \blacksquare$$

**Phys.** This is the point AT.27 missed, and it is the strongest structural result in the tier.
The corpus does not merely fail to expose the locked sector — it exposes *nothing* that could
distinguish a locked interior from an internal flurry of crystallization and dissolution moves.
Three independent rows say so: the mask annihilates $D^-$ at every accessible rung, FT.20 marks
$J^\pm$ not observable, and CT1.12a(2) gives the $S$-odd blocks zero metric coordinates. Both
interiors are retained in full and readable not at all.

The arithmetic closes it. The locked density law
$\langle\rho_{D^-}\rangle=\sum_vO(n_v)(1-f_{\mathrm{adm}}(n_v,p))$ contains **no $D^-$ datum**:
$O(n)$ is the capacity excess and $1-f_{\mathrm{adm}}$ is exactly the binomial tail
$P(\mathrm{Binomial}(n,p)\ge4)$ of the *Janus retention probability*. The locked sector's density
is a statement about how often the flicker retains too many edges at a vertex. For the
valence-eight node that is $O(8)=496$ times a tail which falls strictly as $\varepsilon_q$ grows —
the flicker relieves the very oversubscription that feeds the lock.

So the equivalence is a **subnetwork-level gauge redundancy**: one accessible read, many unmasked
representatives, indexed by boundary data. Not an ontological identity — in the unmasked A8 sum
$D^-$ is a stack aspect and $J^\pm$ are pair-arena aspects, and their weights differ. The corpus
already has the machinery to quotient by it: Def-H.32 sums over topologies, Def-BM.5(1) indexes
the ensemble by boundary data alone, and BM.94 rules that "the composite is an ensemble and ¬a
topology."

Two consequences. AT.27's rows (M1) and (M2) **dissolve** — a $D^-$ state space is unnecessary
because the representative's $\mathcal T_{\mathcal J}^{\,2}(c)$ already exists, and an unmasked read
would be gauge-fixing rather than derivation. And row (M3) **sharpens into a testable
invariance**: if the two representatives are observationally identical, $w_i$ must take the same
value on both, and since AT.5's longitudinal determination reads off $(\kappa_e,\Delta x^0)$ —
boundary and ledger data — that invariance may be a theorem rather than an ansatz. Finally,
History A and History B are not two topologies but two representatives of one boundary-data
class, separated only by the Janus register factor, which is AT.23(3)'s conclusion with its
reason supplied: the topology difference is gauge.

---

## §Open-AT additions from Tier AT.4

| row | content | locus |
|---|---|---|
| ~~(AT-O15)~~ | **DISSOLVED by AT.28(8)** — a $D^-$ state space is unnecessary; the representative's $\mathcal T_{\mathcal J}^{\,2}(c)$ exists [AT.23] and the equivalence is a subnetwork-level gauge redundancy | AT.28 |
| ~~(AT-O16)~~ | **DISSOLVED by AT.28(8)** — an unmasked read would be a gauge-fixing act, not a derivation, and CT4.2 forbids it at accessible rungs | AT.28 |
| (AT-O20) | **the sharpened (M3):** prove or refute that $w_i$ is INVARIANT across observationally equivalent representatives. AT.5's longitudinal $w\!\cdot\!\Delta x$ reads off $(\kappa_e,\Delta x^0)$, both boundary/ledger data — so this may be a theorem, which would retire specialization (S) | AT.28(8); AT.5; AT.6 |
| (AT-O21) | **the quotient construction:** make the subnetwork gauge redundancy explicit — a formal quotient of Def-H.32's $(\Gamma,R)$ sum by the boundary-data class, and whether the resulting reduced sum is finite at every budget | AT.28(7); Def-H.32; Def-BM.5(1) |
| (AT-O17) | **a superposition law for the shift across subnetworks (M3)** — $w_i$ is a per-edge metric coordinate; AT.5 determines only the longitudinal projection. ¬∃ a derived additivity law for $w$ | AT.27(3); Def-H.14; AT.5 |
| (AT-O18) | **the connector term in the merged edge count (M4)** — $E_{\mathrm{int}}$ is additive on disjoint edge sets, but a junction carries $d_{12}$: $k(\Gamma)=k_1+k_2+d_{12}$ | AT.27(3); FT.34(3); BM.2(2) |
| (AT-O19) | whether the **detailed-balance point** $\varepsilon_q=\tfrac18$ has independent structural standing: it simultaneously maximizes $\mathcal W_{\text{round}}$, maximizes $\Gamma_{\mathrm{tr}}$, and equalizes $|\mathcal M_{\mathrm{ann}}|$ and $|\mathcal M_{\mathrm{pair}}$ | AT.22(3),(4),(5); BM.44(7); BM.120(5); BM.142(6) |
