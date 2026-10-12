
"""Platonic solid machinery: exact encodings, automorphism groups, GF(2)/SNF lattice data,
admissible-profile counts, Burnside degeneracies, minimality regimes, defect radicals.
Exact arithmetic only (int / Fraction / Q(sqrt5))."""
import sys, itertools
from fractions import Fraction
sys.path.insert(0, '/home/user/scratch')
from q5 import Q5, gf2_rank, gf2_solve, snf, det3

def binom(n,k):
    if k<0 or k>n: return 0
    r=1
    for i in range(k): r = r*(n-i)//(i+1)
    return r

# ------------------ solid encodings ------------------
def build_tetra():
    V=[(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)]
    V=[tuple(Fraction(x) for x in v) for v in V]
    E=[frozenset(p) for p in itertools.combinations(range(4),2)]
    F=[frozenset({0,1,2,3}-{v}) for v in range(4)]
    return V,E,F

def build_cube():
    V=[(Fraction(a),Fraction(b),Fraction(c)) for a in(-1,1) for b in(-1,1) for c in(-1,1)]
    def d2(u,v): return sum((a-b)**2 for a,b in zip(u,v))
    E=[frozenset((i,j)) for i in range(8) for j in range(i+1,8) if d2(V[i],V[j])==4]
    F=[]
    for ax in range(3):
        for s in (-1,1):
            vs=[i for i in range(8) if V[i][ax]==s]
            F.append(frozenset(vs))
    return V,E,F

def build_octa():
    V=[]
    for ax in range(3):
        for s in (-1,1):
            v=[Fraction(0)]*3; v[ax]=Fraction(s); V.append(tuple(v))
    def anti(u,v): return all(a==-b for a,b in zip(u,v))
    E=[frozenset((i,j)) for i in range(6) for j in range(i+1,6) if not anti(V[i],V[j])]
    F=[]
    for s1 in(-1,1):
        for s2 in(-1,1):
            for s3 in(-1,1):
                idx=[]
                for ax,s in ((0,s1),(1,s2),(2,s3)):
                    for i in range(6):
                        e=[Fraction(0)]*3; e[ax]=Fraction(s)
                        if tuple(e)==V[i]: idx.append(i)
                F.append(frozenset(idx))
    return V,E,F

def build_icosa():
    phi = Q5(Fraction(1,2), Fraction(1,2))  # (1+sqrt5)/2
    verts=[]
    for s1 in (-1,1):
        for s2 in (-1,1):
            verts.append((Q5(0), Q5(s1), Q5(s2)*phi))
            verts.append((Q5(s1), Q5(s2)*phi, Q5(0)))
            verts.append((Q5(s2)*phi, Q5(0), Q5(s1)))
    def d2(u,v):
        s=Q5(0)
        for a,b in zip(u,v):
            dd=a-b; s=s+dd*dd
        return s
    E=[frozenset((i,j)) for i in range(12) for j in range(i+1,12) if d2(verts[i],verts[j])==Q5(4)]
    F=[frozenset(c) for c in itertools.combinations(range(12),3)
       if frozenset((c[0],c[1])) in E and frozenset((c[0],c[2])) in E and frozenset((c[1],c[2])) in E]
    return verts,E,F

def build_dodeca(icosa=None):
    Vi,Ei,Fi = icosa if icosa else build_icosa()
    # dodecahedron vertices = icosa face centers
    ctr=[]
    for f in Fi:
        s=[Q5(0),Q5(0),Q5(0)]
        for v in sorted(f):
            for k in range(3): s[k]=s[k]+Vi[v][k]
        ctr.append(tuple(x*Q5(Fraction(1,3)) for x in s))
    n=len(ctr)
    # edges: faces sharing an icosa edge
    E=[]
    for a in range(n):
        for b in range(a+1,n):
            if len(Fi[a] & Fi[b])==2: E.append(frozenset((a,b)))
    # faces: per icosa vertex, the centers of faces containing it
    F=[]
    for v in range(12):
        F.append(frozenset(i for i in range(n) if v in Fi[i]))
    return ctr,E,F

SOLIDS={}
SOLIDS['tetrahedron']=build_tetra()
SOLIDS['cube']=build_cube()
SOLIDS['octahedron']=build_octa()
_ic=build_icosa()
SOLIDS['icosahedron']=_ic
SOLIDS['dodecahedron']=build_dodeca(_ic)

def edge_index(E):
    return {e:i for i,e in enumerate(E)}

