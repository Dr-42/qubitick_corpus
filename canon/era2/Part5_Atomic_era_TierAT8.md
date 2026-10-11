# $\langle qu(b(i(t|t))ick)\rangle$ — **Part 5 · Atomic era** — Tier AT.8: the spin spine

**Level.** 5. **Era.** 2 (the Atomic era). **Tier.** AT.8 — the duality as a calculational tool,
the polygon spin holonomy, the frame section on the extended carrier, and the ledger-native
moment coupling.
**Tags.** AT.46–AT.49. **Pattern.** BM.130 / BM.144 / BM.152 — the construction tiers and the
status-and-closure tag of a tier.
**Status.** discovery-phase working tier, **closed at AT.49**. Nothing is adopted into the frozen
canon; no declaration issues; §Cal-AT stays empty; no clause of Parts 1–4 is modified, retracted
or renumbered.
**Machine.** `canon/era2/spin_holonomy.py` → **18/18 exact** (AT.46); `canon/era2/frame_section.py`
→ **19/19 exact** (AT.47); `canon/era2/moment_coupling.py` → **17/17 exact** (AT.48); the shared
library `canon/era2/duality.py` (the View1↔View2 rules (D1)–(D6), registered beside `qexact.py`);
`canon/era2/check_era2_format.py` → the format + citation gate over all ten Part 5 documents.
`canon/era2/run_all_era2.py` → **31 checkers, 551 exact markers, 0 failures, exit 0**. Exact
arithmetic: `Fraction`; `Quad(√d)` polygon geometry; `Gauss(i)` matrices with exact nullities by
elimination; integer group tables (the 12 tetrahedral rotations, all 144 arc transports, the
binary tetrahedral 2T over $\mathbb Z[i]/2$); integer polynomial arithmetic in
$\mathbb Z[C,S]/(C^2{+}S^2{-}1)$; exhaustive sign censuses. **No floating point in any assertion.
No measured value enters any derivation [P5].**
**Charter.** Part 5 cites Parts 1–4 and earlier AT-tags only.
**Mandate.** Three Architect directives, executed in order: **(i)** adopt the View 1 (chart) ↔
View 2 (ledger) duality — the CT1.12 dictionary + the BM.134(5) handshake — as a strict
calculational tool, and compute the polygon spin holonomy: the shift's frame-dragging as a ledger
holonomy coupled to the winding and the orientation doublet; **(ii)** *build it* — the frame
section, BM.6(8)/item 21(i)'s named residue, at the locus the R.39 Rmk fixes (Def-H.34's extended
carrier); **(iii)** construct the ledger-native moment coupling, extract the anomalous read, and
adjudicate BM.125(4)'s three grounds — with the standing constraint that a zero or a barred
contraction be reported as a hard no-go with the exact missing definition.
**Discovery record.** `era2/SPIN_HOLONOMY.md`, `era2/FRAME_SECTION.md`, `era2/MOMENT_COUPLING.md`
(the three working documents, with the directive transcripts, the premise corrections, and the
full check ledgers).

---

## Tier AT.8 — the spin spine: duality, drag, frames, moment

### AT.46 — The duality as a calculational tool: the polygon shift holonomy, the quantized frame-dragging, the doublet splitting, and the statistics-flip law

