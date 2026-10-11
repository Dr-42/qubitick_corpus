
#!/usr/bin/env python3
"""verify_H_specification.py — companion to FT.59 / Def-H.22(a) scope / FT.58(1) resolution.
Exact arithmetic over Q(i) only; no floating point."""
import os,sys
HERE=os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,HERE)
from hcommon import *

N=0
def chk(cond,msg):
    global N
    assert cond, "FAIL: "+msg
    N+=1

# ---- CT1.2 basis construction ----
E0=kron2(SIG[0],SIG[0])
SGM=kron2(SIG[1],SIG[1])
for i in (2,3): SGM=cadd(SGM,kron2(SIG[i],SIG[i]))
SWAP=kron2(SIG[1],SIG[1])  # placeholder replaced below
SWAP=[[ZERO]*4 for _ in range(4)]
SWAP[0][0]=ONE; SWAP[3][3]=ONE; SWAP[1][2]=ONE; SWAP[2][1]=ONE
W=[csc(cadd(kron2(SIG[i],SIG[0]),kron2(SIG[0],SIG[i])),QI(Fr(1,2))) for i in (1,2,3)]
eps={(1,2,3):1,(2,3,1):1,(3,1,2):1,(2,1,3):-1,(1,3,2):-1,(3,2,1):-1}
J=[]
for i in (1,2,3):
    acc=[[ZERO]*4 for _ in range(4)]
    for (a,b,c),sg in eps.items():
        if a==i: acc=cadd(acc,csc(kron2(SIG[b],SIG[c]),QI(Fr(sg,2))))
    J.append(acc)
K=[csc(csub(kron2(SIG[0],SIG[i]),kron2(SIG[i],SIG[0])),QI(Fr(1,2))) for i in (1,2,3)]
Eij={}
for i in (1,2,3):
    for j in range(i,4):
        Eij[(i,j)]=csc(cadd(kron2(SIG[i],SIG[j]),kron2(SIG[j],SIG[i])),QI(Fr(1,2)))
G=[Eij[(1,2)],Eij[(1,3)],Eij[(2,3)],csub(Eij[(1,1)],Eij[(2,2)]),csub(Eij[(2,2)],Eij[(3,3)])]

def flat(A): return [x for row in A for x in row]

# 1. sigma2 regression guard
chk(SIG[2][0][1]==QI(0,-1) and SIG[2][1][0]==QI(0,1),"sigma2 faithful entries")
chk(ceq(cmul(SIG[2],SIG[2]),ceye(2)),"sigma2^2 = I")
# 2. CT0.7(1): swap = (E0+Sigma)/2
chk(ceq(csc(cadd(E0,SGM),QI(Fr(1,2))),SWAP),"CT0.7(1): S=(E0+Sigma)/2 = literal swap")
# 3. CT1.4
chk(ceq(comm(W[0],W[1]),csc(W[2],IM)),"CT1.4: [W1,W2]=iW3")
# 4. CT1.6
chk(ceq(comm(J[0],J[1]),csc(W[2],IM)),"CT1.6: [J1,J2]=iW3")
chk(ceq(comm(K[0],K[1]),csc(W[2],IM)),"CT1.6: [K1,K2]=iW3")
# 5. J-block non-closure: iW3 not in span{J}
chk(field_rank([flat(x) for x in J]+[flat(W[2])])==4,"span{J_i} not Lie-closed (W3 outside)")
# 6. CT1.5 exact: [Sigma,J1] = 4i K1
chk(ceq(comm(SGM,J[0]),csc(K[0],QI(0,4))),"CT1.5: [Sigma,J1]=4iK1")
chk(ceq(comm(SGM,K[0]),csc(J[0],QI(0,-4))),"CT1.5: [Sigma,K1]=-4iJ1")
chk(ceq(comm(SGM,W[0]),[[ZERO]*4 for _ in range(4)]),"CT1.5: [Sigma,W1]=0")
# 7. CT1.9: su(4) = span{Sigma,G,W,J,K}: 15-dim, traceless; E0 central
allv=[flat(SGM)]+[flat(x) for x in G]+[flat(x) for x in W]+[flat(x) for x in J]+[flat(x) for x in K]
chk(field_rank(allv)==15,"CT1.9: su(4) dimension 15")
chk(all(ctrace(M)==ZERO for M in [SGM]+G+W+J+K),"all su(4) generators traceless")
chk(all(ceq(comm(E0,M),[[ZERO]*4 for _ in range(4)]) for M in [SGM]+G+W+J+K),"CT1.3/CT1.9: E0 central")
# 8. block dimensions vs 15 (FT.58(3)/FT.59(2) arithmetic)
dims={'J+':3,'J-':3,'G':5,'W':3,'H':1,'D+':1,'EM':1,'strong':8}
chk(all(v<15 for v in dims.values()),"every aspect block dim < 15 = dim su(4)")
chk(dims['G']+dims['H']+dims['W']==9,"pair-observable capacity 9")
chk(dims['EM']+dims['strong']==9,"stack-observable capacity 9")
chk(all(n*n-1>=15 for n in (4,5,6)) and 3*3-1==8<=9,"dim su(N>=4) >= 15 > 9; su(3)=8 fits")
# 9. su(3) embedded in su(4) via matrix units (FT.59(3) premise)
def e3(i,j):
    M=[[ZERO]*3 for _ in range(3)]; M[i][j]=ONE; return M
