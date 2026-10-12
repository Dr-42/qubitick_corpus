
"""hcommon.py — shared exact-arithmetic core for the check suites.
Exact arithmetic only: int / Fraction / Q(sqrt5) / Q(i). No floating point anywhere.
Companion modules import this file from the same directory."""
from fractions import Fraction as Fr
import itertools

# ---------------- exact fields ----------------
class Q5:
    """a + b*sqrt(5), a,b in Fraction."""
    __slots__=('a','b')
    def __init__(s,a,b=0): s.a=Fr(a); s.b=Fr(b)
    def __add__(s,o): return Q5(s.a+o.a,s.b+o.b)
    def __sub__(s,o): return Q5(s.a-o.a,s.b-o.b)
    def __mul__(s,o):
        if isinstance(o,(int,Fr)): o=Q5(o)
        return Q5(s.a*o.a+5*s.b*o.b, s.a*o.b+s.b*o.a)
    __rmul__=__mul__
    def __neg__(s): return Q5(-s.a,-s.b)
    def inv(s):
        n=s.a*s.a-5*s.b*s.b
        assert n!=0
        return Q5(s.a/n,-s.b/n)
    def __truediv__(s,o):
        if isinstance(o,(int,Fr)): o=Q5(o)
        return s*o.inv()
    def __eq__(s,o):
        if isinstance(o,int): o=Q5(o)
        return isinstance(o,Q5) and s.a==o.a and s.b==o.b
    def __hash__(s): return hash((s.a,s.b))
    def __repr__(s): return f"Q5({s.a},{s.b})"

class QI:
    """a + b*i, a,b in Fraction."""
    __slots__=('a','b')
    def __init__(s,a,b=0): s.a=Fr(a); s.b=Fr(b)
    def __add__(s,o): return QI(s.a+o.a,s.b+o.b)
    def __sub__(s,o): return QI(s.a-o.a,s.b-o.b)
    def __mul__(s,o):
        if isinstance(o,(int,Fr)): o=QI(o)
        return QI(s.a*o.a-s.b*o.b, s.a*o.b+s.b*o.a)
    __rmul__=__mul__
    def __neg__(s): return QI(-s.a,-s.b)
    def conj(s): return QI(s.a,-s.b)
    def inv(s):
        n=s.a*s.a+s.b*s.b
        assert n!=0
        return QI(s.a/n,-s.b/n)
    def __truediv__(s,o):
        if isinstance(o,(int,Fr)): o=QI(o)
        return s*o.inv()
    def __eq__(s,o):
        if isinstance(o,int): o=QI(o)
        return isinstance(o,QI) and s.a==o.a and s.b==o.b
    def __hash__(s): return hash((s.a,s.b))
    def __repr__(s): return f"({s.a}+{s.b}i)"

ONE=QI(1); ZERO=QI(0); IM=QI(0,1)

