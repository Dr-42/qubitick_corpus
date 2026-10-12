
"""Master scratch computation : Platonic lattices, admissible loops, Burnside degeneracies,
minimality regimes, defects, sealing counts, rung audit. Exact arithmetic only."""
import sys, itertools
from fractions import Fraction
sys.path.insert(0, '/home/user/scratch')
import solids as SL
from q5 import gf2_rank, gf2_solve, snf

def binom(n,k):
    if k<0 or k>n: return 0
    r=1
    for i in range(k): r=r*(n-i)//(i+1)
    return r

RESULTS={}

def build_all():
    data={}
    for name in ['tetrahedron','cube','octahedron','dodecahedron','icosahedron']:
        S=SL.solid_data(name)
        ne=S['E']; nf=S['F']
        # face-edge incidence: face f bitmask over edges
        fmask=[]
        for f in S['Flist']:
            m=0
            for v1,v2 in itertools.combinations(sorted(f),2):
                key=frozenset((v1,v2))
                if key in S['ei']: m |= 1<<S['ei'][key]
            fmask.append(m)
        S['fmask']=fmask
        # edge -> faces
        e2f=[[] for _ in range(ne)]
        for fi,m in enumerate(fmask):
            for e in range(ne):
                if m>>e & 1: e2f[e].append(fi)
        S['e2f']=e2f
        data[name]=S
    return data

DATA=build_all()

# ---------- GF(2) rank of face-incidence map (all five) ----------
def lattice_report(S):
    rank,_=gf2_rank(S['fmask'], S['E'])
    return rank

# ---------- face 2-colorability (dual bipartite) ----------
def face_bicolor(S):
    nf=S['F']; fmask=S['fmask']
    # dual adjacency: faces sharing an edge
    adj=[set() for _ in range(nf)]
    for e in range(S['E']):
        fs=[f for f in range(nf) if fmask[f]>>e & 1]
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

# ---------- A_S(K): admissible profiles, kappa>=0, sum=K, all face sums even ----------
def count_profiles(S,K,nonneg=True,kmin=0):
    """DFS with pruning. Returns (count, list_of_witnesses (capped))."""
    ne=S['E']; e2f=S['e2f']; L=S['L']
    fmask=S['fmask']
    # order edges so faces complete early: greedy by faces
    order=[]
    remaining=set(range(ne))
    faces_sorted=sorted(range(S['F']), key=lambda f: bin(S['fmask'][f]).count('1'))
    covered=[0]*S['F']
    while remaining:
        # pick edge maximizing newly-completable faces
        best=None; bestscore=None
        for e in remaining:
            score=tuple(sorted((covered[f] for f in e2f[e]),reverse=True))
            if bestscore is None or score>bestscore: best=e; bestscore=score
        order.append(best); remaining.discard(best)
        for f in e2f[best]: covered[f]+=1
    pos={e:i for i,e in enumerate(order)}
    # for each face: positions of its edges in order
    fpos=[[pos[e] for e in range(ne) if fmask[f]>>e & 1] for f in range(S['F'])]
    fcomplete=[max(fp) for fp in fpos]
    count=0; witnesses=[]
    kap=[0]*ne
    fsum=[0]*S['F']
    def rec(i, rem):
        nonlocal count
        if rem<0: return
        if i==ne:
            if rem==0 and all(s%2==0 for s in fsum):
                count+=1
                if len(witnesses)<3: witnesses.append(tuple(kap))
            return
        e=order[i]
        hi=rem
        for x in range(kmin,hi+1):
            kap[e]=x
            for f in e2f[e]: fsum[f]+=x
            # prune: completed faces must be even
            ok=True
            for f in e2f[e]:
                if fcomplete[f]==i and fsum[f]%2: ok=False; break
            if ok: rec(i+1, rem-x)
            for f in e2f[e]: fsum[f]-=x
            if x==0 and kmin==0:
                pass
            if nonneg and x>=1 and rem-x < 0: break
            if x==kmin and kmin>0: pass
        kap[e]=0
    # simpler: iterate x from kmin..rem
    def rec2(i, rem):
        nonlocal count
        if i==ne:
            if rem==0 and all(s%2==0 for s in fsum):
                count+=1
                if len(witnesses)<3: witnesses.append(tuple(kap))
            return
        e=order[i]
        nedges_left=ne-i
        lo=kmin*nedges_left
        if rem<lo: return
        for x in range(kmin, rem-lo+kmin*0+1):
            if rem-x < kmin*(nedges_left-1): continue
            kap[e]=x
            for f in e2f[e]: fsum[f]+=x
            ok=True
            for f in e2f[e]:
                if fcomplete[f]==i and fsum[f]%2: ok=False; break
            if ok: rec2(i+1, rem-x)
            for f in e2f[e]: fsum[f]-=x
        kap[e]=0
    rec2(0,K)
    return count,witnesses

