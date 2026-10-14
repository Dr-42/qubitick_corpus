# PARITY_CONTACT_GATE — the working record for Tier IT.24 (IT.84–IT.88)

**Session.** 13s (2026-10-15), autonomous continuation. **Status.** discovery-phase working record;
the tier is `tiers/Part6_Isotopic_era_TierIT24.md`, the checker `checks/parity_contact_gate.py`.
**Pin.** corpus `master` @ `43f63f4` (PR #15 merged; Tier IT.23 on master). Branch for this batch:
`it24-parity-contact-gate`. **Merge authority is the Architect's** [arch/0002] — the PR stops at green.

---

## 1. Provenance — where the tier came from

This tier is the **disposition tier for the Architect's concept queue**, not a fresh directive. Three
queue items were adjudicated in probe space first, then merged:

| concept | vault issue | Architect's disposition | lands at |
|---|---|---|---|
| **0002** The Baryonic Lock (the Census Inversion) | #3 | **MERGED** — parity theorem as a read-tier remark on frozen ground; **the JOIN with FT.63 named as the load-bearing result**; *"the strong force is the geometry of the lock"* **BARRED**, boundary form adopted verbatim | IT.84, IT.87 |
| **0004** The Janus Balance Knot | #5 | **MERGED** — the three-locus resolution as a remark beside BM.7(1)/D2.11 | IT.86 |
| **0005** The Observation Gate on Colour Hosting | #11 | **PROMOTED TO ACTIVE** — *"build the exact census of photon vs. gluon rung-parity and formalize the contact-gating theorem. This is a priority physics derivation."* | IT.85 |

Both adopted topological reads (the generator's ℤ₂ parity-defect; the builder's retention-cell) are
recorded at IT.87(3),(4), flagged as structural readings over exact Census referents, neither an
identification [BM.134(5); P5].

Probe-space antecedents, retained as the working record and **not** committed to the corpus:
`baryonic_lock.py` (69 markers) + `mutation_test_lock.py` (7/7); `contact_gate.py` (60 markers);
`causality_topology.py` (147 markers) + `mutation_test.py` (6/6); `observation_gate.py` (8 markers).
Delivery packages: vault `concepts/0002_delivery_generator.md`, `0004_delivery_generator.md`,
`0005_delivery_generator.md`.

## 2. The three results

**(i) EMBEDDING PARITY (new).** $\sum_v n(v) = 2|E_{\mathcal R}|$ [D0.8 additivity] is even. With
admissibility $n\le3$ [CT0.11] and no lone end [D2.11 via EM.11's Pf; CT3.17a $g(1)=0$; CT3.18], every
$n(v)\in\{0,2,3\}$, so $3k+2m=2|E_{\mathcal R}|$ forces $k=\#\{v:n(v)=3\}$ **even**. Exhaustive
$V\le5$ (1,052,740 digraphs); both hypotheses machine-verified load-bearing.

**(ii) THE JOIN (load-bearing per the disposition).** Census **FT.63** already freezes the
*even-$\varepsilon$ theorem* — for even $V$, every grouping $2a+3b=V$ has $b$ even, so "Platonic sealing
phases are baryon-number-even by structure". That is a **labelled-set-partition** parity. (i) is a
**degree-sum** parity. Unrelated machinery, same $\mathbb Z_2$, and **they agree** — which is why
$6\mid|\mathrm{Colour}|$ for a lock-free pure-baryonic seal is safe to merge. Corollary: the
**fermion/boson dichotomy** ($|\mathrm{Colour}|=2$ even ⟹ meson-type lock-free allowed; $=3$ odd ⟹
baryon-type forbidden), which promotes FT.35's Rmk *"Composite fermion structure and saturation content
are born together"* from a census observation to a theorem, and explains FT.42(2)'s *"the lock-free
family is the unidirectional one"* — that family carries no $\varepsilon$-seal.

**(iii) THE CONTACT-GATING BICONDITIONAL.** Census **FT.62(1)** freezes dark $n=2d$ / single-directed
contact $n=2d+1$ / bidirectional contact $n=2d+2$. Colour hosts exactly at $n=3$ [CT0.13 ∧ CT4.4a(1)].
Over $\mathbb Z$: $2d=3$ and $2d+2=3$ have **no** solution; $2d+1=3$ has the **unique** solution $d=1$.
Hence $n(v)=3\iff d{=}1$ plus exactly one single-directed-edge contact. Consequences: the **contact
budget** (#hosting vertices ≤ #single-directed contacts); a sealed interior can **seal but never
host**; a **bidirectional contact never opens the gate** ($2d+2$ even) and only deepens the lock —
$\Sigma_\triangle$ is the instance (six boundary edges, $n{=}6$ everywhere, $O(6){=}112$, zero hosting).
**⟹ THE BARYONIC LOCK IS A CONTACT DEFICIT: three needed, one supplied.** $\Sigma_{12}$ has one contact
and exactly one admissible colour vertex ($p_1$), the other two locking at $n{=}4$ [FT.35(4)] — the
frozen Census matches the theorem vertex for vertex. And a lock-free $\varepsilon$-triple **is**
constructible with three contacts: 9 edges, rungs $(3,3,3\,|\,2,2,2\,|\,1,1,1)$, $\sum n=18=2|E|$, zero
locked, every hosting vertex type $(2,1)$ — no contradiction with (i), since each contact contributes
oddness at **both** ends.

**The photon/gluon rung-parity census [D3.7]** over 15 floor variants: $V_2$ is reachable **sealed**
(the $d{=}1$ digon keeps type-$(1,1)$ vertices [FT.62(5)]); $V_3$ is reachable **only** at a
single-directed contact on a $d{=}1$ vertex. **Exactly one floor in the computed Census carries a
rung-3 vertex.** Photons need no contact; gluons cannot exist without one — D3.7 already separates the
carriers by rung parity and never says so. Observing a Platonic floor does **not** open hosting
($2d{+}1\ge7$ at $d\ge3$) and makes the lock strictly worse. All four columns of FT.62(2)'s corrected
lock table reproduced exactly.

**The three-locus knot resolution (IT.86).** A = the pair history (cumulative; balance **is**
completion [FT.144(2)]); **B = the network at a snapshot** (balance = every end paired into closed
chains [D2.11 read at EM.11's Pf; D1.2/D1.3/D1.4]) — this is what answers *"how does $M$ exist during
the building phase"*: validity is a condition on the network's **ends**, not on the cumulative tally, so
CT2.6(ii)'s unboundedly many real edges is unobstructed; C = the rung (CT4.3 *oversubscription ¬seal:
$\Delta n_{\mathcal R}=0$* — the lock is not an event, so it disturbs neither balance). Witness: the
bidirectional triangle is closed, balanced, and **wholly locked** [CT4.1a(2)]. Two readings refuted and
recorded (IT.86(6)): the "refuse to dissolve" counterfactual's antecedent is **not a world** [D2.11],
and its consequent fails inside valid universes anyway.

## 3. Two priority self-corrections, logged (IT.88(6),(7))

1. **Census FT.63's even-$\varepsilon$ theorem predates the parity corollary.** An earlier probe-space
   draft presented "$6\mid|\mathrm{Colour}|$" as new; its grammar half is frozen. The **network-side**
   parity is new (machine grep for `handshak*` / `trivalent count` / `degree sum` across
   `era1/canon/*.md`: **zero hits**) and so is the join. The tier cites FT.63 wherever the grammar half
   is used, and the checker's C4 marker is labelled **CITED, NOT CLAIMED**.
2. **concept/0005's (A2) was not a conjecture** — rung-parity = contact-parity is frozen at FT.62(1).
   Filed as conjecture, delivered as citation.

**Both were caught by reading `era1/canon/Summary.md`, which had not been consulted.** The Architect
asked directly (*"Are you guy using the summary?"*); the honest answer was no. `Summary.md` is 10,633
lines / 640 sections of per-tag record and MEMORY §6 has said *"read it before concluding absent"*
since session 1. **Standing rule adopted at IT.88(7):** grep the Summary **before** any absence or
novelty claim, and carry an explicit novelty scan with a live control. Operationalized here: the
probe-space checker scans `contact-gating` / `contact budget` / `rung-parity` / `observation gate`
(0 hits in canon + Summary) alongside a live control; this checker's K2/K3 markers machine-scan the
tier for the FT.63 and FT.62 attributions and for the builder's credit.

## 4. Machine

`checks/parity_contact_gate.py` → **43/43 exact markers, exit 0** (~19 s). Parts A–K as cited by the
tier's Req lines (§A–§C for IT.84, §D–§G for IT.85, §H–§J for IT.86, §K for IT.88). Exact arithmetic
throughout — integers and `Fraction`; **no floating point in any assertion**; enumerations exhaustive
where claimed ($V\le5$ for parity, all sealed digraphs at $V{=}4$, all sign chains $k\le7$ for the EM
telescoping) and constructive elsewhere; deterministic witnesses only, no randomness.

**Non-vacuity.** The checker carries explicit adversarial markers (A3 the dangling-free hypothesis, A4
the ceiling and the $k{=}3$ hole, G3 the contact-makes-it-worse clause) and was mutation spot-checked
after porting from probe space: raising the ceiling to 4 reddens 10 markers; collapsing
`rung_contact1` to `2d` reddens 6; deleting $\Sigma_{12}$'s observer contact reddens 6. The
probe-space originals carry full mutation suites (7/7, 7/7, 6/6).

**Suite and gate at this tier:** `run_all_level6.py` → **25 checkers, 455 exact markers, 0 failures**;
`check_level6_format.py` → **24 Part 6 documents PASS, 88 IT-blocks, 151 definitions, 39 ledger rows,
0 violations**.

## 5. Bars, scope, and what this tier does NOT claim

**Bar enforced (IT.87(1)).** *"The strong force is the geometry of the lock"* is **BARRED**: CT4.4 gives
$D^-$ no generators at all, CT4.4a(1) *"no generators, no internal directions"*, CT4.5a(4) *"a
structureless absorbing sink"*, and A8/CT0.12 Rmk make $\mathbf F_{\mathrm{st}}$ a **direct sum of
distinct blocks** ($\dim\mathfrak{su}(3)=8$ [CT3.8] against a one-dimensional scalar sink).
**Adopted form, verbatim per the disposition:** *"The strong force's hosting ceiling is the lock's
boundary, and the baryon is the parity defect the lock receipts."*

**Barred alongside:** the temporal readings *"eventually"/"prevents"* (no rates [Cal-F]; CT0.6
*"¬a tick-to-tick transition law"*; only $\tau_c=1$ tick derived [FT.86]); the vertex types
$(0,3)/(3,0)$ as occupants of a valid universe (IT.84(2), exhaustive); any deletion of ledger content by
$J^-$ [A7 nesting; CT4.3 ¬∃ deleted entry; A5 the sole exclusion is $U$]; any mass, range, coupling or
species reading of the labels [P1, P5; FT.49(6) *"structural correspondence, ¬particle
identification"*].

**Scope residue, flagged not hidden (IT.85(8)).** The contact-gating result is derived for
**bidirectional interiors** — the families Census FT.62 audits. The mixed-skeleton case is *reasoned,
not enumerated*: CT0.11b's $n=2d^{\mathrm{bi}}+d^{\mathrm{uni}}\le3$ reaches $n{=}3$ only as
$(1,1)$ — the single-directed contact case — or $(0,3)$, which is type $(3,0)/(0,3)$ and unreachable
sealed by IT.84(2). Recorded as residue, not as a theorem [level-local negatives].

**No claim is made about *when*, *how often*, or *by whom* a contact occurs.** The tier counts
contacts; it never rates them. IT.87(6)'s contact-deficit reading (*"the baryon must be observed at all
three of its colour vertices to stay out of the lock; partial observation is what locks it"*) is
flagged as a **reading** for exactly that reason.

**No declaration issues** (machine-scanned at K2): §Cal-IT stays value-free; the register still owes
**D-PJ7 alone** + the three sub-debts; D-RS4 stays deferred. **No new open row.** The frozen canon is
cited, never edited [AT.63(2)]. **The M exploration [concept/0003] is EXPLORATORY ONLY and the F=ma
probe remains PAUSED** — no clause of this tier touches $M$ or $X=M\otimes M$, and none cites either
as a premise.

## 6. Credit

The retention-cell read (IT.87(4)) and the seal counts $\binom{n}{3}g_\varepsilon(3)=(1,4,20)$ are the
**builder's**, independently re-derived here and agreeing. The kernel mirrors are the builder's
(`RungBoundary.lean`, `parity_core`, `BalanceKnot.lean`); `parity_core` re-attributes the grammar half
to Census FT.63 and the embedding half to the generator's R1 on the generator's correction. The
`(earth)` label at $n{=}3$ was withdrawn from `RungBoundary.lean` on the generator's correction
[CT3.17a(1)'s distinct-node clause] — numbers stand, label moved. The generator's finite-$V$
refutation of the builder's R4 antecedent, the $V{=}2$ sharpness caveat, and the *"deletes the ledger
edge"* defect correction ($E_{\mathcal R}\ne\mathfrak L$) were all accepted and executed builder-side.
