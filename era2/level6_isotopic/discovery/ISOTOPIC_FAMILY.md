# ISOTOPIC_FAMILY — session 10 discovery record (Level 6 / Era 2, the Isotopic era)

> **Directive (Architect):** *"Construct the 1p-kn Isotopic Family and the Contraction Grammar
> Phase Transitions… at k=3 (1p3n, which has N=4 colour attachments) the screen and the mask
> will close something… for N ≥ 4 the δ-sealings enter the ensemble (g_δ(N) > 0), breaking the
> pure ε-protection of the N=3 baryon."*
>
> **Result: the family is constructed as support classes, the transition is located exactly — and
> it is not where the directive put it.** `isotopic_family.py` **8/8 exact**; candidate tags
> IT.6–IT.8 (Tier IT.2). The grammar transition g_δ: 0→3 at N=4 is frozen [BM.31(2)] and
> re-derived triple-certified; but a nucleon is a **3-attachment** ε-triple [BM.17(1)], so the
> family lives at N = 3(k+1) and its **first δ admission is the DEUTERON (N=6, the frozen
> 3/5–2/5 mix)**; at 1p3n (N=12) δ **dominates** (387/427) on the E_int=24 floor. Capacity
> never bites (n=3 saturated-admissible at every k); the (P1)–(P3) closure fires uniformly from
> k=1. Lepton saturation flagged: the δ-mixing cannot touch the connector boundary (telescoping)
> nor the ladder positions (grammar-blind alphabets) — it multiplies SECTORS. One new open row:
> **IT-O4**, the nucleon–nucleon connector species. Declarations: none. P5 quarantine untouched;
> no isotope identified [Def-BM.3(7)].

---

## I. The premise audit (three corrections, one confirmation)

| directive premise | the canon | disposition |
|---|---|---|
| "1p3n has N=4 colour attachments" | a nucleon = ε-sealed 3-juncture, THREE attachments sealed inside as one ε-triple [BM.17(1); Census FT.35(5); D3.9]; fusion/sharing ¬constructed | **CORRECTED: N = 3(k+1); 1p3n → N=12.** The N=4 support exists in the grammar (g=3, all δ — the double-mesonic "tetraquark-type" support, quoted) but is ¬a family member (N ≢ 0 mod 3) and ¬a single junction (slots at n=3 [CT3.11(1)]; n=4 inadmissible, 2⁵=32>16 [CT0.5/6]) |
| "δ enters the ensemble at N=4 → in the family at k=3" | g_δ: 0→3 at N=4 **is frozen** [BM.31(2): "the protection is unique to N=3"] | **CONFIRMED at the grammar; RELOCATED in the family:** first δ admission = deuteron (N=6: 15/25 = 3/5 δ-containing vs 10/25 = 2/5 pure-ε — BM.31(2)'s frozen mix re-derived); at k=3 (N=12): δ-dominant 148995/164395 = 387/427 |
| "the screen and the mask will close something at k=3" | capacity: every junction n=3, D_tick(3)=16=C_cap **exactly saturated, admissible** — never trips at any k; D⁻ lock needs rung ≥4 ≡ inadmissible [AT.50(3),(4),(5)]; (P1)–(P3)/void closure [AT.29; BM.143(1)] applies **uniformly from k=1** | **ADJUDICATED:** what closes at N=4 is the ε-PROTECTION (grammar), ¬capacity; the information closure is not special to k=3. What IS special at k=3, exactly: the disjoint E_int=24 **lands on the computed-cell floor** {2,6,12,24,60} [BM.17(4); Def-BM.14(6) order-isomorphism — an order, ¬a number] and the δ share first exceeds 9/10 |
| the cited g_δ/g_ε values | (1,0,3,10,15,105) and (0,1,0,0,10,0) for N=2..7 [Def-BM.9(3)] | **CONFIRMED**, triple-certified |

Also honored on the record: the Architect's standing flag — *"IT.4 will soon get an exception
when we calculate multi-(p,n,e) systems"* — this tier is the (p,n)-half of that calculus; the
IT.4(4)/(6) exception is recorded as an **expectation** at IT.8(3), to be derived at its own
locus when the electron-saturated members are built (IT-O2), ¬pre-empted.

## II. The grammar engine, triple-certified (machine §A)

g(N) = #(partitions of N attachments into blocks of size 2 (δ) and 3 (ε)) [Def-BM.9(3);
CT3.17a(2); FT.41(b)] computed THREE ways, agreeing entrywise:

1. **exhaustive enumeration** (N ≤ 8, with the full (a,b) block breakdown);
2. **the recurrence** g(N) = (N−1)·g(N−2) + C(N−1,2)·g(N−3) — element 1 is paired (N−1 choices)
   or tripled (C(N−1,2) choices);
3. **the closed form** g(N) = Σ_{2a+3b=N} N!/(a!·2^a·b!·6^b) with term-by-term (a,b) match.

Frozen rows reproduced exactly: g = (1,1,3,10,25,105) for N=2..7; g_δ = (1,**0**,3,10,15,105);
g_ε = (0,1,0,0,10,0); g_δ+g_ε = g; g_ε(N)≠0 ⟺ 3|N (verified to N=18); **g(1) = 0** (the lone
attachment is never sealed [CT3.17a]). Extended exactly: g(8)=385, g(9)=1540, g(10)=7245,
g(11)=32725, **g(12)=164395 = 10395 (6δ) + 138600 (3δ+2ε) + 15400 (4ε)**.

## III. The family census (machine §B)

| k | "name" (quoted) | N | g(N) | g_ε | g_δ | δ share | statistics sectors (4ℤ vs 2ℤ-only) |
|---|---|---|---|---|---|---|---|
| 0 | protium nucleus | 3 | 1 | 1 | 0 | 0 | 1 vs 0 — protected, unique |
| 1 | deuterium nucleus | 6 | 25 | 10 | 15 | **3/5** | 10 vs 15 — first mixing |
| 2 | tritium nucleus | 9 | 1540 | 280 | 1260 | 9/11 | 280 vs 1260 |
| 3 | hydrogen-4 nucleus | 12 | 164395 | 15400 | 148995 | **387/427** | 15400 vs 148995 |
| 4 | hydrogen-5 nucleus | 15 | (computed) | | | increasing | |
| 5 | hydrogen-6 nucleus | 18 | (computed) | | | increasing | |

- The δ share is **strictly increasing** in k; the pure-ε sector **never vanishes**
  (g_ε(3m) > 0 for every member) — the baryon's seal is a sector, never a casualty.
- Statistics composition [BM.31(4); Census FT.49(3); FT.22; BM.129]: pure-ε groupings carry the
  baryon-type Θ_int ∈ 4ℤ; **every δ-containing grouping admits only the 2ℤ class**; 4ℤ ⊊ 2ℤ
  (Θ=2 witness: meson-admissible, baryon-excluded — the partial separator). From the deuteron
  on, the family's seal-ensemble carries **both statistics classes as grouping sectors**.
- Attachment counts are BOUNDARY DATA [Def-BM.9(4)] — each N is its own support class; no clause
  sums over sealings of a fixed support as alternatives [Def-BM.9(5)]; the grammar decides which
  sealings a support ADMITS. The ensemble sector decomposition (BM.31(6)'s disjoint-union
  pattern) is the correct reading, and its weights are IT-O2's calculus.

## IV. Prices, floors, charge, capacity (machine §§D–F)

