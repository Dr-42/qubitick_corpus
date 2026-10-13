# AMPLITUDE_BINDING.md — the session-13g working record (Tier IT.11 candidate, IT.34–IT.36)

**Directive (Architect, session 13g).** *"Close IT-O2 (the amplitude binding) and probe IT-O1 (the transit
obstruction) … does the full Def-H.32 ensemble sum, with its rational dressing and contact terms, preserve
this binding, or does it unlock a dissociation channel? … Scenario A (closure): the amplitude binding is
≤0 AND the contact terms render the transit leg amplitude-dead → close IT-O2 and IT-O1 (transit
structurally impossible). Scenario B (residue): the binding is positive OR the transit leg remains
formable."*

**Machine.** `checks/amplitude_binding.py` → **16/16 EXACT**, no floating point, no external datum.

---

## 0. The decisive structural fact — the binding is norm-layer, the dressing is amplitude-layer

The directive's crucial question ("does the rational dressing flip the static ≤0 binding?") is answered by
a **layer separation** that the canon already fixes:

- **Def-H.32(2):** the **amplitude layer** $v_\Gamma(R)=\sum_\sigma w(R,\sigma)$ is *signed* (it carries
  the $(-1)^\aleph$ dressing; $v=2^{|R|}(-1)^{\sum\kappa}$ on covers [FT.67(2)]). The **norm layer**
  $\nu_\Gamma(R)=\sum_\sigma|w(R,\sigma)|^2=2^{|R|}$ is *positive* — and $|(-1)^\aleph|^2=1$, so **the
  dressing drops out**.
- **Def-H.32(6):** the sector mass $m^2_B(q,S)=\frac{1}{Z^{\rm norm}}\sum \mathcal W^{\rm norm}\#\mathrm{inst}\,\Delta S$
  is built from the **norm layer**.
- **BM.21(2):** the binding $\mathcal B=m^2_B(\text{comp})-\sum m^2_B(\text{sep})$ is a difference of
  **norm-layer** sector masses.

⟹ **The ensemble binding is dressing-free by construction.** Machine witness (B1): for $|R|=3$, the norm
weight is $8=2^3$ under two *different* dressing parities and with no dressing at all. So the dressing and
the contact terms $c_k$ — amplitude-layer objects — **cannot flip the binding sign**. The static ≤0 (IT.9)
is preserved.

## A. The amplitude machinery, correctly scoped (→ IT.35)

- **The dressed resolvent** (re-derived, AT.52): $R_k(z)=c_k+\sum_d a_{k,d}/(1-d^2z)$,
  $a_{k,d}=2^{1-k}\binom{k}{(k+d)/2}$, $c_k=2^{-k}\binom{k}{k/2}$ [k even]; the sum rule $c_k+\sum_d a_{k,d}=1$
  holds for $k=1..8$; the **contact terms** $c_k=(\tfrac12,\tfrac38,\tfrac5{16},\tfrac{35}{128},\tfrac{63}{256})$
  at even $k$, $0$ at odd $k$; the pole-ladder weight is $1-c_k$.
- **Scope correction:** `vertex_correction.py` builds *"the k-channel **two-body** resolvent of the
  **lepton-baryon** composite"*; $k$ is the **pair/channel count** [BM.137(1); AT.54 Rmk], **not** the
  attachment count $N$. So the contact terms are a two-body amplitude feature — they do **not** enter the
  multi-nucleon (norm-layer) binding, and they do **not** bear on the transit-leg formation.

## B. The conflations in the directive's Step 1 (refuted)

- **Register conflation (D1):** "map each grouping sector to its $(q,S)$" / "sum the dressed weights over
  the $g(N)$ sectors" conflates the **colour grouping** $g(N)$ (independent of the edge signs [AT.41(3)]; a
  0/1 gate [Def-BM.9(2),(5)]) with the **amplitude**, which is $(q,S)$-sectored over the *configuration
  space* [Def-H.32(5)]. The $g(N)$ groupings carry no $(q,S)$ labels — the requested sum has no referent
  (re-confirmed from IT.8/IT.26).