# ---------- Burnside fix(g,K) via orbit DP ----------
def orbit_masks(S, eperm):
    ne=S['E']
    seen=[False]*ne; orbits=[]
    for e in range(ne):
        if seen[e]: continue
        o=[]; cur=e
        while not seen[cur]:
            seen[cur]=True; o.append(cur); cur=eperm[cur]
        orbits.append(o)
    # orbit data: (size, face-parity mask: faces with odd intersection)
    data=[]
    for o in orbits:
        m=0
        fcount={}
        for e in o:
            for f in S['e2f'][e]: fcount[f]=fcount.get(f,0)+1
        for f,c in fcount.items():
            if c%2: m|=1<<f
        data.append((len(o),m))
    return data

def fix_count(S, odata, K):
    # DP over orbits: dict (sum, paritymask)->count
    dp={(0,0):1}
    for (s,m) in odata:
        nd={}
        xmax=K//s
        for (cs,cm),cnt in dp.items():
            for x in range(xmax+1):
                ns=cs+s*x
                if ns>K: break
                nm=cm ^ (m if x%2 else 0)
                key=(ns,nm)
                nd[key]=nd.get(key,0)+cnt
        dp=nd
    return dp.get((K,0),0)

def burnside(S,K,idx=None):
    perms=S['eperms'] if idx is None else [S['eperms'][i] for i in idx]
    memo={}
    tot=0
    for ep in perms:
        od=tuple(orbit_masks(S,ep))
        sig=tuple(sorted((s,m) for s,m in od))
        if sig not in memo: memo[sig]=fix_count(S,od,K)
        tot+=memo[sig]
    n=len(perms)
    assert tot%n==0, (S['name'],K,tot,n)
    return tot//n

def orbit_count_direct(S,K):
    """Independent cross-check: enumerate profiles, group into Aut-orbits by canonical form."""
    ne=S['E']
    eperms=S['eperms']
    seen=set(); orbits=0
    def gen(K, allow_zero=True):
        out=[]
        def rec(i,rem,cur):
            if i==ne:
                if rem==0: out.append(tuple(cur))
                return
            for x in range(0,rem+1):
                if rem-x < 0: break
                cur.append(x); rec(i+1,rem-x,cur); cur.pop()
        rec(0,K,[])
        return out
    for kap in gen(K):
        # parity filter
        ok=True
        for m in S['fmask']:
            s=0
            for e in range(ne):
                if m>>e&1: s+=kap[e]
            if s%2: ok=False; break
        if not ok: continue
        if kap in seen: continue
        orbits+=1
        for ep in eperms:
            img=tuple(kap[ep[e]] for e in range(ne))  # careful: action direction consistent
            seen.add(img)
        seen.add(kap)
    return orbits

