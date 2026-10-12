# CALIBRATION_ANCHOR.md — the session-13f working record (Tier IT.10 candidate, IT.31–IT.33)

**Directive (Architect, session 13f, re-issued with REQUIRED DEFINITIONS).** *"Formalize the Macroscopic
Calibration Anchor … using strictly ledger-native definitions, avoiding any smooth-manifold smuggling.
Required Definitions (must be used verbatim): (1) Inter-Nuclear Distance: the lattice spacing scales as
$\Delta x_{\text{lattice}}\propto\mathfrak h/(E_{\text{int}}\ln2)$ [BM.17(3); Def-BM.4(1)] … (2)
Macroscopic Pauli Exclusion: the direct scaling of $C_{\text{cap}}=16$ and $\dim\wedge^3(\mathbb C^2)=0$
[BM.128(5)] … (3) 'BEC Ready': the structural property of a composite whose contraction grammar yields
exclusively the $4\mathbb Z$ statistics class (pure-$\varepsilon$, e.g. He-4, N a multiple of 4 and 3|N)
[IT.6(6); BM.31(4)]."*

**Machine.** `checks/calibration_anchor.py` → **14/14 EXACT**, no floating point, no measured value.

---

## 0. Stance: the definitions are accepted as a ledger-native definitional act, then grounded

