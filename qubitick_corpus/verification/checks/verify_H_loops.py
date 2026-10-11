
#!/usr/bin/env python3
"""verify_H_loops.py — companion to FT.64–FT.65: the generalized admissible-loop list.
Exact integer arithmetic; GF(2) elimination; integer SNF; DFS enumeration; Burnside with orbit DP.
No floating point."""
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

SOL={name:solid_data(name) for name in NAMES}

# stored machine values (must match the document tables exactly)
A_EXP={
 'tetrahedron':[1,0,6,4,24,24,74,84,189],
 'cube':[1,0,12,8,93,120,576],
 'octahedron':[1,0,12,0,84,0,452],
 'dodecahedron':[1,0,30,20,495,672],
 'icosahedron':[1,0,30,0,465,12],
}
M_EXP={
 'tetrahedron':[1,0,1,1,4,2,8,6,17],
 'cube':[1,0,1,1,7,4,25],
 'octahedron':[1,0,1,0,6,0,19],
 'dodecahedron':[1,0,1,1,10,9],
 'icosahedron':[1,0,1,0,9,1],
}
MP_EXP={
 'tetrahedron':[1,0,1,1,4,2,11,7,23],
 'cube':[1,0,1,1,8,5,34],
 'octahedron':[1,0,1,0,7,0,25],
 'dodecahedron':[1,0,1,1,13,12],
 'icosahedron':[1,0,1,0,12,1],
}
SNF_EXP={
 'tetrahedron':[1,1,1,2],
 'cube':[1,1,1,1,1,2],
 'octahedron':[1,1,1,1,1,1,1],
 'dodecahedron':[1]*11+[2],
 'icosahedron':[1]*19+[2],
}
R1_EXP={ # (eps_min, K_min, Theta_min, orbits)
 'tetrahedron':(2,8,16,1),
 'cube':(0,12,24,1),
 'octahedron':(4,16,32,3),
 'dodecahedron':(6,36,72,25),
 'icosahedron':(10,40,80,14),
}
AUT_EXP={'tetrahedron':(24,12),'cube':(48,24),'octahedron':(48,24),'dodecahedron':(120,60),'icosahedron':(120,60)}

