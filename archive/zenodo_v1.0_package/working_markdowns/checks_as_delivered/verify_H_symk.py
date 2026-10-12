
#!/usr/bin/env python3
"""verify_H_symk.py — companion to Def-H.23 / FT.60 (P-H9 consequences).
Exact arithmetic over Q and Q(i); Chebyshev/Z[c] polynomial reductions over Z. No floating point."""
import os,sys
HERE=os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,HERE)
from hcommon import *

N=0
def chk(cond,msg):
    global N
    assert cond, "FAIL: "+msg
    N+=1

# ---------- Sym^k: sl2 triple in monomial basis x^{k-r} y^r ----------
def symk(k):
    n=k+1
    H=[[Fr(0)]*n for _ in range(n)]; E=[[Fr(0)]*n for _ in range(n)]; F=[[Fr(0)]*n for _ in range(n)]
    for r in range(n):
        H[r][r]=Fr(k-2*r)
        if r>=1: E[r-1][r]=Fr(r)
        if r<=k-1: F[r+1][r]=Fr(k-r)
    return H,E,F

for k in range(0,7):
    H,E,F=symk(k)
    chk(meq(mcomm(H,E),[[2*x for x in row] for row in E]),f"Sym^{k}: [H,E]=2E")
    chk(meq(mcomm(H,F),[[-2*x for x in row] for row in F]),f"Sym^{k}: [H,F]=-2F")
    chk(meq(mcomm(E,F),H),f"Sym^{k}: [E,F]=H")
    C=madd(mmul(E,F),mmul(F,E))
    C=madd(C,[[x/2 for x in row] for row in mmul(H,H)])
    C=[[x/2 for x in row] for row in C]
    chk(meq(C,meye(k+1,Fr(k,2)*(Fr(k,2)+1))),f"Sym^{k}: Casimir (k/2)(k/2+1) [CT0.7a normalization]")
    chk([H[r][r] for r in range(k+1)]==[Fr(k-2*r) for r in range(k+1)],f"Sym^{k}: weight ladder k..-k")

# native rungs
H1,_,_=symk(1)
chk(meq(H1,[[Fr(1),Fr(0)],[Fr(0),Fr(-1)]]),"Sym^1 = seed: H=diag(1,-1) (j=1/2)")
H2,_,_=symk(2)
chk([H2[r][r] for r in range(3)]==[Fr(2),Fr(0),Fr(-2)],"Sym^2 weights {2,0,-2} (j=1)")

# ---------- CT0.7/CT0.7a regressions over Q(i) ----------
E0=kron2(SIG[0],SIG[0])
SGM=kron2(SIG[1],SIG[1])
for i in (2,3): SGM=cadd(SGM,kron2(SIG[i],SIG[i]))
SW=[[ZERO]*4 for _ in range(4)]
SW[0][0]=ONE; SW[3][3]=ONE; SW[1][2]=ONE; SW[2][1]=ONE
chk(ceq(csc(cadd(E0,SGM),QI(Fr(1,2))),SW),"CT0.7(1): S=(E0+Sigma)/2")
Wm=[csc(cadd(kron2(SIG[i],SIG[0]),kron2(SIG[0],SIG[i])),QI(Fr(1,2))) for i in (1,2,3)]
sumW2=cmul(Wm[0],Wm[0])
for i in (1,2): sumW2=cadd(sumW2,cmul(Wm[i],Wm[i]))
chk(ceq(sumW2,cadd(csc(E0,QI(Fr(3,2))),csc(SGM,QI(Fr(1,2))))),"CT0.7a: sum W^2 = (3/2)E0+(1/2)Sigma")
PiR=csc(cadd(ceye(4),SW),QI(Fr(1,2))); PiV=csc(csub(ceye(4),SW),QI(Fr(1,2)))
chk(ctrace(PiR)==QI(3) and ctrace(PiV)==QI(1),"CT0.7(1): traces 3 / 1")
for v in ([ONE,ZERO,ZERO,ZERO],[ZERO,ONE,ONE,ZERO],[ZERO,ZERO,ZERO,ONE]):
    w=[]
    for i in range(4):
        acc=ZERO
        for j in range(4): acc=acc+sumW2[i][j]*v[j]
        w.append(acc)
    chk(all(a==QI(2)*x for a,x in zip(w,v)),"CT0.7a: Casimir 2 on symmetric vectors")
av=[ZERO,ONE,QI(-1),ZERO]
w=[]
for i in range(4):
    acc=ZERO
    for j in range(4): acc=acc+sumW2[i][j]*av[j]
    w.append(acc)
chk(all(x==ZERO for x in w),"CT0.7a: Casimir 0 on antisymmetric")

# ---------- FT.54 regression: (U-1)^dag (U-1) = (2-2cos phi) I ----------
def tpower(t,m):
    if m>=0:
        r=ONE
        for _ in range(m): r=r*t
        return r
    r=ONE; tc=t.conj()
    for _ in range(-m): r=r*tc
    return r