def adjacency(nv,E):
    adj=[set() for _ in range(nv)]
    for e in E:
        a,b=sorted(e); adj[a].add(b); adj[b].add(a)
    return adj

def automorphisms(nv,E):
    adj=adjacency(nv,E)
    eset=set(E)
    order=sorted(range(nv), key=lambda v:(-len(adj[v]),v))
    res=[]
    mapping={}
    def rec(k):
        if k==len(order):
            res.append(dict(mapping)); return
        v=order[k]
        img=set(range(nv))-set(mapping.values())
        for u in order[:k]:
            w=mapping[u]
            if u in adj[v]: img &= adj[w]
            else: img -= adj[w]
        for w in sorted(img):
            mapping[v]=w
            rec(k+1)
            del mapping[v]
    rec(0)
    return [tuple(m[v] for v in range(nv)) for m in res]

def det_of_perm(perm,V,field_one,field_zero):
    # build linear map from images of 3 independent vertices
    # find 3 vertices whose coordinate matrix is invertible
    import itertools as it
    for combo in it.combinations(range(len(V)),3):
        M=[[V[c][k] for c in combo] for k in range(3)]  # columns = vertices
        if det3(M)==field_zero: continue
        Mi=inv3_exact(M,field_one,field_zero)
        W=[[V[perm[c]][k] for c in combo] for k in range(3)]
        A=matmul3(W,Mi,field_zero)
        return det3(A)
    raise RuntimeError("no independent triple")

def matmul3(A,B,zero):
    n=3
    C=[[zero]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            acc=zero
            for t in range(n):
                if A[i][t]!=zero and B[t][j]!=zero: acc=acc+A[i][t]*B[t][j]
            C[i][j]=acc
    return C

def inv3_exact(M,one,zero):
    d=det3(M)
    assert d!=zero
    (a,b,c),(dd,e,f),(g,h,i)=M
    adj=[[e*i-f*h, c*h-b*i, b*f-c*e],
         [f*g-dd*i, a*i-c*g, c*dd-a*f],
         [dd*h-e*g, b*g-a*h, a*e-b*dd]]
    return [[x/d for x in row] for row in adj]

def rotation_subgroup(name,V,perms):
    if name in ('icosahedron','dodecahedron'):
        one,zero=Q5(1),Q5(0)
    else:
        one,zero=Fraction(1),Fraction(0)
    rots=[]
    for p in perms:
        d=det_of_perm(p,V,one,zero)
        if d==one: rots.append(p)
    return rots

# ------------------ derived data per solid ------------------
def solid_data(name):
    V,E,F=SOLIDS[name]
    nv=len(V); ne=len(E); nf=len(F)
    ei=edge_index(E)
    perms=automorphisms(nv,E)
    # edge permutation per automorphism
    eperms=[]
    for p in perms:
        eperms.append(tuple(ei[frozenset((p[a],p[b]))] for a,b in (tuple(sorted(e)) for e in E)))
    # face permutation
    Fsets=[set(f) for f in F]
    fperms=[]
    for p in perms:
        fp=[]
        for fi,f in enumerate(Fsets):
            img=frozenset(p[v] for v in f)
            fp.append(Fsets.index(set(img)))
        fperms.append(tuple(fp))
    rots=rotation_subgroup(name,V,perms)
    rot_set=set(rots)
    rot_idx=[i for i,p in enumerate(perms) if p in rot_set]
    return dict(name=name,V=nv,E=ne,F=nf,L=len(F[0]),d=len(adjacency(nv,E)[0]),
                Vcoords=V,Elist=E,Flist=Fsets,ei=ei,perms=perms,eperms=eperms,
                fperms=fperms,rot_idx=rot_idx,nrot=len(rots))

if __name__=='__main__':
    import pickle
    data={}
    for name in ['tetrahedron','cube','octahedron','dodecahedron','icosahedron']:
        data[name]=solid_data(name)
        S=data[name]
        print(f"{name}: V={S['V']} E={S['E']} F={S['F']} L={S['L']} d={S['d']} |Aut|={len(S['perms'])} |Rot|={S['nrot']}")
        assert S['V']-S['E']+S['F']==2
        assert S['F']*S['L']==2*S['E']
        assert S['V']*S['d']==2*S['E']
    with open('/home/user/scratch/soliddata.pkl','wb') as f:
        # store minimal (coords for Q5 not picklable? they are - plain classes)
        pickle.dump({k:{kk:vv for kk,vv in v.items() if kk!='Vcoords'} for k,v in data.items()}, f)
    print("OK")
