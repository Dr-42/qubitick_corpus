# PROBE_CONSOLIDATION.md — the session-13l working record (Tier IT.16 candidate, IT.49–IT.54)

**Directive (Architect, session 13l).** *"Consolidate, Re-Verify, and Merge the Mass-Reads Study into
the Main Corpus … a multi-session subgenerator study … seven interlocking documents … Re-verify every
machine claim … Resolve all name collisions … Separate derived / declared / barred … Determine the
correct tier placement … Do not force a declaration. Do not import a measured value [P5]. Do not add a
new dimensionful scale [P1]."* Plus the Architect's note: *"subgenerator doesn't know that imaginator
hallucinates … clean the documents up with what holds up to corpus discipline."*

**Machine.** `checks/probe_consolidation.py` → **33/33 EXACT**, no floating point, no measured value
(Fraction polynomial rings with exact quotient reductions Q[t₂]/(t₂²−2), Q[ct,st,t₂,t₃]/(ct²+st²−1,
t₂²−2, t₃²−3), Q[x,a₀,z_r,z_i,j]/(j²+1), Q[γ], Q[s]/(s²−Δ); jet-derivation algebra; Faddeev–LeVerrier;
Gauss(i) 4×4 elimination; exhaustive enumeration; rational π-certificates 333/106 < π < 355/113).

---

## 0. What arrived, and what the directive's inventory promised

The directive lists eight source documents; **four were attached**: `CONSOLIDATED.md` (the master
consolidation, Parts I–XII + appendices), `CONTINUUM.md` (the study's self-continuity map),
`photon_phase_jump_audit.md` (PJ.1–PJ.15), `radar_sync_audit.md` (RS.1–RS.10). The four working files
CONSOLIDATED.md itself summarizes (`mass_reads_dimensional_analysis.md` MR.1–MR.18 + amendments,
`phase_math_by_hand.md`, `sixteen_basis_metric_force_check.md`, `gods_gifts_and_the_saturated_node.md`,
`reflection_cpt_rung0_calibration.md`) were NOT delivered — but CONSOLIDATED.md carries their results,
formulas, citations and caveats, and declares itself "one file, self-contained". The consolidation
therefore proceeds from CONSOLIDATED + the two audits, with the amendment chain as recorded in
CONSOLIDATED Part X (17 rows) and the audits' own correction registers (PJ: 6 rows; RS: 6 rows).
The study's five verification scripts (`verify_c3_provenance.py`, `verify_koide_and_binomial_shape.py`,
`verify_phase_parameterized_matrix.py`, `verify_phase_jump_audit.py`, `verify_radar_sync_audit.py`)
were NOT delivered ⟹ **every machine claim was re-derived from scratch** in
`probe_consolidation.py` (house rule: no claim rides on an undelivered certificate).

Two directive references map onto this repo's reality (premise-mapping, recorded):
"CONTINUUM.md project map" is the study's own continuity file — its corpus analogue is the level
README + MEMORY discipline; "`checks/run_all.py`" maps to `run_all_level6.py` (gate first). The study
ran against a READ-ONLY clone under its own standing rule "do not commit to the repo" — this tier is
the merge act the Architect now directs, executed under the house pattern (checker → discovery →
tier → README → commit → PR).

## 1. The citation audit (the hallucination screen)

