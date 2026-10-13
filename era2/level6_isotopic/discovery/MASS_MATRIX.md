# MASS_MATRIX.md — the session-13h working record (Tier IT.12 candidate, IT.37–IT.39)

**Directive (Architect, session 13h).** *"Formalize the Mass Matrix Object and Explore Its Tensor Product
Structure … a 2×2 Hermitian matrix with the Lyapunov mass (informational) and the rung-1 seal mass on the
diagonal, and the off-diagonal coupling … carrying complex phases … When tensored with itself, 16 components
map onto the C²⊗C² force decomposition (AT.59) … identify new content or redundancy. If redundant, state
that honestly. If it conflicts with existing bars, state the exact tension."*

**Machine.** `checks/mass_matrix.py` → **13/13 EXACT**, no floating point, no measured value (Gauss(i) over
`Fraction`).

---

## 0. Stance

The directive invites an honest redundancy/tension verdict, so this record separates **what is exact and
constructible** (the linear algebra) from **what is imported or undeclared** (the off-diagonal parameters)
and **what is redundant** (the force/Pauli structure the corpus already has).

## A. The algebra is exact and correct (→ IT.37)

$M=\begin{pmatrix}m_L & w\\ \bar w & m_S\end{pmatrix}$ on $H_\omega=\mathbb C^2$ [Def-H.33], $w=m_{\rm off}e^{i\Delta\theta}=a+bi$:

- **Hermitian** ($M=M^\dagger$) for real $m_L,m_S$ and conjugate off-diagonals — verified on 4 Gauss(i) witnesses.
- **Pauli decomposition** $v_\mu=\mathrm{Tr}(M\sigma_\mu)$ — the directive's four identities verified **exactly**:
  $v_0=m_L+m_S$, $v_3=m_L-m_S$, $v_1=2a=2m_{\rm off}\cos\Delta\theta$, $v_2=-2b=-2m_{\rm off}\sin\Delta\theta$; all $v_\mu$ real.
- **Eigenvalues** $\lambda_\pm=\tfrac12[(m_L+m_S)\pm\sqrt{(m_L-m_S)^2+4m_{\rm off}^2}]$ (char. poly
  $\lambda^2-(m_L{+}m_S)\lambda+(m_Lm_S-|w|^2)$; discriminant $\ge0$).

## B. The tensor product, and the 16-vs-8 over-count (→ IT.38)

- **$C_{\mu\nu}=\mathrm{Tr}((M\otimes M)(\sigma_\mu\otimes\sigma_\nu))=v_\mu v_\nu$** — verified entrywise on all
  16 $(\mu,\nu)$ by explicit 4×4 multiplication. Named components: $C_{00}=(m_L{+}m_S)^2$, $C_{33}=(m_L{-}m_S)^2$,
  $C_{11}{+}C_{22}=4m_{\rm off}^2$, $C_{03}=m_L^2{-}m_S^2$, $C_{12}=-2m_{\rm off}^2\sin 2\Delta\theta$.
- **The over-count (P3):** the 16 $\sigma_\mu\otimes\sigma_\nu$ span the full 16-dim $\mathrm{End}(\mathbb C^4)$, but
  **AT.56 established the derived force algebra is 8-DIMENSIONAL** — $\mathrm{span}\{I_4,\sigma_i\otimes I_2,
  \sigma_i\otimes\hat\kappa,I\otimes\hat\kappa\}=1{+}3{+}3{+}1$, *"zero new operators."* So **8 of the 16 lie
  outside the derived force algebra** — they are not force channels. "16 components map onto the force basis"
  over-counts by 8; the specific $C_{\mu\nu}\to$force identifications (incl. "$C_{12}\to$ CP-violating mixing")
  are **stipulations**, not derived rows.

## C. Consistency and redundancy (→ IT.38/IT.39)

