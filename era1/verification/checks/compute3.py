
"""compute3: Sym^k machinery (P-H9 consequences), CT0.7a regressions, defect ladder.
Exact arithmetic over Q and Q(i) only."""
from fractions import Fraction as Fr
import sys
sys.path.insert(0,'/home/user/scratch')
from q5 import QI

I=QI(0,1); ONE=QI(1,0); ZERO=QI(0,0)

# ---------- rational matrix helpers ----------
def mat_mul(A,B):
    n=len(A); k=len(B); m=len(B[0])
    C=[[Fr(0)]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            C[i][j]=sum(A[i][t]*B[t][j] for t in range(k))
    return C
def mat_add(A,B): return [[A[i][j]+B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def mat_sub(A,B): return [[A[i][j]-B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def mat_eq(A,B): return all(A[i][j]==B[i][j] for i in range(len(A)) for j in range(len(A[0])))
def eye(n,c=Fr(1)): return [[c if i==j else Fr(0) for j in range(n)] for i in range(n)]

# ---------- Sym^k of C^2 in monomial basis x^{k-r} y^r ----------
def symk_gen(k):
    n=k+1
    H=[[Fr(0)]*n for _ in range(n)]
    E=[[Fr(0)]*n for _ in range(n)]
    F=[[Fr(0)]*n for _ in range(n)]
    for r in range(n):
        H[r][r]=Fr(k-2*r)          # H = x dx - y dy
        if r>=1: E[r-1][r]=Fr(r)   # E = x d/dy : y^r -> r y^{r-1} x
        if r<=k-1: F[r+1][r]=Fr(k-r) # F = y d/dx
    return H,E,F
def comm(A,B): return mat_sub(mat_mul(A,B),mat_mul(B,A))

def check_symk(kmax=6):
    for k in range(0,kmax+1):
        H,E,F=symk_gen(k)
        assert mat_eq(comm(H,E), [[Fr(2)*x for x in row] for row in E]), (k,'[H,E]=2E')
        assert mat_eq(comm(H,F), [[Fr(-2)*x for x in row] for row in F]), (k,'[H,F]=-2F')
        assert mat_eq(comm(E,F), H), (k,'[E,F]=H')
        # physics Casimir sum W^2 = (1/2)(EF+FE+H^2/2) = j(j+1) I, j=k/2  [CT0.7a normalization: W=gens/2]
        C=mat_add(mat_mul(E,F),mat_mul(F,E))
        H2=mat_mul(H,H)
        C=mat_add(C,[[x/2 for x in row] for row in H2])
        C=[[x/2 for x in row] for row in C]
        val=Fr(k,2)*(Fr(k,2)+1)
        assert mat_eq(C, eye(k+1,val)), (k,'Casimir',C,val)
        # weights
        wts=[Fr(k-2*r,2) for r in range(k+1)]
        assert wts==[Fr(k,2)-r for r in range(k+1)]
    print(f"  Sym^k: sl2 relations, Casimir (k/2)(k/2+1), weights k/2..-k/2 verified exactly, k=0..{kmax}")
    # native rungs
    H1,E1,F1=symk_gen(1)
    assert mat_eq(H1,[[Fr(1),Fr(0)],[Fr(0),Fr(-1)]])  # seed: sigma_3 in this basis
    H2,E2,F2=symk_gen(2)
    vals=[H2[r][r] for r in range(3)]
    assert vals==[Fr(2),Fr(0),Fr(-2)]                   # Sym^2 weights 1,0,-1 (j=1)
    print("  native rungs: Sym^1 = seed (H = diag(1,-1)); Sym^2 weights {1,0,-1} (j=1, Casimir 2 = CT0.7a)")

# ---------- CT0.7/CT0.7a regressions over Q(i) ----------
SIG=[[[QI(1),QI(0)],[QI(0),QI(1)]],
     [[QI(0),QI(1)],[QI(1),QI(0)]],
     [[QI(0),QI(0,-1)],[QI(0,1),QI(0)]],
     [[QI(1),QI(0)],[QI(0),QI(-1)]]]           # sigma_3
def kron2(A,B):
    n=len(A); m=len(B)
    C=[[ZERO]*(n*m) for _ in range(n*m)]
    for i in range(n):
        for j in range(m):
            for k2 in range(n):
                for l in range(m):
                    C[i*m+k2][j*m+l]=A[i][j]*B[k2][l]
    return C
def cmat_mul(A,B):
    n=len(A); k=len(B); m=len(B[0])
    C=[[ZERO]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            acc=ZERO
            for t in range(k): acc=acc+A[i][t]*B[t][j]
            C[i][j]=acc
    return C
def cmat_add(A,B): return [[A[i][j]+B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def cmat_sub(A,B): return [[A[i][j]-B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def cmat_eq(A,B): return all(A[i][j]==B[i][j] for i in range(len(A)) for j in range(len(A[0])))
def cmat_scale(A,c): return [[c*x for x in row] for row in A]
def ceye(n): return [[ONE if i==j else ZERO for j in range(n)] for i in range(n)]
def cdag(A): return [[A[j][i].conj() for j in range(len(A))] for i in range(len(A[0]))]
def S4():
    s=[[ZERO]*4 for _ in range(4)]
    # basis |00>,|01>,|10>,|11>
    s[0][0]=ONE; s[3][3]=ONE; s[1][2]=ONE; s[2][1]=ONE
    return s

def check_ct07a():
    SG=SIG
    assert SG[2][0][1]==QI(0,-1), "sigma2 regression guard"
    assert cmat_eq(cmat_mul(SG[2],SG[2]), ceye(2)), "sigma2^2 = I guard"
    E0=kron2(SG[0],SG[0])
    SGM=kron2(SG[1],SG[1])          # Sigma = sum_i sigma_i (x) sigma_i   [C5]
    for i in (2,3):
        SGM=cmat_add(SGM,kron2(SG[i],SG[i]))
    Sg=cmat_scale(cmat_add(E0,SGM),QI(Fr(1,2)))   # S = (E0+Sigma)/2   [CT0.7(1)]
    # S must equal the literal basis swap
    lit=S4()
    assert cmat_eq(Sg,lit), "CT0.7(1): (E0+Sigma)/2 = literal swap" 
    W=[]
    for i in (1,2,3):
        Wi=cmat_scale(cmat_add(kron2(SG[i],SG[0]),kron2(SG[0],SG[i])),QI(Fr(1,2)))
        W.append(Wi)
    sumW2=cmat_mul(W[0],W[0])
    for i in (1,2): sumW2=cmat_add(sumW2,cmat_mul(W[i],W[i]))
    rhs=cmat_add(cmat_scale(E0,QI(Fr(3,2))),cmat_scale(SGM,QI(Fr(1,2))))
    assert cmat_eq(sumW2,rhs), "CT0.7a: sum W_i^2 = (3/2)E0 + (1/2)Sigma"
    # projectors
    PiR=cmat_scale(cmat_add(ceye(4),Sg),QI(Fr(1,2)))
    PiV=cmat_scale(cmat_sub(ceye(4),Sg),QI(Fr(1,2)))
    trR=ZERO
    trV=ZERO
    for i in range(4): trR=trR+PiR[i][i]; trV=trV+PiV[i][i]
    assert trR==QI(3) and trV==QI(1), (trR,trV)
    # eigen: on symmetric vectors v: sumW2 v = 2 v ; antisym: 0
    symv=[[ONE,ZERO,ZERO,ZERO],[ZERO,ONE,ONE,ZERO],[ZERO,ZERO,ZERO,ONE]]
    for v in symv:
        w=[]
        for i in range(4):
            acc=ZERO
            for j in range(4): acc=acc+sumW2[i][j]*v[j]
            w.append(acc)
        w2=[QI(2)*x for x in v]
        assert all(a==b for a,b in zip(w,w2)), "Casimir 2 on symmetric"
    av=[ZERO,ONE,QI(-1),ZERO]
    w=[]
    for i in range(4):
        acc=ZERO
        for j in range(4): acc=acc+sumW2[i][j]*av[j]
        w.append(acc)
    assert all(x==ZERO for x in w), "Casimir 0 on antisymmetric"
    print("  CT0.7a regression: sum W^2 = (3/2)E0+(1/2)S; traces 3/1; Casimir 2/0 on sym/antisym; sigma2 guard OK")

def check_FT54_regression():
    SG=SIG
    pts=[QI(0,1), QI(Fr(3,5),Fr(4,5)), QI(Fr(5,13),Fr(12,13)), QI(Fr(-7,25),Fr(24,25)), QI(1,0), QI(Fr(117,125),Fr(44,125)), QI(Fr(-3,5),QI(Fr(4,5)).b and Fr(-4,5))]
    pts=[QI(0,1), QI(Fr(3,5),Fr(4,5)), QI(Fr(5,13),Fr(12,13)), QI(Fr(-7,25),Fr(24,25)), QI(1,0), QI(Fr(117,125),Fr(44,125)), QI(Fr(-3,5),Fr(-4,5))]
    axes=[[QI(Fr(1,3)),QI(Fr(2,3)),QI(Fr(2,3))],[QI(1,0),QI(0,0),QI(0,0)],[QI(0,0),QI(Fr(3,5)),QI(Fr(4,5))]]
    for t in pts:
        # U = cos(phi) I + i sin(phi) n.sigma with cos(phi)=(t+t^-1)/2... use diagonal n=z: U=diag(t, t^-1)
        tc=t.conj()  # on unit circle t^-1 = conj
        U=[[t,ZERO],[ZERO,tc]]
        Um=cmat_sub(U,ceye(2))
        L=cmat_mul(cdag(Um),Um)
        c2=(t+tc)/QI(2)
        d=QI(2)-QI(2)*c2
        assert cmat_eq(L, cmat_scale(ceye(2), d)), ("FT54 defect scalar", t)
    # non-diagonal axis check: U = cos + i sin n.sigma with rational n and rational cos/sin:
    for (c,s,n) in [(QI(Fr(3,5)),QI(Fr(4,5)),[QI(Fr(1,3)),QI(Fr(2,3)),QI(Fr(2,3))]),
                    (QI(Fr(5,13)),QI(Fr(12,13)),[QI(1),ZERO,ZERO]),
                    (QI(Fr(-7,25)),QI(Fr(24,25)),[ZERO,QI(Fr(3,5)),QI(Fr(4,5))])]:
        SGx=SIG
        ns=cmat_add(cmat_add(cmat_scale(SGx[1],n[0]),cmat_scale(SGx[2],n[1])),cmat_scale(SGx[3],n[2]))
        U=cmat_add(cmat_scale(ceye(2),c),cmat_scale(cmat_scale(ns,I),s))
        Um=cmat_sub(U,ceye(2))
        L=cmat_mul(cdag(Um),Um)
        d=QI(2)-QI(2)*c
        assert cmat_eq(L,cmat_scale(ceye(2),d)), ("FT54 axis-free", c,s)
    print("  FT.54 regression: (U-1)^dag(U-1) = (2-2cos phi) I over Q(i), diagonal + 3 rational axes")

# ---------- defect ladder on Sym^k ----------
def defect_ladder_check():
    # diagonal transport: U = diag(t, t^-1), |t|=1; Sym^k(U) = diag(t^{k-2r})
    def tpower(t,m):
        if m>=0:
            r=ONE
            for _ in range(m): r=r*t
            return r
        r=ONE; tc=t.conj()
        for _ in range(-m): r=r*tc
        return r
    ts=[QI(0,1), QI(Fr(3,5),Fr(4,5)), QI(Fr(5,13),Fr(12,13)), QI(Fr(-7,25),Fr(24,25)), QI(1,0)]
    for t in ts:
        c=(t+t.conj())/QI(2)  # cos phi, rational
        for k in range(1,5):
            defs=[]
            for r in range(k+1):
                m=k-2*r
                tm=tpower(t,m)
                D=QI(2)-tm-tm.conj()
                assert D.b==0
                defs.append((m,D))
            # k=1: state independence
            if k==1: assert defs[0][1]==defs[1][1], "k=1 state-independent (FT.54)"
            # even k: middle weight zero defect
            if k%2==0:
                mid=[d for m,d in defs if m==0]
                assert mid and mid[0]==QI(0), "even-k middle weight defect-massless"
            # Chebyshev consistency: D(m) = 2-2 T_|m|(c), T integer polys
            cache={0:[Fr(1)],1:[Fr(0),Fr(1)]}
            def get_T(m):
                if m in cache: return cache[m]
                a=get_T(m-1); b=get_T(m-2)
                two=[Fr(0)]*(len(a)+1)
                for i2,v in enumerate(a): two[i2+1]+=2*v
                res=two[:]
                for i2,v in enumerate(b): res[i2]-=v
                cache[m]=res
                return res
            for m,D in defs:
                T=get_T(abs(m))
                val=QI(0)
                for pw,co in enumerate(T):
                    if co:
                        pp=QI(1)
                        for _ in range(pw): pp=pp*c
                        val=val+QI(co)*pp
                assert QI(2)-QI(2)*val==D, ("cheb",m,D,val)
    print("  defect ladder: Sym^k diagonal weights t^(k-2r); D(m)=2-2cos(m phi)=2-2T_|m|(cos phi) exact over Q(i);")
    print("    k=1 state-independent (FT.54 recovered); even-k middle weight D=0 exactly (massless middle)")

def platonic_defect_table():
    """Exact vertex-figure defect ladders D(w) = 2-2cos(w*delta/2), w=1..4, per solid."""
    # cos(delta/2) values and their exact algebras:
    # tetra: delta/2 = pi/2 -> cos=0 ; cube: pi/4 -> sqrt2/2 ; octa: pi/3 -> 1/2 ; dodeca: pi/10 -> cos18 ; icosa: pi/6 -> sqrt3/2
    from q5 import Q5
    print("  vertex-figure defect ladder D(w)=2-2cos(w*delta_v/2) (units of mu'^2), w = Sym^k weight:")
    # tetra: D(w)=2-2cos(w pi/2): w:1->2, 2->4, 3->2, 4->0
    tet=[2-2*c for c in [0,-1,0,1]]
    assert tet==[2,4,2,0]
    print(f"    tetrahedron (delta=pi):   D(w), w=1..4: {tet}   (rational; D(4)=0)")
    # octa: cos(w pi/3): w=1:1/2 ->1; w=2:-1/2->3; w=3:-1->4; w=4:-1/2->3
    octa=[2-2*c for c in [Fr(1,2),Fr(-1,2),Fr(-1),Fr(-1,2)]]
    assert octa==[1,3,4,3]
    print(f"    octahedron (delta=2pi/3): D(w), w=1..4: {[str(x) for x in octa]}   (rational)")
    # icosa: cos(w pi/6): sqrt3/2, 1/2, 0, -1/2 -> 2-sqrt3, 1, 2, 3
    print("    icosahedron (delta=pi/3): D(w), w=1..4: 2-sqrt3, 1, 2, 3   (Q(sqrt3))")
    # cube: cos(w pi/4): sqrt2/2, 0, -sqrt2/2, -1 -> 2-sqrt2, 2, 2+sqrt2, 4
    print("    cube (delta=pi/2):        D(w), w=1..4: 2-sqrt2, 2, 2+sqrt2, 4   (Q(sqrt2))")
    # dodeca: cos(w pi/10): w=1: cos18; w=2: cos36=(1+sqrt5)/4 -> (3-sqrt5)/2; w=3: cos54; w=4: cos72=(sqrt5-1)/4 -> (5-sqrt5)/2
    c36=Q5(Fr(1,4),Fr(1,4))
    D2=Q5(2)-2*c36
    assert D2==Q5(Fr(3,2),Fr(-1,2)), D2
    c72=Q5(Fr(-1,4),Fr(1,4))
    D4=Q5(2)-2*c72
    assert D4==Q5(Fr(5,2),Fr(-1,2)), D4
    # verify cos36/cos72 polys: 4c^2-2c-1 at c36; 4c^2+2c-1 at c72
    def q5poly(c,coeffs):
        r=Q5(0)
        for k,a in enumerate(coeffs):
            p=Q5(1)
            for _ in range(k): p=p*c
            r=r+p*Q5(a)
        return r
    assert q5poly(c36,[Fr(-1),Fr(-2),Fr(4)])==Q5(0)
    assert q5poly(c72,[Fr(-1),Fr(2),Fr(4)])==Q5(0)
    print("    dodecahedron (delta=pi/5): D(2)=(3-sqrt5)/2, D(4)=(5-sqrt5)/2 (Q(sqrt5), polys 4c^2-+2c-1 verified);")
    print("      D(1)=2-2cos18, D(3)=2-2cos54: both roots of x^4-8x^3+19x^2-12x+1 (verified in compute2)")

def basis_relativity_witness():
    # tetrahedron uniform kappa0=2: digon basis 6 chains k=2 each; face basis 4 faces k_f=3
    dig=[2]*6; face=[3]*4
    assert sum(dig)==sum(face)==12
    dimdig=1
    for k in dig: dimdig*= (k+1)
    dimface=1
    for k in face: dimface*=(k+1)
    assert dimdig==3**6==729 and dimface==4**4==256 and dimdig!=dimface
    assert sum(Fr(k,2) for k in dig)==sum(Fr(k,2) for k in face)==6
    print(f"  basis-relativity witness (tetrahedron, kappa0=2): digon basis k-multiset {dig} (dim {dimdig}),")
    print(f"    face basis {face} (dim {dimface}): same Sigma k = 12, same j_max = 6, DIFFERENT carrier dims => per-chain granularity needed")

def subloop_obstruction_witness():
    # odd-L uniform minimum is not a count of materialized winding-1 subloops:
    # triangle: kappa=(1,1,1): Theta=3 odd -> off-shell; (2,2,2): Theta=6, k=3
    for kap in [(1,1,1)]:
        assert sum(kap)%2==1
    kap=(2,2,2)
    assert sum(kap)==6 and sum(kap)%2==0
    k=sum(kap)//2
    assert k==3
    # and the on-shell k=1 profiles on the triangle are null-carrying: (1,1,0) perms: Theta=2
    ones=[p for p in [(1,1,0),(1,0,1),(0,1,1)]]
    for p in ones: assert sum(p)==2
    # (2,2,2) = (1,1,0)+(0,1,1)+(1,0,1) as PROFILES, but the summands are digon-supported,
    # not three materialized winding-1 face loops (kappa=(1,1,1) is off-shell):
    s=tuple(sum(x) for x in zip(*ones))
    assert s==(2,2,2)
    print("  subloop-count obstruction (triangle): kappa=(1,1,1) off-shell (Theta=3 odd); uniform min k=3;")
    print("    profile (2,2,2) = sum of three (1,1,0)-type profiles, but those are null/digon-supported:")
    print("    multiplicity != materialized winding-1 subloop count => P-H9 multiplicity datum is irreducible to decomposition")

if __name__=='__main__':
    print("Sym^k / defect ladder checks (exact):")
    check_symk(6)
    check_ct07a()
    check_FT54_regression()
    defect_ladder_check()
    platonic_defect_table()
    basis_relativity_witness()
    subloop_obstruction_witness()
    print("ALL COMPUTE3 OK")
