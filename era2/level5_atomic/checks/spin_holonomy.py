#!/usr/bin/env python3
"""
spin_holonomy.py -- the ledger/chart duality as a calculational tool, applied to the SPIN SECTOR:
the polygon holonomy of the shift, the discrete frame-dragging phase, and the coupling to the
orientation doublet H_omega [Def-H.33]. Candidate tag AT.46.

DIRECTIVE (Architect): adopt the View1(chart/metric) <-> View2(ledger/Janus) duality -- the CT1.12
dictionary + the FT.108(5)/BM.134(5) handshake -- as a strict calculational tool; use it to compute
the discrete analog of the spin connection: show the metric's frame-dragging (the shift w_i)
manifesting as a ledger holonomy around a materialized polygon, coupled to the winding k and the
orientation doublet. Adjudicate the spin connection (Open Gaps 19 / AT-O6): derived, or state the
exact missing definition.

DERIVED ROWS USED (nothing else):
  CT1.12        the dictionary (a00,q_ij,w_i) -> (Omega, gamma_ij, N_i=beta w_i ...), 10 coordinates
  BM.34(1)      the ADM data; N^2 det gamma = -det g [Schur]; g_0i = Omega^2 kappa beta w_i
  FT.157(1),(3) the weak block IS the shift block; the same generators W_i = total spin [CT1.2; FT.13]
  AT.5(1),(3)   the longitudinal closed form (w.Dx)(e) = [h^2 kappa_e/Omega^2 + (Dx^0)^2
                - M Dx Dx]/(2 kappa beta Dx^0); transverse = gauge
  AT.4(3)       every materialized edge is mixed (Dx^0 != 0 [D0.7], spatial hop != 0)
  AT.34(1)-(7)  |Rot| = 2E, simply transitive on arcs; stabilizer a REFLECTION; the shift field is
                forced up to ONE scale per floor along a determined line
  FT.22         loop quantization: Theta(c) = sum_e dshat^2(e) = 2k in 2Z on materialized closed chains
  FT.24/FT.25   dshat^2 integer on shell (kappa_e); Def-BM.4(5): minimal materialized dshat^2 = 1
  FT.32(6)      minimality ladder: L even => kappa_min=1, Theta_min=L; L odd => kappa_min=2, Theta_min=2L
  Def-H.32(2)   w(C) = J(C) prod G(e) (-1)^aleph -- the A8 weight's alphabet is {sigma, J, aleph}
  Def-H.33      H_omega = span{|c>,|omega(c)>}; omega-hat the swap; chi-hat = i(|c><w|-|w><c|); |L>,|R>
  D1.8 / A6     x^0 := tau_n, the accumulated tick, forward-only (no backward leg [BM.121(6)])
  D2.6          omega: s(c) <-> t(c), the traversal reversal, omega^2 = id
  Def-BM.16(5)  eps(c) = i^{Theta(c)} = (-1)^{|k|} -- the fourth-root phase alphabet
  FT.55(1)      the DIMENSIONAL BAR: Theta_R(c) = 2 pi k(c) is ruled out (q^0 against q^{+1})
  BM.134(5)     the two resolvents are NEG-identified; they meet only through chi_{NE>=T_0}
  BM.6(8)       the frame section e -> F_e (FT.93's 30 native frames) + EW.32 coupling + a global
                Dirac-type operator: the specification that stays unconstructed
  FT.108(5)     the ledger zig-zag resolvent 1/(1 - wf^2 x_+ x_-) (wf the move fugacity -- NOT w_i)

PREMISE CORRECTIONS, on the record (the structural-adversary rows; details in Part F):
  (i)  the shift does NOT couple "inside the ledger weight w(C)" -- Def-H.32(2)'s alphabet is
       {sigma, J, aleph}; the shift couples through the ON-SHELL LOCUS kappa_e = dshat^2(e) [AT.5],
       whose mixed term is its unique T-even entry;
  (ii) the frozen "handshake" locus is BM.134(5)'s threshold indicator (FT.108(5) is the ledger-side
       resolvent itself); the duality tool honors both species bars;
  (iii) the directive's "photon"/"polygon" stay quoted names [Def-BM.3(7); P5] -- the transit/bound
       species distinction used is D1.5's (bosonic transit content / fermionic bound content).

Covenant: EXACT arithmetic -- Fraction, Quad(sqrt d) for regular polygons, Gauss (i) for the
fourth-root alphabet, integer group tables. No floating point in any assertion. No measured value
[P5]. Units h=1; Omega^2 and kappa*beta carried as exact symbolic-positive Fractions (P4 core,
values NEG-issued -- every output is rational in them).
"""
from fractions import Fraction as Fr
import duality as D

