# $\langle qu(b(i(t|t))ick)\rangle$ — **Part 5 · Atomic era** — Tier A.2

**Level.** 5. **Era.** 2 (the Atomic era). **Tier.** A.2 — the tensor form of the bit/qubit
distinction, framed through BM.131's Haar–Poisson duality.
**Tags.** A.9–A.14. **Status.** discovery-phase working tier; every clause labelled *derived*,
*marked*, or *scope*. **No declaration issues; §Cal-A stays empty; no clause of Parts 1–4 is
modified or retracted.**
**Machine.** `canon/era2/bit_qubit.py` → **22/22 exact**, exit 0. Arithmetic: 4×4 matrices over
complex-`Fraction`, exact Gaussian elimination over $\mathbb Q(i)$, exhaustive finite-group
enumeration. **No floating point; no numerical integration.**
**Charter (era chain).** Part 5 cites Parts 1–4 and earlier A-tags only.
**No global tick is introduced anywhere in this tier.** BM.131's duality is the frame.

---

## Tier A.2 — the bit/qubit distinction as twirl → block-trace

**Locus.** A.1's census read the corpus as a whole. This tier builds one object the frozen canon
names but does not assemble: the **bit/qubit distinction in tensor form**. BM.131 supplies both
halves — the Haar side as an exact gauge projection, the Poisson side as the recorded dynamics —
and A4 supplies the threshold that makes the surviving invariant binary. What is new here is the
assembly, the rank count, and the uniqueness theorem (A.12): *the bit is not merely "the trace
of the $\Pi_{\mathcal R}$ block"; it is the **unique** Haar-gauge-invariant parameter of the
carrier*, which is why it and nothing else is what a record can hold.

**Method note (why no integration appears).** The Haar integral cannot be evaluated in
`Fraction`, but it does not need to be. The **binary tetrahedral group** $2T$ (24 elements,
entries in $\mathbb Z[i]/2$) maps onto $A_4$, whose 3-dimensional representation is irreducible,
while $\wedge^2$ is the trivial 1-dimensional representation. Two inequivalent irreps ⟹ by Schur
the average over $2T$ **equals** the average over $\mathrm{SU}(2)$ on this decomposition. The
twirl theorem is therefore verified exactly, by 24 matrix multiplications.

---

### A.9 — The carrier, the flip, and the two blocks

**Thm.**
$$(1)\quad\mathcal H_p\otimes\mathcal H_q\cong\mathbb C^4,\qquad F:=\text{the flip},\qquad F^2=I,\quad F^\dagger=F,\quad F(U\otimes U)=(U\otimes U)F\ \ \forall U\in\mathrm{SU}(2);$$
$$(2)\quad \Pi_{\mathcal R}:=\tfrac12(I+F),\qquad \Pi_{\mathcal V}:=\tfrac12(I-F);\qquad \Pi^2=\Pi,\quad \Pi_{\mathcal R}\Pi_{\mathcal V}=0,\quad \Pi_{\mathcal R}+\Pi_{\mathcal V}=I;$$
$$(3)\quad \operatorname{rk}\Pi_{\mathcal R}=3=\dim\vee^2,\qquad \operatorname{rk}\Pi_{\mathcal V}=1=\dim\wedge^2,\qquad \mathfrak T\Pi_{\mathcal R}=3,\quad \mathfrak T\Pi_{\mathcal V}=1;$$
$$(4)\quad\textbf{the two normalizations are what BM.131(4) writes explicitly, and they differ:}$$
$$\text{the }\mathcal R\text{-block is divided by }\mathfrak T\Pi_{\mathcal R}=3;\qquad\text{the }\mathcal V\text{-block is divided by }\mathfrak T\Pi_{\mathcal V}=1,\ \text{i.e. not at all};$$
$$(5)\quad\textbf{status: derived.}$$

**Req.** A1, A3, A5 (Part 1); C13, CT0.7(1), CT1.1 (Part 1); FT.101(3), FT.107(2) (Part 3); BM.131(4), Def-BM.18(1) (Part 4); exact $4\times4$ matrix arithmetic over complex-`Fraction`, exact rank by Gaussian elimination over $\mathbb Q(i)$ [math; machine: `bit_qubit.py` §A].