- **Tag sweep** (the level gate's exact registry logic over all four documents): CONSOLIDATED 167
  distinct tokens / 0 unattested; CONTINUUM 125 / 0; photon audit 124 / **1** (`CT0.20` in PJ.12's
  Req — the document's own bracket flags it "[as CT3.20]": a citation slip, corrected on the record);
  radar audit 104 / 0. **~450 tokens, one unattested, self-flagged.**
- **Clause-level checks (~65)**: all pass. Verified verbatim, among others: BM.102(4) ("converts no
  dimension — the dimensionless exchange rate between the bit currency and the angle currency");
  FT.131(3) ("the only derived clock is the ledger tick … no materialization coupling"); Def-H.41/42's
  arena bars ("no inner product, no dynamics, no state, no Hamiltonian"); FT.142 Rmk ("counting
  spaces … applies verbatim"); C10 (register cost |X|, "Shannon content … ≠ register cost"), C11 (the
  node lifecycle wait→in→tick→out→wait), C13 (𝔬=0, η=(−,+,+,+), "¬an axiom"); BM.102(2)'s exponent
  census; A2 C(p,q)=1𝔮; A3's unique odd slot; BM.28(5)'s unique CPT-fixed triple (0,0,0); FT.108(5)'s
  propagator; FT.119(2) 3δ_q=δ_ℓ; FT.119(7)'s "computed, none adopted" 2/81 table; FT.143(5)'s
  "shared seal numerator is the only cross-channel identity"; FT.143(6)'s "¬a selection principle";
  BM.80(4),(5)'s γ-constants and cubic rows; FT.158(1),(2),(5); BM.8(2)'s γ(8−γ)/16; BM.52(3)'s
  2|q| splitting census; AT.44(1),(2)'s return-word rows; IT.32(5)'s ideal-observer row (and the
  `calibration_anchor.py` "absolute relativity (Step 2)" machine-record string PJ.9(1) cites —
  present).
- **The canon-typo claim (corrections register #14) is CONFIRMED**: FT.116(5) prints
  108(Im z³)² = 108(Im z)²(3(Re z)²−(Im z)²) with the second factor UNSQUARED; the exact identity is
  (Im z³)² = (Im z)²(3(Re z)²−(Im z)²)² (machine: both expansions vs the depressed-cubic discriminant
  −4p³−27q²; witness z=1+i: 432 = 432 ≠ 216). The zero locus — all the clause uses — is identical
  either way: **harmless**. Recorded probe-side; the frozen canon is NEVER edited [AT.63(2)]; an
  erratum row is queued for the Era-2-closure pipeline.
- **Untagged identifications stay untagged**: FT.116's Phys asserts the two C₃ routes meet ("reached
  from the opposite side…") — Phys prose, no numbered clause ⟹ carried as a reading, never a row;
  "the jump factor IS the C₃ order" likewise [FT.143(6): "a datum for deficit 3, ¬a selection
  principle"].

## 2. The reconciliation table (duplicates, contradictions, amendments)

| claim family | status after consolidation |
|---|---|
| MR.1–MR.9 matrix/tensor/derivatives | superseded-in-place by CONSOLIDATED Parts I–II with the register's 17 corrections; the matrix itself = the IT.37–39/IT.43–45 parametric class (declared, ¬derived — the study's own Part XI agrees) |
| MR.3's "ρ_B := m_B/V_eff ∈ 𝔮^{+2}" | **name collision RESOLVED**: that is the corpus's ρ (density) [BM.14(2),(4)]; the corpus's ρ_B is the bridge μ̂'²𝔥²/(ln2)² ∈ 𝔮⁰ [BM.69(2); BM.102(4); BM.83(4); declared A-BM.9, value ¬issued]. Convention: ρ_B always the bridge. The b-slot fork (density vs bridge) stays an open parametric read-choice, both branches carried [BM.30(5) pattern] |
| MR.10/MR.11 amendments (the (3)/(4) files) | absorbed: w_B/w_L/Δ_L claims "no corpus basis" (register #17); the 2 is exact arithmetic at the capacity three |
| "16 maps 1:1 onto the metric" | **amended** (register #9): X occupies 10 of 16; a generic metric is swap-even only on a 7-dim subspace; four prices on any identification |
| PJ.4's temporal phase reading | **overridden by RS §0** (the directive's clarification): the tick labels attach to emission/reception; the PJ verdicts otherwise stand |
| δ vs s_ℓ notation | unified: δ_ch = channel phase; s_ch = the exponent of μ_ch [P4; Cal-F] |
| CT0.20 citation slip | corrected → CT3.20 |
| FT.116(5) canon typo | confirmed, harmless, recorded (never edited) |

## 3. The re-verification (33/33)

Every exact-arithmetic claim of the study re-derived from scratch — the full map is the checker's
check ledger below. Highlights: the cubic ladder γ_ℓ = 2γ_q³−3γ_q (polynomial identity in
Q[t₂,g_q]/(t₂²−2)); the Koide layer phase-free at symbolic δ (Σr=3, Σr²=6, 𝒦=⅔; the tower r''=1−r;
the family-sum zeros; the Newton tower; the z-cubic); 𝒦(N)=2/N at N=3,4,6 exact (general N by the
root-sum argument, a math row); the circulant charpoly by six-permutation Leibniz expansion in
Q[x,a₀,z_r,z_i,j]/(j²+1) + the discriminant/typo certificate; the selection census (subgroup orders
(1,2,2,2,3,6); commutants 9/5/3/2 by orbit counting; Stab(ε)=A₃); the inner C₃ (𝒲³=3𝒲;
charpoly x⁴−3x²; U=E₀−½𝒲²−(i/2)𝒲=u⊗u; U³=E₀; the nine conjugations); the (S,T) sector table
(7,3,3,3 with W=(+,−), J=(−,+), K=(−,−) — register correction #6 enforced); the full commutation
table; **Lie⟨J_i,K_i⟩ = 15-dimensional with E₀ outside** (incremental Gauss(i) elimination);
the nilpotent calculus with the honest negative {A_i,B_j} ≠ δ_ij𝟙 (fermion-like, ¬Clifford);
ΣA_iB_i=Π_ℛ, ΣB_iA_i=3Π_𝒱, Σ[A_i,B_i]=Σ; the Casimirs; the branch-change bridge J_iΠ_ℛ=Π_𝒱J_i;
the order-4 inner reflection (J↦−K, K↦J, A↦iA, B↦−iB, R⁴=iE₀); the 10-of-16 occupancy with
X_{E₀}=½(𝒮−𝒯), X_Σ=⅙(𝒮+𝒯); the phase calculus (four corrected cells a'd/ad'/a''d/ad''; the
readout table; the (1,2n,n²) constrained flow n=1..6; det J_Φ=−a'd'(a²−d²); det H_𝒯=ad·a''d''−(a'd')²;
the eigenvalue-derivative certificate by implicit differentiation in Q[a,b,c,d,a′,s]/(s²−Δ)); the
order-3 triple annihilation (∂q∂ℓ∂ν(M⊗M)=0 on all 81 cells; M⊗³'s ade cell nonzero); the Lyapunov
identities ((1−γ/4)²+γ(8−γ)/16=1; (9/16)⁶=531441/16777216); the saturation census (¼ ∉
[0,ε_q]∪[1−ε_q,1] on witnesses incl. ε_q=¼−10⁻⁶; O(n)=(0,0,0,0,16,48,112); the lock biconditional);
the radar algebra (dτ± the exact roots of BM.34(2)'s null quadratic per leg sign; agreement ⟺
s·dx=0; T-conjugacy); the exhaustive 4ⁿ census vs C(2n,n+Q); the neighbour law (n+1)/n; the unique-2
quotient census; the ℘-ring certificates (3ln1280−4ln960=−ln405; Σ_B=(2,−1,0); 16<27).

## 4. Derived / declared / barred — the separation (the tier's verdict tables carry it in full)

**DERIVED (new rows, certified in `probe_consolidation.py`):** the general law 𝒦(N)=2/N; the
neighbour law R(n)=(n+1)/n and the quotient uniqueness at 3; the cubic ladder + the unique positive
preimage; z_ℓ=2z_q³ with the forced factor 2=B²; the Newton tower + z-cubic; the 3-adic ν-exclusion;
the circle algebra (commutator R_{4π/9}; conjugation R_{2π/9}; the πδ_ℓ rhyme flagged ¬cashed); the
su(4)-from-six generation; the nilpotent calculus + honest negative; the Casimirs; the branch-change
bridge; the order-4 reflection; CPT-triviality-on-16 assembly; the 10-of-16 occupancy + singlet
readouts; the four corrected cells + the full phase calculus; the order-3 annihilation facts; the
direction-blind Lyapunov row; the saturation incompatibility (a real jump cannot occur at ρ_∘); the
radar agreement conditional + return-word one-read consequence + the disjointness row; the O(n)
continuation's real zero z₀=3.

**DECLARED (named, ¬issued — the study's own Part XI + PJ.15 + RS.9, absorbed):** the array M and
its index space; 𝒮,𝒯 as readouts; g and its six coefficients g_i± (count→strength barred);
"uniform" := ρ_∘; the isotropy transport through the X↔X₍₊₎⊕X₍₋₎ dictionary; the channel-index-as-
spatial-index reading; the order-3 line choice; κ=𝔥⁴μ_ℓ as the det weight; D-PJ1–7 (tick order;
angle-state objects; mediation direction; event classification; the general-circle branch rule; a
rider reading-type; the standing IT-O1 package); D-RS1–6 (the pre/post-tick relational reading vs
C11's inverted lifecycle — conflict logged; "radar" as a definitional act; the tick–hop exchange
rate; the stationarity scope; a rider read-type; the standing IT-O1/IT-O3 package); the b-slot fork;
the two-C₃ identification; any Fourier/information reading of the capacity (¬Shannon [D0.9; C10]).

**BARRED (grounds restated):** count→strength couplings [BM.36(3); BM.61(8)(O1); BM.69(4)(iv);
FT.73(5)]; α_B [BM.61(8)]; Ansatz-B α [BM.59(7)]; a second dimensionful scale [P1]; a complex rung
[CT4.4a]; species identification [P5; Def-BM.3(7)]; amplitude=mass [FT.79(5)]; rung=scale [D0.8];
cross-currency sums/conversions as formed reads [BM.83; BM.140(5); IT.43(6)]; the dynamical radar /
photon-mediated phase jump as formed transit content — three grounds (O1, O2/deficit 1′, O4; O3
discharged) [IT.40–IT.42]; "perspectives" as ledger primitives [IT.44(6)].

## 5. Tier placement

Level 6 (the open level — Level 5 is closed, cited never edited). New **Tier IT.16, tags
IT.49–IT.54**: IT.49 the intake + citation audit + collision resolutions + the corrections register;
IT.50 the channel-angle layer (the new derived rows); IT.51 the operator layer on the CT1.2 basis;
IT.52 the tensor-square occupancy + the parametric calculus (the IT.37–39/IT.43–45 class extended);
IT.53 the saturated node, the Lyapunov layer, the radar; IT.54 the verdict tables, the declaration
register, the forks, the declaration census. Amendments are RECORDED, never overwritten (the merge
edits no canon row; the FT.116(5) observation is probe-side). IT-O3 gains a recorded candidate
semantics (the radar protocol) and stays OPEN; no new open row; no declaration forced.

## 6. Check ledger (`probe_consolidation.py`, 33/33)

| # | content |
|---|---|
| A1 | the angle ledger; 27:48:16; the 3-adic ν-exclusion (16≠9·3ᵏ); the γ-order via π>333/106 |
| A2 | the cubic ladder γ_ℓ=2γ_q³−3γ_q in Q[t₂,g_q]/(t₂²−2) |
| A3 | the Koide layer at symbolic δ: Σr=3, Σr²=6, e₂=3/2, 𝒦=⅔; ∏r=(γ−1)/2; the Newton tower; r''=1−r; the family-sum zeros |
| A4 | 𝒦(N)=2/N at N=3,4,6 (Σr=N, Σr²=2N each) |
| A5 | Newton's identities + the z-cubic 4z³−24z²+(21−12γ)z−(γ−1)², Σz=6 |
| A6 | the circle algebra: ÔC₃=θ/3+2π/9, C₃Ô=θ/3+2π/3, commutator R_{4π/9}, conjugation R_{2π/9} |
| A7 | z_ℓ=2z_q³: the factor 2 the unique positive solution of c²=4; 3·(2/27)=2/9 |
| B1 | the exhaustive 4ⁿ census = C(2n,n+Q) (n=1..4); W₃=(1,6,15,20,15,6,1); 20/15=4/3; m_q=(2,1,1) |
| B2 | (2+z+z⁻¹)ⁿ=(1+z)^{2n}/zⁿ coefficient-wise (n=1..6) |
| B3 | R(n)=(n+1)/n (n=1..12); both quotient functions hit 2 uniquely at k=3 |
| B4 | Σ_B=(2,−1,0) in ℘; 3ln1280−4ln960=−ln405≠0; the attenuation certificates; 16<27 |
| C1 | the circulant charpoly by Leibniz expansion in Q[x,a₀,z_r,z_i,j]/(j²+1); disc=108(Im z³)²=the squared expanded form; the UNSQUARED form refuted at z=1+i (432 vs 216) — the FT.116(5) typo certificate |
| C2 | the S₃ subgroup orders (1,2,2,2,3,6); commutants 9/5/3/2; Stab(ε)=A₃; spec(aI₃+bJ) two-level |
| C3 | 𝒲³=3𝒲; charpoly x⁴−3x²; U=E₀−½𝒲²−(i/2)𝒲=u⊗u; U³=E₀; the nine conjugation rows |
| D1 | the (S,T) sector table: E₀,Σ,Ê^{ij}=(+,+); W=(+,−); J=(−,+); K=(−,−); sectors (7,3,3,3) |
| D2 | the full commutation table ([J,J]=[K,K]=iεW; [J_i,K_j]=i(δΣ−E^{ij}); [Σ,J]=4iK; [Σ,K]=−4iJ; [W,·] rows; [E₀,·]=0) |
| D3 | Lie⟨J,K⟩ rank 15 with E₀ outside (rank 16 when added) |
| D4 | the nilpotent calculus; Tr(A_iB_j)=δ; ΣA_iB_i=Π_ℛ; ΣB_iA_i=3Π_𝒱; Σ[A,B]=Σ; {A_i,B_j}≠δ1 |
| D5 | ΣJ²=ΣK²=Π_ℛ+3Π_𝒱; ΣW²=2Π_ℛ; W_iΠ_𝒱=0 |
| D6 | SJ_iS=−J_i; J_iΠ_ℛ=Π_𝒱J_i; K_iΠ_ℛ=Π_𝒱K_i; ΣΠ_ℛ=Π_ℛ; ΣΠ_𝒱=−3Π_𝒱 |
| D7 | Ad(e^{iπΣ/8}): J↦−K, K↦J, W↦W, A↦iA, B↦−iB; Ad²=−id on the six; Ad⁴=id; the branch phases (⅛·4=½; −⅜·4≡½ mod 2) |
| D8 | X=M⊗M: the J/K coefficients vanish identically; the explicit 10-direction expansion on 3 witnesses; X_{E₀}=½(𝒮−𝒯), X_Σ=⅙(𝒮+𝒯) |
| E1 | the Leibniz forms of ∂qX, ∂ℓX, ∂q²X, ∂ℓ²X, ∂q∂ℓX entrywise; the four corrected cells nonzero |
| E2 | the readout derivative table (𝒮 no cross-curvature; 𝒯 only the cross term) |
| E3 | the constrained flow (1,2n,n²) for n=1..6; d²𝒮, d(det), d(tr) rows |
| E4 | det J_Φ=−a'd'(a²−d²); det H_𝒯=ad·a''d''−(a'd')² |
| E5 | the eigenvalue certificate: P(λ±)=0 and (2λ−tr)λ′=tr′λ−det′ in Q[a,b,c,d,a′,s]/(s²−Δ) |
| E6 | ∂q∂ℓ∂ν(M⊗M)=0 on all 81 cells; the ade cell of M⊗³; ∂q∂ℓ𝒯₃=−a'd'e |
| F1 | (1−γ/4)²+γ(8−γ)/16=1; zeros {0,8}; γ=1: (9/16,7/16); (9/16)⁶=531441/16777216 |
| F2 | ¼∉[0,ε]∪[1−ε,1] on witnesses; O(n)=(0,0,0,0,16,48,112); the lock biconditional; 6,16,17,25 |
| F3 | dτ± the exact null-quadratic roots per leg sign; (Σ)(N²−s²)=2GdxN; (Δ)(N²−s²)=2Gdxs; the half-distance and s=0 proper-length rows; T-conjugacy |
| F4 | Õ(3)=0; the slope 16ln2 symbolic; the complex ladder recorded, scoped out |
| G1 | bridge (deg 0, alphabet {μ̂'²,𝔥,ln2}) vs density (deg +2, alphabet {𝔥,ln2,E}): distinct monomials — the convention row |