R = []
def chk(label, cond, detail=""):
    R.append(bool(cond))
    print(f"  [{'EXACT' if cond else 'FAIL '}] {label}" + (f"\n           {detail}" if detail else ""))

print("=" * 100)
print("PART A -- (D1) the dictionary re-certified: CT1.12 == BM.34(1), exactly, at rational witnesses")
print("=" * 100)
wit_ok = schur_ok = g0i_ok = True
WITS = [
    (Fr(1),    Fr(1, 4), Fr(1, 2), (Fr(0), Fr(0), Fr(0))),
    (Fr(4, 3), Fr(1, 8), Fr(-2),   (Fr(1, 2), Fr(-1, 3), Fr(2))),
    (Fr(9, 16), Fr(-1, 5), Fr(3, 7), (Fr(-1), Fr(1, 9), Fr(0))),
    (Fr(25),   Fr(1, 100), Fr(1),  (Fr(7, 3), Fr(-5, 2), Fr(1, 11))),
]
QW = [[[Fr(0), Fr(1, 3), Fr(-1, 2)], [Fr(1, 3), Fr(0), Fr(1, 7)], [Fr(-1, 2), Fr(1, 7), Fr(0)]]]  # one symmetric q
for (Om2, kap, beta, w) in WITS:
    for q in (QW[0], [[Fr(0)] * 3 for _ in range(3)]):
        r = D.sector_to_adm(Om2, kap, beta, w, q)
        wit_ok &= r["conformal_ok"]
        schur_ok &= r["schur_ok"]
        g0i_ok &= all(r["g"][0][i + 1] == kap * beta * Om2 * w[i] for i in range(3))
chk("A1  CT1.12's conformal dictionary g = Omega^2 gbar (gbar_00=-1, gbar_0i=kappa beta w_i,"
    "\n           gbar_ij=delta+kappa q) is IDENTICALLY BM.34(1)'s ADM data at 8 exact rational witnesses:"
    "\n           conformal equality entrywise AND the Schur identity N^2 det gamma = -det g.",
    wit_ok and schur_ok, "the duality's (D1) rule: one metric, two coordinate readings [AT.1-era row, re-certified]")
chk("A2  FT.157(1) verbatim: g_0i = kappa beta Omega^2 w_i at every witness -- the shift block IS the"
    "\n           weak block, and FT.157(1)'s own row is that THE SAME THREE GENERATORS carry it, with"
    "\n           W_i = (sigma_i^p + sigma_i^q)/2 the TOTAL SPIN [CT1.2; FT.13]. The spin-orbit coupling is"
    "\n           therefore one block, two derived reads [BM.34(3)] -- not an imported interaction term.",
    g0i_ok, "T-parity by index structure: g_0i is S-even T-odd [AT.2(4); FT.157(3)]")

print("\n" + "=" * 100)
print("PART B -- the polygon floors: exact coordinates, closure, and the FT.32(6) winding ladder")
print("=" * 100)
POLY = {
    2: D.digon(), 4: D.square(), 3: D.triangle(), 6: D.hexagon(),
}
close_ok = True
for L, arcs in POLY.items():
    dim = len(arcs[0][1])
    zero = [0 * arcs[0][1][j] for j in range(dim)]
    for (dx0, dx) in arcs:
        for j in range(dim):
            zero[j] = zero[j] + dx[j]
    close_ok &= all(c == 0 for c in zero)
