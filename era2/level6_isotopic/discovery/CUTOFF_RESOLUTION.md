# CUTOFF_RESOLUTION.md — the session-13e working record (Tier IT.9 candidate, IT.28–IT.30)

**Directive (Architect, session 13e).** *"please continue [the amplitude side / IT-O5]. Also if you
need inspiration, look at how the 'neutron's' stability was resolved. It was coming ≤ 0. The thing is
the non dynamical picture. That causes this."*

**Machine.** `checks/cutoff_resolution.py` → **16/16 EXACT**, no floating point, no external datum.

---

## 0. The inspiration, made precise — the "neutron stability" precedent

The corpus resolved the "neutron's" stability at **BM.41** (reinforced at **BM.49**, **BM.52(4)**):

> **BM.41(4)(e):** *"the β-decay vertex is kinematically CLOSED on every adopted read: the corpus does
> not make the neutron heavier than the proton."*  $Q=m_n-m_p-m_\ell-m_\nu=-(m_\ell+m_\nu)<0$.

The **cause** (BM.41 Phys): *"every rest read it has ever derived gives the neutron and the proton the
same mass … because no crystallized count carries a charge exponent and every normalized average is
structurally charge-blind."* And BM.41 l.2299: *"the closure is a theorem about the READS, ¬about the
vertex grammar."*

So the corpus's "neutron" is **stable** — $m_n=m_p$ exactly (charge-degenerate) ⟹ $Q=-(m_\ell+m_\nu)<0$
⟹ no decay phase space. **This ≤ 0 / stability is an artifact of the NON-DYNAMICAL picture**, exactly
as the Architect said: the static, charge-degenerate reads cannot split $m_n$ from $m_p$, so they cannot
open a decay. The physically-decaying neutron needs a *dynamical* splitting the static ledger lacks.
BM.49 deepens it ($Q_{\rm corr}=-(\Delta m_{\rm EM}+m_\ell+m_\nu)<0$, "strictly deeper"); BM.52(4):
the closure "survives the complete force operator."

## A. The template applied — the static binding-sign census (→ IT.29)

Every **constructed** static binding/decay read is **≤ 0** (bound or closed):

| read | value | sign | locus |
|---|---|---|---|
| 3-constituent ensemble binding | $\mathcal B(S_j;1,1,1)$ | **< 0** (bound) | BM.21(4) |
| two-chain ensemble binding | $\mathcal B^{(2)}_{\rm ens}=-\tfrac{4u}{1+u}\tfrac{\ln2}{\mathfrak h}$ | **< 0** (bound) | BM.137(3) |
| neutron β-decay Q-value | $Q=-(m_\ell+m_\nu)$ | **< 0** (closed) | BM.41(4)(e) |
| EM-corrected Q-value | $Q_{\rm corr}=-(\Delta m_{\rm EM}+m_\ell+m_\nu)$ | **< 0** (deeper) | BM.49 |
| informational, disjoint | $\mathcal B_{\rm info}=0$ | **= 0** (marginal) | FT.50(1); IT.18(1) |

The **one** static read that is positive — the informational/cardinal **mass excess** of the bridged
composite, $m_{\rm comp}-\sum m_{\rm sep}=(8k{+}6)-6(k{+}1)=+2k\,u$ [FT.50(1); IT.20(1)] — is
**non-physical**: strictly monotone with **no sign change**, it flags the **deuteron (k=1)** "unbound"
exactly as k=3. So it cannot locate a last-bound member.

⟹ **The static/non-dynamical ledger produces NO isotope cutoff.** It gives a **bound (≤0) sequence at
every k**, just as it gives a stable "neutron."

## B. The resonance is dynamical (→ IT.29/IT.30, the relocation to IT-O1)

The empirical hydrogen-4⁺ resonances are **unbound, decaying** states — a *dissociation/transit*
amplitude. That is exactly what the inventory lacks:

> **BM.122(6)(O1–O4):** *"¬∃ a two-transit-quantum supply vertex in the inventory"* on four independent
> grounds (no gauged chiral coupling; the transit alternative is deficit 1′; no momentum-space
> resolvent; the transit object carries no winding carrier) ⟹ **no formed radiation/transit leg** [IT-O1].

So the cutoff **relocates** from a static binding sign flip (IT-O5/IT-O2) to the **dynamics (IT-O1)**.
The neutron precedent confirms the pattern: the corpus's static "neutron" is stable though the physical
one decays — the decay is dynamical, and the static picture cannot produce it. The isotopes are the same
case.

## C. The adjudication (→ IT.30)

- **IT-O5 STATIC SIDE CLOSES.** The isotope cutoff is **NOT a static/non-dynamical phenomenon**: the
  ledger gives a bound (≤0 physical binding) sequence at **every** k, by the same charge-degeneracy /
  additivity that makes the "neutron" stable. There is **no last-bound member in the static picture** —
  the "structural termination at k=2" is **refuted as a static claim**.
- **The empirical cutoff RELOCATES to IT-O1** (the transit/dissociation dynamics). If derived, it is a
  *dynamical dissociation threshold*, not a static binding sign flip. The H-4⁺ widths stay a [P5]
  quarantined [EXT] target.
- **IT-O2 reduced to the binding VALUE.** The multi-nucleon ensemble binding *value* stays open (the
  three IT.27(2) constructions), but it does **not** gate the cutoff *verdict*, which the non-dynamical
  sign structure + the neutron template resolve.
- **Premise corrections (IT.30):** (P1) "the amplitude-weighted ensemble binding is ≥0 (unbound) at
  N=9/12" — refuted as a static claim (every constructed static read ≤0; the informational excess is
  non-physical; the neutron precedent gives stability, not decay). (P2) the cutoff is dynamical (IT-O1).
  (P3) the binding value (IT-O2) is open but not gating the verdict.

**Declarations issued: none. §Cal-IT empty.** No species identified; no measured value [P5] (the neutron
lifetime, the H-4 widths stay quarantined [EXT]); prices not masses; Level-5 and IT.4–IT.8 cited, never
edited.

## Check ledger (`cutoff_resolution.py`, 16/16)

| § | checks | content |
|---|---|---|
| A | A1, A2, A3, A2x, A4 | the neutron template: $m_n=m_p$ (charge-degeneracy), $Q=-(m_\ell+m_\nu)<0$ closed, $Q_{\rm corr}<0$ deeper, the closure is a theorem about the reads, the non-dynamical cause |
| B | B1, B2, B2x, B3 | the ensemble reads ≤0 (BM.21/BM.137 re-derived); the informational mass excess +2ku monotone & non-physical (flags the deuteron); the uniform static pattern |
| C | C1, C2, C3 | BM.122(6)(O1–O4) refute a formed transit leg; the resonance relocates to IT-O1; the neutron precedent confirms |
| D | D1, D2, D3, D4 | IT-O5 static side closes (no static cutoff); the empirical cutoff → IT-O1; the premise corrections; the status |

**Open rows after IT.9:** IT-O1 (the transit/dissociation dynamics — **now the locus of the empirical
isotope cutoff**), **IT-O2 (reduced to the multi-nucleon binding VALUE, ¬the sign/verdict)**, IT-O3,
**IT-O5 (static side CLOSED; the empirical/dynamical side = IT-O1)**, the owed route choice; **IT-O4
stays CLOSED**.
