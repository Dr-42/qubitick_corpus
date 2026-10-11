# $\langle qu(b(i(t|t))ick)\rangle$ — **Part 5 · Atomic era** — Tier AT.3

**Level.** 5. **Era.** 2 (the Atomic era). **Tier.** AT.3 — the seed-tensoring / channel-capacity
collision: the $D^-$ censor.
**Tags.** AT.16–AT.20. **Status.** discovery-phase working tier. **No declaration issues;
§Cal-AT stays empty; no clause of Parts 1–4 is modified or retracted.**
**Machine.** `canon/era2/censor.py` → **19/19 exact**, exit 0. Arithmetic: integers, `Fraction`,
exact Laurent polynomials over $\mathbb Q[z,z^{-1}]$, exhaustive permutation enumeration by cycle
type, rigorous `Fraction` enclosures for $\ln2$. **No floating point; no smooth-limit analogy.**
**Charter.** Part 5 cites Parts 1–4 and earlier AT-tags only.

> **Directive compliance note.** This tier executes the Architect's directive, and **corrects two
> of its steps** on exact grounds, as the standing instruction requires (*"don't directly trust
> the imaginator"*). The censor, every integer bound, the dust equation of state and the
> one-way membrane are all confirmed verbatim. What is **refuted** is the *mechanism*: the
> excess at $n\ge4$ does not "collapse into the $j=0$ scalar singlet" — BM.138(2) gives
> $j=|k|/2$, and CT4.2/CT4.3 give **masking**, not projection. See AT.17.

---

## Tier AT.3 — the capacity censor and the locked sector

**Locus.** BM.138 constructs the seed-tensoring mechanism: the carrier is
$\Psi(c)=\mathrm{Sym}^{|k(c)|}(\mathcal H_{\mathsf v})=\Pi_{|k|}(\mathcal H_{\mathsf v}^{\otimes|k|})$,
with $\Pi_k$ the $S_k$ twirl. The ladder in $k$ is unbounded. CT0.5/CT0.6/CT0.11 bound the
*valence* at $n(v)\le3$. This tier assembles the collision: what the unbounded mechanism would
build, and what the capacity forbids the ledger to expose — and it locates the excess in
$D^-$, whose equation of state and density law are already derived.

---

### AT.16 — The capacity censor: $n\ge4$ is inadmissible, and the excess is exact

**Thm.**
$$(1)\quad\textbf{the tick load:}\qquad D_{\mathrm{tick}}(n)=2^{\,n+1}\qquad[\mathrm{CT0.5}];$$
$$(2)\quad\textbf{the channel capacity:}\qquad C_{\mathrm{cap}}=\dim_{\mathbb R}\mathfrak H(\mathbb C^4)=16,\qquad O(n)=\max\bigl(0,\ 2^{\,n+1}-16\bigr)\qquad[\mathrm{CT0.6}];$$
$$(3)\quad\textbf{the exact threshold table:}\qquad\begin{array}{c|cccccccccc} n&0&1&2&3&4&5&6&7&8&10\\ \hline D_{\mathrm{tick}}(n)&2&4&8&\mathbf{16}&32&64&128&256&512&2048\\ O(n)&0&0&0&\mathbf0&16&48&112&240&496&2032\end{array}$$
$$O(0)=O(1)=O(2)=O(3)=0;\qquad O(4)=16=C_{\mathrm{cap}}\ \ \textbf{exactly};\qquad O(n)=2^{n+1}-16\ (n\ge4);$$
$$(4)\quad\textbf{the admissibility equivalence:}\qquad \boxed{\ \text{channel-admissible}(v)\iff D_{\mathrm{tick}}(n(v))\le C_{\mathrm{cap}}\iff n(v)\le3\ }\qquad[\mathrm{CT0.11};\ \text{machine: every }n\in[0,39]];$$
$$D_{\mathrm{tick}}(3)=16=C_{\mathrm{cap}}\ \ \textbf{is saturation, not slack};\qquad \forall v:\ n(v)\ge4\implies O(n(v))>0;$$
$$(5)\quad\textbf{the derived colour count:}\qquad \max\{\mathcal H^{(n)}_{\mathrm{slot}}:\ \text{admissible}\}=\mathcal H^{(3)}_{\mathrm{slot}}\cong\mathbb C^3,\qquad 3=\lfloor\log_2 C_{\mathrm{cap}}\rfloor-1=\lfloor\log_216\rfloor-1;$$
$$\boxed{\ N_{\text{colour}}=3\ \ \textbf{is derived, not chosen}\ }\qquad[\mathrm{Cor\ CT0.11a}];$$
$$(6)\quad\textbf{where the excess goes:}\qquad \text{ledger-side excess }O(n)>0\ \text{at}\ n\ge4\ \textbf{falls to }D^-\qquad[\mathrm{CT4.1};\ \mathrm{D4.1};\ \mathrm{BM.149}(1)];$$
$$\text{absorption rate}\ \propto O(n)\qquad[\mathrm{D4.2}];\qquad O(4)=16=C_{\mathrm{cap}}:\ \textbf{exactly one further channel quantum per tick}\qquad[\mathrm{CT4.1}];$$
$$(7)\quad\textbf{status: derived.}\qquad\neg\text{a smooth limit, }\neg\text{a manifold analogy: every row is an exact integer.}$$

**Req.** A2, A7, D0.8, D4.1, D4.2, D1.11 (Part 1); CT0.5, CT0.6, CT0.11, Cor CT0.11a, CT0.14, CT4.1, CT4.5 (Part 2); BM.131(6), BM.138(1), BM.149(1),(2) (Part 4); exact integer arithmetic, exhaustive enumeration over $n\in[0,39]$ [math; machine: `censor.py` §A].

**Pf.** $(1)$–$(3)$: CT0.5's load and CT0.6's capacity, evaluated as exact integers; $2^4=16=C_{\mathrm{cap}}$ gives $O(3)=0$ and $O(4)=2^5-16=16$. $(4)$: $2^{n+1}\le16\iff n+1\le4\iff n\le3$, monotone in $n$, verified exhaustively. $(5)$: $\lfloor\log_216\rfloor=4$ since $2^4=16\le16<32=2^5$. $(6)$: CT4.1/D4.1 re-cited. $\blacksquare$

**Phys.** The ledger's per-vertex channel is one qubit [A2], the tick load at rung $n$ doubles
with each step, and the pair arena has exactly sixteen real operator directions. Those two facts
collide at $n=3$: rung three *saturates* the capacity and rung four exceeds it by exactly one
capacity. Nothing continuous is invoked — this is integer bookkeeping, and it is why the corpus
has three colours rather than a chosen three.

---

### AT.17 — The mechanism is MASKING, not collapse: the directive's $j=0$ claim, refuted

**Thm.**
$$(1)\quad\textbf{what seed tensoring actually produces:}\qquad \Pi_k=\frac1{k!}\sum_{\sigma\in S_k}\hat P_\sigma,\qquad \Pi_k^2=\Pi_k,\qquad \operatorname{rk}\Pi_k=k+1=\dim\mathrm{Sym}^k(\mathbb C^2)\qquad[\mathrm{BM.138}(1)];$$
$$\textbf{the exact character:}\qquad \operatorname{Tr}\bigl(\Pi_k D(z)^{\otimes k}\bigr)=\sum_{m\in\{k,\,k-2,\,\dots,\,-k\}}z^{m},\qquad D(z)=\operatorname{diag}(z,z^{-1})\qquad[\mathrm{BM.138}(2);\ \mathrm{FT.60}(4)];$$
$$\textbf{the Casimir and the spin:}\qquad \tfrac k2\bigl(\tfrac k2+1\bigr),\qquad \boxed{\ j=\tfrac{|k|}2\ }\qquad[\mathrm{BM.138}(2);\ \mathrm{Def\text{-}H.38};\ \mathrm{FT.55}(2)];$$
$$(2)\quad\textbf{the refutation:}\qquad \mathrm{Sym}^k(\mathbb C^2)\ \textbf{is the spin-}k/2\ \textbf{irrep, of dimension }k+1,\ \textbf{and is }\neg\textbf{ a scalar singlet for any }k\ge1;$$
$$k=4:\quad j=2,\quad \dim=5,\quad \text{weights}\ \{4,2,0,-2,-4\}\ \text{each with multiplicity }1;$$
$$\boxed{\ \textbf{the seed-tensoring mechanism NEVER yields }j=0\ \textbf{for }k\ge1\ }$$
$$(3)\quad\textbf{the antisymmetric route to a singlet is closed as well:}\qquad \dim\wedge^k(\mathbb C^2)=\binom2k=0\quad\forall k\ge3\qquad[\mathrm{BM.136}(3)];$$
$$\text{so at valence }\ge3\ \text{there is }\neg\text{an }\varepsilon\text{-type singlet available either};\qquad \dim\operatorname{Inv}\bigl((\mathbb C^3)^{\otimes4}\bigr)=0:\ \textbf{four colour slots admit no singlet}\qquad[\mathrm{BM.136}(3)];$$
$$(4)\quad\textbf{what really happens at }n\ge4\textbf{ — masking, with three exact rows:}$$
$$\forall n\le3:\quad \mathcal P_M^{(n)}F_{D^-}\mathcal P_M^{(n)}=0;\qquad \neg\exists\ \text{a pole of }Z(\mathcal R,n)\ \text{carrying locked content}\qquad[\mathrm{CT4.2};\ \mathrm{BM.149}(3)];$$
$$\text{locked content:}\quad\textbf{physical norm }0\ \text{at accessible rungs},\qquad w(C)\ne0\ \text{in the unmasked A8 sum},\qquad \boxed{\ \neg\exists\ \text{a deleted entry}\ }\qquad[\mathrm{CT4.3};\ \mathrm{CT2.8}];$$
$$S_{\mathfrak L}=n_{\mathcal R}\ln2\ \ \textbf{is retained in full on absorption}\qquad[\mathrm{CT4.3};\ \mathrm{CT1.29}];$$
$$(5)\quad\textbf{the two survivors, and neither is a }j=0\textbf{ state:}$$
$$\textbf{accessible:}\ \text{the }n\le3\ \text{sub-ladder, maximal slot }\mathcal H^{(3)}_{\mathrm{slot}}\cong\mathbb C^3\qquad[\mathrm{Cor\ CT0.11a}];$$
$$\textbf{retained:}\ \text{the edge count }E_{\mathrm{int}}=|R|\in\mathbb Z,\quad S_{\mathfrak L}=E_{\mathrm{int}}\ln2\qquad[\mathrm{Def\text{-}BM.5}(4);\ \mathrm{CT1.29}];$$
$$\boxed{\ E_{\mathrm{int}}\ \textbf{is an integer count, spin-blind: it is }\neg\textbf{a representation, so }\neg\textbf{a }j=0\ \textbf{singlet}\ }$$
$$(6)\quad\textbf{the distinction that matters:}\qquad\textbf{a projection onto }j=0\ \text{would have a 1-dimensional image};\qquad\textbf{the mask has a ZERO image:}\ \ \mathcal P_M^{(n)}F_{D^-}\mathcal P_M^{(n)}=0;$$
$$\text{annihilation}\ \neg\text{= folding. The excess is not collapsed, it is made inaccessible while being retained.}$$
$$(7)\quad\textbf{status:}\qquad\textbf{derived:}\ (1),(3),(4),(5),(6);\qquad\textbf{refuted:}\ \text{the }j=0\text{-collapse clause of the directive.}$$

**Req.** A2, A3, CT0.11, Cor CT0.11a (Part 1); CT1.29, CT2.8, CT4.1, CT4.2, CT4.3, D1.11, D4.2 (Part 2); Def-H.38, FT.55(2), FT.60(3),(4) (Part 3); BM.128(2),(3), BM.131(6), BM.136(3), BM.138(1),(2), BM.149(3), Def-BM.5(4) (Part 4); exact Laurent-polynomial character computation by cycle-type enumeration over all $k!$ permutations for $k\le8$, exact binomial ranks [math; machine: `censor.py` §§B–C].

**Pf.**
$$(1):\ \operatorname{Tr}(\hat P_\sigma D(z)^{\otimes k})=\prod_{\text{cycles }L\text{ of }\sigma}(z^{L}+z^{-L})\ \text{exactly};\ \text{averaging over }S_k\ \text{and collecting gives }\sum_{m\in\{k,k-2,\dots,-k\}}z^m\ \text{with every multiplicity }1\ [\text{machine: }k=1..8,\ \text{all }k!\ \text{permutations, rational Laurent coefficients}];$$
$$(2):\ \text{a weight ladder }\{k,k-2,\dots,-k\}\ \text{of length }k+1\ \text{with all multiplicities }1\ \textbf{is}\ \text{the spin-}k/2\ \text{irrep};\ \text{its Casimir is }\tfrac k2(\tfrac k2+1);\ j=0\ \text{would require the single weight }m=0,\ \text{i.e. }k=0;$$
$$(3):\ \binom2k=0\ \text{for }k\ge3\ [\text{machine}];\ \dim\operatorname{Inv}((\mathbb C^3)^{\otimes4})=0\ [\mathrm{BM.136}(3)];$$
$$(6):\ \text{a projection onto a 1-dimensional singlet has rank }1;\ \mathcal P_M^{(n)}F_{D^-}\mathcal P_M^{(n)}=0\ \text{has rank }0. \blacksquare$$

**Phys.** The directive's intuition — that capacity censors the cascade — is exactly right, and
every integer in it checks. The mechanism it proposed is not. Seed tensoring builds spin $k/2$,
and the symmetrizer never produces a scalar; at $k=4$ it produces spin 2. Nor does the excess get
*projected* anywhere: the mask has zero image, not a one-dimensional one, so there is no
singlet to land in. What happens is subtler and, for the corpus's purposes, better: the
higher-spin content is **retained in full and made inaccessible**. $w(C)\ne0$ in the unmasked
A8 sum, no entry is deleted, $S_{\mathfrak L}=n_{\mathcal R}\ln2$ is kept — and yet the physical
norm at every accessible rung is zero and no pole of the resolvent carries it. That is a censor
in the exact sense: it hides, it does not destroy. The accessible residue is the $n\le3$
sub-ladder (hence three colours, derived), and the retained residue is an integer edge count
that is spin-blind and so was never a representation to begin with.

---

### AT.18 — The locked sector's density law and its equation of state

**Thm.**
$$(1)\quad\textbf{the density:}\qquad \boxed{\ \bigl\langle\rho_{D^-}\bigr\rangle_\Gamma(p)=\sum_v O(n_v)\,\bigl(1-f_{\mathrm{adm}}(n_v,p)\bigr),\qquad f_{\mathrm{adm}}(n,p)=\sum_{k\le3}\binom nk p^k(1-p)^{n-k}\ }\qquad[\mathrm{CT4.5a}(1);\ \mathrm{BM.149}(2)];$$
$$f_{\mathrm{adm}}\ \textbf{is an exact polynomial in }p\ \textbf{with integer coefficients};\qquad f_{\mathrm{adm}}(n,1)=1\ (n\le3),\quad 0\ (n\ge4);$$
$$(2)\quad\textbf{the five anchors, reproduced exactly:}\qquad \bigl\langle\rho_{D^-}\bigr\rangle_\Gamma(1)=\bigl(448,\ 896,\ 2976,\ 2240,\ 24384\bigr)\qquad[\mathrm{CT4.5a}(2)];$$
$$\begin{array}{c|ccccc}
\text{solid} & \text{tetra} & \text{cube} & \text{octa} & \text{dodeca} & \text{icosa}\\ \hline
V & 4 & 8 & 6 & 20 & 12\\
d & 3 & 3 & 4 & 3 & 5\\
n_v=2d & 6 & 6 & 8 & 6 & 10\\
O(n_v) & 112 & 112 & 496 & 112 & 2032\\
\langle\rho_{D^-}\rangle & \mathbf{448} & \mathbf{896} & \mathbf{2976} & \mathbf{2240} & \mathbf{24384}\end{array}$$
$$\text{i.e.}\quad 4\,O(6),\quad 8\,O(6),\quad 6\,O(8),\quad 20\,O(6),\quad 12\,O(10);$$
$$(3)\quad\textbf{the equation of state:}\qquad \boxed{\ T^{(D^-)}_{\mu\nu}=\rho_{D^-}u_\mu u_\nu,\qquad w_{D^-}=0,\qquad \rho_{D^-}\ge0,\qquad \rho_{D^-}=0\iff\neg\exists v:\ n(v)\ge4\ }\qquad[\mathrm{CT4.5};\ \mathrm{BM.149}(6)];$$
$$(4)\quad\textbf{the contrast row:}\qquad F_{D^+}=\Lambda\,\mathbb I,\quad w_{D^+}=-1\qquad[\mathrm{A8};\ \mathrm{D4.3};\ \mathrm{CT1.25}];\qquad\text{so the two dark aspects sit at the two ends of the equation-of-state range, }w=0\ \text{and}\ w=-1;$$
$$(5)\quad\textbf{the species bar:}\qquad\text{reading }D^-\ \text{as ``dark matter'' and }D^+\ \text{as ``dark energy'' is a SPECIES IDENTIFICATION and is}\ \neg\text{formed}\ [\mathrm{P5};\ \mathrm{Def\text{-}BM.3}(7)];$$
$$\textbf{recorded, }\neg\textbf{adopted:}\ \text{the equations of state are derived; the names are not issued};$$
$$(6)\quad\textbf{the maximal locked entropy:}\qquad D^-:\ \bigl(S_{\mathrm{raw}},S_{\mathfrak L}\bigr)=\bigl(\min_{\mathrm{acc}},\ \max\wedge\neg\text{accessible}\bigr)\qquad[\mathrm{CT4.7};\ \mathrm{BM.149}(4)];$$
$$(7)\quad\textbf{status: derived, with (5)'s bar.}$$

**Req.** A8, D4.2, D4.3 (Part 1); CT1.25, CT1.29, CT4.1, CT4.3, CT4.5, CT4.5a(1),(2), CT4.7 (Part 2); AT.16(2),(3),(6) (this tier); BM.149(2),(4),(6) (Part 4); exact binomial arithmetic, exact polynomial evaluation in $\mathbb Q[p]$, integer censuses [math; machine: `censor.py` §D].

**Pf.**
$$(1):\ \text{CT4.5a}(1)\ \text{re-cited};\ f_{\mathrm{adm}}(n,1)=\sum_{k\le3}\binom nk\,0^{n-k}=\binom nn=1\ \text{for }n\le3\ \text{and }0\ \text{for }n\ge4\ [\text{machine: the }0^0\ \text{and negative-power cases handled by restricting the sum to }k\le\min(3,n)];$$
$$(2):\ O(6)=2^7-16=112,\ O(8)=2^9-16=496,\ O(10)=2^{11}-16=2032;\ \text{multiplying by }V=(4,8,6,20,12)\ \text{gives the five anchors exactly}\ [\text{machine}];$$
$$(3),(4):\ \text{CT4.5 and CT1.25 re-cited}. \blacksquare$$

**Phys.** The locked sector's density is a closed exact expression: sum over vertices the
oversubscription $O(n_v)$, weighted by the probability that the vertex fails to present an
admissible ($\le3$) sub-configuration. On the five Platonic skeletons at full crystallization
this gives five exact integers, and the largest — the icosahedron's 24384 — comes entirely from
its valence-ten vertices, since $O(10)=2032$ against $O(6)=112$. Its equation of state is that of
pressureless dust, and it vanishes identically unless some vertex has valence at least four, so
the sector is *sourced* by oversubscription and by nothing else. The corpus also carries the
opposite end of the range, $D^+$ at $w=-1$. Naming these two "dark matter" and "dark energy"
would be a species identification, which P5 bars; the equations of state are derived, the names
are not issued.

---

### AT.19 — The two faces of one capacity, and why the formed censor is Schwarzschild-like

**Thm.**
$$(1)\quad\textbf{the two faces:}\qquad\begin{array}{l|l|l}
\text{the face} & \text{the capacity} & \text{the locus}\\ \hline
\text{chart-side} & E_{\mathrm{int}}\le 2r/\mathfrak h:\ \text{the metric resolution of a cell} & [\mathrm{BM.148}(1)]\\
\text{ledger-side} & k_v\le3\ \text{per accessible vertex}:\ \text{the channel capacity} & [\mathrm{CT0.11};\ \mathrm{AT.16}(4)]\end{array}$$
$$\textbf{two independent bounds with one structural role};\qquad\text{chart-side excess: the read is}\neg\text{formed}\ [\mathrm{BM.132}(3)];\qquad\text{ledger-side excess: }O(n)>0\ \text{falls to }D^-;$$
$$(2)\quad\textbf{the chart-side threshold in three exactly equivalent forms:}\qquad \boxed{\ E_{\mathrm{crit}}(r)=\frac{2r}{\mathfrak h}\ }\qquad \boxed{\ S_{\mathrm{crit}}(r)=\frac{2r\ln2}{\mathfrak h}\ }\qquad \boxed{\ k_{\mathrm{crit}}(E)=\frac{E_{\mathrm{int}}^2\ln2}2=\frac{G(E)}{4\pi}\ }$$
$$\textbf{the flux form:}\quad\text{the map breaks}\iff S_{\mathfrak L}(\text{cell})>S_{\mathrm{crit}}(r)\qquad[S_{\mathfrak L}=E_{\mathrm{int}}\ln2;\ \mathrm{CT1.29}];$$
$$(3)\quad\textbf{the horizon form:}\qquad r_s=\tfrac12\mathfrak h E_{\mathrm{int}}\ [\mathrm{AT.1}(3);\ \mathrm{BM.146}(3)\ \text{diagonal}\ +\ \mathrm{ADM}]\ \text{gives}$$
$$\boxed{\ r\ge r_s(E)\iff E_{\mathrm{int}}\le\frac{2r}{\mathfrak h}\iff\text{the chart read is formed}\ }\qquad\text{and BM.149(3)'s one-way membrane is its ledger-side image};$$
$$(4)\quad\textbf{the one-hop capacity:}\qquad E_{\mathrm{crit}}(\mathfrak h)=2:\qquad\boxed{\ \text{a chart cell of one hop carries exactly the digon floor and nothing heavier}\ }\qquad[\mathrm{BM.148}(3);\ \text{Census FT.28}];$$
$$r_s=\bigl(1,\ 3,\ 6,\ 12,\ 30\bigr)\mathfrak h\quad\text{at}\quad E_{\mathrm{int}}\in\{2,6,12,24,60\}\qquad[\mathrm{BM.43}(1)];$$
$$(5)\quad\textbf{no cell is chart-formed at its own envelope:}\qquad r=\Delta x_{\mathrm B}(E)=\frac{\mathfrak h}{E\ln2}\implies E\le E_{\mathrm{crit}}\bigl(\Delta x_{\mathrm B}(E)\bigr)=\frac2{E\ln2}\iff E^2\ln2\le2;$$
$$E_{\mathrm{int}}\ge2\implies E^2\ln2\ge4\ln2=\ln16>2\qquad\Bigl[\ln16>2\iff16>e^2:\quad e^2<\Bigl(\tfrac{876809}{322560}\Bigr)^2<8<16;\ \text{machine}\Bigr];$$
$$\boxed{\ \textbf{no materialized cell is chart-formed at its own envelope}\ }$$
$$(6)\quad\textbf{the formed censor is SCHWARZSCHILD-like, }\neg\textbf{Kerr:}\qquad \mathrm{BM.146}(3)\text{'s cell metric }g_{\mu\nu}=\eta_{\mu\nu}+\tfrac{\mathfrak hE_{\mathrm{int}}}{2r}\mathbb 1_4\ \textbf{is diagonal};$$
$$\text{ADM then forces }N_iN^i=0\implies w_i=0\ \text{on that cell}\ [\mathrm{AT.1};\ \mathrm{BM.34}(4):\ w=0\ \textbf{is a gauge}];$$
$$\textbf{a Kerr-type censor requires a formed nonzero shift, i.e. rotation, i.e. the T-odd block }w_i;$$
$$\mathrm{AT.5}\ \text{determines the LONGITUDINAL }w\!\cdot\!\Delta x\ \text{in closed form and leaves }2E\ \text{transverse dimensions as diffeomorphism gauge};\qquad \mathrm{AT.15}\ \text{shows the bit is T-EVEN, conjugate to the VOLUME mode};$$
$$\boxed{\ \neg\exists\ \text{a carrier-side invariant that fixes the shift's direction}\implies\textbf{the formed censor is spherically symmetric at every computed cell}\ }$$
$$(7)\quad\textbf{status: derived.}\qquad\textbf{The Kerr route is open and is row (AT-O1)/(AT-O2), downstream of the shift and }\neg\textbf{of the capacity bound.}$$

**Req.** D2.9, P1 (Part 1); CT0.11, CT1.29, CT2.6 (Part 2); AT.1(3), AT.5(3),(4), AT.15(4),(5), AT.16(4) (this tier); BM.34(1),(4), BM.43(1), BM.132(3), BM.146(3), BM.147(2), BM.148(1),(3),(4), BM.149(1),(3), Census FT.28, Def-BM.4(1) (Part 4); exact rational threshold algebra, rigorous `Fraction` enclosure of $\ln2$, the exact integer certificate $e^2<(876809/322560)^2<8<16$ [math; machine: `censor.py` §E].

**Pf.**
$$(3):\ r\ge\tfrac12\mathfrak h E\iff 2r/\mathfrak h\ge E\ [\text{cross-multiplication, }\mathfrak h>0];$$
$$(5):\ 4\ln2=\ln16$ and $\ln16>2\iff16>e^2$; the enclosure $e^2<(876809/322560)^2$ with $(876809/322560)^2<8<16$ gives the strict inequality with an exact integer certificate; $4\ln2=2.772588722\ldots>2$ [machine];
$$(6):\ \text{AT.1's PART B: }g_{00}=-N^2\ \text{on BM.146(3)'s cell}\implies N_iN^i=0\implies\varkappa\beta w_i=0,\ \text{and }\Omega^2>0\ \text{unconditionally}\ [\mathrm{CT1.12}]. \blacksquare$$

**Phys.** The corpus has *two* capacity bounds with the same structural job and no shared
machinery: the chart cannot resolve a cell whose content exceeds $2r/\mathfrak h$, and the ledger
cannot expose a vertex whose valence exceeds three. The first is a horizon condition in disguise —
with $r_s=\mathfrak hE_{\mathrm{int}}/2$ it reads exactly $r\ge r_s$ — and BM.149(3)'s one-way
membrane is its ledger-side image. The second is pure integer bookkeeping. That two such
different-looking bounds play one role is the content of BM.149(1)'s "two faces of one capacity."

Two further rows are worth their weight. A single hop carries *exactly* the digon floor and
nothing heavier, which is the smallest possible cell and the smallest possible content, matched.
And no materialized cell is chart-formed at its own envelope, because $E^2\ln2\ge\ln16>2$ — so
self-resolution is impossible for every admissible content, which is a discrete statement of the
same flavour as a censorship theorem and needs no smooth limit to state.

Finally, the shape of the censor: BM.146(3)'s formed metric is diagonal, so the shift vanishes
and the geometry is spherically symmetric. **The formed censor is Schwarzschild-like, not Kerr.**
A rotating censor needs a formed nonzero shift, and Tiers AT.1 and AT.2 established that the
shift's longitudinal part is ledger-determined while its transverse part is diffeomorphism gauge
and its direction is fixed by nothing in the carrier — the bit being T-even and conjugate to the
volume mode. So the Kerr generalization is not blocked by the capacity bound at all; it sits
downstream of rows (AT-O1) and (AT-O2), and reaching it would give the corpus rotation.

---

### AT.20 — Tier AT.3 status and adjudication

**Thm.**
$$(1)\quad\textbf{derived:}\qquad\text{the tick load }2^{n+1};\ \text{the capacity }16;\ O(n);\ \text{the admissibility equivalence }n\le3;\ N_{\text{colour}}=3;\ \text{the routing of the excess to }D^-;$$
$$\text{the spin content }j=|k|/2\ \text{and the exact character of }\Pi_k;\ \dim\wedge^k(\mathbb C^2)=0\ (k\ge3);\ \text{the three masking rows};\ \text{the density law and its five anchors};\ w_{D^-}=0;\ \text{the two faces of one capacity};\ \text{the horizon form};\ \text{the one-hop capacity};\ \text{the envelope impossibility};\ \text{the spherical symmetry of the formed censor};$$
$$(2)\quad\textbf{refuted:}\qquad\text{the directive's clause that the }n\ge4\ \text{excess ``collapses exclusively into the }j=0\ \text{scalar singlet''}\ —\ \text{on two independent exact grounds}:$$
$$(\mathrm i)\ \ \mathrm{Sym}^k(\mathbb C^2)\ \text{is spin }k/2,\ \neg\ \text{a singlet}\ [\mathrm{BM.138}(2);\ \text{the character computed to }k=8];$$
$$(\mathrm{ii})\ \ \mathcal P_M^{(n)}F_{D^-}\mathcal P_M^{(n)}=0\ \text{has rank }0,\ \text{whereas a projection onto a singlet has rank }1\ [\mathrm{CT4.2}];\ \text{annihilation}\ \neg\text{= folding};$$
$$(3)\quad\textbf{corrected in the Phys register:}\qquad\text{``dark matter is dark because the channel capacity forbids it from carrying higher-spin interactions'' overstates the selectivity. The mask annihilates the }\textbf{whole}\ D^-\ \textbf{block at every accessible rung, not its higher-spin part:}\ \neg\exists\ \text{a pole of }Z(\mathcal R,n)\ \text{carrying locked content, and the physical norm is }0\ \text{at accessible rungs}\ [\mathrm{CT4.2};\ \mathrm{CT4.3};\ \mathrm{CT2.8}];$$
$$\text{the correct statement is:}\ \textbf{the locked sector is dark because it has no accessible coupling at all, at any spin};$$
$$(4)\quad\textbf{the cascade is unbounded, }\neg\textbf{infinite:}\qquad\mathrm{Sym}^k\ \text{has rank }k+1<\infty\ \text{for every }k;\ \text{what is unbounded is the ladder in }k,\ \text{and CT0.11 truncates the VALUENCE at }3;\ \text{``an infinite ranked matrix'' should read ``an unbounded ladder of finite ranks''};$$
$$(5)\quad\textbf{barred:}\qquad\text{the species identifications }D^-\to\text{``dark matter''}\ \text{and }D^+\to\text{``dark energy''}\ [\mathrm{P5};\ \mathrm{Def\text{-}BM.3}(7)]:\ \text{the equations of state }w=0\ \text{and}\ w=-1\ \text{are derived, the names are}\neg\text{issued};$$
$$(6)\quad\textbf{the declarations this tier adds: none.}\qquad\neg\text{a P4 addition (§Cal-AT empty)},\ \neg\text{a new dimensionful scale},\ \neg\text{a measured value or an [EXT] datum},\ \neg\text{a species identification},\ \neg\text{an isolated aspect applied},\ \neg\text{a smooth limit used};$$
$$(7)\quad\textbf{open rows added:}\qquad(\mathrm{AT\text{-}O12})\ \text{whether the chart-side face }E_{\mathrm{int}}\le2r/\mathfrak h\ \text{and the ledger-side face }n\le3\ \text{can be shown to be one bound in two charts, or are provably independent};$$
$$(\mathrm{AT\text{-}O13})\ \text{the Kerr route: a formed nonzero shift would make the censor rotating; it needs (AT-O1)'s }\omega_i\ \text{homogeneity and (AT-O2)'s slicing choice, and is }\neg\text{blocked by the capacity bound};$$
$$(\mathrm{AT\text{-}O14})\ \text{whether AT.15's invariant ladder at higher carrier level (BM.131(6)'s }\operatorname{rk}\Pi_k=k+1)\ \text{eventually reaches the }D^-\ \text{sector, i.e. whether locked content has ANY invariant read at some }k;$$
$$(8)\quad\textbf{machine:}\qquad\texttt{canon/era2/censor.py}\to19/19\ \text{exact};\ \texttt{run\_all\_era2.py}\to\text{all green}. $$

**Req.** AT.16–AT.19 (this tier); P5 (Parts 1–2); A2, A8, D4.1, D4.2, D4.3, CT0.5, CT0.6, CT0.11, CT0.14, CT1.25, CT1.29, CT2.8, CT4.1, CT4.2, CT4.3, CT4.5, CT4.5a, CT4.7, Cor CT0.11a (Parts 1–2); Def-H.38, FT.55(2), FT.60(3),(4) (Part 3); BM.128, BM.131(6), BM.136(3), BM.138, BM.143(7), BM.146(3), BM.148, BM.149, Def-BM.3(7), Def-BM.5(4), Census FT.28 (Part 4) [math; machine: `censor.py`].

**Pf.** Row-wise assembly of AT.16–AT.19, each row re-citing its own machine section. $\blacksquare$

**Phys.** The collision the directive asked for is real and it is exact: an unbounded
seed-tensoring ladder against a hard sixteen-dimensional channel capacity, meeting at valence
four. The ledger's answer is not to simplify the state but to hide it — retained in full,
inaccessible at every accessible rung, with no pole and no deleted entry, gravitating as
pressureless dust and sourced only by oversubscription. Three things the directive proposed did
not survive contact with the canon: the collapse is not to $j=0$ because seed tensoring makes
spin $k/2$; it is not a collapse at all because the mask's image is zero rather than
one-dimensional; and the sector is dark because it has no accessible coupling at any spin, not
because higher spins in particular are forbidden. What replaces them is sharper: a censor that
conceals rather than destroys, a derived colour count of three, and a spherical — not rotating —
horizon, with the rotating version waiting on the shift rather than on the capacity.

---

## §Open-AT additions from Tier AT.3

| row | content | locus |
|---|---|---|
| (AT-O12) | are the two faces of one capacity **one bound in two charts**, or provably independent? | AT.19(1); BM.149(1); BM.148(1); CT0.11 |
| (AT-O13) | **the Kerr route** — a formed nonzero shift makes the censor rotating; needs (AT-O1)'s `ω_i` homogeneity and (AT-O2)'s slicing choice; ¬blocked by the capacity bound | AT.19(6); AT.1; AT.5 |
| (AT-O14) | does AT.15's invariant ladder reach the `D⁻` sector at some `k`, i.e. does locked content have **any** invariant read? | AT.15; BM.131(6); BM.138 |
