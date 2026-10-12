# $\langle qu(b(i(t|t))ick)\rangle$ — **Part 5 · Atomic era** — Tier AT.9: the locked sector, the electroweak curl, and the dressed vertex

**Level.** 5. **Era.** 2 (the Atomic era). **Tier.** AT.9 — the rung-4 mask dimension and the
locked-sector adjudication, the electroweak complement and the curl mechanism, and the
ledger-native vertex correction: the moment operator in the fully dressed topology-blind
ensemble.
**Tags.** AT.50–AT.55. **Pattern.** BM.130 / BM.144 / BM.152 — the construction tiers and the
status-and-closure tag of a tier.
**Status.** discovery-phase working tier, **closed at AT.55**. Nothing is adopted into the frozen
canon; no declaration issues; §Cal-AT stays empty; no clause of Parts 1–4 is modified, retracted
or renumbered. Session 4's candidates AT.50/AT.51 (discovery record
`canon/era2/RUNG4_EW_CURL.md`) are consolidated here, content unchanged; session 5's candidates
AT.52–AT.54 (discovery record `era2/VERTEX_CORRECTION.md`) are new.
**Machine.** `canon/era2/rung4_ew_curl.py` → **13/13 exact** (AT.50, AT.51);
`canon/era2/vertex_correction.py` → **23/23 exact** (AT.52–AT.54);
`canon/era2/run_all_era2.py` → **33 checkers, 587 exact markers, 0 failures, exit 0**;
`canon/era2/check_era2_format.py` → the format + citation gate over all eleven Part 5 documents.
Exact arithmetic: integers (the aspect and cover censuses, the exhaustive biconditional and
subset scans), `Fraction`, `Gauss(i)` 4×4 identities, symbolic polynomials in $\mathbb Q[g,g']$
and $\mathbb Q[u]$ with coefficient-wise equality, exhaustive sign enumerations to $2^{16}$.
**No floating point in any assertion. No calibration parameter receives a value. No measured
value enters [P5].**
**Charter.** Part 5 cites Parts 1–4 and earlier AT-tags only.
**Mandate.** Two Architect directives, executed in order: **(i)** (session 4) compute
$\dim\mathcal K_{n\ge4}$ by CT0.14's own method and adjudicate the locked sector (AT-O14/O16);
plus the Architect's hypothesis — electroweak the EM, the $\mathfrak{su}(2)$ complementary dual
outside a colour seal — as a mechanism curling a "photon" chain into a polygon or platonic solid;
**(ii)** (session 5) derive the ledger-native vertex correction: evaluate the moment operator
$\widehat M$ [AT.47(3); AT.48(2a); Def-H.43] in the FULLY DRESSED topology-blind ensemble of the
lepton–baryon composite — the $k$-channel resolvent [AT.44] and the Janus move system
[Def-H.32(7)] beyond the tree-level $k{=}1$ pole, the frozen cover census [FT.106(3); Census
FT.69] — isolate the shift $\delta$ between the dressed and tree ensemble averages of
$\widehat M$, adjudicate BM.125(4)'s three grounds, check the AT-O11 dictionary gap,
and close AT-O6 or locate the obstruction exactly. Standing instruction honored throughout:
*no-gos are level-local — verified, never trusted* [AT.39 Phys; SESSION_SUMMARY §3].

---

## Tier AT.9 — the locked sector, the curl, and the dressed vertex

### AT.50 — $\dim\mathcal K_4 = 26$ by a four-row squeeze, the flag terminates, and the lock is a biconditional
**Thm.**
$$(1)\quad\textbf{THE METHOD RE-EXECUTED (CT0.14's own):}\qquad\dim\mathcal K_n=\sum_{A\in\mathcal A(n)}\dim\mathcal K^{(A)}\ [\mathrm{D2.3}];\qquad\text{the census}\ [\mathrm{CT0.12}/\mathrm{CT0.13}/\mathrm{CT3.8}]:$$
$$J^\pm\ 3{+}3\ |\ G\ 5\ |\ W\ 3\ |\ H\ 1\ |\ D^+\ 1\ (\text{the pair arena},\ 16=C_{\mathrm{cap}})\ |\ \mathrm{EM}\ 1=\dim Z(\mathfrak u(2))\ |\ \text{strong}\ 8=\dim\mathfrak{su}(3)\ |\ D^-\ =\ \text{the unknown};$$
$$\text{reproducing on the nose}\quad\dim\mathcal K_{0..3}=(6,16,17,25)\ \ [\text{machine}]$$
$$(2)\quad\textbf{THE SQUEEZE:}\qquad\dim\mathcal K^{(D^-)}\ge1:\ \ \mathrm{CT0.14}\ \text{freezes}\ \mathcal K_3\subset\mathcal K_{n\ge4}\ \textbf{STRICT};$$
$$\dim\mathcal K^{(D^-)}\le1:\ \ \mathrm{CT4.4}\ \text{``scalar sink,}\ \neg\text{internal directions, contributes}\ \neg\text{generator''}\ +\ \mathrm{D4.1}\ \text{``SINGLE possibility space receiving ALL rung-}\ge4\ \text{configurations'' (the}\ \oplus\ \textbf{collapses}\ [\mathrm{CT4.1}])$$
$$+\ \mathrm{CT4.6}\ \text{``stack block}\perp\text{pair space; gauge content none; disjoint''}\ +\ \mathrm{CT4.4a}(1)\ \text{``no generators, no internal directions''};$$
$$\boxed{\ \dim\mathcal K^{(D^-)}=1\ \ \text{(four frozen rows, no new datum)}\ }\qquad\boxed{\ \dim\mathcal K_4=25+1=26\ }$$
$$(3)\quad\textbf{THE FLAG TERMINATES:}\qquad\mathcal A(n\ge4)=\mathcal A(3)\cup\{D^-\}\ \text{is the SAME set at every}\ n\ge4\ [\mathrm{CT0.13}]\implies\boxed{\ \dim\mathcal K_n=26\ \ \forall n\ge4\ }:\qquad 6\subset16\subset17\subset25\subset26=26=26=\cdots$$
$$\text{the stack registers grow}\ 1\ (\mathrm{EM},\ \text{rung }2),\ 8\ (\text{strong},\ \text{rung }3),\ 1\ (D^-\ \text{scalar},\ \text{rung}\ge4);\qquad\text{the pair arena saturates at}\ 16\ \text{by rung}\ 1\ [\mathrm{CT0.14}\ \mathrm{Rmk}]$$
$$(4)\quad\textbf{THE LOCK IS A BICONDITIONAL (not a contingency):}\qquad\text{for every}\ n=0..16\ [\text{machine}]:$$
$$\boxed{\ D^-\in\mathcal A(n)\iff n\ge4\iff D_{\mathrm{tick}}(n)=2^{n+1}\ge32>16=C_{\mathrm{cap}}\iff n\ \textbf{NOT channel-admissible}\ }\qquad[\mathrm{CT0.13}+\mathrm{CT0.5}/\mathrm{CT0.6}/\mathrm{CT0.11}/\mathrm{CT4.1}]$$
$$\textbf{activation and admissibility are DISJOINT at every rung};\qquad\text{rung }3\ \text{is the last admissible rung AND exactly saturated}\ (D_{\mathrm{tick}}(3)=16=C_{\mathrm{cap}})$$
$$(5)\quad\textbf{THE ADJUDICATION — the third branch the dichotomy did not list:}\qquad(\mathrm i)\ n\le3:\ \mathcal P_M^{(n)}F_{D^-}\mathcal P_M^{(n)}=0\ [\mathrm{CT4.2}]\ \text{— masked (re-certified at block level);}$$
$$(\mathrm{ii})\ n\ge4:\ \mathcal K^{(D^-)}\subseteq\mathcal K_n\ [\mathrm{D2.3}+\mathrm{CT0.13}]\implies\text{the formal projection does}\ \neg\text{annihilate the sink —}\ \textbf{NONZERO AS A FORMAL OBJECT};$$
$$(\mathrm{iii})\ \text{but}\ \iota_4\ \text{is}\ \neg\text{realized}\ (32>16\ [\mathrm{CT4.4a}(1)]),\ \text{the accessible vertex sets are}\ \{V_0..V_3\}\ [\mathrm{CT0.11}],\ \text{and every accessible subnetwork mask runs at rung}\le3\ [\mathrm{AT.16}(4),(5)];$$
$$(\mathrm{iv})\ \text{and even at the formal unlocking there is NOTHING TO READ: structureless}\ [\mathrm{CT4.4}],\ \text{dust}\ w=0\ [\mathrm{CT4.5}],\ \text{entropy maximal and locked}\ [\mathrm{CT4.7}],\ \text{retained}\ \neg\text{accessible}\ [\mathrm{CT4.3};\ \mathrm{D1.11};\ \mathrm{D4.2}],\ \text{``no construction could exist inside the bound''}\ [\mathrm{BM.143}(1)/(\mathrm{P3})];$$
$$\boxed{\ \textbf{NONZERO-BUT-UNREACHABLE: the locked sector is provably unreadable at EVERY accessible rung; AT-O14/O16 CLOSED}\ }$$
$$(6)\quad\textbf{consequence for AT-O11:}\qquad\text{AT.40 sharpened it to ``which invariant is conjugate to which coordinate — a question with a definite answer ONCE}\ \dim\mathcal K_{n\ge4}\ \text{is known'';}$$
$$\dim\mathcal K_{n\ge4}=26\ \textbf{is now known}\implies\textbf{AT-O11 is fully decidable}\ (13\ \text{free invariants at}\ n{=}4\ \text{against the}\ 26\text{-dimensional mask space)}$$
$$(7)\quad\textbf{status:}\qquad\textbf{derived:}\ (1)\text{–}(6);\qquad\neg\text{a declaration},\ \neg\text{a P4 addition},\ \neg\text{a new scale}\ [\mathrm{P1}],\ \neg\text{a measured value}\ [\mathrm{P5}];\qquad\text{``dark''}\ \text{stays quoted vocabulary}\ [\mathrm{AT.18's}\ \neg\text{adopted naming row}]$$

**Req.** A8 (Part 1); CT0.5, CT0.6, CT0.11, CT0.11a, CT0.11b, CT0.12, CT0.13, CT0.14, D2.3, D4.1, D4.2, D1.11 (Part 1); CT3.8, CT4.1, CT4.2, CT4.3, CT4.4, CT4.4a, CT4.5, CT4.6, CT4.7 (Part 2); AT.16(4),(5), AT.18, AT.28, AT.30(7), AT.40 (this level); BM.143(1), BM.149(2) (Part 4); exact integer aspect arithmetic, the exhaustive biconditional census $n=0..16$ [math; machine: `rung4_ew_curl.py` §I, 6/6].

**Pf.** $(1)$: the census re-summed [machine I-A1]; $(2)$: the four frozen rows quoted at their loci [machine I-A2]; $(3)$: $\mathcal A(n\ge4)$ constant [machine I-A3]; $(4)$: $2^{n+1}$ vs $16$ over $n=0..16$ [machine I-B1]; $(5)$: the block-inclusion rows + CT4.4a(1)'s non-realization [machine I-B2]; $(6)$: AT.40's own conditional discharged; $(7)$: assembly. $\blacksquare$

**Phys.** The corpus left one number on its own table — the dimension of the mask at the rung
where the dark aspect wakes — and the number was hiding behind a squeeze that four frozen rows
already contain. The strictness of the flag demands at least one new direction; the sink's own
description (scalar, single, structureless, generator-free) forbids more than one. So the flag
$6\subset16\subset17\subset25$ ends at $26$ and stays there forever: rung 4 adds one direction and
every rung above adds nothing, because there is only ever one sink. And the adjudication of the
locked sector comes out sharper than either branch of the posed dichotomy. The rung-4 projection
does *not* annihilate $D^-$ — formally, the sink unmasked itself the moment it activated. But
activation and admissibility are the *same inequality read twice*: $D^-$ wakes exactly at the
rungs where $2^{n+1}$ outruns the sixteen-dimensional pair arena, so the mask that could read the
sink is a mask no vertex can ever wear. The lock is not a wall held against a pushing reader; it
is a biconditional. And even at the formal unlocking the sink has nothing to say — no charges, no
generators, dust equation of state, maximal locked entropy. What falls in stays in, and what stays
in was never structured to begin with.

---

### AT.51 — The electroweak complement outside the seal, and the curl mechanism (the Architect's hypothesis, verified and bounded)
**Thm.**
$$(1)\quad\textbf{(H1)+(H2) THE COMPLEMENT AND ITS CO-ACTIVATION:}\qquad\dim\mathcal K^{(\mathrm{EM})}=\dim Z(\mathfrak u(2))=1\ [\mathrm{CT0.14}\ \mathrm{Pf}];\qquad\dim F_W=\dim\mathfrak{su}(2)=3\ [\mathrm{CT0.12}];\qquad\boxed{\ 3+1=4=\dim\mathfrak u(2)\ }$$
$$\mathcal A(2)=\mathcal A(1)\cup\{\mathrm{EM}\}\ [\mathrm{CT0.13}]\implies\textbf{NO rung exists with EM active and W inactive}\ [\text{machine:}\ n{=}0..12];\qquad\text{outside a colour seal the active gauge content of a colour-neutral carrier is exactly this}\ \mathfrak u(2)$$
$$(2)\quad\textbf{(H3) THE BRANCH GATE:}\qquad\text{the seed is colour-neutral}\ (T_a\mathsf v=0\ [\mathrm{EW.32}]);\qquad\textstyle\sum_iW_i^2=2\Pi_{\mathcal R}\ [\mathrm{Cor}\ \mathrm{CT0.7a}]\ \text{and}\ W_i\Pi_{\mathcal V}=0\ \forall i\ [\mathrm{FT.101}(1),(2);\ \text{machine: exact }4\times4\ \text{over}\ \mathbb Q(i)];$$
$$\text{the weak acts on the ALIGNED (spatial,}\ \vee^2,\ \alpha=0)\ \text{branch and annihilates the ANTIALIGNED (temporal,}\ \wedge^2,\ \alpha=\pi)\ \text{one}\ [\mathrm{FT.157}(2);\ \mathrm{AT.13}]:\ \textbf{only the weak-active branch can be curled by the su(2) complement}$$
$$(3)\quad\textbf{(H4) THE CURL MECHANISM, four derived steps:}\qquad(\mathrm a)\ \text{the topology-blind sum CONTAINS the closed configurations}\ [\mathrm{Def\text{-}H.32}(1)];\ \text{open transit}\ S=0\ \text{vs closed}\ \Theta=2k\ [\mathrm{Def\text{-}H.32}(4);\ \mathrm{FT.22}];$$
$$(\mathrm b)\ \text{the branch gate}\ (2);\qquad(\mathrm c)\ \textbf{the curl proceeds THROUGH COVERS:}\ \text{a lone directed cycle is amplitude-DEAD}\ (v_\Gamma(R)=0\ [\mathrm{FT.106}(2);\ \mathrm{BM.32}(5)]),\ \text{dissolved digons inside covers are amplitude-LIVE at winding one with the frozen exact integers}\ Z^{\mathrm{amp}}(q,1)=802\ (q{=}\pm1),\ 4796\ (q{=}0)\ [\mathrm{FT.106}(3);\ \mathrm{BM.111}(4)];$$
$$(\mathrm d)\ \textbf{THE CLOSURE DETECTOR IS THE TRANSPORT GRAM:}\qquad m^2_{\mathrm{pole}}(c)=\hat\mu^2\ell_c^2G(c)\ [\mathrm{Def\text{-}H.37}(1);\ \mathrm{EW.33}];$$
$$G(c)=c^TMc,\qquad M=\tfrac14N^TN,\qquad N=\left(\begin{smallmatrix}g&0&0&0\\0&g&0&0\\0&0&g&g'\end{smallmatrix}\right):\qquad\text{PSD, rank }3,\ \ \text{spectrum}\ \{g^2,g^2,0,g^2+g'^2\}/4\ [\mathrm{BM.36}];$$
$$\ker M=\ker N=\mathrm{span}\{(0,0,g',-g)\}\ [\text{machine: exact annihilation, coefficient-wise}]=\ \textbf{the ``photon'' profile};$$
$$\boxed{\ G(c)=\tfrac14\|Nc\|^2=0\iff c\ \text{on the kernel line}:\ \ \textbf{a curled photon profile stays MASSLESS at every coupling, every off-kernel profile curls into a pole mass}\ }$$
$$\text{on the family circle:}\ G(c(i))=A_0-B_0\cos(\delta-\tfrac{2\pi i}3)\ge A_0-B_0=\tfrac38(g-\tfrac{g'}3)^2+\tfrac{g'^2}{48}>0\ [\mathrm{Def\text{-}BM.11}(5);\ \mathrm{BM.39}(1);\ \mathrm{BM.96}(3);\ \text{machine: SOS identity in}\ \mathbb Q[g,g']]$$
$$(4)\quad\textbf{(H5) THE BOUND ON THE HYPOTHESIS:}\qquad\text{a curled COLOUR-NEUTRAL chain forms}\ \textbf{POLYGONS}\ —\ \text{the 2D floors,}\ \Theta_R=0\ \text{identically at every}\ n\ [\mathrm{FT.54}(4)\ \text{on flat floors}];$$
$$\text{but NOT platonic solids: the 3D seals are}\ \varepsilon/\delta\ \text{junctions on COLOUR slots}\ [\mathrm{D3.9};\ \mathrm{CT3.17a}(1)]\ \text{and the EW seed is colour-neutral}\ [\mathrm{EW.32}];\ \text{the platonic floors carry colour attachments (the six-state quark assembly [Tier BM.14])};$$
$$\boxed{\ \textbf{``polygon or platonic solid'' SPLITS: polygons YES (colour-neutral curl); platonic IFF colour attachments are present}\ }$$
$$(5)\quad\textbf{status:}\qquad\textbf{the hypothesis is CONFIRMED as assembled derived structure}\ —\ \neg\text{a new axiom},\ \neg\text{a declaration},\ \neg\text{a calibration value};\qquad\textbf{NEW AT L5:}\ \text{the}\ \mathfrak u(2)\ \text{pairing row}\ (3{+}1{=}4)\ \text{as the complement statement},\ \text{the four-step curl mechanism},\ \text{the kernel-line curl immunity},\ \text{the polygon/platonic split};$$
$$\text{``photon''}\ \text{stays the kernel-line profile's quoted name}\ [\mathrm{Def\text{-}BM.3}(7);\ \mathrm{P5}];\qquad\text{the curl's ABSOLUTE rates remain}\ \mathrm{BM.6}(5)\text{-calibration}\ [\mathrm{CT0.3}];\qquad\text{the identification of the curled states with any species is}\ \neg\text{formed}$$

**Req.** A4, A8 (Part 1); CT0.12, CT0.13, CT0.14, CT1.4, CT0.7a, EW.24, EW.32, EW.33, EW.35 (Part 2); Def-H.32(1),(4), Def-H.37(1), FT.22, FT.54(4), FT.101(1),(2), FT.106(2),(3), FT.157(2) (Part 3); AT.13, AT.44(5), AT.50 (this level); Def-BM.3(7), Def-BM.11(5), BM.6(5), BM.28(4), BM.32(5), BM.36, BM.39(1), BM.96(3), BM.111(4), D3.9, CT3.17a(1), Census FT.42(5) (Part 4); CT0.3; exact integer dimension arithmetic, `Gauss(i)` 4×4 Casimir/annihilation identities, symbolic Gram factorization and SOS identity over $\mathbb Q[g,g']$ [math; machine: `rung4_ew_curl.py` §II, 7/7].

**Pf.** $(1)$: $\dim Z(\mathfrak u(2))=1$, $\dim\mathfrak{su}(2)=3$ [CT0.14 Pf; CT0.12]; the activation census [machine II-A1]; $(2)$: $\Sigma_iW_i^2=2\Pi_{\mathcal R}$ and $W_i\Pi_{\mathcal V}=0$ entrywise over $\mathbb Q(i)$ with $W_i=\tfrac12(\sigma_i\otimes I+I\otimes\sigma_i)$ [machine II-A2]; $(3)$: $M=\tfrac14N^TN$ expanded coefficient-wise; $Nv=0=Mv$ at $v=(0,0,g',-g)$; $\mathrm{tr}\,M=(3g^2+g'^2)/4$; the SOS $A_0-B_0=\tfrac38(g-\tfrac{g'}3)^2+\tfrac{g'^2}{48}$ as a polynomial identity [machine II-B1,B2]; the frozen integers $802=2\cdot401$, $4796=2\cdot2398$, $\tfrac{4796}{802}=\tfrac{2398}{401}$ [machine II-B3]; $(4)$: the colour-slot loci re-cited; $(5)$: assembly. $\blacksquare$

**Phys.** The Architect's eye was right, and the canon had already laid every brick. Electromagnetism
in this corpus was never alone: the rung that switches on the abelian aspect is a rung on which the
weak su(2) has been active since rung one, and the two fit as centre and derived algebra of one
$\mathfrak u(2)$ — one dimension plus three, exactly four, inside the saturated sixteen-dimensional
pair arena. Outside a colour seal that $\mathfrak u(2)$ is the whole gauge story of a neutral
carrier, and it comes with a curl mechanism in four derived steps: the topology-blind sum already
contains the closed shapes; the branch index decides whether the weak can act on the chain at all;
the amplitude layer insists the curl happen *through covers* — a lone cycle is amplitude-dead, and
the frozen integers 802/4796 price the live winding-one curls; and the transport Gram reads the
closure as mass. That last step is the jewel: the Gram of the seed generators is a rank-three sum
of squares whose kernel line is precisely the photon profile, so a curled photon stays massless at
every coupling while anything off the kernel curls into a pole mass, strictly positive on the
family circle by an SOS identity. The hypothesis also met its bound: a colour-neutral curl reaches
the polygon ladder — flat floors, zero holonomy defect — and stops there. Platonic solids are
colour-sealed junctions; the photon does not speak colour. Polygon yes, platonic iff quarks are in
the room. Nothing was declared, nothing fitted, no species named: the mechanism is the assembled
derived structure, and its absolute rates wait, as always, on the calibration era.

---

### AT.52 — The dressed ensemble: the resolvent's residues and contact term, the winding revival ladder $B_{\min}(m) = 2m + \lceil m/2\rceil$, and the lock parity of the tight bound

**Thm.**
$$(1)\quad\textbf{THE DRESSED RESOLVENT, EXACTLY PARTIAL-FRACTIONIZED WITH RESIDUES AND CONTACT.}\ \ R_k(z)=\sum_{m\ge0}N_k(2m)\,z^m,\quad z:=w^2x_+x_-\ \ [\mathrm{AT.44}(1),(2);\ \mathrm{FT.108}(5);\ \mathrm{Def\text{-}H.32}(7)]:$$
$$\boxed{\ R_k(z)\ =\ c_k\ +\ \sum_{d\in\{k,k-2,\dots\}>0}\frac{a_{k,d}}{1-d^2z},\qquad a_{k,d}=2^{1-k}\binom{k}{(k+d)/2}\in\mathbb Q,\qquad c_k=2^{-k}\binom{k}{k/2}\ [k\ \text{even}],\ 0\ [k\ \text{odd}]\ }$$
$$\text{the sum rule}\quad c_k+\sum_d a_{k,d}=R_k(0)=1\quad\text{holds exactly}\qquad[\text{machine: coefficient-wise in}\ \mathbb Q\ \text{to}\ z^{14},\ k=1..8];$$
$$k{=}1:\ a_{1,1}{=}1,\ c_1{=}0\ \text{— the bare zig-zag verbatim}\ [\mathrm{BM.121}(2)];\qquad k{=}2:\ a_{2,2}{=}\tfrac12,\ c_2{=}\tfrac12$$
$$(2)\quad\textbf{THE ATTENUATION ROWS — RATIONAL, CLOSED FORM, CALIBRATION-FREE:}\qquad\text{the dominant residue}\ \ a_{k,k}=2^{1-k}\ \ \text{(geometric,}\ k\le16\text{);}$$
$$\text{the fixed-}d\ \text{ladders are monotone:}\quad d{=}1:\ \Bigl(1,\tfrac34,\tfrac58,\tfrac{35}{64},\dots\Bigr)\ \text{strictly decreasing over}\ k{=}1,3,5,7,\dots;\qquad d{=}2:\ \Bigl(\tfrac12,\tfrac12,\tfrac{15}{32},\tfrac7{16},\dots\Bigr)\ \text{with the exact plateau}\ a_{2,2}{=}a_{4,2}{=}\tfrac12;$$
$$\boxed{\ \textbf{the contact diversion:}\ \ c_k=\Bigl(\tfrac12,\tfrac38,\tfrac5{16},\tfrac{35}{128},\tfrac{63}{256}\Bigr)\ \text{at}\ k=(2,4,6,8,10),\quad c_k=0\ \text{at every odd}\ k\ }$$
$$\textbf{an even channel count moves the exact rational fraction}\ c_k\ \textbf{of the return weight OFF the pole ladder entirely — flicker attenuation IS rational}$$
$$(3)\quad\textbf{THE INTERLEAVINGS:}\qquad N_k(2m)=2^{-k}\textstyle\sum_j\binom kj(2j-k)^{2m}\ \ \text{re-derived (brute-force return words}\ \wedge\ \text{closed form,}\ k\le3,\ 2m\le8\text{)}\ [\mathrm{AT.44}(1)];$$
$$\text{the dominant pole radius}\ \frac1{k\sqrt{x_+x_-}}\ \ \text{re-derived}\ \bigl(\max_j|2j-k|=k,\ k\le12\bigr)\ [\mathrm{AT.44}(3)]:\qquad\boxed{\ \textbf{dressing costs convergence}\ }$$
$$(4)\quad\textbf{THE WINDING REVIVAL LADDER (supersedes the scope of FT.106(3c)'s death row, constructively):}\qquad\textbf{FT.106(3c)'s ``amplitude death of}\ k\ge2\textbf{'' is the}\ B{=}4\ \textbf{census total},\ \neg\textbf{a general law}:$$
$$\text{Census}\ \mathrm{FT.69}(3)(\mathrm v)/(5)\ \text{already FREEZES}\ 504\ \text{four-cycles inside cube covers and}\ 672\ \text{inside octahedron covers}\ (14\,832\ \text{instances at the cube});$$
$$\textbf{the general theorem, proved:}\qquad\boxed{\ \textbf{every winding}\ m\ge1\ \textbf{is amplitude-live from budget}\ \ B_{\min}(m)=2m+\lceil m/2\rceil\ }$$
$$\textbf{the bound (hand):}\ \ \text{a}\ 2m\text{-cycle in a cover alternates}\ m\ \text{centres}\ /\ m\ \text{hubs}\ [\mathrm{FT.69}(3)];\ \ \text{on-cycle centres are SATURATED}\ (\text{type}\ (1,1)\ =\ \text{exactly their two cycle edges}),$$
$$\text{so each hub's extra edge}\ [\mathrm{FT.69}(3)(\mathrm{ii})]\ \text{is read by an OFF-cycle centre, and an off-cycle centre reads at most two hub extras}\ (\text{its single in- and out-edge})\ \implies\ \lceil m/2\rceil\ \text{off-cycle vertices};$$
$$\textbf{the tight witnesses (machine,}\ m{=}1..5\text{):}\qquad\begin{array}{c|ccccc}m&1&2&3&4&5\\\hline V&3&5&8&10&13\\ |R|&4&6&10&12&16\\ |\mathcal C|&2&3&5&6&8\\ v=4^{|\mathcal C|}&16&64&1024&4096&65536\\ \text{lockL}&1&0&1&0&1\end{array}$$
$$\text{each}\ \operatorname{cov}\equiv1\ \text{machine-exact; each classifier}\ =\ \text{brute-force sign sum}\ (\text{exhaustive to}\ |R|\le16);\ \ \text{each}\ 2m\text{-cycle on-shell at}\ S=m\ (\kappa\equiv1,\ \Theta=2m\ [\mathrm{FT.32}(6);\ \mathrm{FT.107}(1)]);$$
$$m{=}1\ \textbf{IS}\ \mathrm{FT.69}(5)\text{'s locked double-digon hub};\qquad\textbf{ODD cycles stay dead at EVERY budget: a triangle cannot alternate}\ [\mathrm{FT.69}(3)(\mathrm{iv})\ \text{— the literal-domain theorem, re-certified}]$$
$$(5)\quad\textbf{THE MINIMAL WINDING-2 COVER — the theta pattern (new witness,}\ V{=}5,\ |R|{=}6\text{):}\qquad R=\{(0{\to}1),(1{\to}2),(2{\to}3),(3{\to}0),(1{\to}4),(4{\to}3)\}:$$
$$\text{the}\ 4\text{-cycle}\ 0{\to}1{\to}2{\to}3{\to}0\ \text{with on-cycle centres}\ \{0,2\},\ \text{hubs}\ \{1,3\},\ \text{ONE off-cycle centre}\ 4\ \text{threading}\ 1{\to}4{\to}3:\qquad\operatorname{cov}(e)=1\ \forall e;\qquad v=64=4^3=2^{|R|};$$
$$\textbf{it is a THETA: TWO distinct}\ 4\text{-cycles}\ —\ (0,1,2,3)\ \textbf{and}\ (0,1,4,3),\ \text{sharing the}\ 2\text{-edge path}\ 3{\to}0{\to}1\ —\ \text{both on-shell at}\ S{=}2,\ 4\ \text{bases each:}\ \boxed{8\ \text{amplitude-live winding-2 instances in the smallest cell}}$$
$$\textbf{minimality, EXHAUSTIVE:}\quad V\le4:\ \text{ZERO covers with a}\ 4\text{-cycle among all}\ 4095\ \text{patterns of the bidirectional}\ K_4\ \ (\mathrm{FT.106}(3\mathrm c)\text{'s row re-derived as budget-local});$$
$$V{=}5:\ \text{every}\ 4..8\text{-edge subset of the bidirectional}\ K_5\ \text{scanned}\ (262\,599):\ \ \text{exactly}\ 60\ \text{distinct covers with a}\ 4\text{-cycle, ALL at}\ |R|{=}6,\ \text{each with TWO}\ 4\text{-cycles, ONE isomorphism class};\ \neg\exists\ \text{at}\ |R|{=}7,8;$$
$$60=5\cdot4\cdot3=(\text{hub-out},\ \text{hub-in},\ \text{shared-path centre})\ \text{choices}=30\ \text{directed}\ 4\text{-cycles}\times4\ \text{completions}\,/\,2;\qquad\text{the tetrahedron's}\ 48+16\ \text{digon-covers reproduced exactly}\ [\mathrm{FT.69}(4),(5)]$$
$$(6)\quad\textbf{THE LOCK PARITY OF THE TIGHT LADDER (new derived row):}\qquad\boxed{\ \textbf{odd windings are born LOCKED; even windings born clean}\ }\qquad\text{lockL}=(1,0,1,0,1)\ \text{for}\ m{=}1..5\ (4);$$
$$\textbf{pigeonhole:}\ \ m\ \text{odd}\ \implies\ \lceil m/2\rceil\ \text{off-cycle centres supply}\ m{+}1\ \text{hub-endpoints to}\ m\ \text{hubs}\ \implies\ \text{one hub carries}\ \ge2\ \text{extras}\ \implies\ k_v=4\ \implies\ \textbf{locked}\ [\mathrm{CT4.5};\ \mathrm{CT0.11}];$$
$$m{=}3\ \text{cell}\ (V{=}8,\ |R|{=}10,\ v{=}1024,\ \text{brute force}):\ \ \text{BOTH tight threadings lock}\ —\ \text{the shared-target variant at hub type}\ (3,1),\ \text{the wrap variant at}\ (2,2);$$
$$\textbf{the first UNLOCKED winding-3 cover sits at}\ V{=}9\ (\text{one graft threaded to a sink}),\ \operatorname{cov}\equiv1,\ v=1024,\ \text{lockL}=0\ [\text{machine}];$$
$$\text{structural parallel to the odd-winding}\leftrightarrow\text{fermionic-sign row}\ [\mathrm{FT.32}(6);\ \mathrm{BM.113}(4)]:\ \ \textbf{FLAGGED},\ \neg\textbf{IDENTIFIED}\ [\mathrm{P5};\ \mathrm{Def\text{-}BM.3}(7)]$$
$$(7)\quad\textbf{THE}\ k{=}2\ \textbf{CONNECTOR CELL, amplitude-live:}\qquad\text{the double-thread hub}\ \{(1{\to}2),(1{\to}4),(2{\to}3),(4{\to}3)\}:\ \ \text{source-hub}\ (0,2)\to\ \text{two centres}\to\ \text{sink-hub}\ (2,0):$$
$$\operatorname{cov}\equiv1,\qquad v=4^2=16\ (\text{brute force})\qquad\textbf{AT.44's two-channel floor as a concrete configuration}\ [\mathrm{FT.67}(3\mathrm d)\text{'s V-thread grammar};\ \mathrm{BM.137}(1)\text{'s independent pairs}]$$
$$(8)\quad\textbf{status:}\qquad\textbf{derived:}\ (1)\text{--}(7);\qquad\textbf{re-scoped on the record},\ \neg\textbf{retracted:}\ \ \mathrm{FT.106}(3\mathrm c)\text{'s death row}\ =\ \text{the}\ B{=}4\ \text{slice of}\ (4)\text{'s ladder};$$
$$\text{the census integers are amplitude-layer STRUCTURAL reads, barred as mass reads}\ [\mathrm{BM.111}(6);\ \mathrm{FT.79}(5);\ \mathrm{BM.30}(5)];\qquad\neg\text{a declaration},\ \neg\text{a P4 addition},\ \neg\text{a measured value}\ [\mathrm{P5}]$$

**Req.** A7, A8 (Part 1); CT0.9, CT0.11, CT4.5, EM.9 (Part 2); Def-H.32(1),(2),(3),(4),(5),(7), FT.22, FT.28, FT.32(6), FT.67(1),(2),(3), FT.69(3),(4),(5), FT.79(2), FT.105, FT.106(2),(3), FT.107(1), FT.108(4),(5), D0.8, D1.4 (Parts 1, 3); Census FT.69(3)(v),(5) (row-wise); AT.42(1),(2), AT.44(1),(2),(3),(5), AT.48(1),(2) (this level); Def-BM.3(7), Def-BM.5(1),(2),(3), BM.19(2), BM.30(5), BM.32(5), BM.111(4),(6), BM.113(4), BM.120(1), BM.121(1),(2), BM.137(1),(4) (Part 4); exact integer cover censuses (exhaustive $2^{12}$ and $262\,599$-subset scans), brute-force sign sums to $2^{16}$, `Fraction` partial-fraction algebra coefficient-wise in $\mathbb Q[[z]]$ [math; machine: `vertex_correction.py` §§A–B, 9/9].

**Pf.**
$$(1):\ \ \bigl[z^m\bigr]\ \text{of both sides}:\ \ N_k(2m)=2^{-k}\textstyle\sum_j\binom kj\bigl((2j-k)^2\bigr)^m=\bigl[z^m\bigr]\bigl(c_k+\sum_d a_{k,d}\sum_m d^{2m}z^m\bigr)\ \text{with the}\ \pm d\ \text{pairing}\ \binom kj{=}\binom k{k-j}\ [\text{machine A1}];$$
$$(2):\ \ a_{k,k}=2^{1-k}\binom kk;\ \ \text{the ladder values entrywise};\ \ c_k>0\iff k\ \text{even}\ [\text{machine A2}];\qquad(3):\ \ \text{word enumeration}\ =\ \text{closed form};\ \max_j|2j-k|=k\ \text{at}\ j\in\{0,k\}\ [\text{machine A3}];$$
$$(4):\ \ \text{the bound: alternation}\ [\mathrm{FT.69}(3)]\ +\ \text{saturation of on-cycle centres}\ [\text{type}\ (1,1)]\ +\ \text{two extras per off-cycle centre};\ \ \text{the witnesses:}\ \operatorname{cov}\ \text{entrywise},\ \text{classifier}\ =\ \text{brute force},\ \Theta=2m\ [\text{machine B4}];$$
$$(5):\ \ \operatorname{cov}\ \text{entrywise};\ 2^6\ \text{signs brute force}\ =64;\ \ \text{the two}\ 4\text{-cycles enumerated};\ \ V\le4:\ 4095\ \text{patterns};\ \ V{=}5:\ 262\,599\ \text{subsets},\ \text{canonical forms under all}\ 120\ \text{relabelings}\ [\text{machine B1--B3}];$$
$$(6):\ \ \text{the pigeonhole count};\ \text{both}\ V{=}8\ \text{threadings and the}\ V{=}9\ \text{unlock entrywise}\ [\text{machine B4,B5}];\qquad(7):\ \ \operatorname{cov}\ \text{entrywise};\ 2^4\ \text{signs}\ [\text{machine C2b}];\qquad(8):\ \ \text{assembly}.\ \blacksquare$$

**Phys.** The directive asked for the higher-order connector configurations beyond the tree pole,
and the ledger answered in two registers. The dynamical register: the $k$-channel resolvent does
not merely partial-fractionize — it does so with exact rational residues and, at every even
channel count, an exact rational contact term that carries weight off the pole ladder entirely.
Dressing attenuates in closed form: the dominant residue halves per channel, the fixed-level
residues fall in monotone rational ladders, and the convergence radius tightens as $1/k$ — the
move system's own statement that a dressed connector is harder to close than a bare one. The
structural register corrected the record: the "amplitude death" of winding $\ge2$ that the frozen
B=4 census reported is a budget artifact, and the canon already knew it — the cube and octahedron
covers carry hundreds of dissolved four-cycles. What was missing was the minimum, and the minimum
is a five-vertex theta: two four-cycles sharing a two-edge path, threaded through one off-cycle
centre, worth $4^3$ at winding two with eight live instances. From there the whole ladder opens
with a tight formula — $2m + \lceil m/2\rceil$ vertices for winding $m$ — proved by a counting
argument the alternation lemma forces, and witnessed machine-exact five rungs deep. The ladder
also carries a parity signature: at the tight bound, odd windings cannot avoid doubling up on one
hub, and doubling locks, so every tight odd-winding cover carries lock content while every tight
even-winding cover is clean — the locked double-digon family the corpus froze at the tetrahedron
is the $m{=}1$ step of this law, not an exception. The parallel to the exchange-sign parity is
flagged and not identified, as always. And the $k{=}2$ connector is no abstraction: the
double-thread hub is a four-edge cover of value sixteen, enumerated, weighed, and censused like
everything else here.

---

### AT.53 — The moment operator on the dressed ensemble: the chain-local telescoping, the discrete Ward identity $\delta = 0$, the $\omega$-split, and the master parity identity

**Thm.**
$$(1)\quad\textbf{THE CHAIN-LOCAL TELESCOPING EXTENSION (Level-5 lemma; EM.9b's locus untouched).}\ \ \text{EM.9b freezes}\ \sum_i f_{v_i}=\tfrac12(\sigma_{e_k}-\sigma_{e_1})\ \text{for chains whose interior vertices are type}\ (1,1);$$
$$\textbf{the algebra extends chain-locally:}\ \ \text{on EVERY simple open path of EVERY configuration of both witness skeletons}\ (17+61\ \text{paths};\ 124+1248\ \text{sign evaluations}),$$
$$\boxed{\ \sum_{\text{chain interiors}}f_v=\tfrac12\bigl(\sigma_{\text{last}}-\sigma_{\text{first}}\bigr)\ \ \textbf{IDENTICALLY — including paths whose interior vertices are HUBS of type}\ (2,1),(1,2),(3,1),(2,2)\ }$$
$$\text{the frozen}\ (1,1)\ \text{clause is a SCOPE,}\ \neg\text{an obstruction};\qquad\text{the cyclic sum vanishes on every cycle}\ (32+144\ \text{evaluations})\ [\mathrm{AT.48}(1)\ \text{transported}]$$
$$(2)\quad\textbf{SECTOR CONSTANCY (machine census).}\ \ \text{The full instance-resolved}\ (q,S)\ \text{census of both witness skeletons}\ (3^6=729\ \text{and}\ 3^{10}=59\,049\ (\text{pattern},\sigma)\ \text{configurations};$$
$$\text{both layers; the theta skeleton at}\ (t,u){=}(1,1)\ \textbf{and}\ (3/4,1/4)):\qquad\widehat M(\text{inst})=-q(\text{inst})\,(I_2\otimes\hat\kappa)\ \ [\mathrm{Def\text{-}H.43};\ \mathrm{AT.47}(3);\ \mathrm{AT.48}(2\mathrm a)]$$
$$\textbf{is the SAME}\ 4\times4\ \textbf{operator on every instance of a sector}\ (q\ \text{is the sector label}),\ \text{and distinct sectors carry distinct operators};$$
$$\text{on closed-chain instances}\ (S\ge1)\ \text{the vertex-contraction channel vanishes}\ [\mathrm{AT.48}(1)]\ \text{while the promoted}\ \mathrm{FT.40}\ \text{closed-core read does not: two reads of one aspect, kept apart}\ [\mathrm{BM.134}(5)\ \text{pattern}]$$
$$(3)\quad\textbf{THE DISCRETE WARD IDENTITY (the vertex correction, evaluated):}\qquad\boxed{\ \delta\ :=\ \bigl\langle\widehat M\bigr\rangle_{\mathrm{dressed}}-\bigl\langle\widehat M\bigr\rangle_{\mathrm{tree}}\ =\ 0\ \ \textbf{EXACTLY}\ }$$
$$\text{the genuine instance-weighted mean}\ \bigl(\sum_i w_i\widehat M(q_i)\bigr)\big/\sum_i w_i,\ \text{computed from the census charge sums, equals}\ -q\,(I_2\otimes\hat\kappa)\ \text{entrywise}$$
$$\text{in EVERY sector}\ (q,S),\ \text{at BOTH layers, at BOTH fugacity specializations — an exact}\ \mathrm{Gauss}(i)\ 4\times4\ \text{identity};\qquad\textbf{the boundary splitting}\ 2|q|\ [\mathrm{AT.48}(5\mathrm i)]\ \textbf{is}\ \neg\textbf{renormalized by any flicker, interleaving, cover or winding}$$
$$\textbf{three independent supports:}\ \ (1)\text{'s chain-local telescoping incl. hub interiors};\quad\text{the charge preservation on}\ \mathcal E(\mathcal X)\ [\mathrm{Def\text{-}BM.5}(1)];\quad(2)\text{'s sector constancy}$$
$$(4)\quad\textbf{NON-VACUITY — the}\ \omega\textbf{-split of the amplitude layer (sharpens FT.106(3b)/(3d) per cell):}\qquad\sigma\mapsto-\sigma\ \text{forces}\ \operatorname{contrib}_R(-q)=(-1)^{|R|}\operatorname{contrib}_R(q):$$
$$\boxed{\ \text{norm layer, cover support}\ (|R|=2|\mathcal C|\ \text{even}\ [\mathrm{FT.79}(2)]),\ \text{and non-cover EVEN support:}\ \omega\textbf{-SYMMETRIC};\qquad\text{non-cover ODD support:}\ \omega\textbf{-ANTISYMMETRIC}\ }$$
$$\implies Z^{\mathrm{amp}}_{\mathrm{ncO}}(0,S)=0\ \ \textbf{exactly — the neutral sector receives no odd non-cover amplitude support};$$
$$\text{the hexagon cell exhibits the asymmetry LIVE:}\quad Z^{\mathrm{amp}}(-1,0)=11\,348\ \ \text{vs}\ \ Z^{\mathrm{amp}}(+1,0)=19\,060,\qquad\text{difference}=2\times(-3856)=\ \text{exactly twice the odd non-cover part};$$
$$\text{the unconditioned norm-layer mixed averages collapse to}\ \langle q\rangle_{\mathrm{ens}}=0\ —\ \text{the neutral operator, by derived symmetry};\qquad\textbf{the ensemble moves the operator read ONLY through the sector MIX, never inside a sector}$$
$$(5)\quad\textbf{THE MASTER PARITY IDENTITY (sharpens AT.48(5ii)):}\qquad\boxed{\ (-1)^{\aleph(R,\sigma)}\ =\ \prod_{e:\ \operatorname{cov}(e)\ \mathrm{odd}}\sigma_e\ \ \textbf{on EVERY configuration}\ }\qquad(668+59\,049\ \text{checked in-census, zero violations});$$
$$\text{FT.67}(1)\text{'s per-centre identity}\ (-1)^{|f_v|}=\sigma_{e_\leftarrow}\sigma_{e_\rightarrow}\ \text{multiplied out};\qquad\textbf{corollaries (exhaustive):}$$
$$\text{single open chains}\ L{=}2..9:\ \ (-1)^{\aleph}=(-1)^{|q|};\qquad\text{closed chains}\ L{=}2..7:\ \ (+1);\qquad\text{covers}:\ (-1)^{\aleph}=\prod_e\sigma_e\ (\operatorname{cov}\equiv1);$$
$$\boxed{\ \textbf{the frozen A8 dressing SIGN is SECTOR-LOCKED: the flicker CANNOT flip it}\ }\qquad\bigl(|f|\equiv f\ \mathrm{mod}\ 2\ \text{termwise};\ \textstyle\sum_{\mathrm{int}}f_v=-q\bigr)$$
$$\text{the A8-dressed operator}\ (-1)^{\aleph}\widehat M=(-1)^{|q|}\widehat M\ \ \textbf{is ALSO sector-constant on single-chain configurations};\qquad\varepsilon_{\mathrm{total}}=i^{\Theta}(-1)^{|q|}\ \ \text{closes in the fourth roots}\ [\mathrm{Def\text{-}BM.16}(5)];$$
$$\text{pointwise:}\quad\aleph-|q|\in2\mathbb Z_{\ge0}\ \ (\text{exhaustive})\qquad\textbf{RECORD:}\ \ \mathrm{AT.48}(5\mathrm{ii})\text{'s ``dressing flicker-SENSITIVE'' is REFINED,}\ \neg\text{retracted — }\aleph\text{'s VALUE fluctuates}\ [\mathrm{AT.54}(1)];\ \text{its PARITY is charge data}$$
$$(6)\quad\textbf{status:}\qquad\textbf{derived:}\ (1)\text{--}(5);\qquad\text{the lemma}\ (1)\ \text{extends EM.9b's scope at Level 5; EM.9b's frozen locus is untouched};\qquad\neg\text{a declaration},\ \neg\text{a calibration value},\ \neg\text{a species identification}\ [\mathrm{P5};\ \mathrm{Def\text{-}BM.3}(7)]$$

**Req.** A8 (Part 1); CT4.5, EM.9, EM.9b, FT.40 (Part 2); Def-H.32(2),(3),(4),(5), Def-H.33, Def-H.34, Def-H.43, FT.22, FT.67(1),(2), FT.79(2), FT.106(3), FT.108(4), D0.8, D1.4, D3.3 (Parts 1–3); AT.44, AT.47(3), AT.48(1),(2),(4),(5) (this level); AT.52 (this level); Def-BM.5(1),(2), Def-BM.16(5), BM.121(2), BM.134(5), BM.137(1),(4) (Part 4); the exhaustive census engine ($3^6$, $3^{10}$ configurations, instance-resolved, both layers), exact `Gauss(i)` 4×4 identities, `Fraction`-weighted means [math; machine: `vertex_correction.py` §C, 5/5].

**Pf.**
$$(1):\ \ \text{the interior sum telescopes as a polynomial in the path's own signs — verified on every path of both skeletons under every assignment}\ [\text{machine C1}];\ \ \text{cyclic sums: the double count cancels}\ [\mathrm{AT.48}(1)\ \text{pattern}];$$
$$(2):\ \ \text{the census groups instances by}\ (q(\text{inst},\sigma),S)\ \text{and compares}\ 4\times4\ \text{operators entrywise}\ [\text{machine C2}];\qquad(3):\ \ \bigl(\sum_i w_i q\bigr)/\sum_i w_i=q\ \text{in}\ \mathbb Q\ \text{per sector}\ \implies\ \text{the operator identity}\ [\text{machine C3}];$$
$$(4):\ \ w(R,-\sigma)=(-1)^{|R|}w(R,\sigma)\ \wedge\ q(c,-\sigma)=-q(c,\sigma)\ [\mathrm{Def\text{-}H.32}(2);\ \mathrm{EM.9}]\ \implies\ \text{the three-way split};\ \text{the census exhibits each part}\ [\text{machine C3}];$$
$$(5):\ \ (-1)^{\aleph}=\prod_{v\in\mathcal C}(-1)^{|f_v|}=\prod_{v\in\mathcal C}\sigma_{e_\leftarrow(v)}\sigma_{e_\rightarrow(v)}=\prod_e\sigma_e^{\operatorname{cov}(e)}=\prod_{\operatorname{cov}\ \mathrm{odd}}\sigma_e\ [\mathrm{FT.67}(1)];\ \ \text{the corollaries: exhaustive}\ [\text{machine C4}];\qquad(6):\ \ \text{assembly}.\ \blacksquare$$

**Phys.** The dressed ensemble was built, the moment operator was applied, and the ledger's
answer is a cancellation with a content. The cancellation first: the vertex correction to the
operator read vanishes identically — not perturbatively, not by a symmetry imported from the
chart, but because the record's own algebra protects it three times over. The interior reads
telescope to the end registers even when the connector threads hubs the frozen lemma never
covered; the ensemble preserves the boundary data by its own definition; and the promoted read
depends on nothing but the sector label. So the tree splitting of two per unit charge survives
every flicker, every interleaving, every dissolved cycle the budget can host — the discrete
cousin of the Ward identity, with the telescoping playing the role of gauge invariance. The
content second: the cancellation is not emptiness. The amplitude layer splits into three exact
$\omega$-classes under the sign involution, and the odd non-cover class is antisymmetric — which
both explains the frozen census's "cancelling support" remark as a mechanism and exhibits live
charge-asymmetric integers, eleven-thousand against nineteen-thousand, in a cell small enough to
enumerate by hand. And the dressing sign itself, which the previous tier called flicker-sensitive,
turns out to be sector-locked: the master parity identity reduces $(-1)^{\aleph}$ to a product of
odd-covered edge signs, so on a single chain it is $(-1)^{|q|}$ and the fluctuation cannot touch
it. What fluctuates is the magnitude, and magnitude lives on the measure layer — exactly where
the next tag finds it, in rationals.

---

### AT.54 — The anomalous read: the exact rational measure content, position versus residue, and BM.125(4)'s three grounds

**Thm.**
$$(1)\quad\textbf{THE}\ \aleph\textbf{-EXCESS MEANS (the flicker attenuation, exact rationals):}\qquad\text{per}\ (L,q):\quad\langle\aleph\rangle=\frac{L-1}2\ [L\ge3],\qquad\langle\aleph\rangle=|q|\ [L{=}2,\ \text{the minimal cell}]\qquad[\text{exhaustive}\ L{=}2..9];$$
$$\text{on the}\ \mathrm{BM.137}(1)\ n\text{-pair-floor measure}:\qquad\boxed{\ \langle\aleph\rangle^{(n)}=\frac{\sum_{j\ge1}\binom nj p^ju^{n-j}\,g(2j)}{1-u^n},\qquad g(2)=|q|,\quad g(2j)=\frac{2j-1}2\ [j\ge2]\ }\qquad[\text{a POLYNOMIAL IDENTITY in}\ \mathbb Q[u],\ n{=}1..6];$$
$$\text{at detailed balance}\ \varepsilon_q=\tfrac18\ (u{=}\tfrac12):\qquad\langle\aleph\rangle^{(2)}=\tfrac76\implies\boxed{\text{excess}=\tfrac16}\ (q{=}\pm1);\qquad\langle\aleph\rangle^{(3)}=\tfrac{10}7\implies\boxed{\text{excess}=\tfrac37};$$
$$\textbf{the anomalous magnitude is a rational function of}\ \varepsilon_q\ \textbf{ALONE — calibration-free — and it never touches the operator layer}\ [\mathrm{AT.53}(3)]$$
$$(2)\quad\textbf{THE FIRST AMPLITUDE-LIVE WINDING-2/3 SECTOR CENSUSES (new derived integers).}\ \ \text{ENGINE CERTIFIED against two frozen rows:}\ \mathrm{BM.137}(4)\text{'s budget-2 pincer}\ Z_2^{\mathrm{norm}}(q,1)=(4,2,2)\ \text{at}\ q{=}(0{+}1{-}1),$$
$$\text{and}\ \mathrm{FT.106}(3\mathrm b)\text{'s cancelling support at the smallest cell:}\ Z_2^{\mathrm{amp}}(0,1){=}{+}4,\ Z_2^{\mathrm{amp}}(\pm1,1){=}(-2,-2),\ \text{summing to EXACTLY}\ 0;\qquad\text{the norm layer matched to}\ \mathrm{FT.106}(3\mathrm a)\text{'s closed form}\ m_q2^{|R|-2}\ \text{per instance};$$
$$\text{new rows at}\ (t,u){=}(1,1),\ \text{as}\ (Z^{\mathrm{amp}};\ Z^{\mathrm{norm}})\ \text{at}\ q{=}(-1,0,{+}1):\qquad\begin{array}{l|lll}\text{cell}&S{=}0&S{=}2&S{=}3\\\hline\text{theta skeleton}\ (V{=}5)&(263,622,263);\ (1071,2142,1071)&\mathbf{(128,256,128);\ (288,576,288)}&—\\ \text{hexagon skeleton}\ (V{=}8)&(11348,37832,19060);\ (217728,435456,217728)&(912,2272,912);\ (11664,23328,11664)&\mathbf{(2816,6656,2816);\ (15552,31104,15552)}\end{array}$$
$$\text{with the exact three-way split}\ Z^{\mathrm{amp}}=Z^{\mathrm{cov}}+Z^{\mathrm{amp}}_{\mathrm{ncE}}+Z^{\mathrm{amp}}_{\mathrm{ncO}}\ \text{per sector}\ [\mathrm{AT.53}(4)];\qquad\text{the cover part is exactly}\ 2{:}1\ \text{between}\ q{=}0\ \text{and}\ q{=}\pm1\ \text{everywhere}\ (m_q\ \text{factorization on covers});$$
$$\boxed{\ \textbf{the winding-2/3 rows are the first amplitude-live higher-winding sector integers in the corpus}\ }\qquad\text{the minimal-budget companions of}\ \mathrm{FT.106}(3)\text{'s frozen}\ B{=}4\ \text{table}\ (802/4796;\ 1196/5336)$$
$$(3)\quad\textbf{POSITION vs RESIDUE — the Lamb-analog row:}\qquad\text{the pole positions}\ W_d=1/(d^2x_+x_-)\ \text{are}\ k\textbf{-INDEPENDENT: the}\ 1/d^2\ \text{ladder is exactly position-degenerate across channel counts}\ [\mathrm{AT.44}(5)\ \text{transport};\ \text{machine}\ d\le6,\ k\le12];$$
$$\text{the dressing splits the degeneracy in the RESIDUES}\ a_{k,d}\ (4\ \text{distinct values at}\ d{=}1\ \text{over}\ k{=}1,3,5,7;\ 3\ \text{at}\ d{=}2\ \text{incl. the plateau}\ \tfrac12)\ \text{and in the contact}\ c_k\ —\ \ \textbf{NEVER in the positions};$$
$$\boxed{\ \textbf{the ledger's Lamb analog is an INTENSITY redistribution at unshifted level prices}\ }\qquad\text{a frequency shift would need a position-moving dressing; the move system has none — exact,}\ \neg\text{approximate};$$
$$\text{the level-price read rule stays the marked specification}\ [\mathrm{AT.44}(8\mathrm{iv});\ \mathrm{AT\text{-}O26}],\ \text{unchanged here}$$
$$(4)\quad\textbf{the frozen ratio, re-certified:}\qquad\frac{4796}{802}=\frac{2398}{401}\ne2=\frac{m_0}{m_{\pm1}}\qquad(401\ \text{PRIME};\ 2398=2\cdot11\cdot109)\qquad[\mathrm{BM.111}(4);\ \mathrm{FT.106}(3),(3\mathrm a)];$$
$$\textbf{the dressing breaks the charge degeneracy at the amplitude layer and can never break it at the operator layer}\ [\mathrm{AT.53}(3)];\qquad\text{amplitude}\ne\text{mass discipline intact}\ [\mathrm{BM.111}(6);\ \mathrm{FT.79}(5);\ \mathrm{BM.30}(5)]$$
$$(5)\quad\textbf{BM.125(4)'s THREE GROUNDS, bypassed one by one:}\qquad(\mathrm i)\ \ \neg\text{a single}\ \Delta(j)\ \text{needed: the evaluation is an OPERATOR-VALUED ensemble average, ray-by-ray on}\ \mathcal H_\omega,\ \text{sector-constant};$$
$$\text{the winding content enters as the}\ S\text{-graded census}\ (2)\ \text{and the revival ladder}\ [\mathrm{AT.52}(4)]\ —\ \mathrm{BM.124}\text{'s multiplet ladder never collapsed};$$
$$(\mathrm{ii})\ \ \neg\text{a product of the two Def-H.37 clauses: the symbol census of the construction is}\ \{q,\ \aleph,\ \hat\kappa,\ N_k,\ \binom kj,\ \varepsilon_q,\ t,\ u\}\ —\ \neg\ell_c,\ \neg\hat\mu,\ \neg\Theta_R,\ \neg G(c),\ \neg\Delta(m);\ \ \mathrm{BM.125}(3)\text{'s matching never invoked};$$
$$(\mathrm{iii})\ \ \text{the dimensions close by census: every ingredient is}\ \mathfrak q^0\ —\ \text{a PRICE in the HistLog}\ \S\mathrm{V.32}\ \text{species};\ \ \text{the refuted ansatz's}\ [\ell_c]{=}\mathfrak q^0\ \text{contradiction cannot arise};$$
$$\textbf{BM.126(1) untouched:}\ \ \text{the channel count}\ k\ \text{is the connector floor's pair count}\ [\mathrm{BM.137}(1)]\ —\ \text{configuration data},\ \neg\text{a spin read};\ \ a_{k,d}\ \text{are binomials of the derived partial fractionization},\ \neg\text{a reweighting}\ x_\pm\mapsto x_\pm(k);$$
$$\text{the measure is the derived stationary one}\ [\mathrm{FT.108}(4);\ \mathrm{Def\text{-}BM.5}(3)];\qquad\text{grounds}\ (\mathrm O1)\text{--}(\mathrm O4)\ \neg\text{engaged}$$
$$(6)\quad\textbf{THE CONTINUOUS ANOMALY: LEVEL-LOCAL NO-GO with three named missing definitions (the AT.43 classification pattern):}$$
$$(\mathrm{M1'})\ \ \text{a declared read rule mapping the measure-side rationals}\ \{a_{k,d},\ c_k,\ \langle\text{excess}\rangle,\ \text{sector weights}\}\ \text{to a chart-currency moment shift}\ (\mathrm{AT\text{-}O26}\text{-class; a closure-phase declaration});$$
$$(\mathrm{M2'})\ \ \text{the value of}\ \varepsilon_q\ [\mathrm{AT\text{-}O27}];\qquad(\mathrm{M3'})\ \ \text{the chart-side scale and}\ e_0\ [\mathrm{P4};\ \mathrm{EM.25}(7)];$$
$$\textbf{sharper than AT.48(5v): not merely ``no loop exists''}\ [\mathrm{BM.88}(1)]\ \textbf{but NO CONTINUOUS LOCUS exists — every dressed operator read is sector-constant}\ [\mathrm{AT.53}(3),(5)];$$
$$\text{absent}\ (\mathrm{M1'})\text{--}(\mathrm{M3'}):\ \ \text{the splitting}\ 2|q|\ \text{stands unrenormalized and the dressing is integers and rationals — by construction,}\ \neg\text{by failure}$$
$$(7)\quad\textbf{status and quarantine:}\qquad\textbf{derived:}\ (1)\text{--}(5);\qquad\textbf{level-local no-go, classified:}\ (6);\qquad a_e,\ a_\mu,\ a_\mu/a_e\approx1.0054,\ \text{the Lamb shift},\ 2S\text{--}2P:\ \ \textbf{quarantined scoring targets}\ [\mathrm{P5}],\ \neg\text{inputs},\ \neg\text{compared};$$
$$\text{the tree-level ``parallel'' (splitting}\ 2\ \text{per unit charge) remains FLAGGED},\ \neg\textbf{IDENTIFIED}\ [\mathrm{AT.48}(5\mathrm i);\ \mathrm{Def\text{-}BM.3}(7)];\qquad\neg\text{a declaration},\ \neg\text{a P4 addition},\ \neg\text{a new dimensionful scale}\ [\mathrm{P1}]$$

**Req.** A8 (Part 1); P1, P4, P5, EM.25(7) (Parts 1–2); Def-H.32(3),(5), FT.67(1), FT.79(2),(5), FT.106(3), FT.108(4) (Part 3); HistLog §V.32 (the price species, row-wise); AT.43, AT.44(5),(8), AT.48(3),(5), AT.52, AT.53 (this level); AT-O6, AT-O26, AT-O27 (this level); Def-BM.3(7), Def-BM.5(3), BM.30(5), BM.88(1), BM.111(4),(6), BM.124(4), BM.125(3),(4), BM.126(1),(2), BM.137(1) (Part 4); binomial moment algebra over $\mathbb Q[u]$ (polynomial identities, $n\le6$), exhaustive enumeration, exact gcd and primality by trial division [math; machine: `vertex_correction.py` §§D–E, 8/8].

**Pf.**
$$(1):\ \ \text{the interior signs are free given the ends}\ \implies\ \text{each of the}\ L{-}1\ \text{gaps flips with weight}\ \tfrac12\ [L\ge3];\ \ L{=}2\ \text{deterministic};\ \ \text{the floor identity coefficient-wise in}\ \mathbb Q[u]\ \text{and at three exact witnesses}\ [\text{machine D1}];$$
$$(2):\ \ \text{the engine on the frozen cells first}\ [\text{machine D2}];\ \ \text{then the witness skeletons};\ \ \text{the closed form}\ m_q2^{|R|-2}\ \text{per instance re-summed independently}\ [\mathrm{FT.106}(3\mathrm a)\ \text{pattern}];$$
$$(3):\ \ W_d\ \text{reads}\ d\ \text{alone}\ [\mathrm{AT.44}(5)];\ \ a_{k,d}\ \text{entrywise distinct across}\ k\ [\text{machine D3}];\qquad(4):\ \ \gcd(4796,802)=2;\ \ 401\ \text{prime by trial division to}\ \lfloor\sqrt{401}\rfloor\ [\text{machine D4}];$$
$$(5):\ \ \text{the symbol census of the construction};\ \ \text{the}\ \mathfrak q\text{-exponent rows}\ [\text{machine E1--E4}];\qquad(6),(7):\ \ \text{the classification and quarantine records}.\ \blacksquare$$

**Phys.** The operator layer came back protected, so the anomaly had to live somewhere else — and
the ledger says exactly where: on the measure, in rationals. The activity magnitude averages to
half-gaps-per-edge on any connector of length three or more, and on the flicker measure of an
$n$-pair floor its excess over the charge is a rational function of the crystallization threshold
alone — one sixth at two pairs, three sevenths at three, at the distinguished balance point. The
dressed resolvent splits each level's weight into a residue that attenuates by exact binomials as
channels are added and, at every even channel count, a contact fraction that leaves the pole
ladder altogether; and the level positions never move. That is the shape of the corpus's Lamb
analog: not a frequency shift — the move system has no position-moving dressing — but an
intensity redistribution at unshifted prices, with the first amplitude-live winding-two and
winding-three sector integers now censured at their minimal budgets, companions to the frozen
table at budget four. The three grounds that killed the naive product ansatz die nowhere near
this construction: it is operator-valued, it multiplies no masses, and every symbol in it is
dimensionless. What remains genuinely missing is named to the symbol — a read rule, a threshold
value, a chart scale — and until those are declared or calibrated, the honest statement is the
strong one: the splitting of two per unit charge is exact and unrenormalized at every order of
dressing the ledger can form, the correction content is integer and rational, and the continuous
anomaly has no locus, not merely no value.

---

### AT.55 — The status of Tier AT.9: adjudication, the consolidated ledger, and the state of the Atomic era

**Thm.**
$$(1)\quad\textbf{the consolidated ledger of the tier:}\qquad\begin{array}{l|l}\textbf{row}&\textbf{the disposition}\\\hline\dim\mathcal K_{n\ge4}=26,\ \text{the terminated flag},\ \text{the activation/admissibility biconditional}&\textbf{DERIVED by a four-row squeeze}\ [\mathrm{AT.50}];\ \ \mathrm{AT\text{-}O14/O16}\ \textbf{CLOSED}\\\text{the locked sector}&\textbf{NONZERO-BUT-UNREACHABLE: the third branch}\ [\mathrm{AT.50}(5)]\\\text{the}\ \mathfrak u(2)\ \text{complement}\ (3{+}1{=}4),\ \text{the four-step curl},\ \text{kernel-line immunity},\ \text{polygon/platonic split}&\textbf{the Architect's hypothesis CONFIRMED as assembled derived structure}\ [\mathrm{AT.51}]\\\text{the dressed resolvent: residues}\ a_{k,d},\ \text{contact}\ c_k,\ \text{the revival ladder}\ B_{\min}(m){=}2m{+}\lceil m/2\rceil,\ \text{lock parity}&\textbf{DERIVED}\ [\mathrm{AT.52}]\\\text{the vertex correction}&\delta=0\ \textbf{EXACTLY — the discrete Ward identity}\ [\mathrm{AT.53}(3)]\\\text{the dressing sign}&\textbf{SECTOR-LOCKED:}\ (-1)^{\aleph}=(-1)^{|q|}\ [\mathrm{AT.53}(5)]\\\text{the anomalous read}&\textbf{measure-side rationals: excess means, residues, sector integers; positions unmoved}\ [\mathrm{AT.54}]\\\mathrm{AT\text{-}O6}&\textbf{CLOSED AS DRESSED STRUCTURE}\ [\mathrm{AT.48}\ \text{coupling};\ \mathrm{AT.53}\ \text{evaluation}];\ \ \text{the continuous anomaly: level-local no-go,}\ (\mathrm{M1'})\text{--}(\mathrm{M3'})\ [\mathrm{AT.54}(6)]\\\mathrm{AT\text{-}O11}&\textbf{DOES NOT BLOCK this tier: zero dictionary calls}\ [\mathrm{AT.54}\ \text{scope};\ \mathrm{AT.50}(6)\ \text{decidability stands}]\\\text{the directive premises}&\text{corrected on the record:}\ \mathrm{FT.106}(3\mathrm c)\text{'s death row is}\ B{=}4\text{-local}\ [\mathrm{AT.52}(4)];\ \ \mathrm{AT.48}(5\mathrm{ii})\text{'s sensitivity refined}\ [\mathrm{AT.53}(5)]\end{array}$$
$$(2)\quad\textbf{THE PROVED ABSENCES (each with its ground):}\qquad\begin{array}{l|l}\textbf{absence}&\textbf{the ground}\\\hline\neg\text{a}\ 4\text{-cycle cover at}\ V\le4&\text{exhaustive}\ (4095\ \text{patterns})\ [\mathrm{AT.52}(5)];\ \ \text{revives at}\ V{=}5\ \text{(the theta)}\\\neg\text{an odd cycle in ANY cover, ANY budget}&\text{a triangle cannot alternate}\ [\mathrm{FT.69}(3)(\mathrm{iv});\ \mathrm{AT.52}(4)]\\\neg\text{an unlocked tight odd-winding cover}&\text{pigeonhole}\ \implies\ \text{a}\ k_v{=}4\ \text{hub}\ [\mathrm{AT.52}(6);\ \mathrm{CT4.5}]\\\neg\text{a renormalization of the boundary splitting}&\text{telescoping}\ +\ \text{charge preservation}\ +\ \text{sector constancy}\ [\mathrm{AT.53}(1)\text{--}(3)]\\\neg\text{a flicker flip of the dressing sign}&\text{the master parity identity}\ [\mathrm{AT.53}(5)]\\\neg\text{a position shift of the}\ 1/d^2\ \text{ladder}&\ W_d\ \text{reads}\ d\ \text{alone}\ [\mathrm{AT.54}(3);\ \mathrm{AT.44}(5)]\\\neg\text{a continuous}\ a=(g{-}2)/2&\neg\text{a loop}\ [\mathrm{BM.88}(1)];\ \ e\ \neg\text{issued}\ [\mathrm{EM.25}(7)];\ \ \neg\text{a continuous locus}\ [\mathrm{AT.53}(3)];\ \ (\mathrm{M1'})\text{--}(\mathrm{M3'})\ [\mathrm{AT.54}(6)]\\\neg\text{a native vector EM read}&\text{the stack aspect carries zero metric coordinates}\ [\mathrm{AT.48}(3),\ \text{unchanged}]\end{array}$$
$$(3)\quad\textbf{SUPERSEDED / RESCOPED / REFINED, on the record:}\qquad\begin{array}{l|l}\textbf{the row}&\textbf{the disposition}\\\hline\mathrm{FT.106}(3\mathrm c)\text{'s ``amplitude death of}\ k\ge2\text{''}&\textbf{RE-SCOPED as the}\ B{=}4\ \textbf{census total},\ \neg\text{retracted — it is true at its locus};\ \text{superseded IN SCOPE constructively}\ [\mathrm{AT.52}(4),(5)];\ \text{the frozen cube/octahedron rows}\ [\text{Census}\ \mathrm{FT.69}(3)(\mathrm v),(5)]\ \text{already carried the larger-budget evidence}\\\mathrm{AT.48}(5\mathrm{ii})\text{'s ``dressing flicker-SENSITIVE''}&\textbf{REFINED: the sign is sector-locked};\ \text{the sensitivity lives in}\ \aleph\text{'s value and the sector weights}\ [\mathrm{AT.53}(5);\ \mathrm{AT.54}(1),(2)]\\\mathrm{FT.106}(3\mathrm b)/(3\mathrm d)\text{'s support and symmetry rows}&\textbf{MECHANIZED per cell: the three-way}\ \omega\text{-split with the live antisymmetry}\ [\mathrm{AT.53}(4)]\\\mathrm{EM.9b}\text{'s type-}(1,1)\ \text{clause}&\textbf{EXTENDED chain-locally to hub interiors as a Level-5 lemma; the frozen locus untouched}\ [\mathrm{AT.53}(1)]\\\mathrm{AT\text{-}O6}&\textbf{CLOSED AS DRESSED STRUCTURE}\ [\mathrm{AT.48};\ \mathrm{AT.53};\ \mathrm{AT.54}]\\\mathrm{AT\text{-}O14/O16}&\textbf{CLOSED}\ [\mathrm{AT.50}(5),\ \text{session 4, consolidated here}]\end{array}$$
$$(4)\quad\textbf{MARKED,}\ \neg\textbf{ADOPTED (unchanged, continued):}\qquad(\mathrm a)\ \ \text{the level-price read rule}\ [\mathrm{AT.44}(8\mathrm{iv});\ \mathrm{AT.49}(3\mathrm c)];\qquad(\mathrm b)\ \ \text{the lift}\ \triangleright\ \text{and the base frame per floor}\ [\mathrm{AT.47}(5);\ \mathrm{AT.49}(3\mathrm a,\mathrm b)];$$
$$(\mathrm c)\ \ \text{specialization}\ (\mathrm S)\ \text{and AT.6's magnetic functional up to}\ \varkappa\beta\ [\mathrm{AT.34}(7)];\qquad(\mathrm d)\ \ \text{the curl's absolute rates stay}\ \mathrm{BM.6}(5)\text{-calibration}\ [\mathrm{AT.51}(5)]$$
$$(5)\quad\textbf{THE OPEN LEDGER at this closure:}\qquad\begin{array}{l|l}\textbf{row}&\textbf{why}\\\hline(\mathrm{AT\text{-}O2})\ w_i^\perp\ \text{gauge}&\textbf{BY NATURE: the momentum constraint's multiplier}\ [\mathrm{AT.5}(4),\ \text{unchanged}]\\(\mathrm{AT\text{-}O3})\ (\varkappa,\beta)&\textbf{BY DESIGN: P4 core},\ \neg\text{issued}\ [\mathrm{AT.49}(5),\ \text{unchanged}]\\(\mathrm{AT\text{-}O7})\ \mathrm{BM.140}(6)\text{'s pin}&\textbf{the convention row}\ [\mathrm{AT.7};\ \mathrm{AT.40}(7),\ \text{unchanged}]\\(\mathrm{AT\text{-}O11})\ \text{the dictionary at}\ n{=}4&\textbf{DECIDABLE}\ (\dim\mathcal K_{n\ge4}=26\ [\mathrm{AT.50}(6)]),\ \text{undecided};\ \ \textbf{did NOT block this tier: zero dictionary calls}\ [\mathrm{AT.54}]\\(\mathrm{AT\text{-}O13})\ \text{the Kerr route}&\textbf{ONE NUMBER AWAY: needs}\ (\mathrm{AT\text{-}O3})\ [\mathrm{AT.34},\ \text{unchanged}]\\(\mathrm{AT\text{-}O26})\ \text{the read-rule declaration}&\textbf{CLOSURE-PHASE ACT}\ [\mathrm{AT.44}(8\mathrm{iv})];\ \ \text{now also the gate of}\ (\mathrm{M1'})\ [\mathrm{AT.54}(6)]\\(\mathrm{AT\text{-}O27})\ \varepsilon_q\text{'s value}&\textbf{CALIBRATION:}\ \tfrac18\ \text{distinguished five ways now}\ [\mathrm{AT.40}(1);\ \mathrm{AT.44}(4),(5);\ \mathrm{AT.54}(1)\ \text{witnesses}],\ \text{adoption}\ \neg\text{issued}\ [\mathrm{P5}]\\(\mathrm{AT\text{-}O28})\ \text{the global Dirac-type operator}&\textbf{TWO SLOTS AWAY: the lift + the base frame}\ [\mathrm{AT.47}(8),(9);\ \mathrm{AT.49}(5),\ \text{unchanged}]\\(\mathrm{AT\text{-}O29})\ \text{a native vector EM read}&\textbf{BY NATURE (proved absence)}\ [\mathrm{AT.48}(3),\ \text{unchanged}]\\\textbf{new}\ (\mathrm{AT\text{-}O30})\ \text{the}\ B\ge5\ \text{winding-resolved cover census}&\textbf{OPEN, blocking nothing: the minimal cells are computed}\ [\mathrm{AT.52}(4)\text{--}(6);\ \mathrm{AT.54}(2)];\ \text{the frozen-cell extension (cube/octahedron winding spectra, the}\ V{=}5..7\ \text{full censuses) is}\ \mathrm{FT.69}(3)(\mathrm v)/\mathrm{FT.106}(3)\text{-type census work at the next budgets}\ [\text{growth data:}\ \mathrm{FT.105}]\end{array}$$
$$(6)\quad\textbf{the declaration census:}\qquad\textbf{the declarations this tier adds: none.}\qquad\neg\text{a P4 addition},\ \neg\text{a new dimensionful scale}\ [\mathrm{P1}],\ \neg\text{a measured value}\ [\mathrm{P5}],\ \neg\text{a species identification}\ [\mathrm{Def\text{-}BM.3}(7)];$$
$$\text{calibration parameters added:}\ 0;\qquad\text{marked rows:}\ (4)\text{'s four, none adopted};\qquad\text{claims withdrawn:}\ 0\ \ (\text{the corrections are premise- and scope-level, recorded at}\ (3))$$
$$(7)\quad\textbf{the machine state:}\qquad\texttt{canon/era2/run\_all\_era2.py}\to\textbf{33 checkers, 587 exact markers, 0 failures, exit 0};\qquad\texttt{check\_era2\_format.py}\to\textbf{11 Part 5 documents PASS};$$
$$\text{the shared libraries:}\ \texttt{qexact.py},\ \texttt{duality.py};\qquad\text{the folder remains deliberately NOT wired into}\ \texttt{verification/run\_all.py};\ \ \texttt{index/},\ \texttt{tags.json},\ \texttt{Summary.md}\ \neg\text{regenerated — promotion stays a closure-phase act}$$
$$(8)\quad\textbf{the era chain:}\qquad\text{every AT-tag of this tier cites Parts 1--4 and earlier AT-tags only.}\ \neg\exists\ \text{a forward pointer used as a premise.}\ \neg\exists\ \text{a circular citation. Acyclic by construction}\ [\text{machine: the format gate's F3}]$$
$$(9)\quad\textbf{THE STATE OF THE ATOMIC ERA:}\qquad\text{the structural agenda is complete to the calibration boundary, third consolidation:}$$
$$\text{grammar}\ [\mathrm{AT.41}]\to\text{dynamics}\ [\mathrm{AT.42}]\to\text{the no-go measured}\ [\mathrm{AT.43}]\to\text{resolvent, price, spectrum}\ [\mathrm{AT.44}]\to\text{duality, drag, statistics flip}\ [\mathrm{AT.46}]\to\text{frame section}\ [\mathrm{AT.47}]\to\text{moment coupling}\ [\mathrm{AT.48}]$$
$$\to\text{the locked sector and the curl}\ [\mathrm{AT.50},\mathrm{AT.51}]\to\textbf{the dressed vertex:}\ \delta=0\ \text{on the operator},\ \text{rationals on the measure},\ \text{the winding ladder revived}\ [\mathrm{AT.52}\text{--}\mathrm{AT.54}];$$
$$\text{between Level 5 and contact stand exactly:}\ \varepsilon_q,\ e_0,\ (\varkappa,\beta),\ \text{the chart-side scales}\ [\mathrm{AT\text{-}O3},\mathrm{AT\text{-}O27}];\ \ \text{the two declared slots}\ [\mathrm{AT\text{-}O28}];\ \ \text{the read-rule declarations}\ [\mathrm{AT\text{-}O26};\ \mathrm{M1'}];\ \ \text{the}\ B\ge5\ \text{census}\ [\mathrm{AT\text{-}O30}];$$
$$\boxed{\ \textbf{coherence is}\ \neg\textbf{contact, and this tier makes no contact claim}\ }\qquad[\mathrm{AT.39}(8)\text{'s standing row, re-cited and unchanged}]$$

**Req.** AT.50, AT.51, AT.52, AT.53, AT.54 (this level); P1, P4, P5, A8 (Parts 1–2); CT4.5, EM.9b, EM.25(7) (Part 2); Def-H.32, Def-H.37(2), Def-H.43, FT.22, FT.40, FT.54(4), FT.67, FT.69, FT.79, FT.93, FT.105, FT.106, FT.107, FT.108 (Part 3); Census FT.69 (row-wise); AT.5, AT.6, AT.7, AT.34, AT.39, AT.40, AT.41, AT.42, AT.43, AT.44, AT.47, AT.48, AT.49, AT-O2, AT-O3, AT-O6, AT-O7, AT-O11, AT-O13, AT-O14, AT-O16, AT-O26, AT-O27, AT-O28, AT-O29, AT-O30 (this level); Def-BM.3(7), BM.6(5), BM.88(1), BM.111, BM.113(4), BM.124, BM.125, BM.126, BM.134(5), BM.137 (Part 4); row-wise assembly only — no new mathematics at this tag [math; machine: both session checkers + `check_era2_format.py`].

**Pf.** Row-wise assembly of AT.50–AT.54, each row re-citing its own machine section and its own
locus; the format gate re-run over all eleven Part 5 documents; the suite re-run end to end. No
new mathematics is introduced at this tag. $\blacksquare$

**Phys.** This tier closed two long-standing rows and corrected two scopes, and its centerpiece is
a vanishing. The locked sector, priority one since the boundary survey, resolved into the third
branch the posed dichotomy had not listed: formally nonzero at the unlocking, provably unreachable
at every accessible rung, structureless even if reached — the lock is a biconditional, not a
wall. The Architect's electroweak curl hypothesis assembled from four frozen steps, with the
transport Gram as the closure detector and the photon's kernel line as its massless immunity. And
the vertex correction — the era's last named structural residue on the moment sector — evaluated
to zero on the operator layer, exactly, at every order the move system can form, protected by the
record's own telescoping rather than by any imported symmetry; the anomaly relocated, whole and
rational, onto the measure: residues that attenuate by binomials, contacts that divert at even
channel counts, excess means in the threshold alone, and the first live winding-two and
winding-three sector integers at their minimal budgets, where a five-vertex theta finally lets a
four-cycle hide. Two scope corrections keep the record honest: a death row that turned out to be a
budget slice, and a dressing sign that turns out to be charge data. The era's shape is now the
BM.23 closure shape a third time over: everything structural derived to the calibration boundary,
every absence proved with its ground, every residue named to the symbol, and the contact claim
still, deliberately, unmade.