The Architect supplies the three terms as **definitions** (a definitional act, which is the Architect's
authority), each citing derived rows. I accept them and verify the grounding — and where a definition
diverges from the census, **the rows win** (alignment order #1) and the correction is logged. This keeps
the tier free of smooth-manifold smuggling: the definitions are geometric reads, cardinalities, and a
statistics sign — never wavefunctions, coordinates, or a Schrödinger equation.

## A. Definition 1 — inter-nuclear distance $\propto\Delta x_B$ (grounded; proportionality stipulated)

- $\Delta x_B=\mathfrak h/(E_{\text{int}}\ln2)$ is a **derived chart-side length** [Def-BM.4(1); BM.13(4)].
- $\Delta x_B\cdot r_s=(\mathfrak h/(E\ln2))(\mathfrak h E/2)=\mathfrak h^2/(2\ln2)$ is **exactly
  $E_{\text{int}}$-independent** [BM.17(3)] — verified: the coefficient is $1/2$ on every floor
  $\{2,6,12,18,24,60\}$ (the $E$ cancels). A shared-currency geometric invariant.
- **Status of the proportionality:** $\Delta x_{\text{lattice}}\propto\Delta x_B$ is the Architect's
  **stipulation** (a definitional bridge). The *multi-composite lattice geometry* is **not** a derived
  ledger object — a corpus-wide scan finds no inter-nuclear-distance row, and IT-O4's connector gives
  $E_{\text{int}}{+}2$ and $d{=}0$, **not** a distance. So the anchor is **structural** (it ties $\mathfrak h$
  to a geometric read given $E_{\text{int}}$); the constant and the lattice are stipulated, not derived.

## B. Definition 2 — macroscopic Pauli exclusion (grounded; "scaling" is a misnomer)

- $\dim\wedge^3(\mathbb C^2)=\binom23=0$ vs $\dim\wedge^3(\mathbb C^3)=\binom33=1$ [BM.128(5)] — a
  **scale-free cardinality** (a dimension count; it holds identically at every scale, so "scaling" is a
  misnomer — nothing scales).
- $C_{\text{cap}}=16=D_{\text{tick}}(3)$ exactly saturated; $D_{\text{tick}}(4)=32>16$ inadmissible [CT0.12/13].
- **The mechanism is grounded:** $g_\delta(N)>0$ for every $N\ge4$ (the grammar forces δ-mixing past the
  protected N=3 [BM.31(2)]), and every $n\ge4$ junction is D⁻-configured/saturated, retained-not-accessible
  [CT4.1; Census FT.35 Rmk]. So "no multi-seal composite occupies the identical boundary state without
  triggering δ-mixing or capacity saturation" is a theorem of the grammar + the capacity census — a
  **combinatorial limit, not a wavefunction antisymmetry**.

## C. Definition 3 — "BEC ready" (CORRECTED: it is the exchange sign $(-1)^A$, not "exclusively $4\mathbb Z$")

- **The correction (the rows win):** "exclusively the $4\mathbb Z$ class" is **false at N=12** — the grammar
  gives $g(12)=164395=g_\varepsilon(12){=}15400$ ($40/427$ pure-ε, $4\mathbb Z$) $+\,g_\delta(12){=}148995$
  ($387/427$ δ-containing, $2\mathbb Z$) — **δ-dominant** [IT.6(6); IT.9(5)]. And the per-grouping
  $4\mathbb Z/2\mathbb Z$ *sealing* class [BM.31(4)] is a **different register** from the whole-composite
  exchange statistics.
- **The correct ledger-native grounding** [BM.128(7); BM.129(4),(5)]: the exchange law is **multiplicative**,
  $\varepsilon(\Gamma)=\prod_a\varepsilon(c_a)=(-1)^A$ for $A$ fermionic nucleons. So a composite is
  **bosonic ("BEC-ready") iff $A$ is even**: "He-4" ($A{=}4$) → $\varepsilon{=}+1$; "He-3" ($A{=}3$) →
  $\varepsilon{=}-1$ (fermion, needs pairing/doublets); deuteron ($A{=}2$) → $\varepsilon{=}+1$.
- **"N a multiple of 4" is too strict:** the deuteron ($A{=}2$, $N{=}6$) is bosonic yet $6\not\equiv0\pmod4$.
  The correct criterion is **$A$ even** (nucleon-count parity), not an attachment-count congruence.

## D. The bypass — the shared geometric/cardinal/sign currency

- **The bar** [BM.83; BM.140(5)]: $2^a3^b5^c=1\Rightarrow a{=}b{=}c{=}0$ (exhaustive, exact Fraction powers),
  and $\ln1280/\ln960$ is **irrational** (the ratio $1280/960=4/3$ is rational, but the log-ratio's
  certificate $(8q{-}6p)\ln2+(q{-}p)\ln5-p\ln3=0$ forces $p{=}q{=}0$ by the ℚ-independence of
  $\{\ln2,\ln3,\ln5\}$). So an absolute macroscopic **mass** ("laptop mass") is a sum across incommensurable
  currencies — **not computable**.
- **The bypass:** the anchor reads are **geometric** ($\Delta x_B$ a length; $\Delta x_B r_s$ an
  $E$-independent length²), **cardinal** ($\dim\wedge^3{=}0$, $C_{\text{cap}}{=}16$), and a **sign**
  ($\varepsilon{=}(-1)^A$), plus the self-averaging observables $(q,S,m_{\rm hid})$ [Cor FT.15.1]. **None is a
  cross-currency mass sum**, so none trips BM.83. Measuring a geometric *consequence* is a different species
  than summing masses — the "laptop mass" no-go is **shifted, not violated**.

## E. The machinery (Steps 1, 3) and the ideal observer (Step 2)

- **Kinematics generator:** BM.131 (Haar–Poisson / Lyapunov contraction) on CT1.12 (the emergent metric);
  the antimatter CP-flip is Def-H.33's orientation involution $\hat\omega$; the frame-by-frame propulsion is
  Def-H.32(7)'s $J^\pm$ Janus move system.
- **Rotational machinery:** AT.46 (spin holonomy + the statistics-flip law); AT.56–AT.58 (the bivector
  census, the Weitzenböck birth at tree coefficient 1).
- **Ideal observer** [Def-H.9's $o$; IT.1(1),(3); IT.2; CT3.22]: an EM-sealed atom is read rung-2-mediated
  (the boundary triple is inter-system accessible); a bare baryon is **dark** by read-species separation. So
  every baryon datum arrives EM-mediated = geometrically — which is *why* the anchor is a geometric read.

## F. The adjudication

- **The Macroscopic Calibration Anchor is DERIVED AS A STRATEGY** (extending IT.5): $\Delta x_{\text{lattice}}
  \propto\mathfrak h/(E_{\text{int}}\ln2)$ anchors $\mathfrak h$ given $E_{\text{int}}$; the cardinal reads
  anchor the exclusion structure; $\varepsilon=(-1)^A$ anchors the statistics — all in a shared currency that
  bypasses the mass-summation bar.
- **NO value is issued.** The Calibration Era is **deferred** (an Era-2-closure act [AT.63(4); IT.1(5)]);
  $\mathfrak h$ is the P1 slot, $\varepsilon_q$ is AT-O27 (a declaration); the read rules (M1′)–(M3′) gate every
  conversion [IT.5; AT.54(6)]; P5 stands. The conceptual gap is **narrowed, not closed**.
- **Premise corrections (IT.33(3)):** (P1) the Def-1 proportionality is stipulated (no lattice geometry
  derived); (P2) the Def-2 exclusion is scale-free, not "scaled"; (P3) Def-3's "exclusively $4\mathbb Z$" is
  false at N=12 and BEC-readiness is $(-1)^A$ (A even), not the $4\mathbb Z$ sealing class nor "N a multiple
  of 4." The species/BEC labels stay quoted [Def-BM.3(7); P5].

**Declarations issued: none. §Cal-IT empty.** No species identified; no measured value [P5] (no lattice
constant, no mass, no $\mathfrak h$, no $\varepsilon_q$ — all quarantined [EXT]); prices not masses; no
currency mixing; Level-5 and IT.1–IT.9 cited, never edited.

## Check ledger (`calibration_anchor.py`, 14/14)

| § | checks | content |
|---|---|---|
| A | A1–A5 | Def 1 ($\Delta x_B$, the E-independent invariant); Def 2 ($\wedge^3{=}0$, $C_{\text{cap}}$, the δ-mixing/saturation mechanism); Def 3 ($\varepsilon{=}(-1)^A$) + the Def-3 correction (N=12 δ-dominant; the deuteron witness) |
| B | B1, B2, B3 | the bar ($2^a3^b5^c{=}1$; $\ln1280/\ln960$ irrational); the shared geometric/cardinal/sign currency bypass |
| C | C1, C2 | the kinematics + rotational machinery; the ideal-observer read |
| D | D1–D4 | the anchor strategy; no value issued; the premise corrections; the adjudication |

**Open rows after IT.10:** unchanged in substance — IT-O1 (the transit/dissociation dynamics, the locus of
the empirical isotope cutoff), IT-O2 (the multi-nucleon binding value), IT-O3, IT-O5 (static side closed),
the owed route choice, **plus the deferred Calibration Era** (the anchor strategy is now derived; the issued
values await the Era-2-closure act + the read-rule declarations (M1′)–(M3′)). IT-O4 stays CLOSED.
