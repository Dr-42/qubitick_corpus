# Revision 1 — substitution sheet: removing $\eta$ as an axiomatic input (Part 1)

*Provenance: this is the author's substitution sheet as delivered for the v1.0
packaging pass (revision 1), archived verbatim. It was applied to `canon/` on
2026-10-08 by `source/pipeline/` (see `source/REVISION1_LOG.md` and HistLog
§V.31). Line numbers refer to the as-delivered `Part1_Qubit_era.md` (frozen in
this folder).*

Source read: `Part1_Qubit_era.md` (unchanged). Line numbers below refer to that file. Each block is raw source: **Replace** is what is there now, **With** is what to paste.

Symbols introduced here were checked against the §D table for clashes ($\Theta$, $\Lambda$, $s$, $k$, $\kappa$, $\varepsilon$ are all taken). Rename freely.

| New symbol | Meaning |
| --- | --- |
| $\mathfrak o\in\{0,1,2,3\}$ | the odd-sign slot of $\eta$ |
| $\eta^{(\mathfrak o)}$ | the sign vector with a single $-1$ at slot $\mathfrak o$ |
| $\zeta_i:=\eta^0\eta^i$, $\zeta_0:=1$ | relative signs |
| $\mathsf D_\zeta:\ \sigma_\mu\mapsto\zeta_\mu\sigma_\mu$ | single-qubit Bloch sign map |
| $\mathrm{sf}(X):=\sigma_2X^{\mathrm T}\sigma_2$ | spin flip |

---

## 0. What the substitution does, and what stays free

**Before:** A3 specifies a vector, $\eta=(-,+,+,+)$.
**After:** A3 specifies one structural fact (*exactly one entry of $\eta$ has sign opposite to the other three*). Everything else about $\eta$ is a convention (C13) or a theorem (CT1.0).

What the convention may and may not vary:

| Choice | Free? | Reason |
| --- | --- | --- |
| Overall sign of $\eta$ | **Yes** | $T$ sees only $\eta^\mu\eta^\nu$, so $T[\eta]=T[-\eta]$. This is mostly-plus vs mostly-minus. |
| Which of slots $1,2,3$ is odd | **Yes** | $T^{(1)},T^{(2)},T^{(3)}$ are conjugate by $\mathrm{Ad}_{U\otimes U}$ (relabelling spatial Pauli axes). |
| Odd slot $=0$ vs odd slot $\in\{1,2,3\}$ | **No — a selection** | Different maps: Bloch *inversion* ($\mathfrak o=0$) vs Bloch *reflection* ($\mathfrak o\ge1$). The sector dimensions $(7,3,3,3)$ are identical, but CT1.2's generator table holds only for $\mathfrak o=0$ (CT1.0 Rmk), and only $\mathfrak o=0$ is $\mathrm{SU}(2)$-covariant. |

So "choose any convention and the maths goes through" is true for the sign and for permuting the three spatial slots, but not for moving the odd entry off slot 0. C13 below states the selection openly instead of calling it a free choice. If you want it derived rather than selected, see Option B (§5).

---

## 1. A3 (lines 39–47)

**Replace:**
```markdown
S(\sigma_\mu\otimes\sigma_\nu)=\sigma_\nu\otimes\sigma_\mu,\quad S^2=\mathbb1;\qquad
T(\sigma_\mu\otimes\sigma_\nu)=\eta^\mu\eta^\nu\,(\sigma_\mu\otimes\sigma_\nu),\quad
\eta=(-,+,+,+),\quad T^2=\mathbb1 .
```

**With:**
```markdown
S(\sigma_\mu\otimes\sigma_\nu)=\sigma_\nu\otimes\sigma_\mu,\quad S^2=\mathbb1;\qquad
T(\sigma_\mu\otimes\sigma_\nu)=\eta^\mu\eta^\nu\,(\sigma_\mu\otimes\sigma_\nu),\quad
T^2=\mathbb1;
$$
$$
\eta\in\{\pm1\}^4;\qquad
\exists!\,\mathfrak o\in\{0,1,2,3\}:\ \ \eta^{\mathfrak o}=-\eta^{\mu}\ \ \forall\mu\ne\mathfrak o .
```

(The first `$$ … $$` of A3 is `\mathcal H_p\otimes\mathcal H_q=\vee^2\oplus\wedge^2;`; the second now ends with `T^2=\mathbb1;`, and the new third display carries the sign condition.)

---

## 2. New convention C13 (insert after C12, line 161)