# ---------- strictly-spacelike minima via coset leaders ----------
def strict_min(S):
    """kappa>=1: kappa=1+x, x>=0, sum(x)=eps; parity: L + (Bx)_f even => Bx = L+1 mod 2 per face."""
    ne=S['E']; nf=S['F']; L=S['L']
    syn=nf*[L%2]  # need Bx ≡ syn? face sum = L + sum x_e over f: even => sum x ≡ L (mod 2)
    syn=[L%2]*nf
    rows=[]  # B rows as bitmask over columns(edges): row f = fmask[f]
    sol=gf2_solve(S['fmask'],syn,ne)
    assert sol is not None
    x0,ker,piv,rref=sol
    # min weight over coset x0 + span(ker)
    best=None; bestvecs=[]
    nk=len(ker)
    for combo in range(1<<nk):
        v=x0
        c=combo; j=0
        while c:
            if c&1: v^=ker[j]
            c>>=1; j+=1
        w=bin(v).count('1')
        if best is None or w<best: best=w; bestvecs=[v]
        elif w==best: bestvecs.append(v)
    # eps_min = best (each x_e in {0,1} at minimum)? careful: x can exceed 1 but min weight = min sum
    return best, bestvecs

def strict_min_orbits(S,bestvecs):
    eperms=S['eperms']
    canon=set(); norb=0
    for v in bestvecs:
        tup=tuple((v>>e)&1 for e in range(S['E']))
        sig=min(tuple(tup[ep[e]] for e in range(S['E'])) for ep in eperms)
        if sig not in canon: canon.add(sig); norb+=1
    return norb

# ---------- SNF of face-edge incidence over Z ----------
def incidence_snf(S):
    nf=S['F']; ne=S['E']
    B=[[1 if S['fmask'][f]>>e&1 else 0 for e in range(ne)] for f in range(nf)]
    return snf(B)

# ---------- sealing grammar g(V) ----------
def g_formula(N):
    from math import factorial
    tot=0
    for b in range(N//3+1):
        rem=N-3*b
        if rem%2: continue
        a=rem//2
        tot+= factorial(N)//(factorial(a)*factorial(b)*(2**a)*(6**b))
    return tot

def g_enum(N):
    # labelled set partitions into parts of size 2,3 (small N)
    from functools import lru_cache
    elems=list(range(N))
    def rec(remaining):
        if not remaining: return 1
        first=remaining[0]; rest=remaining[1:]
        tot=0
        # pair first with one other
        for i in range(len(rest)):
            tot+=rec(rest[:i]+rest[i+1:])
        # triple
        for i in range(len(rest)):
            for j in range(i+1,len(rest)):
                tot+=rec(rest[:i]+rest[i+1:j]+rest[j+1:])
        return tot
    return rec(elems)

# ---------- main report ----------
def main():
    print("="*100)
    for name,S in DATA.items():
        ne=S['E']; nf=S['F']
        rank=lattice_report(S)
        bic=face_bicolor(S)
        divs=incidence_snf(S)
        print(f"\n### {name}: V={S['V']} E={ne} F={nf} L={S['L']} d={S['d']} |Aut|={len(S['perms'])} |Rot|={S['nrot']}")
        print(f"  GF(2) face rank = {rank} (F-1={nf-1}) -> lattice index 2^{rank} = {2**rank}")
        assert rank==nf-1
        print(f"  face 2-colorable (dual bipartite): {bic is not None}")
        print(f"  SNF invariant factors of B: {divs}")
        S['rank']=rank; S['bic']=bic; S['divs']=divs
    print("="*100)
    # g(V) checks
    for name,S in DATA.items():
        V=S['V']
        gf=g_formula(V)
        if V<=8:
            ge=g_enum(V)
            assert gf==ge, (name,gf,ge)
        print(f"g({V}) [{name}] = {gf}" + (f" (enum cross-check ok)" if V<=8 else " (formula)"))
    # even-epsilon parity: V even => b even in every grouping term
    for name,S in DATA.items():
        V=S['V']; assert V%2==0
        for b in range(V//3+1):
            if (V-3*b)%2==0: assert b%2==0, (name,b)
    print("even-V => every sealing grouping has an even number of epsilon-triples: OK")
    return

if __name__=='__main__':
    main()