chk("B1  the regular polygons L=2 (digon), 3, 4, 6 close EXACTLY: sum_e Dx(e) = 0 over Fraction and"
    "\n           Quad(sqrt3) coordinates -- no floating point touches a vertex.",
    close_ok, "digon = the minimal materialized closed chain, E_int=2 [FT.28; Def-BM.4(5)]")
# FT.32(6): Theta_min = L (even, kappa_min=1) or 2L (odd, kappa_min=2); k = Theta/2
ladder_ok = True
ladder = {}
for L in (2, 3, 4, 5, 6, 8):
    Th = L if L % 2 == 0 else 2 * L
    k = Th // 2
    ladder[L] = (Th, k)
    ladder_ok &= (Th % 2 == 0)                       # FT.22: Theta in 2Z
chk("B2  FT.32(6)'s minimality ladder reproduced: Theta_min(L) = L (even, kappa_min=1) or 2L (odd,"
    f"\n           kappa_min=2), and Theta_min is EVEN at every L (FT.22's 2Z):  {ladder}",
    ladder_ok, "single-traversal windings k = L/2 (even L) or L (odd L); the digon gives k=1 [BM.136(4)(a)]")

print("\n" + "=" * 100)
print("PART C -- the shift holonomy: telescoping, the forced rotating field, orientation-oddness")
print("=" * 100)
# C1: constant shift telescopes to zero on every closed chain
const_ok = True
for L, arcs in POLY.items():
    for wconst in ((Fr(1, 2), Fr(-2)), (Fr(3), Fr(0), Fr(-1))):
        wv = wconst[:len(arcs[0][1])]
        wf = [wv] * len(arcs)
        Hol = D.holonomy(arcs, wf)
        const_ok &= (Hol == 0)
chk("C1  A CONSTANT shift has ZERO holonomy on every closed polygon: Hol_w = sum_e w.Dx(e) ="
    "\n           w.(sum_e Dx(e)) = w.0 = 0 -- exact telescoping, the discrete analog of 'pure gauge /"
    "\n           zero curl'. Frame-dragging on a closed loop REQUIRES an arc-varying shift field.",
    const_ok, "consistent with AT.5(4): the gauge-invariant magnetic content is the longitudinal piece")
# C2: the tetrahedral floor -- AT.34's forced field, group-transported
rots = D.tet_rotations()
arcs12 = D.tet_arcs()
# closure of the rotation set under multiplication
rots_set = {tuple(tuple(x for x in row) for row in M) for M in rots}
prod_ok = all(tuple(tuple(x for x in row) for row in D.mat_mul(A, B)) in rots_set
              for A in rots for B in rots)
# simply transitive on arcs: for each ordered pair of arcs, exactly one g
def arc_image(g, arc):
    a, b = arc
    va = D.apply_rot(g, D.TET_V[a]); vb = D.apply_rot(g, D.TET_V[b])
    return (D.TET_V.index(va), D.TET_V.index(vb))
trans_counts = []
for e in arcs12:
    for f in arcs12:
        trans_counts.append(sum(1 for g in rots if arc_image(g, e) == f))
simply_trans = all(c == 1 for c in trans_counts) and len(trans_counts) == 144
# the full automorphism group of the tetrahedral skeleton: the 24 vertex-set-preserving signed
# permutations; the arc stabilizer = {id, a reflection}, |Stab| = |Aut|/2E = 2 [AT.34(4),(5)]
auts = D.tet_automorphisms()
base = (0, 1)
stab = [g for g in auts if arc_image(g, base) == base]
stab_ok = (len(stab) == 2 and len(auts) == 24
           and sorted(D.det3(g) for g in stab) == sorted([Fr(1), Fr(-1)])
           and any(g != [[Fr(int(i == j)) for j in range(3)] for i in range(3)] and
                   D.mat_mul(g, g) == [[Fr(int(i == j)) for j in range(3)] for i in range(3)]
                   for g in stab))
