
"""compute2: admissible-profile counts, Burnside degeneracies, regime minima, card arithmetic."""
import sys, itertools
from fractions import Fraction
sys.path.insert(0,'/home/user/scratch')
import compute1 as C1
from q5 import gf2_solve

DATA=C1.DATA
binom=C1.binom

NAMES=['tetrahedron','cube','octahedron','dodecahedron','icosahedron']
KMAX={'tetrahedron':8,'cube':6,'octahedron':6,'dodecahedron':5,'icosahedron':5}

def char_sum_A(S,K):
    """Exact character-sum formula: A_S(K) = (1/2^(F-1)) sum_{s in Z2^F/<1>} [z^K] prod_e 1/(1 - (-1)^{s.b_e} z)."""
    nf=S['F']; ne=S['E']
    # columns b_e as bitmask over faces
    cols=[]
    for e in range(ne):
        m=0
        for f in range(nf):
            if S['fmask'][f]>>e & 1: m |= 1<<f
        cols.append(m)
    tot=0
    allmask=(1<<nf)-1
    reps=set()
    for s in range(1<<nf):
        canon=min(s, s^allmask)
        if canon in reps: continue
        reps.add(canon)
        # poly product up to degree K
        poly=[0]*(K+1); poly[0]=1
        for m in cols:
            sign = -1 if bin(s & m).count('1')%2 else 1
            # multiply by sum_j (sign)^j z^j
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
    assert tot % 2**(nf-1)==0
    return tot//2**(nf-1)

