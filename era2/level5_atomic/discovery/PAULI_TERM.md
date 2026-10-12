# PAULI_TERM — session 6 discovery record (Level 5 / Era 2, the Atomic era)

> **Directive (Architect):** *"Please continue on the Pauli things."*
>
> **Result: the Pauli term is now a constructed ledger object.** The σ^{μν} census on the native
> frame is exact (six signed Pauli products, two channels, no third); AT.48(3)'s decomposition
> theorem is upgraded from *stated* to *mechanized*; and the Weitzenböck identity — the Pauli
> term **born from the Dirac skeleton's square at tree coefficient exactly 1** — is proved
> *fully symbolically*, slot-free, so AT-O28's two declared slots do not block it. The transport
> curvature is censused on both constructed families: the drag connection is **fiber-abelian**
> (it never births a Pauli term; frame-dragging changes statistics, not moment), and the EW.32
> curvature is **Gaussian-integer valued** on the fourth-root lattice (12 live curvatures of 66
> pairs, every value ±2iσ_k) — the connection-side confirmation of AT.54(6)'s *no continuous
> locus*. 23/23 exact checks (`pauli_term.py`), candidate tags AT.56–AT.58, Tier AT.10.
> Nothing adopted, no declarations, P5 quarantine untouched.

---

## I. Which "Pauli things" — the threads the record left live

1. **AT.48(3)'s DECOMPOSITION THEOREM** — "σ^{μν}F_{μν} splits into the native pseudoscalar
   channel (constructed) + AT.6's shift-mediated magnetic channel (up to ϰβ)" — was *stated and
   adjudicated* in session 3c, but the channel census was never mechanized as exact matrix
   identities. This session mechanizes it, and finds two rows nobody had stated: the **Hodge
   row** (M̂ *is* the duality rotation) and the **ray-wise so(4) split** (the two su(2) copies
   live on the two rays of the orientation doublet).
2. **AT-O28** (priority 1): the global Dirac-type operator, "two slots away". The slots (the
   marked lift [Def-H.37(2)/Open Gaps 19] + the base frame per floor [AT.47(4),(5)]) block the
   *evaluation* of a global operator — but the Pauli term's birth from the skeleton's square is
   a **slot-free algebraic identity**: it holds for every assignment of the undeclared slots,
   and the machine proves it with 16 independent indeterminate transport entries.
3. **frame_section.py's residue (iv)**: "the σ^{μν}F_{μν} moment coupling — needs (i)–(iii) AND
   the global operator". Superseded **in scope** by this session: the coupling is constructed
   [AT.48], the Pauli-tensor anatomy is derived here; what needed the slots was the evaluation,
   never the algebra.
4. **The other Pauli** — exclusion — is derived and standing (dim ∧²(ℂ²) = 1, dim ∧³(ℂ²) = 0
   [BM.128(5)]); re-certified as a gate, untouched.

The magnetism route's old verdict stands and is *sharpened*: session 1 was right that a Pauli
term "presupposes a B to couple to" and that B is a reading, not a substance — but the smooth
σ^{μν}F_{μν}, pulled back to the native frame, needs no B: it decomposes into readings the
ledger already owns (the charge read on the pseudoscalar, the shift on the gauge block), and
its curvature-born part is fed by the *transport commutators*, which are ledger objects too.

## II. The bivector census (machine §§A–B)

Frame: F₀ = (σ₁⊗σ₂, σ₂⊗σ₂, σ₃⊗σ₂, σ₀⊗σ₁) [FT.93(2); AT.47(1),(3)], pseudoscalar
γ_{F₀} = γ₁γ₂γ₃γ₄ = σ₀⊗σ₃ = I⊗κ̂ (the relocation row). Euclidean read — A3's η labels the
T-involution only [CT1.1]; no Minkowski structure enters anywhere.

σ^{μν} := (i/2)[γ_μ, γ_ν]. All six are Hermitian, square to +I₄, traceless, and each is
**±1 × exactly one Pauli product** — six distinct directions of the 15, species 3 mixed +
2 off-diagonal-spatial + 1 diagonal:

