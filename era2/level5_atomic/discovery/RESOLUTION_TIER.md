# RESOLUTION_TIER — session 7 discovery record (Level 5 / Era 2, the Atomic era)

> **Directive (Architect):** *"Please proceed to resolve AT-O11, 28, 06, and 31 for the next tier."*
>
> **Result: all four rows resolved.** AT-O11 CLOSED (the conjugacy table is complete — the
> dictionary's image is the volume coordinate alone, at every carrier level, with n(n−1)/2
> pair-bit conjugates and a Catalan-fed metric-blind kernel). AT-O28 CLOSED AS CONSTRUCTION (the
> global Dirac-type operator built on the tetrahedral floor as an explicit finite family; the
> base-frame slot DISSOLVED as derived gauge; the lift slot proven PHYSICAL — it decides the
> index; a third slot discovered and named: the discrete vielbein). AT-O31 RESOLVED AS GRAMMAR
> (the fine-structure-type splitting grammar: unmoved positions × ray phases × opposite electric
> / common magnetic ray splittings × measure intensities — all quantized; values stay behind
> (M1′)–(M3′)). AT-O6 CLOSED OUTRIGHT (the exhaustive seat census: four seats, all constructed,
> no unnamed direction left). Three new checkers — `dict_nfolds.py` 13/13, `global_dirac.py`
> 12/12, `fine_structure.py` 8/8 — suite **37 checkers, 643 exact markers, 0 failures**; format
> gate **13 Part 5 documents PASS**. Candidate tags AT.59–AT.62, Tier AT.11. Declarations
> issued: none. P5 quarantine untouched.

---

## I. AT-O11 — the metric dictionary at every carrier level (`dict_nfolds.py`)

**The row's history.** Opened in Tier AT.2: "whether the nine metric coordinates with no carrier
conjugate (conformal, 5 shear, 3 shift) acquire one at higher carrier level." Sharpened by
AT.40(5): the invariant supply is the Catalan number `C_n = dim End_SU(2)((ℂ²)^⊗n)` — 13 free
invariants at n=4 against the metric's ten coordinates — "a DICTIONARY gap, not an invariant
gap." Made decidable by AT.50(6): `dim 𝒦_{n≥4} = 26`.

**The squeeze (no heavy elimination).** On (ℂ²)^⊗n, n=2,3,4: the isotypic projectors Π_j by exact
Lagrange interpolation in S²_tot (minimal polynomial, idempotence, orthogonality, ΣΠ_j = I,
traces m_j(2j+1) all verified) give m_j = (1,1), (2,1), (2,3,1); `dim End_SU(2) = Σm_j² = 2, 5,
14` — the Catalans [AT.40(5) reproduced]. Every S_n permutation operator commutes with the
diagonal action and their span has rank exactly Σm_j² — **the commutant IS the permutation span**
(Schur-Weyl by dimension squeeze): the gauge-invariant reads are exactly the exchange reads
Tr(πρ). n=2 reproduces AT.12(2)/AT.15(1) matrix-for-matrix (SWAP = ½(E₀+Σ), Π_𝒭 = ¾E₀+¼Σ).
The permutation representation itself verified genuine (P_πP_σ = P_{πσ}, 36 products).

**THE CONJUGACY THEOREM (the answer).** Embed every CT1.2 aspect generator [CT0.12's blocks] on
every pair (ij) of the n-fold carrier and apply AT.12(1)'s own criterion ([X_emb, S_a] = 0 ∀a,
S_a = ½Σᵢσ_a^(i)): **exactly Σ^(ij) (the H aspect — the volume mode) and E₀^(ij) (the identity,
trace-fixed, zero free content) pass — at every n, every pair** (160 exact commutator tests;
pass census 1+1 / 3+3 / 6+6). W-embeddings fail because W_i^(12) = S_i *is* the gauge generator
(exact matrix identity at n=2); G-embeddings transform as spin-2; J± as spin-1/adjoint. **The
AT.15(5) "none" rows are theorems at every level: conformal, shear and shift NEVER acquire
carrier conjugates.** AT.15(4)'s T-parity mismatch is the n=2 shadow of the commutant failure —
two faces of one theorem.

