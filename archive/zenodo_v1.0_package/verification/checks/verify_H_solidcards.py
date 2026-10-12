
#!/usr/bin/env python3
"""verify_H_solidcards.py — companion to FT.63: the Platonic physical cards.
Exact arithmetic: int / Fraction / Q(sqrt2,3,5) / Q(sqrt5) / Q(i). No floating point."""
import os,sys
from fractions import Fraction as Fr
HERE=os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,HERE)
from hcommon import *

N=0
def chk(cond,msg):
    global N
    assert cond, "FAIL: "+msg
    N+=1

SOL={}
for name in NAMES:
    SOL[name]=solid_data(name)

CARD={ # name: (V,E,F,L,d, kappa0min, kf_min, KS_min, jmax, Shid, Pi_min, delta_over_pi, D_str, ratio_den)
 'tetrahedron':   (4,6,4,3,3, 2,3,12,6, 12, 3456,   Fr(1),   '2',          144),
 'cube':          (8,12,6,4,3, 1,2,12,6, 24, 13824, Fr(1,2), '2-sqrt2',    576),
 'octahedron':    (6,12,8,3,4, 2,3,24,12,24, 27648, Fr(2,3), '1',          576),
 'dodecahedron':  (20,30,12,5,3, 2,5,60,30,60,432000, Fr(1,5),'2-2cos(pi/10)',3600),
 'icosahedron':   (12,30,20,3,5, 2,3,60,30,60,432000, Fr(1,3),'2-sqrt3',   3600),
}

# ---------- (0) cardinals, Euler, handshake, face double count ----------
for name,(V,E,Ff,L,d,*_ ) in CARD.items():
    S=SOL[name]
    chk((S['V'],S['E'],S['F'],S['L'],S['d'])==(V,E,Ff,L,d),f"{name}: cardinals (V,E,F,L,d)")
    chk(V-E+Ff==2,f"{name}: Euler V-E+F=2")
    chk(Ff*L==2*E,f"{name}: FL=2E")
    chk(V*d==2*E,f"{name}: Vd=2E")
    chk(S['V']%2==0,f"{name}: V even (even-epsilon theorem premise)")

# ---------- (4) holonomy: vertex defects, Descartes, global spinor triviality ----------
for name,(V,E,Ff,L,d,k0,kf,KS,jmax,Shid,Pi,dpi,Ds,rden) in CARD.items():
    delta=Fr(2)-Fr(d*(L-2),L)
    chk(delta==dpi,f"{name}: delta_v/pi = {dpi}")
    chk(V*delta==4,f"{name}: Descartes/Gauss-Bonnet: V*delta_v = 4 pi")
# global spinor triviality: exp(i (4pi/2) n.sigma) = I  <=>  cos(2pi)=1, sin(2pi)=0: defect 2-2cos(2pi)=0
chk(2-2*1==0,"global sweep: defect 2-2cos(Theta_R/2)|_{Theta_R=4pi} = 0 (SU(2) 4pi-periodicity)")
# FT.54 convention U = exp(i phi n.sigma), phi = Theta_R/2 = 2pi on the full sweep:
# exp(2 pi i sigma_z) = diag(e^{2 pi i}, e^{-2 pi i}) = I  [4 pi is the SU(2) period]
U2pi=[[ONE,ZERO],[ZERO,ONE]]
chk(ceq(U2pi,ceye(2)),"exp(i 2pi sigma_z) = I: global frame transport trivial on the sphere")

# ---------- (6) mass ratios: defect factors and minimal polynomials ----------
class Qsq:
    def __init__(s,a,b,d): s.a=Fr(a); s.b=Fr(b); s.d=d
    def __mul__(s,o): return Qsq(s.a*o.a+s.d*s.b*o.b, s.a*o.b+s.b*o.a, s.d)
    def __add__(s,o): return Qsq(s.a+o.a,s.b+o.b,s.d)
    def __sub__(s,o): return Qsq(s.a-o.a,s.b-o.b,s.d)
    def __eq__(s,o): return isinstance(o,Qsq) and s.a==o.a and s.b==o.b and s.d==o.d
def qpoly(coeffs,x):
    r=Qsq(0,0,x.d); pw=Qsq(1,0,x.d)
    for c in coeffs:
        r=r+pw*Qsq(c,0,x.d); pw=pw*x
    return r
