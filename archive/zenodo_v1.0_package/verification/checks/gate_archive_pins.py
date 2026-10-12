"""Gate the first-edition (H_archive) pins in the content checkers.

The 21 bundled first editions were externalized to a separate historical-archive
repository, so the pins comparing era-canon text against them are no longer
runnable here.  They are real verification, so they are gated rather than
deleted: each archive-dependent statement is wrapped in `if ARCH:` with
ARCH = era_paths.ARCHIVE_PRESENT, and runs again unchanged wherever the archive
is bundled.

Taint is flow-sensitive in source order: a name is tainted from a tainted
binding until it is rebound from an untainted expression.  Tuple assignments are
resolved element-wise, so in

    E, H13 = rd("E_electromagnetic.md"), rd("H_archive/H13_registries_and_gaps.md")

only H13 is tainted and the era-canon pins on E stay live.

  python3 gate_archive_pins.py            dry run: report + both audits
  python3 gate_archive_pins.py --apply    rewrite in place

Kept in the tree as provenance and so the gating can be re-derived or extended
if a checker gains new first-edition pins.  It is not a checker; run_all.py
ignores it.  Measured at the pass that introduced it: 15 files, 114 gating runs,
196 archive-scoped assertions of the 1269 in those files.
"""
import ast, os, re, sys

APPLY = '--apply' in sys.argv
HERE = os.path.dirname(os.path.abspath(__file__))

FILES = ['verify_F33_dynamic_phase.py', 'verify_H_branch_parity.py', 'verify_H_chiral_closure.py',
         'verify_H_chirality.py', 'verify_H_closure.py', 'verify_H_colour_channel.py',
         'verify_H_force_matrix.py', 'verify_H_form_factor.py',
         'verify_H_koide_channel.py', 'verify_H_parity_identification.py',
         'verify_H_rung1_neutrino.py', 'verify_H_smcomplete.py', 'verify_H_topology_blind.py',
         'verify_L0_ledger_tilt.py', 'verify_L_lyapunov.py']

NEVER_GATE = (ast.Import, ast.ImportFrom, ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)


def names_of(node):
    return {n.id for n in ast.walk(node) if isinstance(n, ast.Name)}


def bound_names(targets):
    out = set()
    for t in targets:
        for n in ast.walk(t):
            if isinstance(n, ast.Name):
                out.add(n.id)
    return out


def seg(src, node):
    return ast.get_source_segment(src, node) or ''


def mentions_archive(node_src):
    return 'H_archive' in node_src


class Walker:
    def __init__(self, src):
        self.src = src
        self.tainted = set()
        self.runs = []
        self.gated = []        # (lineno, source) of every gated chk, for the audit

    def dep(self, node):
        s = seg(self.src, node)
        return mentions_archive(s) or bool(names_of(node) & self.tainted)

    def bind(self, targets, value):
        """flow-sensitive binding; tuple-to-tuple assignments resolve element-wise"""
        if (len(targets) == 1 and isinstance(targets[0], ast.Tuple)
                and isinstance(value, ast.Tuple)
                and len(targets[0].elts) == len(value.elts)):
            for tgt, val in zip(targets[0].elts, value.elts):
                self.bind([tgt], val)
            return
        t = self.dep(value) if value is not None else False
        for nm in bound_names(targets):
            if t:
                self.tainted.add(nm)
            else:
                self.tainted.discard(nm)

    def taint_inner_assignments(self, st):
        for sub in ast.walk(st):
            if isinstance(sub, ast.Assign):
                self.tainted |= bound_names(sub.targets)
            elif isinstance(sub, (ast.AugAssign, ast.AnnAssign)):
                self.tainted |= bound_names([sub.target])
            elif isinstance(sub, ast.For):
                self.tainted |= bound_names([sub.target])

    def classify(self, st):
        if isinstance(st, NEVER_GATE):
            return False, False
        if isinstance(st, ast.For) and self.dep(st.iter):
            self.taint_inner_assignments(st)
            return True, True
        if isinstance(st, (ast.If, ast.While)) and self.dep(st.test):
            self.taint_inner_assignments(st)
            return True, True
        if isinstance(st, (ast.Assign, ast.AugAssign, ast.AnnAssign)):
            return self.dep(st), True
        if isinstance(st, (ast.If, ast.While, ast.Try, ast.With)):
            return False, False        # descend; children are gated individually
        if isinstance(st, ast.Expr):
            return self.dep(st), True
        return self.dep(st), True

    def record(self, st):
        for sub in ast.walk(st):
            if isinstance(sub, ast.Call) and isinstance(sub.func, ast.Name) and sub.func.id == 'chk':
                self.gated.append((sub.lineno, seg(self.src, sub)))

    def body(self, stmts, depth):
        i, n = 0, len(stmts)
        while i < n:
            st = stmts[i]
            gate, skip_into = self.classify(st)
            if gate:
                j = i
                while j + 1 < n and self.classify(stmts[j + 1])[0]:
                    self.apply_taint(stmts[j])
                    j += 1
                self.apply_taint(stmts[j])
                self.runs.append((st.lineno, stmts[j].end_lineno, depth))
                for k in range(i, j + 1):
                    self.record(stmts[k])
                i = j + 1
                continue
            self.apply_taint(st)
            if not skip_into:
                self.descend(st, depth)
            i += 1

    def apply_taint(self, st):
        if isinstance(st, ast.Assign):
            self.bind(st.targets, st.value)
        elif isinstance(st, (ast.AugAssign, ast.AnnAssign)):
            self.bind([st.target], getattr(st, 'value', None))
        elif isinstance(st, ast.For):
            self.bind([st.target], st.iter)

    def descend(self, st, depth):
        for field in ('body', 'orelse', 'finalbody'):
            sub = getattr(st, field, None)
            if isinstance(sub, list) and sub and all(isinstance(x, ast.stmt) for x in sub):
                self.body(sub, depth + 1)
        for h in getattr(st, 'handlers', []) or []:
            if h.body:
                self.body(h.body, depth + 1)