**The positive supply.** Π_𝒭^(ij) = ¾I + ¼Σ^(ij) is an idempotent of trace 3·2^{n−2} for every
pair at every level [AT.15(1),(2) generalized]: the pair bits b_(ij) = ¾ + ¼⟨Σ_(ij)⟩ are
n(n−1)/2 gauge-invariant volume reads (1, 3, 6 at n=2,3,4). **The Casimir identity**
Σ_(i<j)Σ_(ij) = 2S²_tot − (3n/2)I exactly — the total volume read IS the isotypic-weight
(central) read; the traceless pair differences are exchange-resolved (non-central, witnessed).
Rank census: r₂=1, r₃=3, r₄=6; span{Σ} ∩ centre = exactly the Casimir line (union ranks 4, 8 =
r_n + #j − 1).

**The accounting (the "13 vs 26" framing corrected).** Carrier invariants and the mask space 𝒦_n
are different currencies [BM.83; BM.134(5)] — the count comparison never was a conjugacy
question. The dictionary map: IMAGE = volume alone; GENUS = the r_n pair bits; KERNEL = the
multiplicity coherences + the non-Casimir central line — metric-blind exchange content. At n=4:
**13 = 6 volume-conjugate (1 central Casimir + 5 exchange-resolved) + 7 metric-blind**; at n=3:
4 = 3 + 1. *The Catalan growth feeds the exchange reads, never new metric coordinates: the
higher carriers see more of each other, not more of the metric.*

**Scope.** n=3 accessible (D_tick(3) = 16 = C_cap); n=4 formal at every accessible rung
(2⁵ = 32 > 16) — AT.50(5)'s third-branch discipline verbatim. BM.131(6)'s Π_k re-certified
(rk = k+1) and shown to BE the top isotypic projector (matrix equality) — its "k invariants"
suggestion stays superseded by AT.40(5)'s Catalan count, recorded not retracted. (R7′) receives
the permutation-span census as Level-5 data (contributes, does not close the Part-4 row).

## II. AT-O28 — the global Dirac-type operator (`global_dirac.py`)

**The floor.** Tetrahedron: 4 vertices, 12 arcs, Rot = 12 simply transitive [AT.34(1)-(3) —
re-produced: exactly one rotation per arc, exhaustive]. Binary tetrahedral lift 2T rebuilt
(24 elements, closed under 576 products, det 1); the Ad-map 2T → Rot is two-to-one and
SIGN-FREE (R_{−U} = R_U) — sections through it are well-defined despite the cover's sign
ambiguity. **Marked-row discipline: the lift stays Def-H.37(2)'s declared identification
(Open Gaps 19), inherited at use.**

**The operator.** On ℂ⁴_v ⊗ ℋ_ext ⊗ ℂ²_T (32-dimensional):

    D_floor = Σ_{edges {v,w}} E_vw ⊗ γ_{a(e)}(F_e) ⊗ T_e + E_wv ⊗ γ_{a(e)}(F_e) ⊗ T_e†

— section F_e per arc (two lift readings), a(e) the edge→gamma labeling, T_e the transport
(reverse arc = dagger ⟹ Hermitian by construction, verified on all 72 + witnesses).

**The section census.** Seed-only Ad(U⊗I): all 6 shortlist frames are fixed points (144 checks)
→ CONSTANT section [AT.47(5) reproduced]. Diagonal Ad(U⊗U): shortlist = 2 orbits × 3 [AT.47(5)
reproduced]; the section runs through 3 frames (12 distinct signed Pauli directions) over the
12 arcs.

**THE CHIRALITY DICHOTOMY (the lift slot is PHYSICAL).** The global grading nullity
dim{M : {M, every section gamma} = 0} — a similarity invariant, hence GAUGE-INVARIANT — is
**exactly 1** for seed-only (the unique grading = ± the frame's own pseudoscalar; 6 frames →
3 grading directions × 2 signs, direction census by exact elimination) and **exactly 0** for
both diagonal-orbit sections. Seed-only ⟹ 𝒟_floor chiral-odd ({𝒟,Γ}=0, Γ²=I₃₂, spectrum
±-paired, kernel reads exact — nullities 0 on all four witness profiles); diagonal ⟹ no global
grading exists. **The two readings of the marked lift are NOT gauge-equivalent: the lift
declaration decides whether the global operator has an index.** That is the exact physical
content of the corpus's oldest declared slot.

**SLOT (b) DISSOLVES.** Φ(M) = VMV⁻¹, V = I₂⊗S [Def-H.34's S — DERIVED, not marked] is an
algebra automorphism (105 Pauli-pair identities), maps the shortlist to itself with **one orbit
of 3 frames** (cycling the grading directions) — the menu's other factor 2 is the frame-reversal
sign involution: 6 = 3 × 2, both derived. Operator level: (V⊗I_T)𝒟(F,T)(V⁻¹⊗I_T) = 𝒟(ΦF, T)
exactly, for all 6 frames against a mixed lattice profile. **All six base-frame choices give
unitarily equivalent operators up to profile signs — the base-frame slot is a derived gauge, not
a physical choice.** (Sharper than AT.47(4)'s gamma-value row: the orbit census at the
frame-element level.)

**THE GLOBAL WEITZENBÖCK.** 𝒟_floor² = 3·I₃₂ + (triangle blocks) EXACTLY: every diagonal 8×8
block is the degree Laplacian of K₄ (3-regular) times the identity — γ² = I and TT† = I do the
work — **transport-independent** (flat vs Pythagorean profiles give identical diagonals); every
off-diagonal block is exactly the sum of the TWO triangle 2-path terms γ_aγ_b ⊗ T_vwT_wz (4
profiles × 6 blocks, entrywise). **All curvature content of the global square lives on the
2-simplices** — the global born term localizes on the triangles, where the floor's holonomy
lives [AT.46; AT.57's fiber identity is its local factor].

**Triangle holonomy census.** Drag profile: closed-triangle reads diag(i^{±Θ}, i^{∓Θ}), integer
windings Θ ∈ {±1, ±3} on the four triangles × both orientation conventions [AT.46(5)'s D_drag
read on the floor's 2-simplices]; EW fourth-root lattice: Gaussian-integer entries throughout
[AT.57(7)'s economy at the global level]. No continuous locus, no eighth root.

**THE VIELBEIN SLOT (new, named).** Rot acts transitively on the 6 undirected edges (orbit
census: one orbit of 6 from 72 rotation-edge images) ⟹ an equivariant edge→gamma-index labeling
is CONSTANT, and a constant labeling degenerates the Clifford structure. **The global operator
necessarily breaks the floor symmetry to the labeling's stabilizer**: the discrete vielbein is a
THIRD enumerated datum (4⁶ = 4096 labelings on K₄), alongside the lift and the profile. Derived
rows verified labeling-independent (3 witnesses: modular, perfect-matching, asymmetric).

**Verdict.** AT-O28 CLOSED AS CONSTRUCTION. Remaining (declaration/calibration species, not
math): the lift declaration itself (now with exact physical content — the index dichotomy), the
vielbein choice, the P4 transport profile (ℓ_c, 𝐜) [AT.47(6),(9)(iii)], and the extension census
to the other four platonic floors + the polygon ladder (recipe derived; new row **AT-O32**,
blocking nothing).

## III. AT-O31 — the fine-structure grammar, and AT-O6 — the exhaustive seat census (`fine_structure.py`)

**The ray-wise grammar.** 𝖲^±ᵢ = ∓(σᵢ⊗I)P_± reproduced [AT.56(6)]; **the Casimir per ray:
Σᵢ(𝖲^±ᵢ)² = 3P_± EXACTLY** — each ray of the orientation doublet carries a full spin-½ su(2)
at scale −2 (Casimir 4·¾ = 3, an integer; identification with any measured multiplet
QUARANTINED [P5; Def-BM.3(7)]).

**THE SPLITTING LAW.** The electric channel is RAY-ANTISYMMETRIC (P₊e_aP₊ = −σ_a⊗P₊ vs
P₋e_aP₋ = +σ_a⊗P₋; the ray blocks are ω̂-conjugate negatives), the magnetic channel
RAY-SYMMETRIC (W_c acts identically within both rays). Hence the born Pauli term [AT.57(2),(4)]
**splits the two rays in OPPOSITE directions through its electric curvature feed and shifts them
COMMONLY through its magnetic curl feed — the ledger's j = l ± ½-type doublet grammar**, flagged
¬identified. Witness (the AT.57(E4ii) profile, rebuilt from scratch): the born term is
block-diagonal on the rays (cross blocks zero; born = born₊ + born₋ exactly) with the
conjugation laws mag₋ = +ω̂mag₊ω̂, ele₋ = −ω̂ele₊ω̂ — integer 8×8 identities. (Session-7 error
caught by the machine: the first draft claimed ele₊ + ele₋ = 0 — false, the electric channel is
κ̂-diagonal so its ray blocks SUM to it; the antisymmetry is ω̂-conjugate, not vanishing.)

**The quantized splitting census.** Over the fourth-root lattice: 12 live electric feeds (zero
criterion exact), every ray-splitting value a Gaussian integer times 2 — **no continuous
splitting locus before any measure** (AT.54(6)'s no-go at the splitting level).

**The composed read (grammar, not values).** A ladder level of the hydrogen connector carries:

    (position W_d = 1/(d²x₊x₋), UNMOVED [AT.44(5); AT.54(3)])
  × (ray phases i^{Θ±} [AT.46(5),(6); Def-BM.16(5)])
  × (common magnetic shift ± opposite electric splitting [above])
  × (sector intensities [AT.52(1); AT.54(1),(2)])

Witness cell, exact: AT.46(6)'s witness-B windings (Θ₊,Θ₋) = (18,24) → phases (−1,+1) —
OPPOSITE statistics classes on one geometry; the theta-cell intensities Z^amp/Z^norm =
(128,256,128)/(288,576,288) = **4/9 uniformly — a q-blind attenuation** (new small row from the
frozen AT.54(2) integers). The composed table is fourth-root × integer × rational with NO
position shift anywhere: **fine structure in this corpus is a ray/sector splitting at unmoved
prices** — AT.54(3)'s Lamb-analog logic one level down. AT-O31 RESOLVED AS GRAMMAR; the value
conversion stays behind (M1′)–(M3′) [AT.54(6)] + the AT-O28 declaration residue.

**THE EXHAUSTIVE SEAT CENSUS (AT-O6).** The Pauli algebra [AT.56(7)] has 8 directions; as
coupling directions 7 matter (I₄ spectrally inert — verified: adding c·I₄ leaves the splitting
set {0,±2} exactly, four c witnesses). The contraction image re-censured: hit directions are
EXACTLY the 3 magnetic + 3 electric; the (0,3) and (0,0) components zero in every contraction
(grade separation); M̂ purely (0,3). The feeds, complete:

| seat | direction | feed | status |
|---|---|---|---|
| boundary moment | κ̂ | the scalar EM boundary read q [AT.48(2a)] | constructed |
| dressing | (sign) | (−1)^ℵ, the frozen A8 weight [Def-H.32(2)] | constructed |
| magnetic functional | W_c (3) | the shift wᵢ alone [AT.2(4); FT.157(1); AT.6 up to ϰβ, AT.34] | constructed (marked (S)) |
| born Pauli | e_a (3) | the transport curvature 𝔈_a = [T_a,T₄] [AT.57(4)] | constructed (marked profile) |
| σ_c⊗I₂ (3) | — | NO linear seat: products e_aκ̂ and 𝖲^± supports only [AT.56(3),(6)] | proved |

Impossibility rows close the census: no native index-carrying EM read [AT-O29/AT.48(3), grade
reason AT.56(5)]; no M̂ from any bivector contraction [AT.56(5)]; no third channel [AT.56(4)];
no loops [BM.88(1)]; no e issued [EM.25(7)]; no continuous locus [AT.53(3); AT.54(6); AT.57(7);
B4 here]. **FOUR SEATS, ALL CONSTRUCTED, NO UNNAMED DIRECTION LEFT — AT-O6 CLOSED outright.**

## IV. Check ledger

- `dict_nfolds.py` — **13/13 EXACT**: A1 (CT0.12 blocks, ranks 1/1/5/3/3/3, the 2 non-orthogonal
  G-diagonals counted), A2 (carriers, su(2), permutation homomorphism 36), B1 (the squeeze:
  Lagrange projectors, Catalans 2/5/14 = permutation-span ranks), B2 (n=2 matrix reproduction),
  B3 (centre = isotypic weights, 80 commutators), C1 (160 embedding tests), C2 (W_i^(12) = S_i +
  T-parity), D1 (pair-bit idempotents), D2 (Casimir identity ×3), D3 (ranks 1/3/6, central
  intersection 1, non-central witnesses), D4 (the accounting + union ranks), E1 (admissibility
  n=0..8), E2 (BM.131(6) = top isotypic, matrix equality).
- `global_dirac.py` — **12/12 EXACT**: A1 (30/6 frames), A2 (2T: 24, closed, det 1, 2-to-1
  sign-free), A3 (simple transitivity 12/12), B1 (section census: 144 fixed + 2×3 orbits),
  B2 (nullity dichotomy 1 vs 0 + grading direction census), C1 (Φ automorphism: 105 identities,
  orbit 3 × signs), C2 (skeleton equivalence, all 6 frames), D1 (72+ operators: Hermitian,
  chiral-odd seed-only, diagonal fails), D2 (global Weitzenböck: 24 diagonal + 48 off-diagonal
  block identities, transport-independence), D3 (16 triangle holonomies), D4 (Γ²=I₃₂, ±spectra,
  kernel nullities {flat:0, drag:0, ewlat:0, pyth:0}), E1 (edge transitivity: one orbit of 6).
- `fine_structure.py` — **8/8 EXACT**: A1 (ray algebra), A2 (M̂ gates), B1 (Casimir 3P±),
  B2 (splitting law: 12 ray-block identities), B3 (the witness: block-diagonality + conjugation
  laws), B4 (lattice splitting census: 66 + integrality), C1 (composed witness cell: phases
  (−1,+1), uniform 4/9), D1 (the seat census: image directions, grade separation, inertness).

Suite after this session: **37 checkers, 643 exact markers, 0 failures, exit 0**; format gate:
**13 Part 5 documents PASS** (AT.59–AT.62 consolidated in `tiers/Part5_Atomic_era_TierAT11.md`).

## V. Error profile this session

- **ele₊ + ele₋ ≠ 0** (B3 first draft): the electric channel is κ̂-diagonal, so its ray blocks
  sum to it; the antisymmetry is the ω̂-conjugation law. Caught by the explicit witness before
  any tier text was written — the witness-first discipline paying for itself.
- **M̂² vs κ̂M̂ sign slip** in the A2 gate (κ̂·(−κ̂) = −I): caught instantly by the checker.
- **Φ's orbit on FRAMES is 3, not 6** — AT.47(4)'s "one S-orbit" is the orbit on gamma VALUES
  (±σ₀⊗σᵢ as sign classes); at the frame level the orbit is 3 and the sign involution supplies
  the factor 2. The tier states the sharper decomposition 6 = 3 × 2.
- **Basis vectors return scaled**: the nullspace basis of the grading system can come back as
  i·(σ₀⊗σ₂) — direction matching must scan the fourth roots, not just signs.
- Gauss(Fraction) `__repr__` crashes on debug prints (a duality.py cosmetic) — print via mkey.

## VI. Adjudication summary

| row | disposition |
|---|---|
| AT-O11 | **CLOSED** — the conjugacy table complete: image = volume alone at every n; genus = the r_n pair bits; kernel = exchange coherences; the "13 vs 26" framing corrected (cross-currency) |
| AT-O28 | **CLOSED AS CONSTRUCTION** — the operator built (finite parametric family, first floor); slot (b) dissolved (derived gauge); slot (a) physical (index dichotomy); slot (c) discovered+named (vielbein); residue = declarations + calibration + AT-O32 |
| AT-O31 | **RESOLVED AS GRAMMAR** — the composed fine grammar derived and quantized; values behind (M1′)–(M3′) [P5] |
| AT-O6 | **CLOSED OUTRIGHT** — the seat census exhaustive: four constructed seats, every other direction impossible with its ground |
| NEW AT-O32 | the per-floor extension census of the global operator (other four platonic floors + polygon ladder; recipe derived [AT.60]; blocking nothing) |

> *The corpus rewards: read the whole rather than the era; treat every "absent" as level-local;
> let exact arithmetic, not plausibility, decide. — AT.39 Phys*