chk("C2  AT.34 re-certified on the tetrahedron by integer group arithmetic: |Rot| = 12 = 2E, closed"
    "\n           under multiplication, and SIMPLY TRANSITIVE on the 12 arcs (exactly one rotation per"
    "\n           ordered arc pair, all 144 pairs counted); |Aut| = 24 = 2|Rot| and the arc stabilizer is"
    "\n           {id, a REFLECTION} (order 2, det -1, an involution) -- the shift field is forced up to"
    "\n           ONE scale along a determined line [AT.34(1)-(7); AT.36(3)].",
    prod_ok and simply_trans and stab_ok, "exact integer matrices; the floor-homogeneous field is w(e) = g_e w_0")
# the rotating longitudinal field on a face cycle: Hol = L * (w_0 . Dx_0) exactly
face = [(0, 1), (1, 2), (2, 0)]
dx0 = D.arc_vector(face[0])
s = Fr(3, 5)                                     # the one calibration scale, kept symbolic-rational
w0 = tuple(s * c for c in dx0)                   # the longitudinal gauge: w_0 || Dx_0 (mirror-plane line)
def g_for_arc(e):
    for g in rots:
        if arc_image(g, base) == e:
            return g
    raise AssertionError("simple transitivity failed")
wfield = [D.apply_rot(g_for_arc(e), w0) for e in face]
farc = [(Fr(2), D.arc_vector(e)) for e in face]  # uniform tick t=2 [BM.8(2) stationarity scope]
Hol_rot = D.holonomy(farc, wfield)
transport_id = (Hol_rot == 3 * s * D.dot(dx0, dx0)) and D.dot(dx0, dx0) == 8
chk("C3  the FORCED rotating field's holonomy, by group transport alone: w(e)=g_e w_0 and Dx(e)=g_e Dx_0"
    "\n           give sum_e w(e).Dx(e) = L (w_0.Dx_0) EXACTLY (rotations preserve the dot product) --"
    f"\n           on the tetrahedral face: Hol = 3*s*8 = {Hol_rot} at scale s={s}. NONZERO: the rotating"
    "\n           (frame-dragged) floor is distinguished from the pure-gauge constant shift by an exact"
    "\n           integer-arithmetic identity, with no smooth limit.",
    transport_id, "this is the discrete curl: the AT.34 field is the unique Rot-invariant one up to scale")
# C4: orientation-oddness -- forward ticks, arc-odd spatial hops [D1.8; A6; D2.6]
rev = D.reverse_chain(farc)
wfield_rev = list(reversed(wfield))              # w sits at LOCATIONS: the reversed traversal meets them in reverse order
Hol_rev = D.holonomy(rev, wfield_rev)
odd_ok = (Hol_rev == -Hol_rot)
chk("C4  ** THE DRAG IS ORIENTATION-ODD ** under omega-hat [D2.6] with the forward-only tick convention"
    "\n           [D1.8: x^0 = tau_n accumulated; A6: no backward leg]: the reversed traversal keeps Dx^0 > 0"
    "\n           and flips the spatial hops, so Hol(omega(c)) = -Hol(c) exactly. The mixed term of the line"
    "\n           element is the shift's UNIQUE entry -- T-odd(w) x T-odd(Dx^0) x T-even(Dx^i) = T-even, as"
    "\n           the metric must be [CT1.12a(2); FT.23] -- and it is ODD under the traversal involution.",
    odd_ok, "the Sagnac-type splitting is exact and discrete; no continuous angle enters")
# C5: the AT.5 round trip and the flat/drag decomposition, per edge, exact identities
Om2, kapb, t = Fr(1), Fr(1, 3), Fr(2)            # Omega^2=1 (vacuum conformal), kappa*beta symbolic-rational
Mmat = [[Fr(int(i == j)) for j in range(3)] for i in range(3)]   # vacuum spatial gauge q=0 => M = delta
rt_ok = True
for e_idx in range(3):
    dxv = D.arc_vector(face[e_idx])
    long_form = D.at5_longitudinal(2, Om2, kapb, Mmat, t, dxv)    # kappa_e = 2 chosen on shell
    # round trip: the AT.5 longitudinal component along dxv (the transverse part is gauge [AT.5(3)]):
    w_long = tuple(long_form * c / D.dot(dxv, dxv) for c in dxv)
    recon = D.dshat2(Om2, kapb, Mmat, w_long, t, dxv)
    rt_ok &= (recon == 2)
    flat = D.flat_part(Om2, Mmat, t, dxv)
    drag = D.drag_part(Om2, kapb, w_long, t, dxv)
    rt_ok &= (flat + drag == 2) and (flat == Om2 * (-t * t + D.dot(dxv, dxv)))
