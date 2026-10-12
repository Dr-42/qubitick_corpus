# checks/ — machine verification suite for the four-era $\langle qu(b(i(t|t))ick)\rangle$ canon

Pure Python 3 standard library. **No dependencies, no floating point.**
All arithmetic is exact (`fractions.Fraction`, complex-over-`Fraction`,
truncated power series over `Fraction`, exact radical rings), so every PASS is
bit-exact equality.

## Run

```
python3 run_all.py                 # everything (80 checkers)
python3 verify_era_structure.py    # the era laws only
python3 verify_corpus_graph.py     # citation closure, acyclicity, index regeneration
python3 check_format.py            # document structure of the five canon files
```

Exit code `0` = all green. Suite state at delivery: **80/80**.

## The canon files

`Part1_Qubit_era.md`, `Part2_Bosonic_era.md`, `Part3_Fermion_era.md`,
`Part4_Baryomesonic_era.md`, `Census.md`; the ledger annex `HistLog.md`; the
externalized first editions `../H_archive/H01–H21` (separate historical-archive repository; where absent, `era_paths.ARCHIVE_PRESENT` gates the first-edition pins).

## Structural checkers

| File | Purpose |
| --- | --- |
| `verify_era_structure.py` | the laws of the era canon: ownership partition (FT.1–145 + Def-H.1–34 exactly once across Part 3 ∪ Census; the 25 Category-B cells only in Census; the adjudication tags FT.115/121/132/140 and the closure tier FT.146–152 only in HistLog), the interface layer (Def-H.35–43, FT.153–155 present with their constitutive/minimality clauses), declaration hygiene (zero P-H tokens, zero **Status.** lines, zero letter-series locators in the canon), HistLog integrity (22 disposition rows, registry entries, gap items 1–21, Q1–Q12, status ledger), era headers |
| `verify_corpus_graph.py` | tag registry (584 tags), Req-line citation graph (6800+ edges): citation closure, tag-level acyclicity (no whitelist), the era-chain law on Req edges (marked forward pointers exempt: `cf.`, corroboration, re-verification), corollary attribution (**Req (Cor)** → the corollary tag); regenerates `../index/{tags.json,graph.md,tier_index.md,dependency_tree.md}` |
| `check_format.py` | the five canon documents: `$$`/brace balance, citation closure against the corpus-wide registry, **Thm/Req/Pf/Phys** completeness of every theorem block, **Def.** presence in every definition block, single declaration of A1–A9, C1–C12, D0.1–D4.3, P1–P5 (Part 1); **display-delimiter hygiene** — no line holding a single `# checks/ — machine verification suite for the four-era Qubitick canon

Pure Python 3 standard library. **No dependencies, no floating point.**
All arithmetic is exact (`fractions.Fraction`, complex-over-`Fraction`,
truncated power series over `Fraction`, exact radical rings), so every PASS is
bit-exact equality.

## Run

```
python3 run_all.py                 # everything (80 checkers)
python3 verify_era_structure.py    # the era laws only
python3 verify_corpus_graph.py     # citation closure, acyclicity, index regeneration
python3 check_format.py            # document structure of the five canon files
```

Exit code `0` = all green. Suite state at delivery: **80/80**.

## The canon files

`Part1_Qubit_era.md`, `Part2_Bosonic_era.md`, `Part3_Fermion_era.md`,
`Part4_Baryomesonic_era.md`, `Census.md`; the ledger annex `HistLog.md`; the
externalized first editions `../H_archive/H01–H21` (separate historical-archive repository; where absent, `era_paths.ARCHIVE_PRESENT` gates the first-edition pins).

## Structural checkers

| File | Purpose |
| --- | --- |
| `verify_era_structure.py` | the laws of the era canon: ownership partition (FT.1–145 + Def-H.1–34 exactly once across Part 3 ∪ Census; the 25 Category-B cells only in Census; the adjudication tags FT.115/121/132/140 and the closure tier FT.146–152 only in HistLog), the interface layer (Def-H.35–43, FT.153–155 present with their constitutive/minimality clauses), declaration hygiene (zero P-H tokens, zero **Status.** lines, zero letter-series locators in the canon), HistLog integrity (22 disposition rows, registry entries, gap items 1–21, Q1–Q12, status ledger), era headers |
| `verify_corpus_graph.py` | tag registry (584 tags), Req-line citation graph (6800+ edges): citation closure, tag-level acyclicity (no whitelist), the era-chain law on Req edges (marked forward pointers exempt: `cf.`, corroboration, re-verification), corollary attribution (**Req (Cor)** → the corollary tag); regenerates `../index/{tags.json,graph.md,tier_index.md,dependency_tree.md}` |
| `check_format.py` | the five canon documents: `$$`/brace balance, citation closure against the corpus-wide registry, **Thm/Req/Pf/Phys** completeness of every theorem block, **Def.** presence in every definition block, single declaration of A1–A9, C1–C12, D0.1–D4.3, P1–P5 (Part 1);  (a `$` split in two), no line with an odd number of unescaped `# checks/ — machine verification suite for the four-era Qubitick canon

Pure Python 3 standard library. **No dependencies, no floating point.**
All arithmetic is exact (`fractions.Fraction`, complex-over-`Fraction`,
truncated power series over `Fraction`, exact radical rings), so every PASS is
bit-exact equality.

## Run

```
python3 run_all.py                 # everything (80 checkers)
python3 verify_era_structure.py    # the era laws only
python3 verify_corpus_graph.py     # citation closure, acyclicity, index regeneration
python3 check_format.py            # document structure of the five canon files
```

Exit code `0` = all green. Suite state at delivery: **80/80**.

## The canon files

`Part1_Qubit_era.md`, `Part2_Bosonic_era.md`, `Part3_Fermion_era.md`,
`Part4_Baryomesonic_era.md`, `Census.md`; the ledger annex `HistLog.md`; the
externalized first editions `../H_archive/H01–H21` (separate historical-archive repository; where absent, `era_paths.ARCHIVE_PRESENT` gates the first-edition pins).

## Structural checkers

| File | Purpose |
| --- | --- |
| `verify_era_structure.py` | the laws of the era canon: ownership partition (FT.1–145 + Def-H.1–34 exactly once across Part 3 ∪ Census; the 25 Category-B cells only in Census; the adjudication tags FT.115/121/132/140 and the closure tier FT.146–152 only in HistLog), the interface layer (Def-H.35–43, FT.153–155 present with their constitutive/minimality clauses), declaration hygiene (zero P-H tokens, zero **Status.** lines, zero letter-series locators in the canon), HistLog integrity (22 disposition rows, registry entries, gap items 1–21, Q1–Q12, status ledger), era headers |
| `verify_corpus_graph.py` | tag registry (584 tags), Req-line citation graph (6800+ edges): citation closure, tag-level acyclicity (no whitelist), the era-chain law on Req edges (marked forward pointers exempt: `cf.`, corroboration, re-verification), corollary attribution (**Req (Cor)** → the corollary tag); regenerates `../index/{tags.json,graph.md,tier_index.md,dependency_tree.md}` |
| `check_format.py` | the five canon documents: `$$`/brace balance, citation closure against the corpus-wide registry, **Thm/Req/Pf/Phys** completeness of every theorem block, **Def.** presence in every definition block, single declaration of A1–A9, C1–C12, D0.1–D4.3, P1–P5 (Part 1); , and no bare inline `$…# checks/ — machine verification suite for the four-era Qubitick canon

Pure Python 3 standard library. **No dependencies, no floating point.**
All arithmetic is exact (`fractions.Fraction`, complex-over-`Fraction`,
truncated power series over `Fraction`, exact radical rings), so every PASS is
bit-exact equality.

## Run

```
python3 run_all.py                 # everything (80 checkers)
python3 verify_era_structure.py    # the era laws only
python3 verify_corpus_graph.py     # citation closure, acyclicity, index regeneration
python3 check_format.py            # document structure of the five canon files
```

Exit code `0` = all green. Suite state at delivery: **80/80**.

## The canon files

`Part1_Qubit_era.md`, `Part2_Bosonic_era.md`, `Part3_Fermion_era.md`,
`Part4_Baryomesonic_era.md`, `Census.md`; the ledger annex `HistLog.md`; the
externalized first editions `../H_archive/H01–H21` (separate historical-archive repository; where absent, `era_paths.ARCHIVE_PRESENT` gates the first-edition pins).

## Structural checkers

| File | Purpose |
| --- | --- |
| `verify_era_structure.py` | the laws of the era canon: ownership partition (FT.1–145 + Def-H.1–34 exactly once across Part 3 ∪ Census; the 25 Category-B cells only in Census; the adjudication tags FT.115/121/132/140 and the closure tier FT.146–152 only in HistLog), the interface layer (Def-H.35–43, FT.153–155 present with their constitutive/minimality clauses), declaration hygiene (zero P-H tokens, zero **Status.** lines, zero letter-series locators in the canon), HistLog integrity (22 disposition rows, registry entries, gap items 1–21, Q1–Q12, status ledger), era headers |
| `verify_corpus_graph.py` | tag registry (584 tags), Req-line citation graph (6800+ edges): citation closure, tag-level acyclicity (no whitelist), the era-chain law on Req edges (marked forward pointers exempt: `cf.`, corroboration, re-verification), corollary attribution (**Req (Cor)** → the corollary tag); regenerates `../index/{tags.json,graph.md,tier_index.md,dependency_tree.md}` |
| `check_format.py` | the five canon documents: `$$`/brace balance, citation closure against the corpus-wide registry, **Thm/Req/Pf/Phys** completeness of every theorem block, **Def.** presence in every definition block, single declaration of A1–A9, C1–C12, D0.1–D4.3, P1–P5 (Part 1);  in math mode inside a display, which is what halts XeTeX with `! Display math should end with $` (the same `$…# checks/ — machine verification suite for the four-era Qubitick canon