| bivector | exact value | channel |
|---|---|---|
| σ^{12} | −(σ₃⊗σ₀) = −2W₃^ext | magnetic |
| σ^{13} | +(σ₂⊗σ₀) = +2W₂^ext | magnetic |
| σ^{23} | −(σ₁⊗σ₀) = −2W₁^ext | magnetic |
| σ^{14} | σ₁⊗σ₃ = (σ₁⊗I₂)γ_{F₀} | electric |
| σ^{24} | σ₂⊗σ₃ = (σ₂⊗I₂)γ_{F₀} | electric |
| σ^{34} | σ₃⊗σ₃ = (σ₃⊗I₂)γ_{F₀} | electric |

**The channel identities (exact matrix equalities):**
- MAGNETIC: σ^{ab} = −2ε_{abc}W_c^ext — *the magnetic bivectors ARE the gauge block of the
  extended carrier* [EW.32 carrier; AT.47(2)], index-carrying exactly as AT.47(2)'s maximality
  theorem demands (the spatial gammas carry the gauge index — and so do the spatial bivectors).
- ELECTRIC: σ^{a4} = σ_a⊗κ̂ = (σ_a⊗I₂)·γ_{F₀} — the internal Pauli times the shortlist
  pseudoscalar, which is M̂'s matrix [AT.48(2a)].
- BRIDGE: σ^{a4} = −ε_{abc}σ^{bc}γ_{F₀} — the electric channel is the magnetic channel times
  the pseudoscalar. **The two channels of AT.48(3) are the two grades of ONE Cl(3,0).**

**Lie closure** (15 commutators, Gaussian-integer structure constants): [W₁^ext,W₂^ext] =
iW₃^ext (the magnetic channel closes — su(2)-type); [e₁,e₂] = 4iW₃^ext (the electric channel
closes ONTO the magnetic); [W₁^ext,e₂] = ie₃ (adjoint action). **The generated algebra is
exactly 8-dimensional**: span{I₄, σᵢ⊗I₂, σᵢ⊗κ̂, I⊗κ̂} — the Cl(3,0) the electric channel alone
generates. **The Pauli term adds ZERO new operators to the corpus.**

**The ray-wise so(4) split** (the surprise row): with the Hodge star of the frame's Euclidean
read (ε₁₂₃₄ = +1), the self-dual/anti-self-dual combinations collapse to

    Σ⁺ᵢ = ½(σ^{i4} + *σ^{i4}) = −(σᵢ⊗I₂)P₊,     Σ⁻ᵢ = ½(σ^{i4} − *σ^{i4}) = +(σᵢ⊗I₂)P₋,

with P± FT.93(2)'s ray projectors of the orientation doublet [Def-H.33]. Exact:
[Σ⁺ᵢ,Σ⁺ⱼ] = −2iεᵢⱼₖΣ⁺ₖ, [Σ⁻ᵢ,Σ⁻ⱼ] = +2iεᵢⱼₖΣ⁻ₖ, [Σ⁺,Σ⁻] = 0 *because P₊P₋ = 0*.
**The two su(2) copies of the Pauli tensor live on the two RAYS of the doublet** — each
traversal orientation carries its own full internal su(2) of Pauli curvature, and the rays
never mix under it (the born term is grade-even), while M̂ flips them [AT.48(4)]. The two
moment channels are exact grade-conjugates.

## III. The contraction: decomposition mechanized, no third channel, the Hodge row (machine §C)

For every antisymmetric F (verified on the 6 basis elements, 3 fixed integer trials, and
additivity against the basis expansion — exact 4×4 identities over ℚ):

    σ^{μν}F_{μν} = −4·B_c·W_c^ext + 2·E_a·(σ_a⊗κ̂),     B_c := ½ε_{cab}F_{ab},   E_a := F_{a4}.

**No third channel:** the Pauli-basis decomposition (CT1.1 trace orthogonality) of the
contraction has ZERO components in the other 9 Pauli directions, in I₄, **and in I⊗κ̂**.
Adversarial witnesses keep it non-vacuous: γ_{F₀} itself carries (0,3)-component 1, and a
halved magnetic coefficient breaks the identity.

**The grade separation:** Tr(σ^{μν}F_{μν}·γ_{F₀}) = 0 for every F — M̂ = −q(I⊗κ̂) is *never*
a bivector contraction; it is the electric channel's grade-4 partner, formable only by the
SCALAR boundary read (a native index-carrying EM read is absent — AT-O29/AT.48(3) stands,
and now with its exact grade reason).

