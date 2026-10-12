# $\langle qu(b(i(t|t))ick)\rangle$ — **Part 2 · Bosonic\_era** — Geometry · Electroweak · Electromagnetic · Colour · Saturation

**Dep.** Part 1 (axioms A1–A9, conventions C1–C13, the definition layer D0.1–D4.3, calibration P1–P5, pair canon CT0.*/CT1.1–CT1.11b, ledger dynamics L0–L5) — cited by tag at use. Format: Part 1 §0.4.
**Namespace.** This part owns: §C geometry CT1.12–CT1.29a, CT2.1–CT2.11; §D electroweak EW.1–EW.36a; §E electromagnetic EM.1–EM.26, Def-EM.20–Def-EM.22; §F colour CT3.1–CT3.22a; §G saturation CT4.1–CT4.13; §Cal-2 (the bosonic registry note). The definition layer (D2.1–D4.3) and the master symbol table are Part 1 §C–§D; section letters §C–§G preserve the classical canon's file letters.
**DAG law.** Citations resolve to Part 1, to earlier tags of this part, or to marked forward pointers (restatements at use; corroboration-only rows). No citation of Parts 3–4.
**Internal section dependencies.** §C depends on Part 1 §F (and on Part 1 §C's Tier 2–4 definitions). §D depends on §C. §E depends on §C, §D (EM.18 alone, restated at use). §F depends on Part 1 §F and §C; its two borrowed electroweak/EM results (colour masslessness EW.26, coefficient stability EM.18) are restated with full arguments at use, so §F may be read before §D, §E. §G depends on Part 1 §F, §C, §D (EW.27), §F.

---

## §Cal-2 — Calibration note (bosonic era)

The P4 core ($g,\ g';\ h_0;\ c_W;\ \Lambda;\ \varkappa,\ \beta,\ \alpha_\Omega$) and P3 ($G_N$, $\kappa^2$ — named combinations of $\mathfrak h$) are Part 1 §E. Logged spectral datum of this part: $\alpha_{\mathrm{EM}}^{(2)}$ — the EM-block scale read [EM.17]: operatorially defined; no theorem of the corpus fixes its numerical value under the dynamic-phase regime [EM.25(8)]; it is a spectral datum of $\mathbf F$ at the solution level, $\neg$a fitted constant and $\neg$a P4 core member; no result consumes its value — every edge-level phase read uses the registration data $\alpha_e\in\{0,\pi\}$ [Def-EM.20, EM.20]. Any future use that needs a value requires a logged declaration first.

---

## §C — Geometry: Emergent Metric, Masks, Field Equations, Calibration

*Dep.: Part 1 (§A–§F). Notation: $\hat h_{ij}$ — spatial traceless shear (D2.1); $\hat h^{(4)}_{\mu\nu}$ — 4-dim $\eta$-traceless perturbation (CT1.18) — distinct symbols. Machine: `checks/verify_C.py` (exact rational jet calculus; linearization via truncated series); CT1.29a: `checks/verify_merge_tierA.py`; CT1.19b/CT1.29: `checks/verify_promotion_*`.*

## §C.I — Emergent Metric Geometry

### CT1.12 — Metric emergence from sector components

**Thm.** With D2.1 data $\bigl(a_{00},q_{ij},w_i\bigr)\in\mathcal E_{++}\oplus\mathcal E_{+-}$:
$$
\delta^{ij}\hat h_{ij}=0;\qquad \Omega=e^{\alpha_\Omega a_{00}}>0\ \ \forall a_{00}\in\mathbb R;\qquad
\bar g_{ij}\succ0\iff\forall a:\ 1+\varkappa\lambda_a(q)>0\quad(\Leftarrow\ \varkappa>0\wedge\varkappa\|q\|_{\mathrm{op}}<1);
$$
$$
\bar g_{ij}\succ0\implies\operatorname{sig}(\bar g_{\mu\nu})=\operatorname{sig}(g_{\mu\nu})=(-,+,+,+);
$$
$$
\begin{array}{c|c|c}
\text{sector object} & \# & \text{metric role}\\ \hline
a_{00} & 1 & \text{conformal factor}\ \Omega\\
\Sigma_{\mathrm{tr}} & 1 & \text{spatial volume mode}\\
\hat h_{ij} & 5 & \text{spin-2 shear}\\
w_i & 3 & \text{shift}\ N_i=\beta w_i\\ \hline
\text{total} & 10 & \#\{g_{\mu\nu}=g_{\nu\mu}\}=\tfrac{4\cdot5}{2}
\end{array}
$$

**Req.** A3; D2.1; CT1.1, CT1.10; Schur identity $\det\begin{pmatrix}A&B\\ C&D\end{pmatrix}=\det D\cdot\det(A-BD^{-1}C)$, Sylvester criterion [linear algebra].

**Pf.**
$$
\dim\mathcal E_{++}=7=1\oplus5\oplus1\ \text{with coefficients}\ (a_{00},\hat h_{ij},\Sigma_{\mathrm{tr}})\ [\mathrm{CT1.1},\mathrm{CT1.10}];\qquad
\dim\mathcal E_{+-}=3\ \text{with coefficients}\ w_i\ [\mathrm{CT1.1}]
$$
$$
7+3=10=\tfrac{4\cdot5}{2}\implies\text{dictionary is a bijection}
$$
$$
\delta^{ij}\hat h_{ij}=\delta^{ij}q_{ij}-\tfrac13\delta^{ij}\delta_{ij}\Sigma_{\mathrm{tr}}=\Sigma_{\mathrm{tr}}-\tfrac13\cdot3\cdot\Sigma_{\mathrm{tr}}=0\ [\mathrm{D2.1}];\qquad
q_{ij}=\hat h_{ij}+\tfrac13\delta_{ij}\Sigma_{\mathrm{tr}}\ \text{unique (trace functional)}
$$
$$
a_{00}\in\mathbb R\implies\Omega=e^{\alpha_\Omega a_{00}}>0\implies\Omega^2>0
$$
$$
\bar g=\begin{pmatrix}-1&\varkappa N_j\\ \varkappa N_i&\bar g_{ij}\end{pmatrix}:\quad
\det\bar g=\det(\bar g_{ij})\cdot\bigl(-1-\varkappa^2N_i(\bar g^{-1})^{ij}N_j\bigr)\quad[\text{Schur}]
$$
$$
\bar g_{ij}\succ0\implies\det(\bar g_{ij})>0\ \wedge\ (\bar g^{-1})^{ij}\succ0\implies N(\bar g^{-1})N\ge0\implies(\cdot)\le-1<0\implies\det\bar g<0
$$
$$
\bar g_{ij}\succ0:\ 3\ \text{positive directions};\quad\det\bar g<0:\ \text{4th eigenvalue}<0\implies\operatorname{sig}(\bar g)=(-,+,+,+)
$$
$$
\bar g_{ij}=\delta_{ij}+\varkappa q_{ij}:\ \operatorname{spec}=\{1+\varkappa\lambda_a(q)\}\implies\succ0\iff\forall a:\ 1+\varkappa\lambda_a>0
$$
$$
g_{\mu\nu}=\Omega^2\bar g_{\mu\nu},\ \Omega^2>0:\ \operatorname{spec}(g)=\Omega^2\operatorname{spec}(\bar g)\implies\operatorname{sig}(g)=(-,+,+,+).\ \blacksquare
$$

**Rmk (scale hygiene).** $\varkappa$: embedding scale (D2.1, C4); $\ \varkappa\ne\kappa$ (CT2.9); $\ [\varkappa]=[q]^{-1}$; $\neg\exists$ assumed relation $\varkappa\sim\kappa$.

**Phys.** The ten real sector coefficients of a pair — conformal amplitude, spatial trace, five traceless shears, three shifts — are exactly the ten components of a Lorentzian metric in conformal gauge. Gravity is not added to the theory: the metric is a repackaging of the $S$-even operator content, with signature $(-,+,+,+)$ guaranteed in the perturbative regime $\varkappa\|q\|_{\mathrm{op}}<1$.

---

### CT1.12a — The pair-channel audit of the metric dictionary: tiling, block split, and the three discrete read classes

**Thm.** $(1)$ **Tiling.** The $16$ pair-channel registers [CT0.6] tile by aspects:
$$(G_5+W_3+H_1)+(J^+_3+J^-_3)+D^+_1=16\qquad[\mathrm{CT0.12},\ \mathrm{CT1.1},\ \mathrm{CT1.2}]$$
matching the $(S,T)$ block decomposition $7+3+3+3$ [CT1.1] under the dictionary $(G,H,D^+)\leftrightarrow\mathcal E_{++}$, $W\leftrightarrow\mathcal E_{+-}$, $J^+\leftrightarrow\mathcal E_{-+}$, $J^-\leftrightarrow\mathcal E_{--}$ [CT0.12; CT1.11a(0)].
$(2)$ **Block split of the dictionary.** CT1.12's dictionary rows decompose as
$$g_{\mu\nu}\ \leftrightarrow\ \hat h_{ij}\ (5,\ G:\ \text{spin-2 shear})\ \oplus\ \Sigma_{\mathrm{tr}}\ (1,\ H:\ \text{volume mode})\ \oplus\ a_{00}\ (1,\ D^+:\ \Omega\ \text{conformal})\ \oplus\ w_i\ (3,\ W:\ \text{shift}),\qquad 1+1+5+3=10=\tfrac{4\cdot5}{2}$$
every carrier $S$-even [$\mathcal E_{++},\mathcal E_{+-}$ are $S$-even: CT1.1, CT1.2, C3; CT1.12's data live in $\mathcal E_{++}\oplus\mathcal E_{+-}$]; the $S$-odd blocks ($J^\pm$) carry **zero** metric coordinates. Consequence: $g_{\mu\nu}$ is orientation-even (used in CT1.19b(2)).
$(3)$ **Read classes.** The corpus's discrete reads fall into exactly three classes, one per discreteness route: **(R1)** binary registration — $\sigma_e$ [CT0.9], $q_{\mathrm{EM}}\in\{-1,0,+1\}$ [EM.9, D3.4], wall parity $(-1)^{\aleph}$ [$\aleph_v$ from D3.3's $f_v$]; **(R2)** integer winding on materialized closed chains — $\kappa,\Theta,k$ [CT1.19b]; **(R3)** binary singlet admissibility — $\mathcal C\in\{0,1\}$ [D2.14; confinement semantics CT3.22a]. Every further dictionary/aspect datum is either continuous configuration data [P4: $g,g',h_0,c_W,\Lambda,\varkappa,\beta,\alpha_\Omega$] or structural non-observable (per-aspect observability verdicts: audit-layer record — not re-derived here); neither carries an independent quantum.

**Req.** A8; D2.1, D2.14, D3.3; P4; CT0.6, CT0.9, CT0.12, CT1.11a (Part 1); CT1.1, CT1.2, CT1.12; EM.9 (**E**; forward pointer — C DAG note); exact arithmetic [math; machine: `checks/verify_merge_tierB.py` §C].

**Pf.**
$$(1):\ \mathrm{CT0.12}'\text{s rows}:\ 3{+}3{+}5{+}3{+}1{+}1=16=C_{\mathrm{cap}}\ [\mathrm{CT0.6}];\qquad \text{regrouped by CT1.2's parity table}:\ (5{+}1{+}1){+}3{+}3{+}3=(7,3,3,3)\ [\mathrm{CT1.1}]$$
$$(2):\ \mathrm{CT1.12}'\text{s row list}\ (a_{00},\Sigma_{\mathrm{tr}},\hat h_{ij},w_i)\ \text{with counts}\ 1{+}1{+}5{+}3=10=\#\{g_{\mu\nu}=g_{\nu\mu}\};\quad \text{carriers}:\ a_{00}\sim E_0,\ \Sigma_{\mathrm{tr}}\sim\Sigma,\ \hat h\subset\operatorname{span}\{\hat E^{ij}\},\ w\sim W_i\ \text{all}\ S\text{-even}\ [\mathrm{CT1.2};\ \text{machine}]$$
$$J_i\in\mathcal E_{-+},\ K_i\in\mathcal E_{--}\ [\mathrm{CT1.2}]:\ S\text{-odd}\implies\neg\text{rows of an}\ S\text{-even dictionary}$$
$$(3):\ \text{enumeration of the declared discrete reads}:\ \mathrm{CT0.9}\ (\sigma\ \text{binary}),\ \mathrm{EM.9}/\mathrm{D3.4}\ (\text{ternary from two binaries}),\ \mathrm{D3.3}\ (\aleph_v=|f_v|\ \text{from signs}),\ \mathrm{CT1.19b}\ (\kappa,\Theta,k\ \text{integers on-shell}),\ \mathrm{D2.14}\ (\mathcal C\in\{0,1\});\quad \text{continuous residue}=\mathrm{P4}'\text{s list verbatim}.\ \blacksquare$$

**Phys.** The metric speaks only the swap-even dialect: all ten coordinates of spacetime geometry live in the gravity$+$Higgs$+$dark and weak blocks, and the Janus blocks contribute nothing to $g_{\mu\nu}$. Auditing the whole pair channel leaves exactly three routes to discreteness — registration bits, winding integers, sealing booleans — and everything else is continuous configuration data or structure. This is the census of what can be a "quantum" in this corpus.

---

### CT1.13 — Christoffel symbols under conformal rescaling

**Thm.** $\ g_{\mu\nu}=\Omega^2\bar g_{\mu\nu},\ \Upsilon=\ln\Omega\implies$
$$
g^{\mu\nu}=\Omega^{-2}\bar g^{\mu\nu};\qquad
\Gamma^\lambda{}_{\mu\nu}=\bar\Gamma^\lambda{}_{\mu\nu}+\delta^\lambda{}_\mu\bar\nabla_\nu\Upsilon+\delta^\lambda{}_\nu\bar\nabla_\mu\Upsilon-\bar g_{\mu\nu}\bar g^{\lambda\rho}\bar\nabla_\rho\Upsilon .
$$

**Req.** D2.1, D2.2; Levi-Civita formula $\Gamma^\lambda{}_{\mu\nu}=\tfrac12g^{\lambda\rho}(\partial_\mu g_{\rho\nu}+\partial_\nu g_{\rho\mu}-\partial_\rho g_{\mu\nu})$ [math].

**Pf.**
$$
g^{\mu\alpha}g_{\alpha\nu}=\Omega^{-2}\Omega^2\delta^\mu{}_\nu\implies g^{\mu\nu}=\Omega^{-2}\bar g^{\mu\nu}
$$
$$
\partial_\rho g_{\mu\nu}=2\Omega(\partial_\rho\Omega)\bar g_{\mu\nu}+\Omega^2\partial_\rho\bar g_{\mu\nu}=\Omega^2\bigl(2\Upsilon_\rho\bar g_{\mu\nu}+\partial_\rho\bar g_{\mu\nu}\bigr),\qquad\Upsilon_\rho=\partial_\rho\Omega/\Omega\ [\mathrm{D2.2}]
$$
$$
\Gamma^\lambda{}_{\mu\nu}=\tfrac12\Omega^{-2}\bar g^{\lambda\rho}\Omega^2\bigl[(\partial_\mu\bar g_{\rho\nu}+2\bar g_{\rho\nu}\Upsilon_\mu)+(\partial_\nu\bar g_{\rho\mu}+2\bar g_{\rho\mu}\Upsilon_\nu)-(\partial_\rho\bar g_{\mu\nu}+2\bar g_{\mu\nu}\Upsilon_\rho)\bigr]
$$
$$
=\bar\Gamma^\lambda{}_{\mu\nu}+\tfrac12\bar g^{\lambda\rho}\bigl(2\bar g_{\rho\nu}\Upsilon_\mu+2\bar g_{\rho\mu}\Upsilon_\nu-2\bar g_{\mu\nu}\Upsilon_\rho\bigr)
=\bar\Gamma^\lambda{}_{\mu\nu}+\delta^\lambda{}_\nu\Upsilon_\mu+\delta^\lambda{}_\mu\Upsilon_\nu-\bar g_{\mu\nu}\bar g^{\lambda\rho}\Upsilon_\rho
$$
$$
\Upsilon\ \text{scalar}\implies\Upsilon_\mu=\partial_\mu\Upsilon=\bar\nabla_\mu\Upsilon;\qquad\text{RHS symmetric in}\ \mu\leftrightarrow\nu.\ \blacksquare
$$

**Phys.** A conformal change of the metric shifts the connection by first derivatives of the conformal potential only. This single formula generates the whole curvature-transfer chain CT1.14–CT1.17 that relates emergent geometry to its auxiliary background.

---

### CT1.14 — Riemann tensor under conformal rescaling

**Thm.** With $\ C^\rho{}_{\mu\nu}:=\Gamma^\rho{}_{\mu\nu}-\bar\Gamma^\rho{}_{\mu\nu}=\delta^\rho{}_\mu\Upsilon_\nu+\delta^\rho{}_\nu\Upsilon_\mu-\bar g_{\mu\nu}\Upsilon^\rho$ (tensor; $\Upsilon^\rho:=\bar g^{\rho\sigma}\Upsilon_\sigma$):
$$
R^\rho{}_{\sigma\mu\nu}=\bar R^\rho{}_{\sigma\mu\nu}+2\bar\nabla_{[\mu}C^\rho{}_{\nu]\sigma}+2C^\rho{}_{[\mu|\lambda|}C^\lambda{}_{\nu]\sigma}.
$$

**Req.** CT1.13; Riemann definition $R^\rho{}_{\sigma\mu\nu}=\partial_\mu\Gamma^\rho{}_{\nu\sigma}-\partial_\nu\Gamma^\rho{}_{\mu\sigma}+\Gamma^\rho{}_{\mu\lambda}\Gamma^\lambda{}_{\nu\sigma}-\Gamma^\rho{}_{\nu\lambda}\Gamma^\lambda{}_{\mu\sigma}$; $\bar\nabla$ of a $(1,2)$-tensor [math].

**Pf.**
$$
C=\Gamma-\bar\Gamma:\ \text{difference of connections}\implies\text{tensor};\qquad\text{explicit form}=\mathrm{CT1.13}
$$
$$
\Gamma=\bar\Gamma+C\ \text{substituted into the definition}:\quad
O(C^0):\ \bar R^\rho{}_{\sigma\mu\nu}
$$
$$
O(C^1):\ \ \partial_\mu C^\rho{}_{\nu\sigma}-\partial_\nu C^\rho{}_{\mu\sigma}+\bar\Gamma^\rho{}_{\mu\lambda}C^\lambda{}_{\nu\sigma}+C^\rho{}_{\mu\lambda}\bar\Gamma^\lambda{}_{\nu\sigma}-\bar\Gamma^\rho{}_{\nu\lambda}C^\lambda{}_{\mu\sigma}-C^\rho{}_{\nu\lambda}\bar\Gamma^\lambda{}_{\mu\sigma}
$$
$$
-\bar\Gamma^\lambda{}_{\mu\nu}C^\rho{}_{\lambda\sigma}\ \text{cancels between the antisymmetrized halves}\ (\bar\Gamma^\lambda{}_{\mu\nu}=\bar\Gamma^\lambda{}_{\nu\mu})\implies O(C^1)=2\bar\nabla_{[\mu}C^\rho{}_{\nu]\sigma}
$$
$$
O(C^2):\ \ C^\rho{}_{\mu\lambda}C^\lambda{}_{\nu\sigma}-C^\rho{}_{\nu\lambda}C^\lambda{}_{\mu\sigma}=2C^\rho{}_{[\mu|\lambda|}C^\lambda{}_{\nu]\sigma}\quad(\lambda\ \text{excluded from antisymmetrization}).\ \blacksquare
$$

**Phys.** The curvature of the emergent metric differs from the background by a term linear in covariant derivatives of the conformal potential and a term quadratic in it — an exact, closed bookkeeping of how conformal (volume) data manufactures curvature.

---

### CT1.15 — Ricci tensor under conformal rescaling

**Thm.** In $D$ dimensions:
$$
R_{\mu\nu}=\bar R_{\mu\nu}-(D-2)\bar\nabla_\mu\bar\nabla_\nu\Upsilon-\bar g_{\mu\nu}\bar\Box\Upsilon+(D-2)\bigl(\Upsilon_\mu\Upsilon_\nu-\bar g_{\mu\nu}|\bar\nabla\Upsilon|^2\bigr).
$$

**Req.** CT1.14; $\bar\nabla_\mu\Upsilon_\nu=\bar\nabla_\nu\Upsilon_\mu$, $\bar\nabla\bar g=0$ [math].

**Pf.**
$$
\mathrm{CT1.14}\ \text{contracted}\ \rho=\mu:\quad
R_{\sigma\nu}=\bar R_{\sigma\nu}+\bar\nabla_\mu C^\mu{}_{\nu\sigma}-\bar\nabla_\nu C^\mu{}_{\mu\sigma}+C^\mu{}_{\mu\lambda}C^\lambda{}_{\nu\sigma}-C^\mu{}_{\nu\lambda}C^\lambda{}_{\mu\sigma}
$$
$$
C^\mu{}_{\mu\sigma}=\Upsilon_\sigma+D\,\Upsilon_\sigma-\Upsilon_\sigma=D\,\Upsilon_\sigma
$$
$$
\bar\nabla_\mu C^\mu{}_{\nu\sigma}=\bar\nabla_\nu\Upsilon_\sigma+\bar\nabla_\sigma\Upsilon_\nu-\bar g_{\nu\sigma}\bar\Box\Upsilon;\qquad
\bar\nabla_\nu C^\mu{}_{\mu\sigma}=D\,\bar\nabla_\nu\Upsilon_\sigma
$$
$$
\bar\nabla_\nu\Upsilon_\sigma=\bar\nabla_\sigma\Upsilon_\nu\implies\text{derivative part}=-(D-2)\bar\nabla_\nu\Upsilon_\sigma-\bar g_{\nu\sigma}\bar\Box\Upsilon
$$
$$
C^\mu{}_{\mu\lambda}C^\lambda{}_{\nu\sigma}=D\,\Upsilon_\lambda\bigl(\delta^\lambda{}_\nu\Upsilon_\sigma+\delta^\lambda{}_\sigma\Upsilon_\nu-\bar g_{\nu\sigma}\Upsilon^\lambda\bigr)=D\bigl(2\Upsilon_\nu\Upsilon_\sigma-\bar g_{\nu\sigma}|\bar\nabla\Upsilon|^2\bigr)
$$
$$
C^\mu{}_{\nu\lambda}C^\lambda{}_{\mu\sigma}=(D+2)\,\Upsilon_\nu\Upsilon_\sigma-2\,\bar g_{\nu\sigma}|\bar\nabla\Upsilon|^2\quad[\text{9 products; coefficients}\ 1{+}1{+}D{+}1{-}1{-}1{+}1{=}D{+}2;\ {-}1{-}1{=}{-}2]
$$
$$
\text{quadratic difference}=(D-2)\bigl(\Upsilon_\nu\Upsilon_\sigma-\bar g_{\nu\sigma}|\bar\nabla\Upsilon|^2\bigr);\qquad
+\bar R_{\sigma\nu},\ \text{rename}\implies\text{Thm}.\ \blacksquare
$$

**Phys.** The exact response of Ricci curvature to the conformal factor in any dimension. The $(D-2)$ coefficients are what makes $D=4$ (the arena fixed by CT1.12/CT2.6) the non-degenerate case; the identity feeds directly the Einstein-tensor law CT1.17.

---

### CT1.16 — Ricci scalar under conformal rescaling

**Thm.**
$$
R=\Omega^{-2}\Bigl[\bar R-2(D-1)\bar\Box\Upsilon-(D-1)(D-2)|\bar\nabla\Upsilon|^2\Bigr];\qquad
D=4:\quad R=\Omega^{-2}\Bigl[\bar R-6\bar\Box\Upsilon-6|\bar\nabla\Upsilon|^2\Bigr].
$$

**Req.** CT1.13 ($g^{\mu\nu}=\Omega^{-2}\bar g^{\mu\nu}$), CT1.15; $\bar g^{\mu\nu}\bar g_{\mu\nu}=D$ [math].

**Pf.**
$$
R=g^{\mu\nu}R_{\mu\nu}=\Omega^{-2}\bar g^{\mu\nu}R_{\mu\nu}\quad[\mathrm{CT1.13}]
$$
$$
\bar g^{\mu\nu}R_{\mu\nu}=\bar R-(D-2)\bar\Box\Upsilon-D\,\bar\Box\Upsilon+(D-2)|\bar\nabla\Upsilon|^2-D(D-2)|\bar\nabla\Upsilon|^2\quad[\mathrm{CT1.15}]
$$
$$
-(D-2)-D=-2(D-1);\qquad(D-2)-D(D-2)=-(D-1)(D-2)
$$
$$
\times\,\Omega^{-2};\qquad D=4:\ 2(D-1)=6=(D-1)(D-2).\ \blacksquare
$$

**Phys.** The scalar curvature transforms with the standard conformal weights; in $D=4$ the bracket $\bar R-6\bar\Box\Upsilon-6|\bar\nabla\Upsilon|^2$ is what multiplies $\Omega^{-2}$ — the input that makes the Einstein tensor law CT1.17 collapse to four terms.

---

### CT1.17 — Einstein tensor under conformal rescaling in $D=4$

**Thm.**
$$
G_{\mu\nu}=\bar G_{\mu\nu}-2\bar\nabla_\mu\bar\nabla_\nu\Upsilon+2\bar g_{\mu\nu}\bar\Box\Upsilon+2\Upsilon_\mu\Upsilon_\nu+\bar g_{\mu\nu}|\bar\nabla\Upsilon|^2 .
$$

**Req.** CT1.15, CT1.16 ($D=4$); $G_{\mu\nu}:=R_{\mu\nu}-\tfrac12g_{\mu\nu}R$ [math].

**Pf.**
$$
R_{\mu\nu}=\bar R_{\mu\nu}-2\bar\nabla_\mu\bar\nabla_\nu\Upsilon-\bar g_{\mu\nu}\bar\Box\Upsilon+2\Upsilon_\mu\Upsilon_\nu-2\bar g_{\mu\nu}|\bar\nabla\Upsilon|^2\quad[\mathrm{CT1.15},\ D=4]
$$
$$
\tfrac12g_{\mu\nu}R=\tfrac12\Omega^2\bar g_{\mu\nu}\cdot\Omega^{-2}\bigl[\bar R-6\bar\Box\Upsilon-6|\bar\nabla\Upsilon|^2\bigr]=\tfrac12\bar g_{\mu\nu}\bigl[\bar R-6\bar\Box\Upsilon-6|\bar\nabla\Upsilon|^2\bigr]\quad[\mathrm{CT1.16}]
$$
$$
G_{\mu\nu}=\underbrace{\bigl(\bar R_{\mu\nu}-\tfrac12\bar g_{\mu\nu}\bar R\bigr)}_{\bar G_{\mu\nu}}+(-1+3)\,\bar g_{\mu\nu}\bar\Box\Upsilon+(-2+3)\,\bar g_{\mu\nu}|\bar\nabla\Upsilon|^2-2\bar\nabla_\mu\bar\nabla_\nu\Upsilon+2\Upsilon_\mu\Upsilon_\nu.\ \blacksquare
$$

**Phys.** The exact transformation law of the Einstein tensor in the emergent conformal gauge: everything beyond the background Einstein tensor is built from the single field $\Upsilon=\ln\Omega$. The conformal (volume) degree of freedom of the pair algebra gravitates through a closed-form correction — no approximation involved.

---

### CT1.18 — Linearized spin-2 operator

**Thm.** $\ \bar g_{\mu\nu}=\eta_{\mu\nu}+\varkappa\hat h^{(4)}_{\mu\nu}$, $\ \eta^{\mu\nu}\hat h^{(4)}_{\mu\nu}=0$ (as a field), $\ \Upsilon=N_i=\Sigma_{\mathrm{tr}}=0$. To $O(\varkappa)$:
$$
\bar G_{\mu\nu}=\frac{\varkappa}{2}\Bigl[-\Box\hat h^{(4)}_{\mu\nu}+\partial_\mu\partial^\lambda\hat h^{(4)}_{\nu\lambda}+\partial_\nu\partial^\lambda\hat h^{(4)}_{\mu\lambda}-\eta_{\mu\nu}\partial^\lambda\partial^\sigma\hat h^{(4)}_{\lambda\sigma}\Bigr]+O(\varkappa^2),\qquad\Box=\eta^{\alpha\beta}\partial_\alpha\partial_\beta .
$$
With the full linearized Einstein tensor (general $h$)
$$
\bar G^{(1)}[h]_{\mu\nu}:=\tfrac12\Bigl[-\Box h_{\mu\nu}-\partial_\mu\partial_\nu h^\lambda{}_\lambda+\partial_\mu\partial^\lambda h_{\nu\lambda}+\partial_\nu\partial^\lambda h_{\mu\lambda}+\eta_{\mu\nu}\bigl(\Box h^\lambda{}_\lambda-\partial^\lambda\partial^\sigma h_{\lambda\sigma}\bigr)\Bigr]:
$$
$$
h^\lambda{}_\lambda=0\implies\bar G^{(1)}[h]=\text{bracket above}/2;\qquad
\bar G^{(1)}\bigl[h+\partial_\mu\xi_\nu+\partial_\nu\xi_\mu\bigr]=\bar G^{(1)}[h]\ \ \forall\xi;
$$
$$
\partial^\lambda\hat h^{(4)}_{\lambda\nu}=0\ \wedge\ \hat h^{(4)\lambda}{}_\lambda=0\implies\bar G^{(1)}[\hat h^{(4)}]=-\tfrac12\Box\hat h^{(4)}_{\mu\nu}\quad(\text{massless wave operator}).
$$

**Req.** CT1.10 (spin-2 mode), CT1.12; Levi-Civita/Ricci expansion [math]; $\partial_\mu\partial_\nu=\partial_\nu\partial_\mu$.

**Pf.**
$$
\bar g^{\lambda\rho}=\eta^{\lambda\rho}-\varkappa\hat h^{(4)\lambda\rho}+O(\varkappa^2)\implies
\bar\Gamma^\lambda{}_{\mu\nu}=\tfrac\varkappa2\bigl(\partial_\mu\hat h^{(4)\lambda}{}_\nu+\partial_\nu\hat h^{(4)\lambda}{}_\mu-\partial^\lambda\hat h^{(4)}_{\mu\nu}\bigr)+O(\varkappa^2)\quad(\eta\text{-raising})
$$
$$
\bar R_{\mu\nu}=\partial_\lambda\bar\Gamma^\lambda{}_{\mu\nu}-\partial_\nu\bar\Gamma^\lambda{}_{\lambda\mu}+O(\varkappa^2)=\tfrac\varkappa2\bigl(\partial_\mu\partial^\lambda\hat h^{(4)}_{\lambda\nu}+\partial_\nu\partial^\lambda\hat h^{(4)}_{\lambda\mu}-\Box\hat h^{(4)}_{\mu\nu}-\partial_\mu\partial_\nu\hat h^{(4)\lambda}{}_\lambda\bigr)
$$
$$
\hat h^{(4)\lambda}{}_\lambda\equiv0\ \text{(field)}\implies\partial_\mu\partial_\nu\hat h^{(4)\lambda}{}_\lambda=0
$$
$$
\bar R=\eta^{\mu\nu}\bar R_{\mu\nu}=\varkappa\bigl(\partial^\mu\partial^\nu\hat h^{(4)}_{\mu\nu}-\Box\hat h^{(4)\lambda}{}_\lambda\bigr)=\varkappa\,\partial^\lambda\partial^\sigma\hat h^{(4)}_{\lambda\sigma}
$$
$$
\bar G_{\mu\nu}=\bar R_{\mu\nu}-\tfrac12\eta_{\mu\nu}\bar R+O(\varkappa^2)\implies\text{Thm formula}
$$
$$
\bar G^{(1)}[h+\partial\xi+\partial\xi]-\bar G^{(1)}[h]:\ \xi\text{-terms}=\text{combinations of}\ \partial_{(\alpha}\partial_\beta\partial_{\gamma)}\xi_\delta=0\implies\text{invariance}
$$
$$
\partial^\lambda\hat h^{(4)}_{\lambda\nu}=0\implies\partial_\mu\partial^\lambda\hat h^{(4)}_{\nu\lambda}=\partial_\nu\partial^\lambda\hat h^{(4)}_{\mu\lambda}=\partial^\lambda\partial^\sigma\hat h^{(4)}_{\lambda\sigma}=0\implies\bar G^{(1)}[\hat h^{(4)}]=-\tfrac12\Box\hat h^{(4)}_{\mu\nu}.\ \blacksquare
$$
Machine verification (incl. $\bar G^{(0)}=0$, $\bar G^{(1)}=L[\hat h^{(4)}]$ from the full nonlinear pipeline, gauge invariance): `checks/verify_C.py`.

**Rmk (correction).** The traceless-projected transformation $\hat h^{(4)}\mapsto\hat h^{(4)}+\partial_\mu\xi_\nu+\partial_\nu\xi_\mu-\tfrac12\eta_{\mu\nu}\partial\!\cdot\!\xi$ preserves $\eta^{\mu\nu}\hat h^{(4)}_{\mu\nu}=0$ but shifts $\bar G^{(1)}$ by $\tfrac12\bigl(\partial_\mu\partial_\nu-\eta_{\mu\nu}\Box\bigr)\partial\!\cdot\!\xi\ne0$ (machine-verified): gauge invariance holds for the standard linearized diffeomorphism $\partial_\mu\xi_\nu+\partial_\nu\xi_\mu$, which does not preserve tracelessness and need not, since $\bar G^{(1)}$ is defined for general $h$. The prior codex claimed invariance of the projected form — false as stated.

**Phys.** With only the five-component traceless shear excited, the emergent Einstein tensor reduces at leading order to the massless spin-2 wave operator in transverse gauge. The graviton of the corpus is the $\mathcal E_{++}$ quintet of CT1.10 propagating on the auxiliary background; its gauge freedom is linearized diffeomorphism invariance.

---

## §C.II — Masks, Manifold, and Closure

### CT2.1 — Unit and dimension conventions

**Thm.** With $c=\hbar=k_B=1$, $[\mathfrak h]=\mathfrak q^{-1/2}$:
$$
[\text{length}]=\mathfrak q^{-1/2};\quad[\text{area}]=\mathfrak q^{-1};\quad[\text{energy}]=\mathfrak q^{+1/2};\quad[T_{\mu\nu}]=\mathfrak q^{+2};\quad[G_{\mu\nu}]=[\Lambda]=\mathfrak q^{+1};\quad[\kappa^2]=[G_N]=\mathfrak q^{-1};\quad[\kappa]=\mathfrak q^{-1/2};\quad[S_{\mathrm{geom}}]=\mathfrak q^{0},
$$
and every equation of Parts III–IV balances.

**Req.** D0.6, D2.9; dimensional bookkeeping [math].

**Rmk (forward pointers, non-load-bearing).** The normalization of $\kappa$ is cross-checked against CT1.23 and $G_N\propto\kappa^2$ against CT2.9 — consistency pointers only.

**Pf.**
$$
[\mathfrak h]=\mathfrak q^{-1/2}\ [\mathrm{D0.6},\mathrm{D2.9}]\implies[\text{length}]=\mathfrak q^{-1/2},\ [\text{area}]=\mathfrak q^{-1};\qquad\hbar=c=1\implies[\text{energy}]=[\text{length}]^{-1}=\mathfrak q^{+1/2}
$$
$$
[\text{curvature}]=[\text{area}]^{-1}=\mathfrak q^{+1}=[G_{\mu\nu}];\qquad\Lambda g_{\mu\nu}\sim G_{\mu\nu}\implies[\Lambda]=\mathfrak q^{+1}
$$
$$
[T_{\mu\nu}]=\frac{[\text{energy}]}{[\text{volume}]}=\frac{\mathfrak q^{1/2}}{\mathfrak q^{-3/2}}=\mathfrak q^{+2}
$$
$$
[\kappa^2T_{\mu\nu}]=[G_{\mu\nu}]\ [\mathrm{CT1.23}]\implies[\kappa^2]=\mathfrak q^{1-2}=\mathfrak q^{-1},\ [\kappa]=\mathfrak q^{-1/2};\qquad G_N\propto\kappa^2\ [\mathrm{CT2.9}]\implies[G_N]=\mathfrak q^{-1}
$$
$$
[d^4x]=\mathfrak q^{-2},\ [\sqrt{-g}]=\mathfrak q^0,\ [R]=\mathfrak q^{+1},\ [\kappa^{-2}]=\mathfrak q^{+1}\implies[S_{\mathrm{geom}}]=\mathfrak q^0\ (\hbar=1).\ \blacksquare
$$

**Phys.** One information unit $\mathfrak q$ grades the entire continuum layer: lengths $\mathfrak q^{-1/2}$, curvature and $\Lambda$ at $\mathfrak q^{+1}$, stress at $\mathfrak q^{+2}$, Newton’s constant an area $\mathfrak q^{-1}$. The dimensionless action confirms no dimensionful quantity beyond $\mathfrak h$ has been smuggled in.

---

### CT2.2 — The rung mask is a projection

**Thm.**
$$
\bigl(\mathcal P_M^{(n)}\bigr)^2=\mathcal P_M^{(n)}=\bigl(\mathcal P_M^{(n)}\bigr)^\dagger;\qquad
\operatorname{Im}\mathcal P_M^{(n)}=\mathcal K_n;\qquad
\mathfrak T\,\mathcal P_M^{(n)}=\dim\mathcal K_n\in\{6,16,17,25,\dots\}.
$$

**Req.** D2.3; CT0.13, CT0.14 (Part 1); orthogonal-projection facts [linear algebra].

**Pf.**
$$
\mathrm{D2.3}:\ \mathcal P_M^{(n)}=\text{orthogonal projection}\ \mathcal K\to\mathcal K_n=\bigoplus_{A\in\mathcal A(n)}\mathcal K^{(A)}
$$
$$
\text{orthogonal projection}\implies P^2=P=P^\dagger,\quad\mathfrak T P=\dim\operatorname{Im}P\quad[\text{linear algebra}]
$$
$$
\operatorname{Im}=\mathcal K_n\ [\text{construction}];\qquad\dim\mathcal K_n\ [\mathrm{CT0.14}];\qquad\mathcal A(n)\ \text{derived}\ [\mathrm{CT0.13}].\ \blacksquare
$$

**Rmk.** Theorem, not stipulation: CT0.13 derives which blocks are active; D2.3 converts the list into a projector.

**Phys.** Rung selection is a genuine orthogonal projection in force space — idempotent, self-adjoint, with trace equal to the block dimension $6/16/17/25$. Filtering by rung twice is the same as once: the universe’s capability space grows by strict projections, never by deformations.

---

### CT2.3 — Masked force operator

**Thm.** $\ \mathbf F_M^{(n)}:=\mathcal P_M^{(n)}\mathbf F\,\mathcal P_M^{(n)}$ satisfies
$$
\mathbf F_M^{(n)}\big|_{\mathcal K_n^\perp}=0;\qquad
\mathbf F_M^{(n)}(\mathcal K)\subseteq\mathcal K_n;\qquad
\mathbf F^\dagger=\mathbf F\implies\bigl(\mathbf F_M^{(n)}\bigr)^\dagger=\mathbf F_M^{(n)}.
$$

**Req.** A8, C7; D2.3; CT2.2.

**Pf.**
$$
x\in\mathcal K_n^\perp\implies\mathcal P_M^{(n)}x=0\implies\mathbf F_M^{(n)}x=0
$$
$$
\forall x:\ \ \mathbf F_M^{(n)}x=\mathcal P_M^{(n)}\bigl(\mathbf F\,\mathcal P_M^{(n)}x\bigr)\in\operatorname{Im}\mathcal P_M^{(n)}=\mathcal K_n\quad[\mathrm{CT2.2}]
$$
$$
\bigl(\mathcal P\mathbf F\mathcal P\bigr)^\dagger=\mathcal P^\dagger\mathbf F^\dagger\mathcal P^\dagger=\mathcal P\mathbf F\mathcal P\quad[\mathrm{CT2.2};\ \mathbf F^\dagger=\mathbf F].\ \blacksquare
$$

**Phys.** The masked force is exactly the restriction of the full force operator to the rung’s active subspace: it annihilates everything the rung cannot access, stays inside what it can, and inherits Hermiticity — hence a real spectrum — from $\mathbf F$. A8’s $\mathbf F_M=P_M\mathbf F P_M$ is the rung-unresolved form (C7).

---

### CT2.4 — Force restriction by rung

**Thm.**
$$
\mathbf F_M^{(n)}=\bigoplus_{A\in\mathcal A(n)}F_A\big|_{\mathcal K^{(A)}},\qquad
\mathcal A(n)\ \text{as in CT0.13};\qquad
\neg\exists\ \text{independent aspect}\ Z\ \text{at any rung}\ (W_3\ \text{seed}\in F_W)\ [\mathrm{C8}].
$$

**Req.** A8, C8; D2.3; CT0.13 (Part 1), CT2.2, CT2.3.

**Pf.**
$$
\mathrm{A8}:\ \mathbf F=\bigoplus_AF_A,\quad\operatorname{supp}F_A\subseteq\mathcal K^{(A)};\qquad
\mathrm{D2.3}:\ \mathcal P_M^{(n)}\to\bigoplus_{A\in\mathcal A(n)}\mathcal K^{(A)}
$$
$$
\text{block-diagonal conjugated by block-subset projection}\implies\text{retains exactly those blocks}
$$
$$
\mathcal A(n)\ \text{list}=[\mathrm{CT0.13}];\qquad F_W=F_{W^+}\oplus F_{W^-}\oplus F_Z,\ F_Z\equiv F_{W^3}\ \text{single block}\ [\mathrm{C8}].\ \blacksquare
$$

**Phys.** Masking never mixes forces: what survives at rung $n$ is exactly the direct sum of the active aspects. This licenses speaking of gravity from rung 1, electromagnetism from rung 2 and colour from rung 3 as literal block content of one operator.

---

### CT2.5 — Masked resolvent as spectrum generator

**Thm.** $\ \mathbf F_M^{(n)}=\sum_a\lambda_aP_a$ (spectral decomposition; $P_aP_b=\delta_{ab}P_a$, $P_a^\dagger=P_a$). Then
$$
Z(\mathcal R,n)=\Bigl\langle\mathrm{out}\Bigl|(1-\mathbf F_M^{(n)})^{-1}\Bigr|\mathrm{in}\Bigr\rangle=\sum_a\frac{\langle\mathrm{out}|P_a|\mathrm{in}\rangle}{1-\lambda_a};
$$
$$
\text{poles}\iff1\in\operatorname{spec}\mathbf F_M^{(n)};\qquad
\operatorname*{Res}_{\lambda_a\to1}=-\langle\mathrm{out}|P_a|\mathrm{in}\rangle=\text{transition amplitude};\qquad
\mathrm{D2.8}:\ 1\mapsto1+i\varepsilon\ \text{selects the branch}.
$$

**Req.** D2.4, D2.5, D2.8; CT0.14 (**B**: $\dim\mathcal K_n<\infty$), CT2.3 (Hermitian); spectral theorem [math].

**Pf.**
$$
(\mathbf F_M^{(n)})^\dagger=\mathbf F_M^{(n)}\ [\mathrm{CT2.3}]\ \wedge\ \dim\mathcal K_n<\infty\ [\mathrm{CT0.14}]\implies\mathbf F_M^{(n)}=\sum_a\lambda_aP_a\quad[\text{spectral theorem}]
$$
$$
(1-\mathbf F_M^{(n)})^{-1}=\sum_a\frac{P_a}{1-\lambda_a},\quad\text{defined}\iff\forall a:\ \lambda_a\ne1;\quad\text{singular}\iff\exists a:\ \lambda_a=1
$$
$$
Z(\mathcal R,n)=\sum_a\frac{\langle\mathrm{out}|P_a|\mathrm{in}\rangle}{1-\lambda_a}:\ \ \text{simple pole at}\ \lambda_a=1,\ \operatorname{Res}=-\langle\mathrm{out}|P_a|\mathrm{in}\rangle\ [\mathrm{D2.5}:\ \text{amplitude}]
$$
$$
\mathrm{D2.8}:\ 1\mapsto1+i\varepsilon\implies\text{poles off the real axis, fixed direction};\quad\varepsilon\to0^+\ \text{after contour integration}.\ \blacksquare
$$

**Phys.** The rung-$n$ particle spectrum is literally the condition “the masked force has eigenvalue 1”: poles of the resolvent are masses (D2.5), residues are amplitudes. The $i\varepsilon$ sheet makes the sums convergent and selects the branch — the entire spectral content of the corpus sits in this one matrix element.

---

### CT2.6 — Continuum manifold closure

**Thm.** Conditions: (i) valid universe [D2.11] — a definitional precondition (D2.11’s own definition in application, “there is something”), $\neg$ an extra-axiomatic hypothesis [A §0.2a]; (ii) coarse-graining cells contain unboundedly many real edges as $\mathfrak h\to0$ — derived (Part 4, Tier BM.24: the ledger's own unbounded ladder witnesses it [BM.151(1), forward pointer]); (iii) sector coefficient fields [D2.1] of bounded variation across neighbouring cells — derived (Part 4, Tier BM.24: the spectral bound $|r_a|\le\sqrt3$ with convex averaging [BM.151(2), forward pointer]). Then
$$
M:=\Gamma_{\mathcal R}/\!\!\sim\ \ \text{is a smooth 4-manifold};\qquad
\chi([v])=(x^0,x^1,x^2,x^3)=(\tau_n,h_1,h_2,h_3)\ \ \text{charts};
$$
$$
\text{transition maps}=\text{smooth diffeomorphisms};\qquad
g_{\mu\nu}\ [\mathrm{CT1.12}]=\text{smooth Lorentzian metric on}\ M;\qquad
\text{nondegeneracy}\iff\varkappa\|q\|_{\mathrm{op}}<1 .
$$

**Req.** A7; D1.3, D1.8, D1.9, D2.11; CT0.3 (Part 1), CT1.12; conditions (ii)–(iii) [derived — cf. Part 4 Tier BM.24, BM.151, forward pointer]; (i) $=$ D2.11 in application.

**Pf.**
$$
(\mathrm{i}):\ \#J^+=\#J^-\ [\mathrm{D2.11},\mathrm{D1.3}]\implies\textstyle\sum\Delta n_{\mathcal R}=0\ [\mathrm{CT0.3}]\implies\neg\exists\ \text{dangling ledger boundary beyond the sealed Janus boundary}
$$
$$
\sim\ :=\ \text{equal coarse-grained ledger entry under mask-preserving relabeling};\qquad
(\mathrm{ii})\implies\text{cells contain unboundedly many edges}\implies M\ \text{locally a continuum as}\ \mathfrak h\to0
$$
$$
\text{charts}:\ x^0:=\tau_n\ [\mathrm{D1.8}];\quad x^i:=\text{hop counters projected on the 3 shift directions}\ (W_i\ \text{sector})\ [\mathrm{CT1.12}];\quad\chi:U\subseteq M\to\mathbb R^4;\quad 4=1+3\ [\mathrm{CT1.12}]
$$
$$
\text{smoothness}:\ \text{coefficients}=\text{local ledger averages};\ \ \mathrm{D1.9}:\ \text{updates local, finite};\ \ (\mathrm{iii}):\ \text{jumps uniformly bounded}\implies\text{smooth interpolation, deviation}\to0\ \text{with}\ \mathfrak h
$$
$$
\text{transitions}=\text{resynchronizations between valid observers}:\ \text{mask-}\wedge\text{Janus-preserving}\implies\text{finite compositions of translations/permutations/sign reversals}
$$
$$
\implies\text{smooth, constant Jacobian},\ |\det J|=1;\quad\circ\ \text{interpolation}\implies\text{diffeomorphisms}
$$
$$
\text{nondegeneracy}:\ \mathrm{CT1.12}\ (\varkappa\|q\|_{\mathrm{op}}<1)\iff J\ \text{invertible};\qquad
\text{atlas}\implies M\ \text{smooth 4-manifold};\ g_{\mu\nu}\ \text{smooth Lorentzian}.\ \blacksquare
$$

**Phys.** Under three explicit coarse-graining hypotheses — and nothing else — the real-edge network of the ledger becomes a smooth four-dimensional spacetime carrying the emergent Lorentzian metric. This is the bridge theorem of the corpus: it converts combinatorics (edges, ticks, counters) into the differential geometry that Parts III–IV vary.


**Rmk (derivation locus: Part 4 Tier BM.24).** Conditions (ii)–(iii) carry no extra-axiomatic status [A §0.2a]: BM.151 derives both from the ledger's own structure: (ii) from the configuration-space ladder (A7; FT.32; FT.45–FT.46) with the ladder row $\#\{E_{\mathcal R}\ \text{per cell}\}\ge2sE\ln2/\mathfrak h\to\infty$, and (iii) from the pair-state spectral bound (A1; L1; L3(1)) with the convex averaging of the coefficient fields. This theorem's statement, proof and conclusions are unchanged; the point-of-use declarations across the corpus stand as scope-inheritance markers. The extra-axiomatic list of A §0.2a is empty.
---

### CT2.7 — Exact geometric action closure

**Thm.** Under the hypotheses of CT2.6:
$$
S_{\mathrm{geom}}[g]=\frac{1}{2\kappa^2}\int d^4x\,\sqrt{-g}\,\bigl(R-2\Lambda\bigr);\qquad
\neg\exists\ \text{additional local higher-curvature terms}.
$$

**Req.** A8; D1.9, D4.3; CT2.6; Lovelock classification $D=4$; Gauss–Bonnet $=$ total derivative in $D=4$ [math].

**Rmk (forward pointer, non-load-bearing).** The $\kappa$-normalization cross-check against CT1.23 is a consistency pointer, not a derivation input.

**Pf.**
$$
\mathrm{D1.9}:\ \text{tick stencil}=1\ \text{time step}+1\ \text{edge}\implies\text{continuum E--L equations}\le2\ \text{nd order}
$$
$$
\text{arena}=\text{smooth 4-dim Lorentzian manifold}\ [\mathrm{CT2.6}]
$$
$$
\text{weights depend on}\ (\Gamma,\text{registrations})\ \text{only},\ \neg\text{vertex names}\implies\text{relabeling-invariant}\xrightarrow[\mathrm{CT2.6}]{}\text{diffeomorphism-invariant local functional of}\ g
$$
$$
\text{Lovelock}\ (D=4):\ \bigl\{\sqrt{-g}R,\ \sqrt{-g},\ \sqrt{-g}\,\mathcal G\bigr\},\quad\mathcal G=R^2-4R_{\mu\nu}R^{\mu\nu}+R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma}\quad[\text{math}]
$$
$$
\sqrt{-g}\,\mathcal G=\partial(\cdots)\ \text{in}\ D=4\implies\delta S\equiv0\implies\text{dropped}\quad[\text{math}]
$$
$$
F_{D^+}=\Lambda\mathbb I\ [\mathrm{A8}],\ \neg\text{configuration-dependent}\ [\mathrm{D4.3}]\implies\text{zero-derivative density}\ \sqrt{-g}\,\Lambda\ \text{only}
$$
$$
\text{collect at}\ \tfrac{1}{2\kappa^2}\ \text{normalization}\ [\mathrm{CT1.23}]\implies\text{Thm}.\ \blacksquare
$$

**Phys.** The geometric dynamics is closed exactly: tick-locality plus diffeomorphism invariance plus Lovelock leave only Einstein–Hilbert with a cosmological term, and that term is the uniform dark aspect itself. No higher-curvature corrections exist — the higher-derivative question is answered, not deferred.

---

### CT2.8 — Reflection positivity and Hilbert-space closure

**Thm.** With $\ \langle A|B\rangle:=Z\bigl[\Theta_{\mathfrak L}A\cup B\bigr]\ $ on $\mathfrak C(\mathcal R)$ [D0.10]:
$$
(1)\ \ w(\Theta_{\mathfrak L}C)=w(C)^\ast;\qquad
(2)\ \ w(C)=w(C_{\mathrm{left}})\cdot w(C_{\mathrm{right}})\ \ \text{across any interior ledger-time cut};
$$
$$
(3)\ \ \langle A|A\rangle=\sum_C|w(C)|^2\ \ge\ 0;\qquad
(4)\ \ \langle A|A\rangle=0\iff A\ \text{mask-excluded}\ \ (\text{null space}=\text{mask-excluded configurations});
$$
$$
(5)\ \ \text{quotient}\wedge\text{completion}=\text{Hilbert space};\qquad
(6)\ \ Z\big|_{\text{reflected pair}}=\|\cdot\|^2,\ \ \text{convergent on the}\ \mathrm{D2.8}\ \text{sheet}.
$$

**Req.** A8; D0.7, D0.10; D1.2, D1.3, D1.9; D2.6, D2.7, D2.8; D3.3, D3.5, D3.6; CT2.2; Hilbert-space completion [math; machine: `checks/verify_F33_dynamic_phase.py` §D].

**Pf.**
$$
(1):\ \mathcal J(\Theta_{\mathfrak L}C)=\mathcal J(C)^\ast\ [\mathrm{D3.6}];\qquad G(\Theta_{\mathfrak L}e)=G(e)^\ast\ [\mathrm{D2.7},\ \mathrm{D3.5}:\ \alpha_e\widehat{ds}^{\,2}(e)\mapsto-\alpha_e\widehat{ds}^{\,2}(e),\ \sigma_e\ \text{fixed}]
$$
$$
\omega:\ \text{type}(1,1)\mapsto\text{signs exchanged}\implies f_v\mapsto-f_v\implies\aleph_v=|f_v|\ \text{invariant}\implies(-1)^\aleph\in\mathbb R\ \text{invariant}\ [\mathrm{D2.6},\mathrm{D3.3}]
$$
$$
\implies w(\Theta_{\mathfrak L}C)=w(C)^\ast\quad[\mathrm{A8}]
$$
$$
(2):\ \mathrm{A8}:\ w(C)=\mathcal J(C)\prod_{e\in E(C)}G(e)\cdot(-1)^{\aleph(\sigma,C)};\qquad \text{interior cut at a ledger time}:\ E(C)=E_{\mathrm L}\sqcup E_{\mathrm R}\ [\mathrm{D0.7}:\ \text{each edge is registered between consecutive ticks, wholly on one side}]
$$
$$
\prod_{e\in E(C)}G(e)=\prod_{E_{\mathrm L}}G\cdot\prod_{E_{\mathrm R}}G;\qquad (-1)^{\aleph(\sigma,C)}=\prod_v(-1)^{\aleph_v}:\ \aleph_v\ v\text{-local}\ [\mathrm{D3.3};\ \mathrm{D1.9}:\ \operatorname{dom}(\mathrm{tick}(v))\subseteq\{v\}\cup\{e\ni v\}]
$$
$$
\text{interface}:\ \text{the seal data at the cut are boundary data of the halves}\ [\mathrm{D1.2};\ \mathrm{D1.3}:\ \#J^+=\#J^-\ \text{pair at boundaries}];\qquad \text{side convention: each vertex factor belongs to the side holding its tick}
$$
$$
\implies w(C)=w(C_{\mathrm{left}})\cdot w(C_{\mathrm{right}})\quad[\text{product regrouping}]
$$
$$
(3):\ \ A=B:\ \ \langle A|A\rangle=\sum_Cw(\Theta_{\mathfrak L}C)w(C)=\sum_C|w(C)|^2\ge0\quad[(1),(2)]
$$
$$
(4):\ \ =0\implies\forall C:\ w(C)=0;\qquad \mathrm{A8}\ \text{weight}=\text{product of nonzero factors except where excluded}\ [|G(e)|=1\ \mathrm{(D3.5)};\ \mathcal J\ne0];\qquad \text{excluded}\iff\notin\operatorname{Im}\mathcal P_M^{(n)}\ [\mathrm{CT2.2}]
$$
$$
(5):\ \text{PSD form}\implies\text{positive definite on quotient}\implies\text{completion}=\text{Hilbert space}\quad[\text{math: completion theorem; no network-specific input}]
$$
$$
(6):\ \ \mathrm{D2.8}\ \text{sheet}\implies\sum|w|^2\ \text{converges};\ \neg\exists\ \text{indefinite oscillatory spoilage}. \blacksquare
$$

**Phys.** The ledger’s own reflection symmetry makes the configuration sum positive: the reflected pairing is a sum of $|w|^2$, its null space is exactly what the mask forbids, and the quotient completes to a genuine Hilbert space. The split along an interior ledger-time cut is a consequence of A8’s per-edge product structure and tick locality — the seals sit at boundaries [D1.2, D1.3], and no factor straddles an interior cut. This is the positivity property that licenses reading ledger weights as quantum theory.

---

### CT2.10 — Graded matrices and the supertrace

**Thm.** For homogeneous $X,Y$ [D2.10]:
$$
\operatorname{Str}(XY)=(-1)^{|X||Y|}\operatorname{Str}(YX);\qquad
\operatorname{Str}[X,Y\}=0 .
$$

**Req.** D2.10; cyclicity of $\mathfrak T$ [linear algebra].

**Pf.**
$$
|X|=|Y|=0:\ \ X=\operatorname{diag}(X_B,X_F),\ Y=\operatorname{diag}(Y_B,Y_F):\quad
\operatorname{Str}(XY)=\mathfrak T(X_BY_B)-\mathfrak T(X_FY_F)=\mathfrak T(Y_BX_B)-\mathfrak T(Y_FX_F)=\operatorname{Str}(YX);\ (-1)^0=+1
$$
$$
|X|\ne|Y|:\ \ XY,\ YX\ \text{odd}\implies\text{diagonal blocks}=0\implies\operatorname{Str}(XY)=\operatorname{Str}(YX)=0
$$
$$
|X|=|Y|=1:\ \ X=\begin{pmatrix}0&X_1\\ X_2&0\end{pmatrix},\ Y=\begin{pmatrix}0&Y_1\\ Y_2&0\end{pmatrix}:\quad
XY=\operatorname{diag}(X_1Y_2,\ X_2Y_1),\ YX=\operatorname{diag}(Y_1X_2,\ Y_2X_1)
$$
$$
\operatorname{Str}(XY)=\mathfrak T(X_1Y_2)-\mathfrak T(X_2Y_1)=\mathfrak T(Y_2X_1)-\mathfrak T(Y_1X_2)=-\operatorname{Str}(YX);\ (-1)^{1}=-1
$$
$$
\implies\operatorname{Str}[X,Y\}=\operatorname{Str}(XY)-(-1)^{|X||Y|}\operatorname{Str}(YX)=0\ \ \forall\ \text{parities}.\ \blacksquare
$$

**Phys.** The supertrace is graded-cyclic: it vanishes on graded commutators and therefore descends to an invariant form on the graded (bosonic/fermionic) algebra — the tool that lets bound (fermionic) and transit (bosonic) content coexist in one trace formula.

---

## §C.III — Continuum Limit, Effective Action, and Field Equations

### CT1.19 — Continuum limit at leading order

**Thm.** $L=\mathfrak h\,n_{\mathcal R}$ fixed; $\ \mathfrak h\to0\ \wedge\ n_{\mathcal R}\to\infty\implies$
$$
\sum_{e\in\gamma}ds^2(e)\ \longrightarrow\ \int_\gamma g_{\mu\nu}\,dx^\mu dx^\nu=L\int_0^1g_{\mu\nu}\bigl(x(\lambda)\bigr)\dot x^\mu\dot x^\nu\,d\lambda;\qquad
\text{abs.\ error}=O(\mathfrak hL),\quad\text{rel.\ error}=O(\mathfrak h).
$$

**Cor CT1.19a.** $\ \widehat{ds}^{\,2}(e)=ds^2(e)/\mathfrak h^2:$ dimensionless, $O(1)$ generically; $\ \widehat{ds}^{\,2}(e)=0\iff\Delta x_e\ \text{null}$; trivial chain [D1.7] $=$ all-null-edge chain.

**Req.** D0.6, D1.6, D1.7; CT2.6; midpoint Taylor, Riemann sums [math].

**Pf.**
$$
\mathrm{CT2.6}\implies g_{\mu\nu}\ \text{smooth along}\ \gamma;\qquad
\mathrm{D0.6}:\ |\Delta x^\mu_e|=O(\mathfrak h)
$$
$$
\lambda\in[0,1],\ x^\mu(\lambda)\ \text{smooth}:\quad\Delta x^\mu_e=\mathfrak h\,\dot x^\mu(\lambda_e)+O(\mathfrak h^2)\quad[\text{midpoint Taylor}]
$$
$$
\sum_{e}ds^2(e)=\sum_e g_{\mu\nu}(x_e)\,\mathfrak h^2\dot x^\mu_e\dot x^\nu_e+O(\mathfrak h^3n_{\mathcal R})\quad[\mathrm{D1.6}]
$$
$$
=\mathfrak h\sum_e\mathfrak h\,g_{\mu\nu}(x_e)\dot x^\mu_e\dot x^\nu_e+O(\mathfrak h^2L)\xrightarrow[\text{Riemann, mesh}\ \mathfrak h/L]{}L\int_0^1g_{\mu\nu}\dot x^\mu\dot x^\nu d\lambda
$$
$$
\text{leading}=O(\mathfrak hL)\implies\text{rel.}=O(\mathfrak h),\ \text{abs.}=O(\mathfrak hL)\to0.\ \blacksquare
$$
**Pf (Cor).** $[\widehat{ds}^{\,2}]=[\mathfrak h^0]$ [D1.6]; $\ \widehat{ds}^{\,2}(e)=0\iff ds^2(e)=0\iff\Delta x_e$ null; $\ \mathsf{Trivial}\iff\forall e:\ \widehat{ds}^{\,2}(e)=0$ [D1.7]. $\blacksquare$

**Phys.** At fixed macroscopic length, shrinking the hop length makes the sum of discrete line elements converge to the continuum path integral of the metric, with relative error $O(\mathfrak h)$. Spacetime intervals are literally Riemann sums over edge data — and null edges define the trivial chains that later become photons and gluons.

**Rmk (on-shell interface).** On-shell integer quantization is no obstruction to this limit: for materialized closed chains of the fully antialigned class (realized — CT1.19b(3)) each $\kappa_e\in\mathbb Z_{\ge0}$ samples $g_{\mu\nu}\dot x^\mu\dot x^\nu(\lambda_e)$ with $O(\mathfrak h)$ slack, and $\sum_e\kappa_e\,\mathfrak h^2=\sum_e ds^2(e)$ identically [D1.6] — so CT1.19 applies verbatim to on-shell chains (abs.\ error $O(\mathfrak hL)$). Machine: `checks/verify_merge_tierA.py` §G.

---

### CT1.19b — On-shell line-element quantization: even antialigned winding, orientation evenness, the geometry quantum, internal holonomy

**Thm.** A closed chain $c$ [D1.4, D1.5] **materializes** $:=$ it contributes a spectral pole of the masked resolvent at the rung of its active mask [D2.4, D2.5, CT2.5, D1.12, CT0.13] — the corpus's own pole-as-materialization condition as applied in EW.18; instance: wrapping chains [EW.17]. Under EM.20's phase alphabet ($\alpha_e\in\{0,\pi\}$ per real edge, at every accessible rung):
$(1)$ **Even antialigned winding.** For every materialized closed chain the spiral holonomy is single-valued:
$$\operatorname{Hol}_{\mathrm{spiral}}(c)=e^{i\Phi(c)}=+1,\qquad \Phi(c)=\sum_{e\in c}\alpha_e\,\widehat{ds}^{\,2}(e)=\pi\,\Theta_{\mathcal P}(c)=2\pi k,\quad k\in\mathbb Z\ \ (\text{winding}\ [\mathrm{D1.7},\ \mathrm{EW.18}])$$
$$\Theta_{\mathcal P}(c):=\!\!\sum_{e\in\mathcal P(c)}\!\!\widehat{ds}^{\,2}(e)\qquad[\mathcal P(c):\ \text{the antialigned edges of}\ c,\ \mathrm{Def\text{-}EM.21};\quad \alpha_e\in\{0,\pi\}:\ \mathrm{EM.20}(1)]$$
$$\implies\ \Theta_{\mathcal P}(c)=2k\in2\mathbb Z\qquad(n=2,3,\ge4);\qquad \mathcal P(c)=c\ (\text{fully antialigned class}):\ \ \Theta(c)=2k .$$
On rung-3 wrapping chains this reduces verbatim to EW.18 (consistency).
$(2)$ **Orientation evenness.** For a bidirectional channel — both orientations $e_{pq}=(p,q)$, $e_{qp}=(q,p)$ in $\mathcal R$:
$$\widehat{ds}^{\,2}(e_{pq})=\widehat{ds}^{\,2}(e_{qp})$$
$(3)$ **The geometry quantum.** For a materialized 2-cycle $c=(e_1,e_2)$, $e_1=(p,q)$, $e_2=(q,p)$ — the minimal closed chain (A1 excludes self-loops [D1.4]) — writing $\kappa:=\widehat{ds}^{\,2}(e_1)=\widehat{ds}^{\,2}(e_2)$ [clause (2)] and $m:=|\mathcal P(c)|\in\{0,1,2\}$:
$$\Theta_{\mathcal P}(c)=m\kappa\in2\mathbb Z\implies\kappa\in\tfrac2m\mathbb Z\ \ (m\ge1);\qquad m=2:\ \ \kappa\in\mathbb Z;\quad ds^2(e)=\kappa\,\mathfrak h^2\in\mathfrak h^2\mathbb Z\ [\mathrm{D1.6}];\quad \mathfrak h^2=4G_N\ln2\ [\mathrm{CT2.9}]\implies ds^2(e)=4\kappa\,G_N\ln2$$
— the interval quantum is one Bekenstein bit-area [CT1.29: $S=\ln2$ at $A=\mathfrak h^2$] per unit $\kappa$ on the fully antialigned class. Attainment and sign classes: $\kappa=1$ attained on the minimal real edge [D1.1] with $m=2$ (floor tight; both alignment values realizable: EM.20(5)); $\kappa=0\iff$ null edge [CT1.19a] (degenerate floor; all-null transit chains are the trivial chains — photons/gluons [D1.7, D3.7]); $\kappa<0$ admissible $=$ timelike [CT1.12: $\operatorname{sig}(g)=(-,+,+,+)$]. $m=0$: the winding condition is vacuous, $\kappa$ unconstrained by clause (1).
$(4)$ **Internal holonomy.** If a subnetwork's interior edges $\Sigma\setminus\partial\Sigma$ [D2.13] decompose edge-disjointly into materialized closed chains $\{c_i\}$, then:
$$\Theta_{\mathcal P,\mathrm{int}}(\Sigma):=\!\!\sum_{e\ \mathrm{int},\ \alpha_e=\pi}\!\!\widehat{ds}^{\,2}(e)=\sum_i\Theta_{\mathcal P}(c_i)\in2\mathbb Z,\qquad \mathrm{Hol}_{\mathrm{int}}:=e^{i\Phi_{\mathrm{int}}}=e^{i\pi\Theta_{\mathcal P,\mathrm{int}}}=+1$$
and the surviving on-shell integer label is the winding $k(c)=\Theta_{\mathcal P}(c)/2$. On *partial* internal sets (proper subsets of a materialized chain's edges) $\Theta_{\mathcal P,\mathrm{int}}$ is a partial sum of integers with free parity: $\mathrm{Hol}_{\mathrm{int}}=\pm1$ well-defined, nontrivial (witness: a single $\kappa=1$ antialigned edge gives $(-1)^1=-1$). Off-shell, $\widehat{ds}^{\,2}(e)$ remains generic continuous [CT1.19a] — quantization is an on-shell (materialization) property, $\neg$a postulate on every edge.

**Req.** A1; D1.1, D1.4, D1.5, D1.6, D1.7, D1.12; D2.4, D2.5, D2.13; CT0.7(2), CT0.13, CT1.1, CT1.2, C3 (Part 1); CT1.12, CT1.19a, CT1.29, CT2.5, CT2.6 (charts; hypotheses — A §0.2a); D3.7; Def-EM.21, EM.20 (**E**; forward pointers — C DAG note); EW.17, EW.18 (**D**; forward pointers — wrapping instance and winding freedom); single-valued eigenmode condition, quadratic-form evenness [math; machine: `checks/verify_merge_tierB.py` §B].

**Pf.**
$$(1):\ \mathrm{D1.7}:\ \Theta,\ \Phi=\textstyle\sum_e\alpha_e\widehat{ds}^{\,2}(e),\ \operatorname{Hol}_{\mathrm{spiral}}=e^{i\Phi}\ \text{defined for every chain};\qquad \mathrm{EW.17}:\ \text{transport around a closed cycle multiplies the eigenmode by}\ \operatorname{Hol}_{\mathrm{spiral}}$$
$$\mathrm{CT2.5}\ (\text{as applied in EW.18}):\ \text{pole}=\text{eigenvalue condition on a single-valued eigenmode}\implies e^{i\Phi(c)}=1;\qquad \text{winding freedom}\ [\mathrm{EW.18}]:\ \Phi(c)=2\pi k,\ k\in\mathbb Z$$
$$\text{domain step (flagged)}:\ \mathrm{EW.17}'\text{s rung-3 restriction is an existence claim about wrapping chains};\ \mathrm{CT2.5}'\text{s single-valuedness step is chain-generic}\implies\text{the Pf extends to every materialized closed chain with no added premise}$$
$$\mathrm{EM.20}(1):\ \alpha_e\in\{0,\pi\}\ \text{at every accessible rung (the case split is rung-blind; CT0.9 alphabet)}\implies\Phi(c)=\pi\!\!\sum_{e\in\mathcal P(c)}\!\!\widehat{ds}^{\,2}(e)=\pi\Theta_{\mathcal P}(c)\implies\Theta_{\mathcal P}(c)=2k$$
$$(2):\ \mathrm{CT2.6}\ \text{charts}:\ \Delta x_{e_{qp}}=-\Delta x_{e_{pq}};\qquad g_{\mu\nu}\ \text{built solely from}\ S\text{-even data}\ [\mathrm{CT1.12};\ \mathrm{CT1.12a}(2);\ \mathcal E_{++},\mathcal E_{+-}\ S\text{-even: CT1.1, CT1.2, C3};\ S(X)=\mathbb S X\mathbb S:\ \mathrm{CT0.7}(2)]$$
$$\mathrm{D1.6}:\ ds^2(e)=g_{\mu\nu}(e)\,\Delta x^\mu_e\Delta x^\nu_e\ \text{quadratic in}\ \Delta x\ (\text{every monomial of degree}\ 2,\ \text{incl. the shift cross-term}\ 2g_{0i}\Delta x^0\Delta x^i)\implies\Delta x\mapsto-\Delta x\ \text{fixes}\ ds^2$$
$$(3):\ \Theta_{\mathcal P}(c)=m\kappa,\ m=|\mathcal P(c)|\ [(2):\ \text{both edges share}\ \kappa];\quad (1):\ m\kappa\in2\mathbb Z;\quad m=2:\ \kappa\in\mathbb Z;\quad \mathrm{D1.6}:\ ds^2=\kappa\mathfrak h^2;\quad \mathrm{CT2.9}:\ \mathfrak h^2=4G_N\ln2;\quad \mathrm{CT1.29}:\ A=\mathfrak h^2\Rightarrow S=\ln2$$
$$\mathrm{D1.1}:\ \widehat{ds}^{\,2}=1\ \text{on the minimal real edge};\qquad \mathrm{EM.20}(5):\ \alpha_e=0\ \wedge\ \alpha_e=\pi\ \text{each realizable}\implies m=2\ \text{attained}\implies\kappa=1\ \text{attained};\quad \mathrm{CT1.19a}:\ \widehat{ds}^{\,2}=0\iff\text{null};\quad \mathrm{D1.7}/\mathrm{D3.7}:\ \text{all-null transit}=\text{trivial chains}$$
$$(4):\ \text{edge-disjointness}:\ \Theta_{\mathcal P,\mathrm{int}}=\sum_i\Theta_{\mathcal P}(c_i)\in2\mathbb Z\ [(1)];\quad e^{i\pi\cdot2\mathbb Z}=+1;\quad \text{partial sets}:\ \text{single antialigned}\ \kappa=1\ \text{edge}\implies\Theta_{\mathcal P,\mathrm{int}}=1,\ (-1)^1=-1.\ \blacksquare$$

**Rmk (locus of the quantization).** The winding constraint reads on the antialigned content: edges with $\alpha_e=0$ drop out of $\Phi(c)$ [D1.7], so $\Theta(c)$ is constrained exactly on the fully antialigned class $\mathcal P(c)=c$; on a general pattern the constrained sum is $\Theta_{\mathcal P}(c)$ [Def-EM.21]. The alphabet $\{0,\pi\}$ — derived, with no effectivity input [EM.20(1); A §0.2a] — is what makes the constraint integral (machine: §B parity sweep).

**Rmk (sign-factor separation).** Single-valuedness is imposed on the spiral/geometric transport [EW.18]; the registration signs $\sigma_e$ and the wall parity $(-1)^{\aleph}$ are ledger data of the weight $w(C)$ [A8, CT0.9, D3.3], $\neg$of the geometric eigenmode transport.

**Rmk (area language, scoped).** $\Theta_{\mathcal P}(c)\,\mathfrak h^2$ is the $\kappa$-weighted accumulated line element of the antialigned content — dimensionally an area, and equal to CT1.29's pierced-edge area $A=n_{\mathcal R}\mathfrak h^2$ exactly on the minimal-edge fully antialigned class $\kappa\equiv1$ (then $\Theta_{\mathcal P}=\delta h$; the exactness locus of the rate: CT1.29a(2)). It is $\neg$the metric-enclosed area of $c$: the floor 2-cycle traces a degenerate out-and-back locus — zero enclosed area — yet carries $\Theta_{\mathcal P}=2\kappa\ne0$ at $m=2$, because $ds^2$ is quadratic, hence orientation-blind [clause (2)].

**Phys.** The $ds^2$ question is settled on-shell by computation, with no new postulate: the antialigned content of a materialized closed chain winds in even quanta, both orientations of a channel agree on its length, the minimal materialized 2-cycle pins the geometry quantum at one Bekenstein bit-area per hop on the fully antialigned class, and internal holonomy reduces to a single integer winding per chain. Off-shell, nothing is quantized — integrality is a property of materialization, not an axiom about edges.


**Rmk (scope).** Round-trip-closed bidirectional channels realize $\kappa\in\mathbb Z$ per edge; bare cycles admit the rational ladder $\kappa\in\tfrac2L\mathbb Z$, outside hypothesis (ii). The effective-quantum label reads $\bar\kappa$ here [READING]; the transport vocabulary has no corpus referent (nearest declared objects: round-trip bidirectional channels).
---

### CT1.20 — Effective action from the partition function

**Thm.** $\ Z[g]=\sum_{C:\,g(C)=g}|w(C)|\,e^{i\Phi(C)}$ [$\Phi:$ D1.7+D3.5+parity phases]. Semiclassically ($\delta\Phi\ne0$: pairwise cancellation; $\delta\Phi=0$: dominance):
$$
S_{\mathrm{eff}}[g]:=-i\log Z[g]\ \ (\text{branch}\ [\mathrm{D2.8}]);\qquad
\frac{\delta S_{\mathrm{eff}}}{\delta g^{\mu\nu}}=0\iff\frac{\delta Z}{\delta g^{\mu\nu}}=0\ \ (Z\ne0);\qquad
\text{stationary points dominate}.
$$

**Req.** A8; D1.7, D2.8, D3.5; CT1.12, CT2.6 ($\Phi$ differentiable in coarse-grained variables); stationary phase [math].

**Pf.**
$$
\mathrm{CT1.12}:\ C\mapsto g_{\mu\nu}(C)\implies Z\ \text{function of}\ g\ \text{after grouping}\ [\mathrm{A8}]
$$
$$
w(C)=|w(C)|e^{i\Phi(C)};\qquad\Phi=\text{accumulated phase}\ [\mathrm{D1.7},\ \mathrm{D3.5},\ (-1)^\aleph]
$$
$$
\delta\Phi\ne0\ \text{neighbourhoods cancel pairwise};\quad\text{survivors}=\{\delta\Phi=0\}\quad[\text{stationary phase};\ \Phi\ \text{differentiable}\ [\mathrm{CT2.6}]]
$$
$$
S_{\mathrm{eff}}:=-i\log Z\ \ \text{single-valued on the D2.8 sheet}
$$
$$
\delta Z=0\ \wedge\ Z\ne0\iff\delta\log Z=\delta Z/Z=0\iff\delta S_{\mathrm{eff}}=0.\ \blacksquare
$$

**Phys.** Grouping ledger configurations by their emergent metric turns the partition sum into a path-integral-like object dominated by stationary phase; its logarithm is an effective action for geometry. Classical spacetime = the stationary set of the ledger sum; quantum fluctuations = the rest.

---

### CT1.21 — The geometric part of the effective action

**Thm.** $\ S_{\mathrm{geom}}[g]=\dfrac{1}{2\kappa^2}\displaystyle\int d^4x\,\sqrt{-g}\,(R-2\Lambda).$

**Req.** D1.9, D4.3; CT1.20, CT2.7.

**Pf.**
$$
\mathrm{CT1.20}\implies S_{\mathrm{eff}}\ \text{local, diffeomorphism-invariant},\ \le2\ \text{nd order}\ [\mathrm{D1.9}+\text{relabeling}]
$$
$$
\mathrm{CT2.7}:\ \text{unique such functional in}\ D=4\ (\text{topological density dropped};\ F_{D^+}=\Lambda\mathbb I\ \text{included}\ [\mathrm{D4.3}])\implies\text{Thm}.\ \blacksquare
$$

**Phys.** The geometry part of the effective action is exactly Einstein–Hilbert with a cosmological term — derived from the structure of the ledger sum, with $\Lambda$ supplied by the uniform dark aspect of A8.

---

### CT1.22 — Stress-energy tensor from the force operator

**Thm.** With $D^+$ removed from $Z_{\mathrm{force}}$ (carried by $\Lambda$ in $S_{\mathrm{geom}}$):
$$
S_{\mathrm{force}}[g]:=-i\log Z_{\mathrm{force}}[g];\qquad
Z_{\mathrm{force}}[g]=\bigl\langle\mathrm{out}\bigl|(1-\mathbf F_M^{(n)})^{-1}\bigr|\mathrm{in}\bigr\rangle;\qquad
T_{\mu\nu}:=-\frac{2}{\sqrt{-g}}\frac{\delta S_{\mathrm{force}}}{\delta g^{\mu\nu}};
$$
$$
T_{\mu\nu}=T^{\mathrm{bd}}_{\mu\nu}+T^{\mathrm{tr}}_{\mu\nu};\qquad
T^{\mathrm{bd}}_{\mu\nu}=(\rho+p)u_\mu u_\nu+p\,g_{\mu\nu};\qquad
T^{\mathrm{tr}}_{\mu\nu}=\sum_a\Bigl(F^{(a)}_{\mu\alpha}F^{(a)\ \alpha}_{\ \ \nu}-\tfrac14g_{\mu\nu}F^{(a)}_{\alpha\beta}F^{(a)\alpha\beta}\Bigr),
$$
the sum over aspects whose leading transit representation is a connection.

**Req.** A8; D1.1, D1.5, D1.10, D4.3; CT1.19, CT1.21, CT2.4; $\delta\sqrt{-g}=-\tfrac12\sqrt{-g}\,g_{\mu\nu}\delta g^{\mu\nu}$, $\delta(F_{\alpha\beta}F^{\alpha\beta})=2F_{\mu\rho}F_\nu{}^\rho\delta g^{\mu\nu}$ [math].

**Pf.**
$$
\mathrm{A8}\ \text{blocks};\ \mathrm{CT2.4}:\ \text{mask retains exactly}\ \mathcal A(n);\qquad
\Delta S=\mathsf E_{\mathrm{bd}}+\mathsf E_{\mathrm{tr}}\ [\mathrm{D1.5}]\implies\forall\ \text{contribution}\in\text{exactly one channel}\implies T=T^{\mathrm{bd}}+T^{\mathrm{tr}}
$$
$$
\text{bd}:\ \text{closed chain}\implies\text{rest frame selects timelike}\ u^\mu,\ \neg\text{spatial direction};\ \ \text{content}=(\rho,p)\ [\mathrm{D1.10}]
$$
$$
\text{most general symmetric 2-tensor from}\ (g,u,\rho,p),\ u\text{-rotation-invariant}=(\rho+p)u_\mu u_\nu+p\,g_{\mu\nu}\quad[\text{math}]
$$
$$
\text{tr}:\ \mathrm{D1.1}:\ \text{edges carry phases}\implies\text{gauge-invariant local datum}=\text{holonomy};\quad\text{holonomy/area}\to F^{(a)}_{\mu\nu}\ [\mathrm{CT1.19}]
$$
$$
\text{unique local, gauge-invariant},\ \le2\ \text{nd order, quadratic in}\ F:\quad S_a=-\tfrac14\int d^4x\sqrt{-g}\,F^{(a)}_{\mu\nu}F^{(a)\mu\nu}
$$
$$
\delta S_a=-\tfrac14\int\sqrt{-g}\bigl[-\tfrac12g_{\mu\nu}F^2+2F_{\mu\rho}F_\nu{}^\rho\bigr]\delta g^{\mu\nu}\implies T^{(a)}_{\mu\nu}=F^{(a)}_{\mu\rho}F^{(a)\ \rho}_{\ \ \nu}-\tfrac14g_{\mu\nu}F^{(a)}_{\alpha\beta}F^{(a)\alpha\beta}
$$
$$
\text{no double counting}:\ D^+\ \text{excluded from}\ Z_{\mathrm{force}}\ \text{by construction};\ \ \mathrm{D4.3}:\ \neg\text{config.-dependent}\implies\text{removal}=\text{constant factor}\implies\delta\ \text{unaffected}.\ \blacksquare
$$

**Rmk.** Abelian case written out in EM.15 (Part 2), which depends on this result, not the reverse.

**Phys.** The right-hand side of the field equations is built from the same force operator that built the geometry: bound (closed-chain, fermionic) content yields perfect-fluid stress; transit (connection-carrying, bosonic) content yields Maxwell-type stress. $T_{\mu\nu}$ is defined by metric variation of the masked-force resolvent, with the uniform dark part counted once, as $\Lambda$.

---

### CT1.23 — Field equations

**Thm.**
$$
S_{\mathrm{eff}}=S_{\mathrm{geom}}+S_{\mathrm{force}};\qquad
\delta S_{\mathrm{eff}}=0\iff G_{\mu\nu}+\Lambda g_{\mu\nu}=\kappa^2T_{\mu\nu};
$$
$$
\text{dimensions}\ [\mathrm{CT2.1}]:\quad\mathfrak q^{+1}=\mathfrak q^{-1}\cdot\mathfrak q^{+2}=\mathfrak q^{+1};\qquad
\kappa:=\text{coefficient fixed by}\ S_{\mathrm{geom}}\ \text{normalization}.
$$

**Req.** CT1.21, CT1.22, CT2.1; $\delta(\sqrt{-g}R)=\sqrt{-g}\,G_{\mu\nu}\delta g^{\mu\nu}+\partial(\cdots)$, $\delta\sqrt{-g}=-\tfrac12\sqrt{-g}\,g_{\mu\nu}\delta g^{\mu\nu}$ [math].

**Pf.**
$$
\delta S_{\mathrm{geom}}=\frac{1}{2\kappa^2}\int d^4x\sqrt{-g}\,\bigl(G_{\mu\nu}+\Lambda g_{\mu\nu}\bigr)\delta g^{\mu\nu}\quad[\mathrm{CT1.21};\ \delta\text{-identities}]
$$
$$
\delta S_{\mathrm{force}}=-\tfrac12\int d^4x\sqrt{-g}\,T_{\mu\nu}\,\delta g^{\mu\nu}\quad[\mathrm{CT1.22}\ \text{definition}]
$$
$$
\forall\,\delta g^{\mu\nu}:\ \ \delta S_{\mathrm{eff}}=0\iff\frac{1}{2\kappa^2}\bigl(G_{\mu\nu}+\Lambda g_{\mu\nu}\bigr)-\tfrac12T_{\mu\nu}=0\iff G_{\mu\nu}+\Lambda g_{\mu\nu}=\kappa^2T_{\mu\nu}
$$
$$
\implies\kappa=\text{the}\ S_{\mathrm{geom}}\ \text{coefficient (no other normalization admits source}=T_{\mu\nu});\qquad
\text{dimensions}\ [\mathrm{CT2.1}]:\ \text{both sides}\ \mathfrak q^{+1}.\ \blacksquare
$$

**Phys.** Varying the derived effective action yields Einstein-type field equations with a cosmological term and the ledger-sourced stress tensor — and simultaneously fixes $\kappa$ as that coefficient. In this corpus the field equations of gravity are a theorem with both sides constructed from A1–A9.

**Rmk (dependency audit).** The field-equation chain (CT1.20 $\to$ CT1.21 $\to$ CT1.22 $\to$ CT1.23, conservation CT1.24/CT1.26) rests solely on the declared inputs listed in A §0.2a (CT2.6 (i)–(iii) via CT1.19/CT2.6; Lovelock [math]) — no clause depends on persistence data, on any tick-rate/field coupling (count $0$ in Parts 1–2), or on the materialization-selection question (outside Parts 1–2; downstream of and disjoint from this derivation); the spatial components are no shakier than the temporal ones. On-shell interface: CT1.19 Rmk. The "chosen vs forced" upgrade claim has no corpus referent and is blocked by proven no-gos.

---

### CT1.24 — Conservation from the field equations

**Thm.** $\ \Lambda=\mathrm{const}\implies\nabla^\mu T_{\mu\nu}=0.$

**Req.** CT1.23, CT2.9 ($\kappa\ne0$); contracted Bianchi $\nabla^\mu G_{\mu\nu}=0$; metric compatibility $\nabla^\mu g_{\mu\nu}=0$ [math].

**Pf.**
$$
\nabla^\mu G_{\mu\nu}=0\ [\text{Bianchi}];\qquad\nabla^\mu(\Lambda g_{\mu\nu})=\Lambda\nabla^\mu g_{\mu\nu}=0\ [\text{compatibility};\ \Lambda=\mathrm{const}]
$$
$$
\nabla^\mu(\mathrm{CT1.23}):\ \ 0+0=\kappa^2\nabla^\mu T_{\mu\nu};\qquad\kappa^2=\tfrac{2\pi\mathfrak h^2}{\ln2}>0\ [\mathrm{CT2.9}]\implies\nabla^\mu T_{\mu\nu}=0.\ \blacksquare
$$

**Phys.** The Bianchi identity forces covariant conservation of the ledger stress tensor: energy–momentum conservation is a geometric consequence of the field equations, never an extra assumption.

---

### CT1.25 — The cosmological constant is the $D^+$ aspect

**Thm.** $\ F_{D^+}=\Lambda\mathbb I\implies T^{(D^+)}_{\mu\nu}=-\dfrac{\Lambda}{\kappa^2}g_{\mu\nu};\qquad\rho_{D^+}=\dfrac{\Lambda}{\kappa^2};\quad p_{D^+}=-\rho_{D^+};\quad w_{D^+}:=\dfrac{p}{\rho}=-1.$

**Req.** A8; D4.3; CT1.3 (Part 1), CT1.21, CT1.22; $\delta\sqrt{-g}$ identity [math].

**Pf.**
$$
E_0\in Z\ [\mathrm{CT1.3}]\implies D^+\ \text{commutes with every aspect}\implies\neg\exists\ \text{preferred direction}:\ \text{uniform}\wedge\text{isotropic}
$$
$$
S_{\mathrm{geom}}\ni-\frac{1}{\kappa^2}\int d^4x\sqrt{-g}\,\Lambda\quad[\mathrm{CT1.21}]
$$
$$
T^{(D^+)}_{\mu\nu}=-\frac{2}{\sqrt{-g}}\frac{\delta}{\delta g^{\mu\nu}}\Bigl(-\frac{\Lambda}{\kappa^2}\int\sqrt{-g}\Bigr)=-\frac{\Lambda}{\kappa^2}g_{\mu\nu}\quad[\mathrm{CT1.22}\ \text{definition};\ \delta\sqrt{-g}]
$$
$$
\propto g_{\mu\nu}\implies\neg\exists\ \text{rest frame};\qquad
-\rho\,g_{\mu\nu}\overset!=(\rho+p)u_\mu u_\nu+p\,g_{\mu\nu}\implies\rho+p=0\implies p=-\rho
$$
$$
\rho_{D^+}=\frac{\Lambda}{\kappa^2};\qquad w_{D^+}=\frac{p}{\rho}=-1\ \ (\text{derived},\ \text{zero freedom});\qquad\Lambda=\text{configuration data}\ [\mathrm{P4}].\ \blacksquare
$$

**Phys.** The uniform aspect behaves exactly as a cosmological fluid with equation of state $w=-1$: negative pressure equal in magnitude to its energy density — a derived value with no freedom. Only its magnitude $\Lambda$ remains configuration data (P4): the corpus predicts the dark-energy equation of state, not its size.

---

### CT1.26 — Conservation from mask invariance alone

**Thm.** $\bigl(\mathcal P_M^{(n)}\bigr)^2=\mathcal P_M^{(n)}$ $\ \wedge\ $ weight invariance under mask-preserving relabeling $\implies\nabla_\mu T^{\mu\nu}=0$, independently of CT1.23.

**Req.** CT1.22 ($T$ definition), CT2.2; $\delta_\xi g_{\mu\nu}=\nabla_\mu\xi_\nu+\nabla_\nu\xi_\mu$; integration by parts; fundamental lemma ($\forall\xi$ compact: $\int f\xi=0\Rightarrow f=0$) [math].

**Pf.**
$$
\mathrm{CT2.2}:\ \text{sum runs over}\ \operatorname{Im}\mathcal P_M^{(n)}\implies\text{invariant under image-preserving transformations}
$$
$$
\xi^\mu=\text{infinitesimal relabeling};\ \ \text{mask}\wedge\text{weights invariant}\ [\text{hyp}]\implies\delta_\xi Z=0
$$
$$
\delta_\xi g_{\mu\nu}=\nabla_\mu\xi_\nu+\nabla_\nu\xi_\mu\quad[\text{Lie derivative}]
$$
$$
0=\delta_\xi\log Z=\int d^4x\sqrt{-g}\,\tfrac12T^{\mu\nu}\bigl(\nabla_\mu\xi_\nu+\nabla_\nu\xi_\mu\bigr)=\int d^4x\sqrt{-g}\,T^{\mu\nu}\nabla_\mu\xi_\nu\quad[T^{\mu\nu}=T^{\nu\mu}]
$$
$$
\xi\ \text{compactly supported}:\ \ \text{IBP}\implies0=-\int d^4x\sqrt{-g}\,\bigl(\nabla_\mu T^{\mu\nu}\bigr)\xi_\nu\implies\nabla_\mu T^{\mu\nu}=0\quad[\text{fundamental lemma}].\ \blacksquare
$$

**Phys.** Conservation has a second, independent origin: invariance of the ledger sum under relabelings — discrete diffeomorphism invariance. CT1.24 and CT1.26 are two separate routes to $\nabla T=0$; their agreement is a consistency check on the whole continuum layer.

---

### CT1.27 — Quantum geometry state

**Thm.** $A(C):=\sum_\sigma w(C)$; $\ \{|g(C)\rangle\}:\ \langle g(C)|g(C')\rangle=\delta_{CC'}$. Then
$$
|\Psi\rangle:=\sum_CA(C)\,|g(C)\rangle\in\mathcal H\ [\mathrm{CT2.8}];\qquad
Z_B=\langle B|\Psi\rangle\ \ \forall\ \text{boundary}\ |B\rangle;\qquad
\langle B|=\Theta\text{-dual}\implies Z=\langle\Psi|\Psi\rangle=\sum_C|A(C)|^2\ge0;
$$
$$
\text{classical metric}:=g^\ast_{\mu\nu}=g_{\mu\nu}(C^\ast),\ \ \delta\Phi(C^\ast)=0\ [\mathrm{CT1.20}];\qquad
\text{fluctuations}:=\delta g_{\mu\nu}(C)=g_{\mu\nu}(C)-g^\ast_{\mu\nu}\ \ (\text{subleading}\ [\mathrm{CT1.19}]).
$$

**Req.** A8; CT1.12, CT1.19, CT1.20, CT2.8.

**Pf.**
$$
Z(\mathcal R)=\sum_C\sum_\sigma w(C)=\sum_CA(C)\quad[\mathrm{A8}]\implies\text{coefficients}=\text{terms of}\ Z
$$
$$
\mathrm{CT1.12}:\ C\mapsto g_{\mu\nu}(C);\quad\langle g(C)|g(C')\rangle=\delta_{CC'}\ [\text{declaration}]\implies|\Psi\rangle\in\mathcal H\ [\mathrm{CT2.8}]
$$
$$
Z_B=\langle B|\Psi\rangle\quad[\text{linearity}];\qquad
\langle B|=\Theta\text{-dual}:\ \ Z=\sum_C|A(C)|^2=\langle\Psi|\Psi\rangle\ge0\quad[\mathrm{CT2.8}(3)]
$$
$$
\mathrm{CT1.20}:\ \text{dominant}\ C^\ast:\ \delta\Phi(C^\ast)=0;\quad g^\ast:=g(C^\ast);\quad\text{non-stationary subleading in the}\ \mathfrak h\text{-expansion}\ [\mathrm{CT1.19}].\ \blacksquare
$$

**Phys.** The corpus carries genuine quantum states of geometry: superpositions of emergent metrics weighted by ledger amplitudes, with positive-definite inner product. Classical spacetime is the stationary-phase component; the rest of the ket is quantum geometry — superposition applied to metrics themselves, built from A8.

---

### CT1.28 — Singularity resolution by the saturation lock

**Thm.** $\kappa_{\mathrm{ind}}(v):=$ accessible curvature indicator at $v$ (built from accessible registrations):
$$
\kappa_{\mathrm{ind}}(v)\le f\bigl(C_{\mathrm{cap}},\mathfrak h\bigr)=f(16,\mathfrak h)<\infty\quad\forall\,\mathfrak h>0;
\qquad\Longrightarrow\quad\neg\exists\ \text{accessible curvature singularity}.
$$
(Bound $\mathfrak h$-dependent: $\to\infty$ as $\mathfrak h\to0$; finite at fixed $\mathfrak h>0$.)

**Req.** D1.11, D4.1, D4.2; CT0.5, CT0.6, CT0.11 (Part 1), CT1.19.

**Pf.**
$$
\mathrm{CT1.19}:\ \text{curvature}=\text{holonomies per unit hop area}=\text{function of registrations}\implies\text{singularity}\Rightarrow\text{accessible information density unbounded}
$$
$$
\mathrm{D1.11}:\ \text{accessible content at}\ v\leftrightarrow n(v);\qquad
\mathrm{CT0.5}/\mathrm{CT0.6}:\ D_{\mathrm{tick}}(n)=2^{n+1},\ C_{\mathrm{cap}}=16
$$
$$
\mathrm{CT0.11}:\ \text{admissible}\iff n\le3;\qquad n\ge4\implies O(n)=2^{n+1}-16>0
$$
$$
\mathrm{D4.1}/\mathrm{D4.2}:\ n\ge4\implies\text{config}\in F_{D^-},\ \text{excess absorbed}\wedge\text{locked}\ (\in\mathfrak L,\ \neg\text{accessible})
$$
$$
\implies\text{accessible}:\ n\le3\ \wedge\ \text{registers}\le16\implies\kappa_{\mathrm{ind}}\le f(16,\mathfrak h)<\infty\ \ (\mathfrak h>0).\ \blacksquare
$$

**Phys.** Divergent curvature would require unbounded accessible information at a vertex, but the channel caps access at rung 3 / 16 registers and routes all excess into the locked dark sector. Singularities are not cured by new forces — they are administratively excluded: oversubscription is absorbed before it can become geometry.

---

## §C.IV — Entropy, Calibration, and the Single Free Scale

### CT1.29 — Boundary entropy from channel capacity

**Thm.** $\partial\mathcal B:$ closed real-edge surface separating a $D^-$-locked interior. Then
$$
\Omega_{\partial\mathcal B}=2^{\,n_{\mathcal R}(\partial\mathcal B)};\qquad
S_{\partial\mathcal B}=\ln\Omega_{\partial\mathcal B}=n_{\mathcal R}(\partial\mathcal B)\ln2\ \ \text{nats}=n_{\mathcal R}(\partial\mathcal B)\ \ \text{bits};
$$
$$
A:=n_{\mathcal R}(\partial\mathcal B)\,\mathfrak h^2\implies S_{\partial\mathcal B}=\frac{A}{\mathfrak h^2}\ln2 .
$$

**Req.** A2; C9; CT0.9 (Part 1), CT1.19.

**Pf.**
$$
\mathrm{A2}:\ \text{each pair carries}\ 1\mathfrak q\implies\text{each boundary real edge}=1\ \text{independent channel}
$$
$$
\mathrm{CT0.9}:\ \phi_e\in\{0,\pi\}\implies2\ \text{microstates per edge},\ \neg\text{more}
$$
$$
\text{edges independent}\implies\Omega_{\partial\mathcal B}=2^{\,n_{\mathcal R}(\partial\mathcal B)};\qquad
S_{\partial\mathcal B}=\ln\Omega_{\partial\mathcal B}=n_{\mathcal R}(\partial\mathcal B)\ln2\ \ \text{nats}=n_{\mathcal R}(\partial\mathcal B)\ \text{bits}\ [\mathrm{C9}]
$$
$$
\mathrm{CT1.19}:\ \text{edge subtends hop length}\ \mathfrak h\implies\text{area per pierced boundary element}=\mathfrak h^2\implies A=n_{\mathcal R}(\partial\mathcal B)\,\mathfrak h^2
$$
$$
\implies n_{\mathcal R}(\partial\mathcal B)=A/\mathfrak h^2\implies S_{\partial\mathcal B}=\frac{A}{\mathfrak h^2}\ln2\ \ (\neg\exists\ \text{constant beyond}\ \mathfrak h).\ \blacksquare
$$

**Phys.** Boundary entropy is the boundary’s channel capacity counted in bits: one bit per hop-area $\mathfrak h^2$. The area law is a theorem of capacity bookkeeping — its form $S\propto A$ is derived, and its coefficient sets the calibration of gravity (CT2.9).

---

### CT1.29a — The mean edge quantum: structure, sign, and the exactness locus of the entropy–area rate

**Thm.** Hypotheses: (i) $c$ a closed real-edge chain (bound content [D1.5]); (ii) per-edge integer quanta $\kappa_e:=\widehat{ds}^{\,2}(e)\in\mathbb Z_{\ge1}$ [D1.6, CT1.19a; all-nonnull class], with $\Theta(c):=\sum_{e\in c}\kappa_e$, $\delta h(c):=n_{\mathcal R}(c)$, $\bar\kappa(c):=\Theta/\delta h$. The hypothesis class is nonempty on materialized closed chains of the fully antialigned class [CT1.19b(3)]. Then, as exact identities over $\mathbb Q$:
$$(1)\quad S_{\mathrm{reg}}(c)=\delta h\ln2\ [\mathrm{CT0.9},\ \mathrm{C9}];\qquad A_{\mathrm{loop}}(c):=\Theta\,\mathfrak h^2\ [\mathrm{D1.6}];\qquad \frac{S_{\mathrm{reg}}}{A_{\mathrm{loop}}}=\frac{\ln2}{\mathfrak h^2}\cdot\frac1{\bar\kappa}=\frac{\delta h\ln2}{\Theta\,\mathfrak h^2};
$$
$$(2)\quad \text{CT1.29's rate }\ S=\frac{A}{\mathfrak h^2}\ln2\ \text{holds exactly on }\ c\iff\bar\kappa=1\iff\kappa_e\equiv1\ \text{pointwise};
$$
$$(3)\quad \bar\kappa\ge1\ \text{with equality}\iff\kappa\equiv1;\qquad \operatorname{sign}:\ \bar\kappa>0\ \text{always}\ (\Theta\ge\delta h\ge1);\qquad \bar\kappa\in\tfrac1{\delta h}\mathbb Z_{\ge\delta h};
$$
$$(4)\quad \text{uniform-}\kappa\ \text{chains}:\ \bar\kappa=\kappa\in\mathbb Z_{\ge1}\ (\text{exact rate only at }\kappa=1);\qquad\text{deviation}=\frac1{\bar\kappa}\in\mathbb Q:\ \neg\text{free parameter}\ [\mathrm{P1},\ \mathrm{P5}].
$$

**Req.** D1.5, D1.6, D3.7; C9; CT0.9 (Part 1); CT1.19a, CT1.29 (Part 2); hypotheses (i)–(ii) above (declared at use; realization on materialized closed chains of the fully antialigned class — CT1.19b(3), A §0.2a note); exact rational arithmetic [math; machine: `checks/verify_merge_tierA.py` §F].

**Pf.**
$$(1):\ 1\ \text{real edge}=\ln2\ \text{nats}\ [\mathrm{CT0.9}]\implies S_{\mathrm{reg}}=\delta h\ln2;\qquad A_{\mathrm{loop}}=\oint_c ds^2=\sum_e\widehat{ds}^{\,2}(e)\,\mathfrak h^2=\Theta\,\mathfrak h^2\ [\mathrm{D1.6}]
$$
$$
\frac{S_{\mathrm{reg}}}{A_{\mathrm{loop}}}=\frac{\delta h\ln2}{\Theta\,\mathfrak h^2}=\frac{\ln2}{\mathfrak h^2}\cdot\frac{\delta h}{\Theta}=\frac{\ln2}{\mathfrak h^2}\cdot\frac1{\bar\kappa}.\ \blacksquare_{(1)}
$$
$$(2):\ \text{CT1.29}:\ S_{\partial\mathcal B}=\frac{A}{\mathfrak h^2}\ln2\iff S_{\mathrm{reg}}/A_{\mathrm{loop}}=\ln2/\mathfrak h^2\iff\bar\kappa=1\ (1);\qquad \kappa_e\ge1\ \forall e\implies\bar\kappa=1\iff\kappa_e=1\ \forall e
$$
$$(3):\ \Theta=\sum\kappa_e\ge\sum1=\delta h\ge1;\qquad \bar\kappa=\Theta/\delta h\in\tfrac1{\delta h}\mathbb Z;\qquad(4):\ \kappa_e\equiv\kappa\implies\Theta=\kappa\,\delta h.\ \blacksquare
$$

**Phys.** The Bekenstein-type rate of CT1.29 is exact precisely on minimal chains; every heavier integer winding dilutes it by the rational factor $1/\bar\kappa$ — computable from ledger data, never fitted. The sign question is settled with the structure: the mean edge quantum is a positive rational of the form (loop total)/(hop count), integer exactly on uniform chains.

---

### CT2.9 — Calibration closure

**Thm.** $G_N$ defined by $S_{\partial\mathcal B}\overset!=\dfrac{A}{4G_N}$; $\ \kappa$ by the CT1.23 normalization. Then
$$
\mathfrak h^2=4\,G_N\ln2\iff G_N=\frac{\mathfrak h^2}{4\ln2};\qquad
\kappa^2=8\pi G_N=\frac{2\pi\,\mathfrak h^2}{\ln2};\qquad
\frac{A}{4G_N}=\frac{A\ln2}{\mathfrak h^2}=S_{\partial\mathcal B};
$$
$$
[G_N]=[\kappa^2]=\mathfrak q^{-1}\ [\mathrm{CT2.1}];\qquad G_N,\kappa=\text{names for combinations of}\ \mathfrak h\ (\neg\text{independent}).
$$

**Req.** CT1.23, CT1.29, CT2.1.

**Pf.**
$$
\mathrm{CT1.29}:\ \ S_{\partial\mathcal B}=\frac{A\ln2}{\mathfrak h^2};\qquad
\frac{A\ln2}{\mathfrak h^2}=\frac{A}{4G_N}\iff\frac{\ln2}{\mathfrak h^2}=\frac{1}{4G_N}\iff\mathfrak h^2=4G_N\ln2\iff G_N=\frac{\mathfrak h^2}{4\ln2}
$$
$$
\text{check}:\ \ \frac{A}{4\cdot\dfrac{\mathfrak h^2}{4\ln2}}=\frac{A\ln2}{\mathfrak h^2}=S_{\partial\mathcal B}\quad(\ln2\ \text{appears once},\ \neg\text{twice})
$$
$$
\mathrm{CT1.23}:\ S_{\mathrm{geom}}\ \text{coefficient}=\tfrac{1}{2\kappa^2},\ \text{source}=T_{\mu\nu}\implies\kappa^2:=8\pi G_N=8\pi\cdot\frac{\mathfrak h^2}{4\ln2}=\frac{2\pi\,\mathfrak h^2}{\ln2}
$$
$$
[\mathfrak h^2]=\mathfrak q^{-1}\implies[G_N]=[\kappa^2]=\mathfrak q^{-1}\ [\mathrm{CT2.1}];\qquad\mathfrak h\ \text{given}\implies G_N,\kappa\ \text{determined}.\ \blacksquare
$$

**Phys.** Demanding that the boundary-entropy law take the quarter-area form locks the hop length, Newton’s constant and the gravitational coupling together: $\mathfrak h^2=4G_N\ln2$. The $\ln2$ is the one bit per edge of CT0.9 — the theory’s information quantum appearing directly in the calibration of gravity.

---

### CT2.11 — One free scale

**Thm.**
$$
\forall Q\ \text{dimensionful}:\ \ Q=c_Q\,\mathfrak h^{k_Q},\ c_Q\ \text{fixed};\qquad
\forall q\ \text{dimensionless-derived}:\ \ q=\text{fixed number},\ \mathfrak h\text{-free};
$$
$$
\mathfrak h\mapsto\lambda\mathfrak h:\ \ Q\mapsto\lambda^{k_Q}Q,\quad\text{P2 quantities invariant}\implies\text{rescaling}=\text{symmetry}\implies\exists!\ \text{calibration d.o.f.}
$$

**Req.** D2.9; P1, P2, P4; CT0.5, CT0.6, CT0.11(a), CT1.1 (Part 1); CT1.29, CT2.1, CT2.9; remaining P2 entries (**D**, **E**, **F**, **G**).

**Pf.**
$$
\text{sole dimensionful input}=\mathfrak h\quad[\mathrm{D2.9},\ \mathrm{P1}]
$$
$$
\mathrm{CT2.9}:\ G_N,\kappa^2=\text{fixed multiples of}\ \mathfrak h^2;\quad\mathrm{CT2.1}:\ \text{lengths/areas/energies/densities}=\text{fixed powers};\quad\mathrm{CT1.29}:\ S=\text{pure count}
$$
$$
\mathrm{P2}:\ (7,3,3,3)\ [\mathrm{CT1.1}];\ 16\ [\mathrm{CT0.6}];\ 2^{n+1}\ [\mathrm{CT0.5}];\ n\le3,\ \mathbb C^3\ [\mathrm{CT0.11(a)}];\ \text{rest}:\ \mathbf{D},\mathbf{E},\mathbf{F},\mathbf{G}\quad\text{--- all}\ \mathfrak h\text{-free}
$$
$$
\mathfrak h\mapsto\lambda\mathfrak h:\ \ Q\mapsto\lambda^{k_Q}Q;\quad\mathrm{P2}\ \text{invariant}\implies\text{rescaling}=\text{symmetry of the corpus}\implies\mathfrak h=\text{genuine single d.o.f.}\ (\neg\text{internal redundancy})
$$
$$
\mathrm{P4}:\ (g,g',h_0,\Lambda,\varkappa,\beta,\alpha_\Omega)=\text{solution data},\ \neg\text{theory constants};\qquad
\text{predictions}=\text{dimensionless ratios at fixed P4 data}.\ \blacksquare
$$

**Phys.** The entire corpus has exactly one dial: the hop length. Turning it rescales every dimensionful quantity uniformly and leaves every pure-number prediction untouched. Comparing to external measurement means fixing $\mathfrak h$ once — an act that tests A9, never an input to A1–A8.

---

## Closure exports of Part 2 §C (consumed by Part 2 §D–§G, Parts 3–4)

$$
\begin{array}{lll}
\mathrm{CT1.12}\ g_{\mu\nu}=\Omega^2\bar g_{\mu\nu},\ \operatorname{sig}=(-,+,+,+) &
\mathrm{CT1.13\text{–}17}\ \text{conformal laws} &
\mathrm{CT1.18}\ \bar G^{(1)}=-\tfrac12\Box\hat h^{(4)}\ (\text{TT})\\
\mathrm{CT2.1}\ [\cdot]=\mathfrak q\text{-powers} &
\mathrm{CT2.2\text{–}2.4}\ \mathcal P_M^{(n)}\ \text{projection};\ \mathbf F_M^{(n)}=\bigoplus_{\mathcal A(n)}F_A &
\mathrm{CT2.5}\ Z(\mathcal R,n)\ \text{poles}=\text{spectrum}\\
\mathrm{CT2.6}\ M\ \text{smooth 4-manifold} &
\mathrm{CT2.7}/\mathrm{CT1.21}\ S_{\mathrm{geom}}=\tfrac{1}{2\kappa^2}\int\sqrt{-g}(R-2\Lambda) &
\mathrm{CT2.8}\ \text{Hilbert space};\ \langle A|A\rangle\ge0\\
\mathrm{CT1.19}\ \sum ds^2\to\int g\,dx\,dx &
\mathrm{CT1.20}\ S_{\mathrm{eff}}=-i\log Z &
\mathrm{CT1.22}\ T_{\mu\nu}=T^{\mathrm{bd}}+T^{\mathrm{tr}}\\
\mathrm{CT1.23}\ G_{\mu\nu}+\Lambda g_{\mu\nu}=\kappa^2T_{\mu\nu} &
\mathrm{CT1.24}/\mathrm{CT1.26}\ \nabla^\mu T_{\mu\nu}=0\ (\times2\ \text{routes}) &
\mathrm{CT1.25}\ w_{D^+}=-1\\
\mathrm{CT1.27}\ |\Psi\rangle=\sum_CA(C)|g(C)\rangle &
\mathrm{CT1.28}\ \kappa_{\mathrm{ind}}\le f(16,\mathfrak h) &
\mathrm{CT1.29}\ S_{\partial\mathcal B}=\tfrac{A}{\mathfrak h^2}\ln2\\
\mathrm{CT2.9}\ \mathfrak h^2=4G_N\ln2;\ \kappa^2=\tfrac{2\pi\mathfrak h^2}{\ln2} &
\mathrm{CT2.10}\ \operatorname{Str}[X,Y\}=0 &
\mathrm{CT2.11}\ \exists!\ \text{free scale}\ \mathfrak h
\end{array}
$$

$\blacksquare$

---

## §D — Electroweak Sector

*Dep.: Part 1; Part 2 §C. EW.1–EW.4, EW.6, EW.19 are restatement stubs of prior tags (cited nowhere downstream); forward pointer: EW.36$\to$EM.9 (restated at use); EW.8$\to$EW.32 is intra-section. Notation: carrier images $W_i\mapsto\tfrac12\sigma_i$, $Y_{\mathrm{car}}=\tfrac12\sigma_0$ (EW.32); $Y$ — electromagnetic generator with three realizations ($Y_{\mathrm{asp}},Y_{\mathrm{slot}},Y_{\mathrm{car}}$). Machine: `checks/verify_D.py`; EW.5a/EW.36a: `checks/verify_merge_tierA.py`.*

## §D.I — Operator Preliminaries

### EW.1 — Joint $(S,T)$ sector decomposition

**Thm.** $\equiv$ CT1.1: $\ \mathfrak H(\mathbb C^4)=\mathcal E_{++}\oplus\mathcal E_{+-}\oplus\mathcal E_{-+}\oplus\mathcal E_{--}$, $\ \dim=(7,3,3,3)$.

**Req.** CT1.1 (Part 1).

**Pf.** Identity [CT1.1]. $\blacksquare$

**Phys.** The arena of the electroweak sector: the weak triplet will live in the $T$-odd symmetric block $\mathcal E_{+-}$ of the pair operator space.

---

### EW.2 — Generator basis and sector assignment

**Thm.** $\equiv$ CT1.2: $\ \{E_0,\Sigma,\hat E^{ij}\}\subset\mathcal E_{++}\ (1,1,5);\ \ W_i\in\mathcal E_{+-}\ (3);\ \ J_i\in\mathcal E_{-+}\ (3);\ \ K_i\in\mathcal E_{--}\ (3);\ \ 1{+}1{+}5{+}3{+}3{+}3=16$.

**Req.** CT1.2 (Part 1).

**Pf.** Identity [CT1.2]. $\blacksquare$

**Phys.** Fixes the named generators ($W_i$ total spin, $J_i,K_i$ Janus seals, $\Sigma$ exchange scalar) used throughout this document.

---

### EW.3 — The $W_i$ close $\mathfrak{su}(2)$

**Thm.** $\equiv$ CT1.4: $\ [W_i,W_j]=i\,\epsilon_{ijk}W_k$; $\ \operatorname{span}_{\mathbb R}\{W_i\}\cong\mathfrak{su}(2)$ [C2].

**Req.** CT1.4 (Part 1).

**Pf.** Identity [CT1.4]. $\blacksquare$

**Phys.** The weak-isospin algebra is the total-spin algebra of the qubit pair — present from rung 1 (CT0.13), not installed at rung 2.

---

### EW.4 — Central, trace, and mixed commutators

**Thm.** $\equiv$ CT1.3, CT1.5, CT1.6, CT1.7:
$$
(1)\ [E_0,X]=0\ \ \forall X;\qquad
(2)\ [\Sigma,W_i]=0;\qquad
(3)\ [\Sigma,J_i]=4iK_i,\ \ [\Sigma,K_i]=-4iJ_i;
$$
$$
(4)\ [J_i,J_j]=[K_i,K_j]=i\,\epsilon_{ijk}W_k;\qquad
(5)\ [J_i,K_j]=i\bigl(\delta_{ij}\Sigma-E^{ij}\bigr).
$$

**Req.** CT1.3, CT1.5, CT1.6, CT1.7 (Part 1).

**Pf.** Identities [CT1.3, CT1.5, CT1.6, CT1.7]. $\blacksquare$

**Phys.** The commutator backbone of the sector: the scalar $\Sigma$ commutes with the weak triplet but rotates the two Janus sectors into each other; seals close onto the weak triplet; mixed seals close into the metric block.

---

### EW.5 — Second-order Higgs-to-weak pathways

**Thm.**
$$
\bigl[K_j,[\Sigma,J_i]\bigr]=4\,\epsilon_{ijk}W_k;\qquad
\bigl[J_j,[\Sigma,K_i]\bigr]=-4\,\epsilon_{ijk}W_k;
$$
$$
[J_j,K_i]\in\mathcal E_{++}\ \wedge\ \mathcal E_{++}\cap\operatorname{span}\{W_k\}=\{0\}\implies\text{the}\ [J,K]\ \text{pathway}\ \neg\text{reaches the weak sector}.
$$

**Req.** EW.4 (= CT1.5, CT1.6, CT1.7); CT1.1 (direct sum), CT1.2.

**Pf.**
$$
[\Sigma,J_i]=4iK_i\ \implies\ \bigl[K_j,[\Sigma,J_i]\bigr]=4i\,[K_j,K_i]=4i\cdot i\,\epsilon_{jik}W_k=-4\,\epsilon_{jik}W_k=4\,\epsilon_{ijk}W_k\quad[\mathrm{EW.4}(3),(4)]
$$
$$
[\Sigma,K_i]=-4iJ_i\ \implies\ \bigl[J_j,[\Sigma,K_i]\bigr]=-4i\,[J_j,J_i]=-4i\cdot i\,\epsilon_{jik}W_k=4\,\epsilon_{jik}W_k=-4\,\epsilon_{ijk}W_k
$$
$$
[J_j,K_i]=i\bigl(\delta_{ji}\Sigma-E^{ji}\bigr)\in\mathcal E_{++}\ [\mathrm{EW.4}(5),\ \mathrm{EW.2}];\qquad
W_k\in\mathcal E_{+-};\quad\text{direct sum}\ [\mathrm{EW.1}]\implies\mathcal E_{++}\cap\operatorname{span}\{W_k\}=\{0\}.\ \blacksquare
$$

**Phys.** Although the scalar commutes with the weak triplet, it reaches it at second adjoint order — and only through the Janus seals. The scalar’s unique algebraic handle on the weak sector runs through crystallization/dissolution: the algebraic shadow of the wrapping mechanism that actually generates mass in Part IV.

---

### EW.5a — Convention exactness and the rigidity of the named basis

**Thm.** In the Pauli basis of $\mathfrak H(\mathbb C^4)$ [A3, CT1.1], with CT1.2's definitions verbatim ($E_0=\sigma_0\otimes\sigma_0$, $\Sigma=\sum_i\sigma_i\otimes\sigma_i$, $W_i=\tfrac12(\sigma_0\otimes\sigma_i+\sigma_i\otimes\sigma_0)$, $J_i=\tfrac12(\sigma_j\otimes\sigma_k-\sigma_k\otimes\sigma_j)$ cyclic, $K_i=\tfrac12(\sigma_0\otimes\sigma_i-\sigma_i\otimes\sigma_0)$, $E^{ij}=\tfrac12(\sigma_i\otimes\sigma_j+\sigma_j\otimes\sigma_i)$), as **exact matrix equalities over $\mathbb Q(i)$** (no tolerance, no floats):
$(1)$ **The frozen identities hold exactly as stated.** CT1.3 (16 brackets), CT1.4 (6 ordered pairs), CT1.5 (9), CT1.6 with $+i\epsilon_{ijk}W_k$ (12; no sign residue), CT1.7 (9, each with all three $W$-components exactly zero), CT1.8 (12); **EW.5 both clauses at all nine $(i,j)$** (diagonal $i=j$: both sides exactly $0$); CT0.7a; CT0.7(1) (incl.\ $\mathfrak T\Pi_{\mathcal R}=3$, $\mathfrak T\Pi_{\mathcal V}=1$, ranks $3/1$); the associative relation $\Sigma^2=3E_0-2\Sigma$; $[S,T]=0$ on all 16 basis elements with $\eta=(-,+,+,+)$ [A3]; the full $(S,T)$ parity table of CT1.2 (17 generators).
$(2)$ **The convention group is exactly $\mathbb Z_2$.** The group of diagonal sign redefinitions $(J,K,W,\Sigma,E)\mapsto(\lambda_JJ,\lambda_KK,\lambda_WW,\lambda_\Sigma\Sigma,\lambda_EE)$, $\lambda\in\{\pm1\}^5$, with $E_0=I_4$ fixed (the unit), preserving every identity of clause (1) — including $\Sigma^2=3E_0-2\Sigma$ and $\mathbb S=\tfrac12(E_0+\Sigma)$ — is exactly
$$\{\mathrm{id},\ \operatorname{Ad}(\mathbb S)\}\cong\mathbb Z_2,\qquad \operatorname{Ad}(\mathbb S):\ (J_i,K_i)\mapsto(-J_i,-K_i),\quad W_i,\Sigma,E^{ij},E_0\ \text{fixed}$$
(exactly $2$ of the $32$ sign maps survive; exhaustive enumeration).
$(3)$ **EW.5 is invariant under the nontrivial element** (each clause maps to itself: $J,K$ flip together). The naming exchange $J\leftrightarrow K$ maps clause 1 of EW.5 to clause 2 with the wrong sign and is *excluded* by the frozen identity set; Hermiticity excludes continuous phases ($e^{i\varphi}K_i$ Hermitian $\Rightarrow\varphi\in\{0,\pi\}$ — the sign enumeration is exhaustive).

**Req.** A3; C1, C2, C3; CT0.7, CT0.7a, CT1.1–CT1.8 (Part 1); EW.4, EW.5; exact $\mathbb Q(i)$ matrix arithmetic, exhaustive $2^5$ sign enumeration [math; machine: `checks/verify_merge_tierA.py` §B].

**Pf.**
$$(1):\ \text{each identity evaluated entrywise over}\ \mathbb Q(i)\ \text{from CT1.2's definitions; zero residual}\ [\text{machine}]$$
$$(2):\ (\lambda_\Sigma\Sigma)^2=3E_0-2\lambda_\Sigma\Sigma\ \wedge\ \lambda_\Sigma^2=1\ \wedge\ \Sigma^2=3E_0-2\Sigma\ \wedge\ \Sigma\ne0\implies\lambda_\Sigma=1$$
$$\mathrm{CT1.5}:\ \lambda_\Sigma\lambda_J=\lambda_K\ \wedge\ \lambda_\Sigma\lambda_K=\lambda_J\implies\lambda_J=\lambda_K;\qquad \mathrm{CT1.7}:\ \lambda_J\lambda_K=\lambda_\Sigma=1\ \wedge\ \lambda_J\lambda_K=\lambda_E\implies\lambda_E=1$$
$$\mathrm{CT1.6}:\ \lambda_J^2=\lambda_K^2=\lambda_W;\qquad \mathrm{CT1.4}:\ \lambda_W^2=\lambda_W\implies\lambda_W=1;\qquad\implies(\lambda_J,\lambda_K,\lambda_W,\lambda_\Sigma,\lambda_E)\in\{(1,1,1,1,1),(-1,-1,1,1,1)\}$$
$$(-1,-1,1,1,1)=\operatorname{Ad}(\mathbb S):\ \mathbb S J_i\mathbb S=-J_i,\ \mathbb S K_i\mathbb S=-K_i\ [\mathrm{CT0.7}(3):\ J,K\ S\text{-odd}];\quad \mathbb S W_i\mathbb S=W_i,\ \mathbb S\Sigma\mathbb S=\Sigma\ [S\text{-even}]$$
$$(3):\ [K_j,[\Sigma,J_i]]\mapsto[-K_j,[\Sigma,-J_i]]=[K_j,[\Sigma,J_i]]\ \checkmark;\qquad J\leftrightarrow K:\ [J_j,[\Sigma,K_i]]=+4\epsilon_{ijk}W_k\ne-4\epsilon_{ijk}W_k\implies\text{excluded}$$
$$\text{Hermiticity}:\ (e^{i\varphi}K_i)^\dagger=e^{-i\varphi}K_i=e^{i\varphi}K_i\iff e^{2i\varphi}=1\iff\varphi\in\{0,\pi\}.\ \blacksquare$$

**Phys.** The electroweak backbone was accused of a sign slip; the audit finds the opposite — a lock. Once the unit, the associative square of the exchange scalar, and the swap definition are held fixed, the only freedom left in the whole named basis is the simultaneous flip of $J$ and $K$, under which every frozen identity — EW.5 included — is exactly invariant. There is no phase convention left to fix; the basis is rigid up to the one declared $\mathbb Z_2$.

---

## §D.II — Rung Masks and the Electroweak Algebra

### EW.6 — Rung masks and active aspect sets

**Thm.** $\equiv$ CT2.2, CT2.3, CT0.13:
$$
\bigl(\mathcal P_M^{(n)}\bigr)^2=\mathcal P_M^{(n)}=\bigl(\mathcal P_M^{(n)}\bigr)^\dagger;\qquad
\mathbf F_M^{(n)}=\mathcal P_M^{(n)}\mathbf F\,\mathcal P_M^{(n)};
$$
$$
\mathcal A(0)=\{J\};\quad
\mathcal A(1)=\{J,G,W,H,D^+\};\quad
\mathcal A(2)=\mathcal A(1)\cup\{\mathrm{EM}\};\quad
\mathcal A(3)=\mathcal A(2)\cup\{\mathrm{strong}\};\quad
\mathcal A(n\ge4)=\mathcal A(3)\cup\{D^-\}.
$$
$W=\operatorname{span}\{W_1,W_2,W_3\}$: neutral seed $W_3$, $\neg$ independent aspect [C8]; scalar seed $=$ trace mode $h$ of D2.1.

**Req.** CT0.13, CT2.2, CT2.3 (**B**, **C**); C8; D2.1, D3.3.

**Pf.** Identities [CT2.2, CT2.3, CT0.13 — derived there from CT0.7, D3.3, D3.1, D3.2]. $\blacksquare$

**Phys.** Which forces exist at which rung is bookkeeping, already fixed in B: the electroweak content (weak triplet + Higgs scalar + dark + EM centre) is available from rungs 1–2; colour joins only at rung 3.

---

### EW.7 — The rung-2 electroweak mask

**Thm.**
$$
\mathcal A(2)=\{J,\ G,\ W_1,\ W_2,\ W_3,\ H,\ D^+,\ \mathrm{EM}\};\qquad
\mathbf F_M^{(2)}=\mathcal P_M^{(2)}\mathbf F\,\mathcal P_M^{(2)}=\bigoplus_{A\in\mathcal A(2)}F_A\big|_{\mathcal K^{(A)}} .
$$

**Req.** EW.6; CT2.4 (Part 2).

**Pf.**
$$
\mathrm{EW.6}:\ \mathcal A(2)=\mathcal A(1)\cup\{\mathrm{EM}\},\ \ \mathcal A(1)=\{J,G,W,H,D^+\},\ W=\operatorname{span}\{W_1,W_2,W_3\}
$$
$$
\mathrm{CT2.4}:\ \text{mask retains exactly the blocks of}\ \mathcal A(2),\ \text{annihilates the rest}.\ \blacksquare
$$

**Phys.** The rung-2 world carries gravity, weak, Higgs, uniform dark and electromagnetism — and no colour: the electroweak sector is exactly the mask content at rung 2.

---

### EW.8 — The electromagnetic generator

**Thm.** The electromagnetic generator $Y$ is one abstract generator with three realizations:
$$
Y_{\mathrm{slot}}:=Z\bigl(\iota_2(\mathfrak u(2))\bigr)\ (1\text{-dim})\ [\mathrm{D2.12},\mathrm{CT0.13}];\qquad
Y_{\mathrm{asp}}:=\mathcal P^{(\mathrm{EM})}:\ \mathcal K\to\mathcal K^{(\mathrm{EM})},\ \ \operatorname{rk}=1,\ \mathfrak T(Y_{\mathrm{asp}})=1\ [\mathrm{D2.3},\mathrm{CT0.14}];
$$
$$
Y_{\mathrm{car}}:=\tfrac12\sigma_0\ \ \text{on}\ \mathcal H_{\mathsf v}\cong\mathbb C^2\ [\mathrm{EW.32}];
$$
$$
[Y_{\mathrm{asp}},\mathbf F_M^{(n)}]=0\ (\text{block-diagonal});\qquad
[Y_{\mathrm{slot}},\mathfrak{su}(2)]=0;\qquad
[Y_{\mathrm{car}},W_i|_{\mathrm{car}}]=0 .
$$
**Rmk (separation).** $\ \mathcal P_M^{(2)}E_0\mathcal P_M^{(2)}=\mathcal P_M^{(2)}$, $\mathfrak T=17$ [CT2.2, CT0.14]: a mask fact about the *pair* centre $E_0\leftrightarrow F_{D^+}$ [CT0.12] — $\neg$ a definition of $Y$ (the prior codex defined $Y$ this way; repaired).

**Req.** A8; D2.3, D2.12; CT0.12, CT0.13, CT0.14, CT1.2 (Part 1); CT2.2 (Part 2).

**Pf.**
$$
\mathrm{CT0.13}:\ F_{\mathrm{EM}}=\iota_2\bigl(Z(\mathfrak u(2))\bigr),\ 1\text{-dim}\ [\mathrm{D2.12}];\qquad
\mathrm{CT0.14}:\ \dim\mathcal K^{(\mathrm{EM})}=1\implies Y_{\mathrm{asp}}=\mathcal P^{(\mathrm{EM})}:\ \operatorname{rk}1,\ \mathfrak T=1\ [\mathrm{D2.3}]
$$
$$
\mathrm{D2.3}:\ \mathcal K=\bigoplus_A\mathcal K^{(A)}\ \text{orthogonal}\implies[Y_{\mathrm{asp}},\ \text{block-diagonal operators}]=0\implies[Y_{\mathrm{asp}},\mathbf F_M^{(n)}]=0
$$
$$
Z(\mathfrak u(2))\ \text{commutes with the}\ \mathfrak{su}(2)\ \text{factor}\implies[Y_{\mathrm{slot}},\mathfrak{su}(2)]=0;\qquad
[\tfrac12\sigma_0,\tfrac12\sigma_i]=0\ [\text{machine}:\ \text{verify\_D}]
$$
$$
E_0=I_4\ [\mathrm{CT1.2}]\implies\mathcal P_M^{(2)}E_0\mathcal P_M^{(2)}=\mathcal P_M^{(2)}\ [\mathrm{CT2.2}];\quad
E_0\leftrightarrow F_{D^+}\ [\mathrm{CT0.12}]:\ \text{pair-centre fact, kept separate from}\ Y.\ \blacksquare
$$

**Rmk (forward pointer, non-load-bearing).** The carrier realization/transport locus is EW.32 (EW.32 cites EW.8 backward).

**Phys.** Hypercharge is one generator with three coordinated faces: the centre of the rung-2 slot algebra, the rank-one projection onto the EM block, and $\tfrac12\sigma_0$ on the transported seed. Keeping the three apart — and keeping the *pair* centre $E_0$ (which belongs to $D^+$) apart from all of them — is what makes the EM.17 trace formula and the EW.32 charge statements each well-typed.

---

### EW.9 — The abelian algebra

**Thm.** $\ \bigl(\operatorname{span}_{\mathbb R}\{Y\},[\cdot,\cdot]\bigr)\cong\mathfrak u(1):\quad[aY,bY]=ab[Y,Y]=0;\quad\dim=1.$

**Req.** EW.8; Lie-algebra axioms [math].

**Pf.**
$$
\dim\operatorname{span}\{Y\}=1\implies[aY,bY]=ab[Y,Y]=0;\qquad\text{Jacobi}\equiv0;\qquad
1\text{-dim abelian}=\mathfrak u(1).\ \blacksquare
$$

**Phys.** One generator, vanishing bracket: the abelian factor of the electroweak algebra.

---

### EW.10 — The rung-2 electroweak algebra

**Thm.**
$$
\mathfrak g_{\mathrm{EW}}:=\operatorname{span}_{\mathbb R}\{W_1,W_2,W_3,Y\}=\mathfrak{su}(2)\oplus\mathfrak u(1);\qquad
[W_i,W_j]=i\,\epsilon_{ijk}W_k;\quad[W_i,Y]=0;\quad[Y,Y]=0;\quad\dim\mathfrak g_{\mathrm{EW}}=4 .
$$

**Req.** EW.3, EW.8, EW.9; direct-sum criterion (two commuting ideals, trivial intersection) [math].

**Pf.**
$$
\operatorname{span}\{W_i\}\cong\mathfrak{su}(2)\ [\mathrm{EW.3}];\qquad\operatorname{span}\{Y\}\cong\mathfrak u(1)\ [\mathrm{EW.9}]
$$
$$
[Y,W_i]=0\ [\mathrm{EW.8}]\implies\text{each factor an ideal of the sum}
$$
$$
Y\in Z(\mathfrak g_{\mathrm{EW}});\quad\text{no nonzero}\ \textstyle\sum c_iW_i\ \text{central}\ [\mathrm{EW.3}]\implies\operatorname{span}\{W\}\cap\operatorname{span}\{Y\}=\{0\}
$$
$$
\implies\mathfrak g_{\mathrm{EW}}=\mathfrak{su}(2)\oplus\mathfrak u(1);\qquad\dim=3+1=4.\ \blacksquare
$$

**Phys.** The electroweak gauge algebra of the corpus — $\mathfrak{su}(2)\oplus\mathfrak u(1)$, dimension four — is derived as the algebra generated by the rung-2 mask content. Nothing resembling a gauge principle was assumed.

---

### EW.11 — The mechanism is projection, not path integration

**Thm.** $\mathfrak g_{\mathrm{EW}}$ arises from $\bigl(\mathcal P_M^{(2)}\mathbf F\mathcal P_M^{(2)},\ [\cdot,\cdot]\bigr)$ (finite-dimensional restriction); $\ Z(\mathcal R)=\sum_{C}\sum_\sigma w(C)$ (countable sum, A8); continuum $\to$ only after coarse-graining (CT2.6) $\implies\mathfrak g_{\mathrm{EW}}$ fixed before that limit; $\neg\exists$ functional integral over gauge fields in the derivation.

**Req.** A8; CT2.3, CT2.6 (Part 2); EW.10; CT1.4 (Part 1).

**Pf.**
$$
\mathrm{CT2.3}:\ \mathbf F_M^{(2)}=\mathcal P_M^{(2)}\mathbf F\mathcal P_M^{(2)}=\text{operator restriction}\ (\neg\text{integral})
$$
$$
\mathrm{EW.10}\Leftarrow[\mathrm{CT1.4},\ \mathrm{EW.8}]=\text{finite-dimensional matrix identities}
$$
$$
\mathrm{A8}:\ Z(\mathcal R)=\textstyle\sum_{C\in\mathcal R}\sum_\sigma w(C)=\text{sum over a countable set};\qquad
\mathrm{CT2.6}:\ \text{continuum appears only at coarse graining}\implies\text{algebra fixed pre-limit}.\ \blacksquare
$$

**Phys.** The gauge structure is produced by masking a discrete, finite algebra — the continuum functional description is a derived approximation, never the defining mechanism. “Gauge theory” in this corpus names a spectral property of a masked operator sum.

---

## §D.III — The Scalar Trace Mode

### EW.12 — Metric expansion and the scalar trace mode

**Thm.** With D2.1 data:
$$
\delta^{ij}\hat h_{ij}=0;\qquad q_{ij}=\hat h_{ij}+\delta_{ij}h;\qquad h=\tfrac13\Sigma_{\mathrm{tr}};\qquad
\delta_{ij}h\,E^{ij}=h\sum_{i=1}^3E^{ii}=h\,\Sigma .
$$

**Req.** D2.1; C5; CT1.12 (Part 2), EW.2 (= CT1.2).

**Pf.**
$$
\delta^{ij}\hat h_{ij}=\Sigma_{\mathrm{tr}}-\tfrac13\cdot3\cdot\Sigma_{\mathrm{tr}}=0\quad[\mathrm{D2.1},\ \mathrm{CT1.12}]
$$
$$
h=\tfrac13\Sigma_{\mathrm{tr}}\ \text{substituted into}\ \hat h_{ij}=q_{ij}-\tfrac13\delta_{ij}\Sigma_{\mathrm{tr}}\implies q_{ij}=\hat h_{ij}+\delta_{ij}h
$$
$$
E^{ii}=\tfrac12\bigl(\sigma_i\otimes\sigma_i+\sigma_i\otimes\sigma_i\bigr)=\sigma_i\otimes\sigma_i\implies\sum_iE^{ii}=\Sigma\quad[\mathrm{EW.2}].\ \blacksquare
$$

**Phys.** The trace part of the real sector is the operator $h\Sigma$: a scalar field $h$ multiplying the exchange scalar. C5 keeps the bookkeeping honest — $\Sigma$ is an operator, $\Sigma_{\mathrm{tr}}$ a number.

---

### EW.13 — Identification of the scalar mode

**Thm.** The electroweak scalar mode is
$$
H:=h\,\Sigma\qquad(\text{field}\ h;\ \ \text{operator representative}\ h\Sigma),
$$
the noncentral rotation scalar; the central scalar $E_0$ is unavailable (allocated to $F_{D^+}$).

**Req.** CT1.10, CT1.11, CT0.12 (Part 1), CT1.25 (Part 2); EW.1 (= CT1.1), EW.4.

**Pf.**
$$
\dim\mathcal E_{++}=7\ [\mathrm{EW.1}];\qquad\mathcal E_{++}\to\mathbf1\oplus\mathbf5\oplus\mathbf1\ [\mathrm{CT1.10}]:\ \ \text{scalars}=\{E_0,\ \Sigma\}
$$
$$
E_0\in Z;\quad[\Sigma,J_1]=4iK_1\ne0\implies\Sigma\notin Z;\quad E_0\nparallel\Sigma\quad[\mathrm{EW.4}(1),(3);\ \mathrm{CT1.11}]
$$
$$
E_0\ \text{already allocated}:\ F_{D^+}=\Lambda\mathbb I\ [\mathrm{CT0.12}]\to\text{cosmological term}\ [\mathrm{CT1.25}];\quad\text{reallocating}=\text{double counting}
$$
$$
\implies\Sigma=\text{unique remaining rotation-scalar direction}=F_H\ [\mathrm{CT0.12}];\qquad H=h\Sigma.\ \blacksquare
$$

**Phys.** The Higgs-type scalar of the corpus is the exchange scalar weighted by the trace mode: forced, not chosen — once the central scalar has become the uniform dark aspect, exactly one rotation-scalar direction remains, and A8 already names it $F_H$.

---

### EW.14 — The scalar background commutes with the electroweak generators

**Thm.** $\ \forall h_0\in\mathbb R:\quad[h_0\Sigma,\ W_i]=0;\qquad[h_0\Sigma,\ Y_{\mathrm{asp}}]=[h_0\Sigma,\ Y_{\mathrm{car}}]=0.$

**Req.** EW.4(2) (= CT1.5), EW.8.

**Pf.**
$$
h_0\in\mathbb R\implies[h_0\Sigma,X]=h_0[\Sigma,X];\qquad[\Sigma,W_i]=0\ [\mathrm{EW.4}(2)]
$$
$$
[Y_{\mathrm{asp}},F_H\text{-block}]=0\ [\mathrm{EW.8}:\ \text{block-diagonal}];\qquad
[Y_{\mathrm{car}},h_0\Sigma|_{\mathrm{car}}]=0\ [\tfrac12\sigma_0\ \text{central}].\ \blacksquare
$$

**Phys.** A scalar background is invisible to the electroweak algebra at the commutator level — the first half of the statement that this theory has no adjoint Higgs mechanism.

---

### EW.15 — No adjoint electroweak breaking

**Thm.**
$$
\operatorname{Stab}_{\mathfrak g_{\mathrm{EW}}}(h_0\Sigma):=\{X\in\mathfrak g_{\mathrm{EW}}:\ [h_0\Sigma,X]=0\}=\mathfrak g_{\mathrm{EW}}\qquad(\text{full stabilizer});
$$
$$
\implies\neg\exists\ \text{proper subalgebra selected by an adjoint stabilizer mechanism}.
$$
**Consequence.** Any electroweak reduction is a statement about the spectrum of the masked resolvent (Part IV: EW.33 transport), $\neg$ about Lie-algebra stabilizers.

**Req.** EW.10, EW.14.

**Pf.**
$$
\mathrm{EW.14}:\ [h_0\Sigma,X]=0\ \ \forall X\in\{W_1,W_2,W_3,Y\}\implies\operatorname{Stab}=\mathfrak g_{\mathrm{EW}}\implies\neg\exists\ \text{proper reduction by commutators}.\ \blacksquare
$$

**Phys.** The scalar background breaks nothing adjointly: the stabilizer is the whole algebra. Mass generation must therefore be — and in Part IV is — a transport effect on a carried seed, not a commutator effect on generators.

---

### EW.16 — Scalar coupling to the antisymmetric sectors

**Thm.**
$$
[\Sigma,J_i]=4iK_i;\qquad[\Sigma,K_i]=-4iJ_i;\qquad
\bigl[K_j,[\Sigma,J_i]\bigr]=4\,\epsilon_{ijk}W_k;\qquad
\bigl[J_j,[\Sigma,K_i]\bigr]=-4\,\epsilon_{ijk}W_k .
$$

**Req.** EW.4(3), EW.5.

**Pf.** First-order: [EW.4(3)]; second-order: [EW.5]. $\blacksquare$

**Rmk.** $J_i,K_i\ =$ threshold-moving generators [CT0.7]: the scalar’s only algebraic handle on the weak sector runs through crystallization/dissolution — the algebraic shadow of the wrapping mechanism of Part IV.

**Phys.** The scalar talks to the Janus seals at first order and, through them, to the weak triplet at second order. Every algebraic route from the Higgs mode to the weak force passes through the reality-changing generators.

---

## §D.IV — Rung-3 Wrapping, the Seed, and Mass Generation

### EW.17 — Rung-3 closed wrapping chains

**Thm.** $\gamma=$ chain [D1.4]; closed $\iff\#J^+=\#J^-\ \wedge\ \partial\gamma=0$; wrapping $=$ nonzero spatial winding around a closed ledger cycle [D1.7]:
$$
\Theta(\gamma)=\sum_{e\in\gamma}\widehat{ds}^{\,2}(e);\qquad
\Phi(\gamma)=\sum_{e\in\gamma}\alpha_e\,\widehat{ds}^{\,2}(e)\ \ [\mathrm{D1.7};\ \text{uniform-phase case:}\ \Phi=\alpha\,\Theta];\qquad
\operatorname{Hol}_{\mathrm{spiral}}(\gamma)=e^{i\Phi(\gamma)} .
$$
$$
\max\{n:\ \exists\ \text{closed wrapping chain at rung}\ n\}=3 .
$$

**Req.** D1.4, D1.7; CT0.11 (Part 1).

**Pf.**
$$
\mathrm{CT0.11}:\ \text{accessible rungs}=\{0,1,2,3\}
$$
$$
\text{closed wrapping}\Rightarrow\exists v:\ \text{chain continues}\wedge\text{branches back onto itself}\Rightarrow\bigl|\{e\in E_{\mathcal R}:e\ni v\}\bigr|\ge3\Rightarrow n(v)\ge3
$$
$$
\implies n=3.\ \blacksquare
$$

**Phys.** Rung 3 is the first — and by the capacity bound the last — rung at which closed wrapping chains exist. Mass generation is therefore a rung-3 phenomenon, which is also why it coexists with colour (activated at the same rung).

---

### EW.18 — Spiral pole condition

**Thm.** Closed wrapping chain materializes as a rung-3 pole $\implies$
$$
\Phi(\gamma)\in2\pi\mathbb Z\qquad\iff\qquad\sum_{e\in\gamma}\alpha_e\,\widehat{ds}^{\,2}(e)=2\pi k,\ \ k\in\mathbb Z\qquad[\Phi:\ \mathrm{D1.7}].
$$

**Req.** EW.17; D2.4, CT2.5 (Part 2).

**Pf.**
$$
\mathrm{EW.17}:\ \text{transport around the cycle}=\times\operatorname{Hol}_{\mathrm{spiral}}(\gamma)=e^{i\Phi(\gamma)}
$$
$$
\mathrm{CT2.5}:\ \text{pole}=\text{eigenvalue condition on a single-valued eigenmode}\implies e^{i\Phi(\gamma)}=1
$$
$$
\text{winding}\ k:\ \Phi\mapsto\Phi+2\pi k\implies\text{condition}=\Phi(\gamma)\in2\pi\mathbb Z.\ \blacksquare
$$

**Phys.** Materialization of a wrapping chain is quantized: only integer-winding spiral phases support resolvent poles — a single-valuedness (Bohr–Sommerfeld-type) condition derived from the ledger. With the per-edge phase $\alpha_e$ — A4's branch index, alphabet $\{0,\pi\}$ (read in E: Def-EM.20, EM.20) — the constraint reads on the antialigned content: $\Theta_{\mathcal P}(\gamma)=2k$ (CT1.19b).

---

### EW.19 — Mass as pole displacement

**Thm.** $\equiv$ D2.5 (rung-3 context): massless $\iff$ pole at $k^2=0$; massive $\iff$ pole at $k^2=m^2>0$; $m^2:=$ pole displacement of $Z(\mathcal R,3)$ [D2.4].

**Req.** D2.4, D2.5; CT2.5 (Part 2).

**Pf.** Restatement [D2.5]. $\blacksquare$

**Phys.** In this corpus “mass” has one meaning only: how far a resolvent pole sits from the emergent light cone.

---

### EW.32 — The wrapping seed: carrier and normalization

**Thm.** Carrier: $\ \mathcal H_{\mathsf v}\cong\mathbb C^2$ (single qubit). Generator images:
$$
W_i\longmapsto\tfrac12\sigma_i;\qquad Y\longmapsto\tfrac12\sigma_0 ;
$$
$$
\mathfrak T\bigl(\mathcal G_A\mathcal G_B\bigr)=\tfrac12\,\delta_{AB},\quad\mathcal G_A\in\{W_1,W_2,W_3,Y\}\qquad(\text{unique uniform trace normalization});
$$
$$
T_a\,\mathsf v=0\qquad(a=1,\dots,8)\qquad(\text{colour neutrality}).
$$

**Req.** A1, A2; D1.4, D2.6, D2.12, P4; CT0.12 (Rmk), CT0.13, CT0.14, CT1.2 (Part 1); EW.8.

**Pf.**
$$
\mathrm{A2}:\ \text{channel capacity}=1\mathfrak q;\quad\mathrm{A1}:\ \text{carrier of one qubit}=\mathbb C^2;\quad\mathrm{D1.4}:\ \text{chain}=\text{sequence of channels}\implies\text{transported content}=\text{one qubit}:\ \mathcal H_{\mathsf v}\cong\mathbb C^2
$$
$$
\mathrm{CT1.2}:\ W_i=\tfrac12\bigl(\sigma_i^{(p)}+\sigma_i^{(q)}\bigr);\quad\text{restriction to one transported factor}\implies W_i\mapsto\tfrac12\sigma_i
$$
$$
\mathrm{CT0.13}/\mathrm{D2.12}:\ Y_{\mathrm{slot}}=Z\bigl(\iota_2(\mathfrak u(2))\bigr)\ [\mathrm{EW.8}]\implies Y_{\mathrm{car}}=y_0\sigma_0\ \ (y_0\in\mathbb R:\ \text{centre acts as scalar on}\ \mathbb C^2)
$$
$$
\mathfrak T(W_iW_j)=\tfrac14\mathfrak T(\sigma_i\sigma_j)=\tfrac12\delta_{ij};\qquad\mathfrak T(W_iY)=\tfrac12y_0\,\mathfrak T(\sigma_i)=0;\qquad
\mathfrak T(Y^2)=2y_0^2\overset!=\tfrac12\implies y_0=\tfrac12
$$
$$
\text{positive root selected; negative root}=\omega\text{-image}\ [\mathrm{D2.6}]=\text{conjugate seed}
$$
$$
\text{uniqueness}:\ y_0\ne\tfrac12\implies\neg\text{uniform normalization}\implies\text{relative ideal weight free}\ (\neg\mathrm{P4});\quad\text{remaining freedom}=(g,g')\ [\mathrm{P4}]
$$
$$
\mathrm{CT0.12\ Rmk}:\ F_H=\text{pair block},\ F_{\mathrm{strong}}=\text{stack block on}\ \mathcal H^{(3)}_{\mathrm{slot}};\quad\mathrm{CT0.14}:\ \text{orthogonal summands of}\ \mathcal K
$$
$$
\implies\text{seed from the scalar background carries}\ \neg\text{slot index}\implies T_a\mathsf v=0\ \ \forall a.\ \blacksquare
$$

**Phys.** The object transported around a wrapping chain is a single qubit carrying the fundamental of $\mathfrak u(2)$ in the unique uniformly trace-normalized representation — $W_i\to\sigma_i/2$, $Y\to\sigma_0/2$ — and no colour. Representation content is derived from the channel quantum A2; colour-neutrality is what keeps the gluons massless (EW.26).

---

### EW.33 — The wrapping mass form

**Thm.** With $\ \mathcal G=(gW_1,\ gW_2,\ gW_3,\ g'Y)$, $g,g'>0$:
$$
M^2_{AB}=\mu_\star^2\;\operatorname{Re}\bigl\langle\mathcal G_A\mathsf v,\ \mathcal G_B\mathsf v\bigr\rangle,\qquad
\mu_\star^2=c_W\,\varkappa^2\beta^2h_0^2>0\quad(c_W>0:\ \text{rung-3 residue});
$$
$$
M^2\ \text{real symmetric PSD (Gram)};\qquad
\ker M^2=\Bigl\{c\in\mathbb R^4:\ \Bigl(\textstyle\sum_Ac_A\mathcal G_A\Bigr)\mathsf v=0\Bigr\};\qquad
h_0=0\implies M^2\equiv0 .
$$

**Req.** EW.17, EW.32; D1.1; CT1.12, CT2.5, CT2.8 (Part 2); Gram-matrix facts [linear algebra].

**Pf.**
$$
\mathrm{EW.17}:\ \text{transport}=\text{path-ordered product of edge transports}\ [\mathrm{D1.1}];\quad
\text{leading order}:\ \ \mathcal U=\exp\Bigl(i\oint\textstyle\sum_Ac_A\mathcal G_A\,d\ell\Bigr)=1+i\,\ell_\gamma\textstyle\sum_Ac_A\mathcal G_A+O(c^2)
$$
$$
\mathrm{CT2.5}:\ \text{pole displacement}=\text{quadratic single-valuedness defect}:\quad
\bigl\|(\mathcal U-1)\mathsf v\bigr\|^2=\ell_\gamma^2\Bigl\|\textstyle\sum_Ac_A\mathcal G_A\mathsf v\Bigr\|^2+O(c^3)
$$
$$
\Bigl\|\textstyle\sum_Ac_A\mathcal G_A\mathsf v\Bigr\|^2=\sum_{A,B}c_Ac_B\,\operatorname{Re}\langle\mathcal G_A\mathsf v,\mathcal G_B\mathsf v\rangle\qquad
\bigl[c_Ac_B\ \text{sym};\ \operatorname{Im}\langle\cdot,\cdot\rangle\ \text{antisym}\implies\text{Im cancels}\bigr]
$$
$$
\mathrm{CT1.12}:\ \bar g_{0i}=\varkappa N_i=\varkappa\beta w_i;\quad\bar g_{ij}\supset\varkappa h_0\delta_{ij}\implies\text{cycle amplitude}\propto\varkappa^2\beta^2h_0^2;\quad\ell_\gamma^2\ \text{absorbed into}\ c_W>0\implies\mu_\star^2=c_W\varkappa^2\beta^2h_0^2
$$
$$
M^2=\mu_\star^2\cdot\text{Gram}\bigl(\{\mathcal G_A\mathsf v\},\operatorname{Re}\langle\cdot,\cdot\rangle\bigr)\implies\text{symmetric}\ \wedge\ \text{PSD}\quad[\text{linear algebra};\ \text{consistent with}\ \mathrm{CT2.8}:\ \text{residues}\ge0]
$$
$$
c\in\ker M^2\iff c^{\mathsf T}M^2c=0\iff\Bigl\|\textstyle\sum_Ac_A\mathcal G_A\mathsf v\Bigr\|^2=0\iff\textstyle\sum_Ac_A\mathcal G_A\in\operatorname{Ann}(\mathsf v)
$$
$$
h_0=0\implies\mu_\star^2=0\implies M^2\equiv0:\ \forall\ \text{electroweak modes massless}.\ \blacksquare
$$

**Phys.** Mass is a transport defect: the failure of a wrapped seed to return to itself, squared. It is automatically a positive-semidefinite Gram matrix, its kernel is the seed’s stabilizer, and it vanishes without the scalar background — the background is necessary for mass even though (EW.15) it breaks nothing by commutators. The overall scale $\mu_\star^2$ is the sector’s single free positive number (P4 configuration data); every ratio below is free of it.

---

### EW.20 — Weak mass generation

**Thm.** $\langle h\rangle=h_0\ne0$; weak frame with $\mathsf v=$ lower weight state of $W_3$ (an $\mathrm{SU}(2)$ basis choice, always available):
$$
W_3\mathsf v=-\tfrac12\mathsf v;\qquad Y\mathsf v=+\tfrac12\mathsf v;
$$
$$
M^2=\frac{\mu_\star^2}{4}
\begin{pmatrix}
g^2&0&0&0\\
0&g^2&0&0\\
0&0&g^2&-gg'\\
0&0&-gg'&g'^2
\end{pmatrix}
\quad\text{in the ordered basis}\ (W_1,W_2,W_3,Y);
$$
$$
m_W^2:=M^2_{11}=M^2_{22}=\frac{\mu_\star^2g^2}{4}=\frac{c_W\,\varkappa^2\beta^2h_0^2\,g^2}{4}>0 .
$$

**Req.** EW.3, EW.32, EW.33; Bloch-frame fact [linear algebra]; P4.

**Pf.**
$$
\mathsf v\in\mathbb C^2,\ \|\mathsf v\|=1:\ \ \exists!\,\hat n\in S^2:\ (\hat n\cdot\vec\sigma)\mathsf v=-\mathsf v\ \ (\text{negative Bloch direction});\quad
\exists\,U\in\mathrm{SU}(2):\ \hat n\mapsto e_3
$$
$$
U\ \text{acting by conjugation}=\text{automorphism of}\ \mathfrak{su}(2)\ [\mathrm{EW.3}]\implies\text{in the rotated frame}\ \sigma_3\mathsf v=-\mathsf v\implies W_3\mathsf v=-\tfrac12\mathsf v\ [\mathrm{EW.32}]
$$
$$
Y=\tfrac12\sigma_0\ [\mathrm{EW.32}]\implies Y\mathsf v=+\tfrac12\mathsf v\ \ \forall\mathsf v\qquad(\text{hypercharge}\ +\tfrac12:\ \text{derived from trace normalization},\ \neg\text{assigned})
$$
$$
\text{neutral entries}:\ \ \mathcal G_3\mathsf v=-\tfrac g2\mathsf v,\ \ \mathcal G_Y\mathsf v=+\tfrac{g'}2\mathsf v\implies
M^2_{33}=\mu_\star^2\tfrac{g^2}4,\quad M^2_{YY}=\mu_\star^2\tfrac{g'^2}4,\quad M^2_{3Y}=\mu_\star^2\bigl(-\tfrac g2\bigr)\bigl(\tfrac{g'}2\bigr)=-\mu_\star^2\tfrac{gg'}4
$$
$$
\text{charged entries}:\ \ \mathsf v=\binom01:\ \ \sigma_1\mathsf v=\binom10,\ \ \sigma_2\mathsf v=\binom{-i}0\implies
\|W_1\mathsf v\|^2=\|W_2\mathsf v\|^2=\tfrac14;\quad\operatorname{Re}\langle W_1\mathsf v,W_2\mathsf v\rangle=\operatorname{Re}\bigl(\tfrac14\cdot(-i)\bigr)=0
$$
$$
\implies M^2_{11}=M^2_{22}=\tfrac{\mu_\star^2g^2}4,\quad M^2_{12}=0
$$
$$
\text{cross blocks}:\ \ W_{1,2}\mathsf v\propto\binom10\perp\mathsf v;\quad W_3\mathsf v,\ Y\mathsf v\propto\mathsf v\implies M^2_{1,2;\ 3,Y}=0\implies M^2\ \text{block diagonal}
$$
$$
\mu_\star^2>0\ (h_0\ne0,\ c_W>0)\ [\mathrm{EW.33}]\ \wedge\ g>0\implies m_W^2>0;\qquad
\text{undetermined content}=\mu_\star^2\ \text{only}\ [\mathrm{P4}].\ \blacksquare
$$

**Phys.** In the frame where the seed points down the third axis, the Gram mass form is block diagonal: two degenerate charged massive directions and a coupled neutral $2\times2$ block. The $W$ mass is derived; the only number left free is the overall wrapping scale $\mu_\star$.

---

### EW.21 — Charged weak bosons

**Thm.** With $W^\pm=\tfrac1{\sqrt2}(W_1\mp iW_2)$ [D3.10]:
$$
m_{W^+}^2=m_{W^-}^2=m_W^2=\frac{\mu_\star^2g^2}{4}.
$$

**Req.** D3.10; EW.20; eigenvalue invariance of $c\,\mathbb1$ [linear algebra].

**Pf.**
$$
\mathrm{EW.20}:\ M^2\big|_{\text{charged}}=\tfrac{\mu_\star^2g^2}{4}\,\mathbb1_2
$$
$$
\operatorname{spec}\bigl(U(c\,\mathbb1_2)U^{-1}\bigr)=\{c,c\}\ \ \forall\ \text{invertible}\ U\ (\text{incl. complexification to}\ W^\pm)
$$
$$
\bigl[\text{equiv.}:\ SO(2)\ \text{invariance generated by}\ W_3;\ W^\pm:\ \text{eigenvectors with phases}\ e^{\mp i\theta}\bigr]
$$
$$
\implies m_{W^\pm}^2=m_W^2=\tfrac{\mu_\star^2g^2}{4}.\ \blacksquare
$$

**Phys.** The charged weak modes are exactly degenerate: the charged Gram block is a multiple of the identity, so the complex combinations $W^\pm$ inherit the same mass. Charge conjugates share mass by structure, not by assumption.

---

## §D.V — The Neutral Sector

### EW.22 — The unbroken generator

**Thm.**
$$
\ker M^2=\operatorname{span}\{(0,0,g',g)\}\quad\text{in the basis}\ (W_1,W_2,W_3,Y);\qquad
Q:=W_3+Y;\qquad Q\,\mathsf v=0;
$$
$$
A:=\frac{g'W_3+gY}{\sqrt{g^2+g'^2}}\qquad(\text{normalized kernel direction}).
$$

**Req.** EW.20, EW.32, EW.33.

**Pf.**
$$
\mathrm{EW.33}:\ \ker M^2=\{c:\ \textstyle\sum_Ac_A\mathcal G_A\mathsf v=0\}
$$
$$
\mathrm{EW.20}:\ W_{1,2}\mathsf v\perp\mathsf v\ \wedge\ W_{1,2}\mathsf v\ne0;\quad W_3\mathsf v,\ Y\mathsf v\propto\mathsf v\implies c_1\ne0\ \vee\ c_2\ne0\implies\textstyle\sum c_A\mathcal G_A\mathsf v\ne0\implies\ker\subseteq\{c_1=c_2=0\}
$$
$$
\bigl(c_3gW_3+c_Yg'Y\bigr)\mathsf v=\tfrac12\bigl(-c_3g+c_Yg'\bigr)\mathsf v=0\iff c_3g=c_Yg'\iff(c_3,c_Y)\propto(g',g)
$$
$$
\implies\dim\ker M^2=1;\qquad
\text{operator form}:\ g'\cdot gW_3+g\cdot g'Y=gg'\,(W_3+Y)\implies Q=W_3+Y\ \ (gg'\ne0)
$$
$$
Q\mathsf v=\bigl(-\tfrac12+\tfrac12\bigr)\mathsf v=0;\qquad A=(g'W_3+gY)/s,\ \ s=\sqrt{g^2+g'^2}.\ \blacksquare
$$

**Phys.** The massless direction is derived, not posited: it is the unique combination annihilating the seed. Electric charge $Q=W_3+Y$ appears here for the first time — as the stabilizer of the transported qubit.

---

### EW.23 — The neutral mass matrix

**Thm.** In $(W_3,Y)$:
$$
M^2_{\mathrm{neutral}}=\frac{\mu_\star^2}{4}
\begin{pmatrix}g^2&-gg'\\ -gg'&g'^2\end{pmatrix}
=\frac{\mu_\star^2}{4}\,uu^{\mathsf T},\quad u=(g,-g');
$$
$$
\det=0;\qquad\operatorname{tr}=\frac{\mu_\star^2(g^2+g'^2)}{4}=:m_Z^2;\qquad
\operatorname{spec}=\{0,\ m_Z^2\};\qquad
\text{null}=(g',g);\quad\text{massive}=(g,-g').
$$

**Req.** EW.20, EW.22; rank-one facts [linear algebra].

**Pf.**
$$
\text{entries}=[\mathrm{EW.20}];\qquad
\det=\tfrac{\mu_\star^4}{16}\bigl(g^2g'^2-g^2g'^2\bigr)=0;\qquad
\operatorname{tr}=\tfrac{\mu_\star^2}{4}\bigl(g^2+g'^2\bigr)>0
$$
$$
\det=0\ \wedge\ \operatorname{tr}>0\implies\operatorname{rank}=1,\quad\operatorname{spec}=\bigl\{0,\ \tfrac{\mu_\star^2}{4}(g^2+g'^2)\bigr\}
$$
$$
\text{null vector}=(g',g)\ [\mathrm{EW.22}];\qquad\text{massive eigenvector}\perp\text{null}=(g,-g')
$$
$$
m_Z^2:=\tfrac{\mu_\star^2(g^2+g'^2)}{4};\qquad
M^2_{\mathrm{neutral}}=\tfrac{\mu_\star^2}{4}uu^{\mathsf T}\implies\text{PSD}\ [\mathrm{EW.33}].\ \blacksquare
$$

**Phys.** The neutral block is a rank-one Gram matrix — one massive mode ($Z$) and one massless mode — because a single seed direction is being probed by two neutral generators. $m_Z^2=\mu_\star^2(g^2+g'^2)/4$ is derived with zero freedom beyond $\mu_\star$.

---

### EW.24 — The mixing angle

**Thm.**
$$
\cos\theta_W:=\frac{g}{s};\qquad\sin\theta_W:=\frac{g'}{s};\qquad\tan\theta_W=\frac{g'}{g};\qquad s:=\sqrt{g^2+g'^2};
$$
$$
A=\sin\theta_W\,W_3+\cos\theta_W\,Y;\qquad
Z=\cos\theta_W\,W_3-\sin\theta_W\,Y\qquad[\mathrm{D3.10}];
$$
$$
M^2_{\mathrm{neutral}}\,A=0;\qquad M^2_{\mathrm{neutral}}\,Z=m_Z^2\,Z .
$$

**Req.** EW.23; D3.10.

**Pf.**
$$
A\leftrightarrow(\sin\theta_W,\cos\theta_W)\propto(g',g);\qquad Z\leftrightarrow(\cos\theta_W,-\sin\theta_W)\propto(g,-g');\qquad\text{orthonormal}
$$
$$
M^2_{\mathrm{neutral}}A=\frac{m_Z^2}{s^2}\begin{pmatrix}g^2&-gg'\\ -gg'&g'^2\end{pmatrix}\frac1s\begin{pmatrix}g'\\ g\end{pmatrix}
=\frac{m_Z^2}{s^3}\begin{pmatrix}g^2g'-g^2g'\\ -gg'^2+g'g^2\end{pmatrix}=0
$$
$$
M^2_{\mathrm{neutral}}Z=\frac{m_Z^2}{s^2}\begin{pmatrix}g^2&-gg'\\ -gg'&g'^2\end{pmatrix}\frac1s\begin{pmatrix}g\\ -g'\end{pmatrix}
=\frac{m_Z^2}{s^3}\begin{pmatrix}g(g^2+g'^2)\\ -g'(g^2+g'^2)\end{pmatrix}=m_Z^2\,(\cos\theta_W,-\sin\theta_W)=m_Z^2Z.\ \blacksquare
$$

**Phys.** The weak mixing angle is the geometry of the kernel: the angle between the neutral gauge plane and the seed stabilizer. $\tan\theta_W=g'/g$ is a derived relation — $\theta_W$ is not a new parameter, since $g,g'$ are the configuration data (P4).

---

### EW.25 — The photon direction is massless

**Thm.** $\ m_A^2=0$ (pole of $A$ at $k^2=0$).

**Req.** EW.19, EW.24.

**Pf.**
$$
\mathrm{EW.24}:\ M^2A=0\implies\text{pole displacement}=0\implies\text{pole at}\ k^2=0\quad[\mathrm{EW.19}\equiv\mathrm{D2.5}].\ \blacksquare
$$

**Phys.** The photon direction is exactly massless — a protected zero of the Gram matrix (the seed’s stabilizer), not a tuned smallness.

---

### EW.26 — Colour modes remain massless at rung 3

**Thm.** Extending $M^2$ over $\mathcal G\cup\{T_a\}_{a=1}^{8}$:
$$
M^2_{aB}=\mu_\star^2\operatorname{Re}\langle T_a\mathsf v,\ \mathcal G_B\mathsf v\rangle=0;\qquad
M^2_{ab}=0;\qquad
\{T_a\}_{a=1}^8\subseteq\ker M^2;\qquad
m_g^2=0 .
$$

**Req.** EW.6, EW.19, EW.32, EW.33; CT0.12 (Rmk), CT0.14 (Part 1).

**Pf.**
$$
\mathrm{EW.6}:\ \mathcal A(3)=\mathcal A(2)\cup\{\mathrm{strong}\}\implies T_a\ \text{active at rung 3, in the connection}
$$
$$
\mathrm{EW.32}:\ T_a\mathsf v=0\ \ \forall a\implies M^2_{aB}=\mu_\star^2\operatorname{Re}\langle0,\ \mathcal G_B\mathsf v\rangle=0;\quad M^2_{ab}=0
$$
$$
\implies\text{colour block}\equiv0\implies8\ \text{colour directions}\subseteq\ker M^2\implies\text{poles at}\ k^2=0\quad[\mathrm{EW.19}]
$$
$$
\text{structural reason}:\ F_H=\text{pair block}\perp F_{\mathrm{strong}}=\text{stack block}\quad[\mathrm{CT0.12\ Rmk},\ \mathrm{CT0.14}].\ \blacksquare
$$

**Phys.** Gluons stay massless because the wrapping seed is colour-blind: the scalar lives in the pair register and colour in the orthogonal slot register. A structural orthogonality — not a stipulation — protects the colour gauge modes. (Cited in **F**.)

---

### EW.27 — The scalar excitation

**Thm.** $S_{\mathrm{eff}}[h]:=$ CT1.20 action restricted to the trace mode; $h_0:$ nondegenerate stable stationary point. Then
$$
m_H^2:=\left.\frac{\delta^2S_{\mathrm{eff}}}{\delta h^2}\right|_{h=h_0}>0;\qquad
\text{scalar pole at}\ k^2=m_H^2\ \ (\text{simple});\qquad
m_H^2=\text{configuration data}\ [\mathrm{P4}].
$$

**Req.** CT1.20, CT2.5 (Part 2); stability criterion [math]; P4.

**Pf.**
$$
\text{stable stationary}:\quad\left.\frac{\delta S_{\mathrm{eff}}}{\delta h}\right|_{h_0}=0\ \wedge\ \left.\frac{\delta^2S_{\mathrm{eff}}}{\delta h^2}\right|_{h_0}>0
$$
$$
\text{quadratic expansion about}\ h_0:\ \ \text{coefficient}=m_H^2\implies\text{resolvent pole displaced by}\ m_H^2\quad[\mathrm{CT2.5}]
$$
$$
\text{nondegenerate}\implies\text{pole simple};\qquad m_H^2\ \text{value}=\text{shape of}\ S_{\mathrm{eff}}\implies\text{P4 data},\ \neg\text{in the derived ratios}.\ \blacksquare
$$

**Phys.** The Higgs-like particle is the trace-mode fluctuation about a stable background; its mass is configuration data and never enters any of the derived dimensionless ratios. (Cited in **G**.)

---

## §D.VI — Derived Electroweak Relations

### EW.28 — The gauge spectrum

**Thm.**
$$
\begin{array}{c|c|c}
\text{mode} & \text{combination} & m^2\\ \hline
W^+ & \tfrac1{\sqrt2}(W_1-iW_2) & m_W^2=\mu_\star^2g^2/4>0\\
W^- & \tfrac1{\sqrt2}(W_1+iW_2) & m_W^2\\
Z & \cos\theta_W\,W_3-\sin\theta_W\,Y & m_Z^2=\mu_\star^2(g^2+g'^2)/4>0\\
A & \sin\theta_W\,W_3+\cos\theta_W\,Y & 0
\end{array}
\qquad\tan\theta_W=\frac{g'}{g};
$$
exhaustive: $\dim\mathfrak g_{\mathrm{EW}}=4$ and the four directions are independent.

**Req.** EW.10, EW.20, EW.21, EW.23, EW.24, EW.25; D3.10.

**Pf.** Charged: [EW.20, EW.21]; neutral: [EW.23, EW.24]; $m_A^2=0$: [EW.25]; exhaustiveness: $\dim\mathfrak g_{\mathrm{EW}}=4$ [EW.10] $\wedge$ independence $\{W^\pm,Z,A\}$. $\blacksquare$

**Phys.** Exactly four gauge directions materialize: two degenerate charged massive, one neutral massive, one neutral massless — the electroweak spectrum, all eigen-data of one Gram matrix.

---

### EW.34 — The mass ratio

**Thm.**
$$
\frac{m_W^2}{m_Z^2}=\frac{g^2}{g^2+g'^2}=\cos^2\theta_W;\qquad
m_W=m_Z\cos\theta_W;\qquad
\rho:=\frac{m_W^2}{m_Z^2\cos^2\theta_W}=1;
$$
$$
\rho=1\iff j=\tfrac12\iff\dim\mathcal H_{\mathsf v}=2\iff\mathrm{A2}\ (1\mathfrak q\ \text{per channel});\qquad
\rho\ \text{independent of}\ \mu_\star^2,h_0,\varkappa,\beta,c_W,\mathfrak h .
$$

**Req.** A2; EW.20, EW.23, EW.24, EW.32; spin-$j$ ladder algebra [math].

**Pf.**
$$
m_W^2=\tfrac{\mu_\star^2g^2}4,\quad m_Z^2=\tfrac{\mu_\star^2(g^2+g'^2)}4\ \ \text{from one Gram matrix}\ [\mathrm{EW.20},\mathrm{EW.23}]\implies
\frac{m_W^2}{m_Z^2}=\frac{g^2}{g^2+g'^2}=\cos^2\theta_W\ [\mathrm{EW.24}]
$$
$$
\implies\rho\equiv1\ \ \text{(identically in}\ g,g');\qquad\mu_\star^2,h_0,\varkappa,\beta,c_W,\mathfrak h\ \text{cancel}
$$
$$
\text{driver}:\ \ \frac{m_W^2}{m_Z^2}\Big/\cos^2\theta_W\ \text{traces to}\ \frac{\|W_1\mathsf v\|^2}{\|W_3\mathsf v\|^2};\qquad
\text{spin-}j\ \text{lowest weight}:\ \|W_1\mathsf v\|^2=\tfrac14\bigl[j(j{+}1)-(-j)(-j{+}1)\bigr]=\tfrac j2,\quad\|W_3\mathsf v\|^2=j^2
$$
$$
\frac{\|W_1\mathsf v\|^2}{\|W_3\mathsf v\|^2}=\frac{1}{2j}=1\iff j=\tfrac12\iff\mathcal H_{\mathsf v}=\mathbb C^2\ [\mathrm{EW.32}]\iff1\mathfrak q\ \text{per channel}\ [\mathrm{A2}].\ \blacksquare
$$

**Phys.** The tree-level $\rho$ parameter equals one because the seed carrier is a single qubit: for spin $j$ the charged-to-neutral Gram ratio is $1/(2j)$, forced to $1$ exactly at $j=\tfrac12$, which A2 demands. $m_W=m_Z\cos\theta_W$ is a dimensionless prediction with zero freedom — independent of every configuration parameter and of the calibration scale. (Cited in **G**.)

---

### EW.35 — The residual coupling

**Thm.** Neutral connection $\ \mathcal A_{\mathrm{neutral}}=g\,w^3W_3+g'\,y\,Y$; in the mass eigenbasis ($w^3=\sin\theta_W\,\mathsf A+\cos\theta_W\,\mathsf Z$; $y=\cos\theta_W\,\mathsf A-\sin\theta_W\,\mathsf Z$):
$$
\mathsf A\text{-coefficient}=e\,Q;\qquad
e:=\frac{gg'}{\sqrt{g^2+g'^2}}=g\sin\theta_W=g'\cos\theta_W;\qquad
\frac1{e^2}=\frac1{g^2}+\frac1{g'^2}.
$$

**Req.** EW.22, EW.24.

**Pf.**
$$
\text{rotation to mass basis}\ [\mathrm{EW.24}]:\quad
\mathcal A_{\mathrm{neutral}}=\bigl(g\sin\theta_W\,W_3+g'\cos\theta_W\,Y\bigr)\mathsf A+\bigl(g\cos\theta_W\,W_3-g'\sin\theta_W\,Y\bigr)\mathsf Z
$$
$$
g\sin\theta_W\,W_3+g'\cos\theta_W\,Y=\frac{gg'}{s}\,W_3+\frac{g'g}{s}\,Y=\frac{gg'}{s}\,(W_3+Y)=e\,Q\quad[\mathrm{EW.22},\ \mathrm{EW.24}:\ \sin\theta_W=\tfrac{g'}s,\ \cos\theta_W=\tfrac gs]
$$
$$
e=\frac{gg'}{s}=g\sin\theta_W=g'\cos\theta_W;\qquad
\frac1{e^2}=\frac{g^2+g'^2}{g^2g'^2}=\frac1{g^2}+\frac1{g'^2}.\ \blacksquare
$$

**Phys.** The coupling of the massless direction is the harmonic combination of $g$ and $g'$: $e=g\sin\theta_W$ is a derived identity, not a definition. (Cited in **E**, **G**; the broken `$\ne$’ glyphs of the prior codex are the letter $e$.)

---

### EW.36 — The charge spectrum and its consistency with the chain end-charge

**Thm.**
$$
Q\big|_{\mathcal H_{\mathsf v}}=\tfrac12\sigma_3+\tfrac12\sigma_0=\operatorname{diag}(1,0);\qquad
\operatorname{spec}Q=\{0,+1\};\qquad
\omega\ [\mathrm{D2.6}]:\ \operatorname{spec}\mapsto\{0,-1\};
$$
$$
\text{charge alphabet}=q\in\{-1,0,+1\}=q_{\mathrm{EM}}(c)\ \text{alphabet of D3.4}\ [\mathrm{EM.9}].
$$

**Cor EW.36a.** On the carrier: $Q=W_3+Y$; seed hypercharge $=+\tfrac12$ [EW.20].

**Req.** EW.20, EW.22, EW.32; D2.6, D3.4; CT0.9 (Part 1); EM.9 (**E**, forward pointer).

**Pf.**
$$
\mathrm{EW.32}:\ W_3=\tfrac12\sigma_3,\ Y=\tfrac12\sigma_0\implies Q=\tfrac12(\sigma_3+\sigma_0)=\operatorname{diag}(1,0)
$$
$$
\operatorname{spec}\operatorname{diag}(1,0)=\{1,0\};\qquad\text{eigenvalue}\ 1:\ \text{upper weight state};\quad0:\ \mathsf v\ [\mathrm{EW.22}:\ Q\mathsf v=0]
$$
$$
\mathrm{D2.6}:\ \omega\ \text{reverses charge}\implies\text{reversed carrier}:\ \operatorname{spec}=\{0,-1\}\implies\text{alphabet}=\{-1,0,+1\}
$$
$$
\text{independently}:\ \ \mathrm{D3.4}:\ q_{\mathrm{EM}}(c)=\tfrac12\bigl(\sigma_{s(c)}-\sigma_{t(c)}\bigr),\ \ \sigma\in\{+1,-1\}\ [\mathrm{CT0.9}]\implies q_{\mathrm{EM}}\in\{-1,0,+1\}\ [\mathrm{EM.9}]
$$
$$
\text{inputs disjoint}\ (\text{seed carrier}+\text{trace normalization}\ \ \text{vs}\ \ \text{binary edge phase})\implies\text{agreement}=\text{consistency check}.\ \blacksquare
$$

**Phys.** Two independent constructions of charge — the operator route (stabilizer of the seed) and the combinatorial route (difference of edge signs at a chain’s ends) — yield the same ternary alphabet $\{-1,0,+1\}$. Charge quantization is triality of a qubit seed, mirrored by the binary edge register.

---

### EW.29 — The full electroweak spectrum

**Thm.** Rung-3 materialized poles:
$$
\{W^+,\ W^-,\ Z,\ A,\ H\};\qquad
m_{W^\pm}^2=m_W^2>0;\quad m_Z^2=\frac{m_W^2}{\cos^2\theta_W}>0;\quad m_A^2=0;\quad m_H^2>0\ (h_0\ne0\ \text{stable});
$$
exhaustive: gauge directions span $\mathfrak g_{\mathrm{EW}}$ ($\dim=4$) $\oplus$ scalar direction $F_H$ ($\dim=1$).

**Req.** CT0.12 (Part 1); EW.10, EW.27, EW.28, EW.34.

**Pf.** Gauge poles + masses: [EW.28, EW.34]; scalar pole: [EW.27]; exhaustiveness: $\dim\mathfrak g_{\mathrm{EW}}=4$ [EW.10] $+\ \dim F_H=1$ [CT0.12]. $\blacksquare$

**Phys.** The electroweak particle content materialized at rung 3 is exactly: two charged massive, one neutral massive, one neutral massless, one scalar — and nothing else.

---

### EW.30 — Spectral reduction

**Thm.**
$$
\text{rung 2}:\ \mathfrak g_{\mathrm{EW}}=\mathfrak{su}(2)\oplus\mathfrak u(1)\ [\mathrm{EW.10}];\qquad
\text{rung 3}:\ \operatorname{spec}=\{m_W^2,m_W^2,m_Z^2,0\}\ [\mathrm{EW.28}];
$$
$$
\text{“}\mathrm{SU}(2)\times\mathrm{U}(1)\to\mathrm{U}(1)_Q\text{”}\ :=\ \text{naming of the spectral reduction};\qquad
\neg\text{Lie-algebra breaking by commutators}\ [\mathrm{EW.15}];
$$
$$
[Q,Q]=0\implies\text{residual structure}=\mathfrak u(1)_Q\ \ (\text{genuine abelian algebra}).
$$

**Req.** EW.10, EW.15, EW.22, EW.28, EW.33.

**Pf.**
$$
\mathrm{EW.15}:\ \operatorname{Stab}_{\mathrm{adj}}=\mathfrak g_{\mathrm{EW}}\implies\text{algebra intact}
$$
$$
\mathrm{EW.33}:\ \text{reduction occurs in}\ \ker M^2=\text{stabilizer of the transported seed};\quad
\mathrm{EW.22}:\ \dim\ker=1,\ \text{spanned by}\ Q
$$
$$
\mathrm{EW.28}:\ \text{spectrum}=3\ \text{massive}+1\ \text{massless pole};\qquad
[Q,Q]=0\implies\mathfrak u(1)_Q\ \text{abelian}\implies\text{name accurate as spectral description}.\ \blacksquare
$$

**Phys.** The correct statement of “electroweak symmetry breaking” in this corpus: the algebra never breaks — what reduces is the spectrum. Three poles leave the light cone, one stays, and the residual structure is the abelian stabilizer of the seed. The conventional name is retained as a label only.

---

## §D.VII — Completion

### EW.31 — Self-containment of the electroweak sector

**Thm.**
$$
\forall\ \text{statements of}\ \mathbf D:\quad\vdash\ \mathrm{A1\text{–}A9}\ \cup\ \mathrm{C1\text{–}C9}\ \cup\ \mathrm{D0.1\text{–}D4.3}\ \cup\ \{\mathbf B,\mathbf C\ \text{theorems}\};
$$
$$
\neg\exists\ \text{external electroweak law, parameter, or measured value used};\qquad
\text{undetermined}=\{g,\ g',\ h_0,\ c_W,\ \varkappa,\ \beta\}\subset\mathrm{P4};
$$
$$
\forall\ \text{quoted ratios}\ (m_W/m_Z,\ e/g,\ \rho,\ \text{charge alphabet}):\ \ \text{independent of P4 data and of}\ \mathfrak h .
$$

**Req.** EW.1–EW.30; CT-tags as cited; P4.

**Pf.** Dependency trace:
$$
\mathrm{EW.2}\equiv\mathrm{CT1.2}\Leftarrow\mathrm{A3};\quad
\mathrm{EW.3}\equiv\mathrm{CT1.4};\quad
\mathrm{EW.6/7}\Leftarrow\mathrm{CT0.13}\Leftarrow\{\mathrm{CT0.7},\mathrm{D3.1},\mathrm{D3.2},\mathrm{D3.3}\}
$$
$$
\mathrm{EW.8\text{–}10}:\ Y=\text{masked centre}\ [\mathrm{CT2.2},\mathrm{CT0.13}];\ \text{commutation}\Leftarrow\text{centrality}
$$
$$
\mathrm{EW.13}:\ \text{scalar}=\text{unique unallocated rotation scalar}\ [\mathrm{CT1.10},\mathrm{CT1.11},\mathrm{CT0.12}]
$$
$$
\mathrm{EW.14/15}:\ \text{background commutes}\implies\neg\text{adjoint breaking};\quad
\mathrm{EW.33}:\ \text{mass}=\text{transport Gram form}
$$
$$
\mathrm{EW.32}:\ \text{carrier}=\mathbb C^2\Leftarrow\mathrm{A2};\ \text{normalization}\Leftarrow\mathfrak T(\mathcal G_A\mathcal G_B)=\tfrac12\delta_{AB}\ (\text{unique})
$$
$$
\mathrm{EW.33}:\ \text{Gram}\implies\text{PSD};\ \ker=\text{stabilizer};\quad
\mathrm{EW.22\text{–}25}:\ \text{kernel}\implies\theta_W,\ m_Z,\ m_A=0
$$
$$
\mathrm{EW.26}:\ F_H\perp F_{\mathrm{strong}}\ [\mathrm{CT0.14}]\implies m_g=0;\quad
\mathrm{EW.34/35}:\ \text{ratios free of P4}\wedge\mathfrak h;\quad
\mathrm{EW.36}:\ \text{alphabets agree (disjoint inputs)}.\ \blacksquare
$$

**Phys.** Closure audit of the sector: every electroweak statement traces to A1–A9 through B and C; the only undetermined quantities are the P4 configuration data $(g,g',h_0,c_W,\varkappa,\beta)$, and every quoted ratio is independent of all of them.

---

## Closure exports of Part 2 §D (consumed by Part 2 §E–§G, Parts 3–4)

$$
\begin{array}{lll}
\mathrm{EW.10}\ \mathfrak g_{\mathrm{EW}}=\mathfrak{su}(2)\oplus\mathfrak u(1),\ \dim=4 &
\mathrm{EW.18}\ \Phi(\gamma)\in2\pi\mathbb Z &
\mathrm{EW.20}\ M^2\ \text{block form};\ m_W^2=\mu_\star^2g^2/4\\
\mathrm{EW.22}\ Q=W_3+Y;\ Q\mathsf v=0 &
\mathrm{EW.24}\ \tan\theta_W=g'/g;\ A,\ Z\ \text{eigenbasis} &
\mathrm{EW.25}\ m_A^2=0\\
\mathrm{EW.26}\ m_g^2=0\ (\text{cited in F}) &
\mathrm{EW.27}\ m_H^2>0\ (\text{cited in G}) &
\mathrm{EW.28}\ \text{spectrum}\ \{W^\pm,Z,A\}\\
\mathrm{EW.32}\ \mathcal H_{\mathsf v}=\mathbb C^2;\ W_i\mapsto\tfrac12\sigma_i;\ Y\mapsto\tfrac12\sigma_0;\ T_a\mathsf v=0 &
\mathrm{EW.33}\ M^2=\mu_\star^2\,\mathrm{Gram};\ \ker=\text{stabilizer} &
\mathrm{EW.34}\ \rho=1;\ m_W=m_Z\cos\theta_W\\
\mathrm{EW.35}\ e=gg'/\sqrt{g^2+g'^2};\ 1/e^2=1/g^2+1/g'^2 &
\mathrm{EW.36(a)}\ \operatorname{spec}Q=\{0,1\};\ q\in\{-1,0,+1\} &
\mathrm{EW.29/30}\ \text{full spectrum};\ \text{reduction}=\text{spectral}
\end{array}
$$

$\blacksquare$

---

## §E — Electromagnetic Sector

*Dep.: Part 1; Part 2 §C, §D. Forward cross-section pointers, corroboration only ($\neg$load-bearing): EM.18, EM.26 $\to$ CT3.7 (Part 2 §F; the main arguments are CT0.14-based). Notation: $\mathsf E_{\mathrm{bd}},\mathsf E_{\mathrm{tr}}$ [C6]; $\mathcal P_M^{(n)},\mathbf F_M^{(n)}$ [C7]; $Z$ [C8]; $\alpha_e$ — per-edge dynamic phase [D3.5, Def-EM.20, EM.20]. Machine: `checks/verify_E.py`; Def-EM.20/EM.20/EM.23/EM.24: `checks/verify_F33_dynamic_phase.py`.*

## §E.I — Rung-2 Existence and Algebra

### EM.1 — The electromagnetic aspect activates at rung 2

**Thm.**
$$
\mathrm{EM}\in\mathcal A(2);\qquad\mathrm{EM}\notin\mathcal A(1);\qquad\mathrm{EM}\notin\mathcal A(0);
$$
$$
\neg\exists\ \text{independent aspect named}\ Z\ \text{at rungs}\ \le2:\quad\text{neutral seed}=W_3\in F_W\ [\mathrm{C8}].
$$

**Req.** A7, C8; D0.8, D3.3; CT0.13 (Part 1).

**Pf.**
$$
\mathrm{CT0.13}:\ \mathcal A(0)=\{J\};\quad\mathcal A(1)=\{J,G,W,H,D^+\};\quad\mathcal A(2)=\mathcal A(1)\cup\{\mathrm{EM}\}\implies\mathrm{EM}\in\mathcal A(2)
$$
$$
\mathrm{D3.3}:\ f_v\ \text{defined}\iff\partial^{\leftarrow}(v)\ge1\ \wedge\ \partial^{\rightarrow}(v)\ge1\implies n(v)\ge2\quad[\mathrm{D0.8}]
$$
$$
n\le1:\ \neg\exists v:\ (\partial^{\leftarrow}\ge1\wedge\partial^{\rightarrow}\ge1)\implies f_v\ \text{undefined}\ \forall v\implies\mathrm{EM}\ \text{has no support}\implies\mathrm{EM}\notin\mathcal A(0)\cup\mathcal A(1)
$$
$$
\mathrm{CT0.13}:\ W_3\in F_W\ (3\text{-dim block});\quad F_{\mathrm{EM}}=\text{distinct stack block}\implies\neg\exists\ \text{aspect}\ Z\ \text{at rungs}\le2.\ \blacksquare
$$

**Phys.** Electromagnetism switches on exactly at rung 2, because measuring a relative phase needs both an incoming and an outgoing real edge at one vertex. Its existence — and its absence at rungs 0–1 — is a theorem of degree bookkeeping.

---

### EM.2 — The electromagnetic generator

**Thm.** [EW.8 realizations]
$$
Y_{\mathrm{asp}}=\mathcal P^{(\mathrm{EM})}:\ \operatorname{rk}=1;\qquad
\mathfrak T\bigl(Y_{\mathrm{asp}}\bigr)=\dim\mathcal K^{(\mathrm{EM})}=1;\qquad
[Y_{\mathrm{asp}},\ \text{any block-diagonal operator}]=0;
$$
$$
Y_{\mathrm{car}}=\tfrac12\sigma_0;\qquad[Y_{\mathrm{car}},W_i|_{\mathrm{car}}]=0\ [\mathrm{EW.32}];
$$
$$
\text{mask fact}\ (\neg Y):\quad\mathcal P_M^{(2)}E_0\mathcal P_M^{(2)}=\mathcal P_M^{(2)},\quad\mathfrak T\bigl(\mathcal P_M^{(2)}\bigr)=\dim\mathcal K_2=17\quad(E_0\leftrightarrow F_{D^+}\ [\mathrm{CT0.12}]).
$$

**Req.** CT0.12, CT0.13, CT0.14, CT1.2 (Part 1); CT2.2, D2.3 (Part 2); D2.12; EW.8, EW.32 (Part 2).

**Pf.**
$$
\dim\mathcal K^{(\mathrm{EM})}=1\ [\mathrm{CT0.14}]\implies Y_{\mathrm{asp}}=\mathcal P^{(\mathrm{EM})}:\ \operatorname{rk}1,\ \ \mathfrak T=\dim\operatorname{Im}=1\ [\mathrm{D2.3},\ \mathrm{CT2.2}]
$$
$$
\mathrm{D2.3}:\ \mathcal K=\bigoplus_A\mathcal K^{(A)}\ \text{orthogonal}\implies[\mathcal P^{(\mathrm{EM})},\ \text{block-diagonal}]=0
$$
$$
Y_{\mathrm{car}}=\tfrac12\sigma_0:\ [\mathrm{EW.32}:\ \text{uniform trace normalization}\ \mathfrak T(\mathcal G_A\mathcal G_B)=\tfrac12\delta_{AB}];\qquad[\tfrac12\sigma_0,\tfrac12\sigma_i]=0
$$
$$
E_0=I_4\ [\mathrm{CT1.2}]\implies\mathcal P_M^{(2)}E_0\mathcal P_M^{(2)}=\mathcal P_M^{(2)}\ [\mathrm{CT2.2}];\quad\mathfrak T=17\ [\mathrm{CT0.14}];\quad E_0\leftrightarrow F_{D^+}\ [\mathrm{CT0.12}].\ \blacksquare
$$

**Rmk (repair).** The prior codex defined $Y:=\mathcal P_M^{(2)}E_0\mathcal P_M^{(2)}=\mathcal P_M^{(2)}$ (rank $17$) and then used it both as the abelian generator and inside the EM.17 trace formula. The rank-$17$ object is the rung-2 *mask*; the abelian generator is the rank-one block projection $Y_{\mathrm{asp}}$ (aspect space) and $\tfrac12\sigma_0$ (carrier). The three realizations $Y_{\mathrm{slot}},Y_{\mathrm{asp}},Y_{\mathrm{car}}$ are coordinated by EW.8/D2.12.

**Phys.** One generator, three well-typed faces: the centre of the rung-2 slot algebra, the rank-one projection onto the EM block (trace $1$), and $\tfrac12\sigma_0$ on the seed. The trace formula (EM.17) uses the block face; charge statements (EW.36) use the carrier face; the number $17$ belongs to the mask, not to $Y$.

---

### EM.3 — The electromagnetic Lie algebra

**Thm.** $\equiv$ EW.9: $\ \bigl(\operatorname{span}_{\mathbb R}\{Y\},[\cdot,\cdot]\bigr)\cong\mathfrak u(1);\quad[aY,bY]=0;\quad\dim=1.$

**Req.** EW.9 (Part 2).

**Pf.** Identity [EW.9]. $\blacksquare$

**Phys.** The electromagnetic block is the one-dimensional abelian factor: bracket identically zero.

---

### EM.4 — The rung-2 algebra containing the abelian factor

**Thm.** $\equiv$ EW.10: $\ \mathfrak g_{\mathrm{EW}}=\operatorname{span}_{\mathbb R}\{W_1,W_2,W_3,Y\}=\mathfrak{su}(2)\oplus\mathfrak u(1);\quad\dim=4.$

**Req.** EW.10 (Part 2); EM.2, EM.3.

**Pf.** Identity [EW.10: CT1.4 $\mathfrak{su}(2)$; EM.3 $\mathfrak u(1)$; EM.2 commutation; commuting ideals, trivial intersection]. $\blacksquare$

**Phys.** The abelian factor sits inside the rung-2 electroweak algebra as its commuting centre-plus-identity summand.

---

## §E.II — The Photon

### EM.5 — Photon and gluon as trivial chains

**Thm.** [D1.7, D3.7]
$$
\gamma_{\gamma}\in\mathsf{Trivial}\ \wedge\ \gamma_{\gamma}\subseteq V_2\qquad(\text{photon});\qquad
\gamma_g\in\mathsf{Trivial}\ \wedge\ \gamma_g\cap V_3\ne\varnothing\qquad(\text{gluon});
$$
$$
\forall\gamma\in\mathsf{Trivial}:\ \ \Theta(\gamma)=0\ \wedge\ \operatorname{Hol}_{\mathrm{spiral}}(\gamma)=1;\qquad
V_2\cap V_3=\varnothing;
$$
$$
\text{distinguishing datum}=\text{possibility space only}\ (V_2\ \text{vs}\ V_3\ \text{availability});\qquad\neg\text{bound loops}.
$$

**Req.** D0.8, D1.7, D3.7; CT0.13 (Part 1).

**Pf.**
$$
\mathrm{D1.7}:\ \gamma\in\mathsf{Trivial}\iff\forall e\in\gamma:\ \widehat{ds}^{\,2}(e)=0\implies\Theta(\gamma)=\sum_e0=0\implies\Phi(\gamma)=\sum_e\alpha_e\cdot0=0\implies\operatorname{Hol}=e^{i\Phi}=1
$$
$$
\mathrm{D0.8}:\ V_n=\{v:n(v)=n\}\implies V_2\cap V_3=\varnothing
$$
$$
\mathrm{CT0.13}:\ \mathrm{strong}\in\mathcal A(3)\setminus\mathcal A(2)\implies\gamma\subseteq V_2:\ \neg\text{colour index};\quad\gamma\cap V_3\ne\varnothing:\ \text{colour possible}
$$
$$
\text{same class}\ \mathsf{Trivial};\quad\neg\exists\ \text{further distinguishing datum}.\ \blacksquare
$$

**Phys.** Photon and gluon are one kind of object — a null (trivial) chain of the graph — distinguished only by which vertex rungs it may visit. “Being a photon” is a possibility-space property of rung-2 chains, not a different substance. (Cited in **F**.)

---

### EM.6 — Photon masslessness

**Thm.** $\ m_\gamma^2=0$, with two independent supports:
$$
(\mathrm{i})\quad A=\sin\theta_W W_3+\cos\theta_W Y\ \text{spans}\ \ker M^2\ [\mathrm{EW.22},\mathrm{EW.24}];
$$
$$
(\mathrm{ii})\quad\gamma_{\gamma}\in\mathsf{Trivial}\subseteq V_2:\ \ \Theta(\gamma)=0\ \wedge\ \text{winding}=0\implies\neg\exists\ \text{wrapping holonomy}\implies\neg\exists\ \text{wrapping contribution}\ [\mathrm{EM.5},\mathrm{EW.18}].
$$

**Req.** D2.5; EM.5; EW.18, EW.22, EW.24, EW.25, EW.33 (Part 2).

**Pf.**
$$
\mathrm{D2.5}:\ m^2=\text{pole displacement};\qquad
\mathrm{EW.33}:\ \text{displacement source}=\mu_\star^2\Bigl\|\textstyle\sum_Ac_A\mathcal G_A\mathsf v\Bigr\|^2\ (\text{rung-3 wrapping form})
$$
$$
\mathrm{EW.22}:\ \ker M^2=\operatorname{span}\{(g',g)\}_{(W_3,Y)}=A\text{-direction}\ [\mathrm{EW.24}]
$$
$$
(\mathrm{ii}):\ \ \text{trivial}\implies\Theta=0\ [\mathrm{EM.5}];\quad\text{winding}=0\implies e^{i\Phi}=1\ \text{vacuous}\implies\neg\text{materialization from wrapping}\ [\mathrm{EW.18}]
$$
$$
\text{neutral direction with}\ \neg\text{wrapping}=\ker\text{-direction}\implies\gamma=A\implies\text{displacement}=0\implies m_\gamma^2=0\quad[=\mathrm{EW.25}].\ \blacksquare
$$

**Phys.** The photon is massless twice over: algebraically it spans the kernel of the Gram mass form (the seed’s stabilizer), and geometrically a null chain confined to rung-2 vertices cannot wind, so the wrapping defect never sees it. (Cited in **F**, **G**.)

---

### EM.7 — Photon entropy budget

**Thm.** Photon chain of hop count $\delta h$:
$$
\mathsf E_{\mathrm{tr}}=\delta h\,\ln2\ \ \text{nats}=\delta h\ \ \text{bits};\qquad
\mathsf E_{\mathrm{bd}}=0 .
$$

**Req.** C9; D1.5; CT0.9 (Part 1); EM.5.

**Pf.**
$$
\mathrm{CT0.9}+\mathrm{C9}:\ 1\ \text{real edge}=1\ \text{bit}=\ln2\ \text{nats};\qquad
\text{edges}=\text{independent registers}\implies\delta h\ \text{hops}:\ \delta h\ln2
$$
$$
\mathrm{D1.5}:\ \text{open propagating chain}=\text{transit}\ [\mathrm{EM.5}]\implies\mathsf E_{\mathrm{tr}}=\delta h\ln2
$$
$$
\mathsf E_{\mathrm{bd}}=\Delta S_{\mathrm{bound}}\ [\mathrm{D1.5}];\quad\text{photon}\ \neg\text{closed}\implies\mathsf E_{\mathrm{bd}}=0.\ \blacksquare
$$

**Phys.** A photon carries exactly one bit of transit entropy per hop and zero bound entropy: bosonic transport content, measured by the ledger’s own edge count.

---

### EM.8 — Photon polarization count

**Thm.** $D=4$; $k_\mu\ne0$ null $\bigl(k^\mu k_\mu=0\bigr)$; $\epsilon_\mu\sim\epsilon_\mu+k_\mu$ (gauge, EM.14); transversality $k^\mu\epsilon_\mu=0$ (source-free equation, CT1.22). Then
$$
N_{\mathrm{pol}}=\dim\bigl(k^\perp/\operatorname{span}\{k\}\bigr)=(4-1)-1=2,\qquad
k^\perp:=\{v:\ k_\mu v^\mu=0\}.
$$

**Req.** CT1.22, CT2.6 (Part 2); EM.6, EM.14; rank–nullity [linear algebra].

**Pf.**
$$
\mathrm{CT1.22}:\ F_{\mu\nu}=2\nabla_{[\mu}A_{\nu]};\qquad
\mathrm{EM.14}:\ A_\mu\sim A_\mu+\nabla_\mu\chi\implies\epsilon_\mu\propto k_\mu:\ 2k_{[\mu}k_{\nu]}=0\implies F=0:\ \text{pure gauge}
$$
$$
\text{source-free equation}\ [\mathrm{CT1.22}]\implies k^\mu\epsilon_\mu=0\implies\epsilon\in k^\perp
$$
$$
k_\mu\ne0\implies\operatorname{rank}(k_\cdot)=1\implies\dim k^\perp=4-1=3\quad[\text{rank--nullity}]
$$
$$
k^\mu k_\mu=0\implies k\in k^\perp;\quad k\ne0\implies\dim\bigl(k^\perp/\operatorname{span}\{k\}\bigr)=3-1=2.\ \blacksquare
$$

**Phys.** A massless spin-1 mode in four dimensions has exactly two physical polarizations: transversality gives three, gauge redundancy removes one. The count is derived from dimension arithmetic plus nullness — the same $N_{\gamma\text{-pol}}=2$ of policy P2. (Cited in **G**.)

---

## §E.III — Electromagnetic Charge

### EM.9 — Chain end-charge

**Thm.** [D3.4]
$$
q_{\mathrm{EM}}(c)=\frac{\sigma_{s(c)}-\sigma_{t(c)}}{2}\in\{-1,0,+1\};\qquad
\text{all three values attained};\qquad
\begin{array}{c|cccc}
(\sigma_s,\sigma_t) & (+,+) & (+,-) & (-,+) & (-,-)\\ \hline
q_{\mathrm{EM}} & 0 & +1 & -1 & 0
\end{array}
$$

**Req.** D3.4; CT0.9 (Part 1).

**Pf.**
$$
\mathrm{CT0.9}:\ \sigma_e\in\{+1,-1\}\implies\sigma_{s(c)},\sigma_{t(c)}\in\{+1,-1\}\implies q_{\mathrm{EM}}\in\bigl\{\tfrac{1-1}2,\tfrac{1-(-1)}2,\tfrac{-1-1}2,\tfrac{-1-(-1)}2\bigr\}=\{0,+1,-1\}
$$
$$
\text{end phases}=\text{independent registers}\implies\forall(\sigma_s,\sigma_t)\in\{\pm1\}^2\ \text{realizable}.\ \blacksquare
$$

**Phys.** The charge of an open chain is the half-difference of its two end-signs: a ternary alphabet arising from binary edges. (Cited in **D** as EW.36’s independent counterpart, and in **G**.)


**Cor EM.9b (chain-wall telescoping).** Let $c=(e_1,\dots,e_k)$, $k\ge2$, be an oriented chain of distinct real edges [D1.4] with interior vertices $v_1,\dots,v_{k-1}$, $v_i:=t(e_i)=s(e_{i+1})$, each of type $(1,1)$ [A7, D0.8] — the chain's two edges are $v_i$'s only incident real edges. Then the D3.3 vertex reads telescope:
$$
\sum_{i=1}^{k-1}f_{v_i}\ =\ \tfrac12\bigl(\sigma_{e_k}-\sigma_{e_1}\bigr)\ =\ -\,q_{\mathrm{EM}}(c)
\qquad\bigl[\sigma_{s(c)}=\sigma_{e_1},\ \ \sigma_{t(c)}=\sigma_{e_k}:\ \mathrm{D3.4}/\mathrm{EM.9}\ \text{end registers}\bigr]
$$
— the total interior vertex activity of a chain is carried by its two end registers alone. In particular:
$$
\sum_{i=1}^{k-1}f_{v_i}=0\iff\sigma_{e_1}=\sigma_{e_k}\iff q_{\mathrm{EM}}(c)=0;\qquad
\sum_{i=1}^{k-1}\aleph_{v_i}=\#\{i:\ \sigma_{e_{i+1}}\ne\sigma_{e_i}\}\le k-1\qquad[\mathrm{D3.3}:\ \aleph_v=|f_v|;\ \mathrm{CT0.9}].
$$

**Req (Cor).** A7; D0.8, D1.4, D3.3, D3.4; CT0.9 (Part 1); EM.9; finite telescoping [math; machine: `checks/verify_promotion_E_telescoping.py`].

**Pf (Cor).**
$$
\text{type}(1,1)\ [\mathrm{A7},\mathrm{D0.8}]:\ \sigma_{\leftarrow}(v_i)=\sigma_{e_i},\ \ \sigma_{\rightarrow}(v_i)=\sigma_{e_{i+1}};\qquad
\mathrm{D3.3}:\ f_{v_i}=\tfrac12\bigl(\sigma_{\rightarrow}(v_i)-\sigma_{\leftarrow}(v_i)\bigr)=\tfrac12\bigl(\sigma_{e_{i+1}}-\sigma_{e_i}\bigr)
$$
$$
\sum_{i=1}^{k-1}f_{v_i}=\tfrac12\sum_{i=1}^{k-1}\bigl(\sigma_{e_{i+1}}-\sigma_{e_i}\bigr)=\tfrac12\bigl(\sigma_{e_k}-\sigma_{e_1}\bigr)\quad[\text{telescoping}];\qquad
\mathrm{D3.4}/\mathrm{EM.9}:\ q_{\mathrm{EM}}(c)=\tfrac12\bigl(\sigma_{e_1}-\sigma_{e_k}\bigr)=-\sum_{i}f_{v_i}
$$
$$
\mathrm{CT0.9}:\ \sigma\in\{\pm1\}:\ f_{v_i}\ne0\iff\sigma_{e_{i+1}}\ne\sigma_{e_i};\qquad\aleph_{v_i}=|f_{v_i}|\in\{0,1\}\ [\mathrm{D3.3}]\ \blacksquare
$$


---

### EM.9a — The closed-core charge read and the end-register count

**Thm.** $(1)$ **Closed-core read.** For a closed oriented chain $c=(e_1,\dots,e_k)$ based at $v=s(c)=t(c)$ [D1.4: ordered tuple] with first edge $e_1$ (out of $v$) and last edge $e_k$ (into $v$):
$$q_{\mathrm{core}}(c;v):=\frac{\sigma_{e_1}-\sigma_{e_k}}{2}\ \in\ \{-1,0,+1\}$$
is well-defined [D3.4 applied to closed $c$; CT0.9: per-edge independent registers; EM.9: alphabet, all values attained].
$(2)$ **Charge-conjugation law.** Under rebase / orientation reversal the roles of $e_1$ and $e_k$ swap:
$$q_{\mathrm{core}}\ \mapsto\ -\,q_{\mathrm{core}}$$
— consistent with, and an instance of, D2.6's $\omega$ (charge $\mapsto$ $-$charge): the corpus's own charge-conjugation law, verbatim on the core read. At the 2-cycle floor: $q_{\mathrm{core}}=\tfrac12(\sigma_{e_1}-\sigma_{e_2})$ at base $p$, negated at base $q$.
$(3)$ **End-register count.** The EM.9/D3.4 read consumes exactly the two end registers of the chain: $N_{\mathrm{charge}}=2$ is a theorem, $\neg$an enumeration convention; the ternary alphabet is the difference of two binary registers [CT0.9], with all three values attained (witnesses $(\sigma_1,\sigma_k)=(+,-)\mapsto+1$, $(+,+)\mapsto0$, $(-,+)$ or $(-,-)\mapsto$ the remaining values; surjectivity machine-checked).
$(4)$ **Not neutral by closure.** The closed core is $\neg$forced charge-neutral: its ternary read is basepoint data. The observer-facing charge of a transit chain remains the EM.9 end-read.

**Req.** A1; D1.4, D2.6, D3.4; CT0.9 (Part 1); EM.9; witness enumeration [math; machine: `checks/verify_merge_tierB.py` §D].

**Pf.**
$$(1):\ \mathrm{D3.4}\ \text{is stated for oriented chains generally};\quad \text{closed}\ c:\ s(c)=t(c)=v\ \text{with distinguished first/last edges}\ [\mathrm{D1.4}]\implies\sigma_{s(c)}:=\sigma_{e_1},\ \sigma_{t(c)}:=\sigma_{e_k}\ \text{well-defined}
$$
$$\mathrm{CT0.9}:\ \sigma_{e_1},\sigma_{e_k}\in\{\pm1\}\ \text{independent};\qquad q_{\mathrm{core}}\in\{\tfrac12(\pm1\mp1)\}=\{-1,0,+1\};\qquad \mathrm{EM.9}:\ \text{all attained}$$
$$(2):\ \text{rebase/orientation reversal}:\ e_1\leftrightarrow e_k\ \text{roles swap}\implies q_{\mathrm{core}}\mapsto\tfrac12(\sigma_{e_k}-\sigma_{e_1})=-q_{\mathrm{core}};\qquad \mathrm{D2.6}:\ \omega\ \text{maps charge}\mapsto-\text{charge}:\ \text{consistent}$$
$$(3):\ \mathrm{D3.4}'\text{s formula contains exactly}\ \sigma_{s(c)},\sigma_{t(c)}:\ \text{two registers};\ \text{interior signs}\ \neg\text{enter};\quad \#\{\tfrac12(\sigma-\sigma'):\ \sigma,\sigma'\in\{\pm1\}\}=3$$
$$(4):\ (1)'\text{s witnesses include}\ q_{\mathrm{core}}=\pm1\ne0.\ \blacksquare$$

**Phys.** A closed chain carries a ternary charge-type read at its basepoint even though it has no ends: the difference of the two registers where it leaves and re-enters its base. Orientation reversal negates it exactly — charge conjugation acting on the only charge-like label closed content can carry. The count is rigid: two registers make a charge, as a theorem.

---

### EM.10 — Charge quantization

**Thm.**
$$
S^2=T^2=\mathbb1\ [\mathrm{A3}]\implies\phi_e\in\{0,\pi\}\implies\sigma_e\in\{+1,-1\}\implies\sigma_{s}-\sigma_{t}\in\{-2,0,+2\}\implies q_{\mathrm{EM}}\in\mathbb Z\cap\{-1,0,+1\};
$$
$$
q\notin\mathbb Z\implies\phi_e\notin\Phi\implies\neg\mathrm{CT0.9}\qquad(\neg\exists\ \text{finer values}).
$$

**Req.** A3; D0.5, D3.4; CT0.9 (Part 1).

**Pf.**
$$
\mathrm{CT0.9}\ [\Leftarrow\mathrm{D0.5},\ \mathrm{A3}:\ S^2=T^2=\mathbb1\implies\text{residual holonomy}\ \mathbb Z_2]:\ \ \phi_e\in\{0,\pi\}\implies\sigma_e=e^{i\phi_e}\in\{\pm1\}
$$
$$
\sigma_s,\sigma_t\in\{\pm1\}\implies\sigma_s-\sigma_t\in\{-2,0,+2\}\subset2\mathbb Z\implies q_{\mathrm{EM}}=\tfrac12(\sigma_s-\sigma_t)\in\{-1,0,+1\}\subset\mathbb Z
$$
$$
q_{\mathrm{EM}}\notin\mathbb Z\implies\sigma_s-\sigma_t\ \text{odd}\implies\sigma\notin\{\pm1\}\implies\phi_e\notin\{0,\pi\}\implies\neg\mathrm{CT0.9}\implies\bot.\ \blacksquare
$$

**Phys.** Charge quantization is not imposed — it is the arithmetic shadow of the binary edge phase, which is itself forced by the involution axiom $S^2=T^2=\mathbb1$. Integers all the way down. (Cited in **G**.)

---

### EM.11 — Global charge conservation

**Thm.** $U$ valid [D2.11] $\implies\ \displaystyle Q_{\mathrm{EM}}:=\sum_{c\in U}q_{\mathrm{EM}}(c)=0.$

**Req.** D1.2, D1.3, D1.4, D2.11, D3.4; EM.9.

**Pf.**
$$
\mathrm{D3.4}:\ q_{\mathrm{EM}}(c)=\tfrac12\sigma_{s(c)}-\tfrac12\sigma_{t(c)}\implies
Q_{\mathrm{EM}}=\tfrac12\!\!\sum_{\text{source-ends}}\!\!\sigma\ -\ \tfrac12\!\!\sum_{\text{target-ends}}\!\!\sigma\qquad(\text{regroup by ends})
$$
$$
\mathrm{D2.11}:\ \neg\exists\ \text{dangling ledger boundary}\implies\forall\ \text{ends sealed}
$$
$$
\mathrm{D1.2}:\ \text{seal joins two edge-ends};\quad\mathrm{D1.4}:\ \text{chains oriented}\implies\text{seal joins target-end}\to\text{source-end}\ \ (\text{same-orientation join}\implies\neg\text{continuable orientation},\ \bot\,\mathrm{D1.4})
$$
$$
\mathrm{D1.3}:\ \#J^+=\#J^-\implies\text{pairing covers every end exactly once}
$$
$$
\text{seal identifies joined ends}\implies\text{equal}\ \sigma\implies\text{per-seal contribution}=\tfrac12\sigma-\tfrac12\sigma=0
$$
$$
Q_{\mathrm{EM}}=\sum_{\text{seals}}0=0.\ \blacksquare
$$

**Phys.** Total charge vanishes in every valid universe: each chain end is sealed against an oppositely oriented end carrying the same sign. Charge conservation is Janus topology — seals pair sources with sinks — not a Noether afterthought.

---

## §E.IV — Field Strength and Dynamics

### EM.12 — Discrete field strength from phase transitions

**Thm.** [D3.3]
$$
f_v=\tfrac12\bigl(\sigma_{\rightarrow}(v)-\sigma_{\leftarrow}(v)\bigr)\in\{-1,0,+1\};\qquad\aleph_v=|f_v|\in\{0,1\};
$$
$$
\aleph(\sigma,C)=0\iff\forall v:\ \sigma_{\leftarrow}(v)=\sigma_{\rightarrow}(v)\iff\sigma\ \text{constant on connected components}\ \ (\text{flat});
$$
$$
\aleph_v=1\iff\text{oriented transition at}\ v;\qquad
\text{coarse-graining}\ [\mathrm{CT1.19}]:\ f_v\longrightarrow F_{\mu\nu}\ \ (\text{circulation per plaquette})\ [\mathrm{CT1.22}].
$$

**Req.** D3.3; CT0.9 (Part 1); CT1.19, CT1.22 (Part 2).

**Pf.**
$$
\sigma_{\leftarrow},\sigma_{\rightarrow}\in\{\pm1\}\ [\mathrm{CT0.9}]\implies f_v\in\{-1,0,+1\},\ \ |f_v|\in\{0,1\}=\aleph_v\quad[\mathrm{D3.3}]
$$
$$
\aleph=0\iff\forall v:\ \aleph_v=0\iff\forall v:\ \sigma_{\leftarrow}=\sigma_{\rightarrow}\iff\sigma\ \text{constant along components}\quad(\text{zero discrete curvature})
$$
$$
\aleph_v=1\iff\sigma_{\leftarrow}\ne\sigma_{\rightarrow}\iff f_v=\pm1:\ \text{oriented transition}
$$
$$
\mathrm{CT1.19}:\ \text{holonomy per unit area}\to F_{\mu\nu}\ [\mathrm{CT1.22}];\quad\text{vertex sign flip}=\text{nonzero circulation}.\ \blacksquare
$$

**Phys.** The electromagnetic field on the ledger is the sign mismatch at vertices: $f_v$ is the oriented discrete field strength and $\aleph_v$ its magnitude. Zero excitation means signs flow unflipped; each flip is one excitation quantum.

---

### EM.13 — The transition-parity factor in the weight

**Thm.** $w(C)=\mathcal J(C)\prod_{e}G(e)\cdot(-1)^{\aleph(\sigma,C)}$ [A8]:
$$
(-1)^{\aleph}=\begin{cases}+1&\aleph\ \text{even}\\ -1&\aleph\ \text{odd}\end{cases};\qquad
\prod_eG(e)\supseteq\prod_e\sigma_e\ [\mathrm{D3.5}];\qquad
\Bigl(\prod_e\sigma_e\Bigr)\ \text{independent of}\ (-1)^{\aleph}\ [\mathrm{CT0.10}];
$$
$$
Z(\mathcal R)=\sum_C\sum_\sigma w(C):\ \ \Delta\aleph\ \text{odd}\implies\text{sign flip}\implies\text{destructive interference}\ \ (\text{discrete EM dynamics});\quad
\text{coarse-graining}\implies\text{relative signs of}\ F_{\mu\nu}.
$$

**Req.** A8; D3.5; CT0.9, CT0.10 (Part 1).

**Pf.**
$$
(-1)^{\aleph}\in\{+1,-1\}\ \text{by parity}\ [\text{definition}]
$$
$$
\mathrm{D3.5}:\ G(e)=\sigma_e\exp\bigl(i\alpha_e\widehat{ds}^{\,2}(e)\bigr)\implies\prod_eG(e)\supseteq\prod_e\sigma_e
$$
$$
\mathrm{CT0.10}:\ \Bigl(\prod_e\sigma_e,\ (-1)^{\aleph}\Bigr)\ \text{independent},\ \text{joint image}=\{\pm1\}^2\implies\text{two distinct sign data};\ \neg\text{double counting}
$$
$$
Z:\ C\mapsto C'\ \text{with}\ \Delta\aleph\ \text{odd}\implies w(C')=-w(C)\ \text{(ceteris paribus)}\implies\text{cancellation}.\ \blacksquare
$$

**Phys.** The A8 weight assigns a strict minus sign to every odd number of domain walls in the sign field: this destructive interference between one-transition-apart configurations *is* the lattice dynamics of electromagnetism, and it survives coarse-graining as the Maxwell sign structure.

---

### EM.14 — Continuum gauge invariance

**Thm.**
$$
A_\mu\sim A_\mu+\nabla_\mu\chi;\qquad
F_{\mu\nu}=2\nabla_{[\mu}A_{\nu]}\ \mapsto\ F_{\mu\nu}+2\nabla_{[\mu}\nabla_{\nu]}\chi=F_{\mu\nu};
$$
$$
\implies\text{gradient direction}=\text{redundancy};\quad N_{\mathrm{pol}}\ \text{count unaffected}\ [\mathrm{EM.8}].
$$

**Req.** CT1.22, CT2.6 (Part 2); EM.12; $\nabla_{[\mu}\nabla_{\nu]}\chi=0$ for scalars [math].

**Pf.**
$$
\mathrm{EM.12}:\ \text{physical datum}=f_v\propto\sigma_{\rightarrow}-\sigma_{\leftarrow}:\ \text{differences only};\ \neg\text{dependence on common offset}
$$
$$
\text{smooth offset field}\xrightarrow[\mathrm{CT1.19}]{}\chi:\quad A_\mu\mapsto A_\mu+\nabla_\mu\chi
$$
$$
F_{\mu\nu}\mapsto F_{\mu\nu}+2\nabla_{[\mu}\nabla_{\nu]}\chi=F_{\mu\nu}\quad[\nabla_\mu\nabla_\nu\chi=\nabla_\nu\nabla_\mu\chi\ \text{on scalars}].\ \blacksquare
$$

**Phys.** Gauge invariance is the continuum image of a ledger triviality: vertices record sign *changes*, never absolute signs. The redundancy is derived from the discreteness, not postulated.

---

### EM.15 — Electromagnetic stress-energy

**Thm.**
$$
S_{\mathrm{EM}}[A,g]=-\tfrac14\int d^4x\sqrt{-g}\,F_{\mu\nu}F^{\mu\nu};\qquad
T^{(\mathrm{EM})}_{\mu\nu}:=-\frac{2}{\sqrt{-g}}\frac{\delta S_{\mathrm{EM}}}{\delta g^{\mu\nu}}=F_{\mu\rho}F_\nu{}^{\rho}-\tfrac14g_{\mu\nu}F_{\alpha\beta}F^{\alpha\beta};
$$
$$
g^{\mu\nu}T^{(\mathrm{EM})}_{\mu\nu}=0\qquad(D=4).
$$

**Req.** CT1.22 (Part 2); EM.6; $\delta\sqrt{-g}=-\tfrac12\sqrt{-g}\,g_{\mu\nu}\delta g^{\mu\nu}$, $\delta\bigl(g^{\mu\alpha}g^{\nu\beta}F_{\mu\nu}F_{\alpha\beta}\bigr)=2F_{\mu\rho}F_\nu{}^\rho\,\delta g^{\mu\nu}$ [math; machine: `checks/verify_E.py`].

**Pf.**
$$
\mathrm{CT1.22}:\ S_{\mathrm{EM}}=\text{unique local, diff-}\wedge\text{gauge-invariant},\ \le2\text{nd-order functional quadratic in}\ F
$$
$$
\delta S_{\mathrm{EM}}=-\tfrac14\int\sqrt{-g}\Bigl[\underbrace{-\tfrac12g_{\mu\nu}F^2}_{\delta\sqrt{-g}}+\underbrace{2F_{\mu\rho}F_\nu{}^{\rho}}_{\delta(F^2)}\Bigr]\delta g^{\mu\nu}\qquad[F_{\mu\nu}\ \text{fixed lower indices}]
$$
$$
T^{(\mathrm{EM})}_{\mu\nu}=-\tfrac{2}{\sqrt{-g}}\cdot(-\tfrac14)\sqrt{-g}\bigl[2F_{\mu\rho}F_\nu{}^{\rho}-\tfrac12g_{\mu\nu}F^2\bigr]=F_{\mu\rho}F_\nu{}^{\rho}-\tfrac14g_{\mu\nu}F_{\alpha\beta}F^{\alpha\beta}
$$
$$
\text{trace}:\ \ g^{\mu\nu}T_{\mu\nu}=F_{\mu\rho}F^{\mu\rho}-\tfrac14\cdot4\cdot F^2=0\qquad[\text{consistency}:\ \text{massless transit aspect},\ \mathrm{EM.6}].\ \blacksquare
$$

**Phys.** The Maxwell stress tensor is derived as the metric variation of the unique admissible quadratic action — the $a=\mathrm{EM}$ instance of CT1.22 — and its vanishing trace is the local imprint of photon masslessness.

---

## §E.V — The Dynamic Phase

### EM.16 — Edge transfer weight and the per-edge read-back

**Thm.** [D3.5] For every real edge $e$:
$$
G(e)=\sigma_e\,\exp\!\bigl(i\,\alpha_e\,\widehat{ds}^{\,2}(e)\bigr);\qquad
\alpha_e=\frac1i\,\frac{\partial}{\partial\,\widehat{ds}^{\,2}(e)}\log\!\bigl(\sigma_e^{-1}G(e)\bigr);\qquad
[\alpha_e]=\mathfrak q^{0}.
$$

**Req.** D0.5, D1.6, D2.8, D2.9, D3.5; CT2.1 (Part 2).

**Pf.**
$$
\sigma_e^{-1}=\sigma_e\ (\sigma_e^2=1)\implies\sigma_e^{-1}G(e)=\exp\bigl(i\alpha_e\widehat{ds}^{\,2}(e)\bigr)
$$
$$
\log\ \text{on the}\ \mathrm{D2.8}\ \text{branch}=i\alpha_e\widehat{ds}^{\,2}(e);\qquad
\tfrac1i\,\partial_{\widehat{ds}^{\,2}}\implies\alpha_e\quad(\text{constant along the edge: the read-back is per-edge})
$$
$$
[\widehat{ds}^{\,2}]=\frac{[ds^2]}{[\mathfrak h^2]}=\frac{\mathfrak q^{-1}}{\mathfrak q^{-1}}=\mathfrak q^{0}\ [D1.6,D2.9];\qquad[\text{phase}]=\mathfrak q^0\implies[\alpha_e]=\mathfrak q^{0}. \blacksquare
$$

**Phys.** The transfer weight of an edge factors cleanly into a binary registration sign and a dimensionless geometric phase carrying the edge's own $\alpha_e$; hop-normalization makes every per-edge phase a pure number from the outset — not a later repair.

---

### EM.17 — Spectral read of the electromagnetic block

**Thm.** $\ \forall n\ge2:$ the masked force acts as a scalar on the one-dimensional EM block [CT0.14, D2.3]:
$$
\mathbf F_M^{(n)}\big|_{\mathcal K^{(\mathrm{EM})}}=\alpha_{\mathrm{EM}}^{(n)}\cdot\mathrm{id};\qquad
\alpha_{\mathrm{EM}}^{(n)}=\frac{\mathfrak T\bigl(Y_{\mathrm{asp}}\,\mathbf F_M^{(n)}\,Y_{\mathrm{asp}}\bigr)}{\mathfrak T\bigl(Y_{\mathrm{asp}}\bigr)}=\mathfrak T\bigl(Y_{\mathrm{asp}}\,\mathbf F_M^{(n)}\,Y_{\mathrm{asp}}\bigr);\qquad
\mathfrak T\bigl(Y_{\mathrm{asp}}\bigr)=1.
$$
$\alpha_{\mathrm{EM}}^{(n)}$ is the force-space block-scale read at rung $n$; the edge phases $\alpha_e$ are per-edge registration data [D3.5, EM.20].

**Req.** D2.3; CT0.14 (Part 1); CT2.4 (Part 2); EM.2; EW.8 (Part 2); machine: `checks/verify_E.py`.

**Pf.**
$$
\dim\mathcal K^{(\mathrm{EM})}=1\ [CT0.14]\implies\mathbf F_M^{(n)}\big|_{\mathcal K^{(\mathrm{EM})}}=\alpha_{\mathrm{EM}}^{(n)}\cdot\mathrm{id}\quad[\text{every operator on a 1-dim space is a scalar};\ \alpha_{\mathrm{EM}}^{(n)}:=\text{that eigenvalue}]
$$
$$
\mathrm{D2.3}\ \text{orthogonality}:\quad A\ne\mathrm{EM}:\ \ Y_{\mathrm{asp}}F_AY_{\mathrm{asp}}=\mathcal P^{(\mathrm{EM})}F_A\mathcal P^{(\mathrm{EM})}=0\implies Y_{\mathrm{asp}}\mathbf F_M^{(n)}Y_{\mathrm{asp}}=\alpha_{\mathrm{EM}}^{(n)}Y_{\mathrm{asp}}
$$
$$
\mathfrak T:\quad\mathfrak T\bigl(Y_{\mathrm{asp}}\mathbf F_M^{(n)}Y_{\mathrm{asp}}\bigr)=\alpha_{\mathrm{EM}}^{(n)}\,\mathfrak T\bigl(Y_{\mathrm{asp}}\bigr)=\alpha_{\mathrm{EM}}^{(n)}\quad[\mathfrak T(Y_{\mathrm{asp}})=1,\ \mathrm{EM.2}].\ \blacksquare
$$

**Rmk (repair).** The prior formula $\mathfrak T(Y\mathbf F_M^{(n)}Y)/\mathfrak T(Y)$ with $Y=\mathcal P_M^{(2)}$ ($\mathfrak T=17$) is false as written: the rank-$2$ mask retains $J,G,W,H,D^+,\mathrm{EM}$, whose sum is not a scalar on $\mathcal K_2$. With the rank-one $Y_{\mathrm{asp}}$ the identity is exact — a 1-dimensional block has one eigenvalue and nothing else can contribute.

**Phys.** The electromagnetic block scale is read off operatorially: the single eigenvalue of the masked force on the one-dimensional EM block. A spectral formula replaces any fitting procedure. It is force-space data, distinct from the per-edge registration phases of EM.20. (Cited in **F**.)

---

### EM.18 — The colour sector does not shift the block read

**Thm.** $ \alpha_{\mathrm{EM}}^{(3)}=\alpha_{\mathrm{EM}}^{(2)}.$

**Req.** CT0.13, CT0.14 (Part 1); CT2.4 (Part 2); EM.17; [CT3.7 (Part 2) — forward, corroboration only].

**Pf.**
$$
\mathrm{CT0.13}:\ \mathcal A(3)=\mathcal A(2)\cup\{\mathrm{strong}\}\implies\mathbf F_M^{(3)}=\mathbf F_M^{(2)}\oplus F_{\mathrm{strong}}\quad[CT2.4]
$$
$$
\mathrm{CT0.14}:\ \mathcal K^{(\mathrm{strong})}\perp\mathcal K^{(\mathrm{EM})}\implies
Y_{\mathrm{asp}}\,F_{\mathrm{strong}}\,Y_{\mathrm{asp}}=\mathcal P^{(\mathrm{EM})}F_{\mathrm{strong}}\mathcal P^{(\mathrm{EM})}=0
$$
$$
\bigl[\text{corroboration}: \mathfrak T(T_a)=0\ [CT3.7]\implies\mathfrak T(F_{\mathrm{strong}})=\textstyle\sum_af_a\mathfrak T(T_a)=0\ \text{--- independent argument}\bigr]
$$
$$
\implies Y_{\mathrm{asp}}\mathbf F_M^{(3)}Y_{\mathrm{asp}}=Y_{\mathrm{asp}}\mathbf F_M^{(2)}Y_{\mathrm{asp}}\implies\alpha_{\mathrm{EM}}^{(3)}=\alpha_{\mathrm{EM}}^{(2)}\quad[EM.17].\ \blacksquare
$$

**Phys.** Switching colour on at rung 3 adds traceless structure orthogonal to the electromagnetic block: the block read does not run. Two disjoint arguments — block orthogonality and colour tracelessness — agree. (Cited in **F**.)

---

### EM.19 — The saturation sector does not shift the block read

**Thm.** On the accessible rung-2 subspace: $ \alpha_{\mathrm{EM}}^{(n)}=\alpha_{\mathrm{EM}}^{(2)}\quad\forall n\ge4.$

**Req.** CT0.6, CT0.11, CT0.13, CT0.14 (Part 1); D4.1; EM.17, EM.18.

**Pf.**
$$
\mathrm{CT0.13}:\ \mathcal A(n\ge4)=\mathcal A(3)\cup\{D^-\}
$$
$$
\mathrm{D4.1}:\ F_{D^-}=\bigoplus_{m\ge4}F_m\ \text{acts only on oversubscribed rungs}\ m\ge4\ [CT0.6]
$$
$$
\mathrm{CT0.11}:\ \mathcal K_2\ \neg\text{oversubscribed};\quad\mathrm{CT0.14}:\ \mathcal K^{(\mathrm{EM})}\perp\mathcal K^{(D^-)}\implies Y_{\mathrm{asp}}F_{D^-}Y_{\mathrm{asp}}=0
$$
$$
\implies Y_{\mathrm{asp}}\mathbf F_M^{(n)}Y_{\mathrm{asp}}=Y_{\mathrm{asp}}\mathbf F_M^{(3)}Y_{\mathrm{asp}}\overset{\mathrm{EM.18}}{=}Y_{\mathrm{asp}}\mathbf F_M^{(2)}Y_{\mathrm{asp}}\implies\alpha_{\mathrm{EM}}^{(n)}=\alpha_{\mathrm{EM}}^{(2)}\quad[EM.17].\ \blacksquare
$$

**Phys.** The saturation lock absorbs oversubscribed information without renormalizing the accessible electromagnetic block read: $\alpha_{\mathrm{EM}}$ is rung-independent across all accessible rungs.

---

### Def-EM.20 — The per-edge phase at crystallization

**Def.** For each real edge $e=(s,t)$ [A4, D0.1], the phase $\alpha_e\in\Phi$ [D0.5] is the branch index of the A4 crystallization criterion for the pair state $\rho_{st}$ at the seal [A4, D1.2]:
$$
\alpha_e\ :=\ \alpha_{st}\ :=\ \begin{cases} 0 & \text{if } \bigl|\Pi_{\mathcal V}\rho_{st}\bigr|\le\varepsilon_q \quad \text{(aligned branch)} \\ \pi & \text{if } \bigl|\Pi_{\mathcal V}\rho_{st}\bigr|\ge 1-\varepsilon_q \quad \text{(antialigned branch)} \end{cases}
$$
— A4 declares the branch phase $\alpha_{pq}$ and both branches' non-emptiness; A7 declares the edge map $e\mapsto\alpha_e\in\{0,\pi\}$; this definition is the identification $\alpha_e=\alpha_{st}$. The branch windows are disjoint exactly when $\varepsilon_q<1-\varepsilon_q$, guaranteed by the admissible range $\varepsilon_q\in[0,\tfrac14)$ [CT0.8]. The branch read is a registration alternative [D1.1: the reality principle — registration transport acts on the reality line by $\{+1,-1\}$]: aligned $\leftrightarrow+1$, antialigned $\leftrightarrow-1$, so $e^{i\alpha_e}\in\{+1,-1\}$ is the alignment holonomy. Virtual pairs ($\varepsilon_q<\bigl|\Pi_{\mathcal V}\rho_{st}\bigr|<1-\varepsilon_q$) carry no $\alpha_e$ [A4, CT0.1; clause (3) of EM.20]


---

### EM.20 — The dynamic edge phase

**Thm.** With $\alpha_e$ as in Def-EM.20, under A1 ($\mathbb C^2$ qubits), A4 (two-branch crystallization; branch phase $\alpha_{pq}$; both branches populated), A5 (vacuum $\rho_\circ=I/4$; Haar draws), A6 (tick dynamics), A7 (edge phase map), CT0.9 ($\Phi=\{0,\pi\}$), D0.4 ($\varepsilon_q$), D1.6 ($\widehat{ds}^{\,2}$), D3.5 (edge weight):
$(1)$ **Alphabet preservation.** $\alpha_e\in\{0,\pi\}=\Phi$ for every real edge $e$; the phase alphabet is unchanged. [A4, A7; CT0.9]
$(2)$ **Phase determination.** $\alpha_e=\alpha_{st}$ is the branch index of the A4 criterion for the pair state at the moment of crystallization [A4, D1.2]: the phase is a measurement outcome — registration data read at the seal [D1.1] — $\neg$ a declared constant.
$(3)$ **Virtual edges.** For $e\in\mathcal V$ [CT0.1: $\varepsilon_q<\bigl|\Pi_{\mathcal V}\rho_{st}\bigr|<1-\varepsilon_q$] the pair carries the full $\mathbb C^2\otimes\mathbb C^2$ statespace [A1]; $\alpha_e$ is undefined. The binary restriction scopes to real (crystallized) edges.
$(4)$ **Edge weight.** $G(e)=\sigma_e\cdot e^{i\alpha_e\,\widehat{ds}^{\,2}(e)}$ with $\alpha_e$ per-edge. [D3.5]
$(5)$ **Both values attained; distribution governed.** Both A4 branches are populated [A4 populatedness clause]; witnesses: a symmetric-dominated pair ($\bigl|\Pi_{\mathcal V}\rho\bigr|=0\Rightarrow\alpha_e=0$) and the pure singlet ($\bigl|\Pi_{\mathcal V}\rho\bigr|=1\Rightarrow\alpha_e=\pi$). Across $E_{\mathcal R}$ the distribution of $\alpha_e$ is governed by the Haar randomization [A5, A6] and the crystallization criterion [A4].

**Req.** A1; A4; A5; A6; A7; CT0.9 (Part 1); D0.4, D1.1, D1.2, D1.6, D3.5; Def-EM.20; exhaustive exact pair-state census [math; machine: `checks/verify_F33_dynamic_phase.py` §A].

**Pf.**
$$
(1):\ \mathrm{A4}:\ \alpha_{pq}\in\{0,\pi\}\ \forall(p,q)\in\mathcal R;\qquad \mathrm{A7}:\ e\in E_{\mathcal R}\mapsto\alpha_e\in\{0,\pi\};\qquad \mathrm{CT0.9}:\ \Phi=\{0,\pi\}\implies\alpha_e\in\Phi
$$
$$
(2):\ \mathrm{A4}/\mathrm{D1.2}:\ e\in\mathcal R\iff\text{branch membership at a seal};\qquad \mathrm{Def\text{-}EM.20}:\ \alpha_e=\alpha_{st}=\text{branch index}
$$
$$
\mathrm{D1.1}:\ \text{registration transport acts on the reality line by}\ \{\pm1\}\implies e^{i\alpha_e}=\text{alignment holonomy}\in\{+1,-1\}:\ \text{a function of the registered pair state},\ \neg\text{a constant}
$$
$$
(3):\ \mathrm{CT0.1}/\mathrm{A4}:\ e\in\mathcal V\iff\varepsilon_q<\bigl|\Pi_{\mathcal V}\rho_{st}\bigr|<1-\varepsilon_q\iff\neg\bigl(\text{registration}\bigr);\qquad \mathrm{A1}:\ \rho_{st}\in\mathfrak H(\mathbb C^2\otimes\mathbb C^2)\ \text{retained without branch read}\implies\alpha_e\ \text{undefined}
$$
$$
(4):\ \mathrm{D3.5}:\ G(e)=\sigma_e\exp\bigl(i\alpha_e\widehat{ds}^{\,2}(e)\bigr)\ \text{with per-edge}\ \alpha_e=\alpha_{st}\ [\mathrm{A4}];\qquad \mathrm{D1.6}:\ \widehat{ds}^{\,2}(e)\ \text{well-defined per edge}
$$
$$
(5):\ \mathrm{A4}:\ \exists\,\rho:\ \bigl|\Pi_{\mathcal V}\rho\bigr|\le\varepsilon_q\ \wedge\ \exists\,\rho':\ \bigl|\Pi_{\mathcal V}\rho'\bigr|\ge1-\varepsilon_q;\qquad \text{witnesses}:\ \rho=\Pi_{\mathcal R}/3\ (w=0,\ \alpha=0);\quad \rho=\Pi_{\mathcal V}\ (w=1,\ \alpha=\pi)\ [\mathrm{CT0.7};\ \text{machine}]
$$
$$
\mathrm{A5}/\mathrm{A6}:\ \text{node states Haar-drawn per tick}\ (U\notin\mathfrak L:\ \text{draws are not retained; registered reads are});\qquad \mathrm{A4}:\ \text{which pairs crystallize, and on which branch}.\ \blacksquare
$$

**Phys.** Every real edge carries its own geometric phase: the branch index of the pair's crystallization criterion — symmetric-dominated pairs register $0$, singlet-dominated pairs register $\pi$ — valued in exactly the CT0.9 alphabet, with the two branch windows disjoint on the admissible threshold range ($\varepsilon_q<1-\varepsilon_q$; CT0.8). Which branch an edge takes is measurement outcome data, governed by the Haar randomization and the criterion. All downstream phase structure — the alignment patterns and parity classes (EM.23), the CPT bridge (EM.24) — reads this per-edge datum.

---

### EM.21 — Dimensional status of the per-edge phase

**Thm.** $ \ [\alpha_e]=\mathfrak q^{0};\qquad \mathfrak h\mapsto\lambda\mathfrak h:\ \ \{0,\pi\}\mapsto\{0,\pi\};$ i.e. the phase alphabet is a derived pure-number set in the sense of CT2.11, and each $\alpha_e$ is an $\mathfrak h$-free registration value [EM.20(2)].

**Req.** D1.6; CT2.11 (Part 2); EM.16, EM.20.

**Pf.**
$$
[\widehat{ds}^{\,2}]=\mathfrak q^0\ [EM.16];\qquad[\alpha_e\widehat{ds}^{\,2}]=[\text{phase}]=\mathfrak q^0\implies[\alpha_e]=\mathfrak q^0
$$
$$
\mathfrak h\mapsto\lambda\mathfrak h:\ \ ds^2\mapsto\lambda^2ds^2,\ \mathfrak h^2\mapsto\lambda^2\mathfrak h^2\implies\widehat{ds}^{\,2}\ \text{invariant};\qquad
\text{alphabet fixed by}\ \mathfrak h\text{-free data}\ [CT0.9,\ EM.20(1)]\implies\alpha_e\in\{0,\pi\}\ \text{in every calibration}
$$
$$
\mathrm{CT2.11}\ \text{criterion}:\ \text{dimensionless}\ \wedge\ \text{rescaling-invariant}\implies\text{derived pure-number alphabet}. \blacksquare
$$

**Phys.** The phase alphabet $\{0,\pi\}$ is calibration-independent: it survives the rescaling of the single free scale, marking it as a genuine prediction rather than a unit convention. Individual phase values are $\mathfrak h$-free too — binary registration outcomes.

---

## §E.VI — Parity and CPT

### Def-EM.21 — Alignment pattern

**Def.** For a subnetwork $\Sigma$ [D2.13] with real edge set $E_{\mathcal R}(\Sigma):=\{e\in E_{\mathcal R}:\ e\ \text{touches}\ \Sigma\}$ ($|\Sigma|=\#E_{\mathcal R}(\Sigma)$, D2.13), the alignment pattern is
$$
\mathcal P(\Sigma)\ :=\ \bigl\{\,e\in E_{\mathcal R}(\Sigma):\ \alpha_e=\pi\,\bigr\}
$$
— the set of antialigned edges [Def-EM.20]. $\mathcal P(\Sigma)\subseteq E_{\mathcal R}(\Sigma)$; on a chain $c$ [D1.4]: $\mathcal P(c):=\mathcal P(\Sigma)\cap c$; on a configuration $C$ [D0.10]: $\mathcal P(C):=\{e\in E(C):\ \alpha_e=\pi\}$.

---

### Def-EM.22 — Mirror operation

**Def.** A mirror $M$ on $\Sigma$ is an automorphism of the underlying graph of $\Sigma$ that reverses orientation [D2.6 $\omega$-type: $s\leftrightarrow t$]. $M$ acts on the alignment pattern:
$$
M(\mathcal P(\Sigma))\ :=\ \bigl\{M(e):\ e\in\mathcal P(\Sigma)\bigr\}
$$
where $\Sigma$ admits such an automorphism (witnesses: path and cycle reflections — machine, `checks/verify_F33_dynamic_phase.py` §B).

---

### EM.23 — Parity classification

**Thm.** Under Def-EM.21 and Def-EM.22, for a subnetwork $\Sigma$ with mirror $M$:
$(1)$ **Parity-preserving.** $\Sigma$ is parity-even $\iff M(\mathcal P(\Sigma))=\mathcal P(\Sigma)$: the alignment pattern is invariant under the mirror.
$(2)$ **Parity-reversing.** $\Sigma$ is parity-odd $\iff M(\mathcal P(\Sigma))=E_{\mathcal R}(\Sigma)\setminus\mathcal P(\Sigma)$: the alignment pattern inverts under the mirror.
$(3)$ **Distinguishability.** Parity-even and parity-odd subnetworks are distinguishable $\iff\mathcal P(\Sigma)\ne E_{\mathcal R}(\Sigma)\setminus\mathcal P(\Sigma)$ — the alignment pattern is not self-complementary — which holds exactly when $E_{\mathcal R}(\Sigma)\ne\varnothing$: at least one real edge ("there is something" — CT2.6(i) as the definitional precondition it is, D2.11).
$(4)$ **Degrees of freedom.** The number of distinct alignment patterns on $\Sigma$ is $2^{|E_{\mathcal R}(\Sigma)|}$: each real edge carries an independent binary phase [CT0.9, EM.20(5)]. Each pattern is a distinct parity configuration. The uniform assignments ($\mathcal P=\varnothing$ and $\mathcal P=E_{\mathcal R}$) are two points of this space; any single fixed pattern occupies one point.

**Req.** Def-EM.20, Def-EM.21, Def-EM.22; A4; D2.11, D2.13; CT0.9 (Part 1); EM.20; independent-register enumeration, orbit counting [math; machine: `checks/verify_F33_dynamic_phase.py` §B].

**Pf.**
$$
(1),(2):\ \mathrm{Def\text{-}EM.22}:\ M\ \text{permutes}\ E_{\mathcal R}(\Sigma)\implies M(\mathcal P)\subseteq E_{\mathcal R}(\Sigma);\qquad\text{even}:=\text{fixed point of the induced action};\quad\text{odd}:=\text{complement image}
$$
$$
(3):\ e\in E_{\mathcal R}(\Sigma)\ne\varnothing:\ \ e\in\mathcal P\implies e\notin E_{\mathcal R}\setminus\mathcal P\implies\mathcal P\ne E_{\mathcal R}\setminus\mathcal P;\qquad E_{\mathcal R}=\varnothing:\ \mathcal P=\varnothing=E_{\mathcal R}\setminus\mathcal P
$$
$$
\text{even}\wedge\text{odd jointly}\iff M(\mathcal P)=\mathcal P=E_{\mathcal R}\setminus\mathcal P\iff E_{\mathcal R}=\varnothing\implies\text{distinguishable}\iff E_{\mathcal R}(\Sigma)\ne\varnothing
$$
$$
(4):\ \mathrm{CT0.9}/\mathrm{EM.20}(5):\ \text{each}\ e\in E_{\mathcal R}(\Sigma)\ \text{carries an independent}\ \alpha_e\in\{0,\pi\}\implies\#\{\mathcal P(\Sigma)\}=2^{|E_{\mathcal R}(\Sigma)|}\ [\text{power-set count}]
$$
$$
\text{uniform assignments}:\ \alpha\equiv0\iff\mathcal P=\varnothing;\quad\alpha\equiv\pi\iff\mathcal P=E_{\mathcal R}:\ \text{two of the}\ 2^{|E_{\mathcal R}|}.\ \blacksquare
$$

**Phys.** Parity is read off the ledger, not added to it: mirror-invariance of the antialigned set classifies every subnetwork even, odd, or unclassified, and the classification has teeth exactly when there is at least one real edge. The dynamic phase gives the pattern space its full $2^{|E_{\mathcal R}|}$ cardinality — uniform configurations are two points of it.

---

### EM.24 — The CPT bridge

**Thm.** On the configuration space $\mathfrak C(\mathcal R)$ [D0.10]:
$(1)$ **C (charge conjugation).** $q_{\mathrm{EM}}=\tfrac12(\sigma_s-\sigma_t)\in\{-1,0,+1\}$ [D3.4, EM.9]; charge conjugation $C:\sigma_e\mapsto-\sigma_e\ \forall e\in E(C)$ gives $q\mapsto-q$, $f_v\mapsto-f_v$, $\aleph_v$ invariant [D3.3]; the sign-level realization of D2.6's $\omega$ on end and core reads [EM.9a(2)]. Derived.
$(2)$ **P (parity).** The alignment pattern $\mathcal P(\Sigma)$ [Def-EM.21]; parity reversal $P:\mathcal P\mapsto E_{\mathcal R}\setminus\mathcal P$ — equivalently $\alpha_e\mapsto\pi-\alpha_e$ per edge — the inversion locus of EM.23(2). Derived from the dynamic phase [Def-EM.20, EM.20(1)].
$(3)$ **T (time reversal).** The Janus reflection $\Theta_{\mathfrak L}$ [D2.7]: $w(\Theta_{\mathfrak L}C)=w(C)^\ast$ [CT2.8(1)]. Derived.
$(4)$ **CPT composition.** $\mathrm{CPT}:=C\circ P\circ T$: well-defined on $\mathfrak C(\mathcal R)$; each component an involution ($C^2=P^2=T^2=\mathrm{id}$); each component derived from the corpus — no external input.
$(5)$ **CPT invariance.** The exact phase identity and its consequences:
$$
w(\mathrm{CPT}\,C)=(-1)^{|E(C)|}\,e^{i\pi\Theta(C)}\,w(C),\qquad\Theta(C):=\!\!\sum_{e\in E(C)}\!\!\widehat{ds}^{\,2}(e)\in\mathbb R;
$$
$$
\bigl|w(\mathrm{CPT}\,C)\bigr|^2=\bigl|w(C)\bigr|^2\qquad\forall C\ \ (\text{unconditional});
$$
$$
\text{on-shell}\ [\widehat{ds}^{\,2}(e)\in\mathbb Z\ \forall e]:\ \ w(C)\in\mathbb R\ \ \wedge\ \ \bigl(|E(C)|+\Theta(C)\equiv0\ (\mathrm{mod}\ 2)\bigr)\implies w(\mathrm{CPT}\,C)=w(C)^\ast .
$$

**Req.** A8; D0.5, D0.10; D1.6, D2.6, D2.7; D3.3, D3.4, D3.5, D3.6; CT0.9 (Part 1); CT2.8 (Part 2); Def-EM.20, Def-EM.21; EM.9, EM.9a, EM.20, EM.23; exhaustive small-model enumeration over $\mathbb Q(i)$ [math; machine: `checks/verify_F33_dynamic_phase.py` §C].

**Pf.**
$$
(1):\ \mathrm{CT0.9}:\ \sigma_e\in\{\pm1\}\implies-\sigma_e\in\{\pm1\}:\ C\ \text{closed on sign assignments};\qquad\mathrm{D3.4}:\ q\mapsto\tfrac12(-\sigma_s+\sigma_t)=-q;\qquad\mathrm{D3.3}:\ f_v\mapsto-f_v,\ \aleph_v=|f_v|\ \text{invariant}
$$
$$
\mathrm{D2.6}/\mathrm{EM.9a}(2):\ \omega\ \text{maps charge}\mapsto-\text{charge on the end and core reads}:\ C=\text{sign-level realization}
$$
$$
(2):\ \mathrm{EM.20}(1):\ \alpha_e\in\{0,\pi\}\implies\pi-\alpha_e\in\{0,\pi\}:\ P\ \text{closed on patterns};\qquad\mathrm{EM.23}(2):\ \text{the odd locus is}\ M(\mathcal P)=E_{\mathcal R}\setminus\mathcal P
$$
$$
(3):\ \mathrm{D2.7}:\ \Theta_{\mathfrak L}\ \text{reverses the ledger order},\ J^+\leftrightarrow J^-,\ G(e)\mapsto G(e)^\ast;\qquad\mathrm{CT2.8}(1):\ w(\Theta_{\mathfrak L}C)=w(C)^\ast;\qquad\Theta_{\mathfrak L}^2=\mathrm{id}\ [\text{double reversal}]
$$
$$
(4):\ (1),(2),(3)\ \text{map}\ \mathfrak C(\mathcal R)\to\mathfrak C(\mathcal R)\ [\mathrm{D0.10}];\qquad C^2:\ \sigma\mapsto-\sigma\mapsto\sigma;\quad P^2:\ \alpha\mapsto\pi-\alpha\mapsto\alpha;\quad T^2:\ \mathrm{id}\ [(3)]
$$
$$
(5):\ w(C)=\mathcal J(C)\prod_{e}\sigma_e\,e^{i\alpha_e\widehat{ds}^{\,2}(e)}\cdot(-1)^{\aleph(\sigma,C)}=:\mathcal J\,S\,\Gamma\,A\quad[\mathrm{A8},\ \mathrm{D3.5},\ \mathrm{D3.6}]
$$
$$
T:\ \Gamma\mapsto\bar\Gamma\ (\text{per-edge conjugation}),\ \ \mathcal J,S,A\in\mathbb R\ [\mathrm{D2.7},\ \mathrm{D3.6};\ \aleph\in\mathbb Z]\implies w(\Theta_{\mathfrak L}C)=w(C)^\ast
$$
$$
P\circ T:\ \alpha_e\mapsto-\alpha_e\mapsto\pi+\alpha_e\ (\mathrm{mod}\ 2\pi):\ \ e^{-i\alpha_e\widehat{ds}^{\,2}}\mapsto e^{i(\pi+\alpha_e)\widehat{ds}^{\,2}}=e^{i\pi\widehat{ds}^{\,2}}\,e^{i\alpha_e\widehat{ds}^{\,2}}\implies\bar\Gamma\mapsto e^{i\pi\Theta}\,\Gamma\implies w(PT\,C)=e^{i\pi\Theta}\,w(C)
$$
$$
C:\ S\mapsto(-1)^{|E|}S;\quad A\ \text{invariant}\ [\aleph_v=|-f_v|];\quad\mathcal J\ \text{invariant}\implies w(\mathrm{CPT}\,C)=(-1)^{|E|}\,e^{i\pi\Theta}\,w(C)
$$
$$
\Theta\in\mathbb R\ [\mathrm{D1.6}:\ ds^2\ \text{real}]\implies\bigl|(-1)^{|E|}e^{i\pi\Theta}\bigr|=1\implies|w(\mathrm{CPT}\,C)|^2=|w(C)|^2
$$
$$
\text{on-shell}:\ \widehat{ds}^{\,2}\in\mathbb Z\implies e^{i\alpha_e\widehat{ds}^{\,2}}=(\pm1)^{\widehat{ds}^{\,2}}\in\{\pm1\}\implies\Gamma\in\{\pm1\}\implies w\in\mathbb R:\ w^\ast=w;\qquad |E|+\Theta\equiv0\ (2)\implies(-1)^{|E|}e^{i\pi\Theta}=1
$$
$$
\implies w(\mathrm{CPT}\,C)=w(C)=w(C)^\ast .\ \blacksquare
$$

**Phys.** Charge conjugation, parity, and time reversal each exist as derived operations on the ledger's configuration space: sign flip on every edge, complement of the antialigned set, Janus reflection of the record. Their composition leaves every configuration probability $|w|^2$ invariant — the corpus's own CPT theorem — with the conjugate-weight identity exact on the on-shell even locus.


**Rmk (clause-(5) scope).** $|w|^2$-invariance is unconditional; $w(\mathrm{CPT}\,C)=w(C)^\ast$ holds on the stated on-shell even locus.
---

## §E.VII — Spectrum and Completion

### EM.22 — The electromagnetic spectrum

**Thm.**
$$
\begin{array}{c|c|c|c}
\text{object} & \text{type} & \text{mass/charge} & \text{data}\\ \hline
\text{photon} & \text{trivial chain}\subseteq V_2 & m^2=0;\ q_{\mathrm{EM}}=0 & N_{\mathrm{pol}}=2\\
\text{field excitation} & \text{transition vertex} & \aleph_v=1 & f_v=\pm1\\
\text{charged chain end} & \text{chain terminus} & q_{\mathrm{EM}}\in\{+1,-1\} & \text{binary sign}
\end{array}
$$
$$
\neg\exists\ \text{massive abelian gauge boson};\qquad\text{list exhaustive}:\ \dim(\text{abelian block})=1\ [EM.3].
$$

**Req.** D3.4, D3.7; EM.3, EM.5, EM.6, EM.8, EM.9, EM.10, EM.12; EW.22, EW.28 (Part 2).

**Pf.**
$$
\text{photon}: \mathrm{EM.5}\ (\text{trivial}\ V_2);\ \ \mathrm{EM.6}\ (m^2=0);\ \ \mathrm{EM.8}\ (2\ \text{pol})
$$
$$
q_\gamma=0:\ \ \text{trivial}\implies\neg\text{transitions}\ [EM.12]\implies\sigma_{\leftarrow}=\sigma_{\rightarrow}\ \forall v\implies\sigma_{s(c)}=\sigma_{t(c)}\implies q=0\ [\mathrm{D3.4}]
$$
$$
\text{excitations}: \mathrm{EM.12}\ (\aleph_v=1,\ f_v=\pm1);\qquad\text{ends}: \mathrm{EM.9},\ \mathrm{EM.10}
$$
$$
\neg\exists\ \text{massive abelian}: \ \mathrm{EW.22}:\ \ker M^2=\text{1-dim abelian direction}\ A;\quad\text{massive neutral}=Z\in\text{weak part}\ [EW.28]
$$
$$
\text{exhaustive}: 1\ \text{generator}\ [EM.3]\implies\{\text{transit mode}=\gamma,\ \text{curvature data}=\aleph_v,\ \text{sources}=\text{ends}\}. \blacksquare
$$

**Phys.** The complete electromagnetic bestiary: one massless neutral two-polarization transit mode, sign-field vertex excitations, and quantized chain-end charges. The photon’s own charge vanishes identically — a null chain carries no sign flips.

---

### EM.26 — Cross-checks

**Thm.** Four agreements between derivations with pairwise-disjoint inputs:
$$
(1)\ \{-1,0,+1\}:\ \ \mathrm{EM.9}\ [\Leftarrow\mathrm{CT0.9}]\ =\ \mathrm{EW.36}\ [\Leftarrow\mathrm{EW.32}];
$$
$$
(2)\ m_\gamma^2=0:\ \ \mathrm{EM.6(ii)}\ [\Leftarrow\mathrm{D1.7},\mathrm{EW.18}]\ =\ \mathrm{EW.22}\ [\Leftarrow\mathrm{EW.33}];
$$
$$
(3)\ \alpha_{\mathrm{EM}}^{(3)}=\alpha_{\mathrm{EM}}^{(2)}:\ \ \mathrm{EM.18}\ \text{step 2}\ [\Leftarrow\mathrm{CT0.14}]\ =\ \mathrm{EM.18}\ \text{step 3}\ [\Leftarrow\mathrm{CT3.7}];
$$
$$
(4)\ g^{\mu\nu}T_{\mu\nu}=0:\ \ \mathrm{EM.15}\ \text{(explicit variation)}\ =\ \mathrm{EM.6}\ \text{(massless transit}\implies\text{traceless stress)}.
$$

**Req.** CT0.9, CT0.14 (Part 1); CT3.7 (**F**, corroboration); EM.6, EM.9, EM.15, EM.18; EW.18, EW.22, EW.32, EW.33 (Part 2).

**Pf.**
$$
\text{input pairs}: (1)\ \mathrm{CT0.9}\ \text{vs}\ \mathrm{EW.32};\quad(2)\ \{\mathrm{D1.7},\mathrm{EW.18}\}\ \text{vs}\ \mathrm{EW.33};\quad(3)\ \mathrm{CT0.14}\ \text{vs}\ \mathrm{CT3.7};\quad(4)\ \text{variation vs pole location}
$$
$$
\text{shared intermediate results}=\varnothing\ \text{in each pair}\implies\text{agreements}=\text{genuine consistency tests};\qquad\forall4:\ \text{hold}\ [\text{cited tags}]. \blacksquare
$$

**Phys.** The sector cross-validates at four joints against the combinatorics of **B**, the resolvent apparatus of **C**, and the seed calculus of **D** — each check by two routes sharing no intermediate result.

---

### EM.25 — What the corpus does and does not fix about the abelian sector

**Thm.** Fixed with zero freedom:
$$
(1)\ q\in\{-1,0,+1\}\ [\mathrm{EM.9},\mathrm{EM.10},\mathrm{EW.36}];\quad
(2)\ m_\gamma^2=0\ [\mathrm{EM.6}];\quad
(3)\ N_{\mathrm{pol}}=2\ [\mathrm{EM.8}];
$$
$$
(4)\ \alpha_e\in\{0,\pi\}\ \text{per real edge}\ [\mathrm{EM.20}];\quad
(5)\ \alpha_{\mathrm{EM}}^{(n)}=\alpha_{\mathrm{EM}}^{(2)}\ \forall n\ \ (\text{block read runs at no accessible rung})\ [\mathrm{EM.18},\mathrm{EM.19}];\quad
(6)\ e=g\sin\theta_W=g'\cos\theta_W\ [\mathrm{EW.35}].
$$
$\neg$Fixed:
$$
(7)\ \text{the numerical value of}\ e:\quad
\neg\exists\ \text{theorem asserting a value of}\ e;\qquad
e=e(g,g'),\ (g,g')\ \text{free}\ [\mathrm{P4}]\implies\text{family of valid configurations with distinct}\ e,\ \text{all satisfying}\ (1)\text{--}(6);
$$
$$
\text{determining}\ e\ \text{requires one further datum}\ (\theta_W\ \text{or}\ g)=\text{calibration step}\ [\mathrm{P5}];\ \text{then}\ (6)\implies\text{rest}=\text{predictions};
$$
$$
(8)\ \text{the per-edge values}\ \alpha_e:\ \text{registration outcomes governed by}\ \mathrm{A4}/\mathrm{A5}/\mathrm{A6}\ [\mathrm{EM.20}(2),(5)],\ \neg\text{parameters};\qquad
\alpha_{\mathrm{EM}}^{(2)}\ \text{as a number}:\ \text{operator read}\ [\mathrm{EM.17}],\ \neg\exists\ \text{theorem fixing its value}.
$$
Separation and closure:
$$
(9)\ \neg\bigl(\alpha\text{-data determines}\ e\bigr);\qquad\neg\bigl(e\ \text{determines}\ \alpha\text{-data}\bigr);\qquad\neg\exists\ \text{corpus equation relating them}\ [g,g'\ \text{appear nowhere in EM.16--EM.21}];
$$
$$
(10)\ \forall\ \text{statements of}\ \mathbf E:\quad\vdash\ \mathrm{A1\text{–}A9}\cup\mathrm{C1\text{–}C12}\cup\mathrm{D0.1\text{–}D4.3}\cup\{\mathbf B,\mathbf C,\mathbf D\ \text{theorems}\};\qquad
\neg\exists\ \text{external EM law, parameter, or measured value}.
$$

**Req.** P4, P5; EM.6, EM.8, EM.9, EM.10, EM.16, EM.17, EM.18, EM.19, EM.20, EM.21, EM.23, EM.24; EW.24, EW.35, EW.36 (Part 2); citation closure [machine: `checks/verify_corpus_graph.py`].

**Pf.**
$$
(1)\text{--}(6):\ \text{cited proofs use only A}\cup\text{derived results};\ \neg\exists\ \text{parameter introduced};\qquad(4):\ \mathrm{EM.20}(1);\qquad(5):\ \mathrm{EM.18},\ \mathrm{EM.19}
$$
$$
(7):\ \mathrm{P4}:\ (g,g')\in(\mathbb R_{>0})^2\ \text{unconstrained}\implies\forall(g,g'):\ \text{configuration with}\ e=gg'/\sqrt{g^2+g'^2}\ \text{satisfying}\ (1)\text{--}(6);\qquad\tan\theta_W=g'/g\ [\mathrm{EW.24}]
$$
$$
\implies\neg\exists\ \text{function of the axioms alone}\mapsto\text{unique}\ e;\qquad\mathrm{P5}:\ \text{one datum}\ +(6)\implies\text{predictions}
$$
$$
(8):\ \mathrm{EM.20}(2),(5):\ \alpha_e=\text{A4 branch index at the seal}\ [\mathrm{Def\text{-}EM.20}];\qquad\mathrm{EM.17}:\ \alpha_{\mathrm{EM}}^{(n)}=\text{eigenvalue of}\ \mathbf F_M^{(n)}\big|_{\mathcal K^{(\mathrm{EM})}}:\ \text{operator datum},\ \neg\text{a fixed pure number}
$$
$$
(9):\ \mathrm{EM.16}\text{--}\mathrm{EM.21}\ \text{derivations contain}\ \neg\{g,g'\};\qquad\mathrm{EW.35}:\ e=gg'/\sqrt{g^2+g'^2};\qquad(g,g')\mapsto(g_2,g_2'):\ e\mapsto e_2\ne e\ \wedge\ \alpha\text{-data unchanged}\implies\text{independent variation}
$$
$$
(10):\ \text{dependency trace}:\ \text{activation}\Leftarrow\mathrm{CT0.13}+\mathrm{D3.3}\ [\mathrm{EM.1}\text{--}\mathrm{EM.4}];\quad\gamma:\ \text{trivial}\ V_2\ \text{chain},\ m=0,\ 2\ \text{pol},\ \mathsf E_{\mathrm{tr}}\ \text{only}\ [\mathrm{EM.5}\text{--}\mathrm{EM.8}]
$$
$$
\text{charge}:\ \text{end-difference},\ \mathbb Z\text{-quantized by the binary phase},\ Q_{\mathrm{EM}}=0\ \text{by seal pairing}\ [\mathrm{EM.9}\text{--}\mathrm{EM.11}];\qquad f_v;\ \text{sign structures independent};\ \text{gauge}=\text{offset redundancy}\ [\mathrm{EM.12}\text{--}\mathrm{EM.14}]
$$
$$
T_{\mu\nu}=F\text{-bilinear},\ \text{trace}\ 0\ [\mathrm{EM.15}];\qquad\alpha_e:\ \text{per-edge registration read},\ \text{alphabet}\ \{0,\pi\},\ \mathfrak q^0\ [\mathrm{EM.16}\text{--}\mathrm{EM.21}]
$$
$$
\text{parity}:\ \text{pattern data},\ 2^{|E_{\mathcal R}|}\ \text{classes}\ [\mathrm{EM.23}];\qquad\mathrm{CPT}:\ \text{derived components},\ |w|^2\text{-invariance}\ [\mathrm{EM.24}];\qquad\text{spectrum exhaustive}\ [\mathrm{EM.22}];\quad4\ \text{cross-checks}\ [\mathrm{EM.26}].\ \blacksquare
$$

**Phys.** The corpus states exactly which abelian quantities are derived — alphabet, masslessness, polarizations, the per-edge phase alphabet, block-read stability, and the identity $e=g\sin\theta_W$ — and exactly which data stay open: the numerical coupling (configuration data), the per-edge phase values (registration outcomes), and the block-scale number (operator read). It makes no claim to derive a fine-structure constant, and no equation ties phase data to the coupling: an honesty clause that is itself a theorem about the axiom system. Closure audit: every electromagnetic statement traces to A1–A9.

---

## Closure exports of Part 2 §E (consumed by Part 2 §F–§G, Parts 3–4)

$$
\begin{array}{lll}
\mathrm{EM.2}\ Y_{\mathrm{asp}}=\mathcal P^{(\mathrm{EM})},\ \mathfrak T=1;\ Y_{\mathrm{car}}=\tfrac12\sigma_0 &
\mathrm{EM.5}\ \gamma_\gamma,\ \gamma_g\in\mathsf{Trivial}\ (V_2/V_3) &
\mathrm{EM.6}\ m_\gamma^2=0\ (\times2\ \text{routes})\\
\mathrm{EM.8}\ N_{\mathrm{pol}}=2 &
\mathrm{EM.9/10}\ q_{\mathrm{EM}}\in\{-1,0,+1\}\subset\mathbb Z;\ \mathrm{EM.9b}:\ \textstyle\sum_if_{v_i}=\tfrac12(\sigma_{e_k}-\sigma_{e_1}) &
\mathrm{EM.11}\ Q_{\mathrm{EM}}=0\\
\mathrm{EM.12/13}\ f_v;\ (-1)^\aleph\ \text{dynamics} &
\mathrm{EM.14}\ A_\mu\sim A_\mu+\nabla_\mu\chi &
\mathrm{EM.15}\ T^{(\mathrm{EM})}_{\mu\nu};\ \text{traceless}\\
\mathrm{EM.16}\ G(e)=\sigma_e e^{i\alpha_e\widehat{ds}^{\,2}} &
\mathrm{EM.17}\ \alpha_{\mathrm{EM}}^{(n)}=\mathfrak T(Y_{\mathrm{asp}}\mathbf F_MY_{\mathrm{asp}}) &
\mathrm{EM.18/19}\ \alpha_{\mathrm{EM}}^{(n)}=\alpha_{\mathrm{EM}}^{(2)}\ \forall n\\
\mathrm{Def\text{-}EM.20}/\mathrm{EM.20}\ \alpha_e=\alpha_{pq}\in\{0,\pi\}:\ \text{A4 branch, per edge} &
\mathrm{EM.21}\ [\alpha_e]=\mathfrak q^0 &
\mathrm{Def\text{-}EM.21/22}\ \mathcal P(\Sigma);\ M(\mathcal P)\\
\mathrm{EM.23}\ \text{parity classes};\ 2^{|E_{\mathcal R}|}\ \text{patterns} &
\mathrm{EM.24}\ \mathrm{CPT}=C\circ P\circ T;\ |w(\mathrm{CPT}\,C)|^2=|w(C)|^2 &
\mathrm{EM.22}\ \text{spectrum}\ \{\gamma,\ \aleph_v,\ \text{ends}\}\\
\mathrm{EM.25}\ e=\text{P4 data};\ \text{self-containment} &
\mathrm{EM.26}\ 4\ \text{cross-checks} &
\end{array}
$$

$\blacksquare$

---

## §F — Colour Sector

*Dep.: Part 1; Part 2 §C. This section may be read before §D, §E: its two borrowed results — colour masslessness (EW.26) and coefficient stability (EM.18) — are restated with full arguments at use. Notation: $\mathcal H^{(n)}_{\mathrm{slot}}$ [D3.1] $\ne\mathfrak H(\mathbb C^4)$ [A1] — slot space and pair operator space are never identified; $T_a$, $f_{abc}$: colour generators and structure constants in the Hermitian convention [C2]. Machine: `checks/verify_F.py` — exact arithmetic in $\mathbb Q(\sqrt3,i)$; CT3.22a/CT3.17a: `checks/verify_merge_tierA.py`; CT3.10a: `checks/verify_promotion_F_colour.py`.*

## §F.I — Slot Structure

### CT3.20 — The number of colours is forced

**Thm.**
$$
\text{admissible}(v)\iff n(v)\le3;\qquad
\max_{\text{admissible}}\mathcal H^{(n)}_{\mathrm{slot}}=\mathcal H^{(3)}_{\mathrm{slot}}\cong\mathbb C^3;
$$
$$
N_{\text{colour}}=3=\log_2C_{\mathrm{cap}}-1=\log_216-1\qquad(\text{derived from A2}+\mathrm{CT0.9};\ \neg\text{chosen}).
$$

**Req.** A2; D3.1; CT0.5, CT0.6, CT0.9, CT0.11 (Part 1).

**Pf.**
$$
\mathrm{D3.1}:\ \text{rung-}n\ \text{vertex carries}\ n\ \text{slots}
$$
$$
\mathrm{CT0.5}/\mathrm{CT0.6}:\ D_{\mathrm{tick}}(n)=2^{n+1},\ C_{\mathrm{cap}}=16;\qquad
\mathrm{CT0.11}:\ \text{admissible}\iff2^{n+1}\le16\iff n\le3
$$
$$
\implies\mathcal H^{(n)}_{\mathrm{slot}}\in\{\mathbb C^0,\mathbb C^1,\mathbb C^2,\mathbb C^3\};\qquad\max=\mathbb C^3
$$
$$
n\le\log_2C_{\mathrm{cap}}-1=3:\quad\text{inputs}=\mathrm{A2}\ (1\mathfrak q\ \text{per channel})\ +\ \mathrm{CT0.9}\ (\Phi=\{0,\pi\});\quad\neg\exists\ \text{further input}.\ \blacksquare
$$

**Phys.** Three is not a choice: a rung-$n$ vertex loads $2^{n+1}$ registers against a capacity of $16$, so three slots are the most any admissible vertex can carry. The number of colours is fixed by the channel quantum and the binary phase alphabet, and by nothing else.

---

### CT3.1 — Classical trivalent symmetry

**Thm.** Trivalent vertex with distinguishable slots $\{s_1,s_2,s_3\}$:
$$
\text{relabeling symmetry}=\operatorname{Sym}\{s_1,s_2,s_3\}=S_3;\qquad
|S_3|=3!=6;\qquad
S_3=\{e,(12),(13),(23),(123),(132)\}.
$$

**Req.** D3.1; bijection/group facts [math].

**Pf.**
$$
\mathrm{D3.1}:\ \text{rung-3 vertex}:\ \text{slots}=\{s_1,s_2,s_3\}
$$
$$
\text{relabeling}=\text{invertible},\ \text{slot-preserving map}=\text{bijection}\ \{s_1,s_2,s_3\}\to\{s_1,s_2,s_3\}
$$
$$
\text{bijections under composition}=S_3;\qquad|S_3|=3!=6.\ \blacksquare
$$

**Phys.** The classical symmetry of a trivalent vertex is the full permutation group of its three slots — six relabelings, no more.

---

### CT3.2 — Quantum slot space

**Thm.**
$$
|\psi\rangle=\alpha_1|1\rangle+\alpha_2|2\rangle+\alpha_3|3\rangle,\ \ \alpha_i\in\mathbb C;\qquad
\langle\psi|\phi\rangle=\textstyle\sum_i\alpha_i^\ast\beta_i;\qquad
\textstyle\sum_i|\alpha_i|^2=1;
$$
$$
\mathcal H^{(3)}_{\mathrm{slot}}=\operatorname{span}_{\mathbb C}\{|1\rangle,|2\rangle,|3\rangle\}\cong\mathbb C^3 .
$$

**Req.** A1; D3.1.

**Pf.**
$$
\mathrm{A1}:\ \text{carrier spaces}=\text{complex Hilbert spaces}\implies\text{slot excitations admit complex superpositions}
$$
$$
\text{span of 3 independent basis states over}\ \mathbb C=\mathbb C^3\quad[\mathrm{D3.1}].\ \blacksquare
$$

**Phys.** Superposition promotes the discrete slot label to a complex three-dimensional carrier: colour becomes a quantum number with amplitudes.

---

### CT3.3 — Classical permutations embed unitarily

**Thm.** $P_\pi|i\rangle:=|\pi(i)\rangle$, $\ (P_\pi)^i{}_j=\delta^i_{\pi(j)}$. Then
$$
P_\pi^\dagger P_\pi=I_3\implies P_\pi\in U(3);\qquad
P_\pi P_\rho=P_{\pi\circ\rho}\ \ (\text{homomorphism});\qquad
P_\pi=I_3\iff\pi=e\ \ (\text{faithful});\qquad
S_3\hookrightarrow U(3).
$$

**Req.** CT3.1, CT3.2; unitarity criterion [math].

**Pf.**
$$
P_\pi:\ \text{ON basis}\mapsto\text{ON basis}\implies\langle P_\pi\psi,P_\pi\phi\rangle=\langle\psi,\phi\rangle\implies P_\pi^\dagger P_\pi=I_3\implies P_\pi\in U(3)
$$
$$
P_\pi P_\rho|i\rangle=P_\pi|\rho(i)\rangle=|\pi(\rho(i))\rangle=P_{\pi\circ\rho}|i\rangle\implies\text{homomorphism}
$$
$$
P_\pi=I_3\implies\forall i:\ \pi(i)=i\implies\pi=e\implies\text{injective}.\ \blacksquare
$$

**Phys.** The classical relabeling symmetry sits inside the quantum one as the six permutation matrices — a faithful discrete subgroup of $U(3)$.

---

### CT3.4 — Probability preservation gives $U(3)$

**Thm.**
$$
\bigl\{L\ \text{linear}:\ \langle L\psi,L\phi\rangle=\langle\psi,\phi\rangle\ \ \forall\psi,\phi\bigr\}
=\bigl\{L:\ L^\dagger L=I_3\bigr\}=U(3);\qquad
S_3\subseteq U(3)\ [\mathrm{CT3.3}].
$$

**Req.** CT3.2, CT3.3; polarization/inner-product matrix form [math].

**Pf.**
$$
\text{probabilities}=\text{moduli of inner products}\implies\text{preservation}\iff\langle L\psi,L\phi\rangle=\langle\psi,\phi\rangle\ \forall\psi,\phi\quad[\text{polarization}]
$$
$$
\psi^\dagger L^\dagger L\phi=\psi^\dagger\phi\ \ \forall\psi,\phi\iff L^\dagger L=I_3\quad[\psi,\phi\ \text{over a basis}]
$$
$$
\{L:\ L^\dagger L=I_3\}=:U(3)\ \ \text{(group)};\qquad S_3\hookrightarrow U(3)\ [\mathrm{CT3.3}].\ \blacksquare
$$

**Phys.** The full quantum symmetry of the slot carrier is exactly $U(3)$: the linear maps preserving every probability. The classical $S_3$ is its discrete relic.

---

### CT3.5 — The algebra $\mathfrak u(3)$ and its decomposition

**Thm.** [C2]
$$
\mathfrak u(3)=\{X\in M_3(\mathbb C):\ X^\dagger=X\};\qquad
\mathfrak u(3)=\mathfrak{su}(3)\oplus\mathfrak u(1);
$$
$$
\mathfrak{su}(3)=\{X\in\mathfrak u(3):\ \mathfrak T(X)=0\};\qquad
\mathfrak u(1)=\operatorname{span}_{\mathbb R}\{I_3\};\qquad
[\mathfrak{su}(3),\mathfrak u(1)]=0\ \ (\text{commuting ideals});
$$
$$
\forall X\ \exists!\ (X_0,c):\ X=X_0+cI_3,\ \ \mathfrak T(X_0)=0,\ \ c=\tfrac{\mathfrak T(X)}{3}.
$$

**Req.** C2; CT3.4; trace cyclicity [linear algebra].

**Pf.**
$$
X^\dagger=X\wedge Y^\dagger=Y\implies[X,Y]^\dagger=Y^\dagger X^\dagger-X^\dagger Y^\dagger=-[X,Y]\implies-i[X,Y]\ \text{Hermitian}:\ \text{closure}\ [\mathrm{C2}]
$$
$$
\mathfrak T[X,Y]=\mathfrak T(XY)-\mathfrak T(YX)=0\implies\text{traceless Hermitian}=\text{subalgebra}
$$
$$
X_0:=X-\tfrac{\mathfrak T(X)}{3}I_3:\quad\mathfrak T(X_0)=\mathfrak T(X)-\tfrac{\mathfrak T(X)}{3}\cdot3=0\implies X_0\in\mathfrak{su}(3)
$$
$$
\text{uniqueness}:\ \ X=S+cI_3,\ \mathfrak T(S)=0\implies\mathfrak T(X)=3c\implies c=\tfrac{\mathfrak T(X)}3
$$
$$
I_3\in Z\implies[\mathfrak u(1),\mathfrak u(3)]=0\implies\text{both summands ideals};\qquad
cI_3\ \text{traceless}\iff c=0\implies\mathfrak{su}(3)\cap\mathfrak u(1)=\{0\}.\ \blacksquare
$$

**Phys.** The slot symmetry algebra splits canonically into traceless plus centre — the template from which colour and electromagnetism are cut by the subset principle.

---

## §F.II — The Rung-3 Gauge Algebra

### CT3.6 — Rung-3 active set

**Thm.** $\ \mathcal A(3)=\mathcal A(2)\cup\{\mathrm{strong}\};\qquad\mathbf F_M^{(3)}=\mathcal P_M^{(3)}\mathbf F\,\mathcal P_M^{(3)}=\mathbf F\big|_{\mathcal K_3}.$

**Req.** CT0.13 (Part 1); CT2.2, CT2.3, CT2.4 (Part 2).

**Pf.** Active set: [CT0.13 step $n{=}3$]; projector: [CT2.2]; restriction: [CT2.3, CT2.4]. $\blacksquare$

**Phys.** At rung 3 the mask admits one new block — colour — on top of the rung-2 content.

---

### CT3.7 — The strictly new rung-3 algebra is $\mathfrak{su}(3)$

**Thm.** Strictly new gauge structure at rung 3 [D3.2]:
$$
\mathfrak u(3)\big/\mathfrak u(1)\cong\mathfrak{su}(3);\qquad
\pi:\mathfrak u(3)\to\mathfrak{su}(3),\ \ \pi(X)=X-\tfrac{\mathfrak T(X)}{3}I_3:\ \ \text{Lie homomorphism},\ \ \ker\pi=\operatorname{span}_{\mathbb R}\{I_3\},\ \ \text{surjective};
$$
$$
\mathfrak T(T_a)=0\quad\forall a\ \ (\neg\exists\ \text{central component}).
$$

**Req.** D3.2, D2.12; CT0.13 (Part 1); CT3.4, CT3.5; EM.2, EW.8 (**D**/**E**, restated: centre spent at rung 2).

**Pf.**
$$
\mathrm{CT3.4}:\ \text{rung-3 slot symmetry}=U(3)\implies\text{algebra}=\mathfrak u(3);\qquad
\mathrm{CT3.5}:\ \mathfrak u(3)=\mathfrak{su}(3)\oplus\mathfrak u(1)_{\langle I_3\rangle}
$$
$$
\iota_2\bigl(Z(\mathfrak u(2))\bigr)=F_{\mathrm{EM}}\ \text{realized at rung}\ 2\ [\mathrm{D2.12},\ \mathrm{CT0.13},\ \mathrm{EM.2}\ \text{restated}:\ Y_{\mathrm{asp}}=\mathcal P^{(\mathrm{EM})}]
$$
$$
\mathrm{D3.2}\ [\mathrm{D2.12}:\ \text{“realized”}=\text{abstract class in}\ \iota_m(\mathfrak u(m)),\ m<n]:\quad\iota_3\bigl(Z(\mathfrak u(3))\bigr)\cong\mathfrak u(1)\cong\iota_2\bigl(Z(\mathfrak u(2))\bigr)\implies\neg\text{strictly new}
$$
$$
\implies\text{strictly new}=\mathfrak u(3)/\mathfrak u(1)
$$
$$
\pi\ \text{well-defined Lie homomorphism}\ (I_3\ \text{central});\quad
\ker\pi=\{X:\ X=\tfrac{\mathfrak T X}3I_3\}=\operatorname{span}_{\mathbb R}\{I_3\};\quad\text{surjective}\ [\mathrm{CT3.5}\ \text{split}]
$$
$$
\mathfrak{su}(3)=\{\mathfrak T=0\}\implies\mathfrak T(T_a)=0\ \ \forall a.\ \blacksquare
$$

**Phys.** The new force at rung 3 is exactly the traceless slot algebra $\mathfrak su(3)$: eight generators, no central component — the ninth direction of $\mathfrak u(3)$ was already spent on electromagnetism at rung 2 by the subset principle.

---

### CT3.8 — Dimension of the colour algebra

**Thm.** $\ \dim_{\mathbb R}\mathfrak u(3)=3+3\cdot2=9;\qquad\mathfrak T(X)=0:\ 1\ \text{nontrivial real constraint}\ (\mathfrak T(I_3)=3\ne0);\qquad\dim_{\mathbb R}\mathfrak{su}(3)=9-1=8=3^2-1.$

**Req.** CT3.5; Hermitian-matrix parameter count [linear algebra].

**Pf.**
$$
X^\dagger=X:\ 3\ \text{real diagonal}\ +\ 3\ \text{complex off-diagonal}\ (2\ \text{real each})\implies\dim_{\mathbb R}\mathfrak u(3)=9
$$
$$
\mathfrak T:\ \mathfrak u(3)\to\mathbb R\ \text{linear},\ \mathfrak T(I_3)=3\ne0\implies\text{surjective}\implies\dim\ker=9-1=8.\ \blacksquare
$$

**Phys.** The colour algebra is eight-dimensional — the gluon count of CT3.13 and the colour-block dimension of CT0.14 ($\dim\mathcal K_3=25=17+8$).

---

### CT3.9 — Explicit generator basis

**Thm.** With the Gell-Mann matrices
$$
\lambda_1=\begin{pmatrix}0&1&0\\1&0&0\\0&0&0\end{pmatrix},\
\lambda_2=\begin{pmatrix}0&-i&0\\i&0&0\\0&0&0\end{pmatrix},\
\lambda_3=\begin{pmatrix}1&0&0\\0&-1&0\\0&0&0\end{pmatrix},\
\lambda_4=\begin{pmatrix}0&0&1\\0&0&0\\1&0&0\end{pmatrix},
$$
$$
\lambda_5=\begin{pmatrix}0&0&-i\\0&0&0\\i&0&0\end{pmatrix},\
\lambda_6=\begin{pmatrix}0&0&0\\0&0&1\\0&1&0\end{pmatrix},\
\lambda_7=\begin{pmatrix}0&0&0\\0&0&-i\\0&i&0\end{pmatrix},\
\lambda_8=\frac1{\sqrt3}\begin{pmatrix}1&0&0\\0&1&0\\0&0&-2\end{pmatrix},
$$
and $T_a:=\tfrac12\lambda_a$:
$$
T_a^\dagger=T_a;\qquad\mathfrak T(T_a)=0;\qquad
\{T_a\}_{a=1}^{8}:\ \mathbb R\text{-basis of}\ \mathfrak{su}(3);\qquad
[T_a,T_b]=i\,f_{abc}\,T_c,\ \ f_{abc}\in\mathbb R;\qquad
\mathfrak T(T_aT_b)=\tfrac12\,\delta_{ab}.
$$

**Req.** C2; CT3.5, CT3.8; direct computation [machine: `checks/verify_F.py`, exact in $\mathbb Q(\sqrt3,i)$].

**Pf.**
$$
\lambda_a^\dagger=\lambda_a\ \ \forall a\ [\text{inspection}];\qquad
\mathfrak T\lambda_a=0:\ a\le7\ \text{visually};\quad\mathfrak T\lambda_8=\tfrac1{\sqrt3}(1+1-2)=0
$$
$$
\text{supports}:\ \lambda_{1,2}\leftrightarrow(1,2)\text{-entry}\ \{\mathrm{Re},\mathrm{Im}\};\ \ \lambda_{4,5}\leftrightarrow(1,3);\ \ \lambda_{6,7}\leftrightarrow(2,3);\ \ \lambda_{3},\lambda_{8}\leftrightarrow\text{traceless diagonal}\ (\neg\text{proportional})
$$
$$
\implies8\ \text{independent};\qquad\dim\mathfrak{su}(3)=8\ [\mathrm{CT3.8}]\implies\text{basis}
$$
$$
\mathrm{CT3.5}:\ -i[T_a,T_b]\ \text{Hermitian}\wedge\text{traceless}\implies\in\mathfrak{su}(3)=\operatorname{span}_{\mathbb R}\{T_c\}\implies[T_a,T_b]=if_{abc}T_c,\ \ f_{abc}\in\mathbb R
$$
$$
\mathfrak T(\lambda_a\lambda_b)=2\delta_{ab}\ [\text{direct computation, machine-verified}]\implies\mathfrak T(T_aT_b)=\tfrac14\cdot2\delta_{ab}=\tfrac12\delta_{ab}\quad[=\text{uniform normalization of EW.32}].\ \blacksquare
$$

**Phys.** The explicit normalized colour octet: same uniform trace normalization $\mathfrak T(\mathcal G_A\mathcal G_B)=\tfrac12\delta_{AB}$ as the electroweak generators — one gauge convention across the corpus.

---

### CT3.21 — Structure constants

**Thm.** $\ f_{abc}:=-2i\,\mathfrak T\bigl([T_a,T_b]T_c\bigr)$ is totally antisymmetric, with independent nonzero values
$$
f_{123}=1;\qquad
f_{147}=f_{246}=f_{257}=f_{345}=\tfrac12;\qquad
f_{156}=f_{367}=-\tfrac12;\qquad
f_{458}=f_{678}=\frac{\sqrt3}{2};
$$
$\forall$ other independent components $=0$.

**Req.** CT3.9; trace cyclicity [linear algebra]; machine: `checks/verify_F.py` (all 512 components + antisymmetry + all 512 Jacobi triples, exact).

**Pf.**
$$
[T_a,T_b]=if_{abd}T_d;\quad\mathfrak T(T_dT_c)=\tfrac12\delta_{dc}\ [\mathrm{CT3.9}]\implies\mathfrak T\bigl([T_a,T_b]T_c\bigr)=\tfrac i2f_{abc}\implies f_{abc}=-2i\,\mathfrak T\bigl([T_a,T_b]T_c\bigr)
$$
$$
a\leftrightarrow b:\ \text{antisymmetry of}\ [\cdot,\cdot];\qquad
\mathfrak T\bigl([T_a,T_b]T_c\bigr)=\mathfrak T(T_aT_bT_c)-\mathfrak T(T_bT_aT_c)=\mathfrak T\bigl(T_a[T_b,T_c]\bigr)\implies\text{antisymmetry in}\ b\leftrightarrow c
$$
$$
\implies f\ \text{totally antisymmetric}
$$
$$
\text{sample }1:\ \ [\lambda_1,\lambda_2]=2i\lambda_3\implies[T_1,T_2]=\tfrac14\cdot2i\lambda_3=iT_3\implies f_{123}=1
$$
$$
\text{sample }2:\ \ [\lambda_4,\lambda_5]=2i\,\operatorname{diag}(1,0,-1)=i\bigl(\lambda_3+\sqrt3\,\lambda_8\bigr)\implies[T_4,T_5]=\tfrac i2\bigl(T_3+\sqrt3\,T_8\bigr)\implies f_{453}=\tfrac12,\ f_{458}=\tfrac{\sqrt3}2
$$
$$
\forall\ (a,b,c):\ \text{complete exact list machine-verified}\ [\text{verify\_F}];\qquad
\text{Jacobi}:\ \sum_{\mathrm{cyclic}}\bigl[[T_a,T_b],T_c\bigr]=0\ \ \forall(a,b,c)\ [\text{machine, exact}].\ \blacksquare
$$

**Phys.** The colour algebra is fully determined — basis, brackets, normalization, structure constants down to the $\sqrt3/2$ fingerprints of $\lambda_8$. Zero continuous freedom: the strongest rigidity result of the corpus.

---

### CT3.10 — The colour aspect has no central component

**Thm.**
$$
F_{\mathrm{strong}}=\textstyle\sum_af_aT_a\implies\mathfrak T(F_{\mathrm{strong}})=0;\qquad
Y_{\mathrm{asp}}F_{\mathrm{strong}}Y_{\mathrm{asp}}=0;\qquad
\alpha_{\mathrm{EM}}^{(3)}=\alpha_{\mathrm{EM}}^{(2)}\quad[=\mathrm{EM.18},\ \text{restated}].
$$

**Req.** CT0.14 (Part 1); CT3.7; EM.2, EM.17 (**E**, restated at use).

**Pf.**
$$
\mathrm{CT3.7}:\ F_{\mathrm{strong}}=\textstyle\sum_{a=1}^{8}f_aT_a,\ f_a\in\mathbb R;\qquad
\mathfrak T(T_a)=0\ \forall a\implies\mathfrak T(F_{\mathrm{strong}})=\textstyle\sum_af_a\cdot0=0
$$
$$
\mathrm{CT0.14}:\ \mathcal K^{(\mathrm{strong})}\perp\mathcal K^{(\mathrm{EM})};\qquad
\mathrm{EM.2}\ \text{(restated)}:\ Y_{\mathrm{asp}}=\mathcal P^{(\mathrm{EM})}\implies Y_{\mathrm{asp}}F_{\mathrm{strong}}Y_{\mathrm{asp}}=\mathcal P^{(\mathrm{EM})}F_{\mathrm{strong}}\mathcal P^{(\mathrm{EM})}=0
$$
$$
\mathrm{EM.17}\ \text{(restated)}:\ \alpha_{\mathrm{EM}}^{(n)}=\mathfrak T\bigl(Y_{\mathrm{asp}}\mathbf F_M^{(n)}Y_{\mathrm{asp}}\bigr)/\mathfrak T\bigl(Y_{\mathrm{asp}}\bigr);\quad
\text{colour contributes}\ 0\implies\alpha_{\mathrm{EM}}^{(3)}=\alpha_{\mathrm{EM}}^{(2)}.\ \blacksquare
$$

**Phys.** Colour adds only traceless structure orthogonal to the rung-2 subspace: it neither carries a central charge nor disturbs the electromagnetic block read $\alpha_{\mathrm{EM}}$.


**Cor CT3.10a (no per-edge abelian strong phase).** $(1)$ **Coefficient-read obstruction.** EM.17's read $\alpha^{(n)}=\mathfrak T\bigl(Y_{\mathrm{asp}}\mathbf F_M^{(n)}Y_{\mathrm{asp}}\bigr)/\mathfrak T\bigl(Y_{\mathrm{asp}}\bigr)$ yields a single number exactly because the EM block is one-dimensional [CT0.14: $\dim\mathcal K^{(\mathrm{EM})}=1$; EM.17]. The strong block is eight-dimensional [CT0.14, CT3.8: $\dim\mathcal K_3=25=17+8$], and
$$
F_{\mathrm{strong}}=\textstyle\sum_af_aT_a=c\,I_3\quad\iff\quad c=0\ \wedge\ f_a=0\ \ \forall a
$$
[CT3.7: $\mathfrak T(T_a)=0\implies3c=\mathfrak T(F_{\mathrm{strong}})=0$; CT3.9: the $T_a$ are linearly independent] — the read returns no scalar on the strong block: $\neg\exists$ a per-edge abelian strong phase coefficient $\alpha_{\mathrm{strong}}$ defined by derived structure.
$(2)$ **Non-canonicity.** $\mathfrak{su}(3)$ contains $\mathfrak u(1)$ subalgebras [$\operatorname{span}_{\mathbb R}\{T_a\}$, CT3.9], but no generator line is fixed by the adjoint action — all maximal tori are conjugate [math] — so no $\mathfrak u(1)$ choice is distinguished by derived structure. Explicit witnesses (integer-entry $SU(3)$ elements of the CT3.9 basis [CT3.4; $\lambda_a=2T_a$; unitary, $\det=1$ — machine]):
$$
U_2=i\lambda_2+I_3-\lambda_2^{2},\qquad U_5=i\lambda_5+I_3-\lambda_5^{2}\qquad[\lambda_2^{2}=\operatorname{diag}(1,1,0),\ \ \lambda_5^{2}=\operatorname{diag}(1,0,1)]
$$
$$
\operatorname{Ad}_{U_5}(T_1)=U_5\,T_1\,U_5^{\dagger}=-\,T_6\ \notin\ \operatorname{span}_{\mathbb R}\{T_1\};\qquad
\forall a\in\{1,\dots,8\}\ \exists U\in\{U_2,U_5\}:\ \operatorname{Ad}_U(T_a)\notin\operatorname{span}_{\mathbb R}\{T_a\}\qquad[\text{machine census}].
$$
$(3)$ **Consequence (pointer).** With $\alpha_{\mathrm{EM}}^{(3)}=\alpha_{\mathrm{EM}}^{(2)}$ [CT3.10; EM.18 restated], the per-edge scalar factor $e^{i\alpha_e\widehat{ds}^{\,2}(e)}$ of the transfer weight is entirely electromagnetic [D3.5: $\alpha_e\in\Phi$, the same alphabet at every rung], and CT3.22a(0)'s decomposition — EM factor $\times$ $\{0,1\}$ singlet-sealing admissibility [D2.14; CT3.17, CT3.18 — forward in-document pointers, non-load-bearing] — exhausts the per-edge strong datum: no phase factor remains.

**Req (Cor).** D2.14, D3.5; CT0.14 (Part 1); CT3.4, CT3.7, CT3.8, CT3.9, CT3.10; EM.17, EM.18 (**E**, restated at use); torus conjugacy, linear independence [math; machine: `checks/verify_promotion_F_colour.py`].

**Pf (Cor).**
$$
(1):\ \mathfrak T(cI_3)=3c;\quad\mathfrak T(F_{\mathrm{strong}})=\textstyle\sum_af_a\,\mathfrak T(T_a)=0\ [\mathrm{CT3.7}]\implies c=0;\qquad\textstyle\sum_af_aT_a=0\implies f=0\ [\mathrm{CT3.9}:\ \text{basis}]
$$
$$
\dim\mathcal K^{(\mathrm{EM})}=1\ \ \text{vs}\ \ \dim\mathcal K^{(\mathrm{strong})}=8\ [\mathrm{CT0.14},\ \mathrm{CT3.8}]:\ \mathrm{EM.17}\text{'s single-coefficient read (single eigenvalue on a 1-dim block)}\ \neg\text{replicable on the strong block}
$$
$$
(2):\ \lambda_2^{2}=\operatorname{diag}(1,1,0),\ \lambda_5^{2}=\operatorname{diag}(1,0,1)\implies U_2,U_5\ \text{real orthogonal},\ \det=1\ [\text{machine}];\qquad U_5\,T_1\,U_5^{\dagger}=-T_6;\quad U_5\,T_2\,U_5^{\dagger}=T_7\ \ \text{etc.}\ [\text{machine census}]
$$
$$
\text{maximal tori conjugate}\ [\text{math}]\implies\neg\exists\ \text{distinguished}\ \mathfrak u(1)\subseteq\mathfrak{su}(3);\qquad
(3):\ \mathrm{CT3.10}:\ \alpha^{(3)}=\alpha^{(2)};\quad\mathrm{D3.5}:\ G^{(n)}(e)=\sigma_e\,e^{i\alpha^{(n)}_{\mathrm{EM}}\widehat{ds}^{\,2}(e)}\ \blacksquare
$$


---

## §F.III — Colour Objects and Spectrum

### CT3.11 — Colour objects

**Thm.** Within the rung-3 structure:
$$
(1)\ \ \text{colour}:=\text{slot index}\ i\in\{1,2,3\}\ [\mathrm{D3.1}],\ \ \text{fundamental of}\ \mathfrak{su}(3);
$$
$$
(2)\ \ \text{triplet}:\ q^i\mapsto U^i{}_jq^j\ (U\in SU(3));\qquad
(3)\ \ \text{antitriplet}:\ r_i\mapsto r_j(U^{-1})^j{}_i;
$$
$$
(4)\ \ \text{gluon}:=\gamma\in\mathsf{Trivial}\wedge\gamma\cap V_3\ne\varnothing;\qquad
(5)\ \ \text{photon}:=\gamma\in\mathsf{Trivial}\wedge\gamma\subseteq V_2\qquad[\mathrm{D3.7}];
$$
$$
(6)\ \ \text{quark}:=\text{bound loop}\ [\mathrm{D1.5}:\ \text{fermionic}]\ \text{with triplet attachment}\ [\mathrm{D3.8}];
$$
$$
(7)\ \ B:=\varepsilon_{ijk}q^iq^jq^k\ (\text{baryon});\qquad M:=\delta^i{}_jq^jr_i\ (\text{meson})\qquad[\mathrm{D3.9}].
$$

**Req.** D1.5, D3.1, D3.7, D3.8, D3.9; CT3.2, CT3.4, CT3.12, CT3.15, CT3.17.

**Pf.**
$$
(1)\text{--}(3):\ \ \mathrm{CT3.2}/\mathrm{CT3.4}:\ \text{carrier}\ \mathbb C^3,\ \ SU(3)\ \text{defining action};\quad\text{dual law}=\mathrm{CT3.17}\ \text{step 1}
$$
$$
(4),(5):\ \ \mathrm{D3.7};\quad\text{distinguished only by vertex type}=\mathrm{CT3.12}
$$
$$
(6):\ \ \mathrm{D3.8};\quad\text{bound}\implies\text{fermionic}\ [\mathrm{D1.5}]
$$
$$
(7):\ \ \mathrm{D3.9};\quad\text{both contractions invariant}:\ \mathrm{CT3.15},\ \mathrm{CT3.17}.\ \blacksquare
$$

**Phys.** The colour vocabulary, fixed: every term — colour, triplet, antitriplet, gluon, photon, quark, baryon, meson — names a structure already derived from the axioms.

---

### CT3.12 — Photon and gluon are distinguished by possibility space

**Thm.**
$$
\gamma_\gamma,\ \gamma_g\in\mathsf{Trivial}:\ \ \widehat{ds}^{\,2}(e)=0\ \ \forall e,\ \ \Theta=0,\ \ \operatorname{Hol}_{\mathrm{spiral}}=1;
$$
$$
\text{distinction}:\ \ \gamma_\gamma\subseteq V_2\quad\text{vs}\quad\gamma_g\cap V_3\ne\varnothing;
$$
$$
\mathrm{strong}\in\mathcal A(3)\setminus\mathcal A(2)\implies\gamma_\gamma:\ \neg\text{colour index};\quad\gamma_g:\ \text{slot index possible}\ [\mathrm{D3.1}];
$$
$$
\text{class, entropy channel (transit, D1.5), mass}\ (0)\ \text{coincide}.
$$

**Req.** D0.8, D1.5, D1.7, D3.1, D3.7; CT0.13 (Part 1); EM.5, EM.6 (Part 2); CT3.14.

**Pf.**
$$
\mathrm{D3.7}:\ \text{both}\in\mathsf{Trivial};\qquad\mathrm{D1.7}:\ \widehat{ds}^{\,2}\equiv0\implies\Theta=0,\ \operatorname{Hol}=e^{i\alpha\cdot0}=1
$$
$$
\mathrm{D0.8}:\ V_2\cap V_3=\varnothing;\qquad\mathrm{CT0.13}:\ \mathrm{strong}\ \text{active only from rung}\ 3
$$
$$
\text{no further distinguishing property}:\ \text{class}\ \mathsf{Trivial};\ \ \text{channel}=\text{transit}\ [\mathrm{D1.5}];\ \ m^2=0\ [\mathrm{CT3.14},\ \mathrm{EM.6}].\ \blacksquare
$$

**Phys.** Photon and gluon are the same kind of object — a null chain — differing only in where each is allowed to travel. The gluon’s colour is a consequence of touching trivalent vertices; the photon’s neutrality, of never doing so. (= EM.5 seen from the colour side.)

---

### CT3.13 — Gluon count

**Thm.** $\ N_{\mathrm{gluon}}=\dim\mathfrak{su}(3)=8;\qquad\neg\exists\ \text{ninth mode}\ (\text{centre of}\ \mathfrak u(3)\ \text{allocated to}\ F_{\mathrm{EM}}).$

**Req.** CT3.7, CT3.8; adjoint-representation dimension [math].

**Pf.**
$$
\mathrm{CT3.7}:\ \text{colour gauge algebra}=\mathfrak{su}(3);\qquad
\text{gauge mode}=\text{adjoint direction};\quad\dim\mathrm{adj}=\dim\mathfrak{su}(3)=8\ [\mathrm{CT3.8}]
$$
$$
\text{9th direction of}\ \mathfrak u(3)=\text{centre}\to F_{\mathrm{EM}}\ [\mathrm{CT3.7}\ \text{step 3}];\quad\text{reallocation}=\text{double counting}.\ \blacksquare
$$

**Phys.** Eight gluons — one per $\mathfrak{su}(3)$ generator. The ninth possible mode is electromagnetism, already counted at rung 2: the subset principle at work.

---

### CT3.14 — Gluons remain massless

**Thm.** $\ m_g^2=0$, by two independent routes:
$$
(\mathrm{i})\quad T_a\mathsf v=0\ [\mathrm{EW.32}]\implies M^2_{aB}=M^2_{ab}=0\implies\{T_a\}\subseteq\ker M^2\implies\text{zero pole displacement}\quad[=\mathrm{EW.26},\ \text{restated}];
$$
$$
(\mathrm{ii})\quad\gamma_g\in\mathsf{Trivial}\implies\Theta(\gamma_g)=0\implies\neg\text{wrapping holonomy}\implies\neg\text{wrapping contribution}\ [\mathrm{EW.18}].
$$

**Req.** D2.5, D3.7; CT0.14 (Part 1); EW.18, EW.26, EW.32, EW.33 (**D**, restated at use).

**Pf.**
$$
(\mathrm{i})\ \ \mathrm{D2.5}:\ m^2=\text{pole displacement};\qquad\mathrm{EW.33}\ \text{(restated)}:\ \text{rung-3 displacement source}=M^2_{AB}=\mu_\star^2\operatorname{Re}\langle\mathcal G_A\mathsf v,\mathcal G_B\mathsf v\rangle
$$
$$
\mathrm{EW.32}\ \text{(restated)}:\ F_H=\text{pair block}\perp F_{\mathrm{strong}}=\text{stack block}\ [\mathrm{CT0.14}]\implies\text{seed has}\ \neg\text{slot index}\implies T_a\mathsf v=0
$$
$$
\implies M^2_{aB}=\mu_\star^2\operatorname{Re}\langle0,\mathcal G_B\mathsf v\rangle=0,\quad M^2_{ab}=0\implies\{T_a\}_{a=1}^{8}\subseteq\ker M^2\implies m_g^2=0
$$
$$
(\mathrm{ii})\ \ \mathrm{D3.7}:\ \gamma_g\in\mathsf{Trivial}\implies\Theta=0;\qquad\mathrm{EW.18}\ \text{(restated)}:\ \text{materialization requires}\ \Phi\in2\pi\mathbb Z\ \text{from winding}\implies\neg\text{wrapping}\implies\neg\text{contribution}.\ \blacksquare
$$

**Phys.** Gluons are massless structurally: the seed that generates mass is colour-blind (route i), and null chains cannot wind (route ii). Two independent arguments, agreeing — masslessness of the strong gauge modes is as robust as the photon’s.

---

### CT3.15 — Baryon invariance

**Thm.** $\ B=\varepsilon_{ijk}q^iq^jq^k;\qquad U\in SU(3):\quad B\mapsto\varepsilon_{ijk}U^i{}_aU^j{}_bU^k{}_c\,q^aq^bq^c=\det(U)\,\varepsilon_{abc}\,q^aq^bq^c=B.$

**Req.** D3.9; CT3.2; Leibniz identity $\varepsilon_{ijk}U^i{}_aU^j{}_bU^k{}_c=\det(U)\varepsilon_{abc}$ [math]; machine: `checks/verify_F.py`.

**Pf.**
$$
\mathrm{CT3.2}:\ q^i\mapsto U^i{}_aq^a\implies B\mapsto\varepsilon_{ijk}U^i{}_aU^j{}_bU^k{}_c\,q^aq^bq^c
$$
$$
\varepsilon_{ijk}U^i{}_aU^j{}_bU^k{}_c=\det(U)\,\varepsilon_{abc}\quad[\text{Leibniz expansion of}\ \det;\ \text{machine-verified on random exact}\ U]
$$
$$
U\in SU(3)\implies\det U=1\implies B\mapsto\varepsilon_{abc}q^aq^bq^c=B.\ \blacksquare
$$

**Phys.** The totally antisymmetric three-index contraction is a colour singlet: the baryon — three triplets sealed by $\varepsilon$ — is the minimal neutral object of the strong sector.

---

### CT3.16 — Infinitesimal baryon invariance

**Thm.** $\ U=I_3+i\theta^aT_a+O(\theta^2),\ \ \mathfrak T(T_a)=0\implies\det U=1+O(\theta^2)\implies B\mapsto B+O(\theta^2)$ (first-order variation vanishes).

**Req.** CT3.7 ($\mathfrak T T_a=0$), CT3.15; $\det=\exp\mathfrak T\log$ [math].

**Pf.**
$$
\log U=i\theta^aT_a+O(\theta^2);\qquad
\det U=\exp\mathfrak T(\log U)=\exp\bigl(i\theta^a\underbrace{\mathfrak T(T_a)}_{=0}+O(\theta^2)\bigr)=1+O(\theta^2)
$$
$$
\mathrm{CT3.15}:\ B\mapsto\det(U)\,B=B+O(\theta^2).\ \blacksquare
$$

**Phys.** The singlet property holds at the algebra level: tracelessness of the colour generators is exactly the condition that makes baryon sealing infinitesimally exact.

---

### CT3.17 — Invariant tensors

**Thm.** The invariant tensors for sealing colour indices are generated by
$$
\delta^i{}_j,\qquad\varepsilon_{ijk},\qquad\varepsilon^{ijk};
$$
$$
q^ir_i\mapsto U^i{}_aq^a\,r_b(U^{-1})^b{}_i=q^ar_a;\qquad
\varepsilon_{ijk}:\ 3\ \text{fundamentals}\ [\mathrm{CT3.15}];\qquad
\varepsilon^{ijk}:\ 3\ \text{duals}\ \bigl(\det(U^{-1})^{\mathsf T}=1\bigr);
$$
$$
\forall\ \text{invariants of}\ (\mathbf3,\bar{\mathbf3}):\ \ \text{linear combinations of products of}\ \{\delta,\varepsilon,\bar\varepsilon\}.
$$

**Req.** CT3.2, CT3.15; determinant identities [math]; machine: `checks/verify_F.py`.

**Pf.**
$$
\delta:\ \ U^i{}_a(U^{-1})^b{}_i=\delta^b{}_a\implies q^ir_i\ \text{invariant}\quad[\text{machine}:\ U^{-1}U=I]
$$
$$
\varepsilon_{ijk}:\ \mathrm{CT3.15};\qquad
\varepsilon^{ijk}:\ \text{same identity at}\ (U^{-1})^{\mathsf T},\ \ \det(U^{-1})^{\mathsf T}=1
$$
$$
\text{generation}:\ \delta\ \text{seals matched pairs};\ \ \varepsilon/\bar\varepsilon\ \text{seal residues mod}\ 3\ \text{of unmatched indices}\implies\forall\ \text{invariant}=\text{combination of products}.\ \blacksquare
$$

**Phys.** Only three tensors can seal colour: pair-annihilation $\delta$, three-quark $\varepsilon$, three-antiquark $\bar\varepsilon$. The entire hadronic vocabulary — mesons, baryons, antibaryons — is built from these.


**Cor CT3.17a (sealing partition rule; grammar counts).** $(1)$ **Partition rule.** If a colour-attachment set is sealed — $\mathcal C(\Sigma;C)=1$ [D2.14] — then $\mathrm{Colour}(\Sigma)$ partitions into elementary contraction groups of size $2$ ($\delta$-type) and size $3$ ($\varepsilon/\bar\varepsilon$-type) [CT3.17: the invariant tensors are $\delta^{i}{}_{j}$ ($2$ members), $\varepsilon_{ijk}$, $\varepsilon^{ijk}$ ($3$ members); D2.14: $\pi_C(v)=$ the other members of $v$'s elementary group]. A lone attachment is never sealed:
$$
|\mathrm{Colour}(\Sigma)|=1\implies\mathcal C(\Sigma;C)=0
$$
[a contraction partner is a distinct node — A1: $p\ne q$ — hence $\pi_C(v)\not\subseteq\{v\}$; equivalently, CT3.17's list contains no invariant of a single slot].
$(2)$ **Grammar count.** The number $g(N)$ of elementary groupings of a labelled $N$-element attachment set into groups of size $2$ and $3$ (labelled set partitions with parts in $\{2,3\}$) is
$$
g(N)=\!\!\sum_{\substack{a,b\ge0\\ 2a+3b=N}}\!\!\frac{N!}{a!\,b!\,2^{a}\,6^{b}};\qquad
g(1)=0,\quad g(2)=1,\quad g(3)=1,\quad g(4)=3,\quad g(5)=10,\quad g(6)=25\ (15+10),\quad g(7)=105 .
$$
$(3)$ **Type selection.** Attachment-type assignment (triplet/antitriplet per attachment [D3.8]) selects the type-compatible groupings — $\delta^{i}{}_{j}$ consumes one attachment of each type, $\varepsilon_{ijk}$ ($\varepsilon^{ijk}$) three of the same type [CT3.17] — configuration data refining the count of $(2)$.

**Req (Cor).** A1; D2.14, D3.8; CT3.17; labelled set-partition enumeration [math; machine: `checks/verify_promotion_F_colour.py`].

**Pf (Cor).**
$$
(1):\ \mathrm{CT3.17}:\ \text{every invariant}=\text{combination of products of}\ \{\delta,\varepsilon,\bar\varepsilon\}:\ \text{an elementary group consumes}\ 2\ \text{or}\ 3\ \text{slots};\qquad\mathrm{D2.14}:\ \mathcal C=1\iff\forall v:\ \pi_C(v)\subseteq\Sigma
$$
$$
\implies\mathrm{Colour}(\Sigma)=\bigsqcup\ \text{groups of size}\ 2,3;\qquad N=1:\ \mathrm{A1}:\ p\ne q\implies\pi_C(v)\ \text{requires a distinct member}\implies\pi_C(v)\not\subseteq\{v\}\implies\mathcal C=0\ [\mathrm{D2.14}]
$$
$$
(2):\ \text{fix}\ (a,b),\ 2a+3b=N:\ \ \#\{\text{partitions into}\ a\ \text{pairs}+b\ \text{triples}\}=\frac{N!}{a!\,b!\,(2!)^{a}\,(3!)^{b}}\quad[\text{math}:\ \text{labelled elements; block order and within-block order unlabelled}]
$$
$$
(2!)^{a}=2^{a},\ (3!)^{b}=6^{b};\qquad g(4)=\tfrac{4!}{2!\,2^{2}}=3;\quad g(5)=\tfrac{5!}{1!\,1!\,2\cdot6}=10;\quad g(6)=\tfrac{6!}{3!\,2^{3}}+\tfrac{6!}{2!\,6^{2}}=15+10=25;\quad g(7)=\tfrac{7!}{2!\,1!\,2^{2}\cdot6}=105\ [\text{machine}]
$$
$$
(3):\ \mathrm{D3.8}:\ \text{attachment types};\quad\delta^{i}{}_{j}:\ (\mathbf3,\bar{\mathbf3});\quad\varepsilon_{ijk}:\ (\mathbf3,\mathbf3,\mathbf3);\quad\varepsilon^{ijk}:\ (\bar{\mathbf3},\bar{\mathbf3},\bar{\mathbf3})\ [\mathrm{CT3.17}]\ \blacksquare
$$


---

### CT3.18 — Colour-singlet closure

**Thm.**
$$
\text{free colour index}=\text{dangling boundary of the colour ledger}\ \neg\text{admitted by}\ \mathcal P_M^{(3)};
$$
$$
\mathcal P_M^{(3)}\big|_{\text{free index}}=0\implies\neg\exists\ \text{pole}\ [\mathrm{CT2.5}];\qquad
\text{surviving configurations}:\ \text{fully contracted by}\ \{\delta,\varepsilon,\bar\varepsilon\}\implies\text{colour singlets};
$$
$$
\text{minimal singlets}:\ M=\delta^i{}_jq^jr_i,\quad B=\varepsilon_{ijk}q^iq^jq^k\ [\mathrm{D3.9}].
$$

**Req.** D2.3, D2.11, D3.1, D3.9; CT2.5 (Part 2); CT3.17.

**Pf.**
$$
\mathrm{D2.11}:\ \text{valid universe}:\ \text{closed}\ \wedge\ \text{balanced seals}\ \wedge\ \neg\exists\ \text{dangling ledger boundary}
$$
$$
\mathrm{D3.1}:\ \text{colour indices}=\text{ledger labels at trivalent vertices}\implies\text{uncontracted index}=\text{dangling colour-ledger boundary}
$$
$$
\mathrm{D2.3}:\ \mathcal P_M^{(3)}\ \text{projects onto valid configurations}\implies\text{free-index configurations annihilated};\qquad
\mathrm{CT2.5}:\ \neg\text{pole}
$$
$$
\text{survivors fully contracted};\quad\mathrm{CT3.17}:\ \text{contractions}\in\{\delta,\varepsilon,\bar\varepsilon\}\implies\text{invariant}=\text{colour singlet}.\ \blacksquare
$$

**Phys.** The mask admits only colour-sealed configurations: every observable bound rung-3 object is a colour singlet, minimally a meson or a baryon. Validity of the ledger *is* the singlet condition.

---

### CT3.22 — Sealing is confinement

**Thm.**
$$
\neg\exists\ \text{isolated triplet pole of}\ Z(\mathcal R,3);\qquad
\text{isolated triplet}:\ \text{physical norm}=0\ [\mathrm{CT2.8}];
$$
$$
\text{colour charge}\ \neg\text{observable as end-charge}\ [\mathrm{D3.4}];\qquad
\text{contrast}:\ q_{\mathrm{EM}}\ \text{observable on open chains}\ (\text{per-edge registration},\ \neg\text{contraction}).
$$

**Req.** D3.4; CT0.9 (Part 1); CT2.3, CT2.5, CT2.8 (Part 2); CT3.18.

**Pf.**
$$
\mathrm{CT3.18}:\ \text{free colour index}\implies\notin\operatorname{Im}\mathcal P_M^{(3)}
$$
$$
\mathrm{CT2.3}:\ \mathbf F_M^{(3)}\big|_{\mathcal K_3^\perp}=0;\qquad
\mathrm{CT2.5}:\ \text{poles}=\text{eigenvalue conditions on}\ \mathbf F_M^{(3)}\implies\text{excluded configurations support}\ \neg\text{poles}
$$
$$
\mathrm{CT2.8}\ \text{step 3}:\ \text{mask-excluded}=\text{null vectors of}\ \langle\cdot|\cdot\rangle\implies\text{isolated triplet}:\ \text{norm}=0
$$
$$
\text{contrast}:\ \mathrm{D3.4}:\ q_{\mathrm{EM}}=\tfrac12(\sigma_s-\sigma_t)\ \text{from edge signs};\quad
\mathrm{CT0.9}:\ \sigma_e\ \text{registered per real edge},\ \neg\text{contraction required}\implies q_{\mathrm{EM}}\ \text{observable on open chains}.\ \blacksquare
$$

**Phys.** Confinement is a theorem: isolated colour has no pole and no norm — it is filtered out by the mask, not suppressed by a force law. The asymmetry with visible electric charge is exact: a sign is registered per edge; an index must await contraction.

---

### CT3.22a — Subnetwork confinement: the domain restriction, all-or-nothing, and the converse

**Thm.** Let $\Sigma$ be a subnetwork [D2.13] with $\mathcal C(\Sigma;C)$, $\Pi_{\mathcal C}(\Sigma;C)$ [D2.14], and $F_{\mathrm{strong}}|_\Sigma:=$ the strong force operator restricted to the colour slots of $\Sigma$ under the rung mask [CT2.3, CT2.4; D3.1].
$(0)$ **Global sum-restriction.**
$$Z^{(3)}(\mathcal R)=\sum_{\substack{C\in\mathfrak C(\mathcal R):\ \text{colour-sealed}}}\ \sum_\sigma\mathcal J(C)\!\!\prod_{e\in E(C)}\!\!G^{(3)}(e)\ (-1)^{\aleph(\sigma,C)}\qquad[\mathrm{D0.10},\ \mathrm{C12}]$$
— confinement restricts the summation domain, $\neg$any individual edge factor: the per-edge geometric/registration data are rung-independent once the block read is rung-stable ($\alpha_{\mathrm{EM}}^{(3)}=\alpha_{\mathrm{EM}}^{(2)}$ — the EM.18/EM.19 mechanism) and the per-edge phase alphabet is rung-blind ($\alpha_e\in\Phi=\{0,\pi\}$ at every rung [D0.5; CT0.9; EM.20(1)]).
$(1)$ **All-or-nothing.** With $F^\Sigma_{\mathrm{strong}}(C):=\Pi_{\mathcal C}(\Sigma;C)\,F_{\mathrm{strong}}|_\Sigma\,\Pi_{\mathcal C}(\Sigma;C)$:
$$\mathcal C(\Sigma;C)=0\implies F^\Sigma_{\mathrm{strong}}(C)=0$$
— regardless of how many colour-carrying vertices $\Sigma$ contains, and even if $|\partial_{\mathrm{col}}(\Sigma;C)|=1$.
$(2)$ **Converse with the exact exception locus.** $\Pi_{\mathcal C}=\mathcal C\cdot\mathbb I$ with $\mathcal C\in\{0,1\}$ [D2.14: scalar idempotent] $\implies F^\Sigma_{\mathrm{strong}}=\mathcal C\cdot F_{\mathrm{strong}}|_\Sigma$; hence
$$\mathcal C=1\implies F^\Sigma_{\mathrm{strong}}=F_{\mathrm{strong}}|_\Sigma\ne0\quad\text{for nonzero aspect data}\ (f_a\ne0\ \text{on}\ \ge1\ \text{colour slot}\ [\mathrm{CT3.9},\ \mathrm{CT3.10}])$$
with exact exception locus $\{f=0\}\ \cup\ \{\mathrm{Colour}(\Sigma)=\varnothing\}$.
$(3)$ **Singlet diagonal (consistency).** $T_a|\text{singlet}\rangle=0$ [CT3.15, CT3.17 invariance] $\implies\langle\text{singlet}|F_{\mathrm{strong}}|\text{singlet}\rangle=0$ — consistent with CT3.22 (colour is $\neg$observable as end-charge [D3.4]): the nonzero content of the strong block is the admissibility structure and the gluon mode count [CT3.13], $\neg$singlet expectation values.

**Req.** D2.13, D2.14; D0.10, D3.1, D3.4, D3.5, C12; CT2.3, CT2.4, CT2.5, CT2.8 (Part 2); CT3.2, CT3.9, CT3.10, CT3.13, CT3.15, CT3.17, CT3.18, CT3.22; EM.18, EM.19, EM.20(1) for clause (0) note (Part 2); idempotent algebra, the tensor null-factor argument [math; machine: `checks/verify_merge_tierA.py` §A].

**Pf.**
$$(0):\ \mathrm{CT3.18}:\ \mathcal P_M^{(3)}\ \text{admits only colour-sealed}\ C\ (\delta^i{}_j,\ \varepsilon_{ijk},\ \varepsilon^{ijk}\ \text{contractions}\ [\mathrm{CT3.17}]);\qquad \mathrm{CT3.22}:\ \neg\exists\ \text{isolated triplet pole}$$
$$\text{free-index}\ C\notin\operatorname{Im}\mathcal P_M^{(3)};\quad \mathrm{CT2.5}:\ \text{poles}=\text{eigenvalue conditions on}\ \mathbf F_M^{(3)};\quad \mathrm{CT2.3}:\ \mathbf F_M^{(3)}\big|_{\mathcal K_3^\perp}=0\implies\text{excluded}\ C:\ \neg\text{pole}\implies\text{domain restriction}$$
$$\text{edge factors}:\ G^{(n)}(e)=\sigma_e\exp(i\alpha_e\widehat{ds}^{\,2}(e))\ [\mathrm{D3.5}];\quad \alpha_e\in\{0,\pi\}\ \text{at every rung}\ [\mathrm{EM.20}(1);\ \mathrm{CT0.9}];\quad \alpha_{\mathrm{EM}}^{(3)}=\alpha_{\mathrm{EM}}^{(2)}\ [\mathrm{EM.18}/\mathrm{EM.19}]\implies G^{(3)}=G^{(2)}\implies\neg\text{weight modification}$$
$$(1):\ \mathcal C=0:\ \exists v\in\mathrm{Colour}(\Sigma):\ \pi_C(v)\not\subseteq\Sigma\ [\mathrm{D2.14}]\implies v\ \text{carries an index uncontracted relative to}\ \Sigma$$
$$\mathrm{CT3.18}\ \text{with}\ \Sigma\ \text{as ambient}:\ \text{uncontracted index}=\text{dangling colour-ledger boundary}\implies\text{mask-excluded};\qquad \mathrm{CT3.22}+\mathrm{CT2.5}:\ \neg\text{pole of the}\ \Sigma\text{-restricted resolvent}$$
$$\mathrm{CT2.8}:\ \text{physical norm}\ 0\implies\text{the}\ \Sigma\text{-restricted colour state of}\ v\ \text{is a null vector};\qquad \text{colour sector of}\ \Sigma\ =\bigotimes_{\mathrm{Colour}(\Sigma)}(\text{slot spaces})\ [\mathrm{D3.1},\ \mathrm{CT3.2}]$$
$$\text{one null factor}\implies\text{whole product null}\implies F_{\mathrm{strong}}|_\Sigma\ \text{has vanishing matrix elements};\qquad \Pi_{\mathcal C}=0\implies F^\Sigma_{\mathrm{strong}}=0\cdot F_{\mathrm{strong}}|_\Sigma\cdot0=0$$
$$(2):\ \mathcal C\in\{0,1\}\implies\mathcal C^2=\mathcal C\implies\Pi_{\mathcal C}\,F\,\Pi_{\mathcal C}=\mathcal C^2\,F|_\Sigma=\mathcal C\,F|_\Sigma;\qquad \mathcal C=1:\ T_a\ne0\ \text{on}\ \mathbb C^3\ [\mathrm{CT3.9}:\ \text{explicit Gell-Mann basis}]\ \wedge\ f\ne0\ [\mathrm{CT3.10}]\implies F|_\Sigma\ne0$$
$$\text{exception locus}:\ f=0\implies F|_\Sigma=0\ \text{by linearity};\quad \mathrm{Colour}(\Sigma)=\varnothing\implies F|_\Sigma\ \text{has no argument}$$
$$(3):\ \varepsilon_{ijk}U^i{}_aU^j{}_bU^k{}_c=\varepsilon_{abc}\det U=\varepsilon_{abc}\quad\forall U\in SU(3)\ [\mathrm{CT3.15}];\qquad \delta^i{}_j\ \text{likewise invariant}\ [\mathrm{CT3.17}]$$
$$\implies\text{singlets fixed under}\ SU(3)\implies\mathfrak{su}(3)\ \text{annihilates them}\implies\langle\text{singlet}|F_{\mathrm{strong}}|\text{singlet}\rangle=0.\ \blacksquare$$

**Phys.** Confinement becomes a two-sided exact law at subnetwork level: the colour block of a region lives precisely when the region self-seals against the ambient ledger — one dangling attachment anywhere zeroes the entire colour sector, no matter how many safely paired vertices sit inside. Unlike the additive per-vertex read of EM [D3.3], the strong read is $\neg$gradable: a sealed object never carries a colour number, only the grammar of how it composes with its environment.

**Rmk (non-locality and filter placement; witness scope).** $\mathcal C(\Sigma;C)$ is $\neg$a function of $\Sigma$-local data: valid ambient pairs $C,C'$ with identical restrictions $C|_\Sigma=C'|_\Sigma$ yet $\mathcal C=1$ vs $0$ exist once the ambient supplies further triplet carriers to seal (explicit finite witness: two valid ambient groupings, identical $\Sigma$-occupation, opposite seals) — an ambient-richness scope for that witness, $\neg$derivable from A1 alone; no theorem clause above rests on it (A §0.2a note). Hence the completeness filter belongs *downstream* of any $\mathcal M(\Sigma)$ weighting: pre-weighting by $\mathcal C$ would delete the physical EM/$G$/$H$ reads of externally-sealed restrictions, which are colour-independent by construction [D3.3, CT1.12]. Universe-level validity remains CT3.18/CT2.8(3)'s question — distinct from $\Sigma$-relativity.

---

## §F.IV — Completion

### CT3.19 — Self-containment of the colour sector

**Thm.**
$$
\forall\ \text{statements of}\ \mathbf F:\quad\vdash\ \mathrm{A1\text{–}A9}\cup\mathrm{C1\text{–}C9}\cup\mathrm{D0.1\text{–}D4.3}\cup\{\mathbf B,\mathbf C\ \text{theorems}\}\cup\{\mathrm{EW.26},\mathrm{EM.18}\ \text{restated}\};
$$
$$
\neg\exists\ \text{external strong-interaction law, parameter, or measured value};\qquad
\text{open quantities}=\varnothing:
$$
$$
N_{\text{colour}}=3,\quad N_{\mathrm{gluon}}=8,\quad f_{abc},\quad\mathfrak T(T_aT_b)=\tfrac12\delta_{ab},\quad m_g^2=0\qquad\text{all fixed};
$$
$$
\text{colour sector contributes}\ \neg\mathrm{P4}\ \text{data}.
$$

**Req.** CT3.1–CT3.22; P4.

**Pf.** Dependency trace:
$$
3\ \text{slots}\Leftarrow2^{n+1}\le16\ [\mathrm{CT3.20}\Leftarrow\mathrm{CT0.5},\mathrm{CT0.6},\mathrm{CT0.11}]
$$
$$
S_3\hookrightarrow U(3)\ [\mathrm{CT3.1}\text{--}\mathrm{CT3.4}];\quad
\mathfrak u(3)=\mathfrak{su}(3)\oplus\mathfrak u(1)\ [\mathrm{CT3.5}];\quad
\text{centre spent at rung 2}\implies\text{new}=\mathfrak{su}(3)\ [\mathrm{CT3.7},\mathrm{D3.2}]
$$
$$
\dim=8\ [\mathrm{CT3.8}];\quad\text{normalized basis}\ [\mathrm{CT3.9}];\quad f_{abc}\ \text{determined}\ [\mathrm{CT3.21}];\quad\text{normalization}=\mathrm{EW.32}\text{'s}
$$
$$
\mathfrak T=0\implies\neg\text{abelian carry/shift}\ [\mathrm{CT3.10}]
$$
$$
\text{gluons}:\ 8\ \text{massless trivial chains}\ [\mathrm{CT3.13},\mathrm{CT3.14}];\quad\gamma/g\ \text{differ by possibility space only}\ [\mathrm{CT3.12}]
$$
$$
\{\delta,\varepsilon,\bar\varepsilon\}\ [\mathrm{CT3.17}];\quad\text{mask admits only singlets}\ [\mathrm{CT3.18}];\quad\text{isolated colour}:\ \neg\text{pole},\ \text{norm}\ 0\ [\mathrm{CT3.22}].\ \blacksquare
$$

**Phys.** Closure audit: the colour sector is the most rigid in the corpus — number of colours, number of gluons, all structure constants, normalization and masslessness are fixed by the axioms, with not a single configuration parameter of its own.

---

## Closure exports of Part 2 §F (consumed by Part 2 §E, §G, Parts 3–4)

$$
\begin{array}{lll}
\mathrm{CT3.20}\ N_{\text{colour}}=3\ (\text{forced}) &
\mathrm{CT3.7}\ \text{new algebra}=\mathfrak{su}(3),\ \mathfrak T(T_a)=0\ [\text{cited in E}] &
\mathrm{CT3.8}\ \dim=8\ [\text{cited in B: CT0.14}]\\
\mathrm{CT3.9}\ \{T_a\}:\ \mathfrak T(T_aT_b)=\tfrac12\delta_{ab} &
\mathrm{CT3.21}\ f_{abc}\ \text{exact list} &
\mathrm{CT3.10(a)}\ \mathfrak T(F_{\mathrm{strong}})=0;\ \alpha^{(3)}=\alpha^{(2)};\ \neg\exists\,\alpha_{\mathrm{strong}}\\
\mathrm{CT3.13}\ N_{\mathrm{gluon}}=8 &
\mathrm{CT3.14}\ m_g^2=0\ (\times2\ \text{routes}) &
\mathrm{CT3.15}\text{--}\mathrm{CT3.17}\ B,\ M\ \text{singlets};\ \{\delta,\varepsilon,\bar\varepsilon\};\ \mathrm{CT3.17a}:\ g(N)\ \text{grammar}\\
\mathrm{CT3.18}\ \text{mask admits only singlets} &
\mathrm{CT3.22}\ \text{confinement}:\ \neg\text{triplet pole},\ \text{norm}\ 0 &
\mathrm{CT3.19}\ \text{sector rigid},\ \neg\mathrm{P4}\ \text{data}
\end{array}
$$

$\blacksquare$

---

## §G — Saturation Lock, Dark Aspects, Bounds

*Dep.: Part 1; Part 2 §C–§F (EW.27 at use). Order: §G.I the saturation lock (CT4.1, +CT4.1a, CT4.2, CT4.3, CT4.4, +CT4.4a) · §G.II the two dark aspects (CT4.5, +CT4.5a, CT4.6, CT4.7, +CT4.7a, CT4.10) · §G.III bounds and boundaries (CT4.9, CT4.8, CT4.11) · §G.IV falsifiability and the closure audit (CT4.12, CT4.13). Notation as Part 2 §C–§F. Machine: `checks/verify_G.py`; CT4.4a/CT4.7a: `checks/verify_merge_tierA.py`; CT4.5a/CT4.1a: `checks/verify_promotion_G_saturation.py`.*

## §G.I — The Saturation Lock

### CT4.1 — Oversubscription falls to $D^-$

**Thm.**
$$
\forall n\ge4:\quad D_{\mathrm{tick}}(n)=2^{n+1}\ge32>16=C_{\mathrm{cap}}\implies O(n)=2^{n+1}-16>0;
$$
$$
O(4)=32-16=16=C_{\mathrm{cap}}\quad(\text{exactly one further channel quantum per tick});
$$
$$
F_{D^-}=\bigoplus_{n\ge4}F_n\ [\mathrm{D4.1}];\qquad
\text{absorption rate}\propto O(n)\sim2^{n+1}\ [\mathrm{D4.2}];\qquad
\text{last admissible rung}=3 .
$$
$$
\begin{array}{c|c|c|c}
n & D_{\mathrm{tick}}(n)=2^{n+1} & O(n) & \text{status}\\ \hline
0 & 2 & 0 & \text{virtual only},\ \mathcal A(0)=\{J\}\\
1 & 4 & 0 & \text{pair aspects active}\\
2 & 8 & 0 & \text{abelian aspect activates}\\
3 & 16 & 0 & \text{exact saturation};\ \text{colour activates}\\
4 & 32 & 16 & \text{locked in}\ D^-\\
5 & 64 & 48 & \text{locked in}\ D^-\\
n\ge4 & 2^{n+1} & 2^{n+1}-16 & \text{locked in}\ D^-
\end{array}
$$

**Req.** A2; D4.1, D4.2; CT0.5, CT0.6, CT0.11 (Part 1).

**Pf.**
$$
D_{\mathrm{tick}}(n)=2^{n+1}\ [\mathrm{CT0.5}];\qquad C_{\mathrm{cap}}=\dim_{\mathbb R}\mathfrak H(\mathbb C^4)=16\ [\mathrm{CT0.6}\Leftarrow\mathrm{A2}]
$$
$$
n=4:\ \ O(4)=2^{5}-16=16=C_{\mathrm{cap}};\qquad
n\ge4:\ \ 2^{n+1}\ge32>16\implies O(n)=2^{n+1}-16>0
$$
$$
\mathrm{D4.1}:\ n\ge4\implies\text{config}\in F_{D^-}=\bigoplus_{n\ge4}F_n;\qquad
\mathrm{D4.2}:\ \text{rate}\propto O(n)\implies\neg\exists\ \text{rung}\ n\ge4\ \text{escaping}
$$
$$
\mathrm{CT0.11}:\ \text{admissible}\iff n\le3.\ \blacksquare
$$

**Phys.** Rung 4 demands $32$ registers against a budget of $16$ — exactly one extra channel quantum — and every higher rung demands more. All such configurations collapse into a single sink $D^-$ whose absorption grows as $2^{n+1}$: rung 3 is the last rung the universe can access, and above it there is only the lock.


**Cor CT4.1a (universal saturation of bidirectional real-edge subgraphs).** Let $S$ be a bidirectional real-edge subgraph — both orientations of every used channel in $\mathcal R$ [A4] — exhausting the incident real edges at its vertices, with channel degree $d_S(v)$. Then $n(v)=2\,d_S(v)$ [CT0.11b (Part 1), D0.8], and:
$(1)\ \ d_S(v)\ge2\implies n(v)\ge4\implies O\bigl(n(v)\bigr)>0$: every such vertex falls to $F_{D^-}$ [CT4.1, D4.1]; its content is absorbed, retained in $\mathfrak L$ and counted, $\neg$accessible [CT4.2, CT4.3, D4.2, D1.11] — no bidirectional vertex of channel degree $\ge2$ is unoversubscribed.
$(2)\ \ S\ 2$-*regular* (bidirectional cycles, any length $\ge3$): uniform minimal saturation $n(v)=4\ \forall v$; $O(4)=16=C_{\mathrm{cap}}$ — exactly one channel quantum over budget per vertex, independent of cycle length [CT0.6, CT4.1].
$(3)\ \ S\ d$-*regular*: graded oversubscription $O(2d)=2^{2d+1}-16$ [CT0.6]:
$$
O(4)=16,\qquad O(6)=112,\qquad O(8)=496,\qquad O(10)=2032,\qquad O(12)=8176 .
$$
$(4)$ The unoversubscribed real-edge family under directed rung counting is exactly $n(v)\le3$ [CT0.11b, CT0.6]: on bidirectional $S$ only single-channel vertices ($n=2$); mixed skeletons admit unidirectional attachments up to $n=3$; every vertex with $n(v)\ge4$ is saturated [CT0.11, CT4.1].

**Req (Cor).** A4; D0.8, D1.11, D4.1, D4.2; CT0.6, CT0.11, CT0.11b (Part 1); CT4.1, CT4.2, CT4.3; exact ladder arithmetic [math; machine: `checks/verify_promotion_G_saturation.py`].

**Pf (Cor).**
$$
n(v)=2\,d_S(v)\ [\mathrm{CT0.11b},\ \mathrm{D0.8}];\qquad
(1):\ d_S\ge2:\ n\ge4:\ O(n)=2^{n+1}-16>0\ [\mathrm{CT0.6}]\implies F_{D^-}\ [\mathrm{CT4.1},\ \mathrm{D4.1}]
$$
$$
\mathrm{CT4.2}:\ \text{absorbing};\qquad\mathrm{CT4.3}/\mathrm{D4.2}:\ \text{retained}\subseteq\mathfrak L,\ \text{counted},\ \neg\text{accessible}\ [\mathrm{D1.11}]
$$
$$
(2):\ d_S\equiv2:\ n\equiv4;\quad O(4)=2^{5}-16=16=C_{\mathrm{cap}}\ [\mathrm{CT0.6},\ \mathrm{CT4.1}];\qquad
(3):\ O(2d)=2^{2d+1}-16:\ \ 2^{7}{-}16=112,\ \ 2^{9}{-}16=496,\ \ 2^{11}{-}16=2032,\ \ 2^{13}{-}16=8176\ [\text{exact}]
$$
$$
(4):\ \mathrm{CT0.11b}\ \text{verbatim};\qquad n\ge4\implies O>0\implies\text{saturated}\ [\mathrm{CT0.11},\ \mathrm{CT4.1}]\ \blacksquare
$$


---

### CT4.2 — The lock is absorbing

**Thm.**
$$
\forall n\le3:\quad\mathcal P_M^{(n)}\,F_{D^-}\,\mathcal P_M^{(n)}=0;
$$
$$
\text{locked content}:\ \neg\exists\ \text{pole of}\ Z(\mathcal R,n)\ \ \forall n\le3\qquad(\text{one-way transfer w.r.t. the accessible sector}).
$$

**Req.** D4.1; CT0.13, CT0.14 (Part 1); CT2.5 (Part 2).

**Pf.**
$$
\mathrm{D4.1}:\ \operatorname{supp}F_{D^-}\subseteq\mathcal K^{(D^-)};\qquad
\mathrm{CT0.13}:\ D^-\in\mathcal A(n)\iff n\ge4
$$
$$
\mathrm{CT0.14}:\ \text{aspect blocks}=\text{orthogonal summands of}\ \mathcal K;\quad
\mathcal K^{(D^-)}\not\subseteq\mathcal K_n\ \ (n\le3)\implies\mathcal P_M^{(n)}\big|_{\mathcal K^{(D^-)}}=0\implies\mathcal P_M^{(n)}F_{D^-}\mathcal P_M^{(n)}=0
$$
$$
\mathrm{CT2.5}:\ \text{pole}\implies\text{nonzero support in}\ \mathcal K_n;\qquad
\text{locked content has none}\implies\neg\exists\ \text{accessible pole at any}\ n\le3.\ \blacksquare
$$

**Phys.** The lock is a one-way membrane: no accessible mask can bring $D^-$ content back, and locked content supports no accessible spectral pole at any rung. What falls in stays in — with respect to everything an accessible observer can measure.

---

### CT4.3 — Locked, not destroyed

**Thm.**
$$
\text{absorption conserves ledger content}:\quad\text{absorbed}\subseteq\mathfrak L;\qquad\neg\text{accessible}\ [\mathrm{D1.11}];\qquad\neg\exists\ \text{deleted entry};
$$
$$
\text{oversubscription}\ \neg\text{seal}:\ \Delta n_{\mathcal R}=0;
$$
$$
\text{locked content}:\ \ \text{physical norm}=0\ \text{at accessible rungs}\ [\mathrm{CT2.8}]\ \ \wedge\ \ w(C)\ne0\ \text{in the unmasked A8 sum}\ (\text{record survives}).
$$

**Req.** A5, A8; D0.7, D1.11, D4.2; CT0.3 (Part 1); CT2.8 (Part 2); CT4.1, CT4.2.

**Pf.**
$$
\mathrm{D0.7}:\ \mathfrak L=\text{ordered record of retained events};\qquad
\mathrm{A5}:\ \text{sole exclusion}=U\ (\text{Haar draw}),\ \ U\notin\mathfrak L
$$
$$
\mathrm{D4.2}:\ \text{absorbed}=\text{locked}:=\text{retained in}\ \mathfrak L\ \wedge\ \neg\text{accessible}\ [\mathrm{D1.11}]
$$
$$
\mathrm{CT0.3}:\ \text{counters change only via seals};\qquad
\mathrm{CT4.1}:\ \text{oversubscription}=\text{load/capacity mismatch at fixed rung}\implies\Delta n_{\mathcal R}=0\implies\neg\text{seal}\implies\neg\exists\ \text{removed entry}
$$
$$
\mathrm{CT2.8}:\ \text{null vectors}=\text{mask-excluded}\implies\text{locked}:\ \text{norm}\ 0\ \text{at accessible rungs}\ [\mathrm{CT4.2}]
$$
$$
\mathrm{A8}:\ w(C)\ \text{retains nonzero value in the unmasked sum}\implies\text{record survives}.\ \blacksquare
$$

**Phys.** The lock is a loss of access, not of information: the ledger keeps every absorbed register with nonzero weight; only its recoverability — its norm in the accessible physical inner product — is forfeited. (Used again in CT4.7, CT4.8.)

---

### CT4.4 — The locked sector carries no gauge structure

**Thm.**
$$
D^-:\ \ \neg\exists\ \text{nonabelian gauge algebra};\qquad\neg\exists\ \text{abelian gauge algebra};\qquad
\text{contributes}\ \neg\text{generator to any accessible algebra}.
$$

**Req.** D3.2; CT0.11, CT0.12, CT0.13 (Part 1); CT3.20 (Part 2); CT4.2.

**Pf.**
$$
\text{gauge structure arises only from}:\ \ (a)\ \text{pair block};\quad (b)\ \text{slot algebras}\ \mathfrak u(n)
$$
$$
(a):\ \ \mathrm{CT0.12}:\ 16\ \text{pair directions fully allocated to}\ \{J^\pm,G,W,H,D^+\}\implies\neg\exists\ \text{direction left for}\ D^-
$$
$$
(b):\ \ \mathrm{CT3.20}/\mathrm{CT0.11}:\ \text{slot algebra realized only for}\ n\le3;\qquad
\mathrm{CT0.13}+\mathrm{D3.2}:\ \text{strictly new content at rungs}\ 2,3\ \text{allocated to}\ \{\mathrm{EM},\mathrm{strong}\}
$$
$$
n\ge4:\ \neg\text{channel-admissible}\implies\text{slot algebra}\ \neg\text{realized}
$$
$$
\implies F_{D^-}:\ \text{block disjoint from every gauge block}=\text{scalar sink},\ \neg\text{internal directions};\qquad
\mathrm{CT4.2}:\ \neg\text{probing by any accessible mask}.\ \blacksquare
$$

**Phys.** The dark sink is structureless: no charges, no generators, no self-interaction visible from the accessible side. That structurelessness is precisely what allows it to behave as a single simple fluid (CT4.5).

---

### CT4.4a — The realization domain of $\iota_n$: non-existence at $n\ge4$, persistence refuted

**Thm.** $(1)$ **Non-existence.** The aspect realization $\iota_n:\mathfrak u(n)\to\mathcal K$ of D2.12 exists exactly for $n\le3$:
$$n\ge4\implies D_{\mathrm{tick}}(n)=2^{n+1}\ge32>16=C_{\mathrm{cap}}\implies\neg\text{channel-admissible}\ [\mathrm{CT0.5},\ \mathrm{CT0.6},\ \mathrm{CT0.11}]\implies\text{the rung-}n\ \text{slot algebra is}\ \neg\text{realized}\ [\mathrm{CT4.4}\ \text{Pf clause (b), via CT3.20}]$$
and the locked sector receiving rung-$\ge4$ content carries no gauge structure — no generators, no internal directions [CT4.4; D4.1: $F_{D^-}$ a single possibility space; D4.2: absorption at rate $\propto O(n)$]. Hence the silence of D2.12 at $n\ge4$ is a non-existence consequence, $\neg$an underdetermination (scope note added at D2.12): the unique derived read of rung-$n\ge4$ slot content is $D^-$-absorption at the ledger level — locked, retained [CT4.3], never accessible [D1.11].
$(2)$ **No Lie-homomorphic substitute.** Any Lie-homomorphic map $\iota_n$, $n\ge4$, vanishes on $\mathfrak{su}(n)$: $\mathfrak{su}(n\ge4)$ is simple with $\dim=n^2-1\ge15$ [math]; block-wise realization semantics [D2.12, D3.2] require the isomorphism class to lie inside a single aspect block [CT0.12/CT0.13 tables]; the maximal aspect block dimension is $8$ [the $\mathfrak{su}(3)$ colour block; CT3.8] $<15$; the $J^\pm$ spans are $\neg$Lie-closed ($[J_i,J_j]=i\epsilon_{ijk}W_k\notin\operatorname{span}\{J\}$ [CT1.6, CT1.9]); the $H$, EM and $D^+$ blocks are $1$-dim abelian (a simple nonabelian algebra has no nonzero abelian homomorphic image [math]); the $G$ block has $\dim5<15$ [CT0.12]; the $D^-$ block: clause (1). The ambient commutator algebra $\mathfrak u(4)$ [CT1.9] contains an abstract $\mathfrak{su}(4)$, but no aspect block does, and the force sum of A8 has no $\mathfrak{su}(4)$ summand.
$(3)$ **Persistence refuted.** "Strong-hosting of $\mathfrak{su}(3)$ subalgebras at $n\ge4$" is impossible by (1)+(2). The activation persistence of CT0.13 at $n\ge4$ is *configuration-level*: three-slot sealing substructures remain available as data — attachments [D3.8], invariant contractions [CT3.17], the completeness projector [D2.14] — not as $\iota$-images. **Hosting dies at rung 3; sealing persists at every rung.**

**Req.** A8; D1.11, D2.12, D3.2, D3.8, D4.1, D4.2; CT0.5, CT0.6, CT0.11, CT0.12, CT0.13, CT1.6, CT1.9 (Part 1); CT3.8, CT3.17, CT3.20 (Part 2); CT4.2, CT4.3, CT4.4; dimension arithmetic, simplicity of $\mathfrak{su}(n\ge4)$, the classification of low-dimensional simple algebras [math; machine: `checks/verify_merge_tierA.py` §C].

**Pf.**
$$(1):\ \mathrm{CT0.5}:\ D_{\mathrm{tick}}(n)=2^{n+1};\quad \mathrm{CT0.6}:\ C_{\mathrm{cap}}=16;\quad n\ge4:\ 2^{n+1}\ge32>16\implies O(n)=2^{n+1}-16>0\ [\mathrm{CT4.1}]\implies\text{locked}\ [\mathrm{CT4.2}/\mathrm{CT4.3}]$$
$$\mathrm{CT4.4}:\ F_{D^-}\ \text{contributes}\ \neg\text{generator to any accessible algebra};\qquad \mathrm{CT3.20}:\ N=3\ \text{forced at the accessible rungs}\implies\neg\exists\ \mathfrak{su}(n\ge4)\ \text{aspect block}$$
$$(2):\ \dim\mathfrak{su}(n)=n^2-1\ge15\ (n\ge4)\ [\text{math}];\qquad \text{aspect block dimensions}\ \{3,3,5,3,1,1\}\ [\mathrm{CT0.12}]\ \cup\ \{8\}\ [\mathrm{CT3.8}]\implies\max=8<15\implies\neg\exists\ \text{injective block homomorphism}$$
$$[J_1,J_2]=iW_3\notin\operatorname{span}\{J_i\}\ [\mathrm{CT1.6};\ \text{machine over}\ \mathbb Q(i)]\implies J\text{-spans}\ \neg\text{Lie-closed};\qquad \dim1\ \text{blocks abelian}\implies\text{simple nonabelian image}=0\ [\text{math}]$$
$$(3):\ \text{by (1)+(2): no hosted image at}\ n\ge4;\qquad \mathrm{CT0.13}:\ \mathcal A(n\ge4)\ \text{is defined by activation/absorption data},\ \neg\text{by}\ \iota_n\text{-images}.\ \blacksquare$$

**Phys.** The gauge ladder has a hard derived ceiling: nothing above colour ever hosts — no hidden $\mathfrak{su}(4)$, no grand-unification block waiting at high rung. Oversubscribed content is absorbed without structure, and what survives as "colour persists at $n\ge4$" is the sealing *grammar* (which configurations are admissible), never the Lie algebra.

**Rmk (positive side, $n\le3$).** From the same frozen sources: the centre of $\mathfrak u(n)$ maps to $\mathcal K^{(\mathrm{EM})}$ [D2.12]; at $n(w)=2$: $\mathfrak{su}(2)$ hosts into $\operatorname{span}\{W_i\}$ — the $W_i$ close $\mathfrak{su}(2)$ [CT1.4]; at $n(w)=3$: $\mathfrak{su}(3)$ hosts onto $\mathcal K^{(\mathrm{strong})}$ with $8=8$ [D2.12, CT3.7, CT3.8]; the exchange generators host *literally* as matrix units ($\tfrac12(\lambda_1+i\lambda_2)=E_{12}$ and cyclic [CT3.9's basis; machine: `checks/verify_merge_tierB.py` §G]). The hosting ceiling is therefore exact: nontrivial hosting $\iff$ contact exchange degree $\le3$ (the explicit-realization vocabulary stays outside the frozen corpus).

---

## §G.II — The Two Dark Aspects

### CT4.5 — Equation of state of the locked sector

**Thm.**
$$
T^{(D^-)}_{\mu\nu}=\rho_{D^-}\,u_\mu u_\nu;\qquad
p_{D^-}=0;\qquad
w_{D^-}=\frac{p}{\rho}=0;\qquad
\rho_{D^-}\ge0\ \ \bigl(=0\iff\neg\exists v:\ n(v)\ge4\bigr).
$$

**Req.** D1.5; CT1.22, CT1.23 (Part 2); CT4.1, CT4.2, CT4.3.

**Pf.**
$$
\mathrm{CT1.22}:\ \ T=T^{\mathrm{bd}}+T^{\mathrm{tr}}\quad[\text{channels of}\ \mathrm{D1.5}]
$$
$$
T^{\mathrm{tr}}\ \text{requires propagating chain with connection}\ [\mathrm{CT1.22}];\qquad
\mathrm{CT4.2}:\ \text{locked}:\ \neg\text{accessible pole}\implies\neg\text{propagating mode}\implies\mathsf E_{\mathrm{tr}}=0\implies T^{\mathrm{tr}}=0
$$
$$
\implies T^{(D^-)}=T^{\mathrm{bd}}=(\rho+p)u_\mu u_\nu+p\,g_{\mu\nu}\quad[\mathrm{CT1.22};\ u^\mu=\text{rest frame of the locked cell}]
$$
$$
p=\text{spatial momentum flux in rest frame};\quad\neg\text{propagation}\implies\text{flux}\equiv0\implies p_{D^-}=0\implies T^{(D^-)}_{\mu\nu}=\rho_{D^-}u_\mu u_\nu;\qquad w=0/\rho=0
$$
$$
\rho_{D^-}=\text{absorbed registers per volume}=\textstyle\sum O(n)\ge0\ [\mathrm{CT4.1}];\qquad
\mathrm{CT4.3}:\ \neg\text{removal}\implies\rho_{D^-}\ge0;\quad=0\iff\neg\exists v:\ n(v)\ge4.\ \blacksquare
$$

**Phys.** Locked content gravitates as pressureless dust: no propagation, no momentum flux, $w=0$ — derived, not fitted. It couples to geometry through the field equations CT1.23 and through nothing else. Contrast with $D^+$: $w=-1$ (CT1.25, CT4.6).

---

### CT4.5a — The flicker-dust ensemble: exact density polynomial and rate-invariant $w=0$

**Thm.** Hypotheses (ensemble scope, stated): $\Gamma$ a finite skeleton [A7] with potential degrees $n(v)$; every potential edge crystallizes independently with common probability $p\in[0,1]$ (a per-edge Bernoulli ensemble; the *dynamics* realizing such an ensemble is not declared in Parts 1–2 — Merge note). Then:
$(1)$ **Exact dust density.** $k_v\sim\mathrm{Bin}(n(v),p)$, and with $f_{\mathrm{adm}}(n,p):=\sum_{k\le3}\binom{n}{k}p^k(1-p)^{n-k}$ [CT0.11: admissible $\iff k\le3$], $O(n):=\max(0,\,2^{n+1}-16)$ [CT4.1, CT0.6]:
$$\langle\rho_{D^-}\rangle_\Gamma(p)=\sum_v O(n_v)\,\bigl(1-f_{\mathrm{adm}}(n_v,p)\bigr)$$
— an exact polynomial in $p$ with **integer coefficients** [CT4.5's source criterion $\rho_{D^-}>0\iff\exists v:\ k_v\ge4$, read in expectation].
$(2)$ **Anchors.** $\langle\rho\rangle_\Gamma(1)=\sum_vO(n_v)$ — Platonic values $(448,\ 896,\ 2976,\ 2240,\ 24384)$ for (tetra, cube, octa, dodeca, icosa) [$(V,\deg)=(4,3),(8,3),(6,4),(20,3),(12,5)$; math]; at $p=\tfrac12$: $\bigl(154,\ 308,\ \tfrac{15159}{8},\ 770,\ 20193\bigr)$; the polygon family $P_n$ ($n\ge3$, $\deg=2$): the exact monomial $16\,n\,p^4$; the digon identically $0$ ($k=2$ never locks [CT0.6: $O(2)=0$]); $\langle\rho\rangle_\Gamma(0)=0$; strict increase on $(0,1)$ for every lockable $\Gamma$ ($\exists v:\ n(v)\ge4$).
$(3)$ **The flicker modulates $\rho$, never $w$.** CT4.5 applies per configuration: every locked vertex contributes pressureless dust ($w=0$, source side, coupled to geometry through CT1.23 and nothing else). A mixture of $w=0$ components is $w=0$ on the locked part at every $p$ [CT1.22's linearity in the source]; $D^+$'s $w=-1$ [CT1.25, D4.3] is configuration-independent and untouched — CT4.6's contrast table holds ensemble-wise term by term.
$(4)$ **No fluid.** The locked sector supports no further equation-of-state data: a structureless absorbing sink — one possibility space [D4.1], no gauge content [CT4.4], absorption one-way [CT4.2], content retained-and-inaccessible [CT4.3, D1.11]. Statements assigning $D^-$ a pressure response, polarization, or re-emission have no defined ledger referent (the referent would contradict CT4.2/D1.11); "the vacuum is a $D^-$ fluid" is inadmissible as stated. What is derived: locked content gravitates as dust, with the density computed here.

**Req.** Hypotheses (stated above); A7; D1.11, D4.1, D4.2, D4.3; CT0.6, CT0.11 (Part 1); CT1.22, CT1.23, CT1.25 (Part 2); CT4.1, CT4.2, CT4.3, CT4.4, CT4.5, CT4.6; binomial law under per-edge independence, exact polynomial arithmetic [math; machine: `checks/verify_merge_tierB.py` §E].

**Pf.**
$$(1):\ \text{locked}\iff k_v\ge4\ [\mathrm{CT4.5}\ \text{iff};\ \mathrm{CT0.11}:\ \text{admissible}\iff k\le3];\quad \mu_p(k_v\ge4)=1-f_{\mathrm{adm}}(n_v,p)\ [\mathrm{Bin}(n_v,p),\ \text{hypothesis}];\quad \bigl\langle\textstyle\sum_v O(n_v)\mathbf 1_{k_v\ge4}\bigr\rangle=\sum_v O(n_v)(1-f_{\mathrm{adm}})\ [\text{linearity};\ \mathrm{CT4.5}]$$
$$\text{integer coefficients}:\ O(n)\in\mathbb Z\ [\mathrm{CT4.1}]\ \wedge\ \binom{n}{k}\in\mathbb Z\implies(1-f_{\mathrm{adm}})\ \text{expands with}\ \mathbb Z\text{-coefficients}$$
$$(2):\ p{=}1:\ 1-f_{\mathrm{adm}}(n,1)=\mathbf 1_{n\ge4};\quad O(2d)=(16,112,496,2032)\ \text{at}\ 2d=(4,6,8,10)\ [\mathrm{CT4.1}]$$
$$\text{Platonic sums}:\ (4\cdot112,\ 8\cdot112,\ 6\cdot496,\ 20\cdot112,\ 12\cdot2032)=(448,896,2976,2240,24384)\ [\text{machine}]$$
$$p=\tfrac12:\ \text{exact binomial evaluation}\ [\text{machine}];\qquad P_n:\ n(v)=4\ \forall v\implies1-f_{\mathrm{adm}}(4,p)=p^4\implies\textstyle\sum_v16\,p^4=16np^4;\qquad\text{digon}:\ O(2)=0$$
$$\text{monotonicity}:\ \tfrac{d}{dp}P(\mathrm{Bin}(n,p)\ge4)>0\ \text{on}\ (0,1)\ \text{for}\ n\ge4\ [\text{math};\ \text{machine on the rational grid}]$$
$$(3):\ w=0\ \text{per configuration}\ [\mathrm{CT4.5}];\quad \langle T_{\mu\nu}\rangle=\textstyle\sum_c\mu(c)\,T_{\mu\nu}(c)\ [\mathrm{CT1.22}]:\ p_{\mathrm{eff}}=\sum_c\mu_c\cdot0=0\ \text{on the locked part};\quad \mathrm{CT1.25}/\mathrm{D4.3}:\ D^+\ \text{constant}$$
$$(4):\ \text{the cited tags exhaust the}\ D^-\ \text{inventory};\quad \mathrm{CT4.2}:\ \text{one-way};\quad \mathrm{D1.11}:\ \text{inaccessible}\implies\neg\exists\ \text{response read}.\ \blacksquare$$

**Phys.** Shake a crystal at any rate and its dark content has an exact polynomial density — integer coefficients, closed form, every Platonic and polygon anchor reproduced — and its equation of state never moves: dust at every rate. What the flicker changes is *how much* content is locked, never *what locked content does*. And what locked content does is fixed: it gravitates, it absorbs, it does not respond.

---

### CT4.6 — The two dark aspects contrasted

**Thm.**
$$
\begin{array}{c|c|c}
& D^+ & D^-\\ \hline
\text{definition} & F_{D^+}=\Lambda\,\mathbb I\ [\mathrm{D4.3}] & F_{D^-}=\bigoplus_{n\ge4}F_n\ [\mathrm{D4.1}]\\
\text{block} & \text{central pair direction}\ E_0\ [\mathrm{CT0.12}] & \text{stack block}\perp\text{pair space}\ [\mathrm{CT0.12\ Rmk}]\\
\text{activation} & n=1\ [\mathrm{CT0.13}] & n\ge4\ [\mathrm{CT0.13}]\\
\text{config.\ dependence} & \text{none}\ [\mathrm{D4.3}] & \text{full}\ [\mathrm{CT4.1}]\\
\text{rest frame} & \text{none; isotropic}\ [\mathrm{CT1.25}] & \text{one per locked cell}\ [\mathrm{CT4.5}]\\
\text{equation of state} & w=-1\ [\mathrm{CT1.25}] & w=0\ [\mathrm{CT4.5}]\\
\text{gauge content} & \text{none; central}\ [\mathrm{CT1.3}] & \text{none; disjoint}\ [\mathrm{CT4.4}]\\
\text{entropy} & \text{none}\ [\mathrm{CT4.7}] & \text{maximal, locked}\ [\mathrm{CT4.7}]
\end{array}
$$
$$
\forall\ \text{rows differ}\implies D^+\ne D^-\ (\neg\text{two descriptions of one thing});
$$
$$
\mathrm{CT1.23}:\ D^+\ \text{geometric side}\ (\Lambda g_{\mu\nu});\quad D^-\ \text{source side}\ (\rho_{D^-}u_\mu u_\nu);\qquad\neg\text{double counting}\ [\mathrm{CT1.22}].
$$

**Req.** D4.1, D4.3; CT0.12, CT0.13, CT1.3 (Part 1); CT1.22, CT1.23, CT1.25 (Part 2); CT4.1, CT4.4, CT4.5, CT4.7.

**Pf.** Each cell $=$ cited tag; rows differ pointwise; distinct entry into CT1.23 with no double count [CT1.22 step 5]. $\blacksquare$

**Phys.** The corpus’s two dark aspects differ on every structural axis: one is uniform cosmological tension on the geometric side ($w=-1$), the other is oversubscribed ledger sediment on the source side ($w=0$). “Dark” names an observational status, not a shared nature.

---

### CT4.7 — The entropy triangle

**Thm.** In the plane $\bigl(S_{\mathrm{raw}},\ S_{\mathfrak L}\bigr)$ with $S_{\mathrm{raw}}(\rho)=-\mathfrak T(\rho\log\rho)$ [D0.3] and $S_{\mathfrak L}=n_{\mathcal R}\ln2$ [CT1.29], there are exactly three scalar extremes, mutually exclusive:
$$
(1)\ \ \text{Janus vacuum}:\ n_{\mathcal R}=0:\quad\bigl(S_{\mathrm{raw}},S_{\mathfrak L}\bigr)=\bigl(\ln4\ \text{per pair (max)},\ 0\bigr);
$$
$$
(2)\ \ D^+:\ \text{one configuration}:\quad(0,\ 0)\qquad(\ln1=0;\ \neg\text{real edges});
$$
$$
(3)\ \ D^-:\ \text{locked}:\quad\bigl(\min_{\mathrm{acc}},\ \max\ \wedge\ \neg\text{accessible}\bigr).
$$

**Req.** A4; D0.3, D4.3; CT0.1, CT0.2, CT0.8 (Part 1); CT1.29 (Part 2); CT4.1, CT4.3, CT4.9.

**Pf.**
$$
\text{two independent measures}:\ \ S_{\mathrm{raw}}=\text{pair mixedness}\ [\mathrm{D0.3}];\quad S_{\mathfrak L}=\text{registered real edges}\ [\mathrm{CT1.29}]
$$
$$
(1):\ \ \mathrm{CT0.2}:\ n_{\mathcal R}=0\implies\rho=\rho_\circ=I/4,\ \ S_{\mathrm{raw}}=\ln4=\max\ (d=4);\qquad S_{\mathfrak L}=0\cdot\ln2=0
$$
$$
(2):\ \ \mathrm{D4.3}:\ \text{single direction, single value}\ \Lambda\implies\ln1=0;\qquad\neg\text{own real edges}\implies S_{\mathfrak L}\text{-contribution}=0
$$
$$
(3):\ \ \mathrm{CT4.1}:\ \text{locked vertex carries}\ 2^{n+1}>16\ \text{registers};\quad\mathrm{CT4.3}:\ \neg\text{deletion}\implies S_{\mathfrak L}^{\text{locked}}>\text{accessible bound}\ [\mathrm{CT4.9}],\ \ \to\infty\ \text{in}\ n
$$
$$
\mathrm{CT0.1}+\mathrm{A4}:\ \text{interior pairs crystallized};\quad
\mathrm{CT0.8}\ (\varepsilon_q=0):\ \operatorname{supp}\rho\subseteq\vee^2\implies S_{\mathrm{raw}}\le\ln3<\ln4:\ \min_{\mathrm{acc}}
$$
$$
\text{exclusivity}:\ \ (n_{\mathcal R}=0)\ \wedge\ (\exists v:\ n\ge4)\ \text{contradictory};\qquad D^+:\ \neg\text{configuration dependence at all}.\ \blacksquare
$$

**Phys.** The scalar landscape is a triangle in the (pair-entropy, ledger-entropy) plane: the vacuum at (max, 0), $D^+$ at (0, 0), $D^-$ at (min, max-and-hidden). Three distinct ways of being featureless — and by CT4.10, no fourth.

---

### CT4.7a — The vacuum census, closed, and the baseline equality

**Thm.** $(1)$ **The complete census.** The three scalar extremes of CT4.7, with CT4.10's exhaustiveness, are the complete inventory of vacuum-type scalar reads, mutually exclusive:
$$\begin{array}{c|cc|l}
& S_{\mathrm{raw}} & S_{\mathfrak L} & \text{structure}\\ \hline
\text{Janus vacuum}\ (n_{\mathcal R}=0) & \ln4\ \text{per pair (max, argmax unique}\ \tfrac14I) & 0 & [\mathrm{CT0.2},\ \mathrm{A5},\ \mathrm{D0.3};\ \mathrm{CT4.7}(1)]\\
D^+ & 0 & 0 & \text{pure, uniform, configuration-blind};\ w=-1\ [\mathrm{D4.3},\ \mathrm{CT1.25};\ \mathrm{CT4.7}(2)]\\
D^-\ \text{locked} & \min_{\mathrm{acc}} & \max\ \wedge\ \neg\text{accessible} & [\mathrm{CT4.2},\ \mathrm{CT4.3},\ \mathrm{D1.11};\ \mathrm{CT4.7}(3)]
\end{array}$$
$\neg\exists$ a fourth extreme [CT4.10]; $F_H$ is a dynamical field, $\neg$an extreme [EW.27].
$(2)$ **Baseline equality.** For every finite skeleton $S$ [A7], let $\mathrm{VV}(S):=$ the all-virtual state on its potential-edge set ($n_{\mathcal R}=0$, every pair at $\rho_\circ=\tfrac14I$ [A5, CT0.2]) and $V_{\mathrm{raw}}:=$ the global vacuum [CT0.2]. Then every constructible vacuum read coincides:
$$S_{\mathfrak L}(\mathrm{VV}(S))=n_{\mathcal R}\ln2=0=S_{\mathfrak L}(V_{\mathrm{raw}})\ [\mathrm{CT1.29}];\qquad \Delta S_{\mathrm{raw}}=0\ \text{on both sides}\ [\mathrm{CT0.2}:\ \text{every pair at the unique argmax}]$$
$$\rho_{D^-}=0\ \text{on both sides}\ [\mathrm{CT4.5}\ \text{iff}:\ \neg\exists v:\ k_v\ge4];\qquad S_{\partial\mathcal B}\ \text{has no argument on either side}\ (\neg\exists\ \text{closed real-edge surface}\ [\mathrm{CT1.29}\ \text{domain}])$$
hence the vacuum-polarization deficit vanishes identically: $\Delta S_{\text{vac-pol}}(S)\equiv0\ \forall S$. The reason is registration, $\neg$arithmetic: virtual edges carry no registration — $\phi_e/\sigma_e$ are defined on $E_{\mathcal R}$ only [A7, D0.5], and the sole ledger exclusion is the Haar draw [A5: $U\notin\mathfrak L$].
$(3)$ **Honest scope.** The *absolute* raw entropy $|\mathrm{pairs}|\cdot\ln4$ is shape-dependent; every constructible *deficit* and read-difference is shape-independent and zero. No particle or cosmological identification [P5].

**Req.** A4, A5, A7; D0.3, D0.5, D1.11, D4.3; CT0.1, CT0.2, CT0.8 (Part 1); CT1.25, CT1.29 (Part 2); EW.27 (Part 2); CT4.1, CT4.2, CT4.3, CT4.5, CT4.7, CT4.9, CT4.10; exact arithmetic [math; machine: `checks/verify_merge_tierA.py` §D].

**Pf.**
$$(1):\ \mathrm{CT4.7}\ \text{rows verbatim};\qquad \mathrm{CT4.10}:\ \{\text{rotation-scalar directions}\}=\{E_0\to F_{D^+},\ \Sigma\to F_H,\ \text{vacuum configuration},\ D^-\ \text{sink}\};\quad F_H\ \neg\text{extreme}\ [\mathrm{EW.27}]$$
$$(2):\ n_{\mathcal R}=0\implies S_{\mathfrak L}=n_{\mathcal R}\ln2=0\ [\mathrm{CT1.29}];\qquad \text{every pair at}\ \rho_\circ=\tfrac14I\ [\mathrm{A5}]:\ S_{\mathrm{raw}}=\ln4\ \text{per pair}=\max,\ \text{argmax unique}\ [\mathrm{CT0.2},\ \mathrm{D0.3}]\implies\Delta S_{\mathrm{raw}}=0$$
$$k_v=0<4\ \forall v\implies\rho_{D^-}=0\ [\mathrm{CT4.5}\ \text{iff}];\qquad E_{\mathcal R}=\varnothing\implies\neg\exists\ \partial\mathcal B\implies S_{\partial\mathcal B}\ \text{undefined}$$
$$U\notin\mathfrak L\ [\mathrm{A5}]:\ \text{Haar draws leave no ledger record}\implies\text{all-virtual states are ledger-indistinguishable from}\ V_{\mathrm{raw}}\ \text{on every}\ n_{\mathcal R}\text{-based read}.\ \blacksquare$$

**Phys.** The vacuum ledger is closed: exactly three scalar ways to be empty, and every constructible read agrees across all of them — an all-virtual skeleton reads identically to the bare vacuum, shape by shape, because virtual edges were never registered at all. Raw entropy knows the shape; no constructible read consults it.

---

### CT4.10 — The triangle is exhaustive

**Thm.**
$$
\neg\exists\ \text{fourth scalar extreme}:\qquad
\{\text{rotation-scalar directions of the corpus}\}=\{E_0\to F_{D^+},\ \ \Sigma\to F_H,\ \ \text{vacuum configuration},\ \ D^-\ \text{sink}\};
$$
$$
F_H\ \neg\text{extreme}\ (\text{dynamical field}).
$$

**Req.** CT0.2, CT0.12, CT1.2, CT1.10, CT1.11 (Part 1); EW.27 (Part 2); CT3.7 (Part 2); CT4.4.

**Pf.**
$$
\mathrm{CT1.10}:\ \ \mathcal E_{++}\to\mathbf1\oplus\mathbf5\oplus\mathbf1\implies\text{pair-space rotation scalars}=\{E_0,\ \Sigma\}\ \text{exactly}
$$
$$
\mathrm{CT1.11}:\ E_0\nparallel\Sigma;\qquad\mathrm{CT0.12}:\ E_0\mapsto F_{D^+},\ \ \Sigma\mapsto F_H
$$
$$
\mathrm{EW.27}:\ F_H:\ \text{stable stationary background}+\text{massive excitation}\implies\text{dynamical field},\ \neg\text{limiting configuration}
$$
$$
\mathrm{CT1.2}:\ J,\ W,\ G\ \text{carry spatial indices}\implies\neg\text{scalars}
$$
$$
\mathrm{CT4.4}:\ D^-\ \text{supplies}\ \neg\text{generator};\qquad
\mathrm{CT3.7}:\ \mathfrak T(T_a)=0\implies\text{colour}\ \neg\text{scalar direction};\qquad
\text{abelian}=\text{centre, counted}
$$
$$
\text{vacuum corner}=n_{\mathcal R}=0\ \text{configuration}\ (\neg\text{generator}),\ \ \text{unique}\ [\mathrm{CT0.2}]
$$
$$
\implies\{\text{vacuum},\ D^+,\ D^-\}\ \text{complete}.\ \blacksquare
$$

**Phys.** No fourth scalar extreme exists: the operator content of the corpus offers exactly two rotation scalars (one spent on $D^+$, one dynamical as $F_H$), the vacuum is a unique configuration, and the sink is unique by construction. The entropy triangle closes.

---

## §G.III — Bounds and Boundaries

### CT4.9 — Accessible entropy bounds

**Thm.**
$$
(1)\ \ \text{per vertex}:\quad\text{accessible}(v)\implies S(v)\le3\ln2\ \ \text{nats}=3\ \ \text{bits}\qquad(\text{attained at}\ n=3);
$$
$$
(2)\ \ \text{per region}\ \mathcal B,\ \partial\mathcal B\ \text{closed real-edge surface of area}\ A:\quad
S_{\mathrm{acc}}(\mathcal B)\le\frac{A}{\mathfrak h^2}\ \ \text{bits}=\frac{A}{\mathfrak h^2}\ln2\ \ \text{nats}.
$$

**Req.** A2; D0.8, D1.9, D4.2; CT0.9, CT0.11 (Part 1); CT1.29 (Part 2); CT4.1.

**Pf.**
$$
(1):\ \ \mathrm{CT0.11}:\ n\le3\implies\bigl|\{e\in E_{\mathcal R}:e\ni v\}\bigr|\le3\ [\mathrm{D0.8}];\qquad
\mathrm{CT0.9}:\ 1\ \text{bit/edge}\implies2^3\ \text{configs}\implies S\le3\ln2;\quad n=3:\ \text{attained}
$$
$$
(2):\ \ \mathrm{CT1.29}:\ n_{\mathcal R}(\partial\mathcal B)=A/\mathfrak h^2;\quad S_{\partial\mathcal B}=n_{\mathcal R}(\partial\mathcal B)\ln2
$$
$$
\mathrm{A2}+\mathrm{D1.9}:\ \text{ticks local};\ \text{registers cross only boundary edges}\implies S_{\mathrm{acc}}(\mathcal B)\le\text{boundary register count}
$$
$$
\mathrm{CT4.1}+\mathrm{D4.2}:\ \text{interior excess}\implies\text{oversubscribed}\implies\text{locked}\implies\neg\text{contributing}.\ \blacksquare
$$

**Phys.** Accessible information is bounded twice over: three bits at any vertex, one bit per hop-area of any bounding surface — a holographic-type bound whose coefficient is exactly $\ln2$, derived from channel capacity alone.

---

### CT4.8 — Locked regions and their boundaries

**Thm.** Interior locked in $D^-$, boundary $\partial\mathcal B$ of area $A$:
$$
S_{\partial\mathcal B}=\frac{A}{\mathfrak h^2}\ln2\quad\Bigl(=\frac{A}{4G_N}\ [\mathrm{CT2.9}\ \text{naming}]\Bigr);
$$
$$
\text{exterior measurements}=\text{residues of the accessible resolvent}\ [\mathrm{CT2.5}]:\quad
\text{equal boundary register counts}\implies\text{indistinguishable interiors};
$$
$$
\neg\exists\ \text{accessible interior singularity}\ [\mathrm{CT1.28}].
$$

**Req.** CT1.28, CT1.29, CT2.5, CT2.9 (Part 2); CT4.1, CT4.2, CT4.3, CT4.9.

**Pf.**
$$
\mathrm{CT4.2}:\ \text{locked}:\ \neg\text{accessible pole};\qquad
\mathrm{CT2.5}:\ \text{exterior measurement}=\text{residue of accessible resolvent}\implies\neg\exists\ \text{direct interior signal}
$$
$$
\mathrm{CT4.9}\ \text{step}(2):\ \text{accessible registers of}\ \mathcal B=\text{boundary edges only};\qquad
\mathrm{CT1.29}:\ S_{\partial\mathcal B}=\frac{A}{\mathfrak h^2}\ln2
$$
$$
\text{equal boundary content}\implies\text{equal accessible data}\implies\text{interiors indistinguishable}
$$
$$
\mathrm{CT1.28}:\ \text{accessible rung}\le3\implies\neg\text{accessible curvature singularity};\qquad
\mathrm{CT4.1}:\ \text{would-be divergence transferred to}\ D^-;\qquad
\mathrm{CT2.9}:\ \tfrac{A}{\mathfrak h^2}\ln2=\tfrac{A}{4G_N}.\ \blacksquare
$$

**Phys.** A locked region is characterized, for the exterior, by its boundary area alone: exact boundary entropy, indistinguishable interiors, no interior singularity. The corpus’s black-hole-type statement — derived from masks and capacity, with the quarter-area form supplied by the CT2.9 calibration.

---

### CT4.11 — Global closure

**Thm.** With $\ \mathbf F_\oplus=\bigoplus_{\text{all aspects}}F_A$ and $M_\oplus=\bigoplus_n\mathcal P_M^{(n)}$:
$$
Z\bigl[\mathbf F_\oplus,M_\oplus\bigr]\ \ \text{well defined};\qquad
\mathfrak S\bigl(Z[\mathbf F_\oplus,M_\oplus]\bigr)\ne\varnothing\qquad(\text{the object of A9 exists}).
$$

**Req.** A2, A8, A9; C12; D0.10, D2.8, D4.1; CT0.2, CT0.12, CT0.13, CT0.14 (Part 1); CT2.2, CT2.5, CT2.8 (Part 2); CT4.2.

**Pf.**
$$
\text{domain}:\ \ Z\ \text{sums over}\ \mathfrak C(\mathcal R)\ [\mathrm{D0.10},\ \mathrm{C12}]
$$
$$
\text{aspects}:\ \ \mathrm{CT0.12}:\ \text{pair}\ 16=\{J^\pm,G,W,H,D^+\};\quad\mathrm{CT0.13}:\ \text{stack}=\{\mathrm{EM},\mathrm{strong},D^-\}\implies\text{exactly the A8 list}\ (\neg\text{undefined},\ \neg\text{twice})
$$
$$
\text{masks}:\ \ \mathrm{CT2.2}:\ \mathcal P_M^{(n)}\ \text{Hermitian idempotents};\quad\mathrm{CT0.14}:\ \text{strict flag},\ \dim=(6,16,17,25)<\infty
$$
$$
\text{convergence}:\ \ \mathrm{D2.8}:\ \text{convergent sheet};\quad
\mathrm{CT2.5}:\ \text{resolvent finite off poles}\ (\dim\mathcal K_n<\infty);\quad
\mathrm{CT2.8}:\ \text{reflected sum}=\sum|w|^2\ge0,\ \text{finite for square-summable halves}
$$
$$
\text{residual divergence}:\ \ \bigoplus_{n\ge4}F_n\ \text{collected into}\ D^-\ [\mathrm{D4.1}];\quad
\mathrm{CT4.2}:\ D^-\perp\forall\ \text{accessible mask}\implies\text{accessible part of}\ Z=\text{finite blocks only}
$$
$$
\text{nonemptiness}:\ \ \mathrm{CT0.2}:\ \text{global vacuum}\ (n_{\mathcal R}=0,\ \forall\ \text{pairs virtual},\ \mathcal A(0)=\{J\})\ \text{satisfies every axiom}\implies\in\mathfrak S\implies\mathfrak S\ne\varnothing.\ \blacksquare
$$

**Phys.** The total masked partition function named by A9 is well defined — every aspect accounted for exactly once, every mask a finite projection, every sum on the convergent sheet, the infinite tower sealed inside $D^-$ — and its solution set contains at least the empty universe. The falsifiability axiom has mathematical content.

---

## §G.IV — Falsifiability and the Closure Audit

### CT4.12 — Falsifiers

**Thm.** Observation of any row $\implies\neg(\mathrm{A1}\wedge\cdots\wedge\mathrm{A9})$ [A9 contrapositive; each row negates a derived parameter-free statement]:
$$
\begin{array}{c|c}
\text{falsifier} & \text{contradicted tag}\\ \hline
\text{4th accessible slot index}\ (\text{colour algebra}\supsetneq\mathfrak{su}(3)) & \mathrm{CT3.20},\ \mathrm{CT0.11}\\
N_{\mathrm{gluon}}\ne8 & \mathrm{CT3.13}\\
\text{isolated unsealed colour charge} & \mathrm{CT3.18},\ \mathrm{CT3.22}\\
q\notin\{-1,0,+1\} & \mathrm{EM.9},\ \mathrm{EM.10},\ \mathrm{EW.36}\\
m_\gamma\ne0\ \ \vee\ \ N_{\mathrm{pol}}\ne2 & \mathrm{EM.6},\ \mathrm{EM.8}\\
m_W\ne m_Z\cos\theta_W\ \ (\rho\ne1) & \mathrm{EW.34}\\
e\ne g\sin\theta_W & \mathrm{EW.35}\\
\text{uniform vacuum aspect with}\ w\ne-1 & \mathrm{CT1.25}\\
\text{locked non-propagating component with}\ w\ne0 & \mathrm{CT4.5}\\
S_{\partial\mathcal B}\not\propto A\ \ \vee\ \ \text{coefficient}\ne\ln2\ \text{per hop area} & \mathrm{CT1.29}\\
\text{local higher-curvature corrections in}\ D=4 & \mathrm{CT2.7}\\
\nabla^\mu T_{\mu\nu}\ne0\ (\Lambda=\mathrm{const}) & \mathrm{CT1.24},\ \mathrm{CT1.26}\\
\text{accessible curvature singularity} & \mathrm{CT1.28}\\
S_{\mathrm{acc}}>1\ \text{bit per hop area of bounding surface} & \mathrm{CT4.9}
\end{array}
$$
**Rmk ($\neg$falsifiers).** Measured values of $g,\ g',\ \theta_W,\ e,\ h_0,\ \Lambda,\ m_W,\ m_Z,\ m_H,\ \mathfrak h$: configuration/calibration data [P1, P4] — $\neg$falsifying alone; only relations among them falsify. Falsifier rows resting on EM.20 inherit its derived phase alphabet $\alpha_e\in\{0,\pi\}$ [EM.20(1)]; no extra-axiomatic input enters there [A §0.2a].

**Req.** A9; P1, P4; all cited tags.

**Pf.**
$$
\forall\ \text{rows}:\ \text{cited tag}=\text{theorem proved without free parameters}
$$
$$
\text{inspection of cited proofs}:\ \ \neg\exists\ \mathfrak h\text{-dependence surviving}\ (\text{entropy rows fix the coefficient},\ \neg\text{the scale});\quad\neg\exists\ \mathrm{P4}\ \text{data used}
$$
$$
\text{parameter-free derived statement}\ \vdash\ \mathrm{A1}\wedge\cdots\wedge\mathrm{A9}\implies\text{its negation}\implies\neg(\mathrm{A1}\wedge\cdots\wedge\mathrm{A9})\quad[\mathrm{A9}\ \text{contrapositive}].\ \blacksquare
$$

**Phys.** The corpus is falsifiable in the strict sense: fourteen crisp observation types, any single one of which demolishes the axiom set. Magnitudes never falsify — only relations and structures do. That asymmetry is deliberate and stated.

---

### CT4.13 — Closure audit

**Thm.** Every quantity of the corpus lies in exactly one of three categories; the categorization is complete:

$$(\mathbf{I})\ \ \text{derived parameter-free data}\ (\neg\text{freedom},\ \neg\mathfrak h\text{-dependence};\ \text{numbers and constraints}):$$
$$
(7,3,3,3)\ [\mathrm{CT1.1}];\quad C_{\mathrm{cap}}=16\ [\mathrm{CT0.6}];\quad D_{\mathrm{tick}}(n)=2^{n+1}\ [\mathrm{CT0.5}];\quad n\le3\ [\mathrm{CT0.11}];\quad N_{\text{colour}}=3\ [\mathrm{CT3.20}];\quad N_{\mathrm{gluon}}=8\ [\mathrm{CT3.13}];
$$
$$
N_{\mathrm{pol}}=2\ [\mathrm{EM.8}];\quad q\in\{-1,0,+1\}\ [\mathrm{EM.9},\mathrm{EW.36}];\quad\alpha_e\in\{0,\pi\}\ \text{per edge}\ [\mathrm{EM.20}];\quad\rho=1\ [\mathrm{EW.34}];
$$
$$
w_{D^+}=-1\ [\mathrm{CT1.25}];\quad w_{D^-}=0\ [\mathrm{CT4.5}];\quad S=n_{\mathcal R}\ln2\ [\mathrm{CT1.29}];\quad f_{abc}\ [\mathrm{CT3.21}];\quad\mathfrak T(\mathcal G_A\mathcal G_B)=\tfrac12\delta_{AB}\ [\mathrm{EW.32},\mathrm{CT3.9}];
$$
$$
\text{derived constraint}\ (\text{interval; sharp point}\ 0;\ \neg\exists\ \text{theorem depending on the value within it}):\quad\varepsilon_q\in[0,\tfrac14)\ [\mathrm{CT0.8}];
$$
$$(\mathbf{II})\ \ \text{named combinations of}\ \mathfrak h\ (\text{external comparison only}):\qquad
G_N=\frac{\mathfrak h^2}{4\ln2};\quad\kappa^2=8\pi G_N=\frac{2\pi\,\mathfrak h^2}{\ln2}\qquad[\mathrm{CT2.9};\ \neg\exists\ \text{further dimensionful freedom}:\ \mathrm{CT2.11}];
$$
$$(\mathbf{IIIa})\ \ \text{configuration data --- independent core}\ (\mathrm{P4}):\qquad
g,\ g'\ [\mathrm{EW.33}];\quad h_0\ [\mathrm{EW.20}];\quad c_W\ [\mathrm{EW.33}];\quad\Lambda\ [\mathrm{CT1.25}];\quad\varkappa,\ \beta,\ \alpha_\Omega\ [\mathrm{D2.1}];
$$
$$(\mathbf{IIIb})\ \ \text{configuration data --- functionally dependent}\ (\neg\text{further freedom}):\qquad
\theta_W=\arctan(g'/g)\ [\mathrm{EW.24}];\quad e=\frac{gg'}{\sqrt{g^2+g'^2}}\ [\mathrm{EW.35}];\quad\mu_\star^2=c_W\varkappa^2\beta^2h_0^2\ [\mathrm{EW.33}];
$$
$$
m_W^2=\mu_\star^2g^2/4\ [\mathrm{EW.20}];\quad m_Z^2=\mu_\star^2(g^2+g'^2)/4\ [\mathrm{EW.23}];\quad m_H^2=\delta^2S_{\mathrm{eff}}/\delta h^2\big|_{h_0}\ [\mathrm{EW.27}].
$$
$$
\text{completeness}:\ \ \forall\ \text{symbol of the A-Part-4 master table}\in\mathbf I\cup\mathbf{II}\cup\mathbf{IIIa}\cup\mathbf{IIIb}\cup\{\text{structural objects}\};\qquad
\mathbf I,\ \mathbf{II},\ \mathbf{IIIa}\ \text{pairwise disjoint};\quad\mathbf{IIIb}=f(\mathbf{IIIa})\ (\neg\text{independent data}).
$$

**Req.** P1–P5; every cited derivation tag (listed inline).

**Pf.**
$$
\mathbf I:\ \ \forall\ \text{entries proved at the inline-cited tag from A1--A9 + earlier derived only}
$$
$$
\mathbf{II}:\ \ \mathrm{CT2.9};\qquad\mathrm{CT2.11}:\ \mathfrak h\mapsto\lambda\mathfrak h=\text{symmetry}\implies\neg\exists\ \text{further dimensionful freedom}
$$
$$
\mathbf{IIIa}/\mathbf{IIIb}:\ \ \mathrm{P4}\ (\text{core})\ +\ \text{functional dependencies at the inline-cited tags}\ (\mathbf{IIIb})
$$
$$
\text{completeness}:\ \ \text{scan of the master symbol table}:\ \forall\ \text{symbol}=\text{structural}\ \vee\ \mathbf I\ \vee\ \mathbf{II}\ \vee\ \mathbf{III};\quad\neg\exists\ \text{symbol in two categories}
$$
$$
\implies\text{corpus}=1\ \text{calibration d.o.f.}\ (\mathfrak h)\ +\ \text{finite independent core}\ (\mathbf{IIIa})\ +\ \text{closed parameter-free prediction list}\ (\mathbf I).\ \blacksquare
$$

**Phys.** The final audit: everything the corpus says is either a fixed number, a name for the single scale $\mathfrak h$, or data of a particular solution — nothing floats in between. The boundary between prediction and parameter is drawn exactly, and it is the same boundary CT4.12 turns into falsifiers.

---

## Closure exports of Part 2 §G (consumed by Parts 3–4)

$$
\begin{array}{lll}
\mathrm{CT4.1(a)}\ O(n)=2^{n+1}-16;\ O(4)=16;\ n_{\mathrm{bidir}}=2d\ge4 &
\mathrm{CT4.2}\ \mathcal P_M^{(n\le3)}F_{D^-}\mathcal P_M^{(n)}=0 &
\mathrm{CT4.3}\ \text{locked}\subseteq\mathfrak L;\ w(C)\ne0\\
\mathrm{CT4.4}\ D^-:\ \neg\text{gauge structure} &
\mathrm{CT4.5}\ T^{(D^-)}_{\mu\nu}=\rho u_\mu u_\nu;\ w_{D^-}=0 &
\mathrm{CT4.6}\ D^+\ne D^-\ (8\ \text{axes})\\
\mathrm{CT4.7}/\mathrm{CT4.10}\ \text{entropy triangle}\ \{vac, D^+, D^-\}\ \text{complete} &
\mathrm{CT4.9}\ S_v\le3\ln2;\ S_{\mathcal B}\le\tfrac{A}{\mathfrak h^2}\ln2 &
\mathrm{CT4.8}\ \text{locked region}\equiv\text{boundary area}\\
\mathrm{CT4.11}\ Z[\mathbf F_\oplus,M_\oplus]\ \text{well defined};\ \mathfrak S\ne\varnothing &
\mathrm{CT4.12}\ 14\ \text{falsifiers} &
\mathrm{CT4.13}\ \text{categories}\ \mathbf I/\mathbf{II}/\mathbf{III}\ \text{exhaustive}
\end{array}
$$

**Corpus status.** $\mathbf A\to\mathbf B\to\mathbf C\to\mathbf D\to\mathbf E\to\mathbf F\to\mathbf G$ complete; A9 test surface $=$ CT4.12; audit $=$ CT4.13. Verification suite: `checks/run_all.py` (exact arithmetic, no floating point).

$\blacksquare$

---