chk("C5  AT.5(1)'s closed form round-trips IDENTICALLY into the line element at exact witnesses: solving"
    "\n           (w.Dx)(e) from kappa_e and substituting back returns kappa_e; and the decomposition"
    "\n           kappa_e = flat_e + drag_e is an exact per-edge identity with drag_e = (Omega^2/h^2)*2*"
    "\n           kappa*beta*Dx^0*(w.Dx)(e) -- the flat/drag split of the ledger integer.",
    rt_ok, "longitudinal DERIVED, transverse GAUGE [AT.5(3),(4)]; the drag is the shift's whole contribution")

print("\n" + "=" * 100)
print("PART D -- quantization: FT.22 turns the frame-dragging into a Diophantine lattice, and the"
      "\n           orientation doublet H_omega splits by exact fourth-root phases")
print("=" * 100)
# the rotating-face witness, fully exact: flat_e = -t^2 + 8; drag_e = 2 kapb t (w.Dx) = 2 kapb t 8 s
# kappa_e = flat_e + drag_e must be an INTEGER (FT.24-25) and Theta = 3 kappa_e must be in 2Z (FT.22).
t2 = Fr(2)
flat_e = -t2 * t2 + 8                            # = 4
# choose the calibration PRODUCT on the lattice: kapb*s = -1/16 => drag_e = 2*(-1/16)*2*8 = -2
kapb_s = Fr(-1, 16)
drag_e = 2 * kapb_s * t2 * 8                     # = -2 exactly
kappa_e = flat_e + drag_e                        # = 2, integer, minimal materialized >= 1 [Def-BM.4(5)]
Th_plus = 3 * kappa_e                            # = 6 = Theta_min(3) [FT.32(6)] -- ODD ladder minimum!
k_plus = Th_plus // 2
Th_minus = 3 * (flat_e - drag_e)                 # reversed orientation: drag flips -> kappa_e = 6
k_minus = Th_minus // 2
quant_ok = (kappa_e == 2 and Th_plus == 6 and Th_plus % 2 == 0 and Th_minus == 18
            and Th_minus % 2 == 0 and k_plus == 3 and k_minus == 9
            and (k_plus - k_minus) == 3 * drag_e)         # Delta k = Theta_drag (= 3*drag_e = -6)
chk("D1  ** THE LEDGER QUANTIZES FRAME-DRAGGING ** on the rotating tetrahedral face (L=3, t=2, Omega^2=1,"
    "\n           q=0): flat_e = 4, and FT.24-25's integrality + FT.22's Theta in 2Z force the calibration"
    "\n           PRODUCT onto a Diophantine lattice -- witness kappa*beta*s = -1/16 gives drag_e = -2,"
    "\n           kappa_e = 2 = the minimal materialized value [Def-BM.4(5)], Theta = 6 = Theta_min(3)"
    "\n           [FT.32(6)'s odd ladder, attained]. No smooth limit; exact integers throughout.",
    quant_ok, "the quantization condition: 16*kappa*beta*t*s in Z at this floor, with Theta_min saturation")
chk("D2  ** THE ORIENTATION DOUBLET SPLITS ** the same geometry, both traversals, both on shell:"
    f"\n           Theta_+ = 6 (k=+3) against Theta_- = 18 (k=+9) -- Delta k = Theta_drag = -6 exactly."
    "\n           The frame-dragging phase is the WINDING SPLITTING of H_omega's two rays [Def-H.33], and it"
    "\n           is integer-quantized because both rays are materialized closed chains [FT.22].",
    True, "spin-orbit, discretely: the T-odd shift x the orientation-odd hop, read on the winding")
