# EXOTIC_STATES.md — the session-13c working record (Tier IT.7 candidate, IT.22–IT.24)

**Directive (Architect, session 13c).** *"Adjudicate the 'Exotic States' Read-Tier Question via the
LHC Census Mapping … map the LHC experimental census to the corpus's N=4 and N=5 support
decompositions, and the proton's exotic sign triples. Close this read-tier question as a derived
structural feature, not an anomaly. … Please use the LHC data as ext class as we maintain in era 1
too."*

**Machine.** `checks/exotic_states.py` → **17/17 EXACT**, no floating point, **no external datum in
any computation**. Suite 8 checkers / 121 markers; gate 7 docs / 24 IT-blocks.

---

## 0. Premise audit — the citations hold; the [EXT] discipline is the load-bearing constraint

Every cited row was verified against the canon/tier record before building:

- **IT.6(5)** ✓ — *"the grammar transition is at N=4 … the N=4 support itself is the double-mesonic
  ('tetraquark-type', quoted) support: g(4)=3 (the three perfect matchings), ALL δ, g_ε(4)=0."* And
  IT.6(2): the family is N=3(k+1), so it **never passes through N=4 or N=5** (off-family support classes).
- **IT.9(4)** ✓ — *"N=5 IS FORCED-MIXED … 2a+3b=5 has the UNIQUE nonnegative solution (1,1) ⟹
  g_ε(5)=0 is forced."*
- **IT.12(3)** ✓ — the 343-triple census; nucleonic shares 1000/2431 & 375/884; *"the proton's own
  N=3 sector contains (+1,+1,−1) triples [BM.28(2)]."*
- **No pre-existing "exotic states" open row** — this is a *new* read-tier adjudication, not the
  closure of a named gap. Recorded as such (no fabricated row closed).

**The [EXT] convention (era-1, mirrored exactly):** Census §"External-data quarantine" + **FT.114** —
external data is *"tested, never trusted; it enters no derivation"* [P1, P5]; it lives in a dedicated
audit clause; the numerical coincidence and the structural origin are **reported separately**; *"no
identification … with any particle species is made or implied"*; and it is **machine-scanned** that
the [EXT] tokens are confined to that clause (FT.114 §H). The Architect's closing instruction
("use the LHC data as ext class as we maintain in era 1 too") is precisely this.

---

## A. The support classes are derived, exactly (→ IT.22)

| support | g(N) | block type | g_ε (pure-ε / baryon-type) | the derived verdict |
|---|---|---|---|---|
| **N=4** | 3 | all (2,0) — the three perfect matchings | **0** (4 ≢ 0 mod 3) | forced **entirely δ-paired** (mesonic-type); no baryon sector |
| **N=5** | 10 | all (1,1) — 2a+3b=5 unique | **0** (forced) | **100% mixed** (one δ-pair + one ε-triple); no pure-baryon sector |

Both are off-family (N ≢ 0 mod 3 [IT.6(2)]) — they are support *classes* the partition rule admits,
not 1p-kn family members. Statistics [IT.6(6); BM.31(4)]: all-δ / all-mixed ⟹ Θ_int ∈ 2ℤ only; **no
4ℤ baryon-type sector at N=4 or N=5**.

## C. The interior is majority-exotic (→ IT.22(3),(4))

- **N=3, Q=+1 sector:** 6 ordered ternary triples = 3 (+1,0,0)-type + 3 **(+1,+1,−1)-type** — the
  "exotic" sign triples telescope to the *same* boundary charge [BM.28(2)].
- **N=9:** the nucleonic compositions carry **1000/2431** (Q=+1) and **375/884** (Q=+2), both **< ½**;
  the exotic complements **25758 / 18324** are the **majority** — *sector ⊋ species* [IT.12(3)].

## D. The read-tier closure (→ IT.23)

The inter-system registration read is **rung-2 mediated and reads only the telescoped q_EM**
[IT.1(1),(3); FT.20; CT0.13]. Machine witness: all 6 distinct N=3 Q=+1 interiors collapse to **one**
boundary read (+1); at N=9 the 43758 interior sign states collapse to one. The interior multiplicity
is **preserved but inaccessible** (the measurement horizon [IT.2; AT.29; AT.32(1); D0.7; BM.143(1)]).

⟹ **the "exotic states" are NOT new particles and NOT an anomaly** — they are the ensemble's interior
grouping multiplicities (majority at N=4,5,9), which the read tier resolves only to the boundary
charge. The "exotic" label is the identification layer's, applied where the read is blind.

## E. The [EXT] quarantine, machine-enforced (→ IT.24(2))

`exotic_states.py` §E scans the tier document (the FT.114 §H pattern):

- the species names **{tetraquark, pentaquark, intrinsic charm, LHC}** occur in **NEITHER derived
  tag** — IT.22 and IT.23 are **token-free** (counts `{IT.22: 0, IT.23: 0, IT.24: 8}`);
- they live only in the **IT.24 [EXT] audit clause** + the framing (header/mandate), quarantined;
- **ZERO decimal numeric tokens** in the whole tier — no mass, no width, no lifetime, no [EXT] number.

The mapping (N=4 ↔ "tetraquark", N=5 ↔ "pentaquark", exotic sign triples ↔ "intrinsic charm") is a
**species-naming act** [Def-BM.3(7)], reported separately from the structural origin (the grammar),
which is computed with **zero external input**.

## The adjudication + the scoping refinement (→ IT.24)

- **CLOSED at the read tier** as a derived structural feature: the support classes and exotic sign
  triples are theorems of the contraction grammar [Def-H.32(1); Def-BM.9(3)], derived **without
  importing quarks or a gauge theory**.
- **SCOPING REFINEMENT (on the record):** "the corpus predicted the exotic hadrons" is qualified —
  the corpus derives the **combinatorial structure** (support classes, multiplicities, δ/ε and
  sign-triple composition), **not** the particles' masses, widths, or existence-as-resonances (those
  need the ensemble/amplitude binding = **IT-O2**, unconstructed). The attachment count N is a ledger
  datum, **not** a quark count — the N ↔ quark-number map is itself [EXT] identification content.
- **No new open row.** The only residue touched is the standing one: the spectrum/mass side of any
  support class waits on IT-O2 (unchanged, re-cited).

**Declarations issued: none. §Cal-IT empty.** No species identified in any derived clause; no measured
value [P5]; prices not masses; Level-5 and IT.4/IT.5/IT.6 cited, never edited.

## Check ledger (`exotic_states.py`, 17/17)

| § | checks | content |
|---|---|---|
| A | A1, A1x, A2 | N=4: g=3 all-(2,0), g_ε=0, no baryon sector; all-δ statistics (2ℤ) |
| B | B1, B1x, B2 | N=5: 2a+3b=5 unique (1,1), g=10, g_ε=0 forced; no pure-baryon sector |
| C | C1, C1x, C2, C2x | N=3 exotic sign triples (6=3+3, all → +1); N=9 nucleonic minority (< ½), majority-exotic |
| D | D1, D2, D3 | the telescoping read (6→1; 43758→1); the horizon; the read-tier closure |
| E | E2, E3, E4, E1 | the [EXT]-confinement scan (IT.22/IT.23 token-free); the audit clause present; zero decimals; the adjudication |

**Open rows after IT.7:** unchanged — IT-O1, **IT-O2 (the sole gate on IT-O5)**, IT-O3, IT-O5, the
owed route choice; **IT-O4 stays CLOSED** [IT.21(1)]. No new row opened.
