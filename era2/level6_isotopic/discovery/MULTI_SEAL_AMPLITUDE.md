# MULTI_SEAL_AMPLITUDE.md — the session-13d working record (Tier IT.8 candidate, IT.25–IT.27)

**Directive (Architect, session 13d).** *"Construct the N≥4 Multi-Seal Configuration Calculus (the
amplitude side, IT-O2) … Evaluate the flicker ensemble amplitude over the g(N) grouping sectors for
N=5,6,9, incorporating the (−1)^ℵ dressing, the winding revival ladder, and the rational residue
attenuation. Determine if the amplitude-weighted ensemble binding is negative (bound) or positive
(unbound/resonance) at N=9 … Close IT-O2 and IT-O5 (or name the exact remaining obstruction). If the
amplitude sum cannot be computed exactly for N=9, provide a rigorous inequality bound proving its sign
based on the N=5,6 precedents."*

**Machine.** `checks/multi_seal_amplitude.py` → **20/20 EXACT**, no floating point, no external datum.

---

## 0. Premise audit — the register conflation (the load-bearing finding)

The directive's Steps 2–4 ask for "the amplitude sum over the g(N) grouping sectors, with the
(−1)^ℵ dressing per sector." The canon says these are **two independent registers**:

- **The colour-sealing grammar g(N)** = the (a,b) partitions of N attachments into δ/ε contraction
  groups [Def-BM.9(3)]. **AT.41(3): "the strong seal is a COLOUR partition, INDEPENDENT of the edge
  signs … the seal GATES the read without constraining its value."** It acts downstream as a 0/1
  projector Π_C [Def-BM.9(2)], and **"no clause sums over sealings of a fixed support as if they were
  alternatives"** [Def-BM.9(5)]. Every g(N) grouping is sealed (𝒞=1, no lone attachment), so they gate
  *uniformly* — a multiplicity, not distinct amplitude weights.
- **The Def-H.32 amplitude** $Z^{\rm amp}_B(q,S)=\sum_{\Gamma\in\mathcal G_B}\sum_R v_\Gamma(R)\#\{\text{instances}\}$,
  indexed by **(charge q, winding S)** over the **budget-B configuration space** [Def-H.32(5)];
  $v_\Gamma(R)=2^{|R|}(-1)^{\sum\kappa}$ on covers, else 0 [FT.67(2); Def-H.32(2)]. Frozen census: **B=4** [FT.106(3)].

⟹ **"the amplitude over the 1540 grouping sectors" is ill-posed.** The amplitude is not decomposed by
the colour grouping; the grouping is an independent gating register.

Three further corrections:
- **The (−1)^ℵ dressing is q-locked, not grouping-locked.** AT.53(5): $(−1)^\aleph=\prod_{e:\mathrm{cov}(e)\,\mathrm{odd}}\sigma_e$
  — a function of the **cover and signs**; single open chains give $(−1)^{|q|}$. The grouping (a,b) is
  not an argument.
- **The resolvent $R_k$ is channel-indexed, not N-indexed.** AT.54 Rmk: *"the channel count k is the
  connector floor's **pair count** [BM.137(1)] — configuration data, not a spin read."* So $R_k$,
  $a_{k,d}$, $c_k$ are functions of the two-body channel count, **not** the attachment count N.
  "R_k for the N=5, N=6 mixed grammars" mis-indexes it.
- **The composed supports are constructed — but only their cardinal/geometric reads.** Census FT.50(5)
  gives the N=4 double-triangle (E_int=10) and the N=5 bowtie (E_int=12); FT.50(1) gives the
  **informational additivity** under bridged composition. None is the amplitude $Z^{\rm amp}$.

---

## A. What CLOSES (IT-O2 advanced)

**A1. The sector decomposition + colour-statistics map (Step 1) — exact.**

| N | g(N) | (a,b) blocks | 4ℤ (pure-ε, baryon-type) | 2ℤ (δ-containing) |
|---|---|---|---|---|
| 5 | 10 | (1,1):10 | **0** | **10** |
| 6 | 25 | (3,0):15, (0,2):10 | **10** | **15** |

The directive's "at N=6: 10 sectors in 4ℤ, 15 in 2ℤ" is **confirmed exactly** [IT.6(6); BM.31(2),(4)].

**A2. The composed cells from the gluing law** [Census FT.50(4): $E_{\rm int}=E^{(1)}_{\rm int}+E^{(2)}_{\rm int}-|E_{\rm dir}(G)|$]:
- **N=5 bowtie** (two triangles sharing one vertex, $|E_{\rm dir}(G)|=0$): $E_{\rm int}=6+6-0=12$, 5 slots ⟹ $g(5)=10$;
- **N=4 double-triangle** (glued along a bidirectional channel, $|E_{\rm dir}(G)|=2$): $E_{\rm int}=6+6-2=10$, 4 slots ⟹ $g(4)=3$.
Both match FT.50(5)'s frozen values.