def emb(M):
    R=[[ZERO]*4 for _ in range(4)]
    for i in range(3):
        for j in range(3): R[i][j]=M[i][j]
    return R
gens=[]
for (i,j) in [(0,1),(0,2),(1,2)]:
    gens.append(csub(e3(i,j),e3(j,i)))
    gens.append(csc(cadd(e3(i,j),e3(j,i)),IM))
gens.append(csc(csub(e3(0,0),e3(1,1)),IM))
gens.append(csc(csub(e3(1,1),e3(2,2)),IM))
chk(len(gens)==8,"su(3) Cartan-Weyl basis: 8 generators")
G4=[emb(x) for x in gens]
chk(field_rank([flat(x) for x in G4])==8,"embedded su(3): 8-dim independent inside su(4) space")
closed=True
for a in range(8):
    for b in range(a+1,8):
        c=comm(G4[a],G4[b])
        if field_rank([flat(x) for x in G4]+[flat(c)])!=8: closed=False
chk(closed,"embedded su(3) bracket-closed => su(3) subalgebra of su(4)")
# 10. matrix-unit hosting identity (FT.58(1) regression)
lam1=cadd(e3(0,1),e3(1,0))
lam2=csc(csub(e3(0,1),e3(1,0)),QI(0,-1))   # lambda_2 = -i E12 + i E21
lhs=csc(cadd(lam1,csc(lam2,IM)),QI(Fr(1,2)))
chk(ceq(lhs,e3(0,1)),"FT.58(1): (lambda1 + i lambda2)/2 = E12 exactly")
# 11. u(6) ledger and strictly-new ladder (FT.59(4a), FT.41(d))
chk(6*6==36 and 6*6-1==35 and 6*6-6==30,"u(6)=36=1+35; face-floor exchange sector 30")
chk([n*n-n for n in (1,2,3,6)]==[0,2,6,30],"strictly-new ladder N^2-N: 0,2,6,30")
# 12. CT4.4 register side: O(n) growth vs algebra-kernel growth are different ledgers (FT.59(4d))
O=lambda n: max(0,2**(n+1)-16)
chk([O(n) for n in (3,4,5,6)]==[0,16,48,112] and [n*n-1 for n in (3,4,5,6)]==[8,15,24,35],
    "kernel ledger n^2-1 vs absorption ledger O(n)=2^(n+1)-16: distinct growth")

print(f"verify_H_specification: {N} checks green")