def transform(path):
    src = open(path, encoding='utf-8').read()
    tree = ast.parse(src)
    w = Walker(src)
    w.body(tree.body, 0)
    if not w.runs:
        return src, w
    lines = src.split('\n')
    for start, end, depth in sorted(w.runs, key=lambda r: -r[0]):
        block = lines[start - 1:end]
        base = block[0][:len(block[0]) - len(block[0].lstrip())]
        indented = [('    ' + l if l.strip() else l) for l in block]
        lines[start - 1:end] = [base + 'if ARCH:'] + indented
    out = '\n'.join(lines)
    if '\nARCH = ' in out:
        return out, w
    NOTE = (
        "\nif not ARCH:\n"
        '    print("  NOTE: H_archive/ is not bundled - the 21 first editions live in the'
        ' external historical-archive repository,")\n'
        '    print("        so this checker\'s first-edition identity pins are gated off.'
        ' Re-bundle H_archive/ to run them.")\n'
    )
    m = re.search(r'(?m)^import era_paths\s*$', out)
    if m:
        return out[:m.end()] + '\nARCH = era_paths.ARCHIVE_PRESENT\n' + NOTE + out[m.end():], w
    m = re.search(r'(?m)^DOCS\s*=.*$', out)
    if m:
        ins = '\nARCH = os.path.isdir(os.path.join(DOCS, "H_archive"))\n' + NOTE
        return out[:m.end()] + ins + out[m.end():], w
    m = re.search(r'(?m)^HERE\s*=.*$', out)
    assert m, path
    ins = '\nARCH = os.path.isdir(os.path.join(os.path.dirname(HERE), "H_archive"))\n' + NOTE
    return out[:m.end()] + ins + out[m.end():], w


def validate(new_src):
    """safety net: no name bound inside a gated run may be referenced outside one.
    Catches both a runtime NameError and a silently-skipped era-canon assertion."""
    tree = ast.parse(new_src)
    spans = []
    for n in ast.walk(tree):
        if isinstance(n, ast.If):
            t = ast.get_source_segment(new_src, n.test) or ''
            if t.strip() == 'ARCH':
                spans.append((n.lineno, n.end_lineno))
    def inside(ln):
        return any(a <= ln <= b for a, b in spans)
    bound, refs, ungated_bind, params = set(), [], {}, set()
    def binder(n):
        if isinstance(n, ast.Assign):
            return bound_names(n.targets)
        if isinstance(n, (ast.AugAssign, ast.AnnAssign)):
            return bound_names([n.target])
        if isinstance(n, ast.For):
            return bound_names([n.target])
        return set()
    for n in ast.walk(tree):
        if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)):
            a = n.args
            for arg in list(a.args) + list(a.kwonlyargs) + [a.vararg, a.kwarg]:
                if arg is not None:
                    params.add(arg.arg)
        if not hasattr(n, 'lineno'):
            continue
        b = binder(n)
        if inside(n.lineno):
            bound |= b
        else:
            for nm in b:
                ungated_bind[nm] = min(ungated_bind.get(nm, 10 ** 9), n.lineno)
        if not inside(n.lineno) and isinstance(n, ast.Name) and isinstance(n.ctx, ast.Load):
            refs.append((n.id, n.lineno))
    # comprehension targets are comprehension-local in Python 3, so a reference
    # inside a comprehension that binds the same name cannot see a gated binding
    comp_locals = []
    for n in ast.walk(tree):
        if isinstance(n, (ast.ListComp, ast.SetComp, ast.GeneratorExp, ast.DictComp)):
            nm = set()
            for g in n.generators:
                nm |= bound_names([g.target])
            comp_locals.append((n.lineno, n.end_lineno, nm))
    def comp_local(nm, ln):
        return any(a <= ln <= b and nm in names for a, b, names in comp_locals)
    bad = []
    for nm, ln in refs:
        if comp_local(nm, ln):
            continue
        if nm not in bound or nm in params:
            continue                      # never gated, or a local parameter
        if ungated_bind.get(nm, 10 ** 9) < ln:
            continue                      # rebound from an ungated source before this use
        bad.append((nm, ln))
    return sorted(set(bad))