```markdown
**C13.** Signature convention. A3 fixes $T$ only through the products $\eta^\mu\eta^\nu$, and fixes $\eta$ only up to its odd slot $\mathfrak o$ and its overall sign. The corpus takes $\mathfrak o:=0$ (the identity slot $\sigma_0=I_2$, C1) and $\eta^{0}:=-1$, i.e. $\eta:=(-,+,+,+)$ (mostly-plus; D2.1: $\bar g_{00}:=-1$). The overall sign does not change $T$ [CT1.0(2)]; the three choices $\mathfrak o\in\{1,2,3\}$ are conjugate under $\mathrm{SU}(2)$ relabelling of the spatial Pauli axes [CT1.0(4)]; $\mathfrak o=0$ versus $\mathfrak o\ge1$ is the choice of the $\mathrm{SU}(2)$-covariant representative [CT1.0(5)], on which CT1.2's generator table rests [CT1.0 Rmk]. Uses of the representative carry the tag C13. $\neg$ an axiom.
```

---

## 3. §D symbol table (lines 314 and 317, plus two new rows)

**Replace (line 314):**
```markdown
| $S$, $T$ | swap involution; metric-sign involution | A3 |
```
**With:**
```markdown
| $S$, $T$ | swap involution; sign-grading involution ($T=\mathsf D_\zeta\otimes\mathsf D_\zeta$; metric-sign reading: C13) | A3, CT1.0 |
```

**Replace (line 317):**
```markdown
| $\eta$ | signature $(-,+,+,+)$ | A3 |
```
**With:**
```markdown
| $\eta$ | sign vector of the $T$-grading, $\eta\in\{\pm1\}^4$, one odd entry; representative $(-,+,+,+)$ | A3, C13 |
| $\mathfrak o$, $\eta^{(\mathfrak o)}$ | odd-sign slot of $\eta$; sign vector with a single $-1$ at slot $\mathfrak o$ | A3, CT1.0 |
| $\zeta_i$, $\mathsf D_\zeta$, $\mathrm{sf}$ | $\eta^0\eta^i$; Bloch sign map $\sigma_\mu\mapsto\zeta_\mu\sigma_\mu$; spin flip $X\mapsto\sigma_2X^{\mathrm T}\sigma_2$ | CT1.0 |
```

---

## 4. New tag CT1.0 (insert after the heading `## Tier 1A — The Pair Operator Algebra`, line 1032, before `### CT1.1`)

*[The full CT1.0 block — Thm clauses (1)–(5), Req, the symbolic Pf with its
exact-arithmetic justifications, Phys, and the Rmk (what $\mathfrak o\ge1$
would do) — was delivered with the sheet and is applied verbatim; it now
stands in `canon/Part1_Qubit_era.md` at Tier 1A and is reproduced in the
monograph as a Theorem 1.x environment. The Rmk's closing parenthetical
"replace with your `checks/` script" was realized as
`verification/checks/verify_CT10_signature.py`, cited in the Rmk.]*

---

## 5. Option B — derive $\mathfrak o=0$ instead of selecting it (optional)

CT1.0(5) already proves it. To use it, add one clause to A3's new third display:

```markdown
T\,\mathrm{Ad}_{U\otimes U}=\mathrm{Ad}_{U\otimes U}\,T\quad\forall U\in\mathrm{SU}(2)
```

and shorten C13 to: *"The overall sign of $\eta$ is a convention: $\eta^{0}:=-1$, i.e. $\eta:=(-,+,+,+)$ (mostly-plus; D2.1). The odd slot is $\mathfrak o=0$ by CT1.0(5)."*

Trade-off: this turns a selection into a theorem but adds an axiom clause, so you replace one stated choice with one stated input. Option A (sections 1–4) is what you described. Option B is the version where nothing about $\eta$ is chosen except the sign.

*[Not adopted: Option A applied. CT1.0(5) stands as the theorem; C13 states
the selection openly.]*

---

## 6. Downstream edits in Part 1

**CT1.1 Req (line 1038).**
Replace:
```markdown
**Req.** A3; C3; Pauli basis facts:
```
With:
```markdown
**Req.** A3, C13; C3; CT1.0; Pauli basis facts:
```

**CT1.1 Pf, the line that assigns $T=\pm1$ to index pairs.**
Replace:
```markdown
T=+1\iff(\mu,\nu)\in\{0,0\}\cup\{i,j\};\qquad T=-1\iff(\mu,\nu)\in\{0,i\}\cup\{i,0\}
```
With:
```markdown
\eta:=(-,+,+,+)\ [\mathrm{C13}]:\quad T=+1\iff(\mu,\nu)\in\{0,0\}\cup\{i,j\};\qquad T=-1\iff(\mu,\nu)\in\{0,i\}\cup\{i,0\}
```
(Everything above this line in the Pf is unchanged and valid for any $\eta\in\{\pm1\}^4$; the *counts* $(7,3,3,3)$ do not depend on C13, only the naming of which generators fill each block does.)

**CT1.1 Phys (line 1074).** Replace the phrase `metric-sign symmetry ($T$)` with `the sign grading $T$ ($\eta^\mu\eta^\nu$; metric-sign reading by C13)`.

**CT1.2 Req (line 1108).**
Replace: `**Req.** A3; C1, C3; CT1.1.`
With: `**Req.** A3, C1, C3, C13; CT1.0, CT1.1.`