pts=[QI(0,1),QI(Fr(3,5),Fr(4,5)),QI(Fr(5,13),Fr(12,13)),QI(Fr(-7,25),Fr(24,25)),QI(1,0),QI(Fr(117,125),Fr(44,125))]
for t in pts:
    U=[[t,ZERO],[ZERO,t.conj()]]
    Um=csub(U,ceye(2))
    L=cmul(cdag(Um),Um)
    c=(t+t.conj())/QI(2)
    chk(ceq(L,csc(ceye(2),QI(2)-QI(2)*c)),f"FT.54(1): defect scalar 2-2cos(phi) at exact point")
axes=[(QI(Fr(3,5)),QI(Fr(4,5)),[QI(Fr(1,3)),QI(Fr(2,3)),QI(Fr(2,3))]),
      (QI(Fr(5,13)),QI(Fr(12,13)),[ONE,ZERO,ZERO]),
      (QI(Fr(-7,25)),QI(Fr(24,25)),[ZERO,QI(Fr(3,5)),QI(Fr(4,5))])]
for (c,sn,n) in axes:
    ns=cadd(cadd(csc(SIG[1],n[0]),csc(SIG[2],n[1])),csc(SIG[3],n[2]))
    U=cadd(csc(ceye(2),c),csc(csc(ns,IM),sn))
    Um=csub(U,ceye(2))
    chk(ceq(cmul(cdag(Um),Um),csc(ceye(2),QI(2)-QI(2)*c)),"FT.54(1): axis-independent, rational axes")

# ---------- defect ladder on Sym^k: D(m) = 2 - t^m - t^{-m} = 2-2 T_|m|(cos phi) ----------
def cheb(m,cache={0:[Fr(1)],1:[Fr(0),Fr(1)]}):
    if m in cache: return cache[m]
    a=cheb(m-1); b=cheb(m-2)
    two=[Fr(0)]*(len(a)+1)
    for i,v in enumerate(a): two[i+1]+=2*v
    res=two[:]
    for i,v in enumerate(b): res[i]-=v
    cache[m]=res
    return res
for t in pts:
    c=(t+t.conj())/QI(2)
    for k in range(1,5):
        for r in range(k+1):
            m=k-2*r
            tm=tpower(t,m)
            D=QI(2)-tm-tm.conj()
            chk(D.b==0,f"defect real, k={k} m={m}")
            T=cheb(abs(m))
            val=QI(0)
            for pw,co in enumerate(T):
                if co:
                    pp=QI(1)
                    for _ in range(pw): pp=pp*c
                    val=val+QI(co)*pp
            chk(QI(2)-QI(2)*val==D,f"Chebyshev identity D(m)=2-2T_|m|(cos phi), k={k} m={m}")
        if k==1:
            t0=tpower(t,1); D0=QI(2)-t0-t0.conj()
            t1=tpower(t,-1); D1=QI(2)-t1-t1.conj()
            chk(D0==D1,"k=1 state-independence (FT.54(1) recovered)")
        if k%2==0:
            t0=tpower(t,0)
            chk(QI(2)-t0-t0.conj()==ZERO,"even-k middle weight m=0: defect exactly 0")

# ---------- Platonic defect data: exact radicals ----------
class Qsq:
    """a + b*sqrt(d) over Fraction."""
    def __init__(s,a,b,d): s.a=Fr(a); s.b=Fr(b); s.d=d
    def __mul__(s,o): return Qsq(s.a*o.a+s.d*s.b*o.b, s.a*o.b+s.b*o.a, s.d)
    def __add__(s,o): return Qsq(s.a+o.a,s.b+o.b,s.d)
    def __sub__(s,o): return Qsq(s.a-o.a,s.b-o.b,s.d)
    def __eq__(s,o): return s.a==o.a and s.b==o.b and s.d==o.d
def qpoly_val(coeffs,x):
    r=Qsq(0,0,x.d); pw=Qsq(1,0,x.d)
    for c in coeffs:
        r=r+pw*Qsq(c,0,x.d); pw=pw*x
    return r
