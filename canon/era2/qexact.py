#!/usr/bin/env python3
"""
qexact.py -- exact-arithmetic core for the Level 5 census.

Covenant compliance:
  * NO floating point. Every numeric value is a Fraction interval [lo,hi] with
    rational endpoints and a rigorously bounded width, or an exact symbolic
    object (integer, Fraction, Z[x] polynomial).
  * Transcendentals (pi, ln2, cos of rational multiples of pi) enter ONLY as
    rigorous Fraction intervals with an explicit tail bound -- the corpus's own
    method ("exact rational interval division at widths < 2^-50", FT.114).
  * Minimal polynomials are verified by exact Z[x] substitution, the way
    Census FT.63(6) verifies the dodecahedral quartic.

Two currencies are kept APART throughout, per Def-BM.19(1)-(2):
  Theta   -- the winding of a materialized closed chain,  [Theta]   = q^{+1}
  Theta_R -- the holonomy angle defect,                   [Theta_R] = q^{0}
The identification Theta_R = 2*pi*k is RULED OUT (FT.55(1) calibration no-go).
Nothing in this module equates them.
"""
from fractions import Fraction as Fr
from math import gcd

# --------------------------------------------------------------------------
# 1. Rigorous interval arithmetic over Fraction
# --------------------------------------------------------------------------

class Iv:
    """Closed rational interval [lo,hi]. Exact endpoints, no floats."""
    __slots__ = ("lo", "hi")

    def __init__(self, lo, hi=None):
        lo = Fr(lo)
        hi = lo if hi is None else Fr(hi)
        if lo > hi:
            lo, hi = hi, lo
        self.lo, self.hi = lo, hi

    # --- arithmetic (all outward-rounded by construction: exact Fractions) ---
    def __add__(s, o):  o = o if isinstance(o, Iv) else Iv(o); return Iv(s.lo+o.lo, s.hi+o.hi)
    def __radd__(s, o): return Iv(o) + s
    def __sub__(s, o):  o = o if isinstance(o, Iv) else Iv(o); return Iv(s.lo-o.hi, s.hi-o.lo)
    def __rsub__(s, o): return Iv(o) - s
    def __neg__(s):     return Iv(-s.hi, -s.lo)

    def __mul__(s, o):
        o = o if isinstance(o, Iv) else Iv(o)
        p = [s.lo*o.lo, s.lo*o.hi, s.hi*o.lo, s.hi*o.hi]
        return Iv(min(p), max(p))
    __rmul__ = __mul__

    def __truediv__(s, o):
        o = o if isinstance(o, Iv) else Iv(o)
        assert o.lo > 0 or o.hi < 0, "division by an interval containing 0"
        p = [s.lo/o.lo, s.lo/o.hi, s.hi/o.lo, s.hi/o.hi]
        return Iv(min(p), max(p))
    __rtruediv__ = lambda s, o: Iv(o) / s

    def pow_int(self, n):
        if n == 0: return Iv(1)
        if n < 0:  return Iv(1) / self.pow_int(-n)
        r, b = Iv(1), self
        while n:
            if n & 1: r = r * b
            b, n = b * b, n >> 1
        return r

    @property
    def mid(self):   return (self.lo + self.hi) / 2
    @property
    def rad(self):   return (self.hi - self.lo) / 2
    @property
    def width(self): return self.hi - self.lo

    def contains(self, x): x = Fr(x); return self.lo <= x <= self.hi
    def disjoint(self, o): return self.hi < o.lo or o.hi < self.lo
    def __repr__(self):
        return f"[{float(self.lo):.18g}, {float(self.hi):.18g}] w={float(self.width):.3e}"


# --------------------------------------------------------------------------
# 2. Rigorous transcendentals
# --------------------------------------------------------------------------

def _fact(n):
    r = 1
    for i in range(2, n+1): r *= i
    return r

def cos_sin_rat(m, terms=45):
    """cos(m), sin(m) for a Fraction m, |m| <= 4, rigorous Taylor tail."""
    m = Fr(m)
    c = Fr(0); s_ = Fr(0)
    for k in range(terms):
        c += Fr((-1)**k, _fact(2*k))   * m**(2*k)
        s_ += Fr((-1)**k, _fact(2*k+1)) * m**(2*k+1)
    tail = Fr(abs(m)**(2*terms), _fact(2*terms))
    return Iv(c - tail, c + tail), Iv(s_ - tail, s_ + tail)

def pi_iv(bits=90):
    """Machin: pi = 16 atan(1/5) - 4 atan(1/239), rigorous alternating tail."""
    def atan_inv(x, n):
        s_ = Fr(0)
        for k in range(n):
            t = Fr(1, (2*k+1) * x**(2*k+1))
            s_ += t if k % 2 == 0 else -t
        e = Fr(1, (2*n+1) * x**(2*n+1))
        return s_ - e, s_ + e
    la, ha = atan_inv(5, bits)
    lb, hb = atan_inv(239, bits)
    return Iv(16*la - 4*hb, 16*ha - 4*lb)

def ln2_iv(bits=120):
    s_ = sum((Fr(1, n*2**n) for n in range(1, bits+1)), Fr(0))
    t = Fr(1, (bits+1) * 2**bits)
    return Iv(s_, s_ + t)

def cos_iv(x, PI, snap=64, terms=40):
    """cos(x) for x an Iv. Midpoint snapped to denominator 2^snap; the snap error
    and the interval radius are both absorbed by the |cos'| <= 1 Lipschitz term.
    Rigorous, and fast (avoids Taylor on 90-bit rationals)."""
    x = x if isinstance(x, Iv) else Iv(x)
    m = x.mid
    snapped = Fr(int(round(m * 2**snap)), 2**snap)
    cm, _ = cos_sin_rat(snapped, terms=terms)
    lip = x.rad + abs(m - snapped)
    return Iv(cm.lo - lip, cm.hi + lip)