- **E_int, exactly** [BM.17(1): 6 = 2+2+2; Census FT.35(2); AT.40(3): E_int = |R|, exactly
  additive]: DISJOINT reading 6(k+1) = (6,12,18,24,30,36) — floors {2,6,12,24,60} hit at
  **k = 0, 1, 3** (the 1p3n member lands exactly on 24 — the Def-BM.14(6) order-isomorphism
  locus 12/24/60, quoted discipline); TREE reading with k bidirectional Σ₁₂-species connectors
  (2 edges each): 8k+6 = (6,14,22,30,38,46), off-floor except k=0. **The connector between
  nucleons has no frozen species** — count/winding/fusion unconstructed → **IT-O4** (the record
  refuses to guess; FT.34(3)'s k(Γ)=k₁+k₂+d₁₂ is the skeleton, BM.2(2)/(R10) the pattern).
- Per-member derived rows (symbolic, exact): G/(2π ln2) = E², k_crit/ln2 = E²/2, r_s = 𝔥E/2,
  Δx_B = 𝔥/(E ln2), and the **E-independent product Δx_B·r_s = 𝔥²/(2 ln2)** [BM.17(3)]; the
  shell is non-empty at every member on the frozen ln16>2 certificate [BM.148(4); AT.35(2)].
- **Charge:** Q_total = +1 for every member (proton class +1 [AT.41(2)], neutrons 0 [BM.17(2)],
  connector interiors telescope [EM.9b]). The sign census convolves **binomially**:
  W₃(Q) = C(6,Q+3) = (1,6,15,20,15,6,1) (Σ=64=4³) and the (k+1)-fold convolution =
  C(6(k+1), Q+3(k+1)) — **Vandermonde verified entrywise to k=4**. Charge classes overlap the
  mesonic at Q∈{0,+1}; only |Q|=3 baryon-exclusive per nucleon [BM.31(3)].
- **Capacity [machine F1]:** D_tick(n)=2^{n+1} ≤ 16 = C_cap census n=0..8: n=3 → 16 **exactly
  saturated, admissible**; n=4 → 32 inadmissible [AT.50(3)]. Colour slots at n=3 only
  [CT3.11(1); D3.1] ⟹ every family junction is saturated-admissible; **no member at any k trips
  capacity, the rung ladder, or the D⁻ lock**; N≥4 supports spread over junctions.
- **What closes:** (P1) visibility bound, (P2) mask, (P3) **void closure** [BM.143(1)] —
  uniformly from k=1 (first at the deuteron); accessible content = (Q=+1, Θ-class, S,
  N=3(k+1), E_int-reading, rung 3) exactly [AT.32(1)].

## V. Lepton saturation — flagged (machine §G)

- Coupling: the ONE global Def-H.32 sum [AT.42(2)]; open connector; boundary read Q_total=+1 —
  **invariant across every grouping** (telescoping): **the δ-mixing cannot alter the connector's
  boundary condition.**
- The lepton price w_c = 1/√(4ε_q(1−4ε_q)) ≥ 2 [AT.44(4)] and positions W_d = 1/(d²x₊x₋)
  [AT.44(5)] carry the flicker alphabet **alone** — symbol census disjoint from the grammar's:
  **GRAMMAR-BLIND; positions never move** [AT.54(3)].
- What the mixing changes: the nuclear-side ensemble splits into grouping sectors (BM.31(6)
  pattern) with multiplicities g(N), the (−1)^ℵ dressing [Def-H.32(2)], and the Θ-class
  composition — **intensities and statistics composition, never positions**.
- **Isotopy, ledger-natively: SAME boundary charge, DIFFERENT grammar multiplicities.** Chemical
  identification quarantined [P5; Def-BM.3(7)].

## VI. Check ledger

`era2/level6_isotopic/checks/isotopic_family.py` — **8/8 EXACT**, no floating point:
A1 (grammar engine triple-certified + frozen rows), B1 (family census + monotone share +
3/5–2/5 + the N=12 breakdown), B2 (statistics composition), C1 (the N=4 support: 3 perfect
matchings, mod-3 exclusion, the slot/capacity rows), D1 (E_int both readings, floors, symbolic
per-member rows, the E-independent product), E1 (Q_total, W₃, Vandermonde to k=4, Θ classes),
F1 (capacity census n=0..8, D⁻, the (P1)–(P3) rows), G1 (lepton symbol census + isotopy row).
Level runner after this tier: **3 checkers, 33 markers**; gate: **2 Part 6 documents**.

Session-10 error notes (added to MEMORY §7): the brute-force range must not exceed the
enumerated table (KeyError:9 caught on first run); dict-vs-list type discipline in the
convolution helper (AttributeError caught on second run) — both caught by the machine before
any tier text was written, per the witness-first discipline.

## VII. Adjudication

- **The family: CONSTRUCTED as support classes** (grammar sectors, prices, charge, phases,
  capacity) — IT.6/IT.7; **no species identified, no mass values, no measured isotope datum**.
- **The phase transition: LOCATED exactly** — grammar at N=4 (frozen + re-derived), family at
  N=6 (deuteron), dominance at N=12 (387/427), floor landing at k=3 (E_int=24).
- **The directive's "screen and mask" prediction: adjudicated** — ε-protection closes at N=4;
  capacity never closes; (P1)–(P3) closes from k=1; k=3's exact specials named.
- **NEW OPEN ROW IT-O4** (the nucleon–nucleon connector species: count, winding d, fusion) —
  the tree E_int and composite Θ_int stay parametric until it is constructed; IT-O2 absorbs the
  ensemble weights; the Architect's IT.4-exception expectation recorded at IT.8(3).
- Declarations issued: none. §Cal-IT empty. Level-5 closed record cited, never edited [AT.63(2)].

> *The corpus rewards: read the whole rather than the era; treat every "absent" as level-local;
> let exact arithmetic, not plausibility, decide. — AT.39 Phys*