**The Hodge row (new):** σ^{μν}γ_{F₀} = −(*σ)^{μν}, hence

    (σ^{μν}F_{μν}) ∘ M̂ = q·σ^{μν}(*F)_{μν},      (*F)_{μν} := ½ε_{μνρσ}F_{ρσ}.

**The boundary moment operator IS q × the Hodge rotation of the Pauli tensor** — it exchanges
the electric and magnetic channels. Dictionary partner of the smooth EM duality rotation,
NOT its equal [BM.134(5) discipline]. The charge read is what rotates E↔B inside the Pauli
algebra; AT.48(5i)'s splitting 2|q| is the spectrum of that rotation's generator.

**The grading table:** all six bivectors commute with γ_{F₀} (grade-even); the magnetic channel
is χ̂-EVEN (acts within each ray), the electric channel is χ̂-ODD (flips the doublet like M̂
[AT.48(4)]). The smooth magnetic-even/electric-odd pattern is reproduced exactly by the
ledger's own involutions.

**Native feed (assembly row):** the magnetic side needs an index — the only native index-i
carrier is the shift wᵢ [AT.2(4); FT.157(1)] → AT.6's functional, derived up to ϰβ [AT.34].
The electric side's vector datum has no native feed [AT-O29] → it collapses to the scalar
boundary channel M̂ [AT.48(2a)]. **AT.48(3)'s decomposition theorem is now exact AND complete:
two channels, no third, each with its native supply named.**

## IV. The Weitzenböck identity: the Pauli term BORN, slot-free (machine §D)