# ---- phase 1: compute + audit ------------------------------------------------
plan = []
tot_g = tot_c = 0
suspicious = []
for f in FILES:
    p = os.path.join(HERE, f)
    old = open(p, encoding='utf-8').read()
    new, w = transform(p)
    rs = sorted((a, b) for a, b, _ in w.runs)
    for (a1, b1), (a2, b2) in zip(rs, rs[1:]):
        assert b1 < a2, "%s: overlapping runs %s %s" % (f, (a1, b1), (a2, b2))
    ast.parse(new)
    tree = ast.parse(old)
    nchk = sum(1 for n in ast.walk(tree) if isinstance(n, ast.Call)
               and isinstance(n.func, ast.Name) and n.func.id == 'chk')
    # names bound directly from an archive read
    direct = set()
    for n in ast.walk(tree):
        if isinstance(n, ast.Assign) and 'H_archive' in (seg(old, n.value) or ''):
            direct |= bound_names(n.targets)
    # over-taint audit, inverted: flag a gated chk that references a name bound
    # from an ERA-CANON read (a non-archive document).  Those must stay live.
    # names bound from an archive *list* (e.g. _SPLIT_H) make a join over them
    # archive-derived too, so resolve one level of indirection first
    archlist = set()
    for n in ast.walk(tree):
        if isinstance(n, ast.Assign) and 'H_archive' in (seg(old, n.value) or ''):
            archlist |= bound_names(n.targets)
    canon = set()
    for n in ast.walk(tree):
        if isinstance(n, ast.Assign):
            v = seg(old, n.value)
            if not v:
                continue
            if any(re.search(r'(?<![\w.\'])' + re.escape(a) + r'(?![\w])', v) for a in archlist):
                continue          # a join over an archive list is archive-derived
            # element-wise for tuple assignments
            if (len(n.targets) == 1 and isinstance(n.targets[0], ast.Tuple)
                    and isinstance(n.value, ast.Tuple)
                    and len(n.targets[0].elts) == len(n.value.elts)):
                for tgt, val in zip(n.targets[0].elts, n.value.elts):
                    vs = seg(old, val)
                    if vs and 'H_archive' not in vs and re.search(r'\bread\(|era_paths', vs):
                        canon |= bound_names([tgt])
            elif 'H_archive' not in v and re.search(r'\bread\(|era_paths', v):
                canon |= bound_names(n.targets)
    canon -= direct
    for ln, srcseg in w.gated:
        hits = {c for c in canon if re.search(r'(?<![\w.\'])' + re.escape(c) + r'(?![\w])', srcseg)}
        if hits:
            suspicious.append((f, ln, sorted(hits), srcseg.replace('\n', ' ')[:100]))
    tot_g += len(w.gated); tot_c += nchk
    bad = validate(new)
    assert not bad, "%s: gated binding referenced outside its gate: %s" % (f, bad[:6])
    plan.append((f, p, old, new, len(w.runs)))
    print("%-42s runs=%3d gated_chk=%3d / %4d chk" % (f, len(w.runs), len(w.gated), nchk))

print("\ntotals: %d gated chk of %d" % (tot_g, tot_c))
if suspicious:
    print("\n=== OVER-TAINT AUDIT: %d gated chk referencing an era-canon document ===" % len(suspicious))
    for f, ln, hits, s in suspicious:
        print("  %-34s L%-5d canon=%s  %s" % (f.replace('verify_', '').replace('.py', ''), ln, hits, s))
else:
    print("\nover-taint audit: CLEAN - no gated chk references a name bound from an "
          "era-canon read; every gated assertion is a first-edition pin")

if APPLY and not suspicious:
    n = 0
    for f, p, old, new, nr in plan:
        if new != old:
            open(p, 'w', encoding='utf-8').write(new); n += 1
    print("\napplied: rewrote %d file(s)" % n)
elif APPLY:
    print("\nNOT applied: resolve the over-taint audit first")
else:
    print("\ndry run")