**A3. The informational additivity** [FT.50(1), frozen]: $E_{\rm int}(\Sigma)=2E_1+2E_2+2m$ ⟹ the 1p-kn
tree $E_{\rm int}=6(k{+}1)+2k=8k{+}6$, so $\mathcal B_{\rm info}=-2k\,u<0$ for **every** $k\ge1$ — it flags
the deuteron (k=1) "unbound" exactly as k=3. **The informational read cannot adjudicate the cutoff**
(re-confirms IT.18/IT.20 with FT.50(1)'s frozen citation).

**A4. The channel resolvent + rational attenuation** [AT.44; AT.52]: $R_k(z)=c_k+\sum_d a_{k,d}/(1-d^2z)$,
$a_{k,d}=2^{1-k}\binom{k}{(k+d)/2}$, $c_k=2^{-k}\binom{k}{k/2}$ [k even]; the sum rule $c_k+\sum_d a_{k,d}=1$
holds for k=1..8; the **contact diversion** $c_k=(\tfrac12,\tfrac38,\tfrac5{16},\tfrac{35}{128},\tfrac{63}{256})$
at k=2,4,6,8,10, and $c_k=0$ at odd k — an even channel count moves an exact rational fraction off the
pole ladder.

**A5. The ℵ-excess means, re-derived** [AT.54(1)]: $\langle\aleph\rangle^{(n)}=\sum_j\binom nj p^ju^{n-j}g(2j)/(1-u^n)$,
$g(2)=|q|$, $g(2j)=\tfrac{2j-1}{2}$ — at detailed balance $\varepsilon_q=\tfrac18$ (u=p=½):
$\langle\aleph\rangle^{(2)}=\tfrac76$ (excess $\tfrac16$), $\langle\aleph\rangle^{(3)}=\tfrac{10}7$ (excess $\tfrac37$).
The dressing **magnitude** fluctuates as exact rationals; its **sign** is q-locked.

**A6. The N=3 amplitude census, re-derived** [FT.106(3); BM.28(4)(iii)]: $Z^{\rm amp}(0,0)/Z^{\rm amp}(\pm1,0)=5336/1196=\mathbf{58/13}$;
$Z^{\rm amp}(0,1)/Z^{\rm amp}(\pm1,1)=4796/802=\mathbf{2398/401}$; the **amplitude death of $k\ge2$**
($Z^{\rm amp}(q,2)=Z^{\rm amp}(q,3)=0$ — no cover contains a 4-cycle; odd cycles never enter covers).
The amplitude layer is **sparse** and sectored by (q,S), not a sum over groupings.

---

## B. What does NOT close (IT-O5 open) — the exact obstruction

The N=9 ensemble binding sign needs **three constructions the record lacks**:

1. **the composed-support Def-H.32 amplitude configuration space** at N=9 — the covers / $v_\Gamma$ for
   the multi-junction support, **beyond the frozen B=4 census** [FT.106(3)];
2. **the connector's amplitude weight $v_\Gamma$** — IT.6 derived its E_int (+2) and winding (d=0), **not** $v_\Gamma$;
3. **the multi-junction ensemble binding FUNCTIONAL** — BM.21 is 3-constituent, BM.137 is two-chain; the
   composed support's sector mass $m^2_B$ [Def-H.32(6)] is not constructed.

**No inequality bound is available** (the directive's fallback): there is no N=5/N=6 amplitude-binding
*precedent* to bound from — the same three constructions are missing there. And **every constructed
binding read is ≤ 0** (BM.21(4) B<0; BM.137(3) 𝓑_ens≤0; FT.50(1)/IT.18 disjoint B_info=0; IT.20 bridged
−2ku<0), so the directive's hypothesized **"≥ 0 unbound at N=12" has NO derived support** — the partial
evidence points the *other* way (toward bound). The isotope cutoff remains a **conjecture** [P5: no
measured width/mass enters].

---

## Check ledger (`multi_seal_amplitude.py`, 20/20)

| § | checks | content |
|---|---|---|
| A | A1, A2, A2x, A3 | the N=5/N=6 sector decomposition + colour-statistics map; the composed cells from the gluing law |
| B | B1, B2 | FT.50(1) additivity ⟹ B_info=−2ku<0 uniformly; the informational read cannot adjudicate |
| C | C1, C2, C3, C1x | the channel resolvent R_k, residues, sum rule, contact attenuation; the index discipline (k=pair count); + adversarial |
| D | D1, D2, D2x | the register separation (dressing has no (a,b) argument); the ℵ-excess means 1/6, 3/7 re-derived; + adversarial |
| E | E1, E2, E3 | the N=3 amplitude census (58/13, 2398/401); the amplitude death of k≥2; the (q,S) sectoring |
| F | F1, F2, F3, F4 | IT-O2 advanced; IT-O5 open with the three-construction obstruction; every constructed read ≤0; the adjudication |

**Declarations issued: none. §Cal-IT empty.** No species identified; no measured value [P5]; prices not
masses; Level-5 and IT.4–IT.7 cited, never edited.

**Open rows after IT.8:** IT-O1, **IT-O2 (advanced — the sector statistics, composed-cell geometry,
channel resolvent, and N=3 amplitude census are built; the multi-junction amplitude configuration
space is not)**, IT-O3, **IT-O5 (open — gated on the three constructions at §B)**, the owed route
choice; **IT-O4 stays CLOSED**.