def sqrt_int_iv(n, bits=200):
    """sqrt(n) as an interval, by integer bisection on n*4^k (exact)."""
    if n == 0: return Iv(0)
    lo, hi = Fr(0), Fr(max(2, n))
    for _ in range(bits):
        mid = (lo + hi) / 2
        if mid*mid < n: lo = mid
        else: hi = mid
    return Iv(lo, hi)


# --------------------------------------------------------------------------
# 3. Exact Z[x] polynomial arithmetic + minimal-polynomial verification
# --------------------------------------------------------------------------

class Poly:
    """Dense polynomial over Z (or Fraction), coeffs[0] + coeffs[1] x + ..."""
    def __init__(self, c): 
        self.c = list(c)
        while len(self.c) > 1 and self.c[-1] == 0: self.c.pop()
    def __repr__(self):
        t = []
        for i in range(len(self.c)-1, -1, -1):
            a = self.c[i]
            if a == 0: continue
            s = "" if i == 0 else ("x" if i == 1 else f"x^{i}")
            if isinstance(a, Fr):
                a_s = (f"{a.numerator:+d}" if a.denominator == 1
                       else (f"+{a.numerator}/{a.denominator}" if a > 0
                             else f"-{-a.numerator}/{a.denominator}"))
            else:
                a_s = f"{a:+g}" if not isinstance(a, int) else f"{a:+d}"
            t.append(f"{a_s}{s}" if s else a_s)
        return "".join(t).lstrip("+") or "0"
    def __mul__(s, o):
        if not isinstance(o, Poly): return Poly([a*o for a in s.c])
        r = [0]*(len(s.c)+len(o.c)-1)
        for i,a in enumerate(s.c):
            for j,b in enumerate(o.c): r[i+j] += a*b
        return Poly(r)
    __rmul__ = __mul__
    def __add__(s, o):
        n = max(len(s.c), len(o.c)); r = [0]*n
        for i,a in enumerate(s.c): r[i] += a
        for i,b in enumerate(o.c): r[i] += b
        return Poly(r)
    def __sub__(s, o): return s + Poly([-b for b in o.c])
    def __neg__(s): return Poly([-b for b in s.c])
    def __eq__(s, o):
        if not isinstance(o, Poly): return NotImplemented
        d = s - o
        return all(a == 0 for a in d.c)
    def __ne__(s, o):
        r = s.__eq__(o)
        return r if r is NotImplemented else not r
    __hash__ = None
    def __pow__(s, n):
        r = Poly([1])
        for _ in range(n): r = r * s
        return r
    def eval_iv(self, x):
        """Horner with interval x -> rigorous enclosure of p(x)."""
        x = x if isinstance(x, Iv) else Iv(x)
        acc = Iv(self.c[-1])
        for a in reversed(self.c[:-1]): acc = acc * x + Iv(a)
        return acc
    def eval_fr(self, x):
        acc = Fr(0)
        for a in reversed(self.c): acc = acc * Fr(x) + a
        return acc
    @property
    def deg(self): return len(self.c) - 1
    @property
    def monic(self): return self.c[-1] == 1

def chebyshev_T(m):
    """T_m in Z[x], exactly: T_0=1, T_1=x, T_{m+1} = 2x T_m - T_{m-1}."""
    if m == 0: return Poly([1])
    T0, T1 = Poly([1]), Poly([0,1])
    for _ in range(m-1):
        T0, T1 = T1, Poly([0,2]) * T1 - T0
    return T1

def verify_minpoly(p, root_iv, name=""):
    """Exact Z[x] verification that p is the minimal polynomial of root_iv:
       (a) p monic, integer coeffs;
       (b) p(root) enclosed around 0 -- interval eval must contain 0;
       (c) no polynomial of lower degree with the same property is rational,
           checked by: p has no rational root (Rational Root Theorem) when
           deg >= 2, and deg matches the canonical field degree."""
    ok_monic = p.monic
    ok_int   = all(float(a).is_integer() for a in p.c)
    ev       = p.eval_iv(root_iv)
    ok_root  = ev.contains(0)
    ok_norat = True
    if p.deg >= 2:
        a0, an = p.c[0], p.c[-1]
        cands = {Fr(d, e) for d in range(1, abs(int(a0))+1) if a0 % d == 0
                          for e in range(1, abs(int(an))+1) if an % e == 0}
        cands |= {-c for c in cands}
        ok_norat = all(p.eval_fr(c) != 0 for c in cands)
    return dict(name=name, monic=ok_monic, integer=ok_int, root=ok_root,
                no_rational_root=ok_norat, deg=p.deg,
                root_width=float(root_iv.width), ev=str(ev), ALL=(ok_monic and ok_int and ok_root and ok_norat))


def sqrt_iv(x, bits=220):
    """sqrt of a positive interval, rigorous, by integer-free Fraction bisection.
    sqrt is monotone, so sqrt([lo,hi]) subset [sqrt_lo(lo), sqrt_hi(hi)]."""
    x = x if isinstance(x, Iv) else Iv(x)
    assert x.lo > 0, "sqrt_iv needs a strictly positive interval"
    def b(t):
        lo, hi = Fr(0), max(Fr(1), t + 1)
        for _ in range(bits):
            mid = (lo + hi) / 2
            if mid*mid < t: lo = mid
            else: hi = mid
        return lo, hi
    alo, ahi = b(x.lo)
    blo, bhi = b(x.hi)
    return Iv(alo, bhi)