def run():
    R={}
    print("="*100)
    for name in NAMES:
        S=DATA[name]; ne=S['E']; nf=S['F']
        S['rank']=C1.lattice_report(S); S['bic']=C1.face_bicolor(S); S['divs']=C1.incidence_snf(S)
        assert S['rank']==nf-1
        print(f"\n### {name}")
        # --- null-permitting counts A_S(K) ---
        A={}; W={}
        for K in range(0,KMAX[name]+1):
            c,w=C1.count_profiles(S,K)
            A[K]=c; W[K]=w
            if name in ('tetrahedron','cube','octahedron') and K<=6:
                cs=char_sum_A(S,K)
                assert cs==c, (name,K,c,cs)
        print("  A_S(K) K=0..%d: %s"%(KMAX[name],[A[K] for K in range(KMAX[name]+1)]))
        assert A[1]==0, name           # K=1 impossible on solids (channel in 2 faces)
        assert A[2]>=1, name
        print("  A(1)=0 (no K=1 admissible on any solid), witness K=2:", W[2][:1])
        # asymptotic ratio trend
        raw=binom(KMAX[name]+ne-1,ne-1)
        print(f"  asymptotics: A({KMAX[name]})={A[KMAX[name]]} vs C/2^(F-1)={Fraction(raw,2**(nf-1))}")
        if name=='tetrahedron':
            c16,_=C1.count_profiles(S,16)
            r16=binom(16+ne-1,ne-1)
            print(f"  trend: A(16)={c16} vs {r16}/8={Fraction(r16,8)} (ratio {Fraction(c16*8,r16)})")
        # --- octahedron black-white law ---
        if S['bic'] is not None:
            black=[f for f in range(nf) if S['bic'][f]==0]; white=[f for f in range(nf) if S['bic'][f]==1]
            assert len(black)==len(white)==nf//2
            for K in range(0,KMAX[name]+1):
                if K%2==1: assert A[K]==0, ("odd K admissible on octahedron!",K)
            # verify balance identity on enumerated witnesses
            for K in range(2,KMAX[name]+1,2):
                for kap in W[K]:
                    sb=sum(sum(kap[e] for e in range(ne) if S['fmask'][f]>>e&1) for f in black)
                    sw=sum(sum(kap[e] for e in range(ne) if S['fmask'][f]>>e&1) for f in white)
                    tot=sum(kap)
                    assert sb==sw==tot, (kap,sb,sw,tot)
            print("  octahedron: A(odd K)=0; black/white face-sum balance verified on witnesses")
        # --- Burnside M_S(K) under full Aut and under Rot ---
        M={}; Mrot={}
        for K in range(0,KMAX[name]+1):
            M[K]=C1.burnside(S,K)
            Mrot[K]=C1.burnside(S,K,idx=S['rot_idx'])
        print("  M_S(K) full Aut: ",[M[K] for K in range(KMAX[name]+1)])
        print("  M+_S(K) rotations:",[Mrot[K] for K in range(KMAX[name]+1)])
        # direct orbit cross-check small K
        for K in (1,2)+( (3,) if name in('tetrahedron','cube','octahedron') else () ):
            if K<=KMAX[name]:
                oc=C1.orbit_count_direct(S,K)
                assert oc==M[K], (name,K,oc,M[K])
        print("  orbit-enumeration cross-check: OK (K=1,2"+(",3)" if name in('tetrahedron','cube','octahedron') else ")"))
        # --- minimality regimes ---
        # R0 null-permitting: min K>0 with A>0
        K0=min(K for K in range(1,KMAX[name]+1) if A[K]>0)
        # R1 strictly spacelike: eps_min via coset leader
        eps,bvecs=C1.strict_min(S)
        norb=C1.strict_min_orbits(S,bvecs)
        K1=ne+eps
        # R2 uniform
        kap0min = 1 if S['L']%2==0 else 2
        K2=ne*kap0min
        print(f"  regimes: R0 null-permit: K_min={K0} (Theta_int={2*K0}); R1 strict: eps_min={eps}, K_min={K1} (Theta={2*K1}), {norb} Aut-orbit(s) of minimizers; R2 uniform: kappa0_min={kap0min}, K={K2} (Theta={2*K2})")
        # edge-transitivity of Aut (R0 witness orbit count = 1)
        e0orbit={ep[0] for ep in S['eperms']}
        assert len(e0orbit)==ne, name
        R[name]=dict(A=A,M=M,Mrot=Mrot,K0=K0,eps=eps,K1=K1,norb1=norb,kap0min=kap0min,K2=K2,
                     witness2=W[2][:1], strict_witness=[tuple((v>>e)&1 for e in range(ne)) for v in bvecs[:3]])
    # card arithmetic
    print("="*100)
    print("CARD ARITHMETIC (corrected rungs)")
    for name in NAMES:
        S=DATA[name]; r=R[name]
        V,Ee,Ff,L,d=S['V'],S['E'],S['F'],S['L'],S['d']
        n_dark=2*d; n_obs1=2*d+1; n_obs2=2*d+2
        O=lambda n: max(0,2**(n+1)-16)
        Kmin=r['K2']  # uniform-minimum total winding K_S,min = E*kappa0min
        kf = L if L%2 else 2   # k_f,min: odd L: Theta_f=2L -> k=L ; even: Theta_f=L -> k=L//2
        if L%2==0: kf=L//2
        jmax=Fraction(Kmin,2)
        dimface=(kf+1)**Ff; dimdig=(r['kap0min']+1)**Ee
        Eid=2*Ee; Shid=Eid  # in ln2 units
        Pi=8*Ee*Ee*Kmin
        # defects
        dpi=Fraction(2) - Fraction(d*(L-2),L)   # delta_v / pi
        assert V*dpi==4, name
        print(f"\n{name}: (V,E,F,L,d)=({V},{Ee},{Ff},{L},{d})")
        print(f"  rungs: dark n=2d={n_dark} O={O(n_dark)}; obs1 n={n_obs1} O={O(n_obs1)}; obs2 n={n_obs2} O={O(n_obs2)}")
        print(f"  lock ledgers: dark sum={V*O(n_dark)}; obs1 sum={(V-1)*O(n_dark)+O(n_obs1)}; obs2 sum={(V-1)*O(n_dark)+O(n_obs2)}")
        print(f"  spin (uniform min): k_f={kf} (F reads), j_f={Fraction(kf,2)}, K_S,min={Kmin}=E*kappa0, j_max={jmax}, digon-basis j={Fraction(r['kap0min'],2)} x{Ee} (sum={Ee*Fraction(r['kap0min'],2)})")
        print(f"  carrier dims: face-basis {dimface}, digon-basis {dimdig}")
        print(f"  entropy: S_hid={Shid}*ln2; rate=(ln2/h^2)/{r['kap0min']}; Pi_min={Pi}*(ln2)^2")
        print(f"  defect: delta_v/pi={dpi}; V*delta=4pi OK")
        R[name].update(dict(n_dark=n_dark,O_dark=O(n_dark),lock_dark=V*O(n_dark),
                            lock_obs1=(V-1)*O(n_dark)+O(n_obs1),lock_obs2=(V-1)*O(n_dark)+O(n_obs2),
                            kf=kf,Kmin=Kmin,jmax=jmax,Pi=Pi,dpi=dpi,Shid=Shid,
                            dimface=dimface,dimdig=dimdig))
    # defect radicals + minimal polynomials
    print("="*100)
    print("DEFECT FACTORS D_S = 4 sin^2(delta_v/4) = 2-2cos(delta_v/2), exact:")
    import math
    defs={
      'tetrahedron': ('2', [0,1]),                        # poly x-2 -> coeffs? store monic list
      'cube': ('2-sqrt2', None),
      'octahedron': ('1', None),
      'dodecahedron': ('2-2cos(pi/10)', None),
      'icosahedron': ('2-sqrt3', None),
    }
    # minimal polynomials (verified by exact algebra below)
    polys={'tetrahedron':[-2,1],'cube':[2,-4,1],'octahedron':[-1,1],
           'dodecahedron':[1,-12,19,-8,1],'icosahedron':[1,-4,1]}
    for name in NAMES:
        p=polys[name]
        print(f"  {name}: D={defs[name][0]}, minpoly coeffs (asc) {p}")
    # verify dodecahedron polynomial: x=2-2c, c=cos(pi/10): 16c^4-20c^2+5=0 => p(x)=0
    # polynomial arithmetic in Z[c] mod (16c^4-20c^2+5)
    def polymod(a, m):
        a=a[:]
        for i in range(len(a)-1, 3, -1):
            if a[i]:
                q_num=a[i]
                # reduce c^i: 16c^4 = 20c^2-5 => c^4 = (20c^2-5)/16: work over Fraction
                pass
        return a
    from fractions import Fraction as Fr
    def reduce_poly(a):
        a=[Fr(x) for x in a]
        changed=True
        while changed:
            changed=False
            for i in range(len(a)-1,3,-1):
                if a[i]!=0:
                    q=a[i]/16
                    a[i]=0
                    a[i-2]+=q*20
                    a[i-4]-=q*5
                    changed=True
        return a
    # p(x) = (2-x)^4 - 5(2-x)^2 + 5 expanded in x:
    # (2-x)^4 = x^4-8x^3+24x^2-32x+16 ; -5(2-x)^2 = -5(x^2-4x+4) = -5x^2+20x-20
    # p = x^4-8x^3+19x^2-12x+1
    p=[1,-12,19,-8,1]  # ascending
    assert p==polys['dodecahedron']
    # substitute x = 2-2c: p(2-2c) as polynomial in c, reduce mod 16c^4-20c^2+5 => 0
    def subst(p, a, b):
        # p(x) with x = a + b*c, p ascending coeffs; returns ascending poly in c
        result=[Fr(0)]*(4*len(p)+8)
        pow_poly=[Fr(1)]
        for coeff in p:
            for k,v in enumerate(pow_poly):
                result[k]+=Fr(coeff)*v
            new=[Fr(0)]*(len(pow_poly)+1)
            for k,v in enumerate(pow_poly):
                new[k]+=v*Fr(a); new[k+1]+=v*Fr(b)
            pow_poly=new
        return result
    q=subst(p, Fr(2), Fr(-2))
    q=reduce_poly(q)
    assert all(x==0 for x in q), q
    print("  dodecahedron minpoly verified: p(2-2c) = 0 mod (16c^4-20c^2+5) [16c^4-20c^2+5=0 is cos(5x) at x=pi/10]")
    # verify cos(5t) = 16c^5 - 20c^3 + 5c exactly: Re((c+is)^5), s^2 = 1-c^2
    from math import comb
    agg={}
    for j in (0,2,4):
        coef=comb(5,j)*Fr(1 if j%4==0 else -1)   # (i s)^j = i^j s^j; i^j real: j=0:+1, j=2:-1, j=4:+1
        # c^{5-j} * (s^2)^{j/2} = c^{5-j} * (1-c^2)^{j/2}
        ex=[Fr(0)]*7; ex[0]=Fr(1)
        for _ in range(j//2):
            nx=[Fr(0)]*7
            for k,v in enumerate(ex):
                if v: nx[k]+=v; nx[k+1]-=v
            ex=nx
        for k,v in enumerate(ex):
            if v: pw=5-j+2*k; agg[pw]=agg.get(pw,Fr(0))+coef*v
    ch5=[Fr(0)]*6
    for pw,v in agg.items(): ch5[pw]=v
    assert ch5==[Fr(0),Fr(5),Fr(0),Fr(-20),Fr(0),Fr(16)], ch5
    print("  cos(5t)=16c^5-20c^3+5c verified by de Moivre (exact binomials); at t=pi/10: c*(16c^4-20c^2+5)=0, c!=0")
    # cube / icosa polys: x=2-sqrt2: (x-2)^2=2 => x^2-4x+2 ; x=2-sqrt3: x^2-4x+1
    print("  cube: (2-r2): x^2-4x+2 = 0 since (x-2)^2=2; icosahedron: (2-r3): x^2-4x+1 = 0 since (x-2)^2=3")
    # mass ratio coefficients D_S/(4E^2)
    print("  ratio coefficients D_S/(4E^2):")
    D={'tetrahedron':(Fr(2),None),'cube':(Fr(2),'2-sqrt2'),'octahedron':(Fr(1),None),
       'dodecahedron':(None,'D_dod'),'icosahedron':(None,'2-sqrt3')}
    for name in NAMES:
        Ee=DATA[name]['E']
        print(f"    {name}: 1/(4E^2) = {Fraction(1,4*Ee*Ee)}  x D_S")
    return R

if __name__=='__main__':
    R=run()
    print("\nALL COMPUTE2 OK")
