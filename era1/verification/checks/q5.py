
"""Exact arithmetic helpers: Q(sqrt5) field, Q(i) field, integer SNF, GF(2) tools.
No floating point anywhere (corpus discipline)."""
from fractions import Fraction

# ---------- Q(sqrt5): pairs (a,b) = a + b*sqrt(5), a,b in Fraction ----------
class Q5:
    __slots__ = ('a','b')
    def __init__(self, a, b=0):
        self.a = Fraction(a); self.b = Fraction(b)
    def __add__(s,o): return Q5(s.a+o.a, s.b+o.b)
    def __sub__(s,o): return Q5(s.a-o.a, s.b-o.b)
    def __mul__(s,o):
        if isinstance(o,int) or isinstance(o,Fraction): o = Q5(o)
        return Q5(s.a*o.a + 5*s.b*o.b, s.a*o.b + s.b*o.a)
    __rmul__ = __mul__
    def __neg__(s): return Q5(-s.a,-s.b)
    def inv(s):
        n = s.a*s.a - 5*s.b*s.b
        assert n != 0
        return Q5(s.a/n, -s.b/n)
    def __truediv__(s,o): return s*o.inv()
    def __eq__(s,o):
        if isinstance(o,int): o = Q5(o)
        return s.a==o.a and s.b==o.b
    def __hash__(s): return hash((s.a,s.b))
    def __repr__(s): return f"({s.a}+{s.b}r5)"

# ---------- Q(i): pairs (a,b) = a + b*i, a,b in Fraction ----------
class QI:
    __slots__ = ('a','b')
    def __init__(self, a, b=0):
        self.a = Fraction(a); self.b = Fraction(b)
    def __add__(s,o): return QI(s.a+o.a, s.b+o.b)
    def __sub__(s,o): return QI(s.a-o.a, s.b-o.b)
    def __mul__(s,o): return QI(s.a*o.a - s.b*o.b, s.a*o.b + s.b*o.a)
    def __neg__(s): return QI(-s.a,-s.b)
    def conj(s): return QI(s.a,-s.b)
    def inv(s):
        n=s.a*s.a+s.b*s.b
        assert n!=0
        return QI(s.a/n,-s.b/n)
    def __truediv__(s,o):
        if isinstance(o,(int,Fraction)): o=QI(o)
        return s*o.inv()
    def __eq__(s,o):
        if isinstance(o,int): o = QI(o)
        return s.a==o.a and s.b==o.b
    def __hash__(s): return hash((s.a,s.b))
    def __repr__(s): return f"({s.a}+{s.b}i)"

# ---------- exact matrix helpers (any field-like entries with +,-,*,inv,==,0) ----------
def mat_mul(A,B,zero):
    n=len(A); m=len(B[0]); k=len(B)
    C=[[zero]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            acc=zero
            for t in range(k):
                if A[i][t]!=zero and B[t][j]!=zero: acc=acc+A[i][t]*B[t][j]
            C[i][j]=acc
    return C

def mat_vec(A,v,zero):
    return [sum((A[i][j]*v[j] for j in range(len(v)) if A[i][j]!=zero and v[j]!=zero), zero) for i in range(len(A))]

def det3(M):
    (a,b,c),(d,e,f),(g,h,i)=M
    return a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)

def inv3(M, one, zero):
    d = det3(M)
    assert d != zero, "singular"
    (a,b,c),(dd,e,f),(g,h,i)=M
    adj=[[e*i-f*h, c*h-b*i, b*f-c*e],
         [f*g-dd*i, a*i-c*g, c*dd-a*f],
         [dd*h-e*g, b*g-a*h, a*e-b*dd]]
    return [[x/d for x in row] for row in adj]

# ---------- GF(2) linear algebra ----------
def gf2_rank(rows, ncols):
    """rows: list of ints (bitmasks). Returns rank and reduced basis."""
    basis = {}
    for r in rows:
        cur = r
        while cur:
            piv = cur & (-cur)
            if piv in basis: cur ^= basis[piv]
            else: basis[piv] = cur; break
    return len(basis), basis

