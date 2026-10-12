# CONNECTOR_SPECIES.md — the session-13b working record (Tier IT.6 candidate, IT.19–IT.21)

**Directive (Architect, session 13b).** *"Construct the Nucleon-Nucleon Connector Species (IT-O4)
and Adjudicate the Isotope Cutoff (IT-O5) … Define the exact ledger object (count, winding d,
fusion/sharing rules) that connects two ε-sealed 3-junctures … Use this to evaluate the sign of the
2k residue and adjudicate whether the family terminates at k=2 (Tritium) or extends further."*
Constraint: *"If the connector species cannot be formed from the current inventory, state the exact
missing definition."*

**Machine.** `checks/connector_species.py` → **17/17 EXACT**, no floating point in any assertion.

---

## 0. The premise audit — the connector is already in the inventory

The directive frames the connector as a thing to be newly defined. The canon says otherwise: **the
nucleon–nucleon connector is the Σ₁₂ connector, already frozen**, and its winding gap (R10) was
already dispositioned at the Part-4 closure.

- **Census FT.35 / BM.17(1):** Σ₁₂ (the "neutron") = two materialized 2-cycles $c_1=(p_1{\to}q_1{\to}p_1)$,
  $c_2=(p_2{\to}q_2{\to}p_2)$ **joined by the bidirectional connector** $e_{12}=(q_1,p_2)$,
  $\bar e_{12}=(p_2,q_1)$, with $E_{\mathrm{int}}=6=(c_1{:}2)+(c_2{:}2)+(\textbf{connector}{:}2)$.
  The connector's E_int contribution (**2**) is frozen cell data.
- **BM.2(2) / FT.34(3):** for $\Gamma=c_1\cdot P\cdot c_2\cdot\bar P$, the winding is additive,
  $k(\Gamma)=k_1+k_2+d_{12}$ with $d_{12}=\Theta(P)=\Theta(\bar P)\ge0$; $\Theta(\Gamma)=2(k_1+d_{12}+k_2)$.
- **Def-H.32(4):** an **open** chain carries $S=0$ (a bookkeeping label, ¬a spin value).
- **BM.129(1),(3),(4):** the meson and the baryon both use an **open** connector; an open connector
  gives $S=0\Rightarrow d=0\Rightarrow\varepsilon_M=(-1)^d=+1$; the *closed*-connector variant carries
  $\varepsilon_M=(-1)^d$ with $d=\Theta(P)$.
- **BM.143(3) — (R10) reclassified:** "the connector winding is **registration data** … $d=\Theta(P)\ge0$;
  the alphabet is derived ($d\in\mathbb Z_{\ge0}$); the parity law is derived ($\varepsilon_M=(-1)^d$);
  the computed cells are derived (an open connector carries $S=0\Rightarrow d=0\Rightarrow\varepsilon_M=+1$)
  … **(R10) is closed as registration-species: the per-class value is fixed at crystallization.**"

So (R10) — the exact gap `isotopic_family.py` named when it opened IT-O4 — is **not a missing
definition**. The connector species is derivable. What IT.6 supplies is the **inter-nucleon instance**
and the residue-sign adjudication.

---

## A. The connector species, constructed (→ IT.19, IT-O4 CLOSES)

| property | the derived value | locus |
|---|---|---|
| **object** | the bidirectional pair $(e_{12},\bar e_{12})$ | Census FT.35; BM.17(1) |
| **count** | $k$ connectors for $(k{+}1)$ nucleons in a tree | (a tree on $k{+}1$ vertices has $k$ edges) |
| **E_int each** | **2** (frozen) ⟹ $E_{\mathrm{int}}^{\mathrm{tree}}=6(k{+}1)+2k=8k{+}6$ | Census FT.35(2); IT.7(1) |
| **winding $d$** | **0** (open connector ⟹ $S=0$) | Def-H.32(4); BM.129(3); BM.143(3) |
| **statistics $\varepsilon$** | $(-1)^d=(-1)^0=+1$ | BM.129(3) |
| **charge** | telescopes to **net 0** (bidirectional) ⟹ $Q_{\text{total}}=\sum Q_{\text{nucleon}}=+1$ preserved | EM.9b; AT.41; BM.135 |
| **fusion/sharing** | **distinct sealed supports**, $N=3(k{+}1)$; the connector adds *edges*, not shared attachments | IT.6(2); Def-BM.9(4); BM.1(1) |
| **junction vertices** | rung 4, $D_{\text{tick}}(4)=32>16\Rightarrow O(4)=16$, D⁻-locked, **retained ¬accessible** | Census FT.35(4),Rmk; CT0.5/0.6; CT4.1–4.3; D4.2 |

**$E_{\mathrm{int}}^{\mathrm{tree}}=8k{+}6$ is reproduced exactly** from the connector definition — IT.7(1)'s
*parametric* tree reading is now a **construction** (adversarial: $k{\pm}1$ connectors give $8k{+}8/8k{+}4\ne30$
at $k{=}3$). The charge telescoping is verified over all 4 end-sign assignments (net 0). The
open/closed distinction is real (a closed connector at $d{=}1$ would give $\varepsilon=-1\ne+1$).

**The saturation is uniform.** "Composition creates saturation" (Census FT.35 Rmk) is born at the
**first** composite: every connector pushes its junction vertices to rung 4, where D⁻ locks 16
registers of excess — *retained, inaccessible*. Nucleon junctions sit at $n{=}3$ ($D_{\text{tick}}(3)=16=C_{\text{cap}}$,
saturated but **admissible**). This is $k$-independent — it is **not** a $k{=}3$ event.

