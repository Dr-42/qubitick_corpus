# $\langle qu(b(i(t|t))ick)\rangle$ — **Part 1 · Qubit\_era** — Axioms · Conventions · Qubit-Era Definitions · Pair Canon · Ledger Dynamics

**0.1 Corpus map.** The canon is the era chain
$$
\textbf{Part 1 · Qubit\_era}\ \longrightarrow\ \textbf{Part 2 · Bosonic\_era}\ \longrightarrow\ \textbf{Part 3 · Fermion\_era}\ \longrightarrow\ \textbf{Part 4 · Baryomesonic\_era},
$$
each part citing only its priors, itself (earlier tags), and the Census annex (the computed data cells, cited row-wise by tag). Part 1 (this chapter): §A axioms A1–A9 · §B conventions C1–C13 · §C the definition layer D0.1–D4.3 (the corpus-wide vocabulary root: Tiers 0–1 qubit-era, Tiers 2–4 naming the structures the bosonic era derives) · §D master symbol table · §E calibration policy P1–P5 · §F foundations (CT0.1–CT0.14, CT1.0–CT1.11b, L0–L5). Part 2 (section letters preserve the classical canon's): §C CT1.12–CT2.11 (geometry), §D EW.1–EW.36a (electroweak), §E EM.1–EM.26 (electromagnetic), §F CT3.1–CT3.22a (colour), §G CT4.1–CT4.13 (saturation), §Cal-2 (registry note). Part 3: Def-H.1–Def-H.43, FT.1–FT.145 (structural tags), FT.153–FT.155. Part 4: Def-BM.1–Def-BM.2, BM.1–BM.6. Census: the 25 data-cell tags (Category B of the separation charter).

**0.2 Citation closure.** $\forall$ claims in Parts 1–4 cite only: A1–A9, C1–C13, D0.1–D4.3, P1–P5 (Parts 1–2), previously proved tags, and Census cells (row-wise). $\neg\exists$ imported external physical law, constant, or measured value. Physics vocabulary $:=$ naming of derived structures only. External comparison data enter only quarantined audit rows (Census FT.114, FT.120; P1, P5).

**0.2a Math & hypothesis policy.** Standard mathematics (linear algebra, representation theory, tensor calculus, classification theorems) is cited as $[\text{math}]$-class tags in **Req** and is not part of the physical axioms. Conditional theorems carry their hypotheses explicitly in **Thm** and **Req**. The complete list of extra-axiomatic inputs is empty: CT2.6 (ii), CT2.6 (iii) — the two continuum-limit conditions — are derived theorems of Part 4 (Tier BM.24, BM.151): (ii) is witnessed by the ledger's own unbounded ladder, (iii) by the density-matrix spectral bound on the D2.1 coefficient fields; no others exist. The declarations at use stand as scope-inheritance markers over the same loci. CT2.6 (i) is a definitional precondition: the valid-universe condition of D2.11 in application (“there is something”), $\neg$ an extra-axiomatic hypothesis. CT2.8 carries no hypotheses: its reflection and factorization clauses are derived (D2.7, D1.9, D1.3, D2.8). The edge phase is registration data: its alphabet is derived (CT0.9) and its per-edge value is determined at crystallization (Def-EM.20, EM.20). **Integration note.** The integer-edge hypothesis of CT1.29a is *not* independent: it is realized on materialized closed chains of the fully antialigned class (CT1.19b(3)). The ambient-richness condition in the CT3.22a Rmk is a witness scope for that Rmk's non-locality construction only; no theorem clause of Parts 1–2 rests on it. The materialization domain of CT1.19b is CT2.5’s own pole condition (no new input); its domain-generalization step from EW.17’s wrapping chains is flagged in its Pf. The per-edge independence hypothesis of CT4.5a is an ensemble scope for that theorem alone — its dynamics realization (a crystallization-rate datum) is NOT declared in Parts 1–2. The crystallization–tilt coupling of L0 (a seal-time state update: one Gibbs tilt step per A4 event) and the finite-incidence scope of L4 are theorem-local scopes of the same species, declared at use. The interface definitions of Part 3 (Def-H.35–Def-H.43) carry their own non-derived clauses explicitly.

**0.3 Free data.** $\exists!\,$ free dimensionful scale: $\mathfrak h$ (D2.9, P1). Every other quantity: dimensionless-derived, or a power of $\mathfrak h$. Free internal configuration parameters (P4-class, $\neg$constants of the theory): the P4 core (§E) plus the era registries Cal-2 (Part 2), Cal-F (Part 3), Cal-BM (Part 4).

**0.4 Theorem format (all parts).** Per tag:
**Thm** — statement, purely symbolic · **Req** — {axioms, conventions, definitions, prior theorems} used · **Pf** — derivation, purely symbolic, justifications in $[\cdot]$, end $\blacksquare$ · **Phys** — short English summary of the theorem and its physics. Corollaries: **Cor**. Definitions: **Def.** blocks; scope conditions and constitutive clauses are carried inside the **Def.**/**Thm.** text. Forward pointers (scope conditions cited at use) are marked “forward pointer” at the citing site.

**0.5 Symbol reconciliations.** $P_M\equiv\mathcal P_M$ (C7); $F_Z\equiv F_{W^3}$ (C8); $\tau(v)\in\Xi_n$ (type set) vs $v\in V_n$ (vertex set), D0.8.

**0.6 Machine verification.** `checks/`: dependency-free exact-arithmetic verification suite (`python3 checks/run_all.py`). `verify_era_structure.py`: era-chain law, citation closure, census separation, tag ownership, declaration hygiene, **Thm·Req·Pf·Phys** completeness, index regeneration. `verify_B.py`–`verify_G.py` and the `verify_*` content suite: algebraic/geometry/arithmetical identities, exact, no floating point. See `checks/README.md`.

---

## §A — Axioms

**A1.**
$$
\mathcal Q=\{q_n\}_{n\ge1};\qquad
\mathcal H_q\cong\mathbb C^2;\qquad
\forall(p,q)\in\mathcal Q\times\mathcal Q,\ p\ne q:\quad
\rho_{pq}\in\mathfrak H(\mathcal H_p\otimes\mathcal H_q),\ \ \rho_{pq}\succeq0,\ \ \mathfrak T(\rho_{pq})=1 .
$$

**A2.**
$$
\forall(p,q):\qquad C(p,q)=1\,\mathfrak q .
$$

**A3.**
$$
\mathcal H_p\otimes\mathcal H_q=\vee^2\oplus\wedge^2;
$$
$$
S(\sigma_\mu\otimes\sigma_\nu)=\sigma_\nu\otimes\sigma_\mu,\quad S^2=\mathbb1;\qquad
T(\sigma_\mu\otimes\sigma_\nu)=\eta^\mu\eta^\nu\,(\sigma_\mu\otimes\sigma_\nu),\quad
T^2=\mathbb1;
$$
$$
\eta\in\{\pm1\}^4;\qquad
\exists!\,\mathfrak o\in\{0,1,2,3\}:\ \ \eta^{\mathfrak o}=-\eta^{\mu}\ \ \forall\mu\ne\mathfrak o .
$$

**A4.**
$$
(p,q)\in\mathcal R\iff\bigl|\Pi_{\mathcal V}\rho_{pq}\bigr|\le\varepsilon_q\ \ \vee\ \ \bigl|\Pi_{\mathcal V}\rho_{pq}\bigr|\ge1-\varepsilon_q;\qquad
n_{\mathcal R}(p)=\bigl|\{q:(p,q)\in\mathcal R\}\bigr|
$$
$$
\alpha_{pq}:=\begin{cases}0&\bigl|\Pi_{\mathcal V}\rho_{pq}\bigr|\le\varepsilon_q\\[1mm] \pi&\bigl|\Pi_{\mathcal V}\rho_{pq}\bigr|\ge1-\varepsilon_q\end{cases};\qquad
\alpha_{pq}\in\{0,\pi\}\quad\forall(p,q)\in\mathcal R;
$$
$$
\exists\,\rho_{pq}:\ \bigl|\Pi_{\mathcal V}\rho_{pq}\bigr|\le\varepsilon_q;\qquad
\exists\,\rho_{p'q'}:\ \bigl|\Pi_{\mathcal V}\rho_{p'q'}\bigr|\ge1-\varepsilon_q .
$$

**A5.**
$$
\rho_\circ=\tfrac14 I;\qquad
\rho\mapsto U\rho U^\dagger,\quad U\sim\mu_\star\bigl(\mathrm{SU}(2)\bigr),\quad U\notin\mathfrak L .
$$

**A6.**
$$
\mu_\star:=\mu_{\mathrm{Haar}}\bigl(\mathrm{SU}(2)\bigr);\qquad
U\sim\mu_\star;\qquad
U\notin\mathfrak L;\qquad
\mathcal T(\rho):=U\rho U^\dagger;\qquad
\mathcal T^{-1}(\rho)=U^\dagger\rho U
$$
$$
\mathfrak T\bigl(\mathcal T(\rho)\bigr)=\mathfrak T(\rho);\qquad
\mathcal T^{2}\ne\mathbb1;\qquad
\tau_n\to\tau_{n+1}:\ \ \rho\mapsto\mathcal T(\rho);\qquad
\neg\exists\,\tau^{-1}
$$
$$
\bigl|\mathfrak L(\tau_{n+1})\bigr|\ \ge\ \bigl|\mathfrak L(\tau_n)\bigr|;\qquad
\bigl|\mathfrak L(\tau_{n+1})\bigr|\ =\ \bigl|\mathfrak L(\tau_n)\bigr|\,+\,n_{\mathrm{real\_out}}(\tau_n) .
$$

**A7.**
$$
\forall n\ge0:\quad\Gamma=(V,E),\qquad E\subseteq V\times V
$$
$$
\tau(v):=\bigl(\partial^{\leftarrow}(v),\partial^{\rightarrow}(v)\bigr)\in\Xi_n;\qquad
e\in E_{\mathcal R}\mapsto\phi_e;\qquad
e\in E_{\mathcal R}\mapsto\alpha_e\in\{0,\pi\}
$$
$$
\mathfrak L=\bigcup_{n\ge0}\mathfrak L(\tau_n);\qquad
\mathfrak L(\tau_n)\subseteq\mathfrak L(\tau_{n+1});\qquad
\bigl|\mathfrak L(\tau_0)\bigr|=0;\qquad
\bigl|\mathfrak L(\tau_n)\bigr|=\sum_{k<n}n_{\mathrm{real\_out}}(\tau_k) .
$$

**A8.**
$$
\mathbf F=\mathbf F_{(+,\mathcal R)}\oplus\mathbf F_{(-,\mathcal R)}\oplus\mathbf F_{(+,\mathcal V)}\oplus\mathbf F_{(-,\mathcal V)}\oplus\mathbf F_{\mathrm{st}};
$$
$$
\mathbf F_{(+,\mathcal R)}=F_G\oplus F_H\oplus F_{D^+};\qquad
\mathbf F_{(-,\mathcal R)}=F_{W^+}\oplus F_{W^-}\oplus F_Z;\qquad
\mathbf F_{(+,\mathcal V)}=F_{J^+};
$$
$$
\mathbf F_{(-,\mathcal V)}=F_{J^-};\qquad
\mathbf F_{\mathrm{st}}=F_{\mathrm{EM}}\oplus F_{\mathrm{strong}}\oplus F_{D^-};
$$
$$
F_{D^+}=\Lambda\,\mathbb I;\qquad
F_{D^-}:=\bigoplus_{n\ge4}F_n;\qquad
\mathbf F_M=P_M\,\mathbf F\,P_M;
$$
$$
w(C)=\mathcal J(C)\!\!\prod_{e\in E(C)}\!\!G(e)\ \cdot\ (-1)^{\aleph(\sigma,C)};\qquad
Z(\mathcal R)=\sum_{C\in\mathcal R}\ \sum_\sigma w(C) .
$$

**A9.**
$$
\mathcal U_\odot\in\mathfrak S\bigl(Z[\mathbf F_\oplus,M_\oplus]\bigr);\qquad
\mathcal U_\odot\notin\mathfrak S\implies\neg\bigl(\mathrm{A1}\wedge\cdots\wedge\mathrm{A9}\bigr) .
$$

$\blacksquare$

---

## §B — Conventions

**C1.** $\mu,\nu,\rho,\ldots\in\{0,1,2,3\}$: Pauli basis $\sigma_0=I_2,\sigma_1,\sigma_2,\sigma_3$ / emergent spacetime coordinates where a metric exists; $i,j,k,\ldots\in\{1,2,3\}$: spatial/Pauli-spatial; $a,b,c,\ldots\in\{1,\dots,8\}$: colour adjoint. Repeated indices: summed.

**C2.** $T_A^\dagger=T_A$; $\ [T_A,T_B]=i\,f_{AB}{}^{C}\,T_C$; $\ f_{AB}{}^{C}\in\mathbb R$.

**C3.** $\mathcal E_{st}:=\{\,X\in\mathfrak H(\mathbb C^4):\ SX=sX\ \wedge\ TX=tX\,\}$, $s,t\in\{+,-\}$. Symbol $\wedge$: antisymmetrization only ($\wedge^2$, $\varepsilon$-contractions); $\neg$ a sector-label conjunct.

**C4.** $\varkappa$: sector-to-metric embedding scale (D2.1); $\kappa$: gravitational coupling (D2.9, CT2.9); $\varkappa\ne\kappa$; $\neg$ interchangeable.

**C5.** $\Sigma:=\sum_i\sigma_i\otimes\sigma_i$ (operator); $\Sigma_{\mathrm{tr}}:=\delta^{ij}q_{ij}\in\mathbb R$ (scalar, D2.1); $\neg$ interchangeable.

**C6.** $\mathsf E_{\mathrm{tr}}$: transit entropy; $\mathsf E_{\mathrm{bd}}$: bound entropy (D1.5); $\neg$ squared-field notation for either.

**C7.** $P_M\equiv\mathcal P_M$ (A8). Rung-resolved: $\mathcal P_M^{(n)}$ (D2.3); $\ \mathbf F_M^{(n)}=\mathcal P_M^{(n)}\,\mathbf F\,\mathcal P_M^{(n)}$.

**C8.** $F_Z\equiv F_{W^3}$: neutral-weak aspect of A8; $\ F_W:=F_{W^+}\oplus F_{W^-}\oplus F_Z$; pre-mixing seed generator: $W_3$. Bare $Z$ in a spectrum: physical neutral eigenstate (D3.10, EW.24); $Z(\cdot)$ with argument: partition function (A8) / masked resolvent (D2.4).

**C9.** Entropy in nats: $S=\ln\Omega$; _bits_ only where explicit. One real edge $=1$ bit $=\ln2$ nats (CT0.9, CT1.29).

**C10.** Register accounting (reality principle): registrations convert quantum data to classical alternatives at the ledger. Registering a classical alternative set $X$ for single-shot linear readout ($\mathfrak L$ must distinguish which value was carried, D0.7) assigns the alternatives mutually orthogonal register directions: register cost $=|X|$. Shannon content $=\log_2|X|$ bits is a distinct quantity: source-availability register count $\ne$ channel bit throughput. One channel quantum supplies $C_{\mathrm{cap}}=\dim_{\mathbb R}\mathfrak H(\mathcal H_p\otimes\mathcal H_q)=16$ register directions (A2, D0.9). Ledger-level registration data are real: edge transport acts on the reality line by $\{\pm1\}$ (D1.1, CT0.9).

**C11.** A5/A6 reading: the conjugation clause is node-level — $\rho\mapsto U\rho U^\dagger$ [A6: $\mathcal T$] with $\rho\in\mathfrak H(\mathcal H_q)\cong\mathfrak H(\mathbb C^2)$ and $U\sim\mu_\star(\mathrm{SU}(2))$ ($2\times2$: well-typed); $\rho_\circ=\tfrac14I$ is the vacuum pair state ($4\times4$). Node tick lifecycle: wait $\to$ data in $\to$ Haar draw/tick [A6: $\tau_n\to\tau_{n+1}$] (virtual states as basis) $\to$ data out/hop $\to$ wait. Draws are not retained: $U\notin\mathfrak L$ [A5, A6].

**C12.** In A8's $Z(\mathcal R)=\sum_{C\in\mathcal R}\sum_\sigma w(C)$ the summation domain reads $\mathfrak C(\mathcal R)$ (D0.10): the configuration set on the real-edge set. $\mathcal R$ itself (A4, D0.1) is a set of pairs and is never a summation domain.

**C13.** Signature convention. A3 fixes $T$ only through the products $\eta^\mu\eta^\nu$, and fixes $\eta$ only up to its odd slot $\mathfrak o$ and its overall sign. The corpus takes $\mathfrak o:=0$ (the identity slot $\sigma_0=I_2$, C1) and $\eta^{0}:=-1$, i.e. $\eta:=(-,+,+,+)$ (mostly-plus; D2.1: $\bar g_{00}:=-1$). The overall sign does not change $T$ [CT1.0(2)]; the three choices $\mathfrak o\in\{1,2,3\}$ are conjugate under $\mathrm{SU}(2)$ relabelling of the spatial Pauli axes [CT1.0(4)]; $\mathfrak o=0$ versus $\mathfrak o\ge1$ is the choice of the $\mathrm{SU}(2)$-covariant representative [CT1.0(5)], on which CT1.2's generator table rests [CT1.0 Rmk]. Uses of the representative carry the tag C13. $\neg$ an axiom.

---

## §C — The definition layer

Definitions $:=$ vocabulary stipulations. $\forall$ content-bearing claims: theorems of Parts 1–4. Tiers 0–1 are qubit-era vocabulary; Tiers 2–4 name the structures the bosonic era derives — the definition layer is the corpus-wide vocabulary root (the classical canon's A §Part 3).

### Tier 0 — bookkeeping

**D0.1.** $\mathcal R:=\{(p,q):\ \mathrm{A4}\ \text{holds}\}$; $\ \mathcal V:=(\mathcal Q\times\mathcal Q)\setminus\mathcal R$; $\ n_{\mathcal R}:=\sum_p n_{\mathcal R}(p)$; global vacuum $\iff n_{\mathcal R}=0$.

**D0.2.** $\bigl|\Pi X\bigr|:=\mathfrak T(\Pi X\Pi)=\mathfrak T(\Pi X)$; $\ \ \rho\succeq0\wedge\mathfrak T\rho=1\implies\bigl|\Pi\rho\bigr|\in[0,1]$.

**D0.3.** $S_{\mathrm{raw}}(\rho):=-\mathfrak T(\rho\log\rho)=\mathfrak T(\rho K)$; $\ K:=-\log\rho$ (faithful $\rho$). $\ \gamma:=1-4\varepsilon_q$ [A4, D0.4, CT0.8]; $\ \gamma\in(0,1]$ for $\varepsilon_q\in[0,\tfrac14)$. Gibbs tilt (functional calculus): $\tilde{\mathcal T}_\gamma(X):=Xe^{-\gamma X}/\mathfrak T(Xe^{-\gamma X})$ where $\mathfrak T(Xe^{-\gamma X})\ne0$; on states: $\tilde{\mathcal T}_\gamma(\rho)=\rho\,e^{-\gamma\rho}/\mathfrak T(\rho\,e^{-\gamma\rho})$; $\ \gamma=0:$ the identity on trace-$1$ states; for faithful $\rho$: $\tilde{\mathcal T}_\gamma(K)=K\rho^{\gamma}/\mathfrak T(K\rho^{\gamma})$ $\ (\gamma=1:\ =\rho(-\log\rho)/S_{\mathrm{raw}}(\rho))$. Variance functional (reference state explicit): $\mathbb V_\rho(X):=\mathfrak T(\rho X^2)-\bigl(\mathfrak T(\rho X)\bigr)^2$. Lyapunov functional of the tilt: $V(\tilde K):=\mathfrak T(\tilde K^2)$, $\ \tilde K:=K-\mathfrak T(K\rho)\,I$ — monotonicity: L1 (§F, forward pointer). $\tilde{\mathcal T}_\gamma\ne\mathcal T$ [A6]; $\neg$ interchangeable.

**D0.4.** $\varepsilon_q\in[0,1]$: threshold of A4; admissible range: CT0.8; sharp choice: $\varepsilon_q=0$.

**D0.5.** $\Phi$: phase alphabet of a real edge (CT0.9: $\Phi=\{0,\pi\}$); $\ \sigma_e:=e^{i\phi_e}=(-1)^{\phi_e/\pi}\in\{+1,-1\}$.

**D0.6.** hop $:=$ one traversal of one $e\in E_{\mathcal R}$; $\ \delta h(\gamma):=\#\{e\in\gamma\}$; $\ \mathfrak h:=$ length assigned to one hop.

**D0.7.** $\mathfrak L:=$ ordered record of retained events [A6, A7: stratification $\mathfrak L=\bigcup_{n\ge0}\mathfrak L(\tau_n)$, $|\mathfrak L(\tau_0)|=0$, monotone under ticks]; $\ \delta\tau:=$ ledger ticks (retained updates along real edges); $\ U\notin\mathfrak L$ [A5, A6].

**D0.8.** $n(v):=\partial^{\leftarrow}(v)+\partial^{\rightarrow}(v)$; $\ V_n:=\{v\in V:\ n(v)=n\}$ (vertex set); $\ \Xi_n:=\tau(V_n)=\{(a,b)\in\mathbb N^2:\ a+b=n\}$ (type set); “at rung $n$” $:=$ on $V_n$.

**D0.9.** $D_{\mathrm{tick}}(n):=\#\{$independent real registers a vertex of $V_n$ pushes across one pair channel per tick$\}$ — counted by the register accounting of **C10** (one orthogonal direction per admissible classical alternative: source availability, single-shot linear readout; $\neg$ Shannon $\log_2$ counting). $\ C_{\mathrm{cap}}:=\dim_{\mathbb R}\mathfrak H(\mathcal H_p\otimes\mathcal H_q)$ (register directions supplied by $1\mathfrak q$, A2); $\ O(n):=\max\bigl(0,\ D_{\mathrm{tick}}(n)-C_{\mathrm{cap}}\bigr)$.

**D0.10.** $\mathfrak C(\mathcal R):=$ configuration set on $E_{\mathcal R}$: finite oriented edge sets $E(C)\subseteq E_{\mathcal R}$ with sign assignments $\sigma$, seal data (D1.2) and vertex types (A7). $w(C)$ (A8) is defined on $\mathfrak C(\mathcal R)$; valid universes (D2.11) form a subset; $Z(\mathcal R):=\sum_{C\in\mathfrak C(\mathcal R)}\sum_\sigma w(C)$ (C12).

### Tier 1 — graph, chains, ledger dynamics

**D1.1.** $e=(p,q)\in\mathcal R_{\rightarrow}(p)\ \longmapsto\ (\mathcal G_n,\phi_e)$; $\ \mathcal G_n:=$ rung class of $q$; $\ \phi_e:$ D0.5; $\ \neg$registration $\implies e\in\mathcal V$. Reality principle of registration (C10): $\phi_e:=$ phase of the registration transport's action on the reality line $\wedge^2$ (1-dimensional, since $\dim\mathcal H_q=2$ [A1]); the transport preserves the $(S,T)$-grading [A3, A4] and the real Pauli-frame structure — registrations are classical data. On a minimal real edge ($\widehat{ds}^{\,2}=1$ [D1.6]) the geometric factor of the transfer weight $G(e)$ [D3.5] is the edge's alignment holonomy $e^{i\alpha_e}$ — the binary registration read of the A4 branch index at the seal ($\alpha_e=\alpha_{pq}$ for $e=(p,q)$ [A4]; per-edge determination read in **E**: Def-EM.20, EM.20, forward pointer).

**D1.2.** seal $:=$ transition of one pair across the A4 criterion (entry/exit of either branch): $\ J^+:\ n_{\mathcal R}:0\to1$ (crystallization); $\ J^-:\ n_{\mathcal R}:1\to0$ (dissolution).

**D1.3.** Janus-balanced $\iff\ \#J^+=\#J^-$.

**D1.4.** chain $c=(e_1,\dots,e_k)$: $e_i\in E_{\mathcal R}$, $\ t(e_i)=s(e_{i+1})$; $\ s(c):=s(e_1)$; $\ t(c):=t(e_k)$; $\ \partial c:=t(c)-s(c)$ (formal difference of vertices); closed $\iff\ \partial c=0\ \wedge\ \#J^+=\#J^-$.

**D1.5.** bound $:=$ closed self-contained chain (content: fermionic); transit $:=$ propagating open chain (content: bosonic); $\ \Delta S=\mathsf E_{\mathrm{bd}}+\mathsf E_{\mathrm{tr}}$; $\ \mathsf E_{\mathrm{bd}}:=\Delta S_{\mathrm{bound}}$; $\ \mathsf E_{\mathrm{tr}}:=\Delta S_{\mathrm{transit}}$.

**D1.6.** $ds^2(e):=g_{\mu\nu}(e)\,\Delta x^\mu_e\,\Delta x^\nu_e$ [$g_{\mu\nu}:$ D2.1]; $\ \widehat{ds}^{\,2}(e):=ds^2(e)/\mathfrak h^2$.

**D1.7.** $\Theta(\gamma):=\sum_{e\in\gamma}\widehat{ds}^{\,2}(e)$; $\ \Phi(\gamma):=\sum_{e\in\gamma}\alpha_e\,\widehat{ds}^{\,2}(e)$ [$\alpha_e\in\Phi:$ per-edge phase, D3.5; uniform-phase case: $\Phi=\alpha\,\Theta$]; $\ \operatorname{Hol}_{\mathrm{spiral}}(\gamma):=e^{i\Phi(\gamma)}$; $\ \gamma\in\mathsf{Trivial}\iff\forall e\in\gamma:\ \widehat{ds}^{\,2}(e)=0$; wrapping $\iff$ spatial hop projection has winding $\ne0$ around a closed ledger cycle.

**D1.8.** $\tau_n:=\sum\delta\tau$ accumulated along a causal chain of real edges; emergent coordinate $x^0:=\tau_n$.

**D1.9.** tick locality: $\ \operatorname{dom}\bigl(\mathrm{tick}(v)\bigr)\subseteq\{v\}\cup\{e\in E:\ e\ni v\}$, pre- and post-tick data only; $\neg\exists$ read at edge-distance $>1$.

**D1.10.** node force: $\ \mathbf F\!\restriction_v$ resolves local information content into channels {bound, transit, holonomy, charge, flux}; {bound, transit} $:=$ entropy channels [D1.5]; {holonomy, charge, flux} $:=$ registration data [D1.1] $\cup$ transition amplitude [D3.3].

**D1.11.** accessible information content at $v$ $\leftrightarrow n(v)$; content beyond the capacity bound (CT0.11): $\neg$accessible [D4.1].

**D1.12.** $\mathcal A(n):=\{$aspects of $\mathbf F$ acting nontrivially at rung $n\}$; value derived (CT0.13), $\neg$ stipulated.

### Tier 2 — masks, geometry, units

**D2.1.** sector coefficients [basis: CT1.2]: $\ X_{(+)}=a_{00}E_0+q_{ij}E^{ij}$, $q_{ij}=q_{ji}$; $\ X_{(-)}=w_iW_i$;
$$
\Sigma_{\mathrm{tr}}:=\delta^{ij}q_{ij};\quad
\hat h_{ij}:=q_{ij}-\tfrac13\delta_{ij}\Sigma_{\mathrm{tr}};\quad
h:=\tfrac13\Sigma_{\mathrm{tr}};\quad
N_i:=\beta w_i;\quad
\Omega:=e^{\alpha_\Omega a_{00}};\quad
\alpha_\Omega,\beta,\varkappa\in\mathbb R;
$$
$$
\bar g_{00}:=-1;\quad
\bar g_{0i}:=\varkappa N_i;\quad
\bar g_{ij}:=\delta_{ij}+\varkappa\bigl(\hat h_{ij}+\tfrac13\delta_{ij}\Sigma_{\mathrm{tr}}\bigr);\quad
g_{\mu\nu}:=\Omega^2\,\bar g_{\mu\nu}.
$$

**D2.2.** $\Upsilon:=\ln\Omega$; $\ \Upsilon_\mu:=\bar\nabla_\mu\Upsilon$.

**D2.3.** $\mathcal K:$ aspect space; $\ \mathcal K^{(A)}:$ block of aspect $A$; $\ \mathcal K_n:=\bigoplus_{A\in\mathcal A(n)}\mathcal K^{(A)}$; $\ \mathcal P_M^{(n)}:\mathcal K\to\mathcal K_n:$ orthogonal projection.

**D2.4.** $Z(\mathcal R,n):=\bigl\langle\mathrm{out}\bigl|(1-\mathbf F_M^{(n)})^{-1}\bigr|\mathrm{in}\bigr\rangle$; poles of $Z(\mathcal R,n):=$ rung-$n$ spectrum; residues $:=$ amplitudes.

**D2.5.** massless $\iff$ resolvent pole at $k^2=0$; massive $\iff$ pole at $k^2=m^2>0$; $m^2:=$ pole displacement.

**D2.6.** $\omega:$ orientation-reversal involution: $s(c)\leftrightarrow t(c)$; chirality $\mapsto-$chirality; charge $\mapsto-$charge.

**D2.7.** $\Theta_{\mathfrak L}:$ ledger reflection: reverses ledger order; $J^+\leftrightarrow J^-$; $G(e)\mapsto G(e)^\ast$.

**D2.8.** convergence sheet: $1\mapsto1+i\varepsilon$, $\ \varepsilon\to0^+$, for $\forall$ resolvents and configuration sums.

**D2.9.** units $:=$ powers of $\mathfrak q$; $\ c=\hbar=k_B=1$; $\ [\mathfrak h]=\mathfrak q^{-1/2}$; $\ \mathfrak h:=$ single free scale; $\ \kappa,\ G_N:$ names for combinations of $\mathfrak h$ (CT2.9), $\neg$ independent inputs.

**D2.10.** $\mathfrak M=\begin{pmatrix}B&Q\\ R&F\end{pmatrix}$: even blocks $B,F$; odd blocks $Q,R$; Hermitian $\iff B^\dagger=B\wedge F^\dagger=F\wedge R=Q^\dagger$; $\ \operatorname{Str}\mathfrak M:=\mathfrak T B-\mathfrak T F$; $\ [X,Y\}:=XY-(-1)^{|X||Y|}YX$ ($X,Y$ homogeneous).

**D2.11.** valid universe $\iff$ real-edge network closed $\ \wedge\ \#J^+=\#J^-$ [D1.3] $\ \wedge\ \in\operatorname{Im}($active mask$)$ $\ \wedge\ \neg\exists$ dangling ledger boundary beyond the sealed Janus boundary.

**D2.12.** Aspect realization (slot$\to$aspect bridge): $\iota_n:\mathfrak u(n)\to\mathcal K$ — linear realization of the rung-$n$ slot algebra in aspect space, with $\iota_n\bigl(Z(\mathfrak u(2))\bigr)$ spanning $\mathcal K^{(\mathrm{EM})}$ ($n=2$) and $\iota_n\bigl(\mathfrak{su}(3)\bigr)$ spanning $\mathcal K^{(\mathrm{strong})}$ ($n=3$), per the derivation of CT0.13. Slot algebras and pair algebras remain distinct objects (F header); D3.2 “already realized at rung $m$” $:=$ the abstract isomorphism class lies in $\iota_m(\mathfrak u(m))$ or in the pair blocks of CT0.12. **Realization domain:** exactly $n\le3$ — for $n\ge4$ no aspect realization exists [CT4.4a]; the silence of this definition at $n\ge4$ is a non-existence consequence, not an underdetermination.

**D2.13.** Subnetwork and microstate space *(scope clauses)*. $\Sigma\subseteq U$ [D2.11] $:=$ a finite connected vertex set together with its interior edges; $\partial\Sigma:=$ edges with exactly one endpoint in $\Sigma$. $\mathcal M(\Sigma):=$ valid microscopic configurations on $\Sigma$: restrictions $C|_\Sigma$ of valid ambient configurations $C$ [D2.11], carrying edge signs $\sigma_e$ [D0.5, CT0.9], geometric data $\widehat{ds}^{\,2}(e)$ [D1.6], seal data [D1.2] and vertex types [A7, D0.8] — subject to the rung masks [CT0.14, CT2.2] and Janus balance [D1.3], $\neg$ to colour sealing (sealing is ambient-global [CT3.18]; the completeness filter acts downstream: CT3.22a Rmk). $|\Sigma|:=\#\{\text{real edges touching}\ \Sigma\}$ (interior $+$ boundary).

**D2.14.** Colour boundary and the contraction-completeness projector. $\mathrm{Colour}(U):=\{u\in\mathcal Q:\ u\ \text{carries a colour attachment}\ [\mathrm{D3.8}]\}$; for valid $C$, $\pi_C(v)\subseteq\mathrm{Colour}(U):=$ the other members of the elementary invariant contraction group of $v$ under $C$ (one for a meson pair via $\delta^i{}_j$; two for a (anti)baryon triple via $\varepsilon_{ijk}/\varepsilon^{ijk}$ [CT3.17]); $\pi_C$ is total on $\mathrm{Colour}(U)$ for valid $C$ [CT3.18 $+$ D2.11 applied to the colour ledger]. For $\Sigma$ [D2.13]: $\mathrm{Colour}(\Sigma):=\mathrm{Colour}(U)\cap\Sigma$;
$$\partial_{\mathrm{col}}(\Sigma;C):=\{v\in\mathrm{Colour}(\Sigma):\ \pi_C(v)\not\subseteq\Sigma\};\qquad
\mathcal C(\Sigma;C):=\begin{cases}1&\partial_{\mathrm{col}}(\Sigma;C)=\varnothing\\ 0&\text{otherwise}\end{cases};\qquad
\Pi_{\mathcal C}(\Sigma;C):=\mathcal C(\Sigma;C)\cdot\mathbb I^{(\mathrm{strong})}_\Sigma$$
(Hermitian scalar idempotent on the colour slot space of $\Sigma$ [D3.1]; matches the mask pattern $\mathcal P_M^{(n)}$ [CT0.14]).

### Tier 3 — rung-2 and rung-3 structures

**D3.1.** $\mathcal H^{(n)}_{\mathrm{slot}}:=\operatorname{span}_{\mathbb C}\{|1\rangle,\dots,|n\rangle\}\cong\mathbb C^{n}$; $n=3$: slot index $i\in\{1,2,3\}$ $:=$ colour.

**D3.2.** subset principle: strictly new at rung $n$ $:=$ part of the rung-$n$ structure $\neg$realized at any $m<n$.

**D3.3.** at $v$ of type $(1,1)$, edge signs $\sigma_{\leftarrow}(v),\sigma_{\rightarrow}(v)$:
$$
f_v:=\frac{\sigma_{\rightarrow}(v)-\sigma_{\leftarrow}(v)}{2}\in\{-1,0,+1\};\qquad
\aleph_v:=|f_v|;\qquad
\aleph(\sigma,C):=\sum_{v\in C}\aleph_v .
$$

**D3.4.** $q_{\mathrm{EM}}(c):=\dfrac{\sigma_{s(c)}-\sigma_{t(c)}}{2}$ (oriented chain $c$). Closed chains: the basepoint core read $q_{\mathrm{core}}$ is defined, ternary, and charge-conjugation odd [EM.9a].

**D3.5.** $G^{(n)}(e):=\sigma_e\,\exp\!\bigl(i\,\alpha_e\,\widehat{ds}^{\,2}(e)\bigr)$ [D0.5, D1.6]; $\ \alpha_e\in\Phi:$ per-edge dynamic phase $=\alpha_{pq}$ for $e=(p,q)$ — the A4 branch index (read in Part 2 §E: Def-EM.20, EM.20, forward pointer); dimensionless; the same alphabet at every rung. $\ \alpha_{\mathrm{EM}}^{(n)}:$ EM-block spectral read at rung $n$ (EM.17, forward pointer).

**D3.6.** $\mathcal J(C):=\prod_{J^+\in C}(+1)\cdot\prod_{J^-\in C}(+1)^\ast$ $\ \implies\ \mathcal J(\Theta_{\mathfrak L}C)=\mathcal J(C)^\ast$.

**D3.7.** photon $:=$ trivial chain [D1.7] $\subseteq V_2$; $\ $gluon $:=$ trivial chain $\cap\,V_3\ne\varnothing$.

**D3.8.** colour triplet $q^i$: one fundamental slot index; colour antitriplet $r_i$: one dual slot index; quark $:=$ bound (fermionic) loop with a triplet attachment.

**D3.9.** baryon $B:=\varepsilon_{ijk}\,q^iq^jq^k$; $\ $meson $M:=\delta^i{}_j\,q^jr_i$. [Disambiguation: $M$ here $\ne$ total mask $M_\oplus$ of A9.]

**D3.10.** $W^\pm:=\tfrac1{\sqrt2}\bigl(W_1\mp iW_2\bigr)$; $\ Z:=\cos\theta_W\,W_3-\sin\theta_W\,Y$; $\ A:=\sin\theta_W\,W_3+\cos\theta_W\,Y$ [$\theta_W:$ EW.24].

### Tier 4 — saturation

**D4.1.** $F_{D^-}=\bigoplus_{n\ge4}F_n$ [A8]: single possibility space receiving $\forall$ configurations with rung $n\ge4$.

**D4.2.** $D^-$ absorbs information at rate $\propto O(n)$ [D0.9]; absorbed $\implies$ locked $:=$ retained in $\mathfrak L$, $\neg$accessible [D1.11].

**D4.3.** $F_{D^+}=\Lambda\,\mathbb I$ [A8]: uniform scalar aspect; $\neg$configuration-dependent.

---

## §D — Master symbol table

| Symbol | Meaning | Declared |
| --- | --- | --- |
| $\mathcal Q$, $q_n$ | qubit set; $n$-th qubit | A1 |
| $\mathcal H_q$ | carrier space of $q$, $\cong\mathbb C^2$ | A1 |
| $\rho_{pq}$ | state of ordered pair $(p,q)$ | A1 |
| $\mathfrak H(X)$ | real space of Hermitian operators on $X$ | A1 |
| $\mathfrak T(A)$ | trace of $A$ | A1 |
| $\succeq0$ | positive semidefinite | A1 |
| $C(p,q)$, $\mathfrak q$ | channel capacity of a pair; channel quantum | A2 |
| $\vee^2$, $\wedge^2$ | symmetric, antisymmetric square | A3 |
| $S$, $T$ | swap involution; sign-grading involution ($T=\mathsf D_\zeta\otimes\mathsf D_\zeta$; metric-sign reading: C13) | A3, CT1.0 |
| $\sigma_\mu$ | Pauli basis, $\mu\in\{0,1,2,3\}$, $\sigma_0=I_2$ | A3, C1 |
| $\mathbb1$, $I$ | identity operator; identity matrix | A3, A5 |
| $\eta$ | sign vector of the $T$-grading, $\eta\in\{\pm1\}^4$, one odd entry; representative $(-,+,+,+)$ | A3, C13 |
| $\mathfrak o$, $\eta^{(\mathfrak o)}$ | odd-sign slot of $\eta$; sign vector with a single $-1$ at slot $\mathfrak o$ | A3, CT1.0 |
| $\zeta_i$, $\mathsf D_\zeta$, $\mathrm{sf}$ | $\eta^0\eta^i$; Bloch sign map $\sigma_\mu\mapsto\zeta_\mu\sigma_\mu$; spin flip $X\mapsto\sigma_2X^{\mathrm T}\sigma_2$ | CT1.0 |
| $\mathcal R$, $\mathcal V$ | real (crystallized) set; virtual set | A4, D0.1 |
| $\Pi_{\mathcal V}$, $\Pi_{\mathcal R}$ | projections onto $\wedge^2$, $\vee^2$ | A4, CT0.7 |
| $\varepsilon_q$ | crystallization threshold | A4, D0.4 |
| $n_{\mathcal R}(p)$, $n_{\mathcal R}$ | real-edge count at $p$; global count | A4, D0.1 |
| $\rho_\circ$ | vacuum pair state $I/4$ | A5 |
| $U$, $\mu_\star$, $\dagger$ | Haar draw on $\mathrm{SU}(2)$; Haar measure; conjugate transpose | A5, A6 |
| $\mathfrak L$, $\mathfrak L(\tau_n)$, $n_{\mathrm{real\_out}}$ | ledger; ledger stratum at tick $\tau_n$; real-out count per tick | A5, A6, A7, D0.7 |
| $\mathcal T$, $\mathcal T^{-1}$ | tick map (Haar conjugation); its inverse | A6 |
| $\tilde{\mathcal T}_\gamma$, $\gamma$, $K$, $S_{\mathrm{raw}}$, $\mathbb V_\rho$ | $\varepsilon_q$-dependent Gibbs tilt; tilt strength $1-4\varepsilon_q$; surprisal; raw entropy; variance | D0.3 |
| $\tilde K$, $V(\tilde K)$ | centered surprisal; Lyapunov functional | D0.3, L1 |
| $\Gamma=(V,E)$ | directed graph | A7 |
| $\tau(v)$, $\partial^{\leftarrow}$, $\partial^{\rightarrow}$ | vertex type; in-degree; out-degree | A7 |
| $n(v)$, $V_n$, $\Xi_n$ | rung of $v$; rung-$n$ vertex set; type set | D0.8 |
| $E_{\mathcal R}$, $\phi_e$, $\sigma_e$, $\Phi$ | real edges; edge phase; edge sign; phase alphabet | A7, D0.5 |
| $\delta h$, $\mathfrak h$ | hop count; hop length | D0.6 |
| $\delta\tau$, $\tau_n$ | ledger tick count; ledger time | D0.7, D1.8 |
| $D_{\mathrm{tick}}(n)$, $C_{\mathrm{cap}}$, $O(n)$ | tick load; channel capacity; oversubscription | D0.9 |
| $\mathbf F$, $F_A$ | force operator; aspect $A$ | A8 |
| $F_{W^+}$, $F_{W^-}$, $F_Z$, $F_W$ | charged weak; neutral weak ($F_Z\equiv F_{W^3}$); weak block | A8, C8 |
| $F_{J^+}$, $F_{J^-}$ | crystallization; dissolution aspects | A8, D1.2 |
| $F_{\mathrm{EM}}$, $F_{\mathrm{strong}}$ | electromagnetic; colour aspects | A8 |
| $\Lambda$, $\mathbb I$ | stretch scalar; identity on force space | A8 |
| $\mathcal U_\odot$, $\mathfrak S$, $\mathbf F_\oplus$, $M_\oplus$ | observed universe; solution set; total force; total mask | A9 |
| $\mathfrak C(\mathcal R)$ | configuration set on $E_{\mathcal R}$; summation domain of $Z$ | D0.10, C12 |
| $\tilde{\mathcal T}_\gamma(X)$ | operator Gibbs tilt (functional calculus) | D0.3 |
| $\mathcal E_{st}$ | joint $(S,T)$ eigenspace | C3 |
| $f_{AB}{}^{C}$ | structure constants (Hermitian convention) | C2 |
| $\mathsf E_{\mathrm{bd}}$, $\mathsf E_{\mathrm{tr}}$ | bound, transit entropy | C6, D1.5 |
| $E_0$, $E^{ij}$, $W_i$, $J_i$, $K_i$ | generator basis of $\mathfrak H(\mathbb C^4)$ | CT1.2 |
| $\mathcal A(n)$ | active aspect set at rung $n$ | D1.12, CT0.13 |
| $\mathcal G_n$ | target rung class of an edge | D1.1 |
| $J^+$, $J^-$ | crystallization seal; dissolution seal | D1.2 |
| $c$, $\gamma$, $s(c)$, $t(c)$, $\partial c$ | chain; source; target; boundary | D1.4 |
| $ds^2(e)$, $\widehat{ds}^{\,2}(e)$ | discrete line element; hop-normalized | D1.6 |
| $\Theta(\gamma)$, $\Phi(\gamma)$, $\operatorname{Hol}_{\mathrm{spiral}}$, $\mathsf{Trivial}$ | spiral sum; phase; holonomy; trivial class | D1.7 |
| $x^0$ | emergent time coordinate | D1.8 |
| $\neg$, $\wedge$, $\vee$, $\implies$, $\iff$ | negation; conjunction; disjunction; implication; equivalence | — |
| $\oplus$, $\bigoplus$, $\otimes$ | direct sum; indexed direct sum; tensor product | A1, A3, A8 |
| $F_G$, $F_H$, $F_{D^+}$, $F_{D^-}$ | spin-2; scalar (Higgs); uniform dark; saturated dark | A8, D4.1, D4.3 |
| $P_M$, $\mathcal P_M^{(n)}$, $\mathbf F_M^{(n)}$ | mask projection; rung mask; masked force | A8, C7, D2.3 |
| $w(C)$, $\mathcal J(C)$, $G(e)$ | configuration weight; Janus factor; edge transfer weight | A8, D3.5, D3.6 |
| $f_v$, $\aleph_v$, $\aleph(\sigma,C)$ | vertex transition amplitude; indicator; count | D3.3 |
| $Z(\mathcal R)$, $Z(\mathcal R,n)$ | partition function; masked resolvent | A8, D2.4 |
| $\iota_n$ | aspect realization $\mathfrak u(n)\to\mathcal K$ (slot$\to$aspect bridge) | D2.12 |
| $\mathcal P^{(\mathrm{EM})}$, $Y_{\mathrm{asp}}$, $Y_{\mathrm{slot}}$, $Y_{\mathrm{car}}$ | EM block projection; the three realizations of $Y$ | EM.2, EW.8, D2.12 |
| $\varkappa$, $\kappa$, $G_N$ | embedding scale; gravitational coupling; Newton constant | C4, D2.1, D2.9, CT2.9 |
| $\Sigma$, $\Sigma_{\mathrm{tr}}$ | operator $\sum_i\sigma_i\otimes\sigma_i$; scalar $\delta^{ij}q_{ij}$ | C5, D2.1 |
| $a_{00}$, $q_{ij}$, $w_i$ | sector coefficients | D2.1 |
| $\hat h_{ij}$, $h$, $N_i$, $\Omega$, $\Upsilon$ | traceless shear; trace mode; shift; conformal factor; potential | D2.1, D2.2 |
| $\bar g_{\mu\nu}$, $g_{\mu\nu}$ | auxiliary metric; emergent metric | D2.1 |
| $\alpha_\Omega$, $\beta$ | metric embedding constants | D2.1 |
| $\mathcal K$, $\mathcal K^{(A)}$, $\mathcal K_n$ | aspect space; aspect block; rung-$n$ block | D2.3 |
| $m^2$ | mass squared (pole displacement) | D2.5 |
| $\omega$, $\Theta_{\mathfrak L}$ | orientation reversal; ledger reflection | D2.6, D2.7 |
| $\mathfrak M$, $\operatorname{Str}$, $[\cdot,\cdot\}$ | supermatrix; supertrace; graded bracket | D2.10 |
| $\mathcal H^{(n)}_{\mathrm{slot}}$ | slot space $\cong\mathbb C^n$ | D3.1 |
| $q_{\mathrm{EM}}(c)$ | chain end-charge | D3.4 |
| $\alpha_e$, $\alpha_{pq}$ | per-edge dynamic phase $\in\Phi$; branch phase of a crystallizing pair | A4, A7, D3.5 |
| $\alpha^{(n)}_{\mathrm{EM}}$ | EM-block spectral read at rung $n$ | EM.17 |
| $\mathcal P(\Sigma)$, $M(\mathcal P)$ | alignment pattern; mirror image of the pattern | Def-EM.21, Def-EM.22 |
| $q^i$, $r_i$ | colour triplet; antitriplet | D3.8 |
| $B$, $M$ | baryon; meson | D3.9 |
| $W^\pm$, $Z$, $A$, $Y$, $\theta_W$ | weak eigenstates; photon direction; hypercharge (realizations: EW.8); mixing angle | D3.10, EW.8, EW.24 |
| $T_a$, $f_{abc}$ | colour generators; colour structure constants | CT3.9, CT3.21 |
| $\varepsilon_{ijk}$, $\delta^i{}_j$ | colour invariant tensors | CT3.17 |
| $g$, $g'$, $e$, $h_0$ | weak, hypercharge, EM couplings; Higgs background | EW.33, P4 |
| $F_n$ | rung-$n$ saturation block, $n\ge4$ | A8, D4.1 |
| $\Sigma$, $\mathcal M(\Sigma)$, $C|_\Sigma$ | subnetwork, its microstate space, configuration restriction | D2.13 |
| $\partial_{\mathrm{col}}$, $\mathcal C(\Sigma;C)$, $\Pi_{\mathcal C}$ | colour boundary, contraction completeness, its projector | D2.14 |
| $\kappa_e$, $\Theta(c)$, $\bar\kappa$ | per-edge line-element quantum, loop total, mean quantum | CT1.29a |

---

## §E — Calibration policy

**P1.** $\forall$ quantities of the corpus: derived from A1–A9 $\wedge$ C1–C13 $\wedge$ D0.1–D4.3, except the hop length $\mathfrak h$; $[\mathfrak h]=\mathfrak q^{-1/2}$; $\mathfrak h$ fixes the absolute scale.

**P2.** Derived, zero freedom:
$$
(\dim\mathcal E_{++},\dim\mathcal E_{+-},\dim\mathcal E_{-+},\dim\mathcal E_{--})=(7,3,3,3);\quad
C_{\mathrm{cap}}=16;\quad
D_{\mathrm{tick}}(n)=2^{n+1};\quad
n_{\max}=3;
$$
$$
N_{\text{colour}}=3;\quad
N_{\text{gluon}}=8;\quad
N_{\gamma\text{-pol}}=2;\quad
q_{\mathrm{EM}}\in\{-1,0,+1\};\quad
\alpha_e\in\{0,\pi\}\ \text{per edge};
$$
$$
m_W=m_Z\cos\theta_W;\quad
e=g\sin\theta_W;\quad
S=n_{\mathcal R}\ln2;\quad
w_{D^+}=-1 .
$$

**Audit note.** Every entry of this list is re-verified from first principles in exact arithmetic: `checks/verify_merge_tierB.py` §F (totals and cross-references; the identity-level checks live in `verify_B.py`–`verify_G.py`).

**P3.** Named combinations of $\mathfrak h$ (external comparison only; $\neg$ inputs):
$$
G_N=\frac{\mathfrak h^2}{4\ln2};\qquad
\kappa^2=8\pi G_N=\frac{2\pi\,\mathfrak h^2}{\ln2}\qquad[\mathrm{CT2.9}].
$$

**P4.** Free internal configuration parameters ($\neg$ constants of the theory). Independent core: $g,\ g';\ h_0;\ c_W;\ \Lambda;\ \varkappa,\ \beta,\ \alpha_\Omega$. Functionally dependent members (properties of a solution, $\neg$ further freedom): $\theta_W(g,g')$ [EW.24]; $e(g,g')$ [EW.35]; $\mu_\star^2(c_W,\varkappa,\beta,h_0)$ [EW.33]; $m_W,\ m_Z$ [EW.20, EW.23]; $m_H$ [EW.27]. Predictions $:=$ dimensionless ratios among derived quantities at fixed core data.

**P5.** $\neg\exists$ quantity identified with a measured external constant. Comparison procedure: fix $\mathfrak h$ once; read P2 $\wedge$ P3; result $:=$ test of A9, $\neg$ input to A1–A8.
**Era-extension note.** The P4 core lists the bosonic-era free internal parameters (Part 2 loci). The fermion-era parameters (the Janus rate ratio $r=x_+/x_-$; the defect residues $\hat\mu^2$, $\hat\mu'^2$; the Ansatz-B formal temperature $\alpha$; the channel scales $\mu$, $\mu_\nu$; the formal fugacities) are registered in Part 3 §Cal-F under this policy; the baryomesonic era introduces none (Part 4 §Cal-BM).

---

## §F — Foundations: Bookkeeping, Pair Algebra, Ledger Dynamics

*Dep.: §A–§E of this part. Notation: as §A–§C. Machine: `checks/verify_B.py`, `checks/verify_L_lyapunov.py`, `checks/verify_L0_ledger_tilt.py`, `checks/verify_merge_tierB.py`, `checks/verify_promotion_B_rung.py`.*

## Tier 0 — Bookkeeping, Reality, and Capacity

### CT0.1 — Real/virtual dichotomy

**Thm.** $\ \forall(p,q)\in\mathcal Q\times\mathcal Q:\quad\bigl[(p,q)\in\mathcal R\bigr]\ \underline\vee\ \bigl[(p,q)\in\mathcal V\bigr].$

**Req.** A1, A3, A4; D0.1, D0.2, D0.4.

**Pf.**
$$
\bigl|\Pi_{\mathcal V}\rho_{pq}\bigr|=\mathfrak T\bigl(\Pi_{\mathcal V}\rho_{pq}\bigr)\in[0,1]\subset\mathbb R
\quad[\mathrm{D0.2},\ \mathrm{A1}:\ \rho_{pq}\succeq0\wedge\mathfrak T\rho_{pq}=1;\ \mathrm{A3}:\ \Pi_{\mathcal V}=\Pi_{\wedge^2}]
$$
$$
x\in\mathbb R\implies\bigl[(x\le\varepsilon_q\ \vee\ x\ge1-\varepsilon_q)\ \underline\vee\ (\varepsilon_q<x<1-\varepsilon_q)\bigr]\quad[\text{total order of }\mathbb R];\qquad \varepsilon_q\in[0,1]\subset\mathbb R\ [\mathrm{D0.4}]
$$
$$
\bigl[(p,q)\in\mathcal R\bigr]\iff\bigl[\bigl|\Pi_{\mathcal V}\rho_{pq}\bigr|\le\varepsilon_q\ \vee\ \bigl|\Pi_{\mathcal V}\rho_{pq}\bigr|\ge1-\varepsilon_q\bigr]\ [\mathrm{A4}];\qquad
\mathcal V=(\mathcal Q\times\mathcal Q)\setminus\mathcal R\ [\mathrm{D0.1}]
$$
$$
\Longrightarrow\quad\bigl[(p,q)\in\mathcal R\bigr]\ \underline\vee\ \bigl[(p,q)\in\mathcal V\bigr].\ \blacksquare
$$

**Phys.** Every qubit pair has exactly one status — crystallized (real) or uncrystallized (virtual) — decided by A4's two-branch threshold test on its antisymmetric weight. This dichotomy is the bookkeeping ground of the corpus: real pairs become edges of the emergent graph, virtual pairs remain vacuum.

---

### CT0.2 — Global vacuum

**Thm.** $\ n_{\mathcal R}=0\ \implies\ \forall(p,q):\ \bigl[(p,q)\in\mathcal V\ \wedge\ \rho_{pq}=\rho_\circ=\tfrac14 I\bigr]\ \wedge\ S_{\mathrm{raw}}(\rho_\circ)=\ln4=\max_{\rho}S_{\mathrm{raw}}(\rho),$ with $\arg\max=\{\tfrac14 I\}$.

**Req.** A1, A4, A5; D0.1, D0.3; CT0.1; Gibbs lemma: $\ S_{\mathrm{raw}}(\rho)\le\ln d$, $\ S_{\mathrm{raw}}(\rho)=\ln d\iff\rho=I/d$ [linear algebra].

**Pf.**
$$
n_{\mathcal R}=0\implies\neg\,\exists(p,q)\in\mathcal R\ [\mathrm{D0.1}]\implies\forall(p,q):\ (p,q)\in\mathcal V\ [\mathrm{CT0.1}]
$$
$$
\rho_{pq}=\rho_\circ=\tfrac14 I\quad[\mathrm{A5}]
$$
$$
S_{\mathrm{raw}}(\rho_\circ)=-\mathfrak T\bigl(\tfrac14 I\ln\tfrac14 I\bigr)=-4\cdot\tfrac14\ln\tfrac14=\ln4\quad[\mathrm{D0.3}]
$$
$$
\mathfrak H(\mathcal H_p\otimes\mathcal H_q)\cong\mathfrak H(\mathbb C^4),\ d=4:\quad S_{\mathrm{raw}}(\rho)\le\ln4,\quad S_{\mathrm{raw}}(\rho)=\ln4\iff\rho=\tfrac14 I\quad[\mathrm{A1},\ \text{Gibbs}].\ \blacksquare
$$

**Phys.** The empty configuration (no real edges) is all-virtual, with every pair at the maximally mixed state $I/4$ and entropy maximal at $\ln 4$: the vacuum of this theory is a state of maximal raw information. All structure — edges, particles, geometry — is a lowering of this entropy by crystallization.

---

### CT0.3 — Seal increments

**Thm.** $\ J^{+}:\ (\Delta n_{\mathcal R},\ \delta h,\ \delta\tau)=(+1,+1,+1);\qquad J^{-}:\ (\Delta n_{\mathcal R},\ \delta h,\ \delta\tau)=(-1,-1,-1).$

**Req.** A4, A7; D0.1, D0.6, D0.7, D1.2, D1.9.

**Pf.**
$$
J^\pm\ [\mathrm{D1.2}]:\ \ \exists!\,(p,q):\ \Delta\bigl[(p,q)\in\mathcal R\bigr]=\pm1\ [\mathrm{A4}]\implies\Delta n_{\mathcal R}=\pm1\ [\mathrm{D0.1}]
$$
$$
\Delta\bigl|E_{\mathcal R}\bigr|=\Delta n_{\mathcal R}\ [\mathrm{D0.1}]\implies\delta h=\pm1\ [\mathrm{D0.6}:\ \delta h=\#\{e\in E_{\mathcal R}\ \text{traversed}\}]
$$
$$
\text{seal}=\text{retained update along a real edge}\ [\mathrm{D0.7}]\implies\delta\tau=\pm1\ \text{(same sign)}
$$
$$
\mathrm{D1.9}:\ \operatorname{dom}(\mathrm{tick})\subseteq\{v\}\cup\{e\ni v\}\implies\Delta(\text{all further counters})=0.\ \blacksquare
$$

**Phys.** Crystallization ($J^+$) and dissolution ($J^-$) are the atomic ledger events: each adds or removes exactly one real edge, one traversal unit, and one tick of ledger time. Every extensive quantity of the corpus moves in integer steps of these events.

---

### CT0.4 — Real outgoing edge registration

**Thm.** $\ e=(p,q):\quad e\in\mathcal R_{\rightarrow}(p)\iff e\longmapsto(\mathcal G_n,\phi_e).$

**Req.** A7; D0.5, D0.8, D1.1; CT0.1.

**Pf.**
$$
(\Rightarrow):\ \ e\in E_{\mathcal R}\implies\exists\,\phi_e\ [\mathrm{A7}];\qquad q\in V_n\ \text{for}\ n=n(q)\ [\mathrm{D0.8}]\implies\exists\,\mathcal G_n;
$$
$$
\mathrm{D1.1}:\ \ e\longmapsto(\mathcal G_n,\phi_e).\qquad
(\Leftarrow):\ \ \mathrm{D1.1}:\ \neg\bigl[e\longmapsto(\mathcal G_n,\phi_e)\bigr]\implies e\in\mathcal V;
$$
$$
e\longmapsto(\mathcal G_n,\phi_e)\implies e\notin\mathcal V\implies e\in\mathcal R\quad[\mathrm{CT0.1}].\ \blacksquare
$$

**Phys.** “Real” and “registered in the ledger” are the same property of an edge: real edges are exactly those carrying ledger data (target rung class and phase); unregistered edges are virtual. Existence, in this corpus, is recordability.

---

### CT0.5 — Tick load at rung $n$

**Thm.** $\ D_{\mathrm{tick}}(n)=2^{\,n+1}.$

**Req.** A7; C10; D0.7, D0.8, D0.9, D1.9; CT0.9.

**Pf.**
$$
v\in V_n\implies\bigl|\{e\in E_{\mathcal R}:\ e\ni v\}\bigr|=n\quad[\mathrm{D0.8}]
$$
$$
\phi_e\in\Phi,\ |\Phi|=2\ [\mathrm{CT0.9}]\implies(\phi_e)_{e\ni v}\in\Phi^{\,n},\quad\bigl|\Phi^{\,n}\bigr|=2^n
$$
$$
\mathrm{D1.9}:\ \ \mathrm{tick\ datum}=(\mathrm{pre},\mathrm{post})\in\Phi^{\,n}\times\Phi^{\,n},\quad \mathrm{pre}\perp\mathrm{post}
$$
$$
\mathrm{C10}/\mathrm{D0.9}\ (\text{register accounting}):\ \ \text{registration of}\ X\ \text{at single-shot linear readout}=|X|\ \text{orthogonal register directions}
$$
$$
\text{Shannon content}=\log_2|X|=n\ \text{bits}\ \ne\ \text{register cost}\ 2^n\quad(\text{source availability}\ \ne\ \text{throughput})
$$
$$
\Longrightarrow\quad D_{\mathrm{tick}}(n)=2^n+2^n=2^{\,n+1}.\ \blacksquare
$$

**Phys.** A vertex with $n$ real edges must make $2^{n+1}$ classical alternatives linearly distinguishable per tick — $2^n$ pre-tick and $2^n$ post-tick phase configurations (C10 register accounting: one orthogonal direction per admissible value, not $\log_2$ bit encoding). This exponential growth of source availability is what caps accessible complexity at rung 3 (CT0.11).

---

### CT0.6 — Channel capacity and oversubscription

**Thm.**
$$
C_{\mathrm{cap}}=\dim_{\mathbb R}\mathfrak H(\mathbb C^4)=16;\qquad
O(n)=\max\bigl(0,\ 2^{\,n+1}-16\bigr);
$$
$$
O(0)=O(1)=O(2)=O(3)=0;\qquad O(4)=16;\qquad O(n)=2^{\,n+1}-16\quad(n\ge4).
$$

**Req.** A1, A2; D0.9; CT0.5; $\dim_{\mathbb R}\mathfrak H(\mathbb C^d)=d^2$ [linear algebra].

**Pf.**
$$
\mathcal H_p\otimes\mathcal H_q\cong\mathbb C^2\otimes\mathbb C^2\cong\mathbb C^4\ [\mathrm{A1}];\qquad
\dim_{\mathbb R}\mathfrak H(\mathbb C^d)=d^2\ [\text{linear algebra}]
$$
$$
C_{\mathrm{cap}}=\dim_{\mathbb R}\mathfrak H(\mathbb C^4)=4^2=16\ [\mathrm{D0.9}];\qquad C(p,q)=1\,\mathfrak q\ \ \forall(p,q)\ [\mathrm{A2}]
$$
$$
O(n)=\max\bigl(0,\ D_{\mathrm{tick}}(n)-C_{\mathrm{cap}}\bigr)=\max\bigl(0,\ 2^{\,n+1}-16\bigr)\quad[\mathrm{D0.9},\ \mathrm{CT0.5}]
$$
$$
2^{\,n+1}\le16\iff n\le3\implies O(n)=0\ \ (n\le3);\qquad
2^{5}-16=16\implies O(4)=16;\qquad
n\ge4\implies2^{\,n+1}\ge32>16\implies O(n)=2^{\,n+1}-16.\ \blacksquare
$$

**Phys.** One qubit–qubit channel carries exactly 16 real registers per tick — the dimension of the two-qubit Hermitian operator space. Rungs $0$–$3$ fit the budget, rung $3$ exactly saturates it, and rung $4$ doubles the demand to $32$, exceeding it by exactly one channel quantum. All finiteness of the accessible world starts here.


**Cor CT0.6a (transit-hop register bound).** Let $\gamma=(e_1,\dots,e_{\delta h})$ be a transit chain [D1.5, D1.4] of distinct directed real edges with hop count $\delta h(\gamma)$ [D0.6] whose entire edge-register content is registered through one pair channel over $\delta\tau(\gamma)$ ledger ticks [A2, D0.7]. Then:
$$
\mathsf E(\gamma)=\delta h(\gamma)\,\ln2\ \ \text{nats}\qquad(\delta h\ \ \text{independent binary registers}\ [\mathrm{CT0.9},\ \mathrm{C9}]);
$$
$$
\text{single-channel supply over}\ \delta\tau\ \text{ticks}:\ \log_2C_{\mathrm{cap}}\cdot\delta\tau=4\,\delta\tau\ \ \text{bits}\qquad[\mathrm{CT0.6}:\ C_{\mathrm{cap}}=16;\ \mathrm{C10}:\ 16\ \text{directions}\iff2^{4}\ \text{alternatives}]
$$
$$
\implies\quad\delta h(\gamma)\ \le\ 4\,\delta\tau(\gamma);\qquad
\mathsf E(\gamma)\ \le\ \min\bigl(\delta h(\gamma),\ 4\,\delta\tau(\gamma)\bigr)\,\ln2\ \ \text{nats}.
$$
A per-tick payload beyond $4$ hop-bits presents $2^{5}=32>16=C_{\mathrm{cap}}$ alternatives at the crossing — oversubscribed [CT0.6]; this is the payload counterpart of CT0.11's vertex-rung admissibility. The bound is sharp: for $\delta h\le4\,\delta\tau$ a schedule of $\delta\tau$ consecutive groups of $\le4$ hops presents $\le2^{4}=16=C_{\mathrm{cap}}$ alternatives per tick — at capacity, no oversubscription [CT0.6]. (Ledger accounting of registered content vs channel supply over a tick window [D0.7]; $\neg$a tick-to-tick transition law.)

**Req (Cor).** A2; C9, C10; D0.6, D0.7, D1.4, D1.5; CT0.6, CT0.9; exact binary capacity arithmetic [math; machine: `checks/verify_promotion_B_rung.py` §B].

**Pf (Cor).**
$$
\mathrm{CT0.9}:\ \sigma_e\in\{\pm1\}:\ 1\ \text{real edge}=1\ \text{bit}=\ln2\ \text{nats};\qquad\text{distinct edges}=\text{independent registers}\implies\mathsf E(\gamma)=\delta h\ln2\ [\mathrm{C9}]
$$
$$
\mathrm{CT0.6}:\ C_{\mathrm{cap}}=16\ \text{register directions per channel crossing};\qquad\mathrm{C10}:\ |X|\ \text{alternatives}\mapsto|X|\ \text{directions},\ \text{Shannon}\ \log_2|X|:\ 16\ \text{directions}\iff|X|\le16\iff\le4\ \text{bits per tick}
$$
$$
\delta\tau\ \text{ticks}:\ \text{supply}\le4\,\delta\tau\ \text{bits};\qquad\text{registered content}\le\text{supply}\implies\delta h\le4\,\delta\tau;\qquad\mathsf E\le\min(\delta h,\,4\,\delta\tau)\ln2
$$
$$
>4\ \text{bits in one tick}:\ 2^{5}=32>16=C_{\mathrm{cap}}:\ \text{oversubscribed}\ [\mathrm{CT0.6}];\qquad\text{groups of}\ \le4:\ 2^{4}=16=C_{\mathrm{cap}}:\ \text{at capacity}\ [\mathrm{CT0.6}]\ \blacksquare
$$


---

### CT0.7 — Reality is the swap grading

**Thm.** Let $\mathbb S\in\mathcal U(\mathcal H_p\otimes\mathcal H_q):\ |a\rangle\otimes|b\rangle\mapsto|b\rangle\otimes|a\rangle$. Then

$$(1)\quad \mathbb S=\tfrac12\bigl(E_0+\Sigma\bigr);\qquad
\Pi_{\mathcal R}:=\Pi_{\vee^2}=\tfrac14\bigl(3E_0+\Sigma\bigr);\qquad
\Pi_{\mathcal V}:=\Pi_{\wedge^2}=\tfrac14\bigl(E_0-\Sigma\bigr);\qquad
\mathfrak T\Pi_{\mathcal R}=3,\ \ \mathfrak T\Pi_{\mathcal V}=1 .
$$

$$(2)\quad \forall X:\ S(X)=\mathbb S X\mathbb S .
$$

$$(3)\quad SX=X\implies[\mathbb S,X]=0\implies X(\vee^2)\subseteq\vee^2\ \wedge\ X(\wedge^2)\subseteq\wedge^2;
$$
$$
SX=-X\implies\{\mathbb S,X\}=0\implies X(\vee^2)\subseteq\wedge^2\ \wedge\ X(\wedge^2)\subseteq\vee^2;
$$
$$
\underbrace{\dim_{\mathbb R}\mathfrak H(\vee^2)+\dim_{\mathbb R}\mathfrak H(\wedge^2)}_{9+1=10}\ \oplus\ \underbrace{2\dim_{\mathbb C}\operatorname{Hom}(\wedge^2,\vee^2)}_{2\cdot3=6}\ =\ 16 .
$$

$$(4)\quad \mathbf F_{(+,\mathcal R)}=\mathcal E_{++};\quad
\mathbf F_{(-,\mathcal R)}=\mathcal E_{+-};\quad
\mathbf F_{(+,\mathcal V)}=\mathcal E_{-+};\quad
\mathbf F_{(-,\mathcal V)}=\mathcal E_{--}
$$
(first label of $\mathbf F_{(\pm,\cdot)}$: $T$-parity; second label: $S$-parity, $\mathcal R\leftrightarrow+$, $\mathcal V\leftrightarrow-$); $\ F_{J^+}=\mathcal E_{-+}=\operatorname{span}\{J_i\}$, $\ F_{J^-}=\mathcal E_{--}=\operatorname{span}\{K_i\}$: the $S$-odd blocks.

**Req.** A3, A8; C3, C8; D1.2, D3.10; CT0.6, CT1.1, CT1.2.

**Pf.**
$$
(1)\ \ \mathbb S=\tfrac12\Bigl(I\otimes I+\textstyle\sum_i\sigma_i\otimes\sigma_i\Bigr)=\tfrac12\bigl(E_0+\Sigma\bigr)\quad[\mathrm{CT1.2}];
$$
basis check: $\ a=b:\ \tfrac12(1+1)|aa\rangle=|aa\rangle$; $\ a\ne b:\ \sum_i\sigma_i\otimes\sigma_i|ab\rangle=2|ba\rangle-|ab\rangle\implies\tfrac12(|ab\rangle+2|ba\rangle-|ab\rangle)=|ba\rangle$.
$$
\mathbb S^2=\mathbb1\ \wedge\ \mathbb S^\dagger=\mathbb S\implies\operatorname{spec}(\mathbb S)=\{\pm1\},\ \ \text{eigenspaces}\ \vee^2,\ \wedge^2\quad[\mathrm{A3}]
$$
$$
\Pi_{\mathcal R}=\mathbb1-\Pi_{\mathcal V}=\tfrac12(\mathbb1+\mathbb S)=\tfrac14\bigl(3E_0+\Sigma\bigr);\qquad
\Pi_{\mathcal V}=\tfrac12(\mathbb1-\mathbb S)=\tfrac14\bigl(E_0-\Sigma\bigr)\quad[\mathrm{A3},\mathrm{A4}]
$$
$$
\mathfrak T E_0=4,\ \mathfrak T\Sigma=0\implies\mathfrak T\Pi_{\mathcal R}=3=\dim\vee^2,\quad\mathfrak T\Pi_{\mathcal V}=1=\dim\wedge^2\quad[\mathrm{CT1.1}]
$$
$$
(2)\ \ \mathbb S(\sigma_\mu\otimes\sigma_\nu)\mathbb S=\sigma_\nu\otimes\sigma_\mu=S(\sigma_\mu\otimes\sigma_\nu)\ [\mathrm{A3}];\quad\text{linearity}\implies S(X)=\mathbb S X\mathbb S\ \ \forall X
$$
$$
(3)\ \ SX=X\Rightarrow\mathbb S X\mathbb S=X\Rightarrow\mathbb S X=X\mathbb S\ (\times\mathbb S\ \text{right});\qquad SX=-X\Rightarrow\mathbb S X=-X\mathbb S
$$
$$
X=X^\dagger\ \wedge\ [\mathbb S,X]=0\implies X\ \text{preserves each}\ \mathbb S\text{-eigenspace};\qquad
\{\mathbb S,X\}=0\implies X:\ \vee^2\leftrightarrow\wedge^2
$$
$$
\dim:\ \ \mathfrak H(\vee^2)\oplus\mathfrak H(\wedge^2)\cong\mathfrak H(\mathbb C^3)\oplus\mathfrak H(\mathbb C^1):\ 9+1=10;\qquad
\operatorname{Hom}(\wedge^2,\vee^2)\cong\mathbb C^{3}:\ 2\cdot3=6;\qquad 10+6=16\ [\mathrm{CT0.6}]
$$
$$
(4)\ \ S\text{-odd generators}=\{J_i\}\cup\{K_i\}\ (6)\ [\mathrm{CT1.2}];\quad S\text{-even}=\{E_0,\Sigma,\hat E^{ij},W_i\}\ (10)
$$
$$
\mathrm{D1.2}:\ \text{seal moves A4-weight }\wedge^2\!\leftrightarrow\!\vee^2\implies\text{seal generators}=S\text{-odd}\ [(3)]\implies F_{J^\pm}=S\text{-odd blocks}\ [\mathrm{A8}]
$$
$$
T\text{-parity}:\ J_i:+,\ K_i:-\ [\mathrm{CT1.2}]\implies F_{J^+}=\mathcal E_{-+},\ F_{J^-}=\mathcal E_{--}
$$
$$
\mathcal E_{++}\supseteq\{E_0,\Sigma,\hat E^{ij}\}\mapsto\{F_{D^+},F_H,F_G\};\qquad
\mathcal E_{+-}=\operatorname{span}\{W_i\}\mapsto\{F_{W^+},F_{W^-},F_Z\}\quad[\mathrm{A8},\ \mathrm{C8},\ \mathrm{D3.10}].\ \blacksquare
$$

**Cor CT0.7a (spin content).** $\ \sum_iW_i^2=\tfrac32E_0+\tfrac12\Sigma$; $\ \sum_iW_i^2\big|_{\vee^2}=2=1(1{+}1)$; $\ \sum_iW_i^2\big|_{\wedge^2}=0=0(0{+}1)$; i.e. $\vee^2$: spin $1$, $\wedge^2$: spin $0$.

**Req (Cor).** CT0.7, CT1.2.

**Pf (Cor).**
$$
\textstyle\sum_iW_i^2=\tfrac14\sum_i(\sigma_i\otimes\sigma_0+\sigma_0\otimes\sigma_i)^2=\tfrac14\bigl(3E_0+3E_0+2\Sigma\bigr)=\tfrac32E_0+\tfrac12\Sigma
$$
$$
\Sigma=2\mathbb S-E_0\ [\mathrm{CT0.7}(1)];\qquad
\vee^2:\ \mathbb S=+1\implies\Sigma=+1\implies\tfrac32+\tfrac12=2;\qquad
\wedge^2:\ \mathbb S=-1\implies\Sigma=-3\implies\tfrac32-\tfrac32=0.\ \blacksquare
$$

**Phys.** The real/virtual split of A4 *is* the exchange (swap) grading of the pair: real $=$ symmetric $=$ spin-1 triplet, virtual $=$ antisymmetric $=$ spin-0 singlet. The A8 force labels $(\pm,\mathcal R/\mathcal V)$ are precisely the two parities $(T,S)$; the Janus seals are exactly the operators that exchange the two grades, i.e. that create and destroy reality. “Existence” in this corpus is Bose exchange symmetry of a qubit pair.

---

### CT0.8 — Admissible range of the crystallization threshold

**Thm.** $\ \bigl[\mathrm{A4}\wedge\mathrm{A5}\wedge\mathrm{D0.1}\ \text{consistent}\bigr]\implies 0\le\varepsilon_q<\tfrac14;$ $\ \ $in particular $\varepsilon_q<1-\varepsilon_q$ (A4's two branches are disjoint); $\qquad\varepsilon_q=0\implies\bigl[(p,q)\in\mathcal R\iff\operatorname{supp}\rho_{pq}\subseteq\vee^2\ \ \vee\ \ \rho_{pq}=\Pi_{\mathcal V}\bigr]$ (branch reads $\alpha_{pq}=0\ /\ \pi$ [A4]); and $\forall$ theorems of the corpus: A4 enters only via CT0.1 (valid $\forall\varepsilon_q\in[0,1]$) and CT0.2 (valid $\iff\varepsilon_q\in[0,\tfrac14)$).

**Req.** A1, A4, A5; D0.1, D0.2, D0.4; CT0.2, CT0.7.

**Pf.**
$$
\bigl|\Pi_{\mathcal V}\rho_\circ\bigr|=\mathfrak T\bigl(\Pi_{\mathcal V}\cdot\tfrac14 I\bigr)=\tfrac14\,\mathfrak T\Pi_{\mathcal V}=\tfrac14\quad[\mathrm{A5},\ \mathrm{CT0.7}(1):\ \mathfrak T\Pi_{\mathcal V}=1]
$$
$$
\mathrm{D0.1}:\ \text{vacuum}\iff n_{\mathcal R}=0\implies\rho_\circ\notin\mathcal R\ [\mathrm{CT0.2}]\implies\tfrac14>\varepsilon_q\quad[\mathrm{A4}]
$$
$$
\varepsilon_q\ge0\ [\mathrm{D0.4}];\qquad\bigl|\Pi_{\mathcal V}\rho\bigr|\ge0\ [\mathrm{D0.2}]\implies\varepsilon_q=0\ \text{admissible}
$$
$$
\text{branch 2 at the vacuum}:\ \tfrac14\ge1-\varepsilon_q\iff\varepsilon_q\ge\tfrac34:\ \text{excluded by}\ \varepsilon_q<\tfrac14\implies\rho_\circ\ \text{virtual in both branches}
$$
$$
\text{branch disjointness}:\ 0\le\varepsilon_q<\tfrac14\implies\varepsilon_q<\tfrac12<1-\varepsilon_q\implies[0,\varepsilon_q]\cap[1-\varepsilon_q,1]=\varnothing
$$
$$
\varepsilon_q=0:\ \ \mathfrak T\bigl(\Pi_{\mathcal V}\rho_{pq}\bigr)=0\ \wedge\ \Pi_{\mathcal V}\succeq0\ \wedge\ \rho_{pq}\succeq0\iff\Pi_{\mathcal V}\rho_{pq}\Pi_{\mathcal V}=0\iff\operatorname{supp}\rho_{pq}\subseteq\vee^2\quad[\mathrm{A1}]
$$
$$
\varepsilon_q=0,\ \text{branch 2}:\ \ \mathfrak T\bigl(\Pi_{\mathcal V}\rho_{pq}\bigr)=1\ \wedge\ \mathfrak T\rho_{pq}=1\ \wedge\ \rho_{pq}\succeq0\ \wedge\ \operatorname{rk}\Pi_{\mathcal V}=1\ \ [\mathrm{CT0.7}(1)]\iff\rho_{pq}=\Pi_{\mathcal V}
$$
$$
\text{A4-dependence of all later tags}=\{\mathrm{CT0.1},\ \mathrm{CT0.2}\}\implies\text{range}\ [0,\tfrac14)\ \text{suffices; sharp point}\ \varepsilon_q=0.\ \blacksquare
$$

**Phys.** The crystallization threshold is not a free constant: demanding that the vacuum be all-virtual confines it to $0\le\varepsilon_q<\tfrac14$ — which simultaneously keeps A4's two branches disjoint ($\varepsilon_q<1-\varepsilon_q$). The sharp choice $\varepsilon_q=0$ says a pair is real exactly when its antisymmetric weight is exactly zero (aligned branch, $\alpha_{pq}=0$) or the pair is the pure singlet (antialigned branch, $\alpha_{pq}=\pi$). No result depends on where inside the range the tolerance sits — the theory is tolerance-independent.

---

### CT0.9 — The edge phase alphabet is binary

**Thm.** $\ \phi_e\in\Phi=\{0,\pi\}\ (\mathrm{mod}\ 2\pi);\qquad\sigma_e=e^{i\phi_e}=(-1)^{\phi_e/\pi}\in\{+1,-1\};\qquad 1\ \text{real edge}=1\ \text{bit}=\ln2\ \text{nats}.$

**Req.** A1, A3, A4, A7; C9, C10; D0.5, D1.1; $\dim\wedge^2=\binom{d}{2}$ [linear algebra].

**Pf.**
$$
e\in E_{\mathcal R}\mapsto\phi_e\ [\mathrm{A7}];\qquad
\mathrm{D1.1}:\ \phi_e:=\text{phase of the registration transport's action on the reality line}\ \wedge^2
$$
$$
\mathrm{A1}:\ \dim\mathcal H_q=d=2\implies\dim\wedge^2=\tbinom{2}{2}=1\quad(\text{the reality line is 1-dimensional}\iff\text{qubits are}\ \mathbb C^2)
$$
$$
\mathrm{A4}:\ \text{reality test}=\text{extremality of the}\ \wedge^2\ \text{weight (either branch)}\implies\text{registration transport preserves the}\ (S,T)\text{-grading}\ [\mathrm{A3},\ \mathrm{D1.1}]
$$
$$
\mathrm{D1.1}/\mathrm{C10}\ \text{reality principle}:\ \text{transport preserves the real frame structure}\implies\text{action on}\ \wedge^2_{\mathbb R}\ (1\text{-dim real line})=\text{multiplication by}\ c\in\mathbb R
$$
$$
\text{unitarity}\implies|c|=1\implies c\in\{+1,-1\}\implies e^{i\phi_e}\in\{\pm1\}\implies\phi_e\in\{0,\pi\}\ (\mathrm{mod}\ 2\pi);\qquad\sigma_e=(-1)^{\phi_e/\pi}\ [\mathrm{D0.5}]
$$
$$
|\Phi|=2\implies\log_2|\Phi|=1\ \text{bit}=\ln2\ \text{nats}\quad[\mathrm{C9}].\ \blacksquare
$$

**Rmk (repair).** The prior proof argued from the centralizer of $\{S,T\}$ alone — insufficient, since the complex centralizer of the swap is $U(3)\times U(1)$ and contains continuous phases. The binary alphabet follows once the reality principle of D1.1/C10 (registrations are real, grading-preserving frame data — quantum data classicalizes at registration) is explicit. The continuous counterexamples are complex-transport artifacts excluded by that principle.

**Phys.** The only internal datum a real edge can carry is a single sign — and this is *qubit-specific*: the reality line $\wedge^2$ is one-dimensional exactly because the carriers are $\mathbb C^2$ ($\dim\wedge^2=\binom d2=1\iff d=2$); for higher-dimensional carriers continuous grading-preserving phases would survive. Every edge of the emergent graph stores exactly one bit; all later charge and phase structure is built from these signs.

---

### CT0.10 — The two sign structures are independent

**Thm.** With $\ P(C):=\prod_{e\in E(C)}\sigma_e\ $ and $\ \pi(C):=(-1)^{\aleph(\sigma,C)}$ :
$$
\neg\bigl[P(C)\ \text{determines}\ \pi(C)\bigr]\ \wedge\ \neg\bigl[\pi(C)\ \text{determines}\ P(C)\bigr];\qquad
L\ge4:\ \ (P,\pi)\twoheadrightarrow\{\pm1\}^2;
$$
$$
\Longrightarrow\quad w(C)=\mathcal J(C)\prod_{e\in E(C)}G(e)\cdot(-1)^{\aleph(\sigma,C)}\ \ [\mathrm{A8}]\ \text{double-counts no edge-sign data}.
$$

**Req.** A8; D0.5, D3.3.

**Pf.**
$$
\aleph(\sigma,C)=\#\{i<L:\ \sigma_i\ne\sigma_{i+1}\}\quad[\mathrm{D3.3}]\ :\ \text{function of consecutive differences only};\qquad
P=\prod_{i}\sigma_i\ :\ \text{function of the signs}
$$
$$
\text{witness}_1\ [\pi\ \text{equal},\ P\ \text{opposite}]:\quad(+,-,+):\ \aleph=2,\ P=-1;\qquad(-,+,-):\ \aleph=2,\ P=+1
$$
$$
\text{witness}_2\ [P\ \text{equal},\ \pi\ \text{opposite}]:\quad(+,+,+,+):\ P=+1,\ \aleph=0;\qquad(+,+,-,-):\ P=+1,\ \aleph=1
$$
$$
\Longrightarrow\quad P\not\Rightarrow\pi\ \wedge\ \pi\not\Rightarrow P;\qquad
L\ge4:\ \{(P,\pi)\}=\{(+,+),(+,-),(-,+),(-,-)\}\ \text{attained}\implies(P,\pi)\ \text{surjective}
$$
$$
\Longrightarrow\quad\text{the two factors of}\ w(C)\ \text{carry independent information}.\ \blacksquare
$$

**Phys.** The product of edge signs and the transition parity measure different things — net sign content versus the number of domain walls between signs — and neither fixes the other. The A8 weight is therefore free of double counting: bulk sign and wall-count contribute independently to every configuration amplitude.

---

### CT0.11 — Maximal accessible rung

**Thm.** $\ \text{channel-admissible}(v)\iff D_{\mathrm{tick}}\bigl(n(v)\bigr)\le C_{\mathrm{cap}}\iff n(v)\le3;$ accessible vertex sets $=\{V_0,V_1,V_2,V_3\}$ (types $\{\Xi_0,\dots,\Xi_3\}$); $D_{\mathrm{tick}}(3)=C_{\mathrm{cap}}$ (saturation); $\forall v:\ n(v)\ge4\implies O\bigl(n(v)\bigr)>0\implies F_{D^-}$ [D4.1].

**Req.** D0.8, D0.9, D4.1; CT0.5, CT0.6.

**Pf.**
$$
\text{admissible}\iff D_{\mathrm{tick}}(n)\le C_{\mathrm{cap}}\quad[\mathrm{D0.9}]
$$
$$
2^{\,n+1}\le16\iff n+1\le4\iff n\le3\quad[\mathrm{CT0.5},\ \mathrm{CT0.6}]
$$
$$
n=3:\ \ 2^{4}=16=C_{\mathrm{cap}}\ (\text{tight});\qquad
n\ge4:\ \ O(n)>0\ [\mathrm{CT0.6}]\implies\text{configuration}\in F_{D^-}\ [\mathrm{D4.1}].\ \blacksquare
$$

**Cor CT0.11a (three slots).** $\ \max\{\mathcal H^{(n)}_{\mathrm{slot}}:\ \text{admissible}\}=\mathcal H^{(3)}_{\mathrm{slot}}\cong\mathbb C^3;\qquad 3=\lfloor\log_2 C_{\mathrm{cap}}\rfloor-1=\lfloor\log_216\rfloor-1;$ i.e. $N_{\text{colour}}=3$ is derived, not chosen.

**Req (Cor).** D3.1; CT0.6, CT0.11.

**Pf (Cor).** $\mathcal H^{(n)}_{\mathrm{slot}}\cong\mathbb C^n$ [D3.1]; $n\le3$ [CT0.11] $\Rightarrow\max=\mathbb C^3$; $\lfloor\log_2 16\rfloor-1=3$. $\blacksquare$


**Cor CT0.11b (directed rung of bidirectional skeletons).** A channel $\{p,q\}$, $p\ne q$, is *bidirectional* when both orientations are real: $(p,q)\in\mathcal R\ \wedge\ (q,p)\in\mathcal R$ [A4]. Let $S$ be a finite real-edge subgraph whose every used channel is bidirectional, and $d_S(v):=\#\{\text{channels of}\ S\ \text{incident on}\ v\}$. Then:
$$
n(v)\ \ge\ 2\,d_S(v)\qquad[\text{each bidirectional channel adds}\ 1\ \text{to}\ \partial^{\leftarrow}\ \text{and}\ 1\ \text{to}\ \partial^{\rightarrow}\ \text{at each endpoint}]
$$
$$
S\ \text{exhausts the real edges at}\ v\implies n(v)=2\,d_S(v);\qquad
d_S(v)\ge2\implies n(v)\ge4\implies D_{\mathrm{tick}}(n)=2^{n+1}\ge32>16\implies O\bigl(n(v)\bigr)>0\implies F_{D^-}\ [\mathrm{D4.1}]
$$
$$
\text{unoversubscribed}\iff n(v)\le3\ [\mathrm{CT0.6}]:\qquad\text{bidirectional}\ S:\ d_S(v)\le1\ (n\in\{0,2\});\qquad\text{mixed}:\ n(v)=2\,d^{\mathrm{bi}}_S(v)+d^{\mathrm{uni}}_S(v)\le3 .
$$

**Req (Cor).** A4; D0.8, D4.1; CT0.5, CT0.6, CT0.11; directed-degree enumeration [math; machine: `checks/verify_promotion_B_rung.py` §A].

**Pf (Cor).**
$$
\mathrm{A4}:\ \mathcal R\text{-membership per ordered pair};\quad\text{bidirectional channel}=\{e_{pq},e_{qp}\}\subseteq\mathcal R:\ \partial^{\leftarrow}\!+1,\ \partial^{\rightarrow}\!+1\ \text{at each endpoint}\implies n(v)\ge2\,d_S(v)\ [\mathrm{D0.8}]
$$
$$
\text{equality}\iff S\ \text{exhausts}\ v\text{'s incident real edges};\qquad d_S\ge2:\ n\ge4:\ \mathrm{CT0.5}:\ D_{\mathrm{tick}}(n)=2^{n+1}\ge32;\quad\mathrm{CT0.6}:\ O(n)=2^{n+1}-16>0
$$
$$
\mathrm{CT0.11}:\ n\ge4\implies F_{D^-}\ [\mathrm{D4.1}];\qquad O(n)=0\iff n\le3\ [\mathrm{CT0.6}];\qquad\text{mixed count}:\ \text{additivity of}\ \partial^{\leftarrow},\partial^{\rightarrow}\ [\mathrm{D0.8}]\ \blacksquare
$$


**Phys.** The 16-register channel budget admits vertices of degree at most three: rungs $0$–$3$ are accessible, rung $3$ exactly exhausts the channel, and everything of degree $\ge4$ is oversubscribed and falls to the dark sector. The number three — hence the threefold slot (“colour”) structure of the theory — is forced by capacity, not assumed.

**Note.** At rungs $n\ge4$ no aspect realization $\iota_n$ exists: the unique derived read of rung-$\ge4$ slot content is $D^-$-absorption at the ledger level [CT4.4a (Part 2) — forward pointer, non-load-bearing].

---

### CT0.12 — Aspect–capacity match

**Thm.**
$$
\begin{array}{c|c|c}
\text{aspect} & \text{block} & \dim_{\mathbb R}\\ \hline
F_{J^+} & \mathcal E_{-+}=\operatorname{span}\{J_i\} & 3\\
F_{J^-} & \mathcal E_{--}=\operatorname{span}\{K_i\} & 3\\
F_G & \operatorname{span}\{\hat E^{ij}\}\ (\text{traceless}) & 5\\
F_W & \mathcal E_{+-}=\operatorname{span}\{W_i\} & 3\\
F_H & \operatorname{span}\{\Sigma\} & 1\\
F_{D^+} & \operatorname{span}\{E_0\} & 1\\ \hline
\text{total} & \mathfrak H(\mathbb C^4) & 16=C_{\mathrm{cap}}
\end{array}
$$

**Req.** A8; C8; CT0.6, CT0.7(4), CT1.1, CT1.2.

**Pf.**
$$
\text{block assignments}\quad[\mathrm{CT1.2},\ \mathrm{CT0.7}(4)];\qquad
3+3+5+3+1+1=16=\dim_{\mathbb R}\mathfrak H(\mathbb C^4)\quad[\mathrm{CT1.1}]
$$
$$
16=C_{\mathrm{cap}}\quad[\mathrm{CT0.6}].\ \blacksquare
$$

**Rmk.** $\mathbf F_{\mathrm{st}}=F_{\mathrm{EM}}\oplus F_{\mathrm{strong}}\oplus F_{D^-}$ acts on vertex/slot registers [D3.1], not on the pair channel; the CT0.6 bound constrains the pair channel only.

**Phys.** The six pair-sector force aspects of A8 tile the 16 dimensions of the two-qubit operator space exactly: no part of the channel is forceless and no force overruns it. The stack aspects (electromagnetic, colour, dark-saturation) live on separate vertex registers and are not bounded by this count.

---

### CT0.13 — Aspect activation and the active sets

**Thm.**
$$
\mathcal A(0)=\{J\};\qquad
\mathcal A(1)=\{J,\,G,\,W,\,H,\,D^+\};\qquad
\mathcal A(2)=\mathcal A(1)\cup\{\mathrm{EM}\};
$$
$$
\mathcal A(3)=\mathcal A(2)\cup\{\mathrm{strong}\};\qquad
\mathcal A(n\ge4)=\mathcal A(3)\cup\{D^-\};
$$
with $J:=\{J^+,J^-\}$ and $W:=F_W=F_{W^+}\oplus F_{W^-}\oplus F_Z$ [C8]; $\ \neg\exists$ independent aspect named $Z$ at any rung: neutral seed $W_3\in F_W$; physical $Z$: D3.10, EW.24.

**Req.** A7, A8; C8; D0.8, D1.12, D2.12, D3.1, D3.2, D3.3, D4.1, D4.3; CT0.1, CT0.7, CT0.11, CT1.2, CT1.4, CT1.10; $\bigl[L^\dagger L=I_n\iff L\in U(n);\ \ \mathfrak u(n)=\mathfrak{su}(n)\oplus\mathfrak u(1)_{\mathrm{centre}}$ — linear algebra; cf. CT3.4, CT3.5$\bigr]$.

**Pf.**
$$
n=0:\ \ v\in V_0\implies\neg\,\exists e\in E_{\mathcal R}:\ e\ni v\ [\mathrm{D0.8}]\implies\forall\ \text{incident pairs}:\ \in\mathcal V\ [\mathrm{CT0.1}]
$$
$$
\mathrm{CT0.7}:\ \text{operators on the virtual block}=S\text{-odd}=\{F_{J^+},F_{J^-}\}\ [\mathrm{A8}]\implies\mathcal A(0)=\{J\}
$$
$$
n=1:\ \ \bigl|\{e\in E_{\mathcal R}:e\ni v\}\bigr|=1\implies\vee^2\ \text{populated};\qquad
\mathrm{CT0.7}:\ S\text{-even act within}\ \vee^2
$$
$$
\mathrm{CT1.2},\ \mathrm{CT1.10}:\ S\text{-even}=\{E_0,\ \Sigma,\ \hat E^{ij}_{(5)},\ W_i\}\xrightarrow[\mathrm{A8}]{}\{F_{D^+},\ F_H,\ F_G,\ F_W\}
$$
$$
\implies\mathcal A(1)=\{J,G,W,H,D^+\};\qquad
\dim F_W=3\ \text{single block}\implies W_3\ \neg\text{independent}\implies\neg\exists\ \text{aspect}\ Z
$$
$$
\text{slot algebras}:\ \ \mathcal H^{(n)}_{\mathrm{slot}}\cong\mathbb C^n\ [\mathrm{D3.1}];\quad
\text{probability-preserving}\iff L^\dagger L=I_n\iff L\in U(n)
$$
$$
X=\Bigl(X-\tfrac{\mathfrak T X}{n}I_n\Bigr)+\tfrac{\mathfrak T X}{n}I_n\ \text{(unique trace split)}\implies\mathfrak u(n)=\mathfrak{su}(n)\oplus\mathfrak u(1)_{\mathrm{centre}}\quad[\text{linear algebra; }n=3:\ \mathrm{CT3.4},\mathrm{CT3.5}]
$$
$$
n=1\ \text{slot}:\ \ \mathfrak u(1)\ \text{on one slot}=\text{global phase};\ \ \neg\exists\ \text{second slot}\implies\neg\text{configuration-dependent}\implies=F_{D^+}=\Lambda\mathbb I\ [\mathrm{D4.3}]\ \text{(counted)};\quad\neg\text{new}\ [\mathrm{D3.2}]
$$
$$
n=2:\ \ \mathfrak u(2)=\mathfrak{su}(2)\oplus\mathfrak u(1):\quad
\iota_2\bigl(\mathfrak{su}(2)\bigr)\cong\mathfrak{su}(2)\cong\operatorname{span}\{W_i\}\ [\mathrm{CT1.4}]:\ \text{same abstract class realized at rung}\ 1
$$
$$
\implies\neg\text{strictly new}\ [\mathrm{D2.12}\ (\iota_n\ \text{bridge}),\ \mathrm{D3.2}]
$$
$$
\text{centre measurable}:\ \ V_2\ni\text{type}(1,1)\ [\mathrm{A7}]\implies\text{relative in/out phase defined}=f_v\not\equiv0\ [\mathrm{D3.3}]\implies\text{strictly new}=F_{\mathrm{EM}}\ [\mathrm{A8}]
$$
$$
\implies\mathcal A(2)=\mathcal A(1)\cup\{\mathrm{EM}\};\qquad
f_v\ \text{requires}\ \partial^{\leftarrow}\!\ge1\ \wedge\ \partial^{\rightarrow}\!\ge1\implies n\ge2\ [\mathrm{D3.3},\mathrm{D0.8}]\implies\mathrm{EM}\notin\mathcal A(0)\cup\mathcal A(1)
$$
$$
n=3:\ \ \mathfrak u(3)=\mathfrak{su}(3)\oplus\mathfrak u(1):\quad
\mathfrak u(1)\ \text{duplicates}\ F_{\mathrm{EM}}\ (n=2)\implies\neg\text{new};\qquad
\mathfrak{su}(3)\ \text{strictly new}=F_{\mathrm{strong}}\ [\mathrm{A8}]
$$
$$
\implies\mathcal A(3)=\mathcal A(2)\cup\{\mathrm{strong}\}
$$
$$
n\ge4:\ \ \text{oversubscribed}\ [\mathrm{CT0.11}]\implies F_{D^-}\ \text{active there}\wedge\text{only there}\ [\mathrm{D4.1}];\qquad
\text{rung-3 structure persists}\implies\mathcal A(n\ge4)=\mathcal A(3)\cup\{D^-\}.\ \blacksquare
$$

**Phys.** Forces switch on one at a time as vertices acquire edges. Rung $0$ has only the Janus seals that create and destroy reality; rung $1$ lights up gravity ($G$), weak ($W$), Higgs ($H$) and uniform dark ($D^+$); at rung $2$ the local phase along a pass-through becomes measurable — electromagnetism; at rung $3$ the traceless three-slot algebra appears — colour; beyond, configurations lock into dark saturation ($D^-$). The gauge sequence of the corpus is channel bookkeeping, and no rung ever carries an independent $Z$ aspect — only the seed $W_3$ inside $F_W$.

---

### CT0.14 — Mask flag and block dimensions

**Thm.**
$$
\mathcal K_0\subset\mathcal K_1\subset\mathcal K_2\subset\mathcal K_3\subset\mathcal K_{n\ge4}\quad(\text{strict});\qquad
\dim\mathcal K_0=6,\ \ \dim\mathcal K_1=16,\ \ \dim\mathcal K_2=17,\ \ \dim\mathcal K_3=25;
$$
$$
\bigl(\mathcal P_M^{(n)}\bigr)^2=\mathcal P_M^{(n)}=\bigl(\mathcal P_M^{(n)}\bigr)^\dagger;\qquad
\mathfrak T\,\mathcal P_M^{(n)}=\dim\mathcal K_n;\qquad
\dim\mathcal K^{(\mathrm{EM})}=1,\ \ \dim\mathcal K^{(\mathrm{strong})}=8 .
$$

**Req.** A8; D2.3; CT0.12, CT0.13; CT3.8 (**F** — forward pointer: the block-dimension row re-verifies the gluon count).

**Pf.**
$$
\mathrm{CT0.13}:\ \ \mathcal A(0)\subset\mathcal A(1)\subset\mathcal A(2)\subset\mathcal A(3)\subset\mathcal A(n\ge4)\ \ (\text{strict})
$$
$$
\mathrm{D2.3}:\ \ \mathcal K_n=\bigoplus_{A\in\mathcal A(n)}\mathcal K^{(A)}\implies\mathcal K_0\subset\mathcal K_1\subset\mathcal K_2\subset\mathcal K_3\subset\mathcal K_{n\ge4}\ \ (\text{strict})
$$
$$
\dim\mathcal K_0=3+3=6\ [\mathrm{CT0.12}];\qquad
\dim\mathcal K_1=6+(5+3+1+1)=16\ [\mathrm{CT0.12}]
$$
$$
\dim\mathcal K^{(\mathrm{EM})}=\dim Z\bigl(\mathfrak u(2)\bigr)=1\ [\mathrm{CT0.13}\ \text{step}\ n{=}2:\ \text{centre spanned by}\ I_2]\implies\dim\mathcal K_2=17
$$
$$
\dim\mathcal K^{(\mathrm{strong})}=\dim\mathfrak{su}(3)=8\ [\mathrm{CT3.8}]\implies\dim\mathcal K_3=25
$$
$$
\mathrm{D2.3}:\ \mathcal P_M^{(n)}\ \text{orthogonal projection}\implies P^2=P=P^\dagger,\quad\mathfrak T P=\dim\operatorname{Im}P=\dim\mathcal K_n.\ \blacksquare
$$

**Rmk.** $\dim\mathcal K_1=16=C_{\mathrm{cap}}$: rung $1$ already exhausts the pair channel; growth at rungs $2,3$ is carried entirely by stack registers [CT0.12 Rmk].

**Phys.** The rung masks form a strict flag $6\subset16\subset17\subset25$: each new rung adds exactly the block of its new force — one dimension for electromagnetism at rung $2$, eight for colour at rung $3$. “What the universe can do at rung $n$” is literally a nested subspace of force space, and the masks are the orthogonal projections onto it.

---

## Tier 1A — The Pair Operator Algebra

### CT1.0 — Signature classification of the $T$-grading

**Thm.** Let $\eta\in\{\pm1\}^4$ have exactly one odd entry [A3]. Put $\eta^{(\mathfrak o)}:=(+,\dots,-_{\mathfrak o},\dots,+)$, $\zeta_i:=\eta^0\eta^i$, $\zeta_0:=1$, $\mathsf D_\zeta:\sigma_\mu\mapsto\zeta_\mu\sigma_\mu$, $\mathrm{sf}(X):=\sigma_2X^{\mathrm T}\sigma_2$. Then:

$(1)$ $\eta=\pm\eta^{(\mathfrak o)}$ for exactly one $\mathfrak o\in\{0,1,2,3\}$ and exactly one sign.

$(2)$ $T[\eta]=T[-\eta]$, and $T=\mathsf D_\zeta\otimes\mathsf D_\zeta$.

$(3)$ $[S,T]=0$ and $(\dim\mathcal E_{++},\dim\mathcal E_{+-},\dim\mathcal E_{-+},\dim\mathcal E_{--})=(7,3,3,3)$ for every $\mathfrak o$.

$(4)$ $\mathfrak o=0$: $T=\mathrm{sf}\otimes\mathrm{sf}$ (inversion of both Bloch vectors). $\mathfrak o=k\ge1$: $\mathsf D_\zeta$ reflects the Bloch axis $k$. The three maps $\mathfrak o\in\{1,2,3\}$ are conjugate under $\mathrm{Ad}_{U\otimes U}$, $U\in\mathrm{SU}(2)$; the map $\mathfrak o=0$ is conjugate to none of them.

$(5)$ $T\,\mathrm{Ad}_{U\otimes U}=\mathrm{Ad}_{U\otimes U}\,T$ for all $U\in\mathrm{SU}(2)$ $\iff\mathfrak o=0$.

**Req.** A3; C1; $[\text{math}]$: $\mathrm{Ad}_U$ fixes $\sigma_0$ and acts on $\operatorname{span}\{\sigma_i\}$ by $R(U)\in SO(3)$, every $R\in SO(3)$ arising; $\sigma_2U^{\mathrm T}\sigma_2=U^\dagger$ for $U\in\mathrm{SU}(2)$.

**Pf.**
$$
\text{(1)}:\ \text{odd entry}=-1\implies\eta=\eta^{(\mathfrak o)};\quad\text{odd entry}=+1\implies\eta=-\eta^{(\mathfrak o)};\quad\mathfrak o\ \text{is the unique odd slot}\quad[\mathrm{A3}]
$$
$$
\text{(2)}:\ \ \eta^\mu\eta^\nu=(-\eta^\mu)(-\eta^\nu)\implies T[\eta]=T[-\eta];\qquad
\zeta_\mu\zeta_\nu=(\eta^0\eta^\mu)(\eta^0\eta^\nu)=\eta^\mu\eta^\nu\ \ [(\eta^0)^2=1;\ \zeta_0=\eta^0\eta^0]
$$
$$
\implies(\mathsf D_\zeta\otimes\mathsf D_\zeta)(\sigma_\mu\otimes\sigma_\nu)=\zeta_\mu\zeta_\nu\,\sigma_\mu\otimes\sigma_\nu=T(\sigma_\mu\otimes\sigma_\nu)\ \Rightarrow\ T=\mathsf D_\zeta\otimes\mathsf D_\zeta
$$
$$
\text{(3)}:\ \ ST(\sigma_\mu\otimes\sigma_\nu)=\eta^\mu\eta^\nu\,\sigma_\nu\otimes\sigma_\mu=TS(\sigma_\mu\otimes\sigma_\nu)\implies[S,T]=0;\qquad
\sigma_\mu\otimes\sigma_\mu:\ (S,T)=(+,+);\quad
\sigma_\mu\otimes\sigma_\nu\pm\sigma_\nu\otimes\sigma_\mu\ (\mu<\nu):\ (S,T)=(\pm,\eta^\mu\eta^\nu)
$$
$$
n_-:=\#\{\mu<\nu:\eta^\mu\eta^\nu=-1\}=\#\bigl\{\{\mathfrak o,\nu\}:\nu\ne\mathfrak o\bigr\}=3;\qquad n_+=6-n_-=3
$$
$$
\dim\mathcal E_{++}=4+n_+=7,\quad\dim\mathcal E_{+-}=n_-=3,\quad\dim\mathcal E_{-+}=n_+=3,\quad\dim\mathcal E_{--}=n_-=3
$$
$$
\text{(4)}:\ \ \mathfrak o=0:\ \zeta_i=\eta^0\eta^i=-1\ \forall i;\qquad
\mathrm{sf}(\sigma_0)=\sigma_0,\ \ \mathrm{sf}(\sigma_i)=\sigma_2\sigma_i^{\mathrm T}\sigma_2=-\sigma_i\ (i=1,2,3)\implies\mathsf D_\zeta=\mathrm{sf}
$$
$$
\mathfrak o=k\ge1:\ \zeta_k=\eta^0\eta^k=-1,\ \ \zeta_i=+1\ (i\ne k)\implies\mathsf D_\zeta=\text{reflection of Bloch axis }k
$$
$$
\mathrm{Ad}_U\,\mathsf D_\zeta\,\mathrm{Ad}_U^{-1}=\mathsf D_{\zeta'}\ \text{with}\ \operatorname{diag}(\zeta')=R(U)\operatorname{diag}(\zeta)R(U)^{-1}\quad[\text{Req}]
$$
$$
\text{axis reflections}:\ R\ \text{permuting the axes}\implies T^{(1)}\sim T^{(2)}\sim T^{(3)};\qquad
\operatorname{spec}(-\mathbb1_3)=\{-1,-1,-1\}\ne\{-1,+1,+1\}\implies T^{(0)}\not\sim T^{(k)}
$$
$$
\text{(5)}\ (\Leftarrow):\ \ \mathrm{sf}(UXU^\dagger)=\sigma_2\bar UX^{\mathrm T}U^{\mathrm T}\sigma_2=U\,\sigma_2X^{\mathrm T}\sigma_2\,U^\dagger=U\,\mathrm{sf}(X)\,U^\dagger\quad[\sigma_2U^{\mathrm T}\sigma_2=U^\dagger\Rightarrow\sigma_2\bar U\sigma_2=U]
$$
$$
\implies\mathrm{sf}\otimes\mathrm{sf}\ \text{commutes with}\ \mathrm{Ad}_{U\otimes U};\qquad\text{(5)}\ (\Rightarrow):\ \ U_c:=\tfrac12\bigl(\mathbb1-i(\sigma_1+\sigma_2+\sigma_3)\bigr):\ \ \mathrm{Ad}_{U_c}:\ \sigma_1\mapsto\sigma_2\mapsto\sigma_3\mapsto\sigma_1
$$
$$
T\,\mathrm{Ad}_{U_c\otimes U_c}(\sigma_0\otimes\sigma_i)=\eta^0\eta^{i+1}\,\sigma_0\otimes\sigma_{i+1};\qquad
\mathrm{Ad}_{U_c\otimes U_c}\,T(\sigma_0\otimes\sigma_i)=\eta^0\eta^{i}\,\sigma_0\otimes\sigma_{i+1}\quad(i\bmod3)
$$
$$
\implies\eta^1=\eta^2=\eta^3\ \ [\eta^0=\pm1];\qquad\text{exactly one odd entry}\implies\mathfrak o=0.\ \blacksquare
$$

**Phys.** A3 now says only that the sign pattern is $1+3$. The overall sign is the mostly-plus / mostly-minus convention; which spatial slot is odd is a relabelling. What remains is one selection: the odd slot is the identity slot, which is the unique choice making $T$ rotation-covariant, namely the spin flip $\mathrm{sf}\otimes\mathrm{sf}$ (time reversal on the pair). Any other slot gives a reflection that singles out a spatial direction.

**Rmk (what $\mathfrak o\ge1$ would do).** The sector dimensions $(7,3,3,3)$ do not change, but CT1.2's table does. For $\mathfrak o=1$: $W_2,W_3\in\mathcal E_{++}$ (not $\mathcal E_{+-}$); $J_2,J_3\in\mathcal E_{--}$ and $K_2,K_3\in\mathcal E_{-+}$ (swapped); $E^{12},E^{13}\in\mathcal E_{+-}$ (not $\mathcal E_{++}$). Only $W_1,J_1,K_1$ sit where CT1.2 puts them. Symmetric statements hold for $\mathfrak o=2,3$. (Numerical check over all four $\mathfrak o$ on the 16-element basis; machine: `checks/verify_CT10_signature.py`.) So the selection $\mathfrak o=0$ in C13 is load-bearing for CT1.2 and everything built on the $W_i$ triplet, not cosmetic.

### CT1.1 — Joint $(S,T)$ decomposition of $\mathfrak H(\mathbb C^4)$

**Thm.** $\ [S,T]=0;$ $\qquad\mathfrak H(\mathbb C^4)=\mathcal E_{++}\oplus\mathcal E_{+-}\oplus\mathcal E_{-+}\oplus\mathcal E_{--};$ $\qquad(\dim\mathcal E_{++},\dim\mathcal E_{+-},\dim\mathcal E_{-+},\dim\mathcal E_{--})=(7,3,3,3);\qquad7+3+3+3=16.$

**Req.** A3, C13; C3; CT1.0; Pauli basis facts: $\ \mathfrak T(\sigma_\mu\sigma_\alpha)=2\delta_{\mu\alpha}$, $\sigma_\mu^\dagger=\sigma_\mu$ [linear algebra].

**Pf.**
$$
\bigl\{\sigma_\mu\otimes\sigma_\nu\bigr\}_{\mu,\nu=0}^{3}\subset\mathfrak H(\mathbb C^4);\qquad
\mathfrak T\bigl((\sigma_\mu\otimes\sigma_\nu)(\sigma_\alpha\otimes\sigma_\beta)\bigr)=4\,\delta_{\mu\alpha}\delta_{\nu\beta}
$$
$$
\Longrightarrow\ \text{orthogonal}\implies\text{basis};\qquad\dim_{\mathbb R}\mathfrak H(\mathbb C^4)=16
$$
$$
\mathrm{A3}:\ \ S:\ \sigma_\mu\otimes\sigma_\nu\mapsto\sigma_\nu\otimes\sigma_\mu\ (\text{permutation});\qquad
T:\ \sigma_\mu\otimes\sigma_\nu\mapsto\eta^\mu\eta^\nu\,\sigma_\mu\otimes\sigma_\nu,\ \ \eta^\mu\eta^\nu\in\{\pm1\}
$$
$$
\implies S^2=T^2=\mathbb1,\ \ \operatorname{spec}\subseteq\{\pm1\};\qquad
ST(\sigma_\mu\otimes\sigma_\nu)=\eta^\mu\eta^\nu\,\sigma_\nu\otimes\sigma_\mu=TS(\sigma_\mu\otimes\sigma_\nu)\implies[S,T]=0
$$
$$
[S,T]=0\ \wedge\ S^2=T^2=\mathbb1\implies\text{simultaneous eigenspaces}\ \mathcal E_{st}\ \text{span}\ \mathfrak H(\mathbb C^4)\quad[\mathrm{C3}]
$$
$$
\eta:=(-,+,+,+)\ [\mathrm{C13}]:\quad T=+1\iff(\mu,\nu)\in\{0,0\}\cup\{i,j\};\qquad T=-1\iff(\mu,\nu)\in\{0,i\}\cup\{i,0\}
$$
$$
\mathcal E_{++}:\ \{\sigma_\mu\otimes\sigma_\mu\}_{\mu=0}^{3}\ (4)\ \cup\ \{\sigma_i\otimes\sigma_j+\sigma_j\otimes\sigma_i\}_{i<j}\ (3)=7
$$
$$
\mathcal E_{+-}:\ \{\sigma_0\otimes\sigma_i+\sigma_i\otimes\sigma_0\}_{i=1}^{3}=3;\qquad
\mathcal E_{-+}:\ \{\sigma_i\otimes\sigma_j-\sigma_j\otimes\sigma_i\}_{i<j}=3
$$
$$
\mathcal E_{--}:\ \{\sigma_0\otimes\sigma_i-\sigma_i\otimes\sigma_0\}_{i=1}^{3}=3;\qquad
7+3+3+3=16\implies\mathfrak H(\mathbb C^4)=\bigoplus_{s,t}\mathcal E_{st}.\ \blacksquare
$$

**Phys.** The 16-dimensional space of two-qubit observables splits under exchange symmetry ($S$) and the sign grading $T$ ($\eta^\mu\eta^\nu$; metric-sign reading by C13) into blocks $7+3+3+3$. This grading is the skeleton of the whole force structure: the $7$-block supplies gravity, Higgs and uniform dark; the $3$-blocks supply weak, Janus-seal, and the remaining virtual sector.

---

### CT1.2 — Generator basis and sector assignment

**Thm.** Define
$$
E_0:=\sigma_0\otimes\sigma_0;\qquad
\Sigma:=\textstyle\sum_{i=1}^{3}\sigma_i\otimes\sigma_i;\qquad
W_i:=\tfrac12\bigl(\sigma_0\otimes\sigma_i+\sigma_i\otimes\sigma_0\bigr);
$$
$$
J_i:=\tfrac12\bigl(\sigma_j\otimes\sigma_k-\sigma_k\otimes\sigma_j\bigr)\ [(i,j,k)\ \text{cyclic}];\qquad
K_i:=\tfrac12\bigl(\sigma_0\otimes\sigma_i-\sigma_i\otimes\sigma_0\bigr);\qquad
E^{ij}:=\tfrac12\bigl(\sigma_i\otimes\sigma_j+\sigma_j\otimes\sigma_i\bigr).
$$
Then
$$
\begin{array}{c|c|c|c|c}
\text{generator} & \# & S & T & \text{sector}\\ \hline
E_0 & 1 & + & + & \mathcal E_{++}\\
\Sigma & 1 & + & + & \mathcal E_{++}\\
\hat E^{ij}\ (\text{traceless}) & 5 & + & + & \mathcal E_{++}\\
W_i & 3 & + & - & \mathcal E_{+-}\\
J_i & 3 & - & + & \mathcal E_{-+}\\
K_i & 3 & - & - & \mathcal E_{--}
\end{array}
\qquad 1+1+5+3+3+3=16\implies\text{basis of}\ \mathfrak H(\mathbb C^4);
$$
$$
W_i=\tfrac12\bigl(\sigma_i^{(p)}+\sigma_i^{(q)}\bigr)=\text{total-spin generator}.
$$

**Req.** A3, C1, C3, C13; CT1.0, CT1.1.

**Pf.**
$$
S E_0=E_0;\ \ \eta^0\eta^0=+1\implies E_0\in\mathcal E_{++}\quad[\mathrm{A3}]
$$
$$
S E^{ij}=E^{ij}\ (\text{by construction});\ \ \eta^i\eta^j=+1\ [\mathrm{C13}]\implies E^{ij}\in\mathcal E_{++};\qquad\#\{E^{ij}\}_{i\le j}=6
$$
$$
\delta_{ij}E^{ij}=\textstyle\sum_iE^{ii}=\Sigma\ (1\ \text{component})\ \oplus\ \hat E^{ij}\ (5);\qquad S,T\ \text{diagonal on index pairs}\implies\text{both}\subseteq\mathcal E_{++}
$$
$$
W_i:\ S=+;\ \ \eta^0\eta^i=-1\ [\mathrm{C13}]\implies T=-\implies W_i\in\mathcal E_{+-}
$$
$$
J_i:\ S=-;\ \ \eta^j\eta^k=+1\ [\mathrm{C13}]\implies T=+\implies J_i\in\mathcal E_{-+}
$$
$$
K_i:\ S=-;\ \ \eta^0\eta^i=-1\ [\mathrm{C13}]\implies T=-\implies K_i\in\mathcal E_{--}
$$
$$
\text{counts}\ (1,1,5,3,3,3)\ \text{match}\ (7{=}1{+}1{+}5,\ 3,\ 3,\ 3)\ [\mathrm{CT1.1}];\qquad
\text{distinct orthogonal combinations}\implies\text{independent}\implies\text{basis}
$$
$$
\sigma_0\otimes\sigma_i\equiv\sigma_i^{(p)},\ \ \sigma_i\otimes\sigma_0\equiv\sigma_i^{(q)}\implies W_i=\tfrac12\bigl(\sigma_i^{(p)}+\sigma_i^{(q)}\bigr).\ \blacksquare
$$

**Phys.** This fixes the named basis used throughout the corpus: identity $E_0$, exchange scalar $\Sigma$, total spin $W_i$ (weak sector), the antisymmetric spatial and temporal generators $J_i,K_i$ (Janus/seal sectors), and the symmetric spatial tensors $E^{ij}$ (gravity). Each generator’s $(S,T)$ parity decides which force aspect of A8 it belongs to.

---

### CT1.3 — Centrality of the identity

**Thm.** $\ \forall X\in\mathfrak H(\mathbb C^4):\quad[E_0,X]=0.$

**Req.** C1; CT1.2.

**Pf.**
$$
E_0=\sigma_0\otimes\sigma_0=I_2\otimes I_2=I_4\quad[\mathrm{C1},\ \mathrm{CT1.2}];\qquad
[I_4,X]=I_4X-XI_4=0.\ \blacksquare
$$

**Phys.** The identity direction commutes with everything, so the aspect it carries — the uniform dark term $F_{D^+}=\Lambda\mathbb I$ — acts identically on every configuration: a cosmological-constant-type force.

---

### CT1.4 — The $W_i$ close $\mathfrak{su}(2)$

**Thm.** $\ [W_i,W_j]=i\,\epsilon_{ijk}W_k;\qquad\operatorname{span}_{\mathbb R}\{W_i\}\cong\mathfrak{su}(2)\ [\mathrm{C2}].$

**Req.** C2; CT1.2; $\ [\sigma_i,\sigma_j]=2i\,\epsilon_{ijk}\sigma_k$ [Pauli algebra].

**Pf.**
$$
\text{definitions cyclically symmetric}\implies\text{suffices}:\ [W_1,W_2]=iW_3
$$
$$
[W_1,W_2]=\tfrac14\bigl[\sigma_0\otimes\sigma_1+\sigma_1\otimes\sigma_0,\ \ \sigma_0\otimes\sigma_2+\sigma_2\otimes\sigma_0\bigr]\quad[\mathrm{CT1.2}]
$$
$$
[\sigma_0\otimes\sigma_1,\ \sigma_0\otimes\sigma_2]=\sigma_0^2\otimes[\sigma_1,\sigma_2]=2i\,(\sigma_0\otimes\sigma_3)
$$
$$
[\sigma_0\otimes\sigma_1,\ \sigma_2\otimes\sigma_0]=\sigma_2\otimes\sigma_1-\sigma_2\otimes\sigma_1=0;\qquad
[\sigma_1\otimes\sigma_0,\ \sigma_0\otimes\sigma_2]=0\quad[\text{distinct factors}]
$$
$$
[\sigma_1\otimes\sigma_0,\ \sigma_2\otimes\sigma_0]=[\sigma_1,\sigma_2]\otimes\sigma_0^2=2i\,(\sigma_3\otimes\sigma_0)
$$
$$
[W_1,W_2]=\tfrac14\bigl(2i\,\sigma_0\otimes\sigma_3+2i\,\sigma_3\otimes\sigma_0\bigr)=\tfrac i2\bigl(\sigma_0\otimes\sigma_3+\sigma_3\otimes\sigma_0\bigr)=iW_3.\ \blacksquare
$$

**Phys.** The three symmetric mixed generators close a perfect $\mathfrak{su}(2)$: they are the total spin of the qubit pair. This $\mathfrak{su}(2)$ becomes the weak-isospin gauge algebra of the corpus — the weak force is the pair’s rotation algebra, not an added postulate.

---

### CT1.5 — Commutators of $\Sigma$ with $J_i$, $K_i$, $W_i$

**Thm.** $\ [\Sigma,J_i]=4i\,K_i;\qquad[\Sigma,K_i]=-4i\,J_i;\qquad[\Sigma,W_i]=0.$

**Req.** CT0.7(1),(3) $\ [\Sigma=2\mathbb S-E_0;\ \ S\text{-even}\Rightarrow[\mathbb S,\cdot]=0]$, CT1.2, CT1.3; Pauli algebra.

**Pf.**
$$
\text{cyclicity}\implies\text{suffices}:\ i=1
$$
$$
[\sigma_1\otimes\sigma_1,\ J_1]=0:\quad[\sigma_1\otimes\sigma_1,\ \sigma_2\otimes\sigma_3]=(i\sigma_3)\otimes(-i\sigma_2)-(-i\sigma_3)\otimes(i\sigma_2)=0;\quad\text{likewise}\ \sigma_3\otimes\sigma_2
$$
$$
[\sigma_2\otimes\sigma_2,\ \sigma_2\otimes\sigma_3]=\sigma_0\otimes[\sigma_2,\sigma_3]=2i\,(\sigma_0\otimes\sigma_1);\qquad
[\sigma_2\otimes\sigma_2,\ \sigma_3\otimes\sigma_2]=2i\,(\sigma_1\otimes\sigma_0)
$$
$$
\implies[\sigma_2\otimes\sigma_2,\ J_1]=\tfrac12\bigl(2i\,\sigma_0\otimes\sigma_1-2i\,\sigma_1\otimes\sigma_0\bigr)=2i\,K_1
$$
$$
[\sigma_3\otimes\sigma_3,\ \sigma_2\otimes\sigma_3]=-2i\,(\sigma_1\otimes\sigma_0);\qquad
[\sigma_3\otimes\sigma_3,\ \sigma_3\otimes\sigma_2]=-2i\,(\sigma_0\otimes\sigma_1)\implies[\sigma_3\otimes\sigma_3,\ J_1]=2i\,K_1
$$
$$
[\Sigma,J_1]=0+2iK_1+2iK_1=4i\,K_1
$$
$$
[\sigma_1\otimes\sigma_1,\ K_1]=0\ (\text{as above});\qquad
[\sigma_2\otimes\sigma_2,\ \sigma_0\otimes\sigma_1]=-2i\,(\sigma_2\otimes\sigma_3);\qquad
[\sigma_2\otimes\sigma_2,\ \sigma_1\otimes\sigma_0]=-2i\,(\sigma_3\otimes\sigma_2)
$$
$$
\implies[\sigma_2\otimes\sigma_2,\ K_1]=\tfrac12\bigl(-2i\,\sigma_2\otimes\sigma_3+2i\,\sigma_3\otimes\sigma_2\bigr)=-2i\,J_1
$$
$$
[\sigma_3\otimes\sigma_3,\ \sigma_0\otimes\sigma_1]=2i\,(\sigma_3\otimes\sigma_2);\qquad
[\sigma_3\otimes\sigma_3,\ \sigma_1\otimes\sigma_0]=2i\,(\sigma_2\otimes\sigma_3)\implies[\sigma_3\otimes\sigma_3,\ K_1]=-2i\,J_1
$$
$$
[\Sigma,K_1]=-4i\,J_1
$$
$$
\Sigma=2\mathbb S-E_0\ [\mathrm{CT0.7}(1)];\qquad
SW_i=W_i\ (S\text{-even})\implies[\mathbb S,W_i]=0\ [\mathrm{CT0.7}(3)];\qquad
[E_0,W_i]=0\ [\mathrm{CT1.3}]
$$
$$
\implies[\Sigma,W_i]=2[\mathbb S,W_i]-[E_0,W_i]=0.\ \blacksquare
$$

**Phys.** The exchange scalar $\Sigma$ rotates the two seal sectors into one another ($J\leftrightarrow K$, a $90^\circ$ rotation inside the virtual sector) while leaving total spin untouched. The volume/trace mode therefore couples to Janus (edge creation–annihilation) dynamics but not to spin.

---

### CT1.6 — Commutators $[J_i,J_j]$ and $[K_i,K_j]$

**Thm.** $\ [J_i,J_j]=i\,\epsilon_{ijk}W_k;\qquad[K_i,K_j]=i\,\epsilon_{ijk}W_k.$

**Req.** CT1.2; Pauli algebra.

**Pf.**
$$
\text{suffices}:\ [J_1,J_2]=iW_3=[K_1,K_2]
$$
$$
[J_1,J_2]=\tfrac14\bigl[\sigma_2\otimes\sigma_3-\sigma_3\otimes\sigma_2,\ \ \sigma_3\otimes\sigma_1-\sigma_1\otimes\sigma_3\bigr]
$$
$$
[\sigma_2\otimes\sigma_3,\ \sigma_3\otimes\sigma_1]=(i\sigma_1)\otimes(i\sigma_2)-(-i\sigma_1)\otimes(-i\sigma_2)=0
$$
$$
[\sigma_2\otimes\sigma_3,\ -\sigma_1\otimes\sigma_3]=-[\sigma_2,\sigma_1]\otimes\sigma_3^2=2i\,(\sigma_3\otimes\sigma_0)
$$
$$
[-\sigma_3\otimes\sigma_2,\ \sigma_3\otimes\sigma_1]=-\sigma_0\otimes[\sigma_2,\sigma_1]=2i\,(\sigma_0\otimes\sigma_3)
$$
$$
[-\sigma_3\otimes\sigma_2,\ -\sigma_1\otimes\sigma_3]=(i\sigma_2)\otimes(i\sigma_1)-(-i\sigma_2)\otimes(-i\sigma_1)=0
$$
$$
\implies[J_1,J_2]=\tfrac14\bigl(2i\,\sigma_3\otimes\sigma_0+2i\,\sigma_0\otimes\sigma_3\bigr)=iW_3
$$
$$
[K_1,K_2]:\ \ \text{cross terms}=0\ [\text{distinct factors}];\qquad
[K_1,K_2]=\tfrac14\Bigl([\sigma_0\otimes\sigma_1,\sigma_0\otimes\sigma_2]+[\sigma_1\otimes\sigma_0,\sigma_2\otimes\sigma_0]\Bigr)
$$
$$
=\tfrac14\bigl(2i\,\sigma_0\otimes\sigma_3+2i\,\sigma_3\otimes\sigma_0\bigr)=iW_3.\ \blacksquare
$$

**Phys.** Neither seal sector closes on itself: brackets of two $J$’s or two $K$’s land in the total-spin (weak) sector. Reality-flipping operations source the rotational/weak structure of the pair — the first algebraic link between the Janus dynamics and gauge structure.

---

### CT1.7 — Mixed commutators $[J_i,K_j]$

**Thm.**
$$
[J_i,K_j]=i\bigl(\delta_{ij}\Sigma-E^{ij}\bigr)=\tfrac i2\Bigl(2\delta_{ij}\Sigma-\sigma_i\otimes\sigma_j-\sigma_j\otimes\sigma_i\Bigr);
$$
$$
[J_i,K_i]=i\!\!\sum_{k\ne i}\!\!\sigma_k\otimes\sigma_k;\qquad
[J_i,K_j]=-iE^{ij}=-\tfrac i2\bigl(\sigma_i\otimes\sigma_j+\sigma_j\otimes\sigma_i\bigr)\ \ (i\ne j);
$$
$$
[J_i,K_j]\in(\mathcal E_{++})_{\mathrm{sym\ spatial}};\qquad [J_i,K_j]\notin\operatorname{span}\{W_k\}.
$$

**Req.** CT1.1, CT1.2; $\epsilon$-identities: $\ \epsilon_{iab}\epsilon_{bjm}=\delta_{ij}\delta_{am}-\delta_{im}\delta_{aj}$, $\ \epsilon_{iab}\epsilon_{ajm}=\delta_{bj}\delta_{im}-\delta_{bm}\delta_{ij}$.

**Pf.**
$$
J_i=\tfrac12\,\epsilon_{iab}\,\sigma_a\otimes\sigma_b\ (a,b\in\{1,2,3\})\quad[\mathrm{CT1.2}];\qquad
K_j=\tfrac12\bigl(\sigma_0\otimes\sigma_j-\sigma_j\otimes\sigma_0\bigr)
$$
$$
[\sigma_a\otimes\sigma_b,\ \sigma_0\otimes\sigma_j]=\sigma_a\otimes[\sigma_b,\sigma_j]=2i\,\epsilon_{bjm}\,\sigma_a\otimes\sigma_m
$$
$$
[\sigma_a\otimes\sigma_b,\ \sigma_j\otimes\sigma_0]=[\sigma_a,\sigma_j]\otimes\sigma_b=2i\,\epsilon_{ajm}\,\sigma_m\otimes\sigma_b
$$
$$
\implies[J_i,K_j]=\tfrac i2\,\epsilon_{iab}\bigl(\epsilon_{bjm}\,\sigma_a\otimes\sigma_m-\epsilon_{ajm}\,\sigma_m\otimes\sigma_b\bigr)
$$
$$
\epsilon_{iab}\epsilon_{bjm}\,\sigma_a\otimes\sigma_m=\delta_{ij}\Sigma-\sigma_j\otimes\sigma_i;\qquad
\epsilon_{iab}\epsilon_{ajm}\,\sigma_m\otimes\sigma_b=\sigma_i\otimes\sigma_j-\delta_{ij}\Sigma
$$
$$
[J_i,K_j]=\tfrac i2\Bigl(\delta_{ij}\Sigma-\sigma_j\otimes\sigma_i-\sigma_i\otimes\sigma_j+\delta_{ij}\Sigma\Bigr)=\tfrac i2\bigl(2\delta_{ij}\Sigma-\sigma_i\otimes\sigma_j-\sigma_j\otimes\sigma_i\bigr)=i\bigl(\delta_{ij}\Sigma-E^{ij}\bigr)
$$
$$
i=j:\ \ i\bigl(\Sigma-\sigma_i\otimes\sigma_i\bigr)=i\!\!\sum_{k\ne i}\!\!\sigma_k\otimes\sigma_k;\qquad
i\ne j:\ \ \delta_{ij}=0\implies-iE^{ij}
$$
$$
\Sigma,\ E^{ij}\in\mathcal E_{++};\ \ W_k\in\mathcal E_{+-};\ \ \text{direct sum}\ [\mathrm{CT1.1},\ \mathrm{CT1.2}]\implies[J_i,K_j]\notin\operatorname{span}\{W_k\}.\ \blacksquare
$$

**Phys.** Bracketing a spatial seal with a temporal seal produces symmetric spatial — metric-type — data, never weak data. Mixed virtual processes feed the gravitational sector: the algebraic seed of “quantum fluctuations sourcing geometry.”

---

### CT1.8 — Action of $W_i$ on $J_j$ and $K_j$

**Thm.** $\ [W_i,J_j]=i\,\epsilon_{ijk}J_k;\qquad[W_i,K_j]=i\,\epsilon_{ijk}K_k;$ i.e. $\{J_i\}$, $\{K_i\}$: $SO(3)$ vectors under $\operatorname{span}\{W_i\}$.

**Req.** CT1.2; Pauli algebra.

**Pf.**
$$
\text{suffices}:\ [W_3,J_1]=iJ_2,\quad[W_3,K_1]=iK_2
$$
$$
[W_3,J_1]=\tfrac14\bigl[\sigma_0\otimes\sigma_3+\sigma_3\otimes\sigma_0,\ \ \sigma_2\otimes\sigma_3-\sigma_3\otimes\sigma_2\bigr]
$$
$$
[\sigma_0\otimes\sigma_3,\ \sigma_2\otimes\sigma_3]=\sigma_2\otimes[\sigma_3,\sigma_3]=0;\qquad
[\sigma_0\otimes\sigma_3,\ -\sigma_3\otimes\sigma_2]=-\sigma_3\otimes[\sigma_3,\sigma_2]=2i\,(\sigma_3\otimes\sigma_1)
$$
$$
[\sigma_3\otimes\sigma_0,\ \sigma_2\otimes\sigma_3]=[\sigma_3,\sigma_2]\otimes\sigma_3=-2i\,(\sigma_1\otimes\sigma_3);\qquad
[\sigma_3\otimes\sigma_0,\ -\sigma_3\otimes\sigma_2]=0
$$
$$
\implies[W_3,J_1]=\tfrac i2\bigl(\sigma_3\otimes\sigma_1-\sigma_1\otimes\sigma_3\bigr)=iJ_2
$$
$$
[W_3,K_1]=\tfrac14\bigl[\sigma_0\otimes\sigma_3+\sigma_3\otimes\sigma_0,\ \ \sigma_0\otimes\sigma_1-\sigma_1\otimes\sigma_0\bigr]
$$
$$
[\sigma_0\otimes\sigma_3,\ \sigma_0\otimes\sigma_1]=2i\,(\sigma_0\otimes\sigma_2);\qquad
[\sigma_0\otimes\sigma_3,\ -\sigma_1\otimes\sigma_0]=0=[\sigma_3\otimes\sigma_0,\ \sigma_0\otimes\sigma_1]
$$
$$
[\sigma_3\otimes\sigma_0,\ -\sigma_1\otimes\sigma_0]=-[\sigma_3,\sigma_1]\otimes\sigma_0=-2i\,(\sigma_2\otimes\sigma_0)
$$
$$
\implies[W_3,K_1]=\tfrac14\bigl(2i\,\sigma_0\otimes\sigma_2-2i\,\sigma_2\otimes\sigma_0\bigr)=iK_2;\qquad
\text{cyclicity}\implies\text{general form}.\ \blacksquare
$$

**Phys.** Total spin rotates both virtual sectors as vectors: the seal generators carry spin $1$ under the weak $\mathfrak{su}(2)$. The reality/virtuality bookkeeping is rotation-covariant — angular momentum is built into the ledger before any dynamics is introduced.

---

### CT1.9 — Sector closure table and the global algebra

**Thm.**
$$
\begin{array}{c|c}
\text{bracket} & \text{closes in}\\ \hline
[W_i,W_j] & \operatorname{span}\{W_k\}=\mathcal E_{+-}\\
[W_i,J_j] & \operatorname{span}\{J_k\}=\mathcal E_{-+}\\
[W_i,K_j] & \operatorname{span}\{K_k\}=\mathcal E_{--}\\
[J_i,J_j] & \operatorname{span}\{W_k\}\\
[K_i,K_j] & \operatorname{span}\{W_k\}\\
[J_i,K_j] & (\mathcal E_{++})_{\mathrm{sym\ spatial}}\\
[\Sigma,J_i] & \operatorname{span}\{K_i\}\\
[\Sigma,K_i] & \operatorname{span}\{J_i\}\\
[\Sigma,W_i] & 0\\
[E_0,X] & 0\ \ \forall X
\end{array}
$$
$$
\bigl(\mathfrak H(\mathbb C^4),\ (X,Y)\mapsto-i[X,Y]\bigr)\cong\mathfrak u(4)\ [\mathrm{C2}];\qquad
Z\bigl(\mathfrak u(4)\bigr)=\operatorname{span}_{\mathbb R}\{E_0\};
$$
$$
\mathfrak{su}(4)=\operatorname{span}_{\mathbb R}\bigl\{\Sigma,\ \hat E^{ij},\ W_i,\ J_i,\ K_i\bigr\};\qquad
\dim_{\mathbb R}\mathfrak{su}(4)=1+5+3+3+3=15 .
$$

**Req.** C2; CT1.1–CT1.8; $\ \mathfrak T(\sigma_\mu\otimes\sigma_\nu)=4\,\delta_{\mu0}\delta_{\nu0}$.

**Pf.**
$$
\text{rows }1\text{–}5:\ [\mathrm{CT1.4},\ \mathrm{CT1.8},\ \mathrm{CT1.6}];\qquad
\text{row }6:\ [\mathrm{CT1.7}];\qquad
\text{rows }7\text{–}9:\ [\mathrm{CT1.5}];\qquad
\text{row }10:\ [\mathrm{CT1.3}]
$$
$$
\text{sector labels}:\ [\mathrm{CT1.2}]
$$
$$
X,Y\in\mathfrak H(\mathbb C^4)\implies(-i[X,Y])^\dagger=-i[X,Y];\qquad
\text{bilinear}\ \wedge\ \text{antisymmetric}\ \wedge\ \text{Jacobi}\ [\text{associative commutator}]
$$
$$
\dim_{\mathbb R}\mathfrak H(\mathbb C^4)=16\ [\mathrm{CT1.1}]\implies\bigl(\mathfrak H(\mathbb C^4),-i[\cdot,\cdot]\bigr)=\mathfrak u(4)\quad[\mathrm{C2}]
$$
$$
X\in Z\iff[X,Y]=0\ \ \forall Y\in\mathfrak H(\mathbb C^4)\implies X\ \text{scalar}\implies Z=\operatorname{span}_{\mathbb R}\{E_0\}\quad[\mathrm{CT1.3}]
$$
$$
\mathfrak T(\sigma_\mu\otimes\sigma_\nu)=4\,\delta_{\mu0}\delta_{\nu0}\implies E_0\ \text{alone has trace}\implies\text{traceless complement}=\mathfrak{su}(4),\ \dim=16-1=15
$$
$$
\mathfrak{su}(4)=\operatorname{span}_{\mathbb R}\{\Sigma,\hat E^{ij},W_i,J_i,K_i\}:\quad1+5+3+3+3=15.\ \blacksquare
$$

**Phys.** The full commutator structure closes: the $16$ pair observables form $\mathfrak u(4)=\mathfrak u(1)\oplus\mathfrak{su}(4)$, with the central $\mathfrak u(1)$ ($E_0$) as the uniform dark aspect and the $15$ traceless directions carrying gravity ($5$), weak ($3$), the two seal sectors ($3{+}3$) and the exchange scalar ($1$). Every force algebra later in the corpus is a subalgebra of this one $16$-dimensional algebra.

---

### CT1.10 — $SO(3)$ decomposition of $\mathcal E_{++}$

**Thm.** Under $\operatorname{span}\{W_i\}$:
$$
\mathcal E_{++}\ \longrightarrow\ \mathbf 1\oplus\mathbf 5\oplus\mathbf 1\qquad(7=1+5+1);
$$
$$
E_0:\ \mathbf 1;\qquad\Sigma:\ \mathbf 1;\qquad
\hat E^{ij}:=E^{ij}-\tfrac13\delta^{ij}\Sigma:\ \mathbf 5\ (\text{spin }2),\quad\delta_{ij}\hat E^{ij}=0 .
$$

**Req.** CT1.1, CT1.3, CT1.5, CT1.8; symmetric traceless rank-$2$ tensor $=\ell=2$ representation [$SO(3)$ representation theory].

**Pf.**
$$
\dim\mathcal E_{++}=7\quad[\mathrm{CT1.1}]
$$
$$
[E_0,W_i]=0\ [\mathrm{CT1.3}];\ \ E_0\ \text{index-free}\implies E_0:\ \mathbf 1
$$
$$
E^{ij}=\underbrace{\tfrac13\delta^{ij}\Sigma}_{\text{trace}}+\underbrace{\hat E^{ij}}_{\text{traceless}}\ \ (\text{unique split});\qquad
\delta_{ij}\hat E^{ij}=\Sigma-\tfrac13\cdot3\cdot\Sigma=0
$$
$$
[\Sigma,W_i]=0\ [\mathrm{CT1.5}]\implies\Sigma:\ \mathbf 1
$$
$$
[W_a,\sigma_i\otimes\sigma_j]=i\,\epsilon_{aik}\,\sigma_k\otimes\sigma_j+i\,\epsilon_{ajk}\,\sigma_i\otimes\sigma_k\quad[\mathrm{CT1.2},\ \text{Pauli algebra}]
$$
$$
\implies[W_a,E^{ij}]=i\bigl(\epsilon_{aik}E^{kj}+\epsilon_{ajk}E^{ik}\bigr);\qquad
[W_a,\hat E^{ij}]=[W_a,E^{ij}]-\tfrac13\delta^{ij}\underbrace{[W_a,\Sigma]}_{=0\ [\mathrm{CT1.5}]}=i\bigl(\epsilon_{aik}\hat E^{kj}+\epsilon_{ajk}\hat E^{ik}\bigr)
$$
$$
\implies\hat E^{ij}:\ \text{traceless symmetric rank-}2\ \text{tensor}=\ell=2:\ \mathbf 5\quad[SO(3)\ \text{representation theory}]
$$
$$
1+1+5=7=\dim\mathcal E_{++}\implies\mathcal E_{++}=\mathbf 1\oplus\mathbf 5\oplus\mathbf 1.\ \blacksquare
$$

**Phys.** Seen by rotations, the real sector contains exactly two scalars and one five-component spin-$2$ object. The spin-$2$ quintet is the graviton field of the corpus; with the three $W_i$ as shift, the $(7,3)$ real blocks supply the ten components of a Lorentzian metric (CT1.12): conformal ($1$) $+$ traceless metric ($5$) $+$ volume ($1$) $+$ shift ($3$).

---

### CT1.11 — The two scalars are distinct

**Thm.** $\ E_0\in Z\bigl(\mathfrak H(\mathbb C^4)\bigr);\qquad\Sigma\notin Z\bigl(\mathfrak H(\mathbb C^4)\bigr);\qquad\forall c\in\mathbb R\setminus\{0\}:\ E_0\ne c\,\Sigma;$ hence the A8 assignment $E_0\mapsto F_{D^+}$, $\Sigma\mapsto F_H$ [CT0.12] is well-defined and non-degenerate.

**Req.** A8; CT0.12, CT1.3, CT1.5.

**Pf.**
$$
[E_0,X]=0\ \ \forall X\implies E_0\in Z\quad[\mathrm{CT1.3}]
$$
$$
[\Sigma,J_1]=4i\,K_1\ne0\ \ (K_1\ne0)\implies\Sigma\notin Z\quad[\mathrm{CT1.5}]
$$
$$
c\ne0:\ \ X\in Z\iff cX\in Z\implies\bigl[E_0\in Z\ \wedge\ \Sigma\notin Z\bigr]\implies E_0\ne c\,\Sigma\ \ \forall c\ne0
$$
$$
\implies E_0,\ \Sigma:\ \text{independent directions of}\ \mathcal E_{++};\qquad
E_0\mapsto F_{D^+}=\Lambda\,\mathbb I,\ \ \Sigma\mapsto F_H\quad[\mathrm{A8},\ \mathrm{CT0.12}].\ \blacksquare
$$

**Phys.** The two rotation scalars are provably different objects: $E_0$ is central — it cannot distinguish configurations — and supplies the uniform dark aspect $\Lambda\mathbb I$; $\Sigma$ is non-central — it couples to the seals and to geometry — and supplies the scalar (Higgs-type) aspect. The corpus’s two scalar directions are established as distinct before either receives a physical name.

---

### CT1.11a — The involution table of the four sectors

**Thm.** $(0)$ **Dictionary.** A8's four sectors are CT1.1's blocks under the identification
$$
\mathbf F_{(+,\mathcal R)}=F_G\oplus F_H\oplus F_{D^+}\ (5{+}1{+}1)\ \leftrightarrow\ \mathcal E_{++};\qquad
\mathbf F_{(-,\mathcal R)}=F_{W^+}\oplus F_{W^-}\oplus F_Z\ (3)\ \leftrightarrow\ \mathcal E_{+-};
$$
$$
\mathbf F_{(+,\mathcal V)}=F_{J^+}\ (3)\ \leftrightarrow\ \mathcal E_{-+};\qquad
\mathbf F_{(-,\mathcal V)}=F_{J^-}\ (3)\ \leftrightarrow\ \mathcal E_{--}
$$
— first label $=$ the $T$-grading ($\eta^\mu\eta^\nu$ [A3, C13]), $\mathcal R/\mathcal V=$ the $S$-grading (reality is the swap grading [CT0.7]); machine-verified on CT1.2's generator table (17 generators: $E_0,\Sigma,\hat E^{ij}{\times}5,W_i,J_i,K_i$).
$(1)$ **Status of the two gradings.** $S=\operatorname{Ad}(\mathbb S)$ with $\mathbb S=\tfrac12(E_0+\Sigma)$ [CT0.7(1)] — an *inner algebra automorphism* ($\mathbb S^2=\mathbb S$? no: $\mathbb S$ unitary involution, machine). $T$ is a *pure grading*: the diagonal $\pm1$-map $\sigma_\mu\otimes\sigma_\nu\mapsto\eta^\mu\eta^\nu\,\sigma_\mu\otimes\sigma_\nu$ [A3] — $\neg$ multiplicative (witness: $T(\sigma_0\otimes\sigma_1)\,T(\sigma_0\otimes\sigma_2)=(-1)(-1)\ [\mathrm{C13}]\ \sigma_0\otimes(\sigma_1\sigma_2)\ne T(\sigma_0\otimes\sigma_1\sigma_2)$-type failure, machine), hence $\neg$ inner. $[S,T]=0$ on all 16 basis elements [CT1.1]; the grading group on $\mathfrak H(\mathbb C^4)$ is $\mathbb Z_2\times\mathbb Z_2$ with simultaneous eigenspaces $\mathcal E_{st}$, $\dim=(7,3,3,3)$.
$(2)$ **Table of the declared reversals.** With $\omega$ [D2.6] and $\Theta_{\mathfrak L}$ [D2.7]:
$$
\begin{array}{c|cccc|c}
& \mathbf F_{(+,\mathcal R)} & \mathbf F_{(-,\mathcal R)} & \mathbf F_{(+,\mathcal V)} & \mathbf F_{(-,\mathcal V)} & \text{edge/chain data}\\ \hline
S=\operatorname{Ad}(\mathbb S) & + & + & - & - & \text{reality grading [CT0.7]}\\
T\ (\text{grading}) & + & - & + & - & \eta^\mu\eta^\nu\ [\mathrm{A3},\mathrm{C13}]\\
\omega & \text{fixed} & W^+\!\leftrightarrow\!W^-;\ Z\ \text{fixed} & \neg\text{declared} & \neg\text{declared} & s(c)\leftrightarrow t(c);\ \text{charge}\mapsto-\text{charge [D2.6, EM.9];}\ \omega^2=1;\ R\mapsto R^{\mathrm T};\ \omega\notin\operatorname{Aut}(\Gamma),\ |V|\ge3\\
\Theta_{\mathfrak L} & \text{fixed} & \text{fixed} & \leftrightarrow & \leftrightarrow & \text{ledger order}\mapsto\text{reverse};\ J^+\leftrightarrow J^-;\ G(e)\mapsto G(e)^*\ (\alpha_e\widehat{ds}^{\,2}(e)\mapsto-\alpha_e\widehat{ds}^{\,2}(e),\ \sigma_e\ \text{fixed [D3.5]});\ \mathcal J\mapsto\mathcal J^*\ \text{[D3.6]};\ w\mapsto w^*\ \text{[CT2.8(1)]};\ \Theta^2=1\\
\omega\Theta_{\mathfrak L} & \text{fixed} & W^+\!\leftrightarrow\!W^- & \leftrightarrow & \leftrightarrow & \text{the fourth class}
\end{array}
$$
$\omega$ acts on the edge set, $\Theta_{\mathfrak L}$ on phase/ledger order — disjoint data $\Rightarrow$ they commute, and $\langle\omega,\Theta_{\mathfrak L}\rangle\cong\mathbb Z_2\times\mathbb Z_2$ with classes $(1,\omega,\Theta_{\mathfrak L},\omega\Theta_{\mathfrak L})$; $\omega$ is charge-odd [D2.6; covariance of the closed-core charge read: EM.9a], $\Theta_{\mathfrak L}$ phase-odd and charge-even [D2.7, D3.5, D3.6].
$(3)$ **Edge-class answer (the sector question at edge level).** Real edges split into $\sigma_e=\pm1$ [CT0.9: $\Phi=\{0,\pi\}$]; virtual edges carry $\neg$registration [A5, A7, D0.5: $\phi_e$ defined on $E_{\mathcal R}$ only] — a proposed $(\pm,\mathcal V)$ split has no read: the virtual class is single and ungraded (weight $1$, no phase). The two sign structures ($\sigma$ vs $(-1)^{\aleph}$) are independent [CT0.10].
$(4)$ **[READING] rows (recorded, $\neg$adopted).** External CPT vocabulary maps as: $C\leftrightarrow\omega$ (the charge-odd reversal [D2.6]; sign-level realization $\sigma_e\mapsto-\sigma_e$: EM.24(1) — **E**, forward pointer); $T\leftrightarrow\Theta_{\mathfrak L}$ (ledger-time reversal [D2.7] — $\neg$ anti-unitary: no anti-unitary operator is declared; conjugation acts on weights/phases [CT2.8(1), D3.6]); $P\leftrightarrow$ the alignment-pattern reversal $\mathcal P\mapsto E_{\mathcal R}\setminus\mathcal P$ (equivalently $\alpha_e\mapsto\pi-\alpha_e$) with the mirror classification of Def-EM.21/Def-EM.22, EM.23 — **E**, forward pointers: a pattern-level reversal on configuration data (spacetime parity as a Lorentzian field-algebra read has count $0$ in Parts 1–2; the orientation read $\chi=\operatorname{sign}(k)$ remains [CANDIDATE], not adopted); "CPT" $\leftrightarrow$ the derived composition $C\circ P\circ T$ on $\mathfrak C(\mathcal R)$ with unconditional $|w|^2$-invariance [EM.24(4)–(5) — **E**, forward pointer]; at the involution-table level its reversal part is the $\omega\Theta_{\mathfrak L}$ class of $(2)$. This is the exact amount of reversal structure the axioms declare — $\neg$ a Lorentzian CPT theorem (no Lorentzian field algebra, no spinor bundle in the inventory).

**Req.** A3, A5, A7, A8; C3; D0.5, D2.6, D2.7, D3.5, D3.6; CT0.7, CT0.7a, CT0.9, CT0.10, CT0.12, CT1.1, CT1.2, CT1.6, CT1.9, CT1.11 (Part 1); CT2.8(1) (**C** — forward pointer, re-verification); EM.9 (**E** — forward pointer, re-verification); exact $\mathbb Q(i)$ matrix arithmetic, exhaustive pattern enumeration, non-multiplicativity witness [math; machine: `checks/verify_merge_tierA.py` §E].

**Pf.**
$$(0):\ \text{CT1.2's table verbatim: }\ E_0,\Sigma,\hat E^{ij}\in\mathcal E_{++};\ W_i\in\mathcal E_{+-};\ J_i\in\mathcal E_{-+};\ K_i\in\mathcal E_{--}\ \wedge\ \text{CT0.12's aspect rows}\ [\text{machine}]
$$
$$(1):\ \mathbb S=\tfrac12(E_0+\Sigma)\ [\mathrm{CT0.7}(1)];\quad \operatorname{Ad}(\mathbb S)(X)=\mathbb S X\mathbb S=S(X)\ [\mathrm{CT0.7}(2)];\qquad T^2=\mathbb 1,\ S^2=\mathbb 1,\ [S,T]=0\ [\mathrm{A3},\ \mathrm{CT1.1}]
$$
$$
T\ \neg\text{multiplicative}:\ T(\sigma_0\otimes\sigma_1)\,T(\sigma_0\otimes\sigma_2)=(-\sigma_0\otimes\sigma_1)(-\sigma_0\otimes\sigma_2)=\sigma_0\otimes i\sigma_3\ne -\,i\,\sigma_0\otimes\sigma_3=T(\sigma_0\otimes i\sigma_3)\ [\text{machine witness}]
$$
$$(2):\ D2.6/D2.7\ \text{verbatim on data rows};\quad J^\pm\ \text{blocks}:\ \Theta_{\mathfrak L}:\ J^+\leftrightarrow J^-\ [\mathrm{D2.7}]\ \wedge\ \mathbf F_{(+,\mathcal V)}=F_{J^+},\ \mathbf F_{(-,\mathcal V)}=F_{J^-}\ [\mathrm{A8}]\implies\text{sector exchange}
$$
$$
\omega:\ \text{charge}\mapsto-\text{charge}\ [\mathrm{D2.6}]\implies W^+\leftrightarrow W^-\ \text{inside}\ \mathbf F_{(-,\mathcal R)}\ [\text{charge eigen-decomposition of the weak block: }F_{W^+}\oplus F_{W^-}\oplus F_Z,\ \mathrm{A8}];\quad \omega\ \text{on}\ J^\pm:\ \neg\text{declared}
$$
$$
\omega^2=1:\ (R^{\mathrm T})^{\mathrm T}=R;\qquad \omega\notin\operatorname{Aut}(\Gamma):\ p(a)=b\ \wedge\ p(b)=a\ \forall(a,b)\in E:\ \bot\ \text{for}\ |V|\ge3\ [\text{machine: exhaustive on the tetrahedron}]
$$
$$
\text{disjoint supports}\ (\text{edge set vs phase/order})\implies[\omega,\Theta_{\mathfrak L}]=0;\qquad \omega^2=\Theta_{\mathfrak L}^2=1\implies\mathbb Z_2\times\mathbb Z_2.\ \blacksquare
$$

**Phys.** The corpus declares exactly two reversals and they commute: one flips orientation and charge on the edge set, the other flips ledger order and conjugates phases — four classes in total. The four force sectors of A8 are the joint grading atlas of the pair register; the Janus pair is the only sector pair a declared reversal exchanges, and spacetime parity has no force-sector house here — its pattern-level read lives on the alignment data (EM.23, EM.24 — **E**). The table is the complete reversal inventory at sector level: nothing further is derivable without a new declaration.

---

### CT1.11b — The native Clifford frames of the pair register and the weak-covariance pincer

**Thm.** On $\mathfrak H(\mathbb C^4)$ with CT1.2's named basis and CT0.7's $\mathbb S$, $\Pi_{\mathcal R}=\tfrac14(3E_0+\Sigma)$, $\Pi_{\mathcal V}=\tfrac14(E_0-\Sigma)$. Call the $15$ non-identity $\sigma_\mu\otimes\sigma_\nu$ [A3, CT1.1] the *Pauli products* — each Hermitian, squaring to $+I_4$, traceless. A *frame* is a $4$-subset of pairwise-anticommuting Pauli products; for a frame $\mathcal F=(e_1,e_2,e_3,e_4)$ let $\gamma_{\mathcal F}:=e_1e_2e_3e_4$ (its *pseudoscalar*; frame- and order-dependent: every transposition flips its sign).
$(1)$ **Native frames.** There are exactly $30$ frames (unordered; $720$ as ordered tuples) among the $\binom{15}{4}=1365$ candidates. For every frame: $\gamma_{\mathcal F}$ is Hermitian, $\gamma_{\mathcal F}^2=I_4$, $\mathfrak T\gamma_{\mathcal F}=0$, $\{\gamma_{\mathcal F},e_i\}=0$; and the $16$ real products $\{e_{i_1}\cdots e_{i_r}\}_{r=0..4}$ are $\mathbb R$-linearly independent — the frame generates a real subalgebra isomorphic to $Cl(4,0)$ acting on $\mathbb C^4\cong\mathbb R^8$, **with no new axiom**: A3's Pauli facts and CT1.1's basis suffice. The signature is Euclidean ($e_i^2=+I_4$); the representative $\eta=(-,+,+,+)$ [C13] of A3's sign vector labels the $T$-grading only [CT1.1] and enters no Clifford relation. No canonical pseudoscalar exists: a distinguished "$\gamma$-element" would be a choice, $\neg$a derivation.
$(2)$ **The pseudoscalar catalog (exhaustive).** All $15$ Pauli products occur as $\pm\gamma_{\mathcal F}$, **each from exactly $2$ frames**, in three species:
$$
\begin{array}{c|c|c|c}
\text{species} & \gamma_{\mathcal F}\ (\text{up to sign}) & [\gamma_{\mathcal F},\mathbb S] & \text{commuting}\ W_i\\ \hline
\text{mixed}\ (6) & \sigma_0\otimes\sigma_i\ /\ \sigma_i\otimes\sigma_0 & \pm2iJ_i & W_i\ \text{only}\\
\text{diagonal}\ (3) & \sigma_i\otimes\sigma_i\in\mathcal E_{++} & 0 & W_i\ \text{only (anticomm.}\ W_j,W_k)\\
\text{off-diag. spatial}\ (6) & \sigma_i\otimes\sigma_j\ (i\ne j) & \mp2iK_k,\ k=6{-}i{-}j & \text{none (anticomm.}\ W_k)
\end{array}
$$
No pseudoscalar commutes with more than one $W_i$; none anticommutes with more than two. Witness frame $\mathcal F_0=(\sigma_1\otimes\sigma_2,\ \sigma_2\otimes\sigma_2,\ \sigma_3\otimes\sigma_2,\ \sigma_0\otimes\sigma_1)$:
$$
\gamma_{\mathcal F_0}=\sigma_0\otimes\sigma_3=\operatorname{diag}(1,-1,1,-1);\qquad
P^{(\mathcal F_0)}_\pm:=\tfrac12(I_4\mp\gamma_{\mathcal F_0})=\operatorname{diag}(0,1,0,1)\ /\ \operatorname{diag}(1,0,1,0)
$$
— both idempotent, orthogonal, summing to $I_4$, trace $2$, rank $2$ (exact forms, machine).
$(3)$ **The weak-covariance pincer.** No grading involution of the pair register can be weak-covariant, from either side:
**(a) commuting side.** $\{M:[M,W_i]=0\ \forall i\}=\operatorname{span}_{\mathbb C}\{\Pi_{\mathcal R},\Pi_{\mathcal V}\}$ exactly (complex dimension $2$ — Schur on the $3\oplus1$ decomposition [CT1.10, CT0.7]; machine nullspace solve). Its involutions are $a\Pi_{\mathcal R}+b\Pi_{\mathcal V}$ with $a^2=b^2=1$, traces $3a+b\in\{\pm4,\pm2\}$; a pseudoscalar needs trace $0$ (cyclic flip: $\mathfrak T(e_1e_2e_3e_4)=-\mathfrak T(e_2e_3e_4e_1)$) — $3a+b=0\ \wedge\ a^2=b^2=1$ has **no solution**.
**(b) anticommuting side.** $\{M:\{M,W_i\}=0\ \forall i\}=\mathbb C\cdot\Pi_{\mathcal V}$ exactly (complex dimension $1$; machine nullspace solve): rank $1$, trace $1$ — singular, never an involution. Structural reason: an invertible $M$ anticommuting with every $W_i$ would make $\operatorname{Ad}(M)$ a Lie automorphism of $\operatorname{span}\{W_i\}$ equal to $-\mathrm{id}$ — but $-\mathrm{id}$ reverses the bracket ($[W_1,W_2]=iW_3\mapsto-iW_3\ne iW_3$) [CT1.4]: contradiction.
**(c) exhaustive.** Every one of the $15$ attained pseudoscalars fails (a) and (b) explicitly, entrywise: for each, $[\gamma,W_i]\ne0$ for some $i$ and $\{\gamma,W_i\}\ne0$ for some $i$.
**(d) carrier side.** On any $2$-dim carrier with weak action $W_i\mapsto\tfrac12\sigma_i$ (the weak seed locus: EW.32): $\{m:[m,\sigma_i]=0\ \forall i\}=\mathbb C\cdot I_2$ and $\{m:\{m,\sigma_i\}=0\ \forall i\}=\{0\}$ — the weak seed representation is irreducible: no nontrivial projector commutes with the weak action, and no grade anticommutes with it.
$(4)$ **The native selectivity (what the weak force does grade).** The weak force grades the pair arena by **$S$-parity**: $W_i\Pi_{\mathcal V}=0$ exactly $\forall i$; $\sum_iW_i^2=2\Pi_{\mathcal R}$ [Cor CT0.7a]; $\bigcap_i\ker W_i=\operatorname{im}\Pi_{\mathcal V}$ exactly (the $1$-dim singlet line; machine) — a $3$-active/$1$-inactive split. This is a force-arena selectivity; a matter grade would have to live on a carrier on which the gauge action is trivial — the opposite pattern.
$(5)$ **Non-alignment.** $[\gamma_{\mathcal F},\mathbb S]=0\iff\gamma_{\mathcal F}=\pm\,\sigma_i\otimes\sigma_i$: the $S$-definite pseudoscalars are exactly the three diagonal ones — they live in $\mathcal E_{++}$, the gravity/Higgs block [CT1.1, CT1.2], and are still $\neg$weak-covariant (each anticommutes with the two non-own $W$: e.g.\ $[\sigma_3\otimes\sigma_3,\ W_1]=2iE^{23}$ exactly — the weak rotation turns an $S$-definite pseudoscalar into gravitational shear). Under the swap, off-diagonal pseudoscalar grades rotate into the Janus seal sector: $[\sigma_0\otimes\sigma_3,\ \mathbb S]=2iJ_3$. The frame splits and the $S$-split provably do not align: $\operatorname{rank}(P^{(\mathcal F_0)}_\pm\Pi_{\mathcal R})=2$, $\operatorname{rank}(P^{(\mathcal F_0)}_\pm\Pi_{\mathcal V})=1$ — cross-ranks $(2,1,2,1)$ against the $S$-split's $(3,1)$.

**Req.** A3; C3; CT0.7, CT0.7a, CT1.1, CT1.2, CT1.4, CT1.10, CT1.11a (Part 1); EW.32 (**D**; seed-carrier locus — forward pointer, corroboration only: clause (3d) is self-contained by Schur [math]); exhaustive frame enumeration, exact nullspace solves over $\mathbb Q(i)$, Schur's lemma [math; machine: `checks/verify_merge_tierC.py`].

**Pf.**
$$(1):\ \gamma_{\mathcal F}^2=(e_1e_2e_3e_4)(e_1e_2e_3e_4)=(-1)^{\binom42}e_1^2e_2^2e_3^2e_4^2=(-1)^6I_4=I_4;\qquad \mathfrak T\gamma_{\mathcal F}=-\mathfrak T(e_2e_3e_4e_1)=-\mathfrak T\gamma_{\mathcal F}\implies\mathfrak T\gamma_{\mathcal F}=0\ [\text{cyclic}]
$$
$$\{\gamma_{\mathcal F},e_i\}=0:\ e_i\ \text{anticommutes with the three other factors},\ \text{commutes with itself};\qquad 30\ \text{frames}:\ \text{exhaustive enumeration of}\ 1365\ \text{candidates}\ [\text{machine}]
$$
$$\mathbb R\text{-independence of the}\ 16\ \text{products}:\ \text{exact elimination on}\ \mathbb Q\text{-flattened components, all}\ 30\ \text{frames}\ [\text{machine}]$$
$$(2):\ \text{canonical-sign census over the}\ 30\ \text{frames}\ [\text{machine}];\quad \text{species}=\text{index patterns};\quad [\sigma_0\otimes\sigma_3,\mathbb S]=2iJ_3,\ [\sigma_3\otimes\sigma_3,W_1]=2iE^{23}:\ \text{direct products}\ [\text{machine}]
$$
$$\mathcal F_0:\ \text{direct multiplication}:\ \gamma_{\mathcal F_0}=\sigma_0\otimes\sigma_3;\quad P_\pm^2=P_\pm,\ P_+P_-=0,\ P_++P_-=I_4,\ \mathfrak T P_\pm=2\ [\text{machine}]$$
$$(3a):\ \text{nullspace of the}\ 3\times16\ \text{complex linear system}\ [X,W_i]=0\ \text{in the Pauli basis}\ =\ \operatorname{span}\{\Pi_{\mathcal R},\Pi_{\mathcal V}\}\ [\text{machine, exact}];\quad \text{Schur on}\ 3\oplus1\ [\mathrm{CT1.10};\ \text{math}]
$$
$$\text{involutions in the commutant}:\ (a\Pi_{\mathcal R}+b\Pi_{\mathcal V})^2=I_4\iff a^2=b^2=1;\quad \mathfrak T=3a+b\in\{4,2,-2,-4\}:\ \neg\exists\ \text{trace-0 involution}$$
$$(3b):\ \text{nullspace of}\ \{X,W_i\}=0\ =\ \mathbb C\cdot\Pi_{\mathcal V}\ [\text{machine}];\qquad W_i\Pi_{\mathcal V}=0\ [(4)]\implies\operatorname{rank}\Pi_{\mathcal V}=1:\ \text{singular}$$
$$\text{invertible case}:\ \operatorname{Ad}(M)W_i=-W_i\implies\operatorname{Ad}(M)[W_1,W_2]=[-W_1,-W_2]=[W_1,W_2]=iW_3,\ \text{but}\ \operatorname{Ad}(M)(iW_3)=-iW_3:\ \bot\ [\mathrm{CT1.4}]$$
$$(3c):\ \text{entrywise for all}\ 15\ [\text{machine}];\qquad (3d):\ 2\times2\ \text{nullspace solves}\ [\text{machine};\ \text{Schur}]$$
$$(4):\ W_i\ \text{preserves}\ \vee^2,\wedge^2\ [\mathrm{CT0.7}(3)];\quad W_i|_{\wedge^2}=0\ (\text{singlet});\quad \sum_iW_i^2=\tfrac32E_0+\tfrac12\Sigma=2\Pi_{\mathcal R}\ [\text{Cor CT0.7a}];\quad \bigcap\ker W_i:\ \text{machine}$$
$$(5):\ [\sigma_\mu\otimes\sigma_\nu,\mathbb S]=0\iff\sigma_\mu\otimes\sigma_\nu=\sigma_\nu\otimes\sigma_\mu\iff\mu=\nu\ [\text{machine over all}\ 15];\quad \text{ranks by exact elimination}.\ \blacksquare$$

**Phys.** The pair register carries a full Euclidean Clifford structure natively — thirty frames, fifteen pseudoscalars, all of it derived from A3's Pauli facts with no declaration anywhere — and the weak force selects exactly one split inside it: the $3$-active/$1$-inactive $S$-parity grading. But the pincer is exact: from the commuting side the only weak-covariant candidates are the two $S$-projections, whose involutions all have nonzero trace; from the anticommuting side the candidate set collapses to a singular singlet line. No pseudoscalar grade of this register can ever behave as a weak-covariant matter grade — the obstruction is not a shortage of matrices but the absence of a spacetime-side carrier on which the gauge action is trivial, and that absence is a declaration the corpus has not made.

**Rmk (deficit relocation record).** The completeness audit's first deficit is hereby *relocated inside Parts 1–2*: native frames exist (clause (1)); their grades cannot be weak-covariant (clause (3)); a Dirac-type operator would additionally require a per-edge frame assignment $e\mapsto\mathcal F_e$ coupled to the EW.32 transport — an enumerated would-be declaration of the audit layer, recorded here as **not adopted, no tag issued**. The reversal structure declared by the corpus remains exactly $\langle\omega,\Theta_{\mathfrak L}\rangle\cong\mathbb Z_2\times\mathbb Z_2$ [CT1.11a].

---

## Tier 2 — Lyapunov Stability of the Pair State

### L0 — The ledger–tilt coupling

**Thm.** *Dynamical scope (declared at use — the crystallization–tilt coupling; CT4.5a precedent: A4–A7 declare the criterion, the tick and the ledger, $\neg$ a state update at the seal):* every A4 crystallization event applies exactly one Gibbs tilt step [D0.3] to the pair state of that event. Under A5 ($\rho_\circ=\tfrac14I$), A6 ($\mathcal T(\rho)=U\rho U^\dagger$, $U\sim\mu_\star$; $|\mathfrak L(\tau_{n+1})|=|\mathfrak L(\tau_n)|+n_{\mathrm{real\_out}}(\tau_n)$), A7 ($\mathfrak L=\bigcup_{n\ge0}\mathfrak L(\tau_n)$, $|\mathfrak L(\tau_n)|=\sum_{k<n}n_{\mathrm{real\_out}}(\tau_k)$), D0.3/D0.4 ($\gamma:=1-4\varepsilon_q$), CT0.8:
$(1)$ **Tick preserves $V$.** $\ V\bigl(\tilde K(\mathcal T(\rho))\bigr)=V\bigl(\tilde K(\rho)\bigr)$ for every draw [A6; L1(2)].
$(2)$ **Events apply the tilt.** At tick $\tau_n$ the A4 criterion selects $n_{\mathrm{real\_out}}(\tau_n)$ edges into the ledger [A6]; under the declared scope each selection maps its pair state
$$
\rho\ \longmapsto\ \tilde{\mathcal T}_\gamma(\rho)=\frac{\rho\,e^{-\gamma\rho}}{\mathfrak T(\rho\,e^{-\gamma\rho})},\qquad
\gamma=1-4\varepsilon_q\in(0,1]\quad[\mathrm{D0.3};\ \mathrm{CT0.8}];
$$
$Z_\gamma>0$ on faithful $\rho$ [Cor L0a] $\implies\tilde{\mathcal T}_\gamma(\rho)$ faithful, $\succeq0$, $\mathfrak T=1$ [D0.3]; $\ \tilde{\mathcal T}_\gamma\ne\mathcal T$ [D0.3].
$(3)$ **Tilt contracts $V$.** $\ V'\le V$, equality iff $\rho=\tfrac14I$ [A5; L1(5)].
$(4)$ **Ledger counts tilt steps.** $\#\{\text{tilt steps at }\tau_n\}=n_{\mathrm{real\_out}}(\tau_n)$; cumulative count $|\mathfrak L(\tau_n)|=\sum_{k<n}n_{\mathrm{real\_out}}(\tau_k)$ [A6, A7 — exact integer recursion]. On one pair channel with $k$ events interleaved with arbitrary draws, the $V$-sequence is that of $\tilde{\mathcal T}_\gamma^{k}(\rho_0)$ — the interleaving is spectrally inert by $(1)$; per fixed $k$: $\ \mu_k=\bigl(1-\tfrac\gamma4\bigr)^{k}\mu_0+O(\mu_0^2)$ [L2, iterated].
$(5)$ **Contraction is the ledger dynamics.** The deficits of L1–L3 are realized once per ledger increment: the deficit fraction per tilt step is $\tfrac{\gamma(8-\gamma)}{16}$ of $V$ to exact leading order [L2], accumulating as $V\mapsto\bigl(1-\tfrac\gamma4\bigr)^{2k}V+O(\delta\rho_0^3)$ after $k$ recorded events; the inertial read $m_i^2(q)=\Delta S(q)$ [L3(4)] is the deficit read per increment.

**Req.** A4; A5; A6; A7; D0.2; D0.3; D0.4; D1.2; CT0.8; L1; L2 (forward pointers — the derivation order of `index/dependency_tree.md` places this tag after L2); the declared crystallization–tilt dynamical scope (theorem-local; see Status); exact integer recursion, exact Haar covariance over $\mathbb Q(i)$, exact rational $\log/\exp$-enclosures [math; machine: `checks/verify_L0_ledger_tilt.py` §A–§D].

**Pf.**
$$
(1):\ K(\mathcal T\rho)=UKU^\dagger\ [\text{functional-calculus covariance}];\qquad
\mathfrak T\bigl(K(\mathcal T\rho)\,\mathcal T\rho\bigr)=\mathfrak T(K\rho)\ [\text{cyclicity}]\implies\tilde K(\mathcal T\rho)=U\tilde KU^\dagger\implies V'=V\ [\mathrm{L1}(2)]
$$
$$
(2):\ \varepsilon_q\in[0,\tfrac14)\ [\mathrm{CT0.8}]\implies\gamma=1-4\varepsilon_q\in(0,1]\ [\text{exact endpoints}:\ \varepsilon_q=0\mapsto\gamma=1];\qquad
Z_\gamma\in(0,\,e^{-\gamma/4}]\ [\text{Cor L0a}]\implies\lambda_i'=\lambda_ie^{-\gamma\lambda_i}/Z_\gamma>0\ [\exp>0\ \text{on exact enclosures}]
$$
$$
\implies\tilde{\mathcal T}_\gamma(\rho)\ \text{faithful},\ \succeq0,\ \mathfrak T\bigl(\tilde{\mathcal T}_\gamma(\rho)\bigr)=1\ [\mathrm{D0.3}\ \text{normalization}]
$$
$$
(3):\ \mathrm{L1}(5)\ [\text{Jensen on}\ \phi_\gamma;\ \text{zero locus}\ \rho=\tfrac14I]
$$
$$
(4):\ |\mathfrak L(\tau_0)|=0\ [\mathrm{A7}];\quad\text{recursion}\ [\mathrm{A6}]\implies|\mathfrak L(\tau_n)|=\textstyle\sum_{k<n}n_{\mathrm{real\_out}}(\tau_k)\ [\mathrm{A7}]\ \text{by induction on}\ n\ [\text{exact integers; machine}]
$$
$$
\operatorname{spec}\bigl(\mathcal T(\rho)\bigr)=\operatorname{spec}(\rho):\ \mathfrak T\bigl((U\rho U^\dagger)^m\bigr)=\mathfrak T(\rho^m),\ m=1..4\ [\text{cyclicity; machine, exact over}\ \mathbb Q(i)]\implies V\circ\mathcal T=V\ [(1)]
$$
$$
\implies V\bigl(\tilde{\mathcal T}\,\mathcal T\,\tilde{\mathcal T}\cdots(\rho_0)\bigr)=V\bigl(\tilde{\mathcal T}^{\,k}(\rho_0)\bigr)\ [\text{composition}];\qquad
\mu_k=\bigl(1-\tfrac\gamma4\bigr)^k\mu_0+O(\mu_0^2):\ \text{induction on L2's}\ \mu'=\bigl(1-\tfrac\gamma4\bigr)\mu+O(\mu^2)\ [\text{coefficient-wise composition; machine},\ k\le3]
$$
$$
(5):\ \mathrm{L2}\ \text{per step}:\ V'-V=-\tfrac{\gamma(8-\gamma)}{16}V+O(\delta\rho^3);\qquad
\text{accumulation at leading order from}\ (4).\ \blacksquare
$$

**Cor L0a (tilt modular update).** Faithful $\rho$, $K:=-\log\rho$ [D0.3], $K':=K\bigl(\tilde{\mathcal T}_\gamma(\rho)\bigr)$, $Z_\gamma:=\mathfrak T(\rho\,e^{-\gamma\rho})$:
$$
K'=K+\gamma\rho+\log Z_\gamma\cdot I;\qquad
Z_\gamma\in(0,\,e^{-\gamma/4}];\qquad
\mathfrak T(K'-K)=\gamma+4\log Z_\gamma\le0,
$$
with equality iff $\rho=\tfrac14I$; $\ \gamma=1:\ Z_1\le e^{-1/4}$, $\ \mathfrak T(K'-K)=1+4\log Z_1\le0$.

**Req (Cor).** A1; A5; D0.3; CT0.8; Jensen's inequality for $p\,e^{-\gamma p}$, exact rational $\log/\exp$-enclosures [math; machine: `checks/verify_L0_ledger_tilt.py` §B–§C].

**Pf (Cor).**
$$
\rho,\ \tilde{\mathcal T}_\gamma(\rho)\ \text{simultaneously diagonalizable}\ [\text{functional calculus on a commuting family}];\qquad
\lambda_i'=\lambda_ie^{-\gamma\lambda_i}/Z_\gamma
$$
$$
\implies-\log\lambda_i'=-\log\lambda_i+\gamma\lambda_i+\log Z_\gamma\ [\text{exact spectral identity; machine at two enclosure tolerances}]\implies K'=K+\gamma\rho+\log Z_\gamma\cdot I
$$
$$
g(p):=p\,e^{-\gamma p}:\ \ g''(p)=e^{-\gamma p}\bigl(\gamma^2p-2\gamma\bigr)\le0\ \ \text{on}\ \ [0,1],\ \gamma\in(0,1]\quad[\gamma p\le1<2;\ \text{exact rational sign}]
$$
$$
\text{Jensen}:\ Z_\gamma=\textstyle\sum_ig(\lambda_i)\le4\,g\bigl(\tfrac14\bigr)=e^{-\gamma/4},\ \ \text{equality iff}\ \lambda_i=\tfrac14\ \forall i\iff\rho=\tfrac14I\ [\text{strict concavity}];\qquad
Z_\gamma>0\ [\lambda_i>0]
$$
$$
\mathfrak T(K'-K)=\gamma\,\mathfrak T\rho+4\log Z_\gamma=\gamma+4\log Z_\gamma\le\gamma+4\bigl(-\tfrac\gamma4\bigr)=0;\qquad
\gamma=1:\ Z_1\le e^{-1/4},\ \ \mathfrak T(K'-K)=1+4\log Z_1.\ \blacksquare
$$

**Phys.** The Haar tick rotates the pair state without touching the Lyapunov function; the ledger grows exactly at the A4 events; under the declared crystallization dynamics every event is one Gibbs tilt step — the only contraction a pair state undergoes. The monotonicity of L1–L3 is thereby the per-increment dynamics of the ledger: ticks rotate, events contract, and $|\mathfrak L(\tau_n)|$ is the tilt-step count. Each tilt step updates the modular Hamiltonian by $K\mapsto K+\gamma\rho+\log Z_\gamma\cdot I$, whose trace deficit $\gamma+4\log Z_\gamma\le0$ vanishes only at the A5 vacuum. No particle identification.

---

### L1 — The Lyapunov function of the pair state

**Thm.** Faithful pair states $\rho$ [A1: $\rho\in\mathfrak H(\mathbb C^4)$, $\rho\succeq0$, $\mathfrak T\rho=1$, $\operatorname{spec}\rho\subset(0,1]$]; with
$$
\delta\rho:=\rho-\tfrac14I\ \ [\mathrm{A5}:\ \rho_\circ=\tfrac14I];\qquad
\mu:=\operatorname{spec}(\delta\rho)\subset\bigl[-\tfrac14,\tfrac34\bigr];\qquad
\textstyle\sum_i\mu_i=0\ \ [\mathfrak T\rho=1];
$$
$$
\gamma:=1-4\varepsilon_q\in(0,1]\ \ [\mathrm{D0.3};\ \mathrm{A4},\ \mathrm{D0.4},\ \mathrm{CT0.8}];
$$
$$
K:=-\log\rho;\qquad
\tilde K:=K-\mathfrak T(K\rho)\,I\ \ [\mathrm{D0.3}];\qquad
V(\tilde K):=\mathfrak T\bigl(\tilde K^2\bigr)\ \ge0;
$$
$(1)$ **Zero locus.** $V=0\iff\tilde K=0\iff\rho=\tfrac14I$ — the A5 vacuum.
$(2)$ **Tick invariance.** $V\bigl(\tilde K(\mathcal T(\rho))\bigr)=V\bigl(\tilde K(\rho)\bigr)$ for every draw [A6: $\mathcal T(\rho)=U\rho U^\dagger$].
$(3)$ **Decay identity ($\gamma$-dependent).** Under the Gibbs tilt $\rho':=\tilde{\mathcal T}_\gamma(\rho)$ [D0.3], with $V':=V\bigl(\tilde K(\rho')\bigr)$:
$$
V'-V=-\gamma\sum_i\phi_\gamma(\mu_i)+O(\delta\rho^4);\qquad
\phi_\gamma(x):=2x\log(1+4x)-\gamma x^2;
$$
$$
\text{leading}:\ \ V'-V=-\gamma(8-\gamma)\textstyle\sum_i\mu_i^2+O(\delta\rho^3);\qquad
\gamma=1:\ \ V'-V=-\textstyle\sum_i\phi(\mu_i)+O(\delta\rho^4),\ \ \phi:=\phi_1 .
$$
$(4)$ **$\phi_\gamma$-calculus.** $\phi_\gamma(0)=\phi_\gamma'(0)=0$; $\ \phi_\gamma=\phi_1+(1-\gamma)x^2$;
$$
\phi_\gamma''(x)=\frac{14+16x-32x^2}{(1+4x)^2}+2(1-\gamma)\quad[\text{exact rational identity}];
$$
$$
\phi_\gamma\ \text{convex on}\ W_\gamma\supseteq W:=\Bigl[\tfrac{1-2\sqrt2}{4},\tfrac{1+2\sqrt2}{4}\Bigr]\supseteq\bigl[-\tfrac14,\tfrac34\bigr]\quad\forall\gamma\in(0,1];\qquad
\phi_\gamma>0\ \ \text{on}\ \ \bigl[-\tfrac14,\tfrac34\bigr]\setminus\{0\}.
$$
$(5)$ **Monotonicity.** Jensen: $\ \sum_i\phi_\gamma(\mu_i)\ \ge\ 4\,\phi_\gamma\bigl(\tfrac14\sum_i\mu_i\bigr)=0\ $; hence, on the faithful simplex, for every $\gamma\in(0,1]$:
$$
V'\le V,\qquad V'=V\iff\tilde K=0\iff\rho=\tfrac14I .
$$

**Req.** A1; A4; A5; A6; D0.3, D0.4; CT0.8 (Part 1); exact formal-power-series arithmetic over $\mathbb Q$ with rational $\gamma$, exact $\mathbb Q(\sqrt2)$ order, Jensen's inequality, exact rational $\log$-enclosures, continuity–density extension [math; machine: `checks/verify_L_lyapunov.py`].

**Pf.**
$$
(1):\ \tilde K=0\iff K=\mathfrak T(K\rho)I\iff\rho=e^{-c}I\iff\rho=\tfrac14I\ [\mathfrak T\rho=1];\qquad
V=\mathfrak T(\tilde K^2)\ge0\ [\tilde K\ \text{Hermitian}],\quad V=0\iff\tilde K=0
$$
$$
(2):\ K(\mathcal T\rho)=-\log\bigl(U\rho U^\dagger\bigr)=UKU^\dagger\ [\text{functional-calculus covariance}];\qquad
\mathfrak T\bigl(K(\mathcal T\rho)\,\mathcal T\rho\bigr)=\mathfrak T\bigl(UK\rho U^\dagger\bigr)=\mathfrak T(K\rho)\ [\text{cyclicity}]
$$
$$
\implies\tilde K(\mathcal T\rho)=U\tilde KU^\dagger\implies V'=V\ [\text{cyclicity}]
$$
$$
(3):\ \rho\ \text{faithful}\implies\rho,\ \tilde{\mathcal T}_\gamma(\rho)\ \text{simultaneously diagonalizable}:\ \rho=\operatorname{diag}(\lambda),\ \lambda_i=\tfrac14+\mu_i;\qquad
\tilde K=\operatorname{diag}\bigl(-\log\lambda_i-S\bigr),\ \ S:=\mathfrak T(K\rho)=-\textstyle\sum_j\lambda_j\log\lambda_j
$$
$$
\lambda_i'=\lambda_ie^{-\gamma\lambda_i}/Z_\gamma,\ \ Z_\gamma=\textstyle\sum_j\lambda_je^{-\gamma\lambda_j};\qquad
\log\lambda_i'=\log\lambda_i-\gamma\lambda_i-\log Z_\gamma;\qquad e^{-\gamma/4}\ \text{cancels in the ratio}\implies\text{exact}\ \mathbb Q[[t]]\ \text{data}
$$
$$
\text{formal series along}\ \rho(t)=\tfrac14I+t\,\delta_0\ (\delta_0\ \text{Hermitian traceless, exact rational data}),\ \gamma\in\{\tfrac14,\tfrac12,\tfrac34,1\}:
$$
$$
V'-V+\gamma\textstyle\sum_i\phi_\gamma(\mu_i(t))\ \text{has vanishing}\ t^0..t^3\ \text{coefficients}\ [\text{machine, exact}];\qquad
t^4\ \text{coefficient}\ne0\ \text{generically}\implies O(\delta\rho^4)\ \text{sharp}
$$
$$
\phi_\gamma(x)=2x\bigl(4x-8x^2+\tfrac{64}3x^3-\dots\bigr)-\gamma x^2=(8-\gamma)x^2-16x^3+O(x^4)\implies\text{leading}:\ V'-V=-\gamma(8-\gamma)\textstyle\sum_i\mu_i^2+O(\delta\rho^3)
$$
$$
(4):\ \phi_\gamma'(x)=2\log(1+4x)+\tfrac{8x}{1+4x}-2\gamma x;\qquad
\phi_\gamma''(x)=\tfrac8{1+4x}+\tfrac8{(1+4x)^2}-2\gamma=\tfrac{14+16x-32x^2}{(1+4x)^2}+2(1-\gamma)\ [\text{common denominator}]
$$
$$
\gamma\in(0,1]:\ 2(1-\gamma)\ge0\implies\phi_\gamma''\ge\phi_1''\ \text{pointwise}\implies W_\gamma\supseteq W;\qquad
16x^2-8x-7=0\iff x=\tfrac{1\pm2\sqrt2}4\ [\mathbb Q(\sqrt2),\ \text{exact}];\qquad W\supseteq[-\tfrac14,\tfrac34]\ [\sqrt2\ge1]
$$
$$
\phi_\gamma=\phi_1+(1-\gamma)x^2;\qquad\phi_1\ \text{strictly convex on}\ W,\ \phi_1(0)=\phi_1'(0)=0\implies\phi_1>0\ \text{off}\ 0\implies\phi_\gamma>0\ \text{off}\ 0\ \text{on}\ [-\tfrac14,\tfrac34]
$$
$$
(5):\ \text{Jensen on convex}\ \phi_\gamma:\ \tfrac14\sum_i\phi_\gamma(\mu_i)\ge\phi_\gamma\bigl(\tfrac14\sum_i\mu_i\bigr)=\phi_\gamma(0)=0;\qquad
=\iff\mu=0\ \ [\textstyle\sum\mu=0;\ \text{strict convexity}]
$$
$$
\gamma>0\implies V'-V=-\gamma\textstyle\sum_i\phi_\gamma(\mu_i)+O(\delta\rho^4)\le0\ \text{near the vacuum};\qquad
\text{globally: exact rational}\ \log\text{-enclosure sweep},\ \gamma\in\{\tfrac14,\tfrac12,\tfrac34,1\}\ [\text{machine}]
$$
$$
\text{extension to every}\ \gamma\in(0,1]:\ V'-V\ \text{continuous in}\ (\operatorname{spec}\rho,\gamma)\ \text{on the faithful simplex}\times(0,1]\ [\log,\exp,\ \text{rational maps}];\ \ \le0\ \text{on a dense rational set}\implies\le0\ \text{everywhere}\ [\text{math}]
$$
$$
V'=V\iff\tilde K=0:\ (\Leftarrow)\ (1);\qquad(\Rightarrow)\ \text{near vacuum by}\ (3),(4)\ \text{strictness}\ (\gamma>0);\ \ \text{sweep points strict off-vacuum}\ [\text{machine}].\ \blacksquare
$$

**Phys.** The pair state carries a natural nonnegative stability functional: the trace-square of its centered surprisal. Ledger ticks rotate it without changing it — the Haar conjugation of A6 is spectral, not contractive. The Gibbs tilt — a separate operation from the tick, determined by $\varepsilon_q$ — strictly lowers it, by an exact per-eigenvalue deficit $\gamma\phi_\gamma$, driving every faithful state toward the A5 vacuum. The tilt strength $\gamma=1-4\varepsilon_q$ is the normalized distance from the crystallization threshold to the vacuum: at $\varepsilon_q=0$ (sharp crystallization) the tilt is at maximum strength; at the vacuum threshold $\varepsilon_q=\tfrac14$ it vanishes. The tilt is grounded in the ledger–tick coupling [L0]: it is applied once per A4 crystallization event, and the ledger counts the steps.

---

### L2 — The temporal decay law

**Thm.** Under L1's setting, per tilt step [D0.3; L1(3)], to exact leading order:
$$
V'-V=-\Bigl[1-\bigl(1-\tfrac\gamma4\bigr)^{2}\Bigr]V+O(\delta\rho^3)=-\frac{\gamma(8-\gamma)}{16}\,V+O(\delta\rho^3);\qquad
V'=\bigl(1-\tfrac\gamma4\bigr)^{2}V+O(\delta\rho^3);
$$
$$
\gamma=1:\ \ V'-V=-\tfrac7{16}\,V+O(\delta\rho^3),\ \ V'=\tfrac9{16}V+O(\delta\rho^3);\qquad
\gamma\to0:\ \ V'=V\ \ (\text{identity-tilt limit});
$$
$$
\mu'=\bigl(1-\tfrac\gamma4\bigr)\mu+O(\mu^2)\quad[\text{eigenvalue contraction}];\qquad
\gamma=1:\ \ \mu'=\tfrac34\mu;\qquad
1-\bigl(1-\tfrac\gamma4\bigr)^2=\frac{\gamma(8-\gamma)}{16}\ \ [\text{exact rationals}].
$$

**Req.** A1; A4; A5; D0.3, D0.4; CT0.8 (Part 1); L1; exact formal-series arithmetic [math; machine: `checks/verify_L_lyapunov.py` §B].

**Pf.**
$$
K=-\log\bigl(\tfrac14I+\delta\rho\bigr)=\ln4\,I-4\,\delta\rho+O(\delta\rho^2);\qquad \mathfrak T(K\rho)=\ln4+O(\delta\rho^2)\ \ [\mathfrak T\delta\rho=0]
$$
$$
\implies\tilde K=K-\mathfrak T(K\rho)I=-4\,\delta\rho+O(\delta\rho^2)\implies V=16\,\mathfrak T(\delta\rho^2)+O(\delta\rho^3)=16\textstyle\sum_i\mu_i^2+O(\delta\rho^3)\ \ [\gamma\text{-free}]
$$
$$
\mathrm{L1}(3):\ V'-V=-\gamma\textstyle\sum_i\phi_\gamma(\mu_i)+O(\delta\rho^4);\qquad \gamma\phi_\gamma(x)=\gamma(8-\gamma)x^2+O(x^3)
$$
$$
\implies V'-V=-\gamma(8-\gamma)\textstyle\sum_i\mu_i^2+O(\delta\rho^3)=-\frac{\gamma(8-\gamma)}{16}\,V+O(\delta\rho^3)=-\Bigl[1-\bigl(1-\tfrac\gamma4\bigr)^2\Bigr]V+O(\delta\rho^3)
$$
$$
\lambda'=\lambda e^{-\gamma\lambda}/Z_\gamma:\quad\text{series}:\ \ \mu'=\bigl(1-\tfrac\gamma4\bigr)\mu+O(\mu^2)\ [\text{exact coefficient; machine}];\qquad
V'=16\bigl(1-\tfrac\gamma4\bigr)^2\textstyle\sum_i\mu_i^2+O(\delta\rho^3)
$$
$$
\gamma=1:\ \ 1-\tfrac14=\tfrac34,\ \ \bigl(\tfrac34\bigr)^2=\tfrac9{16},\ \ 1-\tfrac9{16}=\tfrac7{16},\ \ \gamma(8-\gamma)=7;\qquad
\gamma\to0:\ \ \bigl(1-\tfrac\gamma4\bigr)^2\to1.\ \blacksquare
$$

**Phys.** Near the vacuum, every tilt step contracts the Lyapunov function by a $\gamma$-dependent exact rational factor: $\bigl(1-\tfrac\gamma4\bigr)^2$ of $V$ survives, $\tfrac{\gamma(8-\gamma)}{16}$ of it is lost. At $\gamma=1$ ($\varepsilon_q=0$, sharp crystallization) the contraction is $\tfrac9{16}$ and the deficit exactly $\tfrac7{16}$ of $V$; at the vacuum threshold ($\gamma\to0$) the contraction is $1$ and the deficit $0$. The $\tfrac7{16}$ is not a stipulation: it is the decay rate at sharp crystallization, derived from $\varepsilon_q=0$ [D0.4]. The tilt is grounded in the ledger–tick coupling [L0]: one step per recorded crystallization event, so the decay law is the per-increment dynamics of the ledger.

---

### L3 — Entropy deficit and the inertial mass reading

**Thm.** Under L1, L2:
$(1)$ **Entropy deficit.** With $\delta\rho=\tfrac14\sum_ar_aG_a$ on the Pauli-tensor basis $\{G_a\}=\{\sigma_\mu\otimes\sigma_\nu\}_{(\mu,\nu)\ne(0,0)}$ [C1; $\mathfrak T(G_aG_b)=4\delta_{ab}$: CT1.1], $|\delta\rho|^2:=\mathfrak T(\delta\rho^2)$:
$$
\Delta S_{\mathrm{pair}}:=2\,|\delta\rho|^2=\tfrac12\,|r|^2;\qquad
S\bigl(\rho\,\big\|\,\tfrac14I\bigr)=\Delta S_{\mathrm{pair}}+O(\delta\rho^3)\qquad\bigl[S(\rho\|\sigma):=\mathfrak T\bigl(\rho(\log\rho-\log\sigma)\bigr)\bigr]
$$
$(2)$ **Lyapunov identification.** $\ \tilde K=-4\,\delta\rho+O(\delta\rho^2);\qquad V(\tilde K)=16\,|\delta\rho|^2+O(\delta\rho^3)=8\,\Delta S_{\mathrm{pair}}+O(\delta\rho^3).$
$(3)$ **Deficit decay ($\gamma$-dependent).** $\ V'-V=-\dfrac{\gamma(8-\gamma)}{2}\,\Delta S_{\mathrm{pair}}+O(\delta\rho^3);\qquad\gamma=1:\ \ V'-V=-\tfrac72\,\Delta S_{\mathrm{pair}}+O(\delta\rho^3).$
$(4)$ **Inertial read.** $\ m_i^2(q):=\Delta S(q)\quad[\Delta S(q):\ \text{the patch deficit, L4};\ \text{dimensionless, nats};\ \neg\text{a particle identification}].$

**Req.** A1; A5; C1; D0.3; CT1.1 (Part 1); L1, L2; exact formal-series arithmetic, relative-entropy eigenvalue identity [math; machine: `checks/verify_L_lyapunov.py` §B].

**Pf.**
$$
(1):\ \delta\rho\ \text{Hermitian}\wedge\ \mathfrak T\delta\rho=0\implies\delta\rho=\tfrac14\sum_ar_aG_a,\ \ r_a=\mathfrak T(\delta\rho\,G_a)\in\mathbb R\ \ [\mathrm{C1},\ \mathrm{CT1.1}:\ \mathfrak T(G_aG_b)=4\delta_{ab}]
$$
$$
|\delta\rho|^2=\mathfrak T(\delta\rho^2)=\tfrac1{16}\sum_{ab}r_ar_b\,\mathfrak T(G_aG_b)=\tfrac14|r|^2\implies2|\delta\rho|^2=\tfrac12|r|^2
$$
$$
S\bigl(\rho\|\tfrac14I\bigr)=\mathfrak T(\rho\log\rho)+\ln4=\textstyle\sum_i\bigl(\tfrac14+\mu_i\bigr)\log(1+4\mu_i)\ [\text{exact eigenvalue identity}]=2\textstyle\sum_i\mu_i^2+O(\mu^3)=\Delta S_{\mathrm{pair}}+O(\delta\rho^3)
$$
$$
(2):\ \mathrm{L2}\ \text{Pf}:\ \tilde K=-4\,\delta\rho+O(\delta\rho^2);\qquad V=16\,\mathfrak T(\delta\rho^2)+O(\delta\rho^3)=8\,\Delta S_{\mathrm{pair}}+O(\delta\rho^3)\ \ [(1)]
$$
$$
(3):\ \mathrm{L2}:\ V'-V=-\tfrac{\gamma(8-\gamma)}{16}V+O(\delta\rho^3)=-\tfrac{\gamma(8-\gamma)}{16}\cdot8\,\Delta S_{\mathrm{pair}}+O(\delta\rho^3)=-\tfrac{\gamma(8-\gamma)}{2}\Delta S_{\mathrm{pair}}+O(\delta\rho^3)
$$
$$
\gamma=1:\ \ \tfrac{\gamma(8-\gamma)}{2}=\tfrac72
$$
$$
(4):\ \text{definition};\qquad\text{a read},\ \neg\text{an identification}.\ \blacksquare
$$

**Phys.** The pair state's departure from the vacuum is one object under three exact leading reads: a squared Bloch radius, an entropy deficit against the maximally mixed pair, and the Lyapunov functional itself — locked by exact rational factors that depend on the tilt strength $\gamma=1-4\varepsilon_q$. The inertial read names the deficit $m_i^2(q)=\Delta S(q)$: mass-as-missing-information per channel, dimensionless in nats — a reading, not a particle claim; no pole-mass identification is asserted. The tilt is grounded in the ledger–tick coupling [L0]; the patch-level deficit $\Delta S(q)$ with its integer degree factor is derived in L4.

---

### L4 — The patch entropy deficit

**Thm.** Vertex $q$ of finite incidence (theorem-local scope); incident pair channels $\{(q,p)\}$ [A1]; $n(q)=\partial^{\leftarrow}(q)+\partial^{\rightarrow}(q)$ [D0.8]; $n_{\mathcal R}(q)$ [A4]; $n_{\mathcal V}(q):=n(q)-n_{\mathcal R}(q)$ [D0.1]. Patch deficit:
$$
\Delta S(q)\ :=\ \sum_{(q,p)\in\mathcal V}S\bigl(\rho_{qp}\,\big\|\,\tfrac14I\bigr)
\qquad[\text{sum over the virtual incident channels of}\ q;\ \ S(\cdot\|\cdot)\ \text{as in L3}(1)]
$$
$(1)$ **Channel sum.** $\ \Delta S(q)=\sum_{(q,p)\in\mathcal V}\Delta S_{\mathrm{pair}}(pq)+O(\delta\rho^3)=2\sum_{(q,p)\in\mathcal V}|\delta\rho_{pq}|^2+O(\delta\rho^3)$ [L3(1) per channel].
$(2)$ **Mean form.** For $n_{\mathcal V}(q)\ge1$, with $\langle\Delta S_{\mathrm{pair}}\rangle_q:=\frac1{n_{\mathcal V}(q)}\sum_{(q,p)\in\mathcal V}\Delta S_{\mathrm{pair}}(pq)$:
$$
\Delta S(q)\ =\ n_{\mathcal V}(q)\,\langle\Delta S_{\mathrm{pair}}\rangle_q+O(\delta\rho^3)\ =\ 2\,n_{\mathcal V}(q)\,\langle|\delta\rho|^2\rangle_q+O(\delta\rho^3)\ =\ \tfrac12\,n_{\mathcal V}(q)\,\langle|r|^2\rangle_q+O(\delta\rho^3);
$$
$n_{\mathcal V}(q)=0\implies\Delta S(q)=0$ [empty sum].
$(3)$ **Patch Lyapunov read.** $\ V_{\mathrm{patch}}(q):=\sum_{(q,p)\in\mathcal V}V(\tilde K_{pq})=8\,\Delta S(q)+O(\delta\rho^3)$; under per-channel tilt steps [D0.3]: $\ V_{\mathrm{patch}}'-V_{\mathrm{patch}}=-\frac{\gamma(8-\gamma)}2\,\Delta S(q)+O(\delta\rho^3)$ [L3(2), (3) summed].
$(4)$ **Inertial read, grounded.** $\ m_i^2(q)=\Delta S(q)$ [L3(4)] $=2\,n_{\mathcal V}(q)\,\langle|\delta\rho|^2\rangle_q+O(\delta\rho^3)$ — an integer multiplicity $n_{\mathcal V}(q)\in\mathbb Z_{\ge0}$ times the mean channel deficit; the read vanishes to leading order iff $n_{\mathcal V}(q)=0$ or every virtual-channel deviation vanishes.

**Req.** A1; A4; A5; C1; D0.1, D0.3, D0.8; L3; the finite-incidence scope (theorem-local); exact formal-series arithmetic over $\mathbb Q$, exact integer bookkeeping [math; machine: `checks/verify_L0_ledger_tilt.py` §E].

**Pf.**
$$
(1):\ S\bigl(\rho\,\|\,\tfrac14I\bigr)=\Delta S_{\mathrm{pair}}+O(\delta\rho^3)\ \text{per channel}\ [\mathrm{L3}(1),\ \text{sharp cubic remainder}];\qquad
\text{finite sum over}\ n_{\mathcal V}(q)\ \text{channels preserves the order}\ [\text{linearity}]
$$
$$
(2):\ n_{\mathcal V}\cdot\tfrac1{n_{\mathcal V}}\textstyle\sum=\sum\ [n_{\mathcal V}\ge1];\qquad|\delta\rho|^2=\tfrac14|r|^2\implies2\cdot\tfrac14=\tfrac12\ [\mathrm{L3}(1);\ \text{exact rationals}];\qquad
n_{\mathcal V}=0:\ \text{empty sum}=0
$$
$$
(3):\ \textstyle\sum_eV(\tilde K_e)=\sum_e\bigl(8\,\Delta S_{\mathrm{pair}}(e)+O(\delta\rho_e^3)\bigr)=8\,\Delta S(q)+O(\delta\rho^3)\ [\mathrm{L3}(2)];
$$
$$
\textstyle\sum_e\bigl(V'(\tilde K_e)-V(\tilde K_e)\bigr)=-\tfrac{\gamma(8-\gamma)}2\sum_e\Delta S_{\mathrm{pair}}(e)+O(\delta\rho^3)=-\tfrac{\gamma(8-\gamma)}2\Delta S(q)+O(\delta\rho^3)\ [\mathrm{L3}(3);\ \text{channel-wise tilt, D0.3}]
$$
$$
(4):\ (2)\ \text{into the L3}(4)\ \text{definition};\qquad n(q),\ n_{\mathcal R}(q)\ \text{integer counts}\ [\mathrm{D0.8},\ \mathrm{A4}]\implies n_{\mathcal V}(q)\in\mathbb Z_{\ge0}.\ \blacksquare
$$

**Phys.** The patch-level entropy deficit is the pair deficit counted with its multiplicity: every virtual channel incident to $q$ contributes its own missing information against the A5 vacuum, and a fully crystallized patch contributes zero. This grounds the symbol $\Delta S(q)$ of the inertial read $m_i^2(q)=\Delta S(q)$ [L3(4)]: mass-as-missing-information is an integer degree-deficit factor $n_{\mathcal V}(q)=n(q)-n_{\mathcal R}(q)$ times the mean channel deficit at leading order. A reading, not an identification.

---

### L5 — The second-order sector flow of the tilt

**Thm.** Under L1's setting, with $c:=1-\tfrac\gamma4$, $\ d:=\tfrac{\gamma(8-\gamma)}8$ [exact rationals in $\gamma$; L2]:
$(1)$ **Quadratic flow.** With $\delta\rho':=\tilde{\mathcal T}_\gamma(\rho)-\tfrac14I$ [D0.3]:
$$
\delta\rho'\ =\ c\,\delta\rho\ -\ d\,\Bigl(\delta\rho^2-\tfrac14|\delta\rho|^2E_0\Bigr)\ +\ O(\delta\rho^3);\qquad
\mathfrak T\Bigl(\delta\rho^2-\tfrac14|\delta\rho|^2E_0\Bigr)=0;\qquad
\delta\rho^2\succeq0 .
$$
$(2)$ **Single-sector landing.** $\delta\rho\in\mathcal E_{st}$ (a single $(S,T)$ sector [C3; CT1.2]) $\implies S(\delta\rho^2)=\delta\rho^2\ \wedge\ T(\delta\rho^2)=\delta\rho^2:\ \delta\rho^2\in\mathcal E_{++}$; the traceless part lies in $\operatorname{span}\{\Sigma,\hat E^{ij}\}$ [CT1.2, CT1.10]; the square channel of $\mathcal E_{++}$ closes in $\mathcal E_{++}$ — the quadratic transport inside the real block is one-directional.
$(3)$ **Partition function.** $\ \log Z_\gamma=-\tfrac\gamma4-d\,|\delta\rho|^2+O(\delta\rho^3)=-\tfrac\gamma4-\tfrac{\gamma(8-\gamma)}{16}\Delta S_{\mathrm{pair}}+O(\delta\rho^3)$ [Cor L0a; L3(1)]; $\ \gamma=1:\ \log Z_1=-\tfrac14-\tfrac78|\delta\rho|^2=-\tfrac14-\tfrac7{16}\Delta S_{\mathrm{pair}}+O(\delta\rho^3)$.
$(4)$ **Modular trace deficit.** $\ \mathfrak T(K'-K)=\gamma+4\log Z_\gamma$ [Cor L0a] $=-4d\,|\delta\rho|^2+O(\delta\rho^3)=-\tfrac{\gamma(8-\gamma)}4\Delta S_{\mathrm{pair}}+O(\delta\rho^3)\le0$ near the vacuum; $\ \gamma=1:\ -\tfrac74\Delta S_{\mathrm{pair}}+O(\delta\rho^3)$.
$(5)$ **Sharp-crystallization table ($\gamma=1$).** $\ c=\tfrac34;\quad d=\tfrac78;\quad1-c^2=\tfrac7{16}\ [\mathrm{L2}];\quad\tfrac d2=\tfrac7{16};\quad2d=\tfrac72\quad[\text{exact rationals}]$.

**Req.** A1; A5; C1, C3; D0.3, D0.4; CT0.8; CT1.1, CT1.2, CT1.10; L0 (Cor L0a); L1, L2, L3; exact formal-series arithmetic over $\mathbb Q$, exhaustive square-channel census over $\mathbb Q(i)$ (all $256$ basis pairs) [math; machine: `checks/verify_L0_ledger_tilt.py` §F].

**Pf.**
$$
(1):\ \rho\,e^{-\gamma\rho}=e^{-\gamma/4}\bigl(\tfrac14E_0+\delta\rho\bigr)e^{-\gamma\,\delta\rho}\ [\text{functional calculus on a commuting family}]
$$
$$
=e^{-\gamma/4}\Bigl[\tfrac14E_0+c\,\delta\rho-\gamma\bigl(1-\tfrac\gamma8\bigr)\delta\rho^2+O(\delta\rho^3)\Bigr],\qquad
\gamma\bigl(1-\tfrac\gamma8\bigr)=\tfrac{\gamma(8-\gamma)}8=d\ [\text{exact rationals}]
$$
$$
Z_\gamma=e^{-\gamma/4}\bigl[1-d\,|\delta\rho|^2+O(\delta\rho^3)\bigr]\ [\mathfrak T\delta\rho=0,\ \mathfrak T\delta\rho^2=|\delta\rho|^2];\qquad
\rho'=\bigl(\tfrac14E_0+c\,\delta\rho-d\,\delta\rho^2\bigr)\bigl(1+d\,|\delta\rho|^2\bigr)+O(\delta\rho^3)
$$
$$
\implies\delta\rho'=c\,\delta\rho-d\bigl(\delta\rho^2-\tfrac14|\delta\rho|^2E_0\bigr)+O(\delta\rho^3)\ [\text{coefficient-wise machine:}\ \gamma\in\{\tfrac14,\tfrac12,\tfrac34,1\}\times5\ \text{exact rational families}];
$$
$$
\mathfrak T\bigl(\delta\rho^2-\tfrac14|\delta\rho|^2E_0\bigr)=|\delta\rho|^2-|\delta\rho|^2=0;\qquad
\delta\rho^2\succeq0\ [\text{Hermitian square}]
$$
$$
(2):\ X^2=\textstyle\sum_ax_a^2G_a^2+\sum_{a<b}x_ax_b\{G_a,G_b\}:\ \text{the commutator channel cancels in squares}\ [\text{ordered double sum}]
$$
$$
\text{square channel}:\ \{G_a,G_b\}\ne0\implies T(G_aG_b)=\vartheta_a\vartheta_b\,G_aG_b\ [\text{exhaustive: all}\ 136\ \text{nonvanishing pairs of the}\ 256;\ \text{machine}];
$$
$$
\text{single sector}\implies\vartheta_a\vartheta_b=t^2=+1;\qquad
S=\operatorname{Ad}(\mathbb S)\ \text{inner}\implies S(G_aG_b)=S(G_a)S(G_b)=s^2G_aG_b\ [\mathrm{CT0.7}(2)]
$$
$$
\implies T(X^2)=X^2\ \wedge\ S(X^2)=X^2\implies X^2\in\mathcal E_{++}\ [\mathrm{CT1.1}];\qquad
\mathcal E_{++}=\operatorname{span}\{E_0,\Sigma,\hat E^{ij}\}\ [\mathrm{CT1.2},\ \mathrm{CT1.10}]\implies\text{traceless part}\subseteq\operatorname{span}\{\Sigma,\hat E^{ij}\}
$$
$$
\text{one-directionality}: (+,+)\cdot(+,+)\ \text{square channel}\mapsto(+,+):\ \text{the same census restricted to}\ \mathcal E_{++}\ [\text{machine}];\qquad
\text{the}\ \neg\text{multiplicativity witness of CT1.11a}(1)\ \text{lies on the commutator channel}\ (\{G_a,G_b\}=0)\ \text{and is reproduced}
$$
$$
(3):\ \log Z_\gamma=-\tfrac\gamma4+\log\bigl(1-d|\delta\rho|^2+O(\delta\rho^3)\bigr)=-\tfrac\gamma4-d|\delta\rho|^2+O(\delta\rho^3)\ [\log(1+u)=u+O(u^2)]
$$
$$
\Delta S_{\mathrm{pair}}=2|\delta\rho|^2\ [\mathrm{L3}(1)];\qquad\tfrac d2=\tfrac{\gamma(8-\gamma)}{16};\qquad\gamma=1:\ d=\tfrac78,\ \tfrac d2=\tfrac7{16}
$$
$$
(4):\ \mathfrak T(K'-K)=\gamma+4\log Z_\gamma\ [\text{Cor L0a}]=\gamma+4\bigl(-\tfrac\gamma4-d|\delta\rho|^2\bigr)+O(\delta\rho^3)=-4d|\delta\rho|^2+O(\delta\rho^3)
$$
$$
-4d=-\tfrac{\gamma(8-\gamma)}2;\qquad-4d|\delta\rho|^2=-2d\,\Delta S_{\mathrm{pair}}=-\tfrac{\gamma(8-\gamma)}4\Delta S_{\mathrm{pair}};\qquad
\gamma=1:\ -\tfrac74\Delta S_{\mathrm{pair}};\qquad\le0\ \text{near the vacuum}\ [\Delta S_{\mathrm{pair}}\ge0,\ \text{zero only at}\ \tfrac14I:\ \mathrm{L1}(1),\ \mathrm{L3}(1)]
$$
$$
(5):\ \text{exact Fraction table}\ [\text{machine}].\ \blacksquare
$$

**Phys.** To second order the tilt does two things: it shrinks the deviation uniformly by $c=1-\tfrac\gamma4$, and it transports the traceless square of the deviation with exact weight $d=\tfrac{\gamma(8-\gamma)}8$ into the $S$-even, $T$-even real block — a quadratic sector flow that lands wholly in $\mathcal E_{++}$ for any single-sector input and stays there under further squaring. At sharp crystallization the transport weight is exactly $\tfrac78$, the partition function reads $-\tfrac14-\tfrac7{16}\Delta S_{\mathrm{pair}}$, and the modular trace deficit reads $-\tfrac74\Delta S_{\mathrm{pair}}$ — one exact rational family with the Lyapunov deficit $\tfrac7{16}$ [L2]. A reading, not an identification.

---

## Closure exports of Part 1 §F (consumed by Part 2)

$$
\begin{array}{lll}
\mathrm{CT0.1}\ \text{dichotomy} & \mathrm{CT0.5}\ D_{\mathrm{tick}}(n)=2^{n+1} & \mathrm{CT1.1}\ (7,3,3,3)\\
\mathrm{CT0.2}\ \rho_\circ,\ \ln4 & \mathrm{CT0.6(a)}\ C_{\mathrm{cap}}=16,\ O(n);\ \delta h\le4\,\delta\tau & \mathrm{CT1.2}\ \text{basis}\ \{E_0,\Sigma,W_i,J_i,K_i,\hat E^{ij}\}\\
\mathrm{CT0.3}\ J^\pm\ \text{increments} & \mathrm{CT0.7}\ \Pi_{\mathcal R},\Pi_{\mathcal V};\ \mathbf F_{(\pm,\cdot)}=\mathcal E_{st} & \mathrm{CT1.3}\text{–}\mathrm{CT1.9}\ \text{closure table};\ \mathfrak u(4)=\mathfrak u(1)\oplus\mathfrak{su}(4)\\
\mathrm{CT0.4}\ \text{real}=\text{registered} & \mathrm{CT0.8}\ 0\le\varepsilon_q<\tfrac14 & \mathrm{CT1.10}\ \mathcal E_{++}=\mathbf1\oplus\mathbf5\oplus\mathbf1\\
\mathrm{CT0.9}\ \Phi=\{0,\pi\};\ 1\ \text{edge}=1\ \text{bit} & \mathrm{CT0.11(a)}\ n\le3;\ \mathbb C^3\ \text{slots};\ \mathrm{CT0.11b}\ n=2d\ \text{(bidirectional)} & \mathrm{CT1.11}\ E_0\nparallel\Sigma\\
\mathrm{CT0.10}\ (P,\pi)\ \text{independent} & \mathrm{CT0.12}\ 3{+}3{+}5{+}3{+}1{+}1=16 & \mathrm{CT0.13}\ \mathcal A(n)\\
\mathrm{CT0.14}\ \dim\mathcal K_n=(6,16,17,25) & &
\end{array}
$$

$\blacksquare$

---

## §G — Master index of results

| Tags | Content | Locus |
| --- | --- | --- |
| A1–A9 · C1–C13 · D0.1–D4.3 · P1–P5 | axioms · conventions · the definition layer · calibration | Part 1 §A–§E |
| CT0.1–CT0.14 (+CT0.6a, CT0.7a, CT0.11a/b) | dichotomy, vacuum, seals, tick load $2^{n+1}$, $C_{\mathrm{cap}}=16$, swap grading, $\varepsilon_q$ range, $\Phi=\{0,\pi\}$, $n\le3$, $\mathcal A(n)$, mask blocks | Part 1 §F |
| CT1.0–CT1.11 (+CT1.11a/b) | signature classification, $(S,T)$ sector decomposition, generator basis, $\mathfrak{su}(2)$ closures, commutator tables, global algebra, involution table, native Clifford frames and the weak-covariance pincer | Part 1 §F |
| L0–L5 (+Cor L0a) | ledger–tilt coupling, tilt modular update, Lyapunov function, decay law $\gamma(8-\gamma)/16$, entropy deficit and the inertial read, patch deficit, second-order sector flow | Part 1 §F |
| CT1.12–CT1.29 (+CT1.12a, CT1.19a/b, CT1.29a) · CT2.1–CT2.11 | metric emergence, conformal rescaling, linearized spin-2, continuum limit, effective action, $T_{\mu\nu}$, field equations, conservation, $\Lambda=D^+$, entropy/calibration, one free scale | Part 2 §C |
| EW.1–EW.36 (+EW.5a, EW.36a) | electroweak: masks, $Q=T_3+Y/2$, abelian $\mathfrak u(1)$, scalar trace mode, rung-3 wrapping, $m_W$, neutral mass matrix, $\theta_W$, $m_W=m_Z\cos\theta_W$, $e=g\sin\theta_W$, spectrum | Part 2 §D |
| EM.1–EM.26 (+EM.9a/b, Def-EM.20–22) | electromagnetic: rung-2 $\mathfrak u(1)$, photon masslessness/polarizations/entropy, end-charge, quantization, conservation, $G(e)$, dynamic per-edge phase, alignment patterns and parity, CPT bridge, spectrum | Part 2 §E |
| CT3.1–CT3.22 (+CT3.10a, CT3.17a, CT3.22a) | colour: $N=3$ forced, $\mathfrak u(3)=\mathfrak{su}(3)\oplus\mathfrak u(1)$, rung-3 algebra, $f_{abc}$, gluons $=8$, masslessness, baryon/meson singlets, sealing grammar, confinement | Part 2 §F |
| CT4.1–CT4.13 (+CT4.1a, CT4.4a, CT4.5a, CT4.7a) | saturation: $O(n)\to D^-$, absorbing lock, $w_{D^-}$, dark contrast, entropy triangle, bounds, global closure, falsifiers, audit | Part 2 §G |
| Def-H.1–Def-H.43 · FT.1–FT.145 (structural) · FT.153–FT.155 | the fermion layer: measurement primitives, the fermion definition, floors, spin/stability, flicker, spectra, Clifford/branches, path integrals, family channels, carrier/parity, rung one; the interface definitions and their derived interface theorems | Part 3 |
| Def-BM.1–2 · BM.1–BM.6 | colour-sealed composites: baryons/mesons, junction grammar, observability, the forced family group, invariance laws, census consumption, construction specs | Part 4 |
| the 25 Category-B cells | the computed data cells and their consumption block | Census |

$\blacksquare$