def gf2_solve(B_rows, rhs, ncols):
    """Solve B x = rhs over GF(2). B_rows: F lists of column indices (or bitmasks over columns).
    Returns (particular solution as int bitmask over columns, kernel basis list of int bitmasks) or None."""
    # rows as bitmasks over columns
    rows = list(B_rows); tgt = list(rhs)
    piv_of = {}  # column pivot -> row index
    rref = []
    for idx,(r,t) in enumerate(zip(rows,tgt)):
        cur, ct = r, t
        for pc, pr in piv_of.items():
            if cur >> pc & 1:
                cur ^= rref[pr][0]; ct ^= rref[pr][1]
        if cur:
            pc = (cur & -cur).bit_length()-1
            piv_of[pc] = len(rref)
            rref.append((cur, ct))
        else:
            if ct: return None  # inconsistent
    # particular: free vars = 0
    x = 0
    for pc, pr in piv_of.items():
        if rref[pr][1]: x |= (1 << pc)
    # kernel: for each non-pivot column, a basis vector
    ker = []
    for c in range(ncols):
        if c in piv_of: continue
        v = (1 << c)
        for pc, pr in piv_of.items():
            if rref[pr][0] >> c & 1: v |= (1 << pc)
        ker.append(v)
    return x, ker, piv_of, rref

# ---------- integer Smith normal form (small matrices) ----------
def snf(M):
    """M: list of lists of ints. Returns list of nonzero elementary divisors (invariant factors)."""
    A = [row[:] for row in M]
    rows = len(A); cols = len(A[0])
    divs = []
    t = 0
    while t < min(rows, cols):
        # find pivot
        found = False
        while True:
            nz = [(i,j) for i in range(t,rows) for j in range(t,cols) if A[i][j]!=0]
            if not nz:
                found = False; break
            i0,j0 = min(nz, key=lambda p: abs(A[p[0]][p[1]]))
            A[t],A[i0] = A[i0],A[t]
            for r in range(rows): A[r][t],A[r][j0] = A[r][j0],A[r][t]
            # eliminate column
            done = True
            for i in range(t+1, rows):
                if A[i][t]:
                    q = A[i][t]//A[t][t]
                    for j in range(t, cols): A[i][j] -= q*A[t][j]
                    if A[i][t]: done = False
            for j in range(t+1, cols):
                if A[t][j]:
                    q = A[t][j]//A[t][t]
                    for i in range(t, rows): A[i][j] -= q*A[i][t]
                    if A[t][j]: done = False
            if done and all(A[i][t]==0 for i in range(t+1,rows)) and all(A[t][j]==0 for j in range(t+1,cols)):
                found = True; break
        if not found: break
        d = A[t][t]
        # ensure divisibility chain
        bad = [i for i in range(t+1,rows) for j in range(t+1,cols) if A[i][j] % d != 0]
        if bad:
            i = bad[0]// (cols)  # approx; do proper:
            # find any entry not divisible, add its row to row t and repeat
            for ii in range(t+1,rows):
                for jj in range(t+1,cols):
                    if A[ii][jj] % d != 0:
                        for j in range(t,cols): A[t][j] += A[ii][j]
                        ii2,jj2 = rows,cols; break
                else: continue
                break
            continue
        divs.append(abs(d)); t += 1
    # divisibility chain fix (post-process): convert multiset of diagonal divs to invariant factors
    if divs:
        changed = True
        while changed:
            changed = False
            for i in range(len(divs)-1):
                a,b = divs[i],divs[i+1]
                if b % a != 0:
                    from math import gcd
                    g = gcd(a,b); l = a*b//g
                    divs[i],divs[i+1] = g,l; changed = True
    return [d for d in divs if d != 0]