On 𝒟 = Σₐ γₐ⊗Tₐ over ℋ_ext⊗ℂ²_T [AT.47(8)'s skeleton], with the four transports Tₐ left as
**independent indeterminates** (16 commuting variables; exact multivariate polynomial
arithmetic over ℚ(i); 416 monomials generated and cancelled):

    𝒟² = I⊗(Σₐ Tₐ²)  −  (i/2)·σ^{μν}⊗𝓕_{μν},        𝓕_{ab} := [Tₐ, T_b]  (transport curvature).

The square of the Dirac skeleton = the transport Laplacian + **the Pauli term at tree
coefficient EXACTLY 1** — for EVERY choice of the undeclared slots. γₐγ_b = −iσ^{ab}
re-certified entrywise. Chirality rides along symbolically: {𝒟, γ_{F₀}⊗I} = 0 (chiral-odd,
AT.47(8) re-certified with general transports), [𝒟², γ_{F₀}⊗I] = 0 (the square — Laplacian +
Pauli — is grade-even: **the Pauli term is born inside the ray algebra, never across rays**).

The born term re-splits by the channel identities (symbolic, fully general):

    −(i/2)σ^{μν}⊗𝓕_{μν} = 2i·W_c^ext⊗𝓑_c − i·(σₐ⊗κ̂)⊗𝓔ₐ,
    𝓑_c := ½ε_{cab}[Tₐ,T_b],   𝓔ₐ := [Tₐ,T₄]

— curvature feeds exactly the two channels; no third channel can be born (§III's census).

**The coefficient is a theorem, not a convention:** all four transports equal (one generic T)
⟹ every 𝓕_{ab} = [T,T] = 0 and 𝒟² = (Σγₐ)²⊗T² exactly — Pauli vanishes while the skeleton
stays nonzero. The coefficient 1 is forced by the Clifford relations alone, with no
normalization choice left. **This is the algebraic root of AT.48(5i)'s FLAGGED tree parallel:
the coefficient is DERIVED; its identification with any measured g stays QUARANTINED**
[P5; Def-BM.3(7); EM.25(7)'s e₀ unissued]. The flag is upgraded from "parallel observed" to
"parallel with its exact algebraic seat named" — still ¬identified.

## V. The transport curvature census on the two constructed families (machine §E)

**(i) The drag connection is FIBER-ABELIAN.** T(Θ) = diag(i^Θ, i^{−Θ}) — AT.46(5)'s D̂_drag =
AT.47(7)'s exp(i(π/2)Θκ̂) — **IS the ẑ-axis member of the EW.32 family**: T(Θ) = U(πΘ/2, ẑ),
verified entrywise on 9 integer windings (odd and even). All drag transports commute (81
pairs) ⟹ 𝓕 ≡ 0 ⟹ **the drag connection NEVER births a Pauli term**; its whole contribution
sits in ΣTₐ² — diagonal fourth-root phases, the winding/statistics side [AT.46(6)].
*Frame-dragging changes how a polygon exchanges, not what moment it couples* — the two AT.46
effects stay separated at the operator layer, now as a theorem of the square.

**(ii) The EW.32 curvature, closed form.** [Uₐ,U_b] = −2i·sinφₐ·sinφ_b·((n̂ₐ×n̂_b)·σ⃗) —
exact matrix identities over ℚ(i), censured over **576 combinations** (8 phase pairs including
(3/5,4/5), (5/13,12/13) and the quarter turns; 3×3 axis pairs). Vanishing iff the axes align
or either phase is a half-turn.

**(iii) The fourth-root lattice census.** φ ∈ (π/2)ℤ × 3 axes = 12 transports; of the 66
pairs, **exactly 12 carry nonzero curvature**, every value = ±2iσₖ — **Gaussian integers**,
zero criterion exact. The curvature-born Pauli read is fourth-root quantized at the operator
layer: **NO CONTINUOUS LOCUS** — the connection-side confirmation of AT.54(6)'s measure-side
no-go; the eighth root never appears [Def-BM.16(5); AT.48(5iii)].

**(iv) Two explicit ℂ⁸ witnesses** (integer entries, direct 8×8 squaring vs the identity):
- T = (iσ₁, iσ₂, I, I): ΣTₐ² = 0 and 𝒟² = the PURE born term 2(σ₃⊗I₂)⊗σ₃ — magnetic channel
  alone, curvature [T₁,T₂] = −2iσ₃;
- T = (iσ₁, iσ₂, I, iσ₃): 𝒟² = −2I₈ + 2(σ₃⊗I₂)⊗σ₃ + 2(σ₁⊗κ̂)⊗σ₂ − 2(σ₂⊗κ̂)⊗σ₁ — BOTH
  channels live, the electric one switched on by [Tₐ,T₄]; the born term is γ_{F₀}-even
  (ray-wise) with Gaussian-integer entries throughout.

## VI. The structural F₁/F₂ dictionary (machine §F; assembly)

Seats derived; **values stay behind (M1′)–(M3′)** [AT.54(6)] — no read rule, no ε_q value, no
chart scale, so no number is converted and nothing is compared [P5]:

| smooth seat | ledger seat | status |
|---|---|---|
| F₁-type (charge/vertex) | the BOUNDARY channel: q read, flicker-immune [Def-BM.5(1); AT.48(5ii)], Ward-protected δ=0 [AT.53(3)], splitting 2\|q\| unrenormalized [AT.54(4)] | constructed |
| F₂-type (anomalous) | the MEASURE dressing: ⟨ℵ⟩ excess rationals (1/6 at n=2, 3/7 at n=3 at ε_q=⅛ witnesses) [AT.54(1)]; residues/contacts redistribute intensity, positions unmoved (the Lamb analog) [AT.54(3)] | constructed (measure-side) |
| σ^{μν}F_{μν} operator layer | the CURVATURE-BORN gauge channel (§IV/§V): Gaussian-integer valued, slot-dependent in EVALUATION only | constructed (algebra); evaluation behind AT-O28's slots + the P4 profile |
| tree g=2 | the coefficient-1 theorem of §IV | derived; identification QUARANTINED [P5] |

Machine rows: the Σ^± su(2) copies are supported on single rays (Σ⁺P₋ = 0, Σ⁻P₊ = 0) while
M̂ flips them — the born (ray-wise, grade-even) term and the boundary (ray-flipping, χ̂-odd)
term are exact grade-conjugates.

**Bars:** BM.125(4)'s three grounds re-passed on the new objects (σ^{μν}, 𝓕, 𝓑, 𝓔, Σ^±):
operator-valued / ¬a mass product / all symbols 𝔮⁰ (structure constants Gaussian integers).
BM.126(1): the crossing-weight alphabet remains {ε_q} alone — the transports are P4-class
PROFILE data (marked [AT.47(9)(iii)]), never reweightings. BM.88(1)'s no-loops, EM.25(7)'s
unissued e, FT.55(1), FT.93(3),(4), BM.134(5) (the chart-side F_{μν} of CT1.19/CT1.22 is a
dictionary partner only), AT-O29 (the vector no-go — now with its grade reason): all
untouched. a_e, a_μ, a_μ/a_e, Lamb: quarantined scoring targets, ¬inputs, ¬compared.

## VII. Error profile this session (the record's own lesson, honored)

- **A double sign-flip bug in σ^{μν}** (the antisymmetry branch applied on top of an already
  order-antisymmetric commutator) made the contraction silently vanish — and C2/C3's early
  runs "passed" on the zero matrix. **C1's adversarial design caught it** (the halved-
  coefficient and γ_{F₀}-component witnesses cannot pass on a zero contraction). Lesson
  re-earned: every census needs a witness that could only pass on the *right nonzero* value;
  a zero matrix satisfies every absence claim.
- The bridge identity's ε-pair filter was inverted on first pass (`a in (b,c)` instead of the
  ε-kills-it automatic); caught by B3 failing loudly.
- Python `sum()` on tuple-typed PG entries CONCATENATES — explicit `pgadd` accumulation is
  mandatory in the symbolic layer. Caught by D1's unpack error.
- The Gaussian-integer test initially divided by 2i and demanded real results — but ±2iσ₂ has
  *real* entries (σ₂ carries the i). Correct test: entries/2 ∈ ℤ[i]. Caught by E3 on the four
  x–z axis pairs.

## VIII. Check ledger

`era2/level5_atomic/checks/pauli_term.py` — **23/23 EXACT**, no floating point:

- §A gates: A1 frame + relocation; A2 triple + M̂; A3 exclusion ranks (∧² = 1, ∧³ = 0)
- §B census: B1 signed Pauli products (6 directions, species 3/2/1); B2 channel identities;
  B3 pseudoscalar bridge; B4 Lie closure (Gaussian-integer constants); B5 ray-wise so(4)
  split; B6 the 8-dimensional generated algebra (64 products close, real rank 8)
- §C contraction: C1 the decomposition identity (6 basis + 3 integer + 3 additivity);
  C2 no-third-channel census + adversarial witnesses; C3 grade separation + Hodge row +
  the M̂-duality rotation (6+6+6 rows); C4 the χ̂/γ_{F₀} grading table (16 identities)
- §D Weitzenböck: D1 the symbolic identity (64 zero polynomials, 416 monomials);
  D2 chirality rows; D3 born-term channel re-split; D4 the coefficient-is-a-theorem witness
- §E transports: E1 drag fiber-abelian (81 pairs + the EW.32 unification); E2 the closed
  commutator form (576 identities); E3 the lattice census (66 pairs, 12 live, Gaussian
  integers, iff criterion); E4 the two ℂ⁸ witnesses
- §F: F1 the ray supports + the dictionary machine rows; F2 the BM.125(4)/BM.126(1) census

Suite after this session: **34 checkers, 610 exact markers, 0 failures, exit 0**; format gate:
**12 Part 5 documents PASS** (AT.56–AT.58 consolidated in `tiers/Part5_Atomic_era_TierAT10.md`).

## IX. Adjudication and the open ledger

- **AT.48(3)'s decomposition theorem: MECHANIZED** (AT.56(4),(5),(8)) — upgraded from
  stated/adjudicated to exact identities + census + native-feed rows.
- **frame_section's residue (iv): SUPERSEDED IN SCOPE** — what needed "(i)–(iii) AND the
  global operator" was the EVALUATION, never the algebra.
- **AT-O28: ADVANCED, NOT CLOSED** — the slot-free algebraic core is constructed (skeleton +
  square + born-term anatomy + curvature census); the GLOBAL operator on the emergent
  geometry still needs the two marked slots [AT.47(5); Def-H.37(2)/Open Gaps 19] and the P4
  transport profile (ℓ_c, c).
- **NEW OPEN ROW AT-O31**: the fine-structure-type read of the hydrogen connector — the seats
  are now identified (the ray-wise Σ^± su(2) for the spin-orbit-type content, the Hodge
  rotation for the channel exchange, the measure rationals of AT.54 for the intensity
  redistribution); blocked by (M1′)–(M3′) [AT.54(6)] and the AT-O28 slots. Blocking nothing.
- Declarations issued: **none**. Marked rows stay marked. Quarantine untouched.

> *The corpus rewards: read the whole rather than the era; treat every "absent" as level-local;
> let exact arithmetic, not plausibility, decide. — AT.39 Phys*