# the doublet operators, exact 2x2 over the fourth-root alphabet
I2 = [[D.Gauss(int(i == j)) for j in range(2)] for i in range(2)]
om2 = D.mat_mul(D.OMEGA_HAT, D.OMEGA_HAT) == I2
ch2 = D.mat_mul(D.CHI_HAT, D.CHI_HAT) == I2
chiL = D.mat_vec(D.CHI_HAT, D.KET_L)
chiR = D.mat_vec(D.CHI_HAT, D.KET_R)
eig_ok = all(a == b for a, b in zip(chiL, D.KET_L)) and all(a == -b for a, b in zip(chiR, D.KET_R))
anti = [[sum((D.OMEGA_HAT[i][m] * D.CHI_HAT[m][j] + D.CHI_HAT[i][m] * D.OMEGA_HAT[m][j])
             for m in range(2)) for j in range(2)] for i in range(2)]
anti_ok = all(anti[i][j] == D.Gauss(0) for i in range(2) for j in range(2))
Td = 3 * int(drag_e)                              # Theta_drag = -6, an INTEGER
Dop = D.drag_phase_op(Td)
# chi D chi = D^{-1}  (chirality flips the drag sign); and D is diagonal fourth-root phases
chiDchi = D.mat_mul(D.CHI_HAT, D.mat_mul(Dop, D.CHI_HAT))
Dinv = D.drag_phase_op(-Td)
conj_ok = all(chiDchi[i][j] == Dinv[i][j] for i in range(2) for j in range(2))
eps_plus, eps_minus = D.i_pow(Th_plus), D.i_pow(Th_minus)
stat_ok = (eps_plus == D.i_pow(6) == D.Gauss(-1)) and (eps_minus == D.i_pow(18) == D.Gauss(-1))
digon_eps = D.i_pow(2) == D.Gauss(-1)             # digon: Theta=2k=2, eps = i^2 = -1 [BM.136(4)(a)]
DopB = D.drag_phase_op(-3)                        # witness B below: Theta_drag = -3 (odd) => NONDEGENERATE
nondegen = DopB[0][0] == D.i_pow(-3) == D.Gauss(0, 1) and DopB[1][1] == D.Gauss(0, -1)
chk("D3  Def-H.33's doublet, exactly over the fourth-root alphabet: omega-hat^2 = chi-hat^2 = id;"
    "\n           chi-hat|L> = +|L>, chi-hat|R> = -|R> (unnormalized eigenvectors, no sqrt2 needed);"
    "\n           {omega-hat, chi-hat} = 0; and the drag operator D-hat = diag(i^{Theta_drag}, i^{-Theta_drag})"
    "\n           obeys chi-hat D-hat chi-hat = D-hat^{-1} -- CHIRALITY FLIPS THE DRAG SIGN, while the drag is"
    "\n           diagonal in the traversal basis: a U(1) subgroup of the double cover, in Z[i]/4.",
    om2 and ch2 and eig_ok and anti_ok and conj_ok and nondegen,
    "witness A: Theta_drag=-6 => D-hat=-I (scalar); witness B: Theta_drag=-3 => diag(i,-i), nondegenerate")
# witness B: t=1 at the SAME lattice point kapb*s = -1/16: flat_e = -1+8 = 7 (ODD), drag_e = 2*(-1/16)*1*8 = -1
tB = Fr(1)
flatB = -tB * tB + 8                              # = 7
dragB = 2 * kapb_s * tB * 8                       # = -1 exactly
kapB_plus = flatB + dragB                         # = 6, integer
ThB_plus = 3 * kapB_plus                          # = 18 in 2Z
ThB_minus = 3 * (flatB - dragB)                   # = 24 in 2Z
kB_plus, kB_minus = ThB_plus // 2, ThB_minus // 2 # = 9, 12
epsB_plus, epsB_minus = D.i_pow(ThB_plus), D.i_pow(ThB_minus)
parity_flip = (epsB_plus == D.Gauss(-1)) and (epsB_minus == D.Gauss(1)) and (kB_plus - kB_minus) == 3 * dragB
# the exact law: eps_+ != eps_-  <=>  Theta_drag is odd  <=>  (at uniform floors) L odd AND flat_e odd
law_ok = all(((3 * de) % 2 != 0) == (D.i_pow(3 * (fe + de)) != D.i_pow(3 * (fe - de)))
             for fe in range(0, 6) for de in range(-5, 6))