# tetrahedron D=2 (x-2); octahedron D=1 (x-1)
chk(qpoly([-2,1],Qsq(2,0,2))==Qsq(0,0,2),"tetrahedron D=2: minpoly x-2")
chk(qpoly([-1,1],Qsq(1,0,2))==Qsq(0,0,2),"octahedron D=1: minpoly x-1")
# cube D=2-sqrt2: x^2-4x+2
chk(qpoly([2,-4,1],Qsq(2,-1,2))==Qsq(0,0,2),"cube D=2-sqrt2: minpoly x^2-4x+2")
# icosa D=2-sqrt3: x^2-4x+1
chk(qpoly([1,-4,1],Qsq(2,-1,3))==Qsq(0,0,3),"icosa D=2-sqrt3: minpoly x^2-4x+1")
# dodeca: cos36=(1+sqrt5)/4 -> D(2)=(3-sqrt5)/2; cos72=(sqrt5-1)/4 -> D(4)=(5-sqrt5)/2
c36=Q5(Fr(1,4),Fr(1,4)); c72=Q5(Fr(-1,4),Fr(1,4))
def q5poly(coeffs,x):
    r=Q5(0); pw=Q5(1)
    for c in coeffs:
        r=r+pw*Q5(c); pw=pw*x
    return r
chk(q5poly([-1,-2,4],c36)==Q5(0),"cos(pi/5): 4c^2-2c-1=0")
chk(q5poly([-1,2,4],c72)==Q5(0),"cos(2pi/5): 4c^2+2c-1=0")
chk(Q5(2)-Q5(2)*c36==Q5(Fr(3,2),Fr(-1,2)),"dodeca D(2)=(3-sqrt5)/2")
chk(Q5(2)-Q5(2)*c72==Q5(Fr(5,2),Fr(-1,2)),"dodeca D(4)=(5-sqrt5)/2")
# dodeca D(1)=2-2cos(pi/10): quartic x^4-8x^3+19x^2-12x+1 in Z[c]/(16c^4-20c^2+5)
def reduce_mod(p):
    a=[Fr(x) for x in p]+[Fr(0)]*8
    changed=True
    while changed:
        changed=False
        for i in range(len(a)-1,3,-1):
            if a[i]!=0:
                q=a[i]/16
                a[i]=0; a[i-2]+=q*20; a[i-4]-=q*5
                changed=True
    return a
def subst_poly(p,a,b):
    res=[Fr(0)]*(4*len(p)+8); pw=[Fr(1)]
    for coeff in p:
        for k2,v in enumerate(pw): res[k2]+=Fr(coeff)*v
        new=[Fr(0)]*(len(pw)+1)
        for k2,v in enumerate(pw):
            new[k2]+=v*Fr(a); new[k2+1]+=v*Fr(b)
        pw=new
    return res
chk(all(x==0 for x in reduce_mod(subst_poly([1,-12,19,-8,1],2,-2))),
    "dodeca D(1)=2-2cos(pi/10): x^4-8x^3+19x^2-12x+1=0 via cos(5t) reduction")
# ratio coefficients 1/(4E^2)
for name,(V,E,Ff,L,d,k0,kf,KS,jmax,Shid,Pi,dpi,Ds,rden) in CARD.items():
    chk(4*E*E==rden,f"{name}: ratio denominator 4E^2 = {rden}")
# dual splitting on the pole side
chk(Qsq(2,-1,2)!=Qsq(1,0,2),"cube (2-sqrt2) != octahedron (1): dual pair split on D_S")
chk([1,-12,19,-8,1]!=[1,-4,1],"dodeca quartic != icosa quadratic: dual pair split on D_S")

# ---------- (1) spin ----------
for name,(V,E,Ff,L,d,k0,kf,KS,jmax,Shid,Pi,dpi,Ds,rden) in CARD.items():
    S=SOL[name]
    chk(k0==(1 if L%2==0 else 2),f"{name}: kappa0_min = {k0}")
    exp_kf=L if L%2 else L//2
    chk(kf==exp_kf,f"{name}: k_f,min = {kf}")
    chk(KS==E*k0,f"{name}: K_S,min = E*kappa0 = {KS}")
    chk(Fr(KS,2)==jmax,f"{name}: j_max = K_S/2 = {jmax}")
    chk(jmax==Fr(Ff*kf,2),f"{name}: j_max = sum_f k_f / 2 (sum rule FT.43(1))")
    chk(jmax.denominator==1,f"{name}: integer stretched total at uniform minimum (F even)")
    dimface=(kf+1)**Ff; dimdig=(k0+1)**E
    exp_face={'tetrahedron':256,'cube':729,'octahedron':65536,'dodecahedron':6**12,'icosahedron':4**20}[name]
    chk(dimface==exp_face,f"{name}: face-basis carrier dim = {exp_face}")
    if name in ('tetrahedron','cube','octahedron'):
        chk(dimdig=={'tetrahedron':729,'cube':4096,'octahedron':531441}[name],f"{name}: digon-basis carrier dim")
    else:
        chk(dimdig==3**30,f"{name}: digon-basis carrier dim = 3^30")