# ---------------- matrices over QI ----------------
def cmul(A,B):
    n=len(A);k=len(B);m=len(B[0])
    C=[[ZERO]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            acc=ZERO
            for t in range(k): acc=acc+A[i][t]*B[t][j]
            C[i][j]=acc
    return C
def cadd(A,B): return [[A[i][j]+B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def csub(A,B): return [[A[i][j]-B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def csc(A,c): return [[c*x for x in row] for row in A]
def ceq(A,B): return all(A[i][j]==B[i][j] for i in range(len(A)) for j in range(len(A[0])))
def ceye(n): return [[ONE if i==j else ZERO for j in range(n)] for i in range(n)]
def comm(A,B): return csub(cmul(A,B),cmul(B,A))
def cdag(A): return [[A[j][i].conj() for j in range(len(A))] for i in range(len(A[0]))]
def ctrace(A):
    t=ZERO
    for i in range(len(A)): t=t+A[i][i]
    return t
def kron2(A,B):
    n=len(A);m=len(B)
    C=[[ZERO]*(n*m) for _ in range(n*m)]
    for i in range(n):
        for j in range(m):
            for k2 in range(n):
                for l in range(m):
                    C[i*m+k2][j*m+l]=A[i][j]*B[k2][l]
    return C
def field_rank(vecs):
    """Gaussian elimination over Q(i); vecs: list of lists of QI."""
    rows=[list(v) for v in vecs if any(x!=ZERO for x in v)]
    if not rows: return 0
    r=0
    for c in range(len(rows[0])):
        pr=None
        for i in range(r,len(rows)):
            if rows[i][c]!=ZERO: pr=i;break
        if pr is None: continue
        rows[r],rows[pr]=rows[pr],rows[r]
        pv=rows[r][c]
        rows[r]=[x/pv for x in rows[r]]
        for i in range(len(rows)):
            if i!=r and rows[i][c]!=ZERO:
                f=rows[i][c]
                rows[i]=[a-f*b for a,b in zip(rows[i],rows[r])]
        r+=1
        if r==len(rows): break
    return r

SIG=[[[ONE,ZERO],[ZERO,ONE]],
     [[ZERO,ONE],[ONE,ZERO]],
     [[ZERO,-IM],[IM,ZERO]],
     [[ONE,ZERO],[ZERO,-ONE]]]

# ---------------- rational matrices ----------------
def mmul(A,B):
    n=len(A);k=len(B);m=len(B[0])
    C=[[Fr(0)]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            C[i][j]=sum((A[i][t]*B[t][j] for t in range(k)),Fr(0))
    return C
def madd(A,B): return [[A[i][j]+B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def msub(A,B): return [[A[i][j]-B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def meq(A,B): return all(A[i][j]==B[i][j] for i in range(len(A)) for j in range(len(A[0])))
def meye(n,c=Fr(1)): return [[c if i==j else Fr(0) for j in range(n)] for i in range(n)]
def mcomm(A,B): return msub(mmul(A,B),mmul(B,A))

# ---------------- GF(2) ----------------
def gf2_rank(rows):
    basis={}
    for r in rows:
        cur=r
        while cur:
            piv=cur&(-cur)
            if piv in basis: cur^=basis[piv]
            else: basis[piv]=cur;break
    return len(basis)

def gf2_solve(B_rows,rhs,ncols):
    """B_rows: list of column-bitmasks; rhs: list of bits. Returns (particular, kernel basis) or None."""
    piv_of={}; rref=[]
    for r,t in zip(B_rows,rhs):
        cur,ct=r,t
        for pc,pr in piv_of.items():
            if cur>>pc&1:
                cur^=rref[pr][0]; ct^=rref[pr][1]
        if cur:
            pc=(cur&-cur).bit_length()-1
            piv_of[pc]=len(rref)
            rref.append((cur,ct))
        else:
            if ct: return None
    x=0
    for pc,pr in piv_of.items():
        if rref[pr][1]: x|=1<<pc
    ker=[]
    for c in range(ncols):
        if c in piv_of: continue
        v=1<<c
        for pc,pr in piv_of.items():
            if rref[pr][0]>>c&1: v|=1<<pc
        ker.append(v)
    return x,ker

# ---------------- integer Smith normal form ----------------
def snf(M):
    A=[row[:] for row in M]
    rows=len(A);cols=len(A[0])
    divs=[];t=0
    while t<min(rows,cols):
        while True:
            nz=[(i,j) for i in range(t,rows) for j in range(t,cols) if A[i][j]!=0]
            if not nz: break
            i0,j0=min(nz,key=lambda p:abs(A[p[0]][p[1]]))
            A[t],A[i0]=A[i0],A[t]
            for r in range(rows): A[r][t],A[r][j0]=A[r][j0],A[r][t]
            done=True
            for i in range(t+1,rows):
                if A[i][t]:
                    q=A[i][t]//A[t][t]
                    for j in range(t,cols): A[i][j]-=q*A[t][j]
                    if A[i][t]: done=False
            for j in range(t+1,cols):
                if A[t][j]:
                    q=A[t][j]//A[t][t]
                    for i in range(t,rows): A[i][j]-=q*A[i][t]
                    if A[t][j]: done=False
            if done and all(A[i][t]==0 for i in range(t+1,rows)) and all(A[t][j]==0 for j in range(t+1,cols)):
                break
        else:
            pass
        if not any(A[i][j] for i in range(t,rows) for j in range(t,cols)):
            break
        d=A[t][t]
        bad=None
        for ii in range(t+1,rows):
            for jj in range(t+1,cols):
                if A[ii][jj]%d!=0: bad=ii
        if bad is not None:
            for j in range(t,cols): A[t][j]+=A[bad][j]
            continue
        divs.append(abs(d)); t+=1
    changed=True
    while changed:
        changed=False
        for i in range(len(divs)-1):
            a,b=divs[i],divs[i+1]
            if b%a!=0:
                from math import gcd
                g=gcd(a,b); divs[i],divs[i+1]=g,a*b//g; changed=True
    return [d for d in divs if d!=0]

# ---------------- Platonic solids (exact encodings) ----------------
def build_tetra():
    V=[tuple(Fr(x) for x in v) for v in [(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)]]
    E=[frozenset(p) for p in itertools.combinations(range(4),2)]
    F=[frozenset({0,1,2,3}-{v}) for v in range(4)]
    return V,E,F

def build_cube():
    V=[(Fr(a),Fr(b),Fr(c)) for a in(-1,1) for b in(-1,1) for c in(-1,1)]
    def d2(u,v): return sum((a-b)**2 for a,b in zip(u,v))
    E=[frozenset((i,j)) for i in range(8) for j in range(i+1,8) if d2(V[i],V[j])==4]
    F=[]
    for ax in range(3):
        for sg in (-1,1):
            F.append(frozenset(i for i in range(8) if V[i][ax]==sg))
    return V,E,F

def build_octa():
    V=[]
    for ax in range(3):
        for sg in (-1,1):
            v=[Fr(0)]*3; v[ax]=Fr(sg); V.append(tuple(v))
    def anti(u,v): return all(a==-b for a,b in zip(u,v))
    E=[frozenset((i,j)) for i in range(6) for j in range(i+1,6) if not anti(V[i],V[j])]
    F=[]
    for s1 in(-1,1):
        for s2 in(-1,1):
            for s3 in(-1,1):
                idx=[]
                for ax,sg in ((0,s1),(1,s2),(2,s3)):
                    for i in range(6):
                        e=[Fr(0)]*3; e[ax]=Fr(sg)
                        if tuple(e)==V[i]: idx.append(i)
                F.append(frozenset(idx))
    return V,E,F

def build_icosa():
    phi=Q5(Fr(1,2),Fr(1,2))
    verts=[]
    for s1 in(-1,1):
        for s2 in(-1,1):
            verts.append((Q5(0),Q5(s1),Q5(s2)*phi))
            verts.append((Q5(s1),Q5(s2)*phi,Q5(0)))
            verts.append((Q5(s2)*phi,Q5(0),Q5(s1)))
    def d2(u,v):
        s=Q5(0)
        for a,b in zip(u,v):
            dd=a-b; s=s+dd*dd
        return s
    E=[frozenset((i,j)) for i in range(12) for j in range(i+1,12) if d2(verts[i],verts[j])==Q5(4)]
    F=[frozenset(c) for c in itertools.combinations(range(12),3)
       if frozenset((c[0],c[1])) in E and frozenset((c[0],c[2])) in E and frozenset((c[1],c[2])) in E]
    return verts,E,F

def build_dodeca(icosa):
    Vi,Ei,Fi=icosa
    ctr=[]
    for f in Fi:
        s=[Q5(0),Q5(0),Q5(0)]
        for v in sorted(f):
            for k in range(3): s[k]=s[k]+Vi[v][k]
        ctr.append(tuple(x*Q5(Fr(1,3)) for x in s))
    n=len(ctr)
    E=[frozenset((a,b)) for a in range(n) for b in range(a+1,n) if len(Fi[a]&Fi[b])==2]
    F=[frozenset(i for i in range(n) if v in Fi[i]) for v in range(12)]
    return ctr,E,F

NAMES=['tetrahedron','cube','octahedron','dodecahedron','icosahedron']

def det3(M):
    (a,b,c),(d,e,f),(g,h,i)=M
    return a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)

def inv3(M):
    d=det3(M); assert d!=0
    (a,b,c),(dd,e,f),(g,h,i)=M
    adj=[[e*i-f*h, c*h-b*i, b*f-c*e],
         [f*g-dd*i, a*i-c*g, c*dd-a*f],
         [dd*h-e*g, b*g-a*h, a*e-b*dd]]
    return [[x/d for x in row] for row in adj]

def m3mul(A,B):
    n=3
    zero=A[0][0]*0
    C=[[zero]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            acc=zero
            for t in range(n):
                if A[i][t]!=zero and B[t][j]!=zero: acc=acc+A[i][t]*B[t][j]
            C[i][j]=acc
    return C

def det_of_perm(perm,V,one,zero):
    for combo in itertools.combinations(range(len(V)),3):
        M=[[V[c][k] for c in combo] for k in range(3)]
        if det3(M)==zero: continue
        Mi=inv3(M)
        W=[[V[perm[c]][k] for c in combo] for k in range(3)]
        return det3(m3mul(W,Mi))
    raise RuntimeError("no independent triple")

def adjacency(nv,E):
    adj=[set() for _ in range(nv)]
    for e in E:
        a,b=sorted(e); adj[a].add(b); adj[b].add(a)
    return adj

def automorphisms(nv,E):
    adj=adjacency(nv,E)
    order=list(range(nv))
    res=[]; mapping={}
    def rec(k):
        if k==len(order):
            res.append(tuple(mapping[v] for v in order)); return
        v=order[k]
        img=set(range(nv))-set(mapping.values())
        for u in order[:k]:
            w=mapping[u]
            if u in adj[v]: img&=adj[w]
            else: img-=adj[w]
        for w in sorted(img):
            mapping[v]=w; rec(k+1); del mapping[v]
    rec(0)
    return res

def solid_data(name):
    if name=='tetrahedron': V,E,F=build_tetra()
    elif name=='cube': V,E,F=build_cube()
    elif name=='octahedron': V,E,F=build_octa()
    elif name=='icosahedron': V,E,F=build_icosa()
    elif name=='dodecahedron': V,E,F=build_dodeca(build_icosa())
    nv=len(V);ne=len(E);nf=len(F)
    E=sorted(E,key=lambda e:sorted(e))
    ei={e:i for i,e in enumerate(E)}
    perms=automorphisms(nv,E)
    eperms=[tuple(ei[frozenset((p[a],p[b]))] for a,b in (tuple(sorted(x)) for x in E)) for p in perms]
    Fsets=[set(f) for f in F]
    fmask=[]
    for f in Fsets:
        m=0
        for v1,v2 in itertools.combinations(sorted(f),2):
            key=frozenset((v1,v2))
            if key in ei: m|=1<<ei[key]
        fmask.append(m)
    e2f=[[] for _ in range(ne)]
    for fi,m in enumerate(fmask):
        for e in range(ne):
            if m>>e&1: e2f[e].append(fi)
    if name in ('icosahedron','dodecahedron'): one,zero=Q5(1),Q5(0)
    else: one,zero=Fr(1),Fr(0)
    rot_idx=[i for i,p in enumerate(perms) if det_of_perm(p,V,one,zero)==one]
    d=len(adjacency(nv,E)[0]); L=len(Fsets[0])
    return dict(name=name,V=nv,E=ne,F=nf,L=L,d=d,Vcoords=V,Elist=E,Flist=Fsets,ei=ei,
                perms=perms,eperms=eperms,rot_idx=rot_idx,nrot=len(rot_idx),
                fmask=fmask,e2f=e2f)

# ---------------- profile counting / Burnside ----------------
def binom(n,k):
    if k<0 or k>n: return 0
    r=1
    for i in range(k): r=r*(n-i)//(i+1)
    return r

def edge_order(S):
    ne=S['E']; e2f=S['e2f']
    order=[]; remaining=set(range(ne)); covered=[0]*S['F']
    while remaining:
        best=None; bestscore=None
        for e in sorted(remaining):
            score=tuple(sorted((covered[f] for f in e2f[e]),reverse=True))
            if bestscore is None or score>bestscore: best=e; bestscore=score
        order.append(best); remaining.discard(best)
        for f in e2f[best]: covered[f]+=1
    return order

def count_profiles(S,K,kmin=0,want=3):
    ne=S['E']; e2f=S['e2f']
    order=edge_order(S)
    fcomplete={}
    for pos,e in enumerate(order):
        for f in e2f[e]: fcomplete[f]=max(fcomplete.get(f,0),pos)
    count=0; witnesses=[]
    kap=[0]*ne; fsum=[0]*S['F']
    def rec(i,rem):
        nonlocal count
        if i==ne:
            if rem==0 and all(x%2==0 for x in fsum):
                count+=1
                if len(witnesses)<want: witnesses.append(tuple(kap))
            return
        e=order[i]; left=ne-i
        if rem<kmin*left: return
        for x in range(kmin,rem-kmin*(left-1)+1):
            kap[e]=x
            for f in e2f[e]: fsum[f]+=x
            ok=True
            for f in e2f[e]:
                if fcomplete.get(f)==i and fsum[f]%2: ok=False;break
            if ok: rec(i+1,rem-x)
            for f in e2f[e]: fsum[f]-=x
        kap[e]=0
    rec(0,K)
    return count,witnesses

def orbit_masks(S,eperm):
    ne=S['E']; seen=[False]*ne; data=[]
    for e in range(ne):
        if seen[e]: continue
        o=[];cur=e
        while not seen[cur]:
            seen[cur]=True;o.append(cur);cur=eperm[cur]
        fc={}
        for x in o:
            for f in S['e2f'][x]: fc[f]=fc.get(f,0)+1
        m=0
        for f,c in fc.items():
            if c%2: m|=1<<f
        data.append((len(o),m))
    return data

def fix_count(S,odata,K):
    dp={(0,0):1}
    for (sz,m) in odata:
        nd={}; xmax=K//sz
        for (cs,cm),cnt in dp.items():
            for x in range(xmax+1):
                ns=cs+sz*x
                if ns>K: break
                nm=cm^(m if x%2 else 0)
                nd[(ns,nm)]=nd.get((ns,nm),0)+cnt
        dp=nd
    return dp.get((K,0),0)

def burnside(S,K,idx=None):
    perms=S['eperms'] if idx is None else [S['eperms'][i] for i in idx]
    memo={}; tot=0
    for ep in perms:
        od=orbit_masks(S,ep)
        sig=tuple(sorted(od))
        if sig not in memo: memo[sig]=fix_count(S,od,K)
        tot+=memo[sig]
    n=len(perms)
    assert tot%n==0
    return tot//n

def orbit_count_direct(S,K):
    ne=S['E']; eperms=S['eperms']
    seen=set(); orbits=0
    def rec(i,rem,cur,out):
        if i==ne:
            if rem==0: out.append(tuple(cur))
            return
        for x in range(0,rem+1):
            cur.append(x); rec(i+1,rem-x,cur,out); cur.pop()
    profs=[]; rec(0,K,[],profs)
    for kap in profs:
        ok=True
        for m in S['fmask']:
            ssum=0
            for e in range(ne):
                if m>>e&1: ssum+=kap[e]
            if ssum%2: ok=False;break
        if not ok or kap in seen: continue
        orbits+=1
        for ep in eperms: seen.add(tuple(kap[ep[e]] for e in range(ne)))
        seen.add(kap)
    return orbits

def face_bicolor(S):
    nf=S['F']; fmask=S['fmask']
    adj=[set() for _ in range(nf)]
    for e in range(S['E']):
        fs=[f for f in range(nf) if fmask[f]>>e&1]
        assert len(fs)==2
        adj[fs[0]].add(fs[1]); adj[fs[1]].add(fs[0])
    color=[None]*nf
    for s0 in range(nf):
        if color[s0] is not None: continue
        color[s0]=0; q=[s0]
        while q:
            u=q.pop()
            for w in adj[u]:
                if color[w] is None: color[w]=color[u]^1; q.append(w)
                elif color[w]==color[u]: return None
    return color

def strict_min(S):
    ne=S['E']; nf=S['F']; L=S['L']
    syn=[L%2]*nf
    sol=gf2_solve(S['fmask'],syn,ne)
    assert sol is not None
    x0,ker=sol
    best=None; bestvecs=[]
    for combo in range(1<<len(ker)):
        v=x0; c=combo; j=0
        while c:
            if c&1: v^=ker[j]
            c>>=1; j+=1
        w=bin(v).count('1')
        if best is None or w<best: best=w; bestvecs=[v]
        elif w==best: bestvecs.append(v)
    return best,bestvecs

def strict_min_orbits(S,bestvecs):
    canon=set(); norb=0
    for v in bestvecs:
        tup=tuple((v>>e)&1 for e in range(S['E']))
        sig=min(tuple(tup[ep[e]] for e in range(S['E'])) for ep in S['eperms'])
        if sig not in canon: canon.add(sig); norb+=1
    return norb

def g_formula(N):
    from math import factorial
    tot=0
    for b in range(N//3+1):
        rem=N-3*b
        if rem%2: continue
        a=rem//2
        tot+=factorial(N)//(factorial(a)*factorial(b)*(2**a)*(6**b))
    return tot

def g_terms(N):
    from math import factorial
    out=[]
    for b in range(N//3+1):
        rem=N-3*b
        if rem%2: continue
        a=rem//2
        out.append((a,b,factorial(N)//(factorial(a)*factorial(b)*(2**a)*(6**b))))
    return out

def g_enum(N):
    def rec(remaining):
        if not remaining: return 1
        rest=remaining[1:]
        tot=0
        for i in range(len(rest)):
            tot+=rec(rest[:i]+rest[i+1:])
        for i in range(len(rest)):
            for j in range(i+1,len(rest)):
                tot+=rec(rest[:i]+rest[i+1:j]+rest[j+1:])
        return tot
    return rec(list(range(N)))

def char_sum_A(S,K):
    nf=S['F']; ne=S['E']
    cols=[]
    for e in range(ne):
        m=0
        for f in range(nf):
            if S['fmask'][f]>>e&1: m|=1<<f
        cols.append(m)
    tot=0; allmask=(1<<nf)-1; reps=set()
    for s0 in range(1<<nf):
        canon=min(s0,s0^allmask)
        if canon in reps: continue
        reps.add(canon)
        poly=[0]*(K+1); poly[0]=1
        for m in cols:
            sign=-1 if bin(s0&m).count('1')%2 else 1
            np=[0]*(K+1)
            for d in range(K+1):
                if poly[d]==0: continue
                zz=1
                for j in range(0,K-d+1):
                    np[d+j]+=poly[d]*zz
                    zz*=sign
            poly=np
        tot+=poly[K]
    assert len(reps)==2**(nf-1)
    assert tot%2**(nf-1)==0
    return tot//2**(nf-1)

def incidence_B(S):
    return [[1 if S['fmask'][f]>>e&1 else 0 for e in range(S['E'])] for f in range(S['F'])]