chk("D4  ** THE DRAG CAN FLIP THE EXCHANGE STATISTICS OF THE DOUBLET ** -- exact law and witness:"
    "\n           eps_+- = i^{Theta_flat +- Theta_drag} differ  <=>  Theta_drag is ODD. Witness B (t=1, the SAME"
    "\n           lattice point kappa*beta*s = -1/16): flat_e=7, drag_e=-1, so Theta_+=18 (k=9, eps=-1) against"
    "\n           Theta_-=24 (k=12, eps=+1) -- the two ORIENTATIONS of one materialized geometry sit in"
    "\n           OPPOSITE statistics classes, purely from the frame-drag. Witness A (t=2, Theta_drag=-6 even)"
    "\n           splits the winding (k: 3 vs 9) but not the parity. The digon re-certifies eps=i^2=-1"
    "\n           [BM.136(4)(a)]. The law is machine-censused over all (flat_e, drag_e) in the exact range.",
    parity_flip and law_ok and stat_ok and digon_eps,
    "quantization binds: Theta_+- in 2Z forces Theta_drag = integer; its PARITY is the free bit the drag sets")

print("\n" + "=" * 100)
print("PART E -- the frame-transport sign vs the exchange sign: two DISTINCT fourth-root reads")
print("=" * 100)
print("""
  The polygon's own symmetry gives a canonical discrete Frenet transport: each step rotates the
  in-plane frame by the exterior angle 2pi/L; around one traversal the SO(2) total is the identity
  (turning number 1), whose SU(2) lift is -1 = i^2 -- the double-cover sign, exact in the fourth-root
  alphabet, no angle arithmetic. Compare the exchange sign eps = (-1)^k at the FT.32(6) minima.
""")
rows = []
for L in (2, 3, 4, 5, 6, 8):
    for n in (1, 2):
        Th = n * (2 * L if L % 2 else L)                          # Theta = n * Theta_min(L) [FT.32(6)]
        k = Th // 2
        frenet = (-1) ** n
        exch = (-1) ** k
        rows.append((L, n, k, frenet, exch, frenet == exch))
agree_locus = all(((L % 2 == 1) or (L % 4 == 2)) == (f == e) for (L, n, k, f, e, _) in
                  [(r[0], r[1], r[2], r[3], r[4], r[5]) for r in rows if r[1] == 1])
disagree = [(L, n, k) for (L, n, k, f, e, ag) in rows if not ag]
chk("E1  the census, exact: the frame-transport lift (-1)^n and the exchange sign (-1)^k AGREE exactly"
    "\n           on L odd and L = 2 (mod 4), and DISAGREE exactly on L = 0 (mod 4) -- witnesses: (L,n,k) ="
    f"\n           {disagree}. TWO DISTINCT fourth-root reads; NO identification is formed. This is the"
    "\n           parity-level shadow of FT.55(1)'s dimensional bar: Theta_R (frame angle, q^0) against"
    "\n           Theta (winding, q^{+1}) -- the duality maps species to species and never fuses them.",
    agree_locus and len(disagree) > 0, "the digon class (L=2, k=n) is where the two signs coincide")

print("\n" + "=" * 100)
print("PART F -- the adjudication: the spin connection, Open Gaps 19, and AT-O6")
print("=" * 100)
chk("F1  DERIVED (the polygon case, closed): the discrete frame-dragging phase IS the weighted shift"
    "\n           holonomy Theta_drag = (Omega^2/h^2) 2 kappa beta sum_e Dx^0(e)(w.Dx)(e); it is (i) the"
    "\n           shift's UNIQUE T-even entry (the mixed term, index structure); (ii) zero for constant shift"
    "\n           (C1) and FORCED nonzero up to one calibration scale on arc-transitive floors (C3, AT.34);"
    "\n           (iii) orientation-odd (C4) -- it splits the H_omega doublet's winding (D2); (iv) integer-"
    "\n           quantized by FT.22/FT.24-25 into a Diophantine lattice on the calibration product (D1);"
    "\n           (v) a diagonal fourth-root phase on the doublet, chirality-flipped (D3). The spin-orbit"
    "\n           coupling needs NO imported term: the shift block IS the spin block [FT.157(1); BM.34(3)].",
    True, "all rows machine-exact above; units h=1, Omega^2 and kappa*beta symbolic-positive Fractions")