**Thm.**
$$(1)\quad\textbf{THE TOOL (rules (D1)–(D6), all re-certified as machine identities).}\ \ \mathrm{(D1)}\ \text{sector}\to\mathrm{ADM}: \mathrm{CT1.12}\equiv\mathrm{BM.34}(1)\ \text{entrywise}\ \wedge\ N^2\det\gamma=-\det g\ \ (8\ \text{rational witnesses});$$
$$\mathrm{(D2)}\ \text{ledger}\to\text{chart per edge}:\ (w\!\cdot\!\Delta x)(e)=\frac{\mathfrak h^2\kappa_e/\Omega^2+(\Delta x^0)^2-M_{ij}\Delta x^i\Delta x^j}{2\varkappa\beta\,\Delta x^0}\ [\mathrm{AT.5}(1)];\qquad\mathrm{(D3)}\ \text{chart}\to\text{ledger}:\ \widehat{ds}^2(e)=\kappa_e\in\mathbb Z\ [\mathrm{FT.24}\text{–}25],\ \ \textstyle\sum_e\kappa_e=2k\in2\mathbb Z\ [\mathrm{FT.22}];$$
$$\mathrm{(D4)}\ \kappa_e=\text{flat}_e+\text{drag}_e,\quad\text{drag}_e=(\Omega^2/\mathfrak h^2)\,2\varkappa\beta\,\Delta x^0(e)\,(w\!\cdot\!\Delta x)(e);\qquad\mathrm{(D5)}\ \mathrm{Hol}_w(c)=\textstyle\sum_e(w\!\cdot\!\Delta x)(e),\quad\Theta_{\mathrm{drag}}=(\Omega^2/\mathfrak h^2)\,2\varkappa\beta\,\textstyle\sum_e\Delta x^0(e)(w\!\cdot\!\Delta x)(e);$$
$$\mathrm{(D6)}\ \text{the doublet reads on}\ \mathcal H_\omega\ [\mathrm{Def\text{-}H.33}]\ \text{over the fourth-root alphabet}\ [\mathrm{Def\text{-}BM.16}(5)];\qquad\textbf{species bars honored:}\ \Theta_R\ \neg\text{equated with}\ 2\pi k\ [\mathrm{FT.55}(1)];\ \text{resolvents}\ \neg\text{identified}\ [\mathrm{BM.134}(5)]$$
$$(2)\quad\textbf{the holonomy theorems:}\qquad\textbf{constant shift}\implies\mathrm{Hol}_w=w\!\cdot\!\bigl(\textstyle\sum_e\Delta x(e)\bigr)=0\ \ \text{on every closed chain (exact telescoping — the discrete zero-curl);}$$
$$\textbf{the forced rotating field}\ [\mathrm{AT.34}:\ |\mathrm{Rot}|=2E,\ \text{simply transitive on the arcs (all 144 transports counted)},\ \text{stabilizer}\ \{\mathrm{id},\text{reflection}\},\ |\mathrm{Aut}|=24]:$$
$$w(e)=g_e w_0,\ \Delta x(e)=g_e\Delta x_0\implies\boxed{\ \mathrm{Hol}_w=\sum_e(g_ew_0)\!\cdot\!(g_e\Delta x_0)=L\,(w_0\!\cdot\!\Delta x_0)\ \ \textbf{EXACTLY, NONZERO}\ }\qquad\text{on the tetrahedral face:}\ 3\cdot s\cdot8;\ s=\tfrac35:\ \tfrac{72}5$$
$$(3)\quad\textbf{orientation-oddness:}\qquad\hat\omega\ [\mathrm{D2.6}]\ \text{with the forward-only tick}\ [\mathrm{D1.8}:\ x^0:=\tau_n;\ \mathrm{A6}:\ \neg\exists\tau^{-1}]\ \text{keeps}\ \Delta x^0>0\ \text{and flips the spatial hops}:$$
$$\boxed{\ \mathrm{Hol}_w(\omega(c))=-\mathrm{Hol}_w(c)\ }\qquad\text{the mixed term is the shift's UNIQUE T-even entry}\ [\mathrm{CT1.12a}(2);\ \mathrm{FT.23}:\ \text{T-odd}\times\text{T-odd}\times\text{T-even}]$$
$$(4)\quad\textbf{THE QUANTIZATION LATTICE:}\qquad\kappa_e\in\mathbb Z\ \wedge\ \Theta=\textstyle\sum\kappa_e\in2\mathbb Z\ \ \textbf{turn frame-dragging into a Diophantine condition on the calibration product};$$
$$\text{witness (tetrahedral face,}\ L{=}3,\ t{=}2,\ \Omega^2{=}1,\ q{=}0,\ \varkappa\beta s{=}{-}\tfrac1{16}\text{):}\quad\text{flat}_e{=}4,\ \text{drag}_e{=}{-}2,\ \kappa_e{=}2\ [\mathrm{Def\text{-}BM.4}(5)\ \text{minimal}],\ \ \Theta{=}6{=}\Theta_{\min}(3)\ [\mathrm{FT.32}(6)\ \text{odd ladder, attained}]$$
$$(5)\quad\textbf{the doublet splits:}\qquad\Theta_\pm=\Theta_{\mathrm{flat}}\pm\Theta_{\mathrm{drag}}\in2\mathbb Z,\qquad k_+-k_-=\Theta_{\mathrm{drag}};\qquad\text{witness A:}\ k_+=3\ \text{vs}\ k_-=9\ (\Theta_{\mathrm{drag}}=-6);$$
$$\widehat D_{\mathrm{drag}}=\mathrm{diag}(i^{+\Theta_d},\,i^{-\Theta_d})\ \ \text{on}\ \mathcal H_\omega\ [\mathrm{Def\text{-}H.33}\ \text{traversal basis}];\qquad\hat\chi\widehat D\hat\chi=\widehat D^{-1}\ \ \textbf{— chirality flips the drag sign};\qquad\{\hat\omega,\hat\chi\}=0$$
$$(6)\quad\textbf{THE STATISTICS-FLIP LAW:}\qquad\varepsilon_\pm=i^{\Theta_\pm}\ [\mathrm{Def\text{-}BM.16}(5)]:\qquad\boxed{\ \varepsilon_+\ne\varepsilon_-\iff\Theta_{\mathrm{drag}}\ \ \textbf{ODD}\ }\qquad[\text{machine-censused over all}\ (\text{flat}_e,\text{drag}_e)\ \text{in range}];$$
$$\text{witness B}\ (t{=}1,\ \text{the SAME lattice point}\ \varkappa\beta s{=}{-}\tfrac1{16}\text{):}\quad\Theta_+{=}18\ (k{=}9,\ \varepsilon{=}{-}1)\quad\text{vs}\quad\Theta_-{=}24\ (k{=}12,\ \varepsilon{=}{+}1);$$
$$\boxed{\ \textbf{the two ORIENTATIONS of one materialized geometry can sit in OPPOSITE statistics classes, purely from the frame-drag}\ }$$
$$(7)\quad\textbf{two distinct fourth-root signs, no identification:}\qquad\text{the discrete Frenet lift of one traversal}\ =(-1)^n\ (\text{turning number}\ n,\ \text{the double cover});\qquad\text{the exchange sign}\ =(-1)^k,\ k=\Theta/2\ [\mathrm{FT.32}(6)];$$
$$\text{census}\ L{=}2..8:\quad\text{AGREE}\iff L\ \text{odd}\ \vee\ L\equiv2\ (4);\qquad\text{DISAGREE}\iff L\equiv0\ (4)\ \ [\text{witnesses}\ (4,1,2),(8,1,4)]\ —\ \text{the parity shadow of}\ \mathrm{FT.55}(1)\text{'s dimensional bar}$$
$$(8)\quad\textbf{premise corrections, on the record:}\qquad(\mathrm{P1})\ \text{the shift couples through the ON-SHELL LOCUS}\ \kappa_e=\widehat{ds}^2(e)\ [\mathrm{AT.5}(1)],\ \neg\text{inside}\ w(C)=\mathcal J(C)\prod G(e)(-1)^{\aleph},\ \text{whose alphabet is}\ \{\sigma,\mathcal J,\aleph\}\ [\mathrm{Def\text{-}H.32}(2),\ \mathrm{(S1)}];$$
$$(\mathrm{P2})\ \text{the frozen handshake locus is}\ \mathrm{BM.134}(5)\text{'s threshold indicator}\ \chi_{\{NE\ge\mathcal T_0\}};\ \ \mathrm{FT.108}(5)\ \text{is the ledger-side resolvent itself (fugacity renamed}\ wf\ \text{in code — the corpus overloads}\ w\text{)};$$
$$(\mathrm{P3})\ \text{``photon''/``polygon'' stay quoted names}\ [\mathrm{Def\text{-}BM.3}(7);\ \mathrm{P5}];\ \text{the species content used is D1.5's transit/bound distinction}\ [\mathrm{Def\text{-}H.4}]$$
$$(9)\quad\textbf{status:}\qquad\textbf{derived:}\ (1)\text{–}(7);\qquad\textbf{marked,}\neg\textbf{adopted:}\ \text{the level-price read rule (AT.44}(8\mathrm{iv})\text{'s, unchanged)};\qquad\textbf{calibration, unchanged:}\ \varepsilon_q,\ (\varkappa,\beta);$$
$$\textbf{the spin connection adjudication:}\ \ \text{the ledger drag holonomy is}\ \mathrm{Def\text{-}H.21}\text{'s connection's DICTIONARY PARTNER,}\ \neg\text{its equal};\qquad\text{Open Gaps 19 stays DECLARED}\ [\mathrm{Def\text{-}H.37}(2)]$$

**Req.** A6, A8, D1.4, D1.5, D1.6, D1.8, D2.6 (Part 1); CT1.12, CT1.12a, CT1.22, D2.1, FT.13 (Part 2); Def-H.4, Def-H.21, Def-H.32(2),(4), Def-H.33, Def-H.37(2), FT.22, FT.24, FT.25, FT.32(6), FT.55(0),(1),(2), FT.108(2),(3),(4),(5), FT.157(1),(3) (Part 3); AT.2(4), AT.5(1),(3),(4), AT.30(3), AT.34(1)–(7), AT.36(3), AT.42(2),(4), AT.44(5) (this level); Def-BM.4(1),(5), Def-BM.5(1), Def-BM.16(5), BM.8(2), BM.19(1),(2),(3), BM.34(1),(3),(4), BM.121(2),(5),(6),(7), BM.123(2), BM.132, BM.134(5), BM.136(4), BM.137(1),(2),(3) (Part 4); exact `Quad(√3)` polygon arithmetic, integer group enumeration (12 rotations, 144 arc transports), `Gauss(i)` 2×2 identities, `Fraction` Diophantine witnesses [math; machine: `spin_holonomy.py` §§A–F, 18/18, on `duality.py`].

**Pf.**
$$(1):\ \text{the eight witnesses entrywise + Schur}\ [\text{machine A1,A2}];\ \text{AT.5's round trip}\ [\text{machine C5}];\ (2):\ \Sigma_e\Delta x(e)=0\ \text{on the exact polygons (digon, triangle, square, hexagon)}\ [\text{machine B1,C1}];\ \text{group transport by orthogonality}\ [\text{machine C2,C3}];$$
$$(3):\ \Delta x^0\ \text{forward,}\ \Delta x^i\ \text{arc-odd}\implies\text{the mixed term arc-odd}\ [\text{machine C4}];\ (4):\ \text{the witness arithmetic}\ [\text{machine D1}];\ (5):\ \text{Def-H.33's algebra over}\ \mathbb Z[i]\ [\text{machine D3}];$$
$$(6):\ \text{the law censused over all}\ (\text{flat}_e,\text{drag}_e);\ \text{witnesses A,B exact integers}\ [\text{machine D2,D4}];\ (7):\ \text{the lift}\ (-1)^n\ \text{vs}\ (-1)^k\ \text{at FT.32(6)'s minima}\ [\text{machine E1}];\ (8),(9):\ \text{the record rows}.\ \blacksquare$$

**Phys.** The duality asked to be used as a tool, and the tool cut clean. On the chart side, frame
dragging is the shift's circulation; on the ledger side it is one integer per edge — the mixed term
of the line element — and FT.22's quantization turns the circulation into a Diophantine condition
on the calibration product, witnessed at $\varkappa\beta s=-\tfrac1{16}$ where the rotating
tetrahedral face attains the odd-ladder minimum $\Theta=6$ with the *minimal* materialized edge
value $\kappa_e=2$. A constant shift telescopes to zero on every closed chain, exactly as a
curl-free field must; the rotating field that arc-transitivity forces — unique up to one scale per
floor — does not, and the group-transport identity $L(w_0\!\cdot\!\Delta x_0)$ is its exact nonzero
certificate. Because the ledger's ticks only run forward while spatial hops are arc-odd, the drag
is orientation-odd: the two rays of the orientation doublet acquire opposite winding shifts, and
the statistics phase $i^\Theta$ splits with them. The sharp surprise is the flip law — at odd
$\Theta_{\mathrm{drag}}$, witnessed at $t=1$ on the very same quantization lattice, the two
orientations of *one materialized geometry* sit in *opposite statistics classes*. Frame dragging,
in this corpus, can change how a polygon exchanges, with no smooth limit and no imported
interaction. And the discipline held where it had to: the Frenet lift's $(-1)^n$ and the exchange
sign are distinct fourth-root reads that disagree exactly at $L\equiv0\ (4)$ — the parity shadow of
FT.55(1)'s dimensional bar — so the ledger drag holonomy is the spin connection's dictionary
partner, never its equal.

---

### AT.47 — The frame section on the extended carrier: the spacetime spin factor is maximal, the pseudoscalar relocates, and the section reduces to a six-frame menu

**Thm.**
$$(1)\quad\textbf{GATES (re-produced,}\ \neg\textbf{new):}\qquad\text{the }15\ \text{Pauli products on}\ \mathbb C^4\ \text{are Hermitian, square to}\ +I_4,\ \text{traceless};\qquad\textbf{exactly }30\ \text{pairwise-anticommuting }4\text{-frames among}\ \binom{15}{4}=1365\ \ [\mathrm{FT.93}(1)];$$
$$\text{the pseudoscalar catalog: }15\ \text{values (up to sign), EACH from exactly }2\ \text{frames, species}\ 6/3/6;\qquad\mathcal F_0:\ \gamma_{\mathcal F_0}=\sigma_0\otimes\sigma_3=\mathrm{diag}(1,-1,1,-1),\ \ P_\pm^{(\mathcal F_0)}=\mathrm{diag}(0,1,0,1)/\mathrm{diag}(1,0,1,0)\ [\mathrm{FT.93}(2)];$$
$$\textbf{the pincer re-proved at its locus:}\quad\dim\{M:[M,W_i^{\mathrm{pair}}]=0\}=2=\mathrm{span}\{\Pi_{\mathcal R},\Pi_{\mathcal V}\};\quad\dim\{M:\{M,W_i^{\mathrm{pair}}\}=0\}=1=\mathbb C\!\cdot\!\Pi_{\mathcal V};\quad\text{seed side: nullities}\ (1,0)\ \ [\mathrm{FT.93}(3)]$$
$$(2)\quad\textbf{THE SPACETIME SPIN FACTOR EXISTS AND IS MAXIMAL.}\ \ \text{On}\ \mathcal H_{\mathrm{ext}}=\mathcal H_{\mathrm{int}}\otimes\mathcal H_\omega\ [\mathrm{Def\text{-}H.34};\ \text{R.39 Rmk: ``exactly the extended-carrier locus that FT.93(7) identified''}]\ \text{with}\ W_i^{\mathrm{ext}}=\tfrac12\sigma_i\otimes I_\omega\ [\mathrm{EW.32}\ \text{carrier}]:$$
$$\text{Def-H.34's triple}\ (\hat\omega,\hat\chi,\hat\kappa)=(I\otimes\sigma_1,\ I\otimes(-\sigma_2),\ I\otimes\sigma_3):\ \ \text{Hermitian involutions, pairwise anticommuting},\ \hat\omega\hat\chi=-i\hat\kappa\ \text{(cyclic)},\ \textbf{GAUGE-TRIVIAL};$$
$$\text{the 8 real products are}\ \mathbb R\text{-independent}\ (\mathrm{Cl}(3,0));\qquad\text{the commutant is}\ I\otimes\mathrm{End}(\mathcal H_\omega)\ (\text{nullity }4);\qquad\{A,\sigma_i\}=0\ \forall i\implies A=0\ (\text{nullity }0);$$
$$\boxed{\ \textbf{NO gauge-trivial fourth anticommuting element exists: a fully gauge-scalar Dirac frame is IMPOSSIBLE, proven as a nullity}\ }$$
$$(3)\quad\textbf{THE RELOCATION ROW:}\qquad\gamma_{\mathcal F_0}=\sigma_0\otimes\sigma_3=I\otimes\hat\kappa\ \ \textbf{AS MATRICES}\ —\ \mathrm{FT.93}(2)\text{'s example pseudoscalar IS Def-H.34's partner involution, in the extended basis;}$$
$$\text{the SAME matrix: pincered in the pair arena}\ ([\gamma,W_3^{\mathrm{pair}}]=0,\ [\gamma,W_{1,2}^{\mathrm{pair}}]\ne0)\ \text{and WEAK-SCALAR in the extended arena};\qquad\boxed{\ \textbf{the pincer is ARENA-RELATIVE}\ }\ —\ \mathrm{FT.93}(3)\ \text{stands untouched at its locus}$$
$$(4)\quad\textbf{THE FRAME SHORTLIST:}\qquad\text{of the }30\ \text{native frames, EXACTLY }6\ \text{admit a weak-scalar chirality on}\ \mathcal H_{\mathrm{ext}}:\ \gamma=\pm\sigma_0\otimes\sigma_i\ =\ \text{the three gradings}\times\text{two signs}\ =\ \textbf{ONE S-transform orbit};$$
$$\text{the gauge-trivial element count across the }30:\ \ \{0{:}\,15,\ 1{:}\,6,\ 2{:}\,9\}\ —\ \textbf{no frame is fully gauge-trivial};\qquad\mathrm{SU}(2)_L\text{-type chiral coupling stays}\ \neg\textbf{natively derivable}\ [\mathrm{FT.93}(4)]$$
$$(5)\quad\textbf{THE ASSIGNMENT REDUCTION:}\qquad\text{on an arc-transitive floor}\ [\mathrm{AT.34}],\ \text{an equivariant section}\ \mathcal F_e=g_e\triangleright\mathcal F_{e_0}\ \textbf{is ONE base frame per floor}:\ \ \text{item 21(i)'s per-edge undeclared datum shrinks from}\ 30^E\ \text{to a finite enumerated menu;}$$
$$\textbf{MARKED (}\neg\textbf{derived,}\ \neg\textbf{adopted):}\ \ \triangleright\ \text{is Def-H.37(2)'s DECLARED holonomy identification (Open Gaps 19), inherited at use.}\ \ \text{Under it, exact censuses (2T rebuilt: }24,\ \text{closed},\ \det=1\text{):}$$
$$\text{diagonal}\ \mathrm{Ad}(U\otimes U):\ 10\ \text{orbits}\times3\ (\text{shortlist: }2\times3);\qquad\text{seed-only}\ \mathrm{Ad}(U\otimes I):\ 6\ \text{singletons}+8\ \text{triples};\qquad\boxed{\ \textbf{the shortlist frames ARE the six seed-only singletons}\ }$$
$$(6)\quad\textbf{THE TRANSPORT COUPLING (formal, exact):}\qquad U(\phi)=\cos\phi\,I+i\sin\phi\,\hat n\!\cdot\!\vec\sigma\ [\mathrm{EW.32};\ \mathrm{Def\text{-}H.34}'\text{s}\ h(\mathbf c)]:\qquad U^L=\cos(L\phi)\,I+i\sin(L\phi)\,\hat n\!\cdot\!\vec\sigma$$
$$[\text{machine: the recursion in}\ \mathbb Z[C,S]/(C^2{+}S^2{-}1)\ \text{vs matrix powers},\ L{=}2..8,\ 5\ \text{Pythagorean pairs}\times3\ \text{axes}=105\ \text{identities}];\qquad\boxed{\ \text{the fourth-root quantization:}\ L\phi\in\tfrac\pi2\mathbb Z\ }\ —\ \text{a CONDITION on the P4-class data}\ (\ell_c,\mathbf c),\ \neg\text{a value}$$
$$(7)\quad\textbf{THE UNIFICATION:}\qquad\widehat D_{\mathrm{drag}}=\mathrm{diag}(i^{+\Theta_d},i^{-\Theta_d})\ [\mathrm{AT.46}]\ \ =\ \exp\bigl(i\tfrac\pi2\Theta_{\mathrm{drag}}\,\hat\kappa\bigr)\qquad[\text{machine: }11\ \text{integer witnesses}];$$
$$\boxed{\ \textbf{the polygon's discrete spin connection IS the shortlist pseudoscalar's fourth-root exponential at the drag winding}\ }\qquad\hat\omega\hat\kappa\hat\omega=-\hat\kappa\implies\widehat D(\omega(c))=\widehat D(c)^{-1}$$
$$(8)\quad\textbf{THE DIRAC SKELETON:}\qquad\{\gamma_a,\gamma_{\mathcal F_0}\}=0\ \ \forall a\ [\mathrm{FT.93}(1)\ \text{on}\ \mathcal F_0]:\ \ \text{any}\ \mathcal D=\sum_a\gamma_a\otimes(\text{transport})_a\ \ \text{is CHIRAL-ODD}\ (\mathcal D:\ P_+\leftrightarrow P_-)\ —\ \text{the graded shape is derived for EVERY slot choice;}$$
$$\text{the three spatial gammas}\ \sigma_i\otimes\sigma_2\ \text{carry the gauge index}\ ((2)\text{'s theorem});\ \ \text{the fourth}\ I\otimes\hat\omega\ \text{is gauge-trivial}$$
$$(9)\quad\textbf{ADJUDICATION:}\qquad\textbf{CONSTRUCTED, derived:}\ (2),(3),(4),(6),(7),(8);\qquad\textbf{REDUCED to a finite menu:}\ \text{the section}\ e\mapsto\mathcal F_e\ (5);\qquad\textbf{STILL DECLARED/OPEN:}\ (\mathrm i)\ \text{the lift};\ (\mathrm{ii})\ \text{the base frame per floor};\ (\mathrm{iii})\ \text{the P4 values}\ (\ell_c,\mathbf c);\ (\mathrm{iv})\ \text{the global Dirac-type operator on the emergent geometry};$$
$$\neg\text{a declaration},\quad\neg\text{a P4 addition},\quad\neg\text{a new dimensionful scale}\ [\mathrm{P1}],\quad\neg\text{a measured value}\ [\mathrm{P5}],\quad\neg\text{a species identification}\ [\mathrm{Def\text{-}BM.3}(7)]$$

**Req.** A3 (Part 1); CT1.1, CT1.2, CT1.5, CT0.7, EW.32, EW.33 (Part 2); Def-H.14, Def-H.33, Def-H.34, FT.93(1),(2),(3),(4),(7), FT.122(6), item 21(i) (Part 3); AT.10, AT.34, AT.44, AT.46 (this level); Def-BM.3(7), Def-BM.16(5), Def-BM.18, BM.6(8), BM.34(3), BM.125(4), BM.134(5), BM.137(1) (Part 4); exhaustive 4-frame enumeration over `Gauss(i)`, exact nullities by elimination over $\mathbb Q(i)$, real-rank by $\mathbb Q$-elimination, the binary tetrahedral group over $\mathbb Z[i]/2$, de Moivre in $\mathbb Z[C,S]/(C^2{+}S^2{-}1)$ [math; machine: `frame_section.py` §§A–H, 19/19].

**Pf.**
$$(1):\ 1365\ \text{subsets scanned entrywise;}\ \text{nullities by exact elimination}\ [\text{machine A1--A3, B1--B3}];\ (2):\ \text{the triple's identities entrywise;}\ \text{nullities}\ 4\ \text{and}\ 0;\ \text{real rank}\ 8\ [\text{machine C1,C2}];$$
$$(3):\ \text{the matrix equality and the four commutators}\ [\text{machine C3}];\ (4):\ \text{the census over all }30;\ \text{the S-orbit via}\ \tfrac12S^\dagger\sigma_jS\ [\text{machine D1}];\ (5):\ 576\ \text{products};\ \text{orbit partitions exhaustive}\ (30=10\cdot3=6+24;\ 6=2\cdot3=6\cdot1)\ [\text{machine E1,E2}];$$
$$(6):\ 105\ \text{identities}\ [\text{machine F1,F2}];\ (7):\ 11\ \text{witnesses};\ \hat\omega\hat\kappa\hat\omega=-\hat\kappa\ \text{entrywise}\ [\text{machine G1,G2}];\ (8):\ \text{the four anticommutators}\ [\text{machine H1}];\ (9):\ \text{assembly}.\ \blacksquare$$

**Phys.** The corpus told us where to dig. FT.93 proved the pair arena can never carry a
weak-scalar chirality — and then named, precisely, what was missing: *a spacetime spin factor, a
carrier on which the gauge action is trivial*. One tier later Def-H.34 built exactly such a factor
— the orientation doublet with its quaternionic triple — and the R.39 Rmk said so in words. This
tag puts the two facts together by machine: the triple is gauge-trivial, closes to $\mathrm{Cl}(3,0)$,
and is **maximal** — there is no fourth gauge-trivial gamma, proven as a nullity, so any Dirac
frame's spatial gammas must carry the gauge index. That is deficit 1's residue, not as a lament but
as a dimension count. And the relocation is a matrix equality: FT.93's example pseudoscalar
$\sigma_0\otimes\sigma_3$ *is* Def-H.34's partner involution — the same matrix, pincered in one
arena and weak-scalar in the other, because the pincer was always about the *action*, not the
algebra. From there the section almost builds itself: arc-transitivity makes an equivariant
assignment one base frame per floor; the census narrows the menu to six frames in a single S-orbit
— and under the seed-only lift the six are exactly the fixed points, the singleton orbits. The
transport couples by de Moivre, exactly, and the fourth-root alphabet turns the winding into a
Diophantine condition on the P4 data. Then the unification: AT.46's drag operator *is*
$\exp(i\frac\pi2\Theta_{\mathrm{drag}}\hat\kappa)$ — the pseudoscalar's exponential at the quantized
drag winding. The frame datum and the ledger holonomy are one object, and the chirality the
traversal involution flips is the chirality the drag splits. What remains open is named to the
symbol: the lift, the base frame, the profile values, and the global operator — whose spatial
gammas, by theorem, carry the gauge index or do not exist.

---

### AT.48 — The ledger-native moment coupling: a vanishing lemma, two native channels, the exact anomalous read, and the proved vector no-go

**Thm.**
$$(1)\quad\textbf{THE VANISHING LEMMA (the directive's anticipated zero, proved):}\qquad\sum_v f_v=\tfrac12\sum_v\bigl(\sigma_{\rightarrow}(v)-\sigma_{\leftarrow}(v)\bigr)\equiv0\ \ \textbf{on EVERY configuration}$$
$$\text{(every edge counted once outgoing, once incoming)};\qquad[\text{machine: all }120\ \text{open chains with end reads}\ (f_{\mathrm{src}}{=}\tfrac12\sigma_{\text{first}},\ f_{\mathrm{tgt}}{=}{-}\tfrac12\sigma_{\text{last}})\ \text{and all }120\ \text{closed cycles},\ L{=}3..6];$$
$$\therefore\ \textbf{the naive TOTAL contraction with any gamma is identically zero on closed chains}$$
$$(2)\quad\textbf{THE TWO NON-VANISHING NATIVE CHANNELS:}\qquad(\mathrm a)\ \ \textbf{the boundary channel (open connectors): by EM.9b telescoping, the operator IDENTITY}$$
$$\boxed{\ \widehat M:=\Bigl(\sum_{\text{interior }v}f_v\Bigr)\cdot\gamma_{\mathcal F_0}\ =\ -\,q_{\mathrm{EM}}(c)\cdot\bigl(I_2\otimes\hat\kappa\bigr)\ }\qquad[\gamma_{\mathcal F_0}=I\otimes\hat\kappa:\ \mathrm{AT.47}(3);\ \text{machine: all }120\ \text{open configurations}];\qquad[\gamma_{\mathcal F_0},W_i^{\mathrm{ext}}]=0\ (\text{gauge-admissible});$$
$$(\mathrm b)\ \ \textbf{the activity channel (every configuration):}\quad\aleph(\sigma,C)=\sum|f_v|\ \ \text{— the NON-telescoping residue — coupled by the FROZEN A8 weight}\ \ w(C)=\mathcal J(C)\prod_eG(e)\,(-1)^{\aleph(\sigma,C)}\ [\mathrm{Def\text{-}H.32}(2)];$$
$$\mathrm{AT.30}(3)\ \text{re-verified:}\ 14\ \text{of}\ 32\ \text{five-edge chains have}\ q{=}0\ \wedge\ \aleph{>}0;\qquad\text{the amplitude layer's deaths}\ [\mathrm{FT.106}(3\mathrm c)]\ \text{are its frozen consequence}$$
$$(3)\quad\textbf{THE VECTOR CONTRACTION IS A HARD NO-GO, with the exact missing definition:}\qquad\text{the native EM reads}\ \{\sigma_e,f_v,\aleph,q_{\mathrm{EM}},Q\}\ \textbf{are ALL index-free scalars};$$
$$\text{the only native index-}i\ \text{carriers are}\ w_i\ (\text{the shift — the weak block}\ [\mathrm{FT.157}(1);\ \mathrm{AT.2}(4)])\ \text{and}\ W_i;\qquad\text{EM is a STACK aspect with ZERO metric coordinates}\ [\mathrm{AT.2}(3),(4);\ \mathrm{CT1.12a}(2)];$$
$$\boxed{\ \textstyle\sum_i(\mathrm{EM})_i\,\sigma_i\otimes\sigma_2\ \ \textbf{is}\ \neg\textbf{formable ledger-natively};\qquad\textbf{the missing definition: a ledger-native index-carrying EM read}\ }$$
$$\textbf{THE DECOMPOSITION THEOREM:}\quad\sigma^{\mu\nu}F_{\mu\nu}\ \ \text{splits into}\ \ \begin{cases}(\mathrm a)+(\mathrm b):&\text{the native pseudoscalar channel — CONSTRUCTED here}\\ \mathrm{AT.6}'\text{s functional}:&\text{the shift-mediated magnetic channel — derived up to}\ \varkappa\beta\ [\mathrm{AT.34}]\end{cases}$$
$$\text{the chart-side route (coarse-grained}\ F_{\mu\nu}\ [\mathrm{CT1.19}/\mathrm{CT1.22}])\ \text{crosses species}\ [\mathrm{BM.134}(5)\ \text{discipline}]\ \text{and is excluded by the directive}$$
$$(4)\quad\textbf{THE ACTION ON}\ \mathcal H_{\mathrm{ext}}\ \textbf{— IT FLIPS THE CHIRALITY:}\qquad\widehat M|c\rangle=-q|c\rangle,\quad\widehat M|\omega(c)\rangle=+q|\omega(c)\rangle,\quad\mathrm{spec}=\{-q,-q,+q,+q\};$$
$$\boxed{\ \{\widehat M,\hat\chi\}=0\ }\qquad(\{\hat\kappa,\hat\chi\}=0\ \text{is Def-H.34's quaternion triple doing the work});\qquad[\widehat M,\hat\kappa]=0,\qquad\{\widehat M,\hat\omega\}=0;$$
$$\text{the chiral basis:}\quad\tfrac12U^\dagger\widehat M U=-q\,I_2\otimes\sigma_1\ \ \text{— purely OFF-DIAGONAL, amplitude}\ {-}q;\qquad\text{the smooth moment term's}\ L\leftrightarrow R\ \text{mixing, derived from the quaternion algebra}$$
$$(5)\quad\textbf{THE ANOMALOUS READ (derived, integer-exact, calibration-free):}$$
$$(\mathrm i)\ \ \gamma_{\mathcal F_0}^2=I\implies\mathrm{spec}\{\pm1\}:\quad\boxed{\ \text{the doublet splitting is}\ 2|q|\in\{0,2\};\qquad\textbf{splitting per unit charge}=2\ \textbf{EXACTLY}\ }\qquad\text{the tree-gyromagnetic parallel is FLAGGED,}\ \neg\text{IDENTIFIED,}\ \neg\text{compared}\ [\mathrm{P5};\ \mathrm{Def\text{-}BM.3}(7)];$$
$$(\mathrm{ii})\ \ \textbf{THE EXACT DICHOTOMY:}\ \ \text{the boundary channel is FLICKER-IMMUNE}\ (q\ \text{preserved on}\ \mathcal E(\mathcal X)\ [\mathrm{Def\text{-}BM.5}(1)]\implies\langle\widehat M\rangle_{\mathcal E}=\widehat M\ \text{exactly});\ \ \text{the dressing is FLICKER-SENSITIVE}\ (\aleph\ \text{interior}\ [\mathrm{AT.30}(3)]);$$
$$\boxed{\ \textbf{the ANOMALOUS part IS the fluctuation-derived dressing}\ (-1)^{\aleph}\ }$$
$$(\mathrm{iii})\ \ \textbf{the dressed phase:}\quad\varepsilon_{\mathrm{total}}=i^{\Theta}(-1)^{\aleph}\ [\mathrm{Def\text{-}BM.16}(5)\times\mathrm{Def\text{-}H.32}(2)]\ \ \text{is CLOSED within}\ \{\pm1,\pm i\}\ —\ \text{the eighth-root never appears};$$
$$(\mathrm{iv})\ \ \textbf{the neutral/charged dichotomy:}\quad q{=}0\implies\widehat M{=}0\ \text{but}\ \aleph{>}0\ \text{survives}\ (14/32):\ \ \textbf{the neutral class's moment content is ENTIRELY interior};$$
$$(\mathrm v)\ \ \textbf{NOT derivable, BY DESIGN:}\ \ \text{a continuous}\ a=(g{-}2)/2:\ \ \neg\exists\ \text{a loop, a}\ \beta\text{-function, a counterterm}\ [\mathrm{BM.88}(1)];\ e\ \neg\text{issued}\ [\mathrm{EM.25}(7);\ \mathrm{P4}];\ a_\mu\ \text{targets stay quarantined}\ [\mathrm{P5}]$$
$$(6)\quad\textbf{BM.125(4)'s THREE GROUNDS, PASSED ONE BY ONE:}\qquad(\mathrm i)\ \ \neg\text{a single}\ \Delta(j)\ \text{needed:}\ \widehat M\ \textbf{is operator-valued}, acts ray-by-ray, the BM.124 ladder untouched;$$
$$(\mathrm{ii})\ \ \neg\text{a product of the two Def-H.37 clauses:}\ \widehat M=(\text{an EM read})\times(\text{a Clifford unit})\ —\ \text{one operator, no}\ [m^4];\qquad(\mathrm{iii})\ \ \text{the dimensions close by census: every ingredient is}\ \mathfrak q^0\ —\ \neg\ell_c,\ \neg\hat\mu,\ \neg\mathfrak h;$$
$$\textbf{BM.126(1) untouched:}\ \ \text{the crossing-weight alphabet remains}\ \{\varepsilon_q\}\ \textbf{alone}\ —\ \text{this is a READ on configurations,}\ \neg\text{a reweighting};\ (-1)^{\aleph}\ \text{is A8's own frozen weight}$$
$$(7)\quad\textbf{ADJUDICATION:}\qquad\boxed{\ \textbf{AT-O6 CLOSED AS STRUCTURE for the coupling:}\ \ \text{the anomalous read is the derived integer pair}\ \bigl(2|q|\ \text{boundary splitting};\ (-1)^{\aleph}\ \text{dressing}\bigr)\ }$$
$$\textbf{HARD NO-GO, named:}\ (3)\text{'s vector channel};\qquad\textbf{STILL OPEN:}\ \mathrm{AT.47}\text{'s two slots},\ \text{the global Dirac-type operator},\ \text{the continuous anomaly}\ (5\mathrm v);$$
$$\textbf{BARS UNTOUCHED:}\ \mathrm{FT.55}(1)\ (\widehat M\ \text{contains no}\ \Theta_R),\ \mathrm{BM.134}(5),\ \mathrm{BM.125}(4),\ \mathrm{BM.126},\ \mathrm{FT.93}(3),(4)\ (\text{the contraction uses the SHORTLIST pseudoscalar — AT.47's theorem, not a pincer violation})$$

**Req.** A8 (Part 1); D3.3, D3.4 (Parts 1–2); CT1.2, CT1.12a, CT1.19, CT1.22, EM.9, EM.9b, EM.12, EM.24(1) (Part 2); Def-H.32(2),(5), Def-H.33, Def-H.34, FT.93(2), FT.106(3), FT.108(5), FT.157(1) (Part 3); AT.2(3),(4), AT.6, AT.30(2),(3), AT.34, AT.42(2), AT.44, AT.46, AT.47 (this level); Def-BM.3(7), Def-BM.4(5), Def-BM.5(1), Def-BM.16(5), BM.23(4), BM.88(1), BM.124, BM.125(4), BM.126(1), BM.134(5), BM.137(1), EM.25(7) (Part 4); exhaustive sign enumeration (240 configurations), exact `Gauss(i)` 4×4 identities, `Fraction` ensemble weights [math; machine: `moment_coupling.py` §§A–F, 17/17].

**Pf.**
$$(1):\ \text{the double count cancels}\ [\text{machine: }240\ \text{configurations}];\ (2):\ \mathrm{EM.9b}\ [\text{machine: }120];\ \gamma_{\mathcal F_0}=I\otimes\hat\kappa\ [\mathrm{AT.47}(3)];\ \text{the weak-scalar row re-certified}\ [\text{machine}];\ 14/32\ [\text{machine}];$$
$$(4):\ \hat\kappa|c\rangle=|c\rangle,\ \hat\kappa|\omega(c)\rangle=-|\omega(c)\rangle;\ \{\hat\kappa,\hat\chi\}=0\ \text{entrywise};\ \tfrac12S^\dagger\sigma_3S=\sigma_1\ [\text{machine}];\ (5):\ \text{the spectrum from the matrix per}\ q\in\{-1,0,1\};\ \langle\widehat M\rangle=\widehat M\ \text{via BM.137(1)'s weights summing to }1;\ \varepsilon_{\mathrm{total}}\ \text{closed over}\ \Theta\in2\mathbb Z\ (\mathrm{mod}\ 8)\times\aleph\ [\text{machine}];$$
$$(6):\ \text{the symbol census of}\ \widehat M\text{'s construction};\ (7):\ \text{assembly}.\ \blacksquare$$

**Phys.** Ask the ledger for $\sigma^{\mu\nu}F_{\mu\nu}$ and it answers, first, with a zero: the
total vertex read cancels on every configuration, because every edge is somebody's out and
somebody's in. That cancellation is not a failure — it is the ledger's Gauss law in disguise, and
it forces the question to be asked correctly. What survives is exactly two things. On an *open*
connector — and hydrogen's connector is open, running from the $Q{=}+1$ register to the $Q{=}-1$
one — the interior read telescopes to the boundary charge, and charge times the shortlist
pseudoscalar is an honest operator: diagonal on the two traversals, splitting them by $2|q|$,
anticommuting with the chirality, mixing $L$ and $R$ with amplitude $-q$ — the smooth moment
term's defining behavior, falling out of Def-H.34's quaternion algebra with nothing imported. And
on *every* configuration, closed ones included, the absolute activity $\aleph$ survives — the
non-telescoping residue the A8 weight has been coupling all along as $(-1)^{\aleph}$. The anomalous
read is the pair: a flicker-immune boundary splitting of exactly $2$ per unit charge, and a
flicker-sensitive sign dressing that is the fluctuation-derived correction. The neutral class
carries only the dressing — interior moment content at zero boundary charge — and the fourth-root
phase economy never needs an eighth root. What the ledger cannot give is the vector contraction,
and now we know precisely why: electromagnetism is a stack aspect with zero metric coordinates, so
it has no native index to offer; the smooth coupling *decomposes* into the pseudoscalar channel
built here and the shift-mediated magnetic channel of AT.6, and the missing definition is named to
the symbol. No loop exists, $e$ is unissued, and the continuous anomaly stays a calibration
question by design — BM.125(4)'s three grounds are passed not by dodging but by building an
operator where the refuted ansatz multiplied two masses.

---

### AT.49 — The status of Tier AT.8: adjudication, the consolidated ledger, and the state of the Atomic era

**Thm.**
$$(1)\quad\textbf{DERIVED — the positive content of AT.46–AT.48:}\qquad\begin{array}{l|l}\textbf{the row} & \textbf{the locus}\\\hline\text{the duality tool (D1)--(D6), species bars honored} & \mathrm{AT.46}(1)\\ \text{constant shift}\implies\text{zero holonomy; the forced rotating field gives}\ L(w_0\!\cdot\!\Delta x_0)\ne0 & \mathrm{AT.46}(2)\\ \textbf{the drag is orientation-odd (forward ticks, arc-odd hops)} & \mathrm{AT.46}(3)\\ \textbf{frame-dragging is Diophantine-quantized; the witness attains}\ \Theta_{\min}(3)=6 & \mathrm{AT.46}(4)\\ \text{the doublet splits:}\ k_+-k_-=\Theta_{\mathrm{drag}};\ \hat\chi\widehat D\hat\chi=\widehat D^{-1} & \mathrm{AT.46}(5)\\ \textbf{THE STATISTICS-FLIP LAW:}\ \varepsilon_+\ne\varepsilon_-\iff\Theta_{\mathrm{drag}}\ \text{odd (one geometry, two statistics)} & \mathrm{AT.46}(6)\\ \text{Frenet lift vs exchange sign: distinct reads, agreeing}\ \iff L\ \text{odd}\vee L\equiv2\,(4) & \mathrm{AT.46}(7)\\ \textbf{the spacetime spin factor = Def-H.34's triple: gauge-trivial}\ \mathrm{Cl}(3,0),\ \textbf{MAXIMAL (nullity 0)} & \mathrm{AT.47}(2)\\ \textbf{the relocation:}\ \gamma_{\mathcal F_0}=I\otimes\hat\kappa;\ \text{the pincer is arena-relative} & \mathrm{AT.47}(3)\\ \text{the weak-scalar shortlist: }6\ \text{frames, one S-orbit; no frame fully gauge-trivial} & \mathrm{AT.47}(4)\\ \text{the section} = \text{ONE base frame per floor; shortlist} = \text{the six seed-only singletons} & \mathrm{AT.47}(5)\\ \text{de Moivre exact (105 identities); the fourth-root lattice}\ L\phi\in\tfrac\pi2\mathbb Z & \mathrm{AT.47}(6)\\ \textbf{the unification:}\ \widehat D_{\mathrm{drag}}=\exp(i\tfrac\pi2\Theta_{\mathrm{drag}}\hat\kappa)\ —\ \text{frame datum} = \text{holonomy generator} & \mathrm{AT.47}(7)\\ \text{the Dirac skeleton is chiral-odd for every slot choice} & \mathrm{AT.47}(8)\\ \textbf{the vanishing lemma:}\ \Sigma_v f_v\equiv0\ \text{on every configuration (240 proved)} & \mathrm{AT.48}(1)\\ \textbf{the moment operator identity:}\ \widehat M=-q_{\mathrm{EM}}(I\otimes\hat\kappa)\ (120\ \text{configurations}) & \mathrm{AT.48}(2)\\ \text{the vector contraction is}\ \neg\textbf{formable; the smooth coupling DECOMPOSES into two ledger channels} & \mathrm{AT.48}(3)\\ \widehat M\ \textbf{flips the chirality}\ (\{\widehat M,\hat\chi\}=0);\ \text{chiral basis}\ -q\,I\otimes\sigma_1 & \mathrm{AT.48}(4)\\ \textbf{the anomalous read:}\ (2|q|\ \text{splitting, per-charge}\ 2;\ (-1)^{\aleph}\ \text{dressing});\ \text{immune/sensitive dichotomy} & \mathrm{AT.48}(5)\\ \mathrm{BM.125}(4)\text{'s three grounds passed; BM.126's}\ \{\varepsilon_q\}\ \text{alphabet untouched} & \mathrm{AT.48}(6)\end{array}$$
$$(2)\quad\textbf{THE MEASURED ABSENCES (no-gos with loci, not shrugs):}\qquad\begin{array}{l|l}\textbf{the absence} & \textbf{the exact reason}\\\hline\text{the total vertex contraction vanishes} & \text{each edge counted once out, once in — a census identity}\ [\mathrm{AT.48}(1)]\\ \text{no gauge-trivial fourth gamma} & \text{the commutant is}\ I\otimes\mathrm{End}(\mathcal H_\omega);\ \{A,\sigma_i\}{=}0\implies A{=}0\ \text{(nullity 0)}\ [\mathrm{AT.47}(2)]\\ \text{no native vector EM read} & \text{EM is a stack aspect with ZERO metric coordinates}\ [\mathrm{AT.2}(3),(4);\ \mathrm{AT.48}(3)]\\ \text{no continuous anomaly number} & \neg\exists\ \text{a loop}\ [\mathrm{BM.88}(1)];\ e\ \neg\text{issued}\ [\mathrm{EM.25}(7)]\ —\ \text{by design}\ [\mathrm{AT.48}(5\mathrm v)]\\ \text{no Frenet/exchange identification} & \mathrm{FT.55}(1)\text{'s dimensional bar, witnessed at parity level}\ [\mathrm{AT.46}(7)]\end{array}$$
$$(3)\quad\textbf{MARKED,}\ \neg\textbf{ADOPTED:}\qquad(\mathrm a)\ \text{the lift}\ \triangleright\ [\mathrm{AT.47}(5):\ \text{Def-H.37(2)'s declared identification, Open Gaps 19, inherited at use}];\qquad(\mathrm b)\ \text{the base frame per floor (a menu of six)}\ [\mathrm{AT.47}(4),(5)];$$
$$(\mathrm c)\ \text{the level-price read rule}\ [\mathrm{AT.44}(8\mathrm{iv}),\ \text{continued}];\qquad(\mathrm d)\ \text{specialization (S) and AT.6's magnetic functional up to}\ \varkappa\beta\ [\mathrm{AT.34}(7),\ \text{unchanged}]$$
$$(4)\quad\textbf{SUPERSEDED / RESCOPED, on the record:}\qquad\begin{array}{l|l}\textbf{the row} & \textbf{the disposition}\\\hline\text{item 21(i)'s ``frame section unconstructed''} & \textbf{REDUCED:}\ \text{the carrier, the grading, the shortlist, the transport coupling and the polygon connection are constructed}\ [\mathrm{AT.47}];\ \text{the residue is two enumerated slots}\ (3\mathrm a,\mathrm b)\\ \mathrm{FT.93}(7)\text{'s ``missing spacetime spin factor''} & \textbf{LOCATED AND BUILT:}\ \text{Def-H.34's triple at the R.39 locus, gauge-trivial and maximal}\ [\mathrm{AT.47}(2),(3)];\ \text{what remains missing is the section (reduced) and the global operator}\\ \mathrm{AT\text{-}O6}\ \text{``the anomalous moment''} & \textbf{CLOSED AS STRUCTURE:}\ \text{the coupling is constructed natively}\ [\mathrm{AT.48}];\ \text{the numerical anomaly is calibration-species by P5 design}\\ \text{the directive premises} & \text{corrected at}\ \mathrm{AT.46}(8)\ \text{(P1)--(P3)}: \text{the shift couples through the on-shell locus, the handshake locus is BM.134(5)'s indicator, names stay quoted}\end{array}$$
$$(5)\quad\textbf{THE OPEN LEDGER at this closure:}\qquad\begin{array}{l|l}\textbf{row} & \textbf{why}\\\hline(\mathrm{AT\text{-}O2})\ w_i^\perp\ \text{gauge} & \textbf{BY NATURE:}\ \text{the momentum constraint's multiplier}\ [\mathrm{AT.5}(4),\ \text{unchanged}]\\ (\mathrm{AT\text{-}O3})\ (\varkappa,\beta) & \textbf{BY DESIGN:}\ \text{P4 core,}\ \neg\text{issued}\ [\mathrm{C4};\ \text{§Cal-2}];\ \text{AT.6/AT.34/AT.46 all bottom out here}\\ (\mathrm{AT\text{-}O11})\ \text{the dictionary at}\ n{=}4 & 13\ \text{invariants vs}\ 10\ \text{coordinates; needs}\ \dim\mathcal K_{n\ge4}\ [\text{unchanged}]\\ (\mathrm{AT\text{-}O13})\ \text{the Kerr route} & \textbf{ONE NUMBER AWAY:}\ \text{needs}\ (\mathrm{AT\text{-}O3})\ \text{and nothing structural}\ [\mathrm{AT.34}]\\ (\mathrm{AT\text{-}O14/O16})\ \text{the locked sector} & \textbf{BLOCKED BY A MISSING DIMENSION:}\ \mathrm{CT0.14}\ \text{silent at}\ n\ge4\ [\text{unchanged; still priority 1}]\\ (\mathrm{AT\text{-}O26})\ \text{the read-rule declaration} & \textbf{CLOSURE-PHASE ACT:}\ \mathrm{AT.44}(8\mathrm{iv})\text{'s level price}\ [\mathrm{BM.30}(5)\ \text{pattern}]\\ (\mathrm{AT\text{-}O27})\ \varepsilon_q\text{'s value} & \textbf{CALIBRATION:}\ \tfrac18\ \text{distinguished four ways}\ [\mathrm{AT.40}(1);\ \mathrm{AT.44}(4),(5)],\ \text{adoption}\ \neg\text{issued}\ [\mathrm{P5}]\\ \textbf{new}\ (\mathrm{AT\text{-}O28})\ \text{the global Dirac-type operator} & \textbf{TWO SLOTS AWAY:}\ \text{needs the lift}\ (3\mathrm a)\ +\ \text{the base frame}\ (3\mathrm b);\ \text{the skeleton's graded shape is derived}\ [\mathrm{AT.47}(8)];\ \text{spatial gammas gauge-carrying by}\ \mathrm{AT.47}(2)\\ \textbf{new}\ (\mathrm{AT\text{-}O29})\ \text{a native vector EM read} & \textbf{BY NATURE (proved absence):}\ \text{the stack aspect carries zero metric coordinates}\ [\mathrm{AT.48}(3)];\ \text{reopening would need a new derived read-species, not a construction on this one}\end{array}$$
$$(6)\quad\textbf{the declaration census:}\qquad\textbf{the declarations this tier adds: none.}\qquad\neg\text{a P4 addition},\ \neg\text{a new dimensionful scale}\ [\mathrm{P1}],\ \neg\text{a measured value}\ [\mathrm{P5}],\ \neg\text{a species identification}\ [\mathrm{Def\text{-}BM.3}(7)];$$
$$\text{calibration parameters added:}\ 0;\qquad\text{marked rows:}\ (3)\text{'s four, none adopted};\qquad\text{claims withdrawn:}\ 0\ \ (\text{the corrections are premise-level and recorded at}\ \mathrm{AT.46}(8))$$
$$(7)\quad\textbf{the machine state:}\qquad\texttt{canon/era2/run\_all\_era2.py}\to\textbf{31 checkers, 551 exact markers, 0 failures, exit 0};\qquad\texttt{check\_era2\_format.py}\to\textbf{10 Part 5 documents PASS}\ (\text{math balance, block anatomy, citation attestation against the 640-tag canon registry});$$
$$\text{the shared libraries:}\ \texttt{qexact.py},\ \texttt{duality.py}\ ((\mathrm{D1})\text{–}(\mathrm{D6}),\ \text{registered as a helper beside the runner});\qquad\text{the folder remains deliberately NOT wired into}\ \texttt{verification/run\_all.py};\ \texttt{index/},\ \texttt{tags.json},\ \texttt{Summary.md}\ \neg\text{regenerated}\ —\ \text{promotion stays a closure-phase act}$$
$$(8)\quad\textbf{the era chain:}\qquad\text{every AT-tag of this tier cites Parts 1--4 and earlier AT-tags only.}\ \neg\exists\ \text{a forward pointer used as a premise.}\ \neg\exists\ \text{a circular citation. Acyclic by construction}\ [\text{machine: the format gate's F3}]$$
$$(9)\quad\textbf{THE STATE OF THE ATOMIC ERA:}\qquad\textbf{the structural agenda is complete to the calibration boundary}\ —\ \text{the BM.23 closure shape, second consolidation:}$$
$$\text{grammar}\ [\mathrm{AT.41}]\ \to\ \text{dynamics}\ [\mathrm{AT.42}]\ \to\ \text{the no-go measured}\ [\mathrm{AT.43}]\ \to\ \text{the resolvent, the lepton price, the spectrum}\ [\mathrm{AT.44}]\ \to\ \text{duality + drag + statistics flip}\ [\mathrm{AT.46}]\ \to\ \text{the frame section}\ [\mathrm{AT.47}]\ \to\ \text{the moment coupling}\ [\mathrm{AT.48}];$$
$$\text{between Level 5 and contact stand exactly:}\ \varepsilon_q,\ e_0,\ (\varkappa,\beta),\ \text{the chart-side scales}\ [\mathrm{AT\text{-}O3},\mathrm{AT\text{-}O27}];\ \text{the two declared slots}\ [\mathrm{AT\text{-}O28}];\ \text{the read-rule declarations}\ [\mathrm{AT\text{-}O26}];\ \text{the locked-sector dimension}\ [\mathrm{AT\text{-}O14/O16}];$$
$$\boxed{\ \textbf{coherence is}\ \neg\textbf{contact, and this tier makes no contact claim}\ }\qquad[\mathrm{AT.39}(8)\text{'s standing row, re-cited and unchanged}]$$

**Req.** AT.46, AT.47, AT.48 (this level); P1, P4, P5, C4, §Cal-2, A3, A6, A8, D1.4, D1.5, D1.8, D2.6, D3.3, D3.4 (Parts 1–2); CT1.2, CT1.12, CT1.12a, CT1.19, CT1.22, CT1.23, EW.32, EW.33, EM.9, EM.9b, EM.12, EM.24(1), EM.25(7) (Part 2); Def-H.4, Def-H.21, Def-H.32, Def-H.33, Def-H.34, Def-H.37(2), FT.13, FT.22, FT.24, FT.25, FT.28, FT.32(6), FT.55, FT.93, FT.105, FT.106(3), FT.108, FT.122(6), FT.157, item 21(i) (Part 3); AT.2, AT.5, AT.6, AT.10, AT.30, AT.34, AT.36(3), AT.39, AT.40, AT.41, AT.42, AT.43, AT.44, AT-O2, AT-O3, AT-O6, AT-O11, AT-O13, AT-O14, AT-O16, AT-O19, AT-O26, AT-O27 (this level); Def-BM.3(7), Def-BM.4, Def-BM.5(1), Def-BM.16(5), Def-BM.18, BM.6(8), BM.8(2), BM.19, BM.23(4), BM.34, BM.83, BM.88(1), BM.96, BM.121, BM.123, BM.124, BM.125(4), BM.126(1), BM.132, BM.133, BM.134(5), BM.136(4), BM.137 (Part 4); row-wise assembly only — no new mathematics at this tag [math; machine: all three AT.8 checkers + `check_era2_format.py`].

**Pf.** Row-wise assembly of AT.46–AT.48, each row re-citing its own machine section and its own
locus; the format gate re-run over all ten Part 5 documents; the suite re-run end to end. No new
mathematics is introduced at this tag. $\blacksquare$

**Phys.** This tier began with a change of basis and ended with an operator. The duality — chart on
one side, ledger on the other, species bars between them — was adopted as a tool, and the first
thing the tool showed is that frame-dragging in a forward-only ledger is an *integer*: the drag
enters through the mixed term alone, FT.22 quantizes it, and the calibration product lands on a
Diophantine lattice whose first witness attains the odd-ladder minimum with the minimal materialized
edge value. The second thing it showed is that orientation is physical twice over: the drag splits
the doublet's windings, and at odd drag it splits their *statistics* — one geometry, two exchange
classes, no smooth limit anywhere. Then the frame section, which the corpus had named as missing
data in three places, turned out to be hiding behind a theorem: the spacetime spin factor was
already built (Def-H.34's triple), gauge-trivial and — the new impossibility — maximal, so the
fourth gamma must carry the gauge index or not exist. The relocation row made the hiding place
exact: FT.93's example pseudoscalar *is* Def-H.34's partner involution, one matrix, two arenas, a
pincer that binds only where the weak action is $3\oplus1$. And the moment coupling, asked of the
ledger honestly, gave its zero first — the total vertex read cancels always — and then its two
survivors: the charge-chirality operator on open connectors, splitting the doublet by exactly two
per unit charge and flipping the chirality as the smooth moment term must, and the activity sign
the A8 weight has carried since Part 1. The anomalous read is the pair, and the dichotomy is the
content: the boundary part is flicker-immune, the anomalous part is the fluctuation itself. What
the era still owes is exactly what it has always owed — values, not structure — and the ledger of
what is missing now fits in nine rows, each with a reason.