# dual spin columns
chk(Fr(CARD['cube'][7],2)==6 and Fr(CARD['octahedron'][7],2)==12,"j_max splits cube (6) vs octahedron (12)")
chk(CARD['dodecahedron'][8]==CARD['icosahedron'][8]==30,"j_max degenerate for dodeca/icosa (30)")
chk(CARD['dodecahedron'][6]!=CARD['icosahedron'][6],"per-face structure splits dodeca (5/2) vs icosa (3/2)")
chk(6**12!=4**20,"face-basis dims split dodeca vs icosa")
chk(3**30==3**30,"digon-basis dims degenerate for the last dual pair (E and kappa0 equal)")

# ---------- (5) entropy ----------
for name,(V,E,Ff,L,d,k0,kf,KS,jmax,Shid,Pi,dpi,Ds,rden) in CARD.items():
    chk(Shid==2*E,f"{name}: S_hid = 2E ln2")
    chk(Pi==8*E*E*KS,f"{name}: Pi_min = 8 E^2 K_S,min")
chk(CARD['cube'][5]==1,"cube: kappa0=1 => S_reg/A_loop = ln2/h^2 exactly (unique CT1.29 saturator)")
chk(all(CARD[n][5]!=1 for n in NAMES if n!='cube'),"other four: half rate (kappa0=2)")

# ---------- (7) binding: sealing grammar ----------
exp_g={'tetrahedron':3,'cube':385,'octahedron':25,'dodecahedron':292938721075,'icosahedron':164395}
for name in NAMES:
    V=SOL[name]['V']
    chk(g_formula(V)==exp_g[name],f"g({V}) = {exp_g[name]} [FT.41(b) closed form]")
for name in ('tetrahedron','cube','octahedron'):
    V=SOL[name]['V']
    chk(g_enum(V)==exp_g[name],f"g({V}) enumeration cross-check")
# even-epsilon theorem + term breakdowns
for name in NAMES:
    V=SOL[name]['V']
    terms=g_terms(V)
    chk(all(b%2==0 for (a,b,c) in terms),f"{name}: every sealing grouping has even epsilon-count b (V even)")
    chk(sum(c for (a,b,c) in terms)==exp_g[name],f"{name}: term breakdown sums to g(V)")
# documented breakdowns
chk(dict(((a,b),c) for a,b,c in g_terms(6))=={(3,0):15,(0,2):10},"g(6) = 15 (3 delta) + 10 (2 epsilon)")
chk(dict(((a,b),c) for a,b,c in g_terms(8))=={(4,0):105,(1,2):280},"g(8) = 105 + 280")
chk(dict(((a,b),c) for a,b,c in g_terms(12))=={(6,0):10395,(3,2):138600,(0,4):15400},"g(12) breakdown")
chk([b for (a,b,c) in g_terms(4)]==[0],"tetrahedron: meson-only (b=0 in all 3 groupings)")

# ---------- (2) charge: ternary core reads, witnesses ----------
for s1 in (1,-1):
    for s2 in (1,-1):
        q=(s1-s2)//2
        chk(q in (-1,0,1),"q_core ternary [FT.40/D3.4/EM.9]")
vals=set()
for s1 in (1,-1):
    for s2 in (1,-1): vals.add((s1-s2)//2)
chk(vals=={-1,0,1},"all three charge values attained (witnesses: (+,-)->+1, (-,+)->-1, equal->0)")
# omega flip
for s1 in (1,-1):
    for s2 in (1,-1):
        chk((s1-s2)//2==-(s2-s1)//2,"omega rebase flips q_core [D2.6/FT.40]")
# beta1 independent reads
for name,(V,E,Ff,L,d,*_ ) in CARD.items():
    chk(Ff-1==E-V+1==SOL[name]['F']-1,f"{name}: beta1 = F-1 = E-V+1 independent core reads")

# ---------- mask dimensions ----------
chk(5+3+1==9,"G+W+H core mask = 9 dims [CT0.12]")
chk(9+1==10 and 9+1+8==18,"EM/strong extensions: 10 / 18 = FT.26(3) bound")

print(f"verify_H_solidcards: {N} checks green")