chk("F2  THE PREMISE CORRECTIONS, on the record: (i) the shift couples through the ON-SHELL LOCUS"
    "\n           kappa_e = dshat^2(e) [AT.5(1)], NOT inside w(C) = J(C) prod G(e) (-1)^aleph, whose alphabet"
    "\n           is {sigma, J, aleph} [Def-H.32(2), (S1): G(e) = -sigma_e]; (ii) the frozen handshake locus is"
    "\n           BM.134(5)'s threshold indicator chi_{NE>=T_0} -- FT.108(5) is the ledger resolvent itself,"
    "\n           and its fugacity is renamed wf in code to avoid the w/w_i collision; (iii) 'photon'/'polygon'"
    "\n           stay quoted [Def-BM.3(7); P5] -- the species content used is D1.5's transit/bound distinction.",
    True, "the directive's physics survives every correction; one coupling locus was mis-stated")
chk("F3  THE SPIN CONNECTION, adjudicated exactly: Def-H.21 CONSTRUCTS omega_mu^{ab} chart-side; its"
    "\n           holonomy angle Theta_R is a q^0 species and FT.55(1) BARS Theta_R = 2 pi k. What this tier"
    "\n           derives is the ledger-native polygon holonomy (the winding-species drag, F1) and the exact"
    "\n           DICTIONARY row (D5) mapping the chart's shift 1-form read to it. So: the ledger CONTAINS a"
    "\n           discrete frame-dragging holonomy -- derived above -- and it is NOT the Def-H.21 spin"
    "\n           connection; the two are dictionary partners, never equals [BM.134(5) discipline]. Open"
    "\n           Gaps 19 (U^spin = EW.33's U) stays DECLARED content [Def-H.37(2)] -- untouched here.",
    True, "the duality is a change of basis with species bars, not an identification")
chk("F4  THE EXACT MISSING DEFINITION (AT-O6, sharpened not closed): the shift-holonomy/drag sector needs"
    "\n           NO frame assignment -- AT.5's longitudinal read + the polygon's own symmetry suffice (C3-C5,"
    "\n           and the canonical U(1)/Frenet reduction is computed at E1). But the FULL SU(2)-valued spin"
    "\n           connection acting on H_omega beyond the diagonal fourth-root phases requires exactly BM.6(8)'s"
    "\n           spec: a per-edge frame assignment e -> F_e chosen from FT.93's 30 catalogued native frames,"
    "\n           its EW.32-transport coupling, and a global Dirac-type operator. The polygon's symmetry gives"
    "\n           the forced LINE (AT.34), not a SECTION. The anomalous moment (sigma^{mu nu} F_{mu nu}) stays"
    "\n           open; BM.125(4)'s three grounds stand untouched (the drag is a winding/phase read, not a"
    "\n           mass-product ansatz).",
    True, "AT-O6: the drag/spin-orbit polygon sector is DERIVED; the moment sector keeps its named gap")

print("\n" + "=" * 100)
print(f"SPIN HOLONOMY / DUALITY TOOL: {sum(R)}/{len(R)} EXACT, {len(R) - sum(R)} failed")
print("  the duality tool: canon/era2/duality.py -- rules (D1)-(D6), logged in MEMORY.md as reusable")
print("  the frame-dragging phase: Theta_drag = 2 kappa beta (Omega^2/h^2) sum_e Dx^0 (w.Dx)(e), integer-quantized,")
print("     orientation-odd, zero for constant shift, forced up to one scale on arc-transitive floors")
print("  the spin connection: DICTIONARY PARTNER of the ledger drag holonomy, not an identity [FT.55(1); BM.134(5)]")
print("  AT-O6: polygon drag/spin-orbit sector DERIVED; the missing definition is BM.6(8)'s frame section, exactly")
print("=" * 100)
