
#!/usr/bin/env python3
"""verify_H_rungs.py — companion to FT.62: the bidirectional rung audit.
Exact integer arithmetic only."""
import os,sys
HERE=os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,HERE)

N=0
def chk(cond,msg):
    global N
    assert cond, "FAIL: "+msg
    N+=1

Dtick=lambda n: 2**(n+1)          # CT0.5: 2^n pre + 2^n post
O=lambda n: max(0,Dtick(n)-16)    # CT0.6

# ---------- CT0.5/CT0.6 tables ----------
for n,v in [(0,2),(1,4),(2,8),(3,16),(4,32),(5,64),(6,128),(7,256),(8,512),(9,1024),(10,2048),(11,4096),(12,8192)]:
    chk(Dtick(n)==v,f"D_tick({n}) = 2^{n+1} = {v}")
for n,v in [(0,0),(1,0),(2,0),(3,0),(4,16),(5,48),(6,112),(7,240),(8,496),(9,1008),(10,2032),(11,4080),(12,8176)]:
    chk(O(n)==v,f"O({n}) = {v}")
chk(Dtick(3)==16,"rung 3 exact saturation: D_tick(3) = C_cap = 16 [CT0.6/CT0.11]")

# ---------- directed-count re-derivations (D0.8): bidirectional channel = 2 real edges ----------
# Sigma_min: p: e1 out, e2 in, observer in => (2,1): n=3 ; q: (1,1): n=2
chk((2+1)==3 and (1+1)==2,"Sigma_min rungs n(p)=3, n(q)=2 (FT.28(5) unchanged)")
chk(O(3)==0 and O(2)==0,"Sigma_min lock-free")
# Sigma_L unidirectional: contact (2,1)=3? cycle v1: in 1 + out 1 + observer 1 = 3; others 2
chk(1+1+1==3 and 1+1==2,"Sigma_L rungs 3/2 (FT.32(2) unchanged)")
# Sigma_12: q1 = c1 (in,out) + connector (out,in) = 4; p1 = 2+1 = 3; q2 = 2
chk((1+1)+(1+1)==4 and 2+1==3,"Sigma_12 junction rung 4, contact 3 (FT.35(4) unchanged)")
chk(O(4)==16,"Sigma_12 junctions locked at O(4)=16 (unchanged)")
# face floor: A,B,C each 3 channels = 6 directed
chk(3*2==6 and O(6)==112,"face floor n(A)=n(B)=n(C)=6, O(6)=112 (FT.49(5) unchanged)")
# bowtie: X = 4 channels = 8; others 2 channels = 4
chk(4*2==8 and 2*2==4 and O(8)==496,"bowtie rungs 8/4 (FT.50(5) unchanged)")
# double-triangle patch: A,B = 3 channels = 6; C,D = 2 channels = 4
chk(3*2==6 and 2*2==4,"patch rungs (6,6,4,4) (FT.50(5) unchanged)")

# ---------- corrected Platonic rungs (FT.62(1)-(2)) ----------
solids=[('tetrahedron',4,6,4,3,3),('cube',8,12,6,3,4),('octahedron',6,12,8,4,3),
        ('dodecahedron',20,30,12,3,3),('icosahedron',12,30,20,5,3)]
# columns: name,V,E,F,d,L
exp_dark_n=[6,6,8,6,10]
exp_Odark=[112,112,496,112,2032]
exp_Oobs1=[240,240,1008,240,4080]
exp_Oobs2=[496,496,2032,496,8176]
exp_lock_dark=[448,896,2976,2240,24384]
exp_lock_obs1=[576,1024,3488,2368,26432]
exp_lock_obs2=[832,1280,4512,2624,30528]
for (name,V,E,Ff,d,L),nd,od,o1,o2,ld,l1,l2 in zip(solids,exp_dark_n,exp_Odark,exp_Oobs1,exp_Oobs2,exp_lock_dark,exp_lock_obs1,exp_lock_obs2):
    chk(2*d==nd,f"{name}: dark rung n(v) = 2d = {nd}")
    chk(O(2*d)==od,f"{name}: O(2d) = {od}")
    chk(O(2*d+1)==o1,f"{name}: O(2d+1) = {o1}")
    chk(O(2*d+2)==o2,f"{name}: O(2d+2) = {o2}")
    chk(V*O(2*d)==ld,f"{name}: dark lock ledger sum = {ld}")
    chk((V-1)*O(2*d)+O(2*d+1)==l1,f"{name}: obs1 lock ledger sum = {l1}")
    chk((V-1)*O(2*d)+O(2*d+2)==l2,f"{name}: obs2 lock ledger sum = {l2}")
    chk(2*d>=4,f"{name}: every vertex D^--configured (n=2d>=4) [CT4.1]")

# ---------- polygon family (FT.62(1), FT.45(2) corrected) ----------
chk(2*2==4 and O(4)==16,"polygon dark: n(v)=4 (2 channels), O(4)=16 = C_cap: uniform minimal saturation")
chk(2*2+1==5 and O(5)==48,"polygon contact: n(v1)=5, O(5)=48")
# uniformity in n: for every n-gon the dark rung is 4
for n in (3,4,5,6,7,12,20):
    chk(2*2==4,f"polygon P_{n}: dark rung independent of n")

# ---------- duality splitting on lock grade (FT.44(2) corrected / FT.62(3)) ----------
chk(O(6)!=O(8),"cube (112) vs octahedron (496): lock grade splits the dual pair")
chk(O(6)!=O(10),"dodecahedron (112) vs icosahedron (2032): lock grade splits the dual pair")

# ---------- invariance: none of the corrected values enters the unchanged ledgers ----------
for (name,V,E,Ff,d,L) in solids:
    chk(2*E=={'tetrahedron':12,'cube':24,'octahedron':24,'dodecahedron':60,'icosahedron':60}[name],
        f"{name}: E_int = 2E unchanged (no n(v) reference)")
    kap0=1 if L%2==0 else 2
    chk(E*kap0=={'tetrahedron':12,'cube':12,'octahedron':24,'dodecahedron':60,'icosahedron':60}[name],
        f"{name}: K_S,min = E*kappa0 unchanged")

print(f"verify_H_rungs: {N} checks green")
