# ISOTOPE_CUTOFF.md — the session-13 working record (Tier IT.5 candidate, IT.16–IT.18)

**Directive (Architect, session 13).** *"Prove the Hydrogen Isotope Cutoff at k=2 (Tritium) via the
δ-Dominance and Binding Read Collapse … Prove that for N ≥ 12 the flicker ensemble cannot form a
stable, bound-state composite, and instead exists only as a transient, unbound resonance."* Four
steps: (1) the grammar tipping point at N=3,6,9,12; (2) the binding-read collapse B_ens ≥ 0 at
N=12; (3) the boundary degradation / resonance classification; (4) the adjudication closing the
bound sequence at k=2. Plus a full Tritium→He-3 β⁻ structural derivation (§§1–6 of the directive),
and the standing instruction: **"Verify the tritium computation without assuming the decay products.
Run a forward compute. We are in exploration state now, so if lacking data, don't [give] a nogo but
add it as an open thing. If possible to close via simple mathematical calculation bridge rather than
requiring physical insight or direction, perform the derivation of that specific O direction."**

**Machine.** `checks/isotope_cutoff.py` → **20/20 EXACT**, no floating point in any assertion;
fresh Laurent convolution + fresh set-partition enumeration (independent of `isobar_transition.py`).

---

## 0. The state move found on resume (premise audit, part 0)

The crash-recovery re-clone surfaced that **the remote had advanced past the session-11 handoff**:
a **session 12** had (i) merged PR #2 (Tier ML.3 → master), (ii) **renamed Level 6 "Molecular" →
"Isotopic"** (the bijection ML.n ↦ IT.n, n=1..11; ML-Ok ↦ IT-Ok; §Cal-ML ↦ §Cal-IT), and (iii)
built **Tier IT.4** = `isobar_transition.py` (25/25), tags **IT.12–IT.15**: *"the N=9 isobar doublet
and its single-seed weak transition."* Master then took the Architect's `.github/CODEOWNERS`
(`* @Dr-42`).

**Consequence for this directive:** Part B (the Tritium→He-3 β⁻ construction, directive §§1–6) is
**already delivered and machine-certified as IT.4**, with a premise audit (IT.15(1)–(2)) that
independently reached the same corrections this session would have:

- ⟨m⟩ ∝ W(Q) is the **route-(ii) measure PRICE**, barred as a physical mass [BM.30(5); BM.37(6);
  BM.97 Rmk; HistLog §V.32]; on **every adopted read** the doublet is exactly degenerate and the
  β⁻ vertex is **kinematically CLOSED** [BM.41(4)(e) pattern].