- **(P2) REDUNDANT:** $M$ is the **same species** as **BM.22's static force matrix** $F_{\rm ext}(\mathbf c,q)=
  h(\mathbf c)\otimes I_2+q\,I_2\otimes\hat\kappa$ — a Hermitian operator on the 2-dim carrier with a diagonal
  ($h$) and an off-diagonal flipping block ($q\hat\kappa$, splitting $2|q|$). $M$ **replaces the derived charge
  read $q$ with the undeclared $m_{\rm off}e^{i\Delta\theta}$**. The Pauli/tensor structure is AT.56–58's anatomy.
- **(P1) THE UNDECLARED SLOTS (the exact tension):** $m_{\rm off}$ and $\Delta\theta$ are **not derived reads**.
  $\Delta\theta$ is neither the winding $\Theta$ ($[\Theta]=\mathfrak q$) nor the defect angle $\Theta_R$
  ($[\Theta_R]=\mathfrak q^0$) — *"the two angles are kept apart … not proportional on a dimension count"*
  [HistLog]. Introducing them as free parameters is a **P4-class addition / a logged declaration** [BM.6(4)
  precedent] — **none issued**. So $M$ is a **parametric construction class**, not a derived row.
- **The currency is clean on the diagonal:** $m_L$ (informational/"Lyapunov") and $m_S$ (rung-1 seal,
  $E_{\rm int}=2\Rightarrow 2\ln2/\mathfrak h$) are **both** $m=E_{\rm int}\ln2/\mathfrak h$ reads [FT.44(4)] —
  same currency, **no BM.83 mix**. The off-diagonal's currency is undeclared.

## D. The over-claims refuted, and the verdict (→ IT.39)

- **(P4) "unified origin for the forces" — NO:** the forces are derived separately (the rung activation AT.50;
  the Pauli anatomy AT.56–58, $\sigma^{ab}=-2\varepsilon_{abc}W_c^{\rm ext}$ magnetic / $\sigma^{a4}=
  (\sigma_a\otimes I_2)\gamma_{F_0}$ electric). A 2×2 mass matrix **repackages**, it does not unify.
- **"explains the BEC statistics (4ℤ vs 2ℤ)" — NO:** the statistics is the multiplicative exchange
  $\varepsilon=(-1)^A$ [BM.128(7); IT.31(4)], a **winding-parity** read, not a mass-matrix eigenvalue.
- **"connects to IT.10" — only trivially** (both involve mass reads).

**VERDICT:** $M$ is **constructible** and its algebra is **exact**, but it **adds no new derived content** —
it is **REDUNDANT** with BM.22's force matrix + AT.56–58's Pauli anatomy, **PARAMETRIC** in two undeclared
slots ($m_{\rm off},\Delta\theta$), and its 16-component force map **over-counts** the 8-dim derived algebra.
It is consistent with the corpus only as a **parametric construction class** whose derived content already
exists. Recorded honestly; **not adopted; no declaration issued.**

**Declarations issued: none. §Cal-IT empty.** No species identified; no measured value [P5] ($m_L,m_S,m_{\rm
off}$ are ledger reads/slots, not SM masses; $\Delta\theta$ structural, unmeasured); prices not masses; no
currency mixing; Level-5 and IT.1–IT.11 cited, never edited.

## Check ledger (`mass_matrix.py`, 13/13)

| § | checks | content |
|---|---|---|
| A | A1, A2, A3, A2x | Hermiticity; the Pauli decomposition (the four identities); the eigenvalues; + adversarial |
| B | B1, B2, B3 | $C_{\mu\nu}=v_\mu v_\nu$ (explicit 4×4); the named components; the 16-vs-8 force-algebra over-count |
| C | C1, C2, C3 | redundancy with BM.22's $F_{\rm ext}$; the undeclared slots ($m_{\rm off},\Delta\theta$); the diagonal currency |
| D | D1, D2, D3 | the over-claims refuted; the REDUNDANT+PARAMETRIC verdict; the status |

**Open rows after IT.12:** unchanged — IT-O1 (transit dynamics), IT-O2 (the binding value), IT-O3, IT-O5
(static side closed), the owed route choice, the deferred Calibration Era. **No new row** (the mass matrix is
a parametric construction class, recorded not adopted). **IT-O4 stays CLOSED.**