- **Dressing scope (D2):** $(-1)^\aleph=(-1)^{|q|}$ holds for **single open chains** [AT.53(5)]; a multi-seal
  composite is not one. And in any case the dressing is amplitude-layer (§0), absent from the binding.

## C. No dissociation channel; the transit absence is level-local (→ IT-O1)

- **BM.122(6)(O1–O4):** a formed transit-quantum supply vertex is refuted on four independent grounds ⟹
  *"the pair channel's amplitude is ¬formed."* So the amplitude cannot "unlock a dissociation channel" —
  there is no transit leg to dissociate into. This is a **structural inventory absence, independent of the
  contact terms**.
- **Level-local, not impossible (D3):** BM.122(6) says "¬∃ … **in the inventory**" — an absence a future
  construction (a gauged charge read = deficit 1′, a momentum-space resolvent) could fill. Per **alignment
  order #2 (no-gos are level-local)**, Scenario A's *"IT-O1 closed, transit structurally impossible"*
  **over-reaches**. IT-O1 stays open.

## D. The verdict — the honest third scenario (→ IT.36)

- **IT-O2: the SIGN verdict RESOLVES; the VALUE stays open.** The dressing cannot flip the binding
  (layer separation, §0); every constructed norm-layer binding is ≤0 (BM.21(4), BM.137(3) re-derived);
  no dissociation channel is formable (BM.122(6)). So the static ≤0 (IT.9) is **preserved** — the
  amplitude side unlocks nothing. **But the multi-nucleon binding VALUE is not computed**: the
  composed-support norm-layer configuration space is beyond the frozen B=4 census [FT.106(3)], and the
  multi-junction binding **functional** is undefined (BM.21 is 3-constituent, BM.137 is two-chain).
- **IT-O1: OPEN.** The transit leg is level-local-absent (BM.122(6)); the contact terms don't bear on it;
  "structurally impossible" over-reaches. The empirical cutoff stays dynamical (IT.30).
- **Neither Scenario A nor B holds as stated.** A over-reaches (IT-O1 level-local; IT-O2 value uncomputed);
  B mis-frames (the binding is not positive — the dressing cannot make it so). The honest verdict: **the
  amplitude side preserves the bound (≤0) verdict and unlocks no dissociation channel; IT-O2's sign closes,
  its value stays open; IT-O1 stays open.**

**Declarations issued: none. §Cal-IT empty.** No species identified; no measured value [P5] (no binding
energy in MeV, no isotope width); prices not masses; no currency mixing; Level-5 and IT.1–IT.10 cited,
never edited.

## Check ledger (`amplitude_binding.py`, 16/16)

| § | checks | content |
|---|---|---|
| A | A1, A2, A3 | the dressed resolvent $R_k$/residues/contact terms (re-derived); the two-body/channel-index scope |
| B | B1, B2, B3, B4 | **the layer separation**: the norm weight is dressing-free ($2^{|R|}$ under any dressing); the binding is norm-layer; the dressing is amplitude-layer; ⟹ the dressing cannot flip the sign |
| C | C1, C2 | every constructed norm-layer binding ≤0; no dissociation channel (BM.122(6)) |
| D | D1, D2, D3 | the register conflation refuted; the dressing scope; the transit absence is level-local |
| E | E1, E2, E3, E4 | IT-O2 sign resolved / value open; IT-O1 open; the third scenario; the status |

**Open rows after IT.11:** IT-O1 (the transit/dissociation dynamics — the empirical cutoff), **IT-O2
(the multi-nucleon binding VALUE — the sign is now resolved, dressing-invariant ≤0)**, IT-O3, IT-O5 (static
side closed [IT.30]), the owed route choice, the deferred Calibration Era. **IT-O4 stays CLOSED.**