- In `E = N√(m²+p²) − Nⁱpᵢ` the **N is the LAPSE**, not the attachment count [BM.34(4); BM.35(7)].
- "E_int = 18" is the **disjoint** reading (the tree reading is 22; 18 is off the floors {2,6,12,24,60}).
- The ν status is **conditionally forced** [BM.41(3)'s on-record upgrade of BM.23(6)], not merely admissible.
- Refinement: **sector ⊋ species** at species granularity (nucleonic shares 1000/2431, 375/884).

So the genuinely new work is **Part A (the isotope cutoff)** plus the Architect's explicit ask: an
**independent forward compute** re-deriving the tritium combinatorics *without assuming IT.4's
answers or the decay products*. That is Part A of the checker below.

---

## A. The forward compute — the N=9 doublet re-derived, decay-product-free (→ IT.16)

Everything is computed from the **support combinatorics alone** (the generating function and the
sector definition Q = the boundary charge), never from the tritium/helium-3 labels or the ℓ/ν decay:

| quantity | forward compute | IT.12 certified | verdict |
|---|---|---|---|
| `(2+z+z⁻¹)⁹` | fresh Laurent convolution = `C(18,Q+9)` entrywise; 19 classes; Σ = 4⁹ = 262144; symmetric; peak W₉(0) = 48620 | IT.12(2) | ✓ identical |
| "tritium" sector | W₉(+1) = C(18,10) = **43758** | 43758 | ✓ |
| "helium-3" sector | W₉(+2) = C(18,11) = **31824** | 31824 | ✓ |
| ratio | 43758/31824 = **11/8** exact (gcd 3978) | 11/8 | ✓ |
| g(9) | enumeration = recurrence = closed form = **1540** = (3,1):1260 + (0,3):280; 280 = 9!/(3!³·3!) | 1540 = 1260+280 | ✓ |
| 343-triple census | exhaustive 7³ reproduces W₉ entrywise (Vandermonde) | IT.12(3) | ✓ |
| nucleonic sub-census | (Q_j∈{0,+1}) = (8000, 18000, 13500, 3375) at Q=(0,1,2,3) | same | ✓ |
| shares / complements | 18000/43758 = **1000/2431**; 13500/31824 = **375/884**; complements **25758 / 18324** | same | ✓ |

**Adversarial witnesses (non-vacuity):** the reversed ratio 8/11 ≠ 11/8 (orientation exhibited);
the nucleonic shares ≠ 1/2 and the nucleonic compositions are a strict MINORITY of their own
sectors (18000 < 25758, 13500 < 18324) — **sector ⊋ species** re-derived independently.

**Verdict:** IT.4's tritium computation is **CONFIRMED to the integer** by a from-scratch compute.
The status of 11/8 is unchanged from IT.14: a **channel-width ratio and the route-(ii) price seed**
— its mass reading is a priced-not-adopted declaration owed [BM.30(5)], quarantined from any
physical mass [P5].

---

## B. The grammar tipping point along N = 3, 6, 9, 12 (→ IT.17, Step 1 — CLOSES)

The contraction grammar [Def-BM.9(3); BM.31(2)] by the triple-certified engine:

| N (=3(k+1)) | k | g(N) | g_ε(N) (pure-ε backbone) | g_δ(N) (≥1 δ) | g_δ/g_ε | δ-share g_δ/g |
|---|---|---|---|---|---|---|
| 3 | 0 | 1 | 1 | **0** | 0 | **0** |
| 6 | 1 | 25 | 10 | 15 | 3/2 | 3/5 |
| 9 | 2 | 1540 | 280 | 1260 | 9/2 | 9/11 |
| 12 | 3 | 164395 | 15400 | 148995 | **387/40** | **387/427** |

- Both `g_δ/g_ε` and the δ-share are **strictly monotone** for N ≥ 6. At N=12 the δ-containing
  groupings outnumber the protected pure-ε backbone **387 : 40** (≈ 90.6 %).
- **The protection is UNIQUE to N=3** [BM.31(1),(6)]: g_δ(3)=0 because a δ sub-pairing on 3
  attachments leaves one dangling → 𝒞=0 → the colour block vanishes [D2.14; FT.19]; so
  ℰ_δ(𝒳_{N=3}) = ∅. And **g_δ(N) > 0 for every N ≥ 4** (witnessed to N=12).

**(P1) the premise refinement — δ-dominance is a DEGREE, not a kind-change at N=12.** The
δ-admixture is already present at **N=6 (the deuteron**, 15 δ-containing vs 10 pure-ε), a
constructed family member the record does **not** adjudicate as unbound. So "δ overwhelms the
backbone at N=12" is exact arithmetic, but it does **not** single out N=12: every multi-nucleon
support (N ≥ 6) already lacks the N=3 protection. Grammar alone cannot locate a last-bound member.

---

## C. The boundary-data census at N=12 (→ IT.17, Step 3 — PARTIALLY CLOSES)

- **Width:** W₁₂(Q) = C(24,Q+12) by fresh convolution — 25 classes, Σ = 4¹² = 16777216, symmetric,
  peak W₁₂(0) = C(24,12) = 2704156. The boundary charge datum Q of the 1p3n support class.
- **Θ_int-class mixture** [BM.31(4); Census FT.49(3); FT.22; FT.34(3)]: the pure-ε groupings
  (g_ε(12)=15400, the (0,4) block) carry **baryon-type Θ_int ∈ 4ℤ**; the δ-containing groupings
  (g_δ(12)=148995) drop to **Θ_int ∈ 2ℤ**. Grammar-weighted shares **40/427 (4ℤ)** and **387/427
  (2ℤ)**, summing to 1 — the N=12 ensemble spans **both** statistics classes. 4ℤ ⊊ 2ℤ (witness
  Θ_int=2 ∈ 2ℤ∖4ℤ), so the statistics label is a **partial** separator.

**(P2) "interior fuzz bleeding into the boundary" is REFUTED as stated.** It contradicts the
**measurement-horizon theorem** [IT.2; AT.29; AT.32(1)]: the non-transit boundary leaks no rung ≥ 2
summand, the interior is void-closed [D0.7; BM.143(1)], and the accessible content is EXACTLY the
triple (Q, Θ_int class, S) + |R| + n — **at every N**, uniformly. Machine witness: the width is a
pure function of Q at both N=9 (19 classes) and N=12 (25 classes); nothing interior bleeds. What
changes at N=12 is the **ensemble's statistics mixture** (a grammar-weighted span of two Θ_int
classes), **not** the sharpness of any member's boundary triple.

**(P4) the "scattering resonance" classification imports a category the ledger lacks.** A
*resonance* in the corpus is **an eigenvalue of a multi-chain ensemble with its two threshold
functions** [Def-BM.17; BM.114–BM.117], and *"nothing is stable as a category"* [Tier BM.21
locus]: there is no sharp bound-vs-scattering dichotomy to inherit, and the materialization
threshold's locus "is never empty at any n." Classifying N=12 as a resonance needs the **N=12
multi-chain eigenvalues + threshold/width evaluation** = IT-O2 (open). The empirical "H-4+ are
resonances" is a **[P5] scoring target**, quarantined, cited in no clause.

---

## D. The binding-read adjudication (→ IT.18, Step 2/4 — the honest core)

**The bridge that CLOSES (the "simple mathematical calculation bridge").** The **informational /
disjoint** binding read vanishes **exactly at every k**:

> E_int^disjoint(3(k+1)) = 6(k+1) [IT.7(1); BM.17(1); Census FT.35(2)] is exactly additive over the
> (k+1) nucleons (each 6), so **B_info = (E_comp − E_sep)·u = 0·u = 0** for k=0,1,2,3 (N=3,6,9,12).

This is BM.21(1) ("the informational binding read vanishes exactly") generalized along the family.
**Consequence:** the cutoff **cannot** arise on the informational read — the binding is *zero
uniformly*, so there is no sign change to locate a "last bound member." Machine certificate: the
coefficient is the integer 0 at every k (adversarial: it is neither >0 nor <0 anywhere).

**The residue that OPENS.** The only read that could distinguish bound from unbound is the
**ensemble / tree-connected** one:

- **Tree reading:** E_int^tree = 8k+6; its excess over the disjoint 6(k+1) is **exactly 2k** =
  (0,2,4,6) — the **connector residue** (k Σ₁₂-species connectors, 2 edges each) [IT.7(1);
  IT.12(4); FT.34(3)]. Whether that 2k is *binding* or *stress* is the **connector SPECIES**
  (count, winding d, fusion) — **UNCONSTRUCTED (IT-O4)**. The directive's "unsealed connector
  stress" *is* that unconstructed connector.
- **Constructed-read census — every derived binding read is ≤ 0:** BM.137(3)'s two-chain
  𝓑_ens^(2) = −4u/(1+u)·(ln2/𝔥) = −16ε_q/(1+4ε_q)·(ln2/𝔥), re-derived and **strictly < 0** on a
  63-point rational ε_q grid (=0 iff ε_q=0); BM.21(4)'s three-constituent B(S_j;1,1,1) < 0 in every
  sector [frozen]. **Neither is an INTER-nucleon (multi-seal) binding** — BM.21 is *intra*-nucleon
  (3 constituents → one nucleon), BM.137 is the two-chain meson/lepton floor. The inter-nucleon
  binding object is **absent from the inventory**.

**(P3) "B_ens ≥ 0 at N=12, B_ens < 0 for N ≤ 9" has no derived support.** No constructed read gives
≥ 0 (zero non-negative witnesses in the sign census); the informational read gives exactly 0 at
*every* k (so not "< 0 for N ≤ 9" either). The claim is a **conjecture**, recorded — not forced —
per the exploration-state instruction.

**The adjudication (Step 4).** The hydrogen isotope cutoff at k=2 is **NOT a derived row**. What
closes: the grammar tipping point (B), the N=12 boundary census (C), and B_info = 0 (D). What is
gated: the inter-nucleon binding read (needs IT-O4 connectors + IT-O2 amplitude) and the resonance
classification (needs the IT-O2 multi-chain eigenvalues). ⇒

> **NEW OPEN ROW IT-O5 — the inter-nucleon (multi-seal) binding read and the hydrogen isotope
> cutoff.** The "last bound member" question for the 1p-kn family. Gated on **IT-O4** (the
> nucleon–nucleon connector species: count, winding d, fusion — the sign of the 2k tree residue)
> and **IT-O2** (the Def-H.32 amplitude sum over the N=3(k+1) grouping sectors with (−1)^ℵ
> dressing). Sharpens, does not contradict, IT.4's residues. The empirical H-4+ resonance fact is a
> quarantined [P5] target, cited nowhere.

---

## Check ledger (`isotope_cutoff.py`, 20/20)

| § | checks | content |
|---|---|---|
| A | A1, A2, A2x, A3, A4, A4x | the forward compute: W₉ = C(18,Q+9); the doublet sectors 43758/31824, 11/8; g(9)=1540=1260+280; the 343-triple Vandermonde + nucleonic shares; + orientation and minority adversarial witnesses |
| B | B1, B2, B2x, B3 | the N=3,6,9,12 grammar census (three engines); the monotone g_δ/g_ε and δ-share; the protection-uniqueness at N=3 and the deuteron-already-mixes refinement (P1) |
| C | C1, C2, C2x, C3 | W₁₂ = C(24,Q+12); the Θ_int 4ℤ/2ℤ mixture (40/427, 387/427); 4ℤ ⊊ 2ℤ; the horizon-holds-uniformly witness (P2) |
| D | D1, D1x, D2, D3, D3x, D4 | B_info = 0 exactly at every k (the bridge); the 2k connector residue (IT-O4); the constructed-reads-≤0 census; the no-derived-unbound witness; the IT-O5 adjudication |

**Declarations issued: none. §Cal-IT stays empty.** No species identified; no measured value in any
clause [P5]; prices not masses [BM.30(5); BM.37(6)]; no currency mixing [BM.83; BM.134(5)]; the
Level-5 record and Tier IT.4 cited, never edited [AT.63(2)].

**Open rows after IT.5:** IT-O1 (transit-leg), IT-O2 (N≥4 amplitude, sharpened at N=9 by IT.4),
IT-O3 (handshake), IT-O4 (connector species, gating), **IT-O5 (the inter-nucleon binding read /
the isotope cutoff — new)**, and the owed **mass-read route choice** declaration [IT.14(3)].