# tetra D=2; octa D=1: rational
# cube: D=2-sqrt2, minpoly x^2-4x+2
r2=Qsq(2,-1,2)
chk(qpoly_val([2,-4,1],r2)==Qsq(0,0,2),"cube: (2-sqrt2)^2-4(2-sqrt2)+2=0")
# icosa: D=2-sqrt3, minpoly x^2-4x+1
r3=Qsq(2,-1,3)
chk(qpoly_val([1,-4,1],r3)==Qsq(0,0,3),"icosa: (2-sqrt3)^2-4(2-sqrt3)+1=0")
# cube ladder w=1..4: 2-2cos(w pi/4) = 2-sqrt2, 2, 2+sqrt2, 4
c45=Qsq(Fr(0),Fr(1,2),2)  # cos(pi/4) = sqrt2/2
D1c=Qsq(2,0,2)-Qsq(2,0,2)*c45
chk(D1c==Qsq(2,-1,2),"cube ladder w=1: 2-sqrt2")
# icosa ladder: cos(pi/6)=sqrt3/2 -> 2-sqrt3; cos(pi/3)=1/2 -> 1; cos(pi/2)=0 -> 2; cos(2pi/3)=-1/2 -> 3
c30=Qsq(Fr(0),Fr(1,2),3)  # cos(pi/6) = sqrt3/2
chk(Qsq(2,0,3)-Qsq(2,0,3)*c30==Qsq(2,-1,3),"icosa ladder w=1: 2-sqrt3")
chk(Qsq(2,0,3)-Qsq(2,0,3)*Qsq(Fr(1,2),0,3)==Qsq(1,0,3),"icosa ladder w=2: 1")
# octa ladder: cos(pi/3)=1/2 ->1; cos(2pi/3)=-1/2 ->3; cos(pi)=-1 ->4; w=4: cos(4pi/3)=-1/2 ->3
octL=[2-2*Fr(1,2),2-2*Fr(-1,2),2-2*Fr(-1),2-2*Fr(-1,2)]
chk(octL==[1,3,4,3],"octa ladder (1,3,4,3) rational")
tetL=[2-2*0,2-2*(-1),2-2*0,2-2*1]
chk(tetL==[2,4,2,0],"tetra ladder (2,4,2,0) rational; exact zero at w=4")
# dodeca: cos36=(1+sqrt5)/4, cos72=(sqrt5-1)/4 in Q(sqrt5)
r5=Q5(Fr(0),Fr(1))
c36=Q5(Fr(1,4),Fr(1,4)); c72=Q5(Fr(-1,4),Fr(1,4))
def q5poly(coeffs,x):
    r=Q5(0); pw=Q5(1)
    for c in coeffs:
        r=r+pw*Q5(c); pw=pw*x
    return r
chk(q5poly([-1,-2,4],c36)==Q5(0),"cos36: 4c^2-2c-1=0")
chk(q5poly([-1,2,4],c72)==Q5(0),"cos72: 4c^2+2c-1=0")
D2d=Q5(2)-Q5(2)*c36
chk(D2d==Q5(Fr(3,2),Fr(-1,2)),"dodeca ladder w=2: (3-sqrt5)/2")
D4d=Q5(2)-Q5(2)*c72
chk(D4d==Q5(Fr(5,2),Fr(-1,2)),"dodeca ladder w=4: (5-sqrt5)/2")
# dodeca w=1: D=2-2cos18: quartic x^4-8x^3+19x^2-12x+1 via Z[c]/(16c^4-20c^2+5)
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
    "dodeca: x=2-2cos(pi/10) satisfies x^4-8x^3+19x^2-12x+1=0 in Z[c]/(16c^4-20c^2+5)")
# cos5t = 16c^5-20c^3+5c by de Moivre (exact binomials)
from math import comb
agg={}
for j in (0,2,4):
    coef=Fr(comb(5,j)*(1 if j%4==0 else -1))
    ex=[Fr(0)]*7; ex[0]=Fr(1)
    for _ in range(j//2):
        nx=[Fr(0)]*7
        for k2,v in enumerate(ex):
            if v: nx[k2]+=v; nx[k2+1]-=v
        ex=nx
    for k2,v in enumerate(ex):
        if v:
            pw=5-j+2*k2; agg[pw]=agg.get(pw,Fr(0))+coef*v
ch5=[Fr(0)]*6
for pw,v in agg.items(): ch5[pw]=v
chk(ch5==[Fr(0),Fr(5),Fr(0),Fr(-20),Fr(0),Fr(16)],"cos(5t)=16c^5-20c^3+5c (de Moivre)")

# ---------- basis-relativity witness (FT.60(7a)) ----------
dig=[2]*6; face=[3]*4
chk(sum(dig)==sum(face)==12,"tetra kappa0=2: both bases sum to K_S=12")
dimdig=1
for x in dig: dimdig*=(x+1)
dimface=1
for x in face: dimface*=(x+1)
chk(dimdig==729 and dimface==256 and dimdig!=dimface,"carrier dims 3^6=729 vs 4^4=256: basis-relative")
chk(Fr(sum(dig),2)==Fr(sum(face),2)==6,"j_max = K_S/2 = 6 in both bases")

# ---------- subloop obstruction witness (FT.60(7b)) ----------
chk((1+1+1)%2==1,"triangle kappa=(1,1,1): Theta=3 odd, off-shell [FT.22]")
chk((2+2+2)%2==0 and (2+2+2)//2==3,"uniform minimum kappa=(2,2,2): k=3")
s=tuple(sum(x) for x in zip((1,1,0),(0,1,1),(1,0,1)))
chk(s==(2,2,2),"profile identity (2,2,2)=(1,1,0)+(0,1,1)+(1,0,1): summands are null/digon-supported")

print(f"verify_H_symk: {N} checks green")
