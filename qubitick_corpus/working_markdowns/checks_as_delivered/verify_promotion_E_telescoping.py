#!/usr/bin/env python3
"""
verify_promotion_E_telescoping.py — exact machine checks for the imported E
corollary.

  Cor EM.9b (chain-wall telescoping):
      for an oriented chain c = (e_1,...,e_k) of distinct real edges whose
      interior vertices v_i = t(e_i) = s(e_{i+1}) are of type (1,1):
          sum_i f_{v_i} = (sigma_{e_k} - sigma_{e_1}) / 2 = -q_EM(c)
      with f_v = (sigma_out - sigma_in)/2 in {-1,0,+1}; zero-sum equivalence
      sigma_{e_1} = sigma_{e_k} <=> q_EM = 0; wall count sum_i aleph_{v_i}
      = #{i : sigma_{e_{i+1}} != sigma_{e_i}} <= k-1.
      Exhaustive over all sign assignments, k = 2..9 (integers doubled to
      stay in Z; no division, no floating point).

Pure Python 3 standard library. Deterministic. Exit code 0 = all green.
"""
import itertools
import era_paths
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.normpath(os.path.join(HERE, ".."))

PASS = FAIL = 0


def chk(name, cond, detail=""):
    global PASS, FAIL
    if cond:
        PASS += 1
    else:
        FAIL += 1
        print(f"  FAIL: {name} {detail}")


def build_chain(k):
    """Nodes 0..k; edge e_i = (i-1 -> i) for i = 1..k (D1.4 head-to-tail).
    Returns (edges as (source, target), interior nodes 1..k-1)."""
    edges = [(i - 1, i) for i in range(1, k + 1)]
    interior = list(range(1, k))
    return edges, interior


def type_1_1(edges, interior, extra_edges=()):
    """Each interior node has exactly one incoming and one outgoing real edge
    among the chain edges (A7/D0.8 type (1,1) domain of D3.3)."""
    all_e = list(edges) + list(extra_edges)
    for v in interior:
        inn = sum(1 for (a, b) in all_e if b == v)
        out = sum(1 for (a, b) in all_e if a == v)
        if (inn, out) != (1, 1):
            return False
    return True


total_cases = 0
ok_types = True
ok_all = True
for k in range(2, 10):
    edges, interior = build_chain(k)
    if not type_1_1(edges, interior):
        ok_types = False
    for sigma in itertools.product((1, -1), repeat=k):
        total_cases += 1
        # f at interior node i (1-based edge indices): in = sigma[i-1], out = sigma[i]
        twice_f = [sigma[i] - sigma[i - 1] for i in range(1, k)]   # 2*f_{v_i} in Z
        lhs2 = sum(twice_f)
        rhs2 = sigma[k - 1] - sigma[0]                              # 2 * (1/2)(s_k - s_1)
        if lhs2 != rhs2:
            ok_all = False
        # q_EM(c) = (sigma_{s(c)} - sigma_{t(c)})/2 = (sigma_1 - sigma_k)/2 = -sum f
        twice_q = sigma[0] - sigma[k - 1]
        if lhs2 != -twice_q:
            ok_all = False
        # f values in {-1, 0, +1}  (doubled: {-2, 0, 2})
        if any(t not in (-2, 0, 2) for t in twice_f):
            ok_all = False
        # zero-sum equivalence
        if (lhs2 == 0) != (sigma[0] == sigma[k - 1]) != (twice_q == 0):
            ok_all = False
        # wall count: aleph_{v_i} = |f_{v_i}| in {0,1}; equals sign-change indicator
        walls = sum(1 for t in twice_f if t != 0)
        changes = sum(1 for i in range(1, k) if sigma[i] != sigma[i - 1])
        if walls != changes or walls > k - 1:
            ok_all = False

chk("chain build: interior vertices are type (1,1) for k = 2..9", ok_types)
chk(f"telescoping + q_EM identity + wall count hold on all sign assignments "
    f"({total_cases} cases, k = 2..9)", ok_all and total_cases == sum(2 ** k for k in range(2, 10)))

# type-(1,1) hypothesis is load-bearing as a domain condition: adding an extra
# incident real edge at an interior node breaks the literal D3.3 domain
edges, interior = build_chain(4)
chk("extra incident edge at interior node => type (1,2): outside D3.3 literal domain",
    not type_1_1(edges, interior, extra_edges=[(1, 7)]))

# closed-chain consistency (EM.9a convention): e_k returns to the base node
# k edges around a cycle: telescoping over ALL k vertices gives 0 exactly
for k in range(3, 9):
    for sigma in itertools.product((1, -1), repeat=k):
        s = sum(sigma[(i + 1) % k] - sigma[i] for i in range(k))
        if s != 0:
            ok_all = False
chk("cyclic variant: total wall sum around a closed cycle is exactly 0", ok_all)

# ------------------------------------------- document integration
e_src = era_paths.read("E_electromagnetic.md")
chk("E_electromagnetic.md contains **Cor EM.9b (", "**Cor EM.9b (" in e_src)
blk = e_src.split("**Cor EM.9b (", 1)[1]
cut = min([blk.find(m) if blk.find(m) != -1 else len(blk)
           for m in ("\n---", "\n**Phys.**", "\n### ", "\n## ")])
body = blk[:cut]
chk("Cor EM.9b: has Req (Cor) and Pf (Cor) with terminator",
    "**Req (Cor).**" in body and "**Pf (Cor).**" in body and r"\blacksquare" in body)
chk("Cor EM.9b: cites no FT./Def-H./P-H token",
    not re.search(r"FT\.|Def-H\.|P-H\d", body))
chk("E closure exports mention EM.9b", r"\mathrm{EM.9b}" in e_src)
chk("E header lists verify_promotion_E_telescoping.py",
    "verify_promotion_E_telescoping.py" in e_src)

print(f"verify_promotion_E_telescoping: {PASS} checks green" + (f", {FAIL} FAILED" if FAIL else ""))
sys.exit(1 if FAIL else 0)