Pure Python 3 standard library. **No dependencies, no floating point.**
All arithmetic is exact (`fractions.Fraction`, complex-over-`Fraction`,
truncated power series over `Fraction`, exact radical rings), so every PASS is
bit-exact equality.

## Run

```
python3 run_all.py                 # everything (80 checkers)
python3 verify_era_structure.py    # the era laws only
python3 verify_corpus_graph.py     # citation closure, acyclicity, index regeneration
python3 check_format.py            # document structure of the five canon files
```

Exit code `0` = all green. Suite state at delivery: **80/80**.

## The canon files

`Part1_Qubit_era.md`, `Part2_Bosonic_era.md`, `Part3_Fermion_era.md`,
`Part4_Baryomesonic_era.md`, `Census.md`; the ledger annex `HistLog.md`; the
externalized first editions `../H_archive/H01–H21` (separate historical-archive repository; where absent, `era_paths.ARCHIVE_PRESENT` gates the first-edition pins).

## Structural checkers

| File | Purpose |
| --- | --- |
| `verify_era_structure.py` | the laws of the era canon: ownership partition (FT.1–145 + Def-H.1–34 exactly once across Part 3 ∪ Census; the 25 Category-B cells only in Census; the adjudication tags FT.115/121/132/140 and the closure tier FT.146–152 only in HistLog), the interface layer (Def-H.35–43, FT.153–155 present with their constitutive/minimality clauses), declaration hygiene (zero P-H tokens, zero **Status.** lines, zero letter-series locators in the canon), HistLog integrity (22 disposition rows, registry entries, gap items 1–21, Q1–Q12, status ledger), era headers |
| `verify_corpus_graph.py` | tag registry (584 tags), Req-line citation graph (6800+ edges): citation closure, tag-level acyclicity (no whitelist), the era-chain law on Req edges (marked forward pointers exempt: `cf.`, corroboration, re-verification), corollary attribution (**Req (Cor)** → the corollary tag); regenerates `../index/{tags.json,graph.md,tier_index.md,dependency_tree.md}` |
| `check_format.py` | the five canon documents: `$$`/brace balance, citation closure against the corpus-wide registry, **Thm/Req/Pf/Phys** completeness of every theorem block, **Def.** presence in every definition block, single declaration of A1–A9, C1–C12, D0.1–D4.3, P1–P5 (Part 1);  inside `\text{}`/`\textbf{}`/`\emph{}` is legal and allowed); **row-break hygiene** — no `array` row break immediately followed by a `[` that is not a length, which LaTeX reads as optional vertical space and which halts XeTeX with `! Illegal unit of measure (pt inserted).` (the idiom is `\\{}[`; a genuine `\\[6pt]` is allowed) |

## Content checkers

`verify_B.py`–`verify_G.py`, `verify_merge_tier{A,B,C}.py`,
`verify_promotion_*.py`, `verify_F33_dynamic_phase.py`,
`verify_L_lyapunov.py`, `verify_L0_ledger_tilt.py`: the algebraic, geometric
and arithmetic identities of Parts 1–2 (operator algebra, jet calculus,
electroweak Gram forms, charge alphabets, colour arithmetic in
$\mathbb Q(\sqrt3,i)$, saturation arithmetic, the Lyapunov/tilt passes).

`verify_H_*.py` (the per-tier suite): the fermionic-layer content — floors,
ladders, Platonic/polygon cells, covers, flicker ensembles, pole spectra,
Clifford census, form factors, channels, carrier/parity, rung one, the 3+1
chiral asymmetry. Where these pin first-edition texts in `../H_archive/` (the
identity base) and the transplanted mathematics in Part 3 / Census — except
`verify_H_3p1_chiral_asymmetry.py` (Tier F.44), which pins the era-canon
texts directly: Tier F.44 is new canon content with no first edition.

`verify_H_full_scope_mass_splitting.py` (Tier BM.13 of Part 4, `BM.51`–`BM.56`):
the full-scope mass splitting — the Lyapunov contraction identity
$(1-\gamma/4)^2+\gamma(8-\gamma)/16=1$ in $\mathbb Q[\gamma]$, the iteration
$(9/16)^6=531441/16777216$ with its injectivity census, $\operatorname{spec}\Sigma=\{1,1,1,-3\}$
and both branch witnesses ($\mathfrak T(\delta\rho^2)=(\tfrac34,\tfrac1{12})$,
$V=8\Delta S_{\mathrm{pair}}$), the block dictionary $7+3+3+3=16$ and
$\dim\mathcal K_3=25$, the chiral splitting $2|q|\in\{0,2\}$ with the charge-blind
force trace, the seven charge-exponent-zero monomials and both lock identities, the
Mandelstam–Tamm witness saturating $\Delta t\,\Delta E=\tfrac12$ over $\mathbb Q(i)$,
the count binding zero $6-(2{+}2{+}2)=0$ and the four class-degenerate ensemble
bindings, the cross-multiplied ratio identity $m_n(4\pi+ce^2)=m_p\cdot4\pi$ with the
truncated geometric series $(1+x)(1-x+x^2-x^3)=1-x^4$, and the tier's hygiene and
standing-bar scans.