**CT1.2 Pf (lines 1112–1127).** Four justification edits; the $E_0$ line is unchanged because $\eta^0\eta^0=+1$ for any $\eta\in\{\pm1\}^4$.

| Replace | With |
| --- | --- |
| `\eta^i\eta^j=+1\implies E^{ij}\in\mathcal E_{++}` | `\eta^i\eta^j=+1\ [\mathrm{C13}]\implies E^{ij}\in\mathcal E_{++}` |
| `\eta^0\eta^i=-1\implies T=-\implies W_i\in\mathcal E_{+-}` | `\eta^0\eta^i=-1\ [\mathrm{C13}]\implies T=-\implies W_i\in\mathcal E_{+-}` |
| `\eta^j\eta^k=+1\implies T=+\implies J_i\in\mathcal E_{-+}` | `\eta^j\eta^k=+1\ [\mathrm{C13}]\implies T=+\implies J_i\in\mathcal E_{-+}` |
| `\eta^0\eta^i=-1\implies T=-\implies K_i\in\mathcal E_{--}` | `\eta^0\eta^i=-1\ [\mathrm{C13}]\implies T=-\implies K_i\in\mathcal E_{--}` |

**Involution-table tag (lines 1516–1523).**

| Line | Replace | With |
| --- | --- | --- |
| 1516 | `the $T$-grading ($\eta^\mu\eta^\nu$ [A3])` | `the $T$-grading ($\eta^\mu\eta^\nu$ [A3, C13])` |
| 1517 | `=(-1)(-1)\sigma_0\otimes(\sigma_1\sigma_2)` | `=(-1)(-1)\ [\mathrm{C13}]\ \sigma_0\otimes(\sigma_1\sigma_2)` |
| 1523 | `\eta^\mu\eta^\nu\ [\mathrm{A3}]` | `\eta^\mu\eta^\nu\ [\mathrm{A3},\mathrm{C13}]` |

**Native-frames clause (line 1562).**
Replace: `A3's $\eta=(-,+,+,+)$ labels the $T$-grading only [CT1.1]`
With: `the representative $\eta=(-,+,+,+)$ [C13] of A3's sign vector labels the $T$-grading only [CT1.1]`

**Optional (line ~1962).** `\eta_a\eta_b` there is the $T$-eigenvalue of generator $G_a$, not a component of the slot vector $\eta$. Renaming it to $\vartheta_a\vartheta_b$ avoids a reader mixing the two.

*[Applied: both occurrences in L5 renamed.]*

---

## 7. Cross-reference sweep

Convention-range and tag-index updates:

| Line | Replace | With |
| --- | --- | --- |
| 7 | `§B conventions C1–C12` | `§B conventions C1–C13` |
| 7 | `CT1.1–CT1.11b` | `CT1.0–CT1.11b` |
| 9 | `A1–A9, C1–C12, D0.1–D4.3` | `A1–A9, C1–C13, D0.1–D4.3` |
| 393 | `A1–A9 $\wedge$ C1–C12 $\wedge$ D0.1–D4.3` | `A1–A9 $\wedge$ C1–C13 $\wedge$ D0.1–D4.3` |
| 2019 | `A1–A9 · C1–C12 · D0.1–D4.3 · P1–P5` | `A1–A9 · C1–C13 · D0.1–D4.3 · P1–P5` |
| 2021 | `CT1.1–CT1.11 (+CT1.11a/b)` | `CT1.0–CT1.11 (+CT1.11a/b)`, and prepend "signature classification, " to the description |

**Not covered, because only Part 1 was available to me.**

- Grep Parts 2–4, `Census.md` and `HistLog.md` for `\eta`, `(-,+,+,+)` and citations of A3 that rely on the representative; each needs `[C13]` added (CT1.12 metric emergence and the EW/EM sections that use $W_i$, $K_i$, $J_i$ are the likely ones).
- `checks/verify_era_structure.py` regenerates tag indexes and checks citation closure, so it will need CT1.0 and C13 registered.
- Any `checks/` script that hard-codes $\eta=(-,+,+,+)$ should read it from C13 instead.

*[Sweep executed: Part 2 Dep line; Part 3 FT.156(1)/Pf(1)/Phys and FT.158;
Part 4 Dep line, BM.9(2), BM.19 Thm, BM.152 Req; HistLog §III FT.156 row;
corpus README layout rows. CT1.12 (Part 2) and the metric-side `sig(g)`
citations derive the signature from D2.1/det<0 independently of A3's
representative and needed no edit. Registration: `check_format.py` and
`verify_corpus_graph.py` regexes extended to C13; the hard-coded
$\eta=(-,+,+,+)$ uses in the checkers are computational witnesses of the C13
representative and stand; the one A3 document pin
(`verify_H_3p1_chiral_asymmetry.py` §E) was replaced by pins on the revised A3
and on C13.]*