**Pf.** $(1)$: $F$ permutes the tensor factors, so $F(|a\rangle|b\rangle)=|b\rangle|a\rangle$ and $F(U\otimes U)=(U\otimes U)F$ since $U$ acts identically on both factors [machine: verified on a generating set $\{\pm I,\pm i\sigma_j\}$]. $(2),(3)$: direct computation; $\mathfrak T\Pi_{\mathcal R}=3\ne1=\mathfrak T\Pi_{\mathcal V}$ re-derives FT.101(3). $\blacksquare$

**Phys.** The pair carrier is four-dimensional and splits, under the swap, into a three-dimensional
symmetric block and a one-dimensional antisymmetric one. That split is the corpus's
real/virtual distinction at the level of the carrier, and it is *exactly* the decomposition the
Haar twirl diagonalizes. The two blocks carry different traces, which is why BM.131(4)'s formula
has two different denominators — a detail worth pinning, since a single normalization would be
wrong.

---

### A.10 — The twirl theorem, verified exactly by a finite subgroup

**Thm.** Let $2T$ be the binary tetrahedral group, $|2T|=24$, entries in $\mathbb Z[i]/2$,
$\det U=1$ for every element, closed under multiplication and inversion.
$$(1)\quad\textbf{the Schur hypothesis:}\qquad 2T\to A_4\ \text{is onto with kernel }\{\pm I\};\qquad \vee^2\ \text{carries }A_4\text{'s irreducible 3-dimensional representation};\qquad \wedge^2\ \text{carries the trivial one};$$
$$(2)\quad\textbf{the finite average IS the Haar twirl:}\qquad \frac1{24}\sum_{U\in 2T}(U\otimes U)\rho(U\otimes U)^\dagger\ =\ \int_{\mathrm{SU}(2)}(U\otimes U)\rho(U\otimes U)^\dagger d\mu_\star(U);$$
$$(3)\quad\textbf{BM.131(4), verified:}\qquad \boxed{\ \int_{\mathrm{SU}(2)}\!(U\otimes U)\rho\,(U\otimes U)^\dagger d\mu_\star(U)\ =\ \frac{\mathfrak T(\Pi_{\mathcal R}\rho)}{3}\,\Pi_{\mathcal R}\ +\ \mathfrak T(\Pi_{\mathcal V}\rho)\,\Pi_{\mathcal V}\ }$$
$$\text{verified on five exact carriers:}\quad \tfrac14I\ (\tfrac34,\tfrac14),\quad |00\rangle\langle00|\ (1,0),\quad \Pi_{\mathcal V}\ (0,1),\quad \tfrac13\Pi_{\mathcal R}\ (1,0),\quad \tfrac12\Pi_{\mathcal V}+\tfrac16\Pi_{\mathcal R}\ (\tfrac12,\tfrac12);$$
$$(4)\quad\textbf{the block traces are invariant under EVERY group element, not merely on average:}$$
$$\mathfrak T\bigl(\Pi_{\mathcal R}(U\otimes U)\rho(U\otimes U)^\dagger\bigr)=\mathfrak T(\Pi_{\mathcal R}\rho)\qquad\forall U\in2T\quad[\text{machine: }5\times24=120\ \text{exact conjugations}];$$
$$(5)\quad\textbf{status: derived.}$$

**Req.** A9(1),(2),(3) (this tier); A3, A5, A6 (Part 1); CT0.7(1) (Part 1); BM.131(1),(3),(4) (Part 4); Schur's lemma on a two-isotypic decomposition, the character theory of $A_4$ (irreps of dimensions $1,1,1,3$), exact complex-`Fraction` matrix arithmetic, exhaustive 576-product closure census [math; machine: `bit_qubit.py` §§B–C].

**Pf.**
$$(1):\ \text{the 24 elements are enumerated exhaustively; closure over all }576\ \text{products and inversion are verified entrywise}\ [\text{machine}];\ \vee^2\ \text{is }A_4\text{'s 3-dimensional rotation representation, which is irreducible since }A_4\text{'s irreps have dimensions }1,1,1,3;$$
$$(2):\ \text{two inequivalent irreps}\implies\operatorname{End}_{2T}(\mathbb C^4)=\mathbb C\Pi_{\mathcal R}\oplus\mathbb C\Pi_{\mathcal V}=\operatorname{End}_{\mathrm{SU}(2)}(\mathbb C^4)\ [\text{Schur}];\ \text{both averages are the projection onto this commutant, hence equal};$$
$$(3):\ \text{the average lies in the commutant, so it is }\alpha\Pi_{\mathcal R}+\beta\Pi_{\mathcal V};\ \text{applying }\mathfrak T(\Pi_{\mathcal R}\cdot)\ \text{and using (4) gives }\alpha\cdot3=\mathfrak T(\Pi_{\mathcal R}\rho),\ \text{and }\mathfrak T(\Pi_{\mathcal V}\cdot)\ \text{gives }\beta\cdot1=\mathfrak T(\Pi_{\mathcal V}\rho);$$
$$(4):\ \Pi_{\mathcal R},\Pi_{\mathcal V}\ \text{commute with }U\otimes U\ \text{by A9(1)}\implies\text{cyclicity of }\mathfrak T. \blacksquare$$

**Phys.** The Haar twirl is not an approximation to be integrated and not a limit to be taken —
on this carrier it is a **24-term exact average**, because the tetrahedral group is already large
enough to act irreducibly on both blocks. That is what makes the whole construction
machine-checkable in exact arithmetic, and it is the reason the bit is exactly defined rather
than defined up to an integral.

---

### A.11 — The tensor form: the twirl is a rank-2 idempotent superoperator

**Thm.**
$$(1)\quad\textbf{the twirl as a }(2,2)\text{-tensor on the 16-dimensional operator space:}$$
$$\boxed{\ \mathrm{Twirl}(\rho)_{ab}=\mathcal W_{ab}{}^{cd}\,\rho_{cd},\qquad \mathcal W_{ab}{}^{cd}=\frac{(\Pi_{\mathcal R})_{ab}(\Pi_{\mathcal R})^{cd}}{3}+(\Pi_{\mathcal V})_{ab}(\Pi_{\mathcal V})^{cd}\ }$$
$$(2)\quad\textbf{idempotence:}\qquad \mathcal W^2=\mathcal W\qquad[\text{machine: all }256\ \text{entries of }\mathcal W^2\ \text{compared entrywise over }\mathbb Q(i)];$$
$$(3)\quad\textbf{rank:}\qquad \boxed{\ \operatorname{rk}\mathcal W=2\ }\qquad[\text{machine: exact elimination on the flattened }16\times16\ \mathcal W];\qquad \operatorname{im}\mathcal W=\operatorname{span}\{\Pi_{\mathcal R},\Pi_{\mathcal V}\};$$
$$(4)\quad\textbf{trace preservation:}\qquad \mathfrak T(\mathrm{Twirl}(\rho))=\mathfrak T(\Pi_{\mathcal R}\rho)+\mathfrak T(\Pi_{\mathcal V}\rho)=\mathfrak T\rho;$$
$$(5)\quad\textbf{the rank drop:}\qquad \boxed{\ 15\ \longrightarrow\ 2\ \longrightarrow\ 1\ }$$
$$\rho_{ab}\ \text{Hermitian, PSD},\ \mathfrak T\rho=1:\ 15\ \text{real parameters}\quad\xrightarrow{\ \mathcal W\ }\quad \operatorname{span}\{\Pi_{\mathcal R},\Pi_{\mathcal V}\}:\ 2\quad\xrightarrow{\ \mathfrak T\rho=1\ }\quad b\in[0,1]:\ 1;$$
$$(6)\quad\textbf{status: derived.}$$

**Req.** A9, A10 (this tier); CT0.7(1), CT1.1 (Part 1); BM.131(4) (Part 4); exact $16\times16$ matrix multiplication and Gaussian elimination over $\mathbb Q(i)$ [math; machine: `bit_qubit.py` §D].

**Pf.** $(2)$: $\mathcal W^2$ expands using $\Pi_{\mathcal R}^2=\Pi_{\mathcal R}$, $\Pi_{\mathcal V}^2=\Pi_{\mathcal V}$, $\Pi_{\mathcal R}\Pi_{\mathcal V}=0$, $\mathfrak T\Pi_{\mathcal R}=3$, $\mathfrak T\Pi_{\mathcal V}=1$ [A9(2),(3)] — verified entrywise rather than argued. $(3)$: exact elimination. $(5)$: $\dim\mathfrak H(\mathbb C^4)=16$, the trace condition removes one, giving 15; $\operatorname{rk}\mathcal W=2$ by (3); $\mathfrak T\rho=1$ relates the two block traces, leaving one. $\blacksquare$

**Phys.** This is the tensor form the tier was asked for. The qubit is a 15-parameter carrier;
the twirl is a rank-2 idempotent acting on it; the trace condition collapses the rank-2 image to
a single parameter. **The bit/qubit distinction is a rank drop under a gauge projection** —
$15\to2\to1$ — and the 14 parameters the twirl annihilates are precisely the $\mathrm{SU}(2)$
gauge freedom that A6 declares unrecorded ($U\notin\mathfrak L$).

---

### A.12 — The bit is the UNIQUE Haar-gauge-invariant parameter

**Thm.**
$$(1)\quad\textbf{the invariant-functionals theorem:}\qquad L(\rho)=\mathfrak T(X\rho)\ \text{is Haar-invariant}\iff (U\otimes U)^\dagger X(U\otimes U)=X\ \forall U\iff X\in\operatorname{End}_{\mathrm{SU}(2)}(\mathbb C^4);$$
$$(2)\quad\textbf{the commutant is exactly two-dimensional:}\qquad \{X:[X,W_i]=0,\ i=1,2,3\}=\operatorname{span}_{\mathbb C}\{\Pi_{\mathcal R},\Pi_{\mathcal V}\},\qquad \dim=2$$
$$[\text{machine: }48\ \text{complex equations from }[X,W_i]=0\ \text{on }16\ \text{unknowns, exact elimination over }\mathbb Q(i);\ \text{constraint rank }14,\ \text{nullity }2];$$
$$(3)\quad\textbf{hence, on the physical slice:}\qquad r:=\mathfrak T(\Pi_{\mathcal R}\rho),\quad v:=\mathfrak T(\Pi_{\mathcal V}\rho),\quad r+v=\mathfrak T\rho=1\implies v=1-r;$$
$$\boxed{\ b(\rho)\ :=\ \mathfrak T(\Pi_{\mathcal R}\rho)\ =\ (\Pi_{\mathcal R})^{ab}\rho_{ba}\ \in[0,1]\quad\textbf{is the UNIQUE free Haar-gauge-invariant parameter of the carrier}\ }$$
$$(4)\quad\textbf{the exact bit values:}\qquad b(\tfrac14I)=\tfrac34;\quad b(|00\rangle\langle00|)=1;\quad b(\Pi_{\mathcal V})=0;\quad b(\tfrac13\Pi_{\mathcal R})=1;\quad b(\tfrac12\Pi_{\mathcal V}+\tfrac16\Pi_{\mathcal R})=\tfrac12;$$
$$(5)\quad\textbf{status: derived.}\qquad\textbf{This clause sharpens the direction given: the bit is not merely "the trace of the }\Pi_{\mathcal R}\text{ block" — it is the only invariant there is, which is why the record can hold it and nothing else.}$$

**Req.** A9, A10(4), A11 (this tier); A3, A5, A6 (Part 1); CT1.2 ($W_i$), CT0.7(1) (Part 1); L1(2), BM.131(3),(4) (Part 1/Part 4); Schur's lemma, exact linear algebra over $\mathbb Q(i)$ [math; machine: `bit_qubit.py` §E].

**Pf.** $(1)$: $\mathfrak T(X(U\otimes U)\rho(U\otimes U)^\dagger)=\mathfrak T((U\otimes U)^\dagger X(U\otimes U)\rho)$ by cyclicity, and this equals $\mathfrak T(X\rho)$ for all $\rho$ iff the operators agree. $(2)$: exact elimination; the nullity $2$ is attained by $\Pi_{\mathcal R},\Pi_{\mathcal V}$, which are independent since $\mathfrak T\Pi_{\mathcal R}=3\ne1=\mathfrak T\Pi_{\mathcal V}$. $(3)$: $\mathfrak T\rho=\mathfrak T((\Pi_{\mathcal R}+\Pi_{\mathcal V})\rho)=r+v$. $\blacksquare$

**Phys.** The uniqueness is the content. A record can only hold gauge-invariant quantities, and on
the pair carrier there is exactly one: the real-block trace. Everything else about the qubit —
all 14 remaining parameters — is $\mathrm{SU}(2)$ gauge and is forgotten by construction, which is
A6's "$U\notin\mathfrak L$" read as a statement about information rather than about bookkeeping.
The bit is not a coarse-graining choice; it is the whole invariant content.

---

### A.13 — A4 makes the bit binary: the crystallization threshold on the block trace

**Thm.**
$$(1)\quad\textbf{the criterion, in terms of the bit:}\qquad e\in\mathcal R\iff |\Pi_{\mathcal V}\rho|\le\varepsilon_q\ \vee\ |\Pi_{\mathcal V}\rho|\ge1-\varepsilon_q\qquad[\mathrm{A4};\ \mathrm{D1.1};\ \mathrm{CT0.1};\ \mathrm{Def\text{-}BM.18}(1)];$$
$$v=1-b\implies\boxed{\ b\ge1-\varepsilon_q\ \ (\text{the ALIGNED branch},\ \alpha=0)\qquad\text{or}\qquad b\le\varepsilon_q\ \ (\text{the ANTIALIGNED branch},\ \alpha=\pi)\ }$$
$$\varepsilon_q<b<1-\varepsilon_q\ \ (\text{equivalently }\varepsilon_q<v<1-\varepsilon_q):\ \textbf{UNREGISTERED — the flicker window};$$
$$(2)\quad\textbf{the window:}\qquad\text{width in }v\ \text{is}\ 1-2\varepsilon_q;\qquad \varepsilon_q=0\implies\text{the window is the whole open interval, so ONLY }v\in\{0,1\}\ \text{register};$$
$$\varepsilon_q\to\tfrac14{}^-\implies\text{width}\to\tfrac12;\qquad \varepsilon_q\in[0,\tfrac14)\ [\mathrm{CT0.8};\ \mathrm{D0.4}];$$
$$(3)\quad\textbf{the branch states attain the extremes exactly:}\qquad b(\tfrac13\Pi_{\mathcal R})=1,\quad b(\Pi_{\mathcal V})=0;$$
$$\alpha=0\ (\text{aligned},\ \vee^2,\ \text{Casimir }2):\ \textbf{weak-active};\qquad \alpha=\pi\ (\text{antialigned},\ \wedge^2,\ \text{Casimir }0):\ \textbf{weak-blind}\qquad[\mathrm{FT.101}(1)\text{--}(2)];$$
$$(4)\quad\textbf{both branches are realized, and both crystallize:}\qquad\text{A4's ``both branches are realized'' is the statement that the threshold has TWO registered sides, not one};$$
$$(5)\quad\textbf{status: derived.}$$

**Req.** A9, A12 (this tier); A4, D0.4, D1.1, CT0.1, CT0.8 (Part 1); FT.101(1)–(3) (Part 3); Def-BM.5(5), Def-BM.18(1), BM.19(3) (Part 4); exact rational interval arithmetic on $[0,\tfrac14)$ [math; machine: `bit_qubit.py` §F].

**Pf.** $(1)$: substitute $v=1-b$ [A12(3)] into Def-BM.18(1)'s criterion. $(2)$: the window is the open interval $(\varepsilon_q,1-\varepsilon_q)$, of width $1-2\varepsilon_q$; at $\varepsilon_q=0$ it is $(0,1)$, so registration requires $v\in\{0,1\}$ — which is Def-BM.5(5)'s collapse to the single crystallized configuration, and BM.19(3)'s $x_-=4\varepsilon_q=0$ (no dissolution move exists). $(3)$: A12(4). $\blacksquare$

**Phys.** The bit is continuous before crystallization and binary after it, and the threshold that
bins it is A4's — the corpus's own crystallization criterion, not a new one. Both extremes
register, which is why the corpus has two branches rather than a bit and its absence: the aligned
branch is weak-active and the antialigned is weak-blind [FT.101], so the *same* binary datum
carries the 3+1 selectivity that FT.157(3) identifies as the weak support. At
$\varepsilon_q=0$ nothing flickers and only pure branch states exist; the flicker window is what
makes the intermediate values physical at all.

---

### A.14 — The duality as the frame, with no global tick

**Thm.**
$$(1)\quad\textbf{the factorization:}\qquad \rho\ \longmapsto\ U\,\tilde{\mathcal T}_\gamma(\rho)\,U^\dagger,\qquad U\sim\mu_\star,\ U\notin\mathfrak L\qquad[\mathrm{BM.131}(1);\ \mathrm{A6};\ \mathrm{L0}];$$
$$\textbf{the Haar side is the exact gauge freedom of the record};\qquad\textbf{the Poisson side }\tilde{\mathcal T}_\gamma(\rho)=\frac{\rho e^{-\gamma\rho}}{\mathfrak T(\rho e^{-\gamma\rho})},\ \gamma=1-4\varepsilon_q,\ \textbf{is the recorded dynamics};$$
$$(2)\quad\textbf{the fixed loci:}\qquad\text{Haar:}\ \Bigl\{\tfrac x3\Pi_{\mathcal R}+(1-x)\Pi_{\mathcal V}:x\in[0,1]\Bigr\}\ \text{(the block-maximal-mixed family)};\qquad\text{Poisson:}\ \lambda_i'=\lambda_i\iff\lambda_i\ \text{all equal}\iff\rho=\tfrac14I;$$
$$\boxed{\ \{\text{Poisson fixed}\}\cap\{\text{Haar-twirl fixed}\}\ =\ \{\tfrac14I\}\ }\qquad\text{at }x=\tfrac34,\ \text{where }b=\mathfrak T(\Pi_{\mathcal R}\tfrac14I)=\tfrac34;$$
$$(3)\quad\textbf{the record is blind to the Haar factor:}\qquad V\ \text{invariant under the Haar factor}\ [\mathrm{L1}(2)],\ \text{strictly contracting under the Poisson factor}\ [\mathrm{L2}];$$
$$V_n=\Bigl(1-\tfrac\gamma4\Bigr)^{2n}V_0+O,\qquad \Bigl(1-\tfrac\gamma4\Bigr)^2+\tfrac{\gamma(8-\gamma)}{16}=1\qquad[\mathrm{BM.51}(2),(3);\ \text{exact in }\mathbb Q[\gamma]];$$
$$\boxed{\ \textbf{the unrecorded Haar draws drop out of the record exactly: }V_n\ \textbf{depends on the tilt count alone}\ }$$
$$(4)\quad\textbf{NO GLOBAL TICK IS USED:}\qquad\text{the index }n\ \text{in }V_n\ \textbf{counts tilt events (Poisson steps), not ticks};\qquad b(\rho)\ \text{is defined by a gauge projection,}\ \neg\text{by a time ordering};$$
$$\text{the only ordering invoked is A6's strict forwardness of the tilt, which BM.131(1) already factorizes and BM.131(5) already shows the record to be blind to the Haar part of};$$
$$(5)\quad\textbf{the construction, assembled:}\qquad\begin{array}{l|l}
\textbf{QUBIT} & \rho\in\mathfrak H(\mathbb C^4),\ \mathfrak T\rho=1:\ 15\ \text{real parameters, carrying an exact }\mathrm{SU}(2)\ \text{gauge orbit}\\
\textbf{TWIRL} & \mathcal W_{ab}{}^{cd}=(\Pi_{\mathcal R})_{ab}(\Pi_{\mathcal R})^{cd}/3+(\Pi_{\mathcal V})_{ab}(\Pi_{\mathcal V})^{cd}:\ \mathcal W^2=\mathcal W,\ \operatorname{rk}=2\\
\textbf{BIT} & b(\rho)=\mathfrak T(\Pi_{\mathcal R}\rho)\in[0,1]:\ \text{the unique gauge invariant, thresholded by A4 into }\alpha\in\{0,\pi\}\\
\textbf{RECORD} & \text{the Poisson tilt count, to which }V_n=(1-\tfrac\gamma4)^{2n}V_0\ \text{reduces exactly}\end{array}$$
$$(6)\quad\textbf{status: derived.}\qquad\neg\text{a declaration},\ \neg\text{a P4 addition},\ \neg\text{a new dimensionful scale},\ \neg\text{a measured value}\ [\mathrm{P5}],\ \neg\text{a species identification},\ \neg\text{a global tick.}$$

**Req.** A9–A13 (this tier); A5, A6, D0.3, D0.4, L0, L1(1),(2), L2, CT0.8 (Part 1); BM.34(2), BM.51(2),(3), BM.131(1),(2),(3),(4),(5),(7) (Part 4); exact formal-series identities in $\mathbb Q[\gamma]$, the pointwise finite twirl at four exact $x$ [math; machine: `bit_qubit.py` §G].

**Pf.** $(2)$: on the block family the eigenvalues are $(x/3,x/3,x/3,1-x)$; the Poisson side is fixed only when all are equal [BM.131(4): $e^{-\gamma\lambda_i}=Z_\gamma\ \forall i$ with $\gamma>0$], i.e. $x/3=1-x\iff x=\tfrac34$, giving spectrum $(\tfrac14,\tfrac14,\tfrac14,\tfrac14)$, i.e. $\rho=\tfrac14I$ — the A5 vacuum. Verified pointwise by the exact finite twirl at $x\in\{0,\tfrac14,\tfrac34,1\}$. $(3)$: L1(2)'s invariance composed with L2's contraction and BM.51's identity. $\blacksquare$

**Phys.** The duality *is* the frame, exactly as directed, and it makes the bit/qubit distinction
a statement about what a record can hold. The Haar side is pure gauge — it moves the carrier and
leaves every read untouched, which is why the draws are not in the ledger. The Poisson side is
the only part that changes anything, and what it changes is $V$, contracting by the exact rational
factor $(1-\gamma/4)^2$ per tilt. The bit sits at the junction: it is the one number the gauge
cannot touch, and the tilt count is the one number the record keeps. Their unique common fixed
point is the vacuum $\rho_\circ=\tfrac14I$ at $b=\tfrac34$ — the state that carries no bit at all,
because it is the state on which the twirl and the tilt agree that nothing is happening.

---

## §Open-A additions from Tier A.2

| row | content | locus |
|---|---|---|
| (A-O8) | whether the **Poisson side** admits a tensor form dual to $\mathcal W$: $\tilde{\mathcal T}_\gamma$ is spectral, not a fixed superoperator, since $\delta K=\gamma\rho+\log Z_\gamma\cdot I$ is $\rho$-dependent [BM.131(2)]. A tensor form would be state-dependent, i.e. nonlinear — worth stating as a no-go or constructing as a family | A.14(1); BM.131(2) |
| (A-O9) | the **carrier-level companion**: BM.131(6)'s finite-group twirl $\Pi_k=\frac1{k!}\sum_{\sigma\in S_k}\hat P_\sigma$ with $\operatorname{rk}\Pi_k=k+1$, $\operatorname{im}\Pi_k=\mathrm{Sym}^k(\mathbb C^2)$, gives the same bit/qubit pattern at every $k$; the seed-tensoring mechanism BM.138 is named but not assembled here | A.11; BM.131(6); BM.138 |
| (A-O10) | the **relation to the metric**: BM.131(7) supplies the proper-time contraction $ds^2=-N^2d\tau^2+g_{ij}(dx^i+N^id\tau)(dx^j+N^jd\tau)$ as the duality's metric read. Whether the bit $b$ has a metric conjugate — and if so whether it is the T-odd shift block of A.2 — is open and is the natural join between Tiers A.1 and A.2 | A.14; BM.131(7); A.2 |