`verify_H_constituent_transport_splitting.py` (Tier BM.14 of Part 4, `Def-BM.13`,
`Def-BM.14`, `BM.57`–`BM.64`): the constituent transport splitting — §A the
continuation censuses ($\operatorname{Stab}_{S_3}(\varepsilon)=A_3$ of order 3 against
$S_1\times S_1$ of order 1, asymmetry 2), the Gram block, kernel, sum-of-squares and
charpoly over $\mathbb Q(i)\otimes\mathbb Q[g,g']$, the profile evaluation and orbit
value set in $\mathbb Q[g,g',c,s,r_3]/(c^2{+}s^2{-}1,r_3^2{-}3)$, and the trace law with
$1+\omega+\omega^2=0$ in $\mathbb Q[\omega]/(\omega^2{+}\omega{+}1)$; §B the metric
token census, the charge-exponent-zero monomials and the two mask vocabularies; §C the
end-pair census $m_q=(2,1,1)$, the parity law exhaustive to $k=7$, $W=(1,6,15,20,15,6,1)$
by two agreeing routes, and the prime-log ring $\mathbb Q\oplus\bigoplus_p\mathbb Q\ln p$
whose every sign test is an exact comparison of two non-negative integers
($\Sigma_{\mathrm B}=\ln\tfrac43$, the contraction $16<27$, the single admissible
reference); §D the channel spectrum, Vieta, $Q=\tfrac23$ and the fractional-charge
impossibility; §E the $\alpha_B$ inventory scans, the grammar counts $g(1..7)$ and the
coupling-blindness theorem with four integer-certified enclosures; §F the extended
splitting $\Delta m=[\ln(4/3)-6c\,\varepsilon_{\mathrm{EM}}\ln2]/\mathfrak h$, the exact
critical strength enclosed by $2^{13}>3^8$, $2^{11}<3^7$, $2^8>3^5$, $2^{31}<3^{20}$, the
sub-criticality bar witnessed by $64>54$ and $1024>972$, and the closure margin
$Q_\beta<-\ln3/\mathfrak h$; §G the hygiene scans, block completeness, citation closure,
the Namespace/charter/closure/ledger rows and 33 text pins.

`verify_H_directed_3vertex_splitting.py` (Tier BM.14, `Def-BM.14` + `BM.60`): the
six-state assembly — the three Platonic mass floors from $2E\in\{12,24,24,60,60\}$,
the dual pairs splitting on all four finer ledgers at fixed $E$, the self-dual floor's
weight ladder $D_S(m)=2-2\cos(m\pi/2)=(2,4,2,0)$, the $3\times2=6$ census,
$\delta_v/\pi=(1,\tfrac12,\tfrac23,\tfrac15,\tfrac13)$ with $V\delta_v=4\pi$ on all
five solids, the branch order on the exact radical rings $\mathbb Q(\sqrt2)$,
$\mathbb Q(\sqrt3)$, $\mathbb Q(\sqrt5)$ with the certificates $4>2$, $2>1$, $5>1$,
$\cos^2\tfrac\pi{10}=(5+\sqrt5)/8$ as a root of $16y^2-20y+5$, the dodecahedral quartic
verified by substitution in $\mathbb Z[c]/(16c^4-20c^2+5)$ from de Moivre's
$\cos5t=16c^5-20c^3+5c$, the informational ladder $1{:}2{:}5$ against the inverted
defect ladder, the unique order-isomorphism out of $3!=6$ bijections, and the
$D_S/4E^2$, $K_{S,\min}$, $j_{\max}$, Euler and $\beta_1$ rows.

`verify_H_organic_bridge_post_bm14.py` (Tier BM.15 of Part 4, `BM.65`–`BM.72`):
the organic bridge after BM.14 — §A the operator EM lift: $\operatorname{Tr}\widehat F=2c_0$
(charge-blind), $\operatorname{Tr}\widehat F^2=c_0^2+C^2+4\widehat Q^2$,
$I_F=4\widehat Q^2$ as polynomial identities over $\mathbb Q[c_0,C,Q]$, the correction
$\tfrac{E_{\mathrm{int}}}4c\,\varepsilon_{\mathrm{EM}}\ln2\,I_F$ reproducing $6c\varepsilon_{\mathrm{EM}}\ln2$
at $Q=\pm1$ and $0$ at $Q=0$, the identical agreement with BM.46(1)'s monomial, and the
matrix route over complex-with-rational-parts on 18 exact witnesses plus the power-sum
charpoly rows; §B the census $m_q=(2,1,1)$, $W=(1,6,15,20,15,6,1)$ by two routes,
$\Sigma_{\mathrm B}=\ln\tfrac43$ and the ratio bar $1280^3\ne960^4$ in the prime-log ring;
§C the critical-strength enclosure $\tfrac19<\varepsilon^{\mathrm{crit}}(\tfrac35)<\tfrac18<\varepsilon^{\mathrm{crit}}(\tfrac12)<\tfrac17$
on $2^{13}>3^8$, $2^{11}<3^7$, $2^8>3^5$, $2^{31}<3^{20}$, cross-checked by exact rational
$\ln$-enclosures; §D the holonomy lift: $U(\gamma)=(-1)^{N_\pi}$ exhaustively to length 7,
the parity lock to $k=7$ and on all 27 triples, the two-torsion image reaching exactly 2
of 6 states, the rung law $m\delta_v\in\pi\mathbb Z\iff D_S(m)\in\{0,2,4\}$ on all five
ladders via the exact quadratic rings and the quartic-avoidance argument, and Descartes
$V\delta_v=4\pi$; §E the joint entropy: the register products on the tested domains, the
$\Sigma_{12}$ strict/null-permitting fibres by stars-and-bars and Burnside, the infinite
mixed-signature fibre witnessed, the tetrahedron $A_S(K)=(1,0,6,4,24)$ and $M_S(K)=(1,0,1,1,4)$
re-derived, the six $D_S$ distinct by pairwise-coprime minimal polynomials; §F the decay
audit: the margin ladder $-\ln3,-\ln12,-\ln24$ on $4<12$, $4<48$, $4<96$, the on-shell
non-existence and Källén zero polynomials, the MT reciprocal monomial, the
reconfiguration sign census, the nearby fractions; §G the forbidden-token scans
($\alpha_B$ barred-row-only, Yukawa negated-only, zero external numerals and units, zero
decimal numerals in the tier and in the checker itself), block completeness, citation
closure, the header/charter/closure/HistLog rows and the text pins.

`verify_H_continuum_limit_era1_closure.py` (Tier BM.24 of Part 4,
`BM.145`–`BM.152`): the Continuum-Limit Tier — §A the force-operator census
(the block sums $3{+}3{+}5{+}3{+}1{+}1{=}16$, the mask ladder $(6,16,17,25)$,
the activation chain, $O(n)$ to $n{=}8$) and the composed-action locus census;
§B the limit function: the count/flux monomial, the envelope-ratio identity
$G/(4\pi k)=\mathfrak hE/(2r)$, the four domain conditions with the capacity
cross-multiplication, the Archimedean refinement witness at $T=10^6$; §C the
map: the dictionary dimension count, $G_Nm=\mathfrak hE/4$, the pure-trace
linearized solve and the conformal-mode rational identity, the inverse reads;
§D the threshold: the three critical forms, the dimension census,
$E_{\mathrm{crit}}(\mathfrak h)=2$, $r_s=(1,3,6,12,30)\mathfrak h$, the envelope
corollary on the exact $e^2<8<16$ enclosure; §E the locked sector: $O(6),O(8),O(10)$,
the five Platonic anchors recomputed to the integer, $f_{\mathrm{adm}}(n,1)$,
the membrane and retention pins; §F the universality: the per-force table pins,
the three fingerprints, the source-free witness rows, the Lovelock pin; §G the
reclassification: the polytope vertex enumeration with the unique orbit
$(\tfrac34,-\tfrac14,-\tfrac14,-\tfrac14)$, $\max\sum\mu^2=\tfrac34$,
$|r_a|\le\sqrt3$, the state-functional bound $|c_{\mu\nu}|\le1$ on exact
rational density samples, the constructive cycle witnesses $L=2..8$, the BV
algebra $(2\sqrt3)^2=12$, the range-width table, the A §0.2a and CT2.6
amendment pins with the frozen-scope audit; §H the era closure: block
completeness, forbidden-token and species scans, citation closure, the
Namespace/charter/closure rows, the HistLog ledger rows and (V.30), the suite
count 79, the index and Summary regeneration, the checker self-scan and the
text pins.

`verify_H_bm_closing_tier.py` (Tier BM.23 of Part 4, `Def-BM.20` +
`BM.131`–`BM.144`): the Closing Tier — §A the Haar–Poisson duality and the
lapse: the exact K-update $\delta K=\gamma\rho+\log Z_\gamma I$ as a formal-series
identity in $\mathbb Q[[t,\gamma]]$ with $\delta K=0$ at the vacuum, the twirl
block formula with idempotence, block-trace preservation and equivariance on 40
exact rational $\mathrm{SU}(2)$ points, the unique common fixed point
$\{\tfrac14I\}$, the $S_k$-twirl ranks $k+1$, the proper-time exponent rows, and
the lapse $N^2=1-\frac{G}{4\pi k}=1-\frac{E_{\mathrm{int}}^2\ln2}{2k}$ as a
monomial identity with the formed domain, the envelope and interior rows on the
exact enclosure $e<\tfrac{876809}{322560}<4$, the monotonicity, limits and the
three substitutions; §B the composition selection: the three fixed-point rows
re-verified, $|F'_{(\mathrm{iii})}|=1-(1+G)\mathsf g_{\mathrm{fp}}\in(0,1)$ on the
squaring certificate $0<4a^2G^2$, the inflation chain, the pole collapse, the
completed coupling monomial and its monotonicity; §C the resolvent: the master
dispersion identity on rational ADM witnesses, the form-uniqueness solve, the
delta-Jacobian coefficient, $\Phi_2$, both fluxes and the exponent censuses; §D
the charge censuses ($W_2$, $W_3$, the stretched states, the saturation, the
sum-closure scan); §E the colour/vertex equivariance, the intertwiner on the
explicit 27-tensor, the $S_4$ product law on all 576 pairs,
$\chi(\sigma)=d^{c(\sigma)}$ at $d\in\{2,3\}$, the antisymmetrizer ranks,
$\dim\operatorname{Inv}((\mathbb C^3)^{\otimes4})=0$ by the weight census, the
625-quadruple exchange law and the $112/104$ vs $140/76$ variant censuses; §F
the $n$-pair ensemble law with BM.94(6) reproduced exactly, the two-chain
measure, the binding $-\frac{4u\ln2}{(1+u)\mathfrak h}$, the $B=2$ pincer
enumeration with $Z_2^{\mathrm{norm}}=(4,2,2)$, and the 21 distinct
$\lambda^{(2)}$ in $\mathbb M$; §G the symmetrizer ranks and idempotence to
$k=6$, the infinitesimal commutation over $\mathbb Q(i)$, the Laurent character
identity to $k=8$ and the composition closure; §H the declaration pins: the
star values $(32,96,672)$, the derangement hub values, the $k_f/k_{vf}$
re-derivation, the massless readings, the four A-BM.10–13 addenda logged before
use; §I the Platonic scan, the defect minima, the $D_S$ order in $\mathbb M$ by
dyadic embedding, the ceiling's minimal polynomial
$x^4-48x^3+304x^2-512x+256$, the $<7$ certificate $28824005<32114889$, the
channel-ratio enclosures by Taylor bounds and Newton certificates; §J the
Jensen factorizations, the Sturm-isolated suprema and crossing, the SOS
certificates; §K the nilpotent supply vertex over $\mathbb Z$, the amplitude and
cross-section monomials, the dimensional censuses and the ratio identity; §L the
house-cleaning pins: the void/phantom grounds, the §Cal-BM register, the final
residue census and the Part-5 rows; §M the era closure: forbidden-token scans,
block completeness, citation closure, the Namespace/charter/closure rows, the
HistLog ledger rows and (V.29), the suite count 78, the checker self-scan and
the text pins.

`verify_H_janus_tunnel_concrete_spin.py` (Tier BM.22 of Part 4,
`Def-BM.18`–`Def-BM.19` + `BM.119`–`BM.130`): the Annihilation Channel,
Concrete Spin and Fermion Identification Tier — §A the Janus register and the
c-threshold: the move algebra $\hat J_\pm^2=0$, $\hat J_+\hat J_-=P_{\mathcal V}$,
$\hat J_-\hat J_+=P_{\mathcal R}$, $\{\hat J_+,\hat J_-\}=\mathrm{id}$, the generator
decomposition $Q=x_+(\hat J_+-P_{\mathcal V})+x_-(\hat J_--P_{\mathcal R})$ with zero row sums
at eight rational witnesses, $(x_-,x_+)Q=0$, $\det Q=0$, $\operatorname{rk}Q=1$,
$\operatorname{spec}Q=\{0,-(x_++x_-)\}$ with both eigenvectors, detailed balance as an
identity, $p=1-4\varepsilon_q$ at seven thresholds, the SOS parabola with its
256-point grid maximum, AM–GM with its equality locus coinciding with the
detailed-balance point, the cleared subluminal identity $(E-p)(E+p)=m^2$ with the
$v^2$ monotonicity, the $\ln2$ enclosure and the two-bit floor, and
$\rho_\circ=I/4$ with its rank and trace rows; §B the two channels: the even
resolvent $1/(1-w^2x_+x_-)$ in $\mathbb Q[w]/(w^{12})$ verified coefficient-wise at five
exact values with every odd coefficient zero, the ladder $(x_+x_-)^m\le4^{-m}$
with both endpoint annihilations, the pole at $|w|\ge2$, the pointwise-fixed
round-trip word, the charge census, the threshold monomials and their
$\mathfrak q$-exponents, the nilpotent step $\widehat V^2=0$ with $\operatorname{rk}1$,
$\dim\ker3$, $[W_3\otimes I_\omega,\widehat V]=\widehat V$ and its $\hat\omega$-image
$E_+\otimes P_R$, the annihilation weight $x_-^2$ and the direction ratio
$(x_-/x_+)^2=1\iff\varepsilon_q=\tfrac18$, and $\Gamma_{\mathrm{tr}}$ re-certified; §C the
concrete spin: $\Theta=2k=4j$ with $\#m=k+1=2j+1$ and the Casimir to $k=8$, the
Chebyshev recursion over $\mathbb Z[x]$ to $m=8$ with the exact six-cycle witness
$T_m(\tfrac12)=\cos(m\pi/3)$, the ladder $\Delta(m)=2-2T_{|m|}(\cos(\Theta_R/2))$
with its evenness, its standing zero exactly at even $k$ and its range $[0,4]$,
the $\mathfrak q$-exponent bar $[k]=\mathfrak q^{+1}$ against $[\Theta_R]=\mathfrak q^0$,
and the matching identity's dimension row; §D the spin-blindness refutation and
the identification: the one-symbol alphabet census of all three crossing
monomials, the four standing grounds as symbol-set and exponent rows,
$w_{\mathrm{mat}}$ and $\Gamma_{\mathrm{tr}}$ as functions of $\varepsilon_q$ alone, the
winding-parity census with both BM.106(1) anchors on one kind, the induction
certificate $i^{2k}=(-1)^k$ to $k=16$ and its orientation-sign blindness; §E the
three-chain structure: $\dim\mathcal H_3=8\prod(|k_a|+1)$ at six anchors, the $S_3$
group law on all 36 pairs with the order and inversion censuses and $|A_3|=3$,
the character formula $\chi(\sigma)=d^{\,c(\sigma)}$ on all permutations at
$(n,d)\in\{2,3\}^2$, the explicit antisymmetrizer ranks $0$ on $(\mathbb C^2)^{\otimes3}$
and $1$ on $(\mathbb C^3)^{\otimes3}$ with the symmetrizer ranks $\binom{d+2}3$, the
multiplicative exchange law on all 125 triples and 36 pairs, the meson's
unconditional $+1$ on both orientation readings, the baryon's odd-count
criterion with 62 of 125 fermionic, and the six-row cycle-ladder parity; §F the
forbidden-token scans (species names confined to Locus/Rmk/Phys per
Def-BM.3(7), zero cosmological and black-hole tokens, $\alpha_B$
barred-row-only, the Yukawa/seesaw/right-ray/mixing-matrix/Dirac-operator
tokens negated-only, zero external numerals, zero decimal numerals in the tier
and in the checker itself), block completeness of Def-BM.18–Def-BM.19 and
BM.119–BM.130, the zero-declaration row, citation closure, the
Namespace/charter/closure/§Cal-BM rows, the HistLog ledger rows and (V.26), the
suite count, the checker self-scan and the text pins.

`verify_H_antimatter_resonance_spectrum.py` (Tier BM.21 of Part 4,
`Def-BM.15`–`Def-BM.17` + `BM.108`–`BM.118`): the Antimatter and Resonance
Tier — §A the CP-conjugate: the fourth-root phase alphabet closed under
multiplication, $\mu_{\mathrm{CP}}=e^{i\pi\Theta}=(-1)^\Theta$ with $\mu_{\mathrm{CP}}=1$
on the whole on-shell locus $\Theta\in2\mathbb Z$, the CPT character's collapse to
$(-1)^{|E|}$ on $\Theta\in4\mathbb Z$ and its extra sign off it, $|\lambda|^2=1$, L2's
contraction identity $1-(1-\gamma/4)^2=\gamma(8-\gamma)/16$ with $(\tfrac9{16})^6$, the
ternary charge census with one CP-fixed $n$-tuple and $W_n(+Q)=W_n(-Q)$, the
CP-pair weight $4\varepsilon_q(1-4\varepsilon_q)=\tfrac14-16(\varepsilon_q-\tfrac18)^2$ on a
256-point grid with its exact maximum and two endpoint zeros, the transition
weight's range $[0,\tfrac13]$ with the monotonicity certificate and the three-tick
reciprocal, and the pair's Laurent monomials; §B the meson seal: the grammar
counts $g(1..7)=(0,1,1,3,10,25,105)$ with $g(2)=1$ and $g(1)=0$, the
type-selection rows, $\dim\mathcal H_2=4(|k_1|+1)(|k_2|+1)$ at both anchors, the
BM.6(2) two-requirement discharge, and the $\varepsilon$-protection at $N=3$ with its
failure at $N=4$; §C the meson mass: the two vanishing binding rows, the
fifteen-value threshold ladder with span ratio exactly 30, the defect
blind-spot scan, and FT.106(3)'s norm-layer $2{:}1$ rows against the amplitude
ratios $58/13$ and $2398/401$; §D the exchange operator: $\hat\omega,\hat\chi,P_{L/R}$
re-verified entrywise over $\mathbb Q(i)$, the flip and $\hat P_{12}$ as involutions,
$\operatorname{Tr}\hat P_{12}=d\mu_{\mathrm{CP}}$, the orientation block's $(3,1)$ split with
$\operatorname{Tr}=2=d$ and $\hat\omega\otimes\hat\omega$'s $(2,2)$ split with $\operatorname{Tr}=0$, the
eigenspace dimensions and the character identity to $k=8$, the induction
certificate $i^{2k}=(-1)^k$ to $k=16$, the spin–statistics census with both
BM.106(1) anchors, the four priced sector loci including the determinant
line's disagreement at $k=2$, and the five-way symbol-set disjointness; §E the
threshold and width: the $\mathfrak q$-exponent census of $\mathcal T_0$, $m_{\mathrm{hid}}$, $r_s$, $G$ and
$\rho$, the three agreeing readings, both nested ladders with span ratios
exactly 30 and 5 and curvature ratios 900 and 25, the never-empty half-line at
every level and lapse, the $\ln2$ enclosure driving $E_{\mathrm{int}}\ln2>1\iff E_{\mathrm{int}}\ge2$, the
width's four zeros, its bound, its three-tick floor and its monotone energy
dependence; §F the resonance spectrum: $(2+z+z^{-1})^n=(z+1)^{2n}/z^n$ as an exact
Laurent identity against the exhaustive $4^n$ census, the orbit law
$\binom{6+n-1}n$ with stabilizer multiplicities summing to $6^n$, the degree-16
field $\mathbb M$ with its three defining relations and exact interval ordering from
integer square roots, the 6/21/55 eigenvalue counts, the single collision
$2+2+2=6=4+1+1$, the multiplicity censuses, the minimal-polynomial degree
censuses with each polynomial evaluated at its own root, the degree-16
generator, the three minimal quartics, the ceiling $4n$ attained once, and the
eight grouping families with 8 in none; §G the forbidden-token scans (species
names confined to Locus/Rmk/Phys per Def-BM.3(7), zero cosmological tokens,
$\alpha_B$ barred-row-only, the Yukawa/seesaw/right-ray/mixing-matrix/Dirac-operator
tokens negated-only, zero external numerals, zero decimal numerals in the tier
and in the checker itself), block completeness of Def-BM.15–Def-BM.17 and
BM.108–BM.118, the zero-declaration row, citation closure, the
Namespace/charter/closure/§Cal-BM rows, the HistLog ledger rows and (V.25), the
suite count, the checker self-scan and the text pins.

`verify_H_six_objective_resolution.py` (Tier BM.20 of Part 4, `BM.101`–`BM.107`): the
six objective resolutions — §A the energy-scale graph: $Q^{\mathrm{inv}}=-Q^{\mathrm{fwd}}$
as an identity, the uniform informational verdict on a rational lattice, the crossing
strength $\varepsilon_\ast=(2-\log_23)/(3w)$ in the $\log_2$ ring with its enclosure on
$2^{13}>3^8$ and $3^{12}>2^{19}$, $\varepsilon_{\mathrm{eff}}=e^2/(4\pi)$ as a monomial,
$G=\beta x^2$ with $[\beta]=\mathfrak q^0$, the three profile shapes with their monotonicity
and limit rows, the stationarity cubic $2\beta x^3-3\beta x^2-1$ with $h(\tfrac32)=-1$,
$h(2)=4\beta-1$ and $P_{\max}=1-\tfrac3{2x_\ast}$ as a polynomial identity modulo the cubic,
the three crossing equations with their root counts via
$c\beta x^3+(c-1)x+1=-x(1+\beta x^2)(P-c)$, and the flatness of the specified and pure-pole
reads by token census; §B the dimensional bridge: the complete $\mathfrak q$-exponent census
with the four balance rows, the chart-side current density $\mathfrak q^{3/2}$ from
$\partial_\mu F^{\mu\nu}=eJ^\nu_Q$ and the field-energy row, the two-bridge separation
$[\mathfrak h]=\mathfrak q^{-1/2}$ against $[\rho_{\mathrm B}]=\mathfrak q^0$, and the A-BM.9
declaration pins (§II.4 entry, §Cal-BM slot row, “value ¬issued”, “DECLARED AND LOGGED”);
§C the eigenvalue composition: $W(Q)=\binom6{Q+3}$ against the exhaustive $4^3$ census and the
Laurent identity $(2+z+z^{-1})^3=(z+1)^6/z^3$, the family cubic's Vieta rows and the depressed
cubic expansion, the elimination row in the quotient ring, the four quadratic-ring minimal
polynomials plus the dodecahedral quartic derived from $(2-y)^2=(5+\sqrt5)/2$, the
$g(N)=(1,1,3,10,25,105)$ grammar count and the capacity ratios, and the referent-census pins;
§D the curvature composition: $G_{\mathrm{corr}}=G(1+a\mathsf g)$ as a monomial, the three
fixed-point rows verified by substitution over $\mathbb Q[G,a]$, the quadratic's root sign
census and its $a\to0$ limit by conjugate clearing, the pole locus with the $Q=0$ row, and the
alphabet disjointness that excludes the loop; §E the general weight: the measure-free bounds
with both equality loci, the family form with the exhaustive eight-configuration census and
its normalization, $\langle E^2\rangle$ via $|S|^2=\sum1_i+2\sum1_i1_j$, the uniform recovery
$1/D$ at six thresholds, the AM–GM row $3(1-R)-S=\sum u-3\prod u\ge0$ with its equality locus,
monotonicity on an exact rational grid, and the (W6) refutation pins; §F the kind structure:
$j=|\kappa|/2$ at $\kappa=1,2$ with the Casimir rows, $\Theta_{\mathrm{int}}=2\kappa$,
$(\tfrac9{16})^6=531441/16777216$, the wall-parity census exhaustive to $k=7$, the sign-free
transport assembly, $16\delta_\nu=9\delta_\ell=27\delta_q=2$, and the statistics referent pins;
§G the forbidden-token scans ($\alpha_B$ barred-row-only; Yukawa, seesaw, right-ray and
mixing-matrix tokens negated-only; zero external numerals, units and species names; zero decimal
numerals in the tier and in the checker itself), block completeness of BM.101–BM.107, the
one-declaration row, citation closure, the Namespace/charter/closure/§Cal-BM rows, the HistLog
ledger rows and (V.24), the suite count, the checker self-scan and the text pins.

`verify_H_flicker_integral_restmass.py` (Tier BM.19 of Part 4, `BM.94`–`BM.100`): the
flicker integral, the rest-mass Q-value and the relating equation — §A the flicker
integral: the exact binomial distribution $P(E{=}2j)=\binom3jp^j(1-p)^{3-j}$ on
$\{0,2,4,6\}$ over $\mathbb Q[p]$ with its normalization and unconditioned moments, the
materialization restriction and the vacuum weight $(1-p)^3\to1$, the conditional moments
$\langle E\rangle_{\mathrm{mat}}=6/D$, $\operatorname{Var}_{\mathrm{mat}}=12p(1-p)(3-2p)/D^2$
with $D=3-3p+p^2$, the relative-width maximum $(10+7\sqrt7)/162$ at $p=(5-\sqrt7)/6$ in
$\mathbb Q(\sqrt7)$ and its bound on $175<256$, the weight $w_{\mathrm{mat}}=1/D\in(\tfrac13,1]$
with $\langle E\rangle_{\mathrm{mat}}\in(2,6]$ and the digon limit $2$, the snapshot weight
$p^2/D$ with deficit $3(1-p)/D$, and the reciprocal register's Cauchy–Schwarz row
$(18-27p+11p^2)/(2D^2)\in[1,\tfrac65)$ on an exact quartic positivity; §B the vertex
superposition: the exhaustive ternary fibre census against $W=(1,6,15,20,15,6,1)$, the
weights $\tfrac25/\tfrac1{10}$ and $\tfrac4{15}/\tfrac1{15}$, the entropy decomposition
$\Sigma_{\mathrm{cl}}=H+\langle\ln\prod_im\rangle$ in the prime-log ring, the two positive
parts of $\ln\tfrac43$ on $512>243$, the independence factorization and the bounds
$16<20$, $12<15$; §C the rung-one $\nu$ line: $\delta_\nu=\tfrac18$, the three exact
radical values $G_i$ and their order on the Taylor enclosures $\cos\tfrac14>\tfrac{31}{32}$,
$c>\tfrac{63}{64}$, $s_\nu>\tfrac18-\tfrac1{3072}$, the affine/spectral second route and the
order inversion, the SOS sandwich and strict positivity, the occupancy row $(1,0)$ with the
$\mathbb Q(i)$ projector algebra, the no-fixed-sector census, and the four no-seesaw bars as
document pins; §D the rest-mass Q-value: the three-candidate species census, the four
$\Delta T$ values, the flicker-blind alphabet scan, the pure-pole critical locus
$\Delta_g^{\mathrm{crit}}=s(2M_0+s)$ as a cleared identity, the universal and rational
witnesses on both sides ($5000>101$, $11<16$, $1875>1600$, $75>64$, $6560>2$), the
enclosure $\rho^{\mathrm{crit,pole}}\in(\tfrac25,\tfrac67)$ on $7921>7500$ and $192<196$, the
generation order, the $\nu$-positivity shift and the two-body condition; §E the relating
equation: the four forms as Laurent-monomial and rational-function identities with
$\mathfrak q$- and $\mathfrak h$-exponent censuses, the flicker enhancement $D^2<9$,
$G^{\mathrm{eff}}=G/D^2\in(8\pi\ln2,72\pi\ln2]$, the coupling monotonicity, the shifted
vanishing locus, and the residue localization; §F the materialized splitting: the assembly
at $w_{\mathrm{mat}}$, the two-sided parameter-free bar on $2^{13}>3^8$ and $3^{12}>2^{19}$,
the tightened bound $\ln80/\ln60\in(\tfrac{16}{15},\tfrac{15}{14})$ on $2^{28}>3^{16}\!\cdot\!5$
and $2^{26}<3^{15}\!\cdot\!5$, the tightened Q-value ratio on $81>80$ and $80>27$, and the
rescoped dissolution row; §G the forbidden-token scans ($\alpha_B$ barred-row-only, Yukawa
and seesaw negated-only, zero external numerals and units, zero decimal numerals in the
tier and in the checker itself), block completeness of BM.94–BM.100, citation closure, the
header/charter/closure/HistLog rows, the suite count 75, the checker self-scan and the text
pins.

`verify_H_em_self_energy_correction.py` (Tier BM.18 of Part 4, `BM.87`–`BM.93`): the
EM self-energy correction — §A the category adjudication: the exterior/interior
decomposition on exact coefficients ($c_{\mathrm{ext}}=\tfrac12$, $\iota_{\mathrm{ball}}=\tfrac1{10}$,
$E_{\mathrm{in}}/E_{\mathrm{out}}=\tfrac15$, $E_{\mathrm{tot}}/E_{\mathrm{out}}=\tfrac65$, $c_{\mathrm{ball}}=\tfrac35$), the field and
potential routes agreeing coefficient by coefficient, the UV row on four rational
witnesses, the selector $(1,0,1)$, the dimension row and the five referent-census
document pins; §B the running coupling: $\Delta x_{\mathrm B}\cdot m_{\mathrm{hid}}=1$ as a Laurent
identity with its strictly decreasing ladder, $f(k)=1-\tfrac1k$ with $f(1)=0$ and the exact
step $1/(k(k+1))$, the curvature lock $G=(\Delta x_{\mathrm B})^2\kappa^2\rho=2\pi E_{\mathrm{int}}^2\ln2$ as one
monomial with the $\mathfrak h$-exponent zero and the P4-symbol scan, the lapse $N=1$ at the
vacuum gauge, three priced curvature compositions distinct at every cell, and the energy
monotonicity at three radii; §C the path integral: BM.19's generator kernel on an
exhaustive rational grid with $\dim\ker Q=1$, $p=1-4\varepsilon_q$ as an identity at seven
thresholds, $w(0)=1$ with $0<w\le1$ strictly decreasing, the Bernoulli average $6p$, the
monomial $3Nw\mathsf g\,\varepsilon_{\mathrm{EM}}\ln2/\mathfrak h$ and its agreement with the exterior value at
$(1,1,1)$, the four route-(ii) values $15m^2_B$, and the attenuation row; §D the
branch-blindness theorem: the disjoint measure/defect alphabets, $w$'s $D_S$-free
definition, the four grounds on record and one weight over the six states; §E the
corrected splitting: the attenuated assembly in a multivariate prime-log ring with the
$w$-cancellation and the two-monomial structure, the factorized monotonicity in $w$ in an
exact three-indeterminate polynomial ring, the critical strength with its squeeze on
$3^5<2^8$ and $3^{12}>2^{19}$, the parameter-free bar and the trichotomy on a sixty-point
lattice, the universal bound $1<m_n/m_p<\tfrac{10}9$ on $20^{10}>15^{11}$ and $20^9<15^{10}$, and the
ensemble-robust non-attainment of $\tfrac43$ on $64<405$; §F the Q-value: the three margin
identities, the uniform closure on ninety lattice points, the four ratio-form certificates
$3^{13}<2^{16}\cdot25$, $3^{20}>2^{24}\cdot125$, $27>20$, $243<400$, the specified read's four $\Delta T$
values and eight witnesses intact, and the alphabet disjointness with the $\mathsf g$/$g$ token
distinction; §G the forbidden-token scans, block completeness of BM.87–BM.93, citation
closure, the header/charter/closure/HistLog rows, the suite count 74, the checker
self-scan and the text pins.

`verify_H_mass_ratio_census.py` (Tier BM.17 of Part 4, `BM.79`–`BM.86`): the
mass-ratio census — §A the ladder law $D(m)=4\sin^2(m\delta_v/4)=2-2T_{|m|}(\cos\tfrac{\delta_v}2)$
on all five solids at both priced windings ($k_f=(3,2,3,5,3)$, $k_{vf}=(3,3,2,3,5)$ from
the minimality rule), $V\delta_v=4\pi$, the period/distinct-value/monotonicity/ceiling rows,
the rung law $D(m)\in\{0,2,4\}\iff m\delta_v\in\pi\mathbb Z$, the top-weight row
$D(k_f)=(2,2,4,2,2)$, the tetrahedral degeneracy and the even-$k$ zero modes, the
Chebyshev tower closing at $T_5(\mathsf c)=\mathsf c(16\mathsf c^4-20\mathsf c^2+5)=0$, the six
dodecahedral values with their minimal polynomials, and the six $D_S$ of `Def-BM.14(3)`
as ladder rungs; §B the half-angle and sine-ratio laws, the (A) and (B) intra-generational
ratios with $x^2-2x-2$, $x^8-24x^6+76x^4-64x^2+16$, $x^2-2x-1$, $x^2-4x+1$,
$x^4-14x^3+51x^2-34x+1$, the exact order on $48<49$ and $12500>12321$, the ceiling
$x^4-48x^3+304x^2-512x+256$ and the range bar on $2401^2\cdot5<5667^2$; §C the six-state
table, the branch order, $\Delta_1>\Delta_2>\Delta_3$ on the squaring chain ending at
$341+140\sqrt6>0$, $\Delta_2/m^2_{\mathrm{up}}=\sqrt2/2$ exactly, the doublet ratios with
$2x^2-4x+1$ and the octic of constant term $1$ (both norms as multiplication determinants),
the order $\mathcal F_2<\mathcal F_1<\mathcal F_3$ on $720>361$, the two inverted hierarchies and the
three non-proportional ladders; §D the angle ledger, the addition and triple-angle
identities on eight exact rational points of the unit circle, the mass-squared cubic
$4z^3-24z^2+(21-12\gamma)z-(\gamma-1)^2$ by exact elimination in $\mathbb Q[\gamma][r]$, Vieta,
$Q=\tfrac23$, the ordered constants, $r^{(\ell)}_0=1+\gamma_q$, the twelve $10^{-12}$ brackets with
the re-certification of Part 3's frozen decimals, and the hierarchy order on
$\pi^2>6\sum_{n\le10}n^{-2}=\tfrac{1968329}{211680}>\tfrac{64}9$; §E the bridge identity and its
$\mathfrak q$-exponent row, the six factors $\mathcal R_s$ with four minimal polynomials, the exact
order, the span $50/(1-\mathsf c)$ with its quartic and its exact $25=(30/6)^2$, the thirty
$\rho_{\mathrm B}$-free pole ratios with their single collision at $2$, the seven informational ratios,
and the six cross-currency square-root forms; §F the prime-log representations of $\ln1280$
and $\ln960$, the independence census, the irrationality theorem at every rational $t$, the
exact non-attainment of $4/3$ at $t=-\ln405/\ln16<0$, the three-symbol localization and the
nine cross-channel factors with the light-end concentration; §G the assembly, the monotone
decrease, the range theorem $0<m_n/m_p<\tfrac{21}{20}$ on $2^{44}>3^{26}\cdot5$ and
$2^{34}<3^{21}\cdot5$, the irrational critical locus on the $2^p\ne3^q$ census, `BM.62(7)`'s four
certificates from one reduction rule, the trichotomy at sixteen rational couplings and the
four fractional splittings; §H the three margin identities, the four ratio-form certificates
$3^{13}<2^{16}\cdot25$, $3^{20}>2^{24}\cdot125$, $3^{21}<2^{24}\cdot625$, $3^{16}>2^{18}\cdot125$, the four
$\Delta T$ values with `BM.77`'s opening, closing, critical and two-body witnesses, and the
alphabet disjointness; §I the forbidden-token scans, block completeness of BM.79–BM.86,
citation closure, the header/charter/closure/HistLog rows, the suite count 74, the checker
self-scan and the text pins.

`verify_H_chiral_assignment_opening.py` (Tier BM.16 of Part 4, `BM.73`–`BM.78`):
the chiral assignment and the specified opening — §A the chiral algebra over
$\mathbb Q(i)$: $\hat\chi^2=\mathrm{id}$, the projector rows, $\hat\omega\hat\chi\hat\omega^{-1}=-\hat\chi$,
$\hat\omega|L_u\rangle=-i|R_u\rangle$, the quaternionic triple, the canonicity circle on the
rational witnesses $(\tfrac35,\tfrac45),(\tfrac5{13},\tfrac{12}{13}),(\tfrac8{17},\tfrac{15}{17})$, and the
branch-label coupling census; §B the assignment censuses: the $2!$ forced shape, the
$E_+$ rows ($E_+^2=0$, $[\sigma_3,E_+]=2E_+$), and the weight$\leftrightarrow$branch bijection
census with exactly one survivor; §C the vertex operator $\widehat V=E_+\otimes P_L$:
$\widehat V^2=0$, rank $1$ by exact elimination, the image ray, $[W_3\otimes I,\widehat V]=\widehat V$,
both conjugates $=E_+\otimes P_R$; §D the attached splitting: $\cos^2\tfrac\pi{10}=\tfrac{5+\sqrt5}8$
in $\mathbb Q(\sqrt5)$ as a root of $16y^2-20y+5$, the three $\Delta_g>0$ on integer
certificates, the four-currency sign census; §E the opening branch:
$\Delta T=5m^2_B=(\tfrac{4219785}{98956},\tfrac{9608310}{393679},\tfrac{455}{23},\tfrac{68565}{3088})$,
the SOS sandwich, the witnesses $828100>5819$ and $7500>1849$ with $4219785<4255108$,
the $\rho^{\mathrm{crit}}$ enclosure on $99<100$, $75>64$, $273>253$, $42197850<42748992$, the
two-body cleared identity and $3312400>5819$; §F the frozen rate rows ($x_+x-$ SOS with
the $k/256$ grid census, $\Gamma_{\mathrm{tr}}(\tfrac18)=\tfrac13$, the $2{:}1$ Beta-rational ratio);
§G the forbidden-token scans, block completeness of BM.73–BM.78, citation closure, the
addendum/Q1$'$/item-20/ledger/(V.20) rows, the suite count 74, and the text pins.

`verify_H_em_self_interaction.py` (Tier BM.12 of Part 4, `Def-BM.12` +
`BM.46`–`BM.50`): the EM self-interaction correction — the Coulomb
harmonicity in the rule ring, the shell self-energy by two exactly agreeing
routes ($1/8\pi$), the uniform-ball split ($1/40\pi + 1/8\pi = 3/20\pi$), the
unified monomial $E^{\mathrm{self}}=c\,\varepsilon_{\mathrm{EM}}q^2m_{\mathrm{hid}}$
with the dimensionless fractional correction, the $q^2$ selector
$(1,0,1)$, the mixed-triple census $20=8+12$, the splitting monomial
$3ce^2\ln2/(2\pi\mathfrak h)$ with its positive sign census; the range rows
(the Yukawa factor at $m=0$, the exact antiderivatives $d(-1/r)/dr=1/r^2$ and
$d(r^5/5)/dr=r^4$ by symbolic Laurent differentiation, the dipole tail, the
Gauss/EM.11 flux cancellation, the seal asymmetry idempotent-vs-census, the
nearby fractions $1-1/k$); the two-body potential signs and the hydrogenic
coefficient identities ($e^4/32\pi^2=\varepsilon^2/2$, $E_2/E_1=1/4$); the
corrected Q-value's all-negative sign structure, the no-opening sign
contradiction, the Beta moments $\mathrm B(4,3)/\mathrm B(3,3)=1/2$ with the
scale-invariance row and the $2\cdot3\ne4\cdot1$ refutation of the
$4/3\leftrightarrow E_{\max}:\langle E\rangle$ identification; and the document
pins. Exact arithmetic only, no floating point, no numerical coupling.

`verify_H_neutron_decay_vertex.py` (Tier BM.11 of Part 4, `Def-BM.11` +
`BM.39`–`BM.45`): the neutron decay vertex — the family transport-profile map
(the EW.33 Gram form recomputed over $\mathbb Q(i)\otimes\mathbb Q[g,g']$,
FT.158(1)'s inner $C_3$ re-derived on the pair register with
$\mathcal W^3=3\mathcal W$, $U^3=E_0$, $UW_iU^\dagger=W_{i+1}$, the cosine-triplet
identities in $\mathbb Q[c,s,r_3,r_2]/(c^2{+}s^2{-}1,r_3^2{-}3,r_2^2{-}2)$, the
orbit evaluation $G(c(i))=A_0-B_0\cos(\delta-\tfrac{2\pi j}3)$, the SOS
positivity $\tfrac38(g-\tfrac{g'}3)^2+\tfrac{g'^2}{48}$, the kernel-line
unreachability, the sum rule $3A_0$, the splitting factorization and FT.54(1)'s
defect identity); the rung-1 isospin row ($\sum_iW_i^2=\tfrac32E_0+\tfrac12\Sigma
=2\Pi_{\mathcal R}$ entrywise with $\Sigma=\vec\sigma\otimes\vec\sigma$, the branch
eigen-rows, and the $\sigma$-vs-branch token disjointness); the vertex kinematics
(the two-body impossibility $2m_n(E_p-m_p)=-m_\ell^2$, the Källén factorization,
the Q-value sign theorem, both-sign route-(ii) witnesses, the endpoint identities,
the collinear reverse-Cauchy identity, the Lagrange CS SOS); angular momentum
(the Casimir ladder, the tensor charpolys $(x-2)^3x$,
$(x-\tfrac{15}4)^4(x-\tfrac34)^4$, $x^2(x-2)^9(x-6)^5$ by exact
Faddeev–LeVerrier, the Lagrange decomposition of $p^2$, the conserved moment
current on the dust class by symbolic differentiation, the CN adjudication
$\tfrac14<\tfrac34$, the $(-1)^\ell$ characters and the $\ell$-selection census);
curvature (the proton's six monomials and the $72\pi\ln2$ lock, the linearized
field equations in the weight-truncated jet ring, $\nabla^2\Phi=4\pi G_N\rho$,
the harmonicity of $1/r$, the source-side superposition); time (the resolvent mod
$w^{12}$, the SOS parabola, $\Gamma_{\mathrm{tr}}\in[0,\tfrac13]$,
$\tau_{\mathrm{life}}\ge3$ ticks); and the document pins. Exact arithmetic only,
no floating point.

`verify_H_kinetic_energy_metric.py` (Tier BM.10 of Part 4, `Def-BM.10` +
`BM.34`–`BM.38`): the kinetic energy from the metric and the vacuum-balanced
entropy — the ADM split of CT1.12's emergent metric as exact polynomial
identities (the Schur lapse row $N^2\det\gamma=-\det g$, the cleared adjugate
rows of $g^{00}=-1/N^2$, $g^{0i}=N^i/N^2$, $g^{ij}=\gamma^{ij}-N^iN^j/N^2$, the
line-element identity, three rational witnesses under exact Fraction
inversion); the master dispersion identity
$(p_0-N^ip_i)^2=N^2(m^2+\gamma^{ij}p_ip_j)$ cleared by $(\det\gamma)^2$, its
vacuum-flat specialization and its T-parity; the NR binomial series
$(1,\tfrac12,-\tfrac18,\tfrac1{16},-\tfrac5{128},\tfrac7{256})$ and the KE
assembly with the dimensionally forced $1/m$; the Sylvester positivity regime;
the zero-point bounds $\tfrac74$, $\tfrac38$, $\tfrac{\sqrt7}2$ (in
$\mathbb Q(\sqrt7)$, comparison by squaring); the $1/8$-grid Gibbs census
($165$ compositions, uniqueness of $I/4$ by integer comparison), the exact
$\ln2$ enclosure, the balance identity $\ln4=2\ln2$ and the reframing
monomial $m_{\mathrm{rest}}=m_{\mathrm{hid}}$; the mask-flag censuses
$(6,16,17,25)$ with the dimension ratios $(\tfrac13,8,\tfrac1{25})$, the
EW.33 Gram form recomputed from Pauli spinors over
$\mathbb Q(i)\otimes\mathbb Q[g,g']$ (charpoly factorization, kernel line
$(0,0,g',g)$, the sandwich); the route values $1$, $\tfrac43$,
$\tfrac{58}{13}$, $\tfrac{2398}{401}$ with the disjoint input-alphabet token
census, and $Q=\tfrac23$ re-verified in
$\mathbb Q[c,s,r,u]/(c^2{+}s^2{-}1,r^2{-}3,u^2{-}2)$. Exact arithmetic only,
no floating point.

`verify_H_mesonic_flicker_test.py` (Tier BM.9 of Part 4, `Def-BM.9` +
`BM.31`–`BM.33`): the mesonic flicker test — the contraction grammar by
exhaustive set-partition enumeration into blocks of size 2 and 3, reproducing
CT3.17a(2)'s frozen $g(N)=(1,1,3,10,25,105)$ for $N\le7$ and splitting it into
the $\delta$-containing census $(1,0,3,10,15,105)$ and the $\varepsilon$-only
census (nonzero exactly where $3\mid N$), which makes $N=3$ the unique protected
attachment count; the boundary-data comparison (the charge-range overlap with
the $W_3=(1,6,15,20,15,6,1)$ and $W_2=(1,4,6,4,1)$ censuses, $4\mathbb Z$
strictly inside $2\mathbb Z$, and both representation contents carrying exactly
one singlet by exact rank over $\mathbb Q$: $27-26$ and $9-8$); the projector
verdict $Z_\delta=0$ by filtration with both mass routes invariant; the
amplitude layer's orthogonality against FT.106(3)'s exact integers; and the
$N\ge4$ failure of the protection. Exact arithmetic only, no floating point.

`verify_H_probability_space_restriction.py` (Tier BM.8 of Part 4, `Def-BM.8` +
`BM.30`, and the replaced `BM.28`): the charge-constrained probability space of
a sealed composite — the ternary alphabet and the integer-valued additive read
$Q=\sum_iq_{\mathrm{core}}(c_i)$ with range $\{-3..+3\}$ (so fractional charge is
unreachable, not merely absent); EM.9's end-pair census $m_q=(2,1,1)$; the
exhaustive $4^3=64$ end-sign census giving $\#\{Q=k\}=(1,6,15,20,15,6,1)$ and the
ordered-triple census $(1,3,6,7,6,3,1)$; the probability-space sizes
$W(0)=20$, $W(\pm1)=15$ with the exact ratio $4/3$; the $S_3$ orbits and the CPT
bijections with $(0,0,0)$ the unique fixed triple; and the route theorem — a
uniform sector factor cancels exactly in a normalized average (verified at
factors $1,2,3,15,20,\tfrac73$) while it multiplies a total, giving
$T(0)/T(+1)=4/3$ and the derived ordering, against the amplitude layer's third
ratios $5336/1196=58/13$ and $4796/802=2398/401$. Arithmetic: integers,
`Fraction`, exhaustive enumeration, generating-function convolution over
$\mathbb Q$ — no floating point and no transcendental in any assertion.

`verify_H_proton_cpt.py` (Tier BM.7 of Part 4, `Def-BM.7` + `BM.25`–`BM.29`):
the CPT-sector layer — $\Theta_{\mathfrak L}$ as an exact involution on ledger
records (fixing every completed single-pair word, bijecting the two-pair
interleavings, preserving the Janus balance) with the weight conjugation
$w(\Theta_{\mathfrak L}C)=w(C)^\ast$ verified on 24696 enumerated configurations
over the exact fourth-root phase alphabet $G(e)=\sigma_e i^{m_e}$; EM.24(5)'s
phase identity with $\lambda\in\{\pm1,\pm i\}$, $|\lambda|^2=1$ and the on-shell
refinement $|E|+\Theta\equiv0\ (2)$; the sector orbit census (three orbits of
size two, $q=0$ the unique charge fixed point); FT.106(3)'s census ratio
$Z^{\mathrm{norm}}(0,S)=2Z^{\mathrm{norm}}(\pm1,S)$ and the $\omega$-symmetry; the
baryon-type character $\lambda=(-1)^{|E|}$ at $\Theta_{\mathrm{int}}\in4\mathbb Z$;
the $\Theta_{\mathfrak L}$-invariance of $E_{\mathrm{int}}$ and the charge-blindness
of all seven geometric monomials; $F_{LR}=qI_2$ with splitting $2|q|\in\{0,2\}$,
the $\omega$-parity census, and the scar's zero contribution to $E_{\mathrm{int}}$.
Arithmetic: integers, `Fraction`, complex-over-`Fraction` — every phase that
occurs is a power of $i$, so no transcendental enters an assertion. Tier BM.7 is
new canon content with no first edition; its pins resolve against Part 4 directly.

`verify_H_topo_blind_neutron.py` (Tier BM.6 of Part 4, `Def-BM.5`–`Def-BM.6` +
`BM.19`–`BM.24`): the flicker layer — the Janus move generator's kernel over
$\mathbb Q[x_+,x_-]$ (one-dimensional, spanned by $(x_-,x_+)$, so the stationary
measure is derived) with the $\varepsilon_q$ specialization and the no-flicker
limit; the mass as curvature flux ($RV=\kappa^2m$, the $\Lambda$ clause, the
normalized ensemble average) in a Laurent-monomial ring; FT.107(3)'s exact
rational sector masses against the additive informational count (the binding
read is zero in the count and nonzero in the ensemble); the weak ladder
$[\sigma_3,E_\pm]=\pm2E_\pm$ giving $\Delta q=\pm1$, the ternary-alphabet
overflow and EM.11's unique compensating value (the forced carrier), the
promoted force matrix $F_{LR}=qI_2$ with splitting $2|q|\in\{0,2\}$ and its
charpoly on four rational witnesses; the transition resolvent
$1/(1-w^2x_+x_-)$ with $x_+x_-\le\tfrac14$; the $C_3$-covariant family spectrum
in $\mathbb Q[c,s,r]/(c^2{+}s^2{-}1,r^2{-}3)$ giving $Q=2/3$ exactly at every
phase; and the document pins. Tier BM.6 is new canon content with no first
edition; its pins resolve against Part 4 directly.

`verify_H_noether.py` (Tier BM.4 of Part 4, `Def-BM.3` + `BM.7`–`BM.12`): the
conservation and symmetry layer of the baryomesonic era — the Janus balance and
the telescoping endpoint read (exhaustive ledger-word and sign censuses, the
Catalan relaxation census, the $S_3$ hom/root census behind the no-$U(1)$
obstruction), the continuum promotion (exact $\mathbb Q[x,\ell]$ hop calculus,
the rotation one-parameter group in
$\mathbb Q[i][c,s,c',s',X]/(c^2{+}s^2{-}1,X^3{-}X)$, exact $\mathbb Q$ colour
structure constants and Killing determinant), the stress-energy tensor
(multivariate jet-ring identities, the canonical/Hilbert sign reconciliation, an
exact pp-wave curvature witness with $\det g=-1$ and the nonlinear contracted
Bianchi identity), the canonical pair (the Wielandt–Wintner trace obstruction on
the 16-basis, cyclotomic Weyl pairs in $\mathbb Q[z]/(z^8{+}1)$, the
noncommutative Heisenberg quotient $\mathbb Q(i)\langle x,p\rangle/([x,p]-i)$,
the Mandelstam–Tamm and Carruthers–Nieto witnesses), the continuum limit (exact
rational grid telescoping, moment-matrix determinants, the two routes to
$\nabla_\mu T^{\mu\nu}=0$), and the document pins. Tier BM.4 is new canon
content with no first edition, so its pins resolve against Part 4 directly.

`verify_H_calibration_lock.py` (Tier BM.5 of Part 4, `Def-BM.4` + `BM.13`–`BM.18`):
the calibration layer of the baryomesonic era — the Born width
$\Delta x_{\mathrm B}=\mathfrak h/(E_{\mathrm{int}}\ln2)$ and its quantized sub-hop
ladder, the coherence volume and the density $\rho=(E_{\mathrm{int}}\ln2)^4/\mathfrak h^4$,
the exact trace of CT1.23 giving $R=\kappa^2(\rho-3p)+4\Lambda$ with the
component round trip, the curvature scale $2\pi E^4(\ln2)^3/\mathfrak h^2$ and its
radius, the two lock identities $(\Delta x_{\mathrm B})^2\kappa^2\rho=2\pi E^2\ln2$
and $\Delta x_{\mathrm B}r_s=2G_N$, the crossing gap below the minimal floor, the
neutron row at $E_{\mathrm{int}}=6$ [Census FT.35(2)] and the five-cell family table.
Arithmetic: the exact Laurent-monomial ring $\mathbb Q[\mathfrak h,E,\ln2,\pi]^{\pm}$,
a rational polynomial ring in $(\rho,p,\Lambda,\kappa^2)$ for the frame algebra,
exact rational $\ln2$ enclosures from $\ln2=\sum_{n\ge1}1/(n2^n)$ (tail $<2^{-12}$),
Archimedes' $223/71<\pi<22/7$, and square-comparison inequalities (no radicals in
any assertion). Tier BM.5 is new canon content with no first edition; its pins
resolve against Part 4 directly.

`era_paths.py`: the resolver mapping the legacy letter-series filenames to the
era files (`A_axioms.md` → Part 1 + Part 2; `B_foundation.md` → Part 1;
`C…G` → Part 2; `H…R` → Part 3 + Census + HistLog; `S`/`T` → HistLog). The
content checkers read through it; pins resolve because the theorem mathematics
was transplanted unmodified. It is also the **single place that knows whether
`../H_archive/` is bundled**: `ARCHIVE_PRESENT`, `ABSENT` (the first editions
requested while absent) and `archive_note()`. `read()` yields `""` for an absent
archive document and records it, so a checker that forgot to gate degrades
visibly instead of dying at import time.

`qmath.py`, `q5.py`, `hcommon.py`, `solids.py`, `bypasscore.py`, `compute*.py`,
`audit_heavy_quark_scheme.py`: shared exact-arithmetic helpers (not checkers;
ignored by `run_all.py` discovery).

## The externalized first editions (`H_archive/`)

The 21 bundled first editions were **moved out of this repository** into a
separate historical-archive repository that traces the theory from its roots.
They were the *identity base* of the content checkers: a body of pins asserting
that the transplanted era-canon text still matches the first edition it came
from. Those pins are real verification, so they were **gated, not deleted** —
they are skipped here and run again unchanged wherever the archive is bundled
(in this repo, if `H_archive/` is restored, or in the archive repo's own
checkout).

The mechanism is one shared flag plus one uniform guard:

```python
ARCH = era_paths.ARCHIVE_PRESENT        # era_paths.py: os.path.isdir(../H_archive)

if ARCH:
    H13 = rd("H_archive/H13_registries_and_gaps.md")
    chk("§G ...", "pin" in H13)
```

Each affected checker prints one `NOTE:` line at load when the archive is
absent, naming what was skipped. **15 checkers carry gated first-edition pins:
196 of the 1269 assertions in those files are archive-scoped, and the other
1073 — every assertion about this repository's era canon — runs
unconditionally.** The gating is flow-sensitive: a name is archive-tainted from
a tainted binding until it is rebound, so a loop variable reused later for
era-canon work keeps its checks live; gating a whole `for` loop taints the names
it accumulates, so no downstream assertion runs against a value the skipped loop
never produced. Two mixed statements were split rather than gated, so their
era-canon halves stay live (`E, H13 = rd(…), rd(…)` in
`verify_L_lyapunov.py`, and the conjunctive `Koide` pin in
`verify_H_koide_channel.py`).

`gate_archive_pins.py` is the tool that produced the gating and can re-derive or
extend it. It is not a checker (`run_all.py` ignores it). It computes the taint
flow-sensitively over the AST, groups the archive-dependent statements into
contiguous runs, wraps each run in `if ARCH:` at the statement's own indentation,
and refuses to write unless three audits pass: every run parses, no two runs
overlap, no gated chk references a name bound from an era-canon read
(over-taint), and no name bound inside a gate is referenced outside one
(scope-aware, allowing parameters, prior ungated rebindings and
comprehension locals). `--apply` writes; without it the tool is a dry run.

Everything the suite verifies about **this** repository — the era canon's
mathematics, structure, citation graph and hygiene — is unaffected and still
runs unconditionally.

## Retired

`verify_H_format.py` — the whole-layer format validator of the split canon
H01–H21 (tier order, tag uniqueness and completeness, per-theorem block
presence, citation closure, `$$` balance, artifact scan, the P-H registry rows,
the gap log, the part headers). **Every one of its checks read the concatenation
of the 21 first editions**, so externalizing `H_archive/` left it no subject matter
in this repository. Its coverage is not lost: `check_format.py` and
`verify_era_structure.py` enforce the same properties — block completeness,
citation closure, `$$` and brace balance, tag ownership, declaration hygiene —
against the era canon, which is now the sole authority here.

`verify_H_rung_closure.py` — the consolidation-law checker of the letter-series
canon (byte-identity with the first editions, letter ownership, S/T parses).
Its object no longer exists in the canon; the era laws are checked by
`verify_era_structure.py`. Retirement recorded in `../HistLog.md` §V (including
the one-character whitespace drift it had detected between `H_archive/H01` and
the consolidated FT.6 line — HistLog §0.4(a)).
