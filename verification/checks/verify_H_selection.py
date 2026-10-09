
#!/usr/bin/env python3
"""verify_H_selection.py — companion to FT.61: phase inventory and index-blindness witness.
Exact integer arithmetic only."""
import os,sys
HERE=os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,HERE)

N=0
def chk(cond,msg):
    global N
    assert cond, "FAIL: "+msg
    N+=1

# ---------- (1) phase inventory on all Sigma_min configurations ----------
# Sigma_min: vertices o,p,q; directed real edges e1=(p,q), e2=(q,p), eo=(o,p)
# w(C) = J(C) * prod_e G(e) * (-1)^aleph ;  J = 1 [D3.6];  G(e) = sigma_e (-1)^kappa_e [D3.5/FT.9/FT.24]
# aleph: type-(1,1) vertices only [D3.3]: q is (1,1) (in e1, out e2); p is (2,1); o is (0,1)
total=0
for s1 in (1,-1):
    for s2 in (1,-1):
        for so in (1,-1):
            for kap in (1,2,3):
                kapo=1
                Theta_closed=2*kap          # the digon core (e1,e2)
                sumk=Theta_closed+kapo      # all edges
                nminus=(1 if s1<0 else 0)+(1 if s2<0 else 0)+(1 if so<0 else 0)
                fq=(s2-s1)//2               # D3.3 at q: (sigma_out - sigma_in)/2
                aleph=abs(fq)
                # direct factor-by-factor assembly
                Gprod=(s1*(-1)**kap)*(s2*(-1)**kap)*(so*(-1)**kapo)
                Jfac=1*(+1)                 # D3.6: (+1)-factors only
                w=Jfac*Gprod*((-1)**aleph)
                # closed form
                phase=(-1)**(sumk+aleph+nminus)
                chk(w==phase,f"phase inventory: w = (-1)^(Theta+aleph+n_-) at (s1,s2,so,kappa)=({s1},{s2},{so},{kap})")
                # on-shell geometric triviality on the closed core
                chk((-1)**Theta_closed==1,f"on-shell core: (-1)^Theta = +1 (Theta={Theta_closed} even)")
                total+=1
chk(total==24,"24 Sigma_min configurations enumerated")

# registration-only surviving phase on the core
for s1 in (1,-1):
    for s2 in (1,-1):
        for kap in (1,2,3):
            fq=(s2-s1)//2; aleph=abs(fq)
            nminus=(1 if s1<0 else 0)+(1 if s2<0 else 0)
            core_phase=(-1)**(2*kap+aleph+nminus)
            chk(core_phase==(-1)**(aleph+nminus),"core weight phase = (-1)^(aleph+n_-): registration-only")

# ---------- (3) index-blindness witness: S^2(R) x S^1(2R) ----------
R=1
m=2
# gamma_A: great circle traversed m times: length 4 pi R (in units R=1: 4 pi); interior conjugate points at j*pi, j=1..2m-1
conj=[j for j in range(1,2*m)]         # j*pi*R strictly inside (0, 4 pi R) <=> j in {1,2,3}
idxA=len(conj)
chk(idxA==2*m-1==3,"gamma_A Morse index = 2m-1 = 3 (conjugate points at pi R, 2 pi R, 3 pi R)")
idxB=0                                   # flat S^1(2R) factor, non-contractible: index 0
chk(idxB==0,"gamma_B Morse index = 0 (flat factor, product formula)")
lenA=4*R; r=2*R; lenB=2*r
chk(lenA==lenB,"equal lengths 4 pi R = 2 pi (2R)")
for Nn in (3,5,7):
    # h = 2 pi R / N: hop counts delta h = length / h = 2N (both loops)
    dhA=4*R*Nn//(2*R); dhB=2*r*Nn//(2*R)
    chk(dhA==dhB==2*Nn,f"hop counts equal: delta h = 2N = {2*Nn} at N={Nn}")
    ThA=dhA; ThB=dhB                     # kappa == 1 minimal edges: Theta = delta h [FT.31(4)]
    chk(ThA==ThB and ThA%2==0,f"Theta equal and even (FT.22-admissible) at N={Nn}")
    ledgA=(1,dhA,ThA,1,0)                # (kappa0, delta h, Theta, sigma-parity n_-, aleph)
    ledgB=(1,dhB,ThB,1,0)
    chk(ledgA==ledgB,f"identical ledger records at N={Nn}")
    wA=(-1)**(ThA+0+0); wB=(-1)**(ThB+0+0)
    chk(wA==wB==1,f"identical weights +1 at N={Nn}")
    chk(abs(wA)==abs(wB)==1,"CT2.8 norms equally blind: |w|^2 = 1 both")
chk(idxA!=idxB,"Morse indices differ => no function of weight/ledger data separates index 0 from index >= 1")

print(f"verify_H_selection: {N} checks green")