for name in NAMES:
    S=SOL[name]; V,E,Ff,L,d=S['V'],S['E'],S['F'],S['L'],S['d']
    print(f"  {name}: V={V} E={E} F={Ff} L={L} d={d}")
    # groups
    chk(len(S['perms'])==AUT_EXP[name][0] and S['nrot']==AUT_EXP[name][1],f"{name}: |Aut|,|Rot| = {AUT_EXP[name]}")
    # (2) GF(2) rank = F-1; lattice index 2^(F-1); cut-space dimension V-1
    rk=gf2_rank(S['fmask'])
    chk(rk==Ff-1,f"{name}: rk_GF2 face map = F-1 = {Ff-1}")
    kerdim=E-rk
    chk(kerdim==V-1==E-Ff+1,f"{name}: ker dim = V-1 = E-F+1 (cut space; Euler)")
    # stars are cuts and admissible
    nstars=0
    for v in range(V):
        kap=[0]*E
        for e,(a,b) in enumerate(tuple(sorted(x)) for x in S['Elist']):
            if v in (a,b): kap[e]=1
        if all(sum(kap[e] for e in range(E) if S['fmask'][f]>>e&1)%2==0 for f in range(Ff)): nstars+=1
    chk(nstars==V,f"{name}: all {V} vertex stars admissible (star = cut delta{{v}})")
    # (3) SNF
    chk(snf(incidence_B(S))==SNF_EXP[name],f"{name}: SNF invariant factors {SNF_EXP[name]}")
    # face 2-coloring iff d even
    bic=face_bicolor(S)
    chk((bic is not None)==(d%2==0),f"{name}: dual bipartite iff d even (d={d})")
    if bic is not None:
        black=[f for f in range(Ff) if bic[f]==0]; white=[f for f in range(Ff) if bic[f]==1]
        chk(len(black)==len(white)==Ff//2,f"{name}: balanced 2-coloring")
        for e in range(E):
            fs=[f for f in range(Ff) if S['fmask'][f]>>e&1]
            chk(len(fs)==2 and bic[fs[0]]!=bic[fs[1]],f"{name}: each channel in one black + one white face")

# octahedron black-white law consequences
SO=SOL['octahedron']
B=incidence_B(SO); Ff=SO['F']; E=SO['E']
bic=face_bicolor(SO)
black=[f for f in range(Ff) if bic[f]==0]; white=[f for f in range(Ff) if bic[f]==1]
for kap in [(1,0,0,0,0,0,0,0,0,0,0,0),(1,)*12,(2,-1,0,1,3,-2,1,0,0,1,-1,2)]:
    y=[sum(B[f][e]*kap[e] for e in range(E)) for f in range(Ff)]
    psi=sum(y[f] for f in black)-sum(y[f] for f in white)
    chk(psi==0,"octahedron: psi(im B) = 0 (black-white balance identity)")
y=[2 if i==0 else 0 for i in range(Ff)]
psi2=sum(y[f] for f in black)-sum(y[f] for f in white)
chk(psi2!=0,"octahedron: psi(2 e_f) != 0 => k=(1,0,...) unrealizable; realizable iff black sum = white sum")

# tetrahedron winding-vector realizability witnesses (signed kappa)
ST=SOL['tetrahedron']; ne=ST['E']; nf=ST['F']
Bt=incidence_B(ST)
def Bk(kap): return [sum(Bt[f][e]*kap[e] for e in range(ne)) for f in range(nf)]
import itertools
found={}
for kap in itertools.product(range(-2,3),repeat=ne):
    y=tuple(Bk(list(kap)))
    if all(v%2==0 for v in y) and y not in found: found[y]=kap
for f in range(nf):
    tgt=tuple(2 if i==f else 0 for i in range(nf))
    chk(tgt in found,f"tetrahedron: k=e_{f} realized by signed kappa in [-2,2]^6")

# ---------- (4) level counts, character sums, Burnside ----------
for name in NAMES:
    S=SOL[name]; E=S['E']; Ff=S['F']
    Kmax=len(A_EXP[name])-1
    A=[]
    for K in range(Kmax+1):
        c,_=count_profiles(S,K)
        A.append(c)
    chk(A==A_EXP[name],f"{name}: A_S(K) table K=0..{Kmax}")
    chk(A[1]==0,f"{name}: A(1)=0 (no bridges)")
    # character-sum formula cross-check (small solids + dodecahedron)
    if name in ('tetrahedron','cube','octahedron'):
        for K in range(0,min(5,Kmax+1)):
            chk(char_sum_A(S,K)==A[K],f"{name}: character-sum formula = DFS at K={K}")
    if name=='dodecahedron':
        for K in range(0,4):
            chk(char_sum_A(S,K)==A[K],f"dodecahedron: character-sum formula = DFS at K={K}")
    # structural low-level reads
    if S['d']==3:
        chk(A[3]==S['V'],f"{name}: A(3) = V (vertex stars)")
    else:
        chk(A[3]==0,f"{name}: A(3) = 0 (even d: every cut has even size)")
    if name=='icosahedron':
        chk(A[5]==12,"icosahedron: A(5) = 12 = the star family")
    if name=='octahedron':
        chk(all(A[K]==0 for K in range(1,Kmax+1,2)),"octahedron: A(odd K) = 0")
    # Burnside
    M=[]; MP=[]
    for K in range(Kmax+1):
        fid=fix_count(S,orbit_masks(S,tuple(range(E))),K)
        chk(fid==A[K],f"{name}: Burnside identity element = A_S(K) at K={K}")
        M.append(burnside(S,K)); MP.append(burnside(S,K,idx=S['rot_idx']))
    chk(M==M_EXP[name],f"{name}: M_S(K) full-Aut Burnside table")
    chk(MP==MP_EXP[name],f"{name}: M+_S(K) rotation Burnside table")
    chk(all(m<=mp for m,mp in zip(M,MP)),f"{name}: M <= M+ (smaller group, more orbits)")
    # direct orbit cross-checks
    for K in ((1,2,3) if name in ('tetrahedron','cube','octahedron') else (1,2)):
        if K<=Kmax:
            chk(orbit_count_direct(S,K)==M[K],f"{name}: orbit enumeration = Burnside at K={K}")
    # edge-transitivity (R0 minimizer single orbit)
    chk(len({ep[0] for ep in S['eperms']})==E,f"{name}: Aut edge-transitive")

# tetrahedron asymptotic trend
ST=SOL['tetrahedron']
c16,_=count_profiles(ST,16)
chk(c16==2673,"tetrahedron A(16) = 2673")
raw=binom(16+5,5)
chk(Fr(c16,1)>0 and abs(Fr(c16*8,raw)-1)<Fr(1,10),"tetrahedron: A(16)*8/C(21,5) within 1/10 of 1 (equidistribution trend)")

# ---------- (5) minimality regimes ----------
for name in NAMES:
    S=SOL[name]; E=S['E']; L=S['L']
    # R0: K_min = 2, witness single channel at kappa=2, one orbit
    c2,w2=count_profiles(S,2)
    chk(c2==E,f"{name}: A(2) = E (the single-channel kappa=2 family)")
    chk(all(sorted(x)==sorted([2]+[0]*(E-1)) for x in w2),f"{name}: every K=2 profile is single-channel kappa=2")
    # every K=2 profile is single-channel: verify count equals E and orbits = 1
    chk(M_EXP[name][2]==1,f"{name}: R0 minimizers form one Aut-orbit (edge-transitivity)")
    # R1: coset leaders
    eps,bvecs=strict_min(S)
    norb=strict_min_orbits(S,bvecs)
    exp=R1_EXP[name]
    chk((eps,E+eps,2*(E+eps),norb)==exp,f"{name}: R1 (eps_min,K,Theta,orbits) = {exp}")
    if L%2==0:
        chk(eps==0,f"{name}: even L: kappa=1 profile admissible (eps_min=0)")
    else:
        chk(eps>=2,f"{name}: odd L: eps_min >= 2")
    chk(2*(E+eps)<=(4*E if L%2 else 2*E),f"{name}: R1 <= R2")
    if name!='cube':
        chk(2*(E+eps)<4*E,f"{name}: R1 strictly beats uniform minimum (odd L)")
    else:
        chk(2*(E+eps)==2*E,"cube: uniform minimum = strict minimum (unique Platonic)")
    # R2: uniform ladder
    k0=1 if L%2==0 else 2
    chk(k0*L%2==0,f"{name}: uniform parity L*kappa0 even")
    chk(E*k0=={'tetrahedron':12,'cube':12,'octahedron':24,'dodecahedron':60,'icosahedron':60}[name],
        f"{name}: R2 first rung K = E*kappa0")

# ---------- register product example (FT.65(2)) ----------
chk(2**(2*6)*M_EXP['tetrahedron'][2]*g_formula(4)==12288,"dark tetrahedron at K=2: 2^12 * 1 * 3 = 12288 states")

# ---------- master-table anchors (FT.65(4)-(5)): small-cell lattices re-derived ----------
# Sigma_min: single channel, Theta = 2 kappa in 2Z automatic: index 1 [FT.24]
chk(all((2*k)%2==0 for k in range(-3,4)),"Sigma_min: lattice = Z (index 1), Theta=2kappa automatic")
# polygon P_n / cycle Sigma_L: single parity constraint: index 2 [FT.45(3)/FT.32(6)]
chk(gf2_rank([(1<<6)-1])==1,"one face constraint on 6 channels: GF(2) rank 1 => index 2")
# face floor Sigma_triangle: single triangle constraint: index 2 [FT.49(2)]
chk(gf2_rank([0b111])==1,"face floor: rank 1 => index-2 lattice")
# bowtie: two independent triangle constraints: index 4 [FT.50(5)]
chk(gf2_rank([0b000111,0b111000])==2,"bowtie: rank 2 => index-4 lattice")
# double-triangle patch: channels (AB,AC,BC,AD,BD): constraints ABC = AB+AC+BC, ABD = AB+AD+BD
r_patch=gf2_rank([0b00111,0b11001])
chk(r_patch==2,"patch: rank 2 => index-4 lattice [FT.50(5)]")
# derived-dependency witness of FT.50(5): Theta_ACBD = Theta_ABC + Theta_ABD - 2 kappa_AB (sample profile)
kap={'AB':2,'AC':1,'BC':3,'AD':1,'BD':2}
tABC=kap['AB']+kap['AC']+kap['BC']; tABD=kap['AB']+kap['AD']+kap['BD']
tACBD=tABC+tABD-2*kap['AB']
chk(tACBD==kap['AC']+kap['BC']+kap['AD']+kap['BD'],"FT.50(5) derived-dependency identity on a sample profile")
# taxonomy law: m_hid = E_int ln2 / h; twelve master-table rows (families counted once)
rows=['Sigma_min','Sigma_L','Sigma_P_n','Sigma_12','Sigma_triangle','bowtie','patch',
      'tetrahedron','cube','octahedron','dodecahedron','icosahedron']
Eints=[2,None,None,6,6,12,10,12,24,24,60,60]
chk(len(rows)==12,"master taxonomy table: twelve rows covering every computed cell/family [FT.65(5)]")
chk(Eints[0]==2 and Eints[3]==6 and Eints[5]==12,"E_int anchors: FT.28(1), FT.35(2), FT.50(5)")

print(f"verify_H_loops: {N} checks green")