---

## B. The residue sign, and where the cutoff actually lives (→ IT.20)

**The informational read.** On $m=E_{\mathrm{int}}\cdot u$ [FT.44(4)], the tree binding is
$$\mathcal B_{\mathrm{info}}^{\mathrm{tree}}=\bigl(6(k{+}1)-(8k{+}6)\bigr)u=-2k\,u<0\quad\text{for every }k\ge1,$$
values $(0,-2,-4,-6)u$ at $k{=}0,1,2,3$ — **strictly monotone, never crossing zero for $k\ge1$**. So
the cardinality read flags the **deuteron ($k{=}1$) "unbound" by $-2u$** exactly as it flags $k{=}3$ by
$-6u$. Since the deuteron is a constructed family member, **the informational read cannot be the
physical binding and cannot locate a last-bound member** (no sign change). This extends IT.18(1):
the disjoint reading gives $\mathcal B_{\mathrm{info}}=0$; the tree reading gives $-2k u$; neither
adjudicates the cutoff.

**The connector is $k$-identical.** $(d{=}0,\ +2\ E_{\mathrm{int}},\ \varepsilon{=}+1)$ at every $k$ — it does
**not** change character at $k{=}3$. So the connector cannot terminate the family at $k{=}2$; the
grammar/connector structure **extends uniformly**.

**The directive's Step-3 mechanisms, refuted row by row:**
- *capacity overload* — the rung-4 D⁻ saturation is uniform from $k{=}1$ and **retained-not-accessible**
  (the nonzero-but-unreachable chain of IT.3/IT.10), not an overload that terminates at $k{=}3$;
- *winding mismatch* — $d=0$ for every open connector, uniformly;
- *flicker attenuation* — that is the ensemble/amplitude read = **IT-O2**, not a connector property.

---

## C. The adjudication (→ IT.21)

- **IT-O4 CLOSES.** The nucleon–nucleon connector species is **derived**: the open bidirectional
  Σ₁₂-species connector, $d=0$, $+2$ E_int, charge-telescoping, $\varepsilon=+1$, distinct supports,
  uniform rung-4 saturation. (R10) confirmed as registration data; the inter-nucleon instance built;
  $E_{\mathrm{int}}^{\mathrm{tree}}=8k{+}6$ discharged from parametric to constructed.
- **IT-O5 SHARPENED, not closed.** The isotope cutoff is **relocated**: it is *not* in the connector
  (IT-O4 discharged, $k$-identical) and *not* in the cardinality read ($-2ku<0$ uniformly, calls the
  deuteron unbound too). The **only** read that can adjudicate bound-vs-unbound is the **ensemble
  binding** (BM.21(2)–(4)/BM.137(3) species) for the multi-nucleon configuration = the Def-H.32
  amplitude sum over the grouping sectors with $(-1)^{\aleph}$ dressing = **IT-O2**. **IT-O5 is now
  gated on IT-O2 alone.**
- The bound-sequence termination at $k{=}2$ remains a **conjecture** — but the obstruction is now a
  single, precisely-named construction (the multi-nucleon amplitude/ensemble binding), not two.

**Premise corrections logged (IT.20):** (P1) the connector does not "go repulsive at $k{=}3$" — it is
$k$-identical; (P2) the Step-3 mechanisms do not fire (saturation uniform, $d{=}0$, flicker = IT-O2);
(P3) the residue sign is read-relative and the cardinality read cannot adjudicate. The empirical H-4
resonance fact stays a [P5] scoring target, cited nowhere.

---

## Check ledger (`connector_species.py`, 17/17)

| § | checks | content |
|---|---|---|
| A | A1, A2, A2x, A3, A4, A4x, A5, A6 | the connector object (+2, frozen); open ⟹ $d{=}0$, $\varepsilon{=}+1$; the winding additivity; $E_{\mathrm{int}}^{\mathrm{tree}}=8k{+}6$ reproduced; the charge telescoping (net 0); distinct supports ($N{=}3(k{+}1)$); + the closed-connector and connector-count adversarial witnesses |
| B | B1, B2 | the rung-4 D⁻ saturation ($D_{\text{tick}}(4)=32>16\Rightarrow O(4)=16$, retained); capacity never bites (uniform, no $k{=}3$ termination) |
| C | C1, C1x, C2, C3 | $\mathcal B_{\mathrm{info}}^{\mathrm{tree}}=-2ku<0$ uniformly (the deuteron too); the connector $k$-identical; the three Step-3 mechanisms refuted |
| D | D1, D2, D3 | IT-O4 CLOSED; IT-O5 sharpened to IT-O2 alone; the declaration census (none) + the bars |

**Declarations issued: none. §Cal-IT stays empty.** No species identified; no measured isotope datum
[P5]; prices not masses; no currency mixing; Level-5, IT.4 and IT.5 cited, never edited.

**Open rows after IT.6:** IT-O1 (transit-leg), **IT-O2 (the amplitude side — now the SOLE gate on
IT-O5)**, IT-O3 (handshake), ~~IT-O4~~ **CLOSED**, **IT-O5 (the isotope cutoff — gated on IT-O2
alone)**, and the owed mass-read route choice [IT.14(3)].
