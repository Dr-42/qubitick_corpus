"""qparse.py — parser for the Qubitick era canon markdown files.

Splits each canon file into an ordered list of chunks:
  h1        the file title line (# ...)
  h2        a '## ' section heading
  h3        a '### ' heading that is NOT a registry tag block (Tier headings etc.)
  tagblock  a '### TAG — title' block (TAG in the registry) or a paragraph-level
            tag (**A1.**, **C3.**, **D0.1.**, **P1.**, **Cor CT0.7a ...**)
  raw       everything else (paragraphs, displays, tables, quotes, lists),
            kept verbatim as markdown for the converter
  hr        a '---' separator line

Tag blocks carry: tag, title (for ### blocks), lines (body without heading),
and — for ### blocks — nested 'cor' sub-blocks split out (paragraph-level
**Cor TAG** markers with TAG in the registry).
"""
import json
import os
import re
import sys

_PKG = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
REG_PATH = os.path.join(_PKG, "era1", "canon", "index", "tags.json")

def load_registry():
    return json.load(open(REG_PATH, encoding="utf-8"))

# paragraph-level tag markers: **A1.** / **C10.** / **D2.13.** / **P5.** / **Cor CT0.7a (...).**
PARA_TAG = re.compile(r"^\*\*(?:Cor\s+)?([A-Za-z][A-Za-z0-9.\-]*?)(?:\s*\([^)]*\))?\.\*\*")
COR_TAG = re.compile(r"^\*\*Cor\s+([A-Za-z][A-Za-z0-9.\-]*?)(?:\s*\(([^)]*)\))?\.\*\*")
H3_TAG = re.compile(r"^### (\S+) — (.*)$")

def tag_class(tag):
    if re.match(r"^A\d$", tag): return "axiom"
    if re.match(r"^C\d+$", tag): return "convention"
    if re.match(r"^P\d$", tag): return "policy"
    if re.match(r"^D\d+\.", tag): return "definition"
    if tag.startswith("Def-"): return "definition"
    return "theorem"

def parse_file(path, registry):
    src = open(path, encoding="utf-8").read()
    lines = src.split("\n")
    chunks = []
    i, n = 0, len(lines)

    def para_tag_at(idx):
        """If line idx starts a paragraph-level registry tag, return (tag, is_cor, cor_title)."""
        ln = lines[idx]
        m = COR_TAG.match(ln)
        if m and m.group(1) in registry:
            return m.group(1), True, (m.group(2) or "")
        m = PARA_TAG.match(ln)
        if m and m.group(1) in registry:
            return m.group(1), False, ""
        return None

    _watch = -1
    while i < n:
        if i == _watch:
            print("STALL at line", i+1, repr(lines[i][:80]), file=sys.stderr); i += 1
        _watch = i
        ln = lines[i]
        st = ln.strip()
        if i == 0 and st.startswith("# "):
            chunks.append({"kind": "h1", "text": ln}); i += 1; continue
        if st.startswith("## ") and not st.startswith("### "):
            chunks.append({"kind": "h2", "text": st[3:].strip()}); i += 1; continue
        m = None
        if st.startswith("### "):
            rest = ln.strip()[4:].strip()
            if " \u2014 " in rest:
                tok, t2 = rest.split(" \u2014 ", 1)
                if tok in registry:
                    m = (tok, t2.strip())
        if m:
            tag, title = m[0], m[1]
            if True:
                # collect body until next heading / EOF
                j = i + 1
                body = []
                while j < n and not re.match(r"^#{1,3} ", lines[j]):
                    body.append(lines[j]); j += 1
                # trim trailing hr
                while body and body[-1].strip() == "": body.pop()
                trailing_hr = False
                if body and re.fullmatch(r"-{3,}", body[-1].strip()):
                    body.pop(); trailing_hr = True
                while body and body[-1].strip() == "": body.pop()
                # split nested Cor sub-blocks
                segs = []          # list of ("main"|"cor", tag, title, lines)
                cur = []
                k = 0
                while k < len(body):
                    pt = para_tag_at(i + 1 + k) if False else None
                    cm = COR_TAG.match(body[k])
                    if cm and cm.group(1) in registry:
                        if cur: segs.append(("main", None, None, cur)); cur = []
                        cbody = [body[k]]
                        k += 1
                        while k < len(body) and not COR_TAG.match(body[k]):
                            cbody.append(body[k]); k += 1
                        segs.append(("cor", cm.group(1), cm.group(2) or "", cbody))
                    else:
                        cur.append(body[k]); k += 1
                if cur: segs.append(("main", None, None, cur))
                chunks.append({"kind": "tagblock", "tag": tag, "title": title,
                               "segs": segs, "file": os.path.basename(path)})
                if trailing_hr:
                    chunks.append({"kind": "hr"})
                i = j; continue
        elif st.startswith("### "):
            chunks.append({"kind": "h3", "text": st[4:].strip()}); i += 1; continue
        if re.fullmatch(r"-{3,}|\*{3,}|_{3,}", st):
            chunks.append({"kind": "hr"}); i += 1; continue
        pt = para_tag_at(i)
        if pt and (pt[1] or tag_class(pt[0]) != "theorem"):
            tag, is_cor, ctitle = pt
            # paragraph-level tag body: until next heading, hr, next para-tag, or a
            # blank line followed by a non-indented line that starts a new **bold** para
            body = [lines[i]]; j = i + 1
            while j < n:
                l2 = lines[j]
                s2 = l2.strip()
                if re.match(r"^#{1,3} ", l2) or re.fullmatch(r"-{3,}|\*{3,}|_{3,}", s2):
                    break
                if para_tag_at(j) and (para_tag_at(j)[1] or tag_class(para_tag_at(j)[0]) != "theorem"):
                    break
                if s2 == "" and j + 1 < n:
                    nxt = lines[j+1].strip()
                    # a following paragraph that starts with a bold run-in marker and is
                    # a registry tag ends the body; plain paragraphs/displays continue
                    if para_tag_at(j+1) and (para_tag_at(j+1)[1] or tag_class(para_tag_at(j+1)[0]) != "theorem"):
                        break
                    if re.match(r"^\*\*[A-Z§]", nxt) and not nxt.startswith("**Thm") \
                       and not nxt.startswith("**Req") and not nxt.startswith("**Pf") \
                       and not nxt.startswith("**Phys") and not nxt.startswith("**Cor") \
                       and not nxt.startswith("**Def"):
                        break
                body.append(l2); j += 1
            while body and body[-1].strip() == "": body.pop()
            chunks.append({"kind": "paratag", "tag": tag, "is_cor": is_cor,
                           "title": ctitle, "lines": body, "file": os.path.basename(path)})
            i = j; continue
        if st == "":
            i += 1; continue
        # raw region: accumulate until heading/hr/para-tag
        buf = []
        while i < n:
            l2 = lines[i]; s2 = l2.strip()
            if re.match(r"^#{1,3} ", l2) or re.fullmatch(r"-{3,}|\*{3,}|_{3,}", s2):
                break
            _pt = para_tag_at(i)
            if _pt and (_pt[1] or tag_class(_pt[0]) != "theorem"):
                break
            buf.append(l2); i += 1
        while buf and buf[-1].strip() == "": buf.pop()
        if buf:
            chunks.append({"kind": "raw", "text": "\n".join(buf)})
        elif i < n:
            chunks.append({"kind": "raw", "text": lines[i]}); i += 1
    return chunks

if __name__ == "__main__":
    reg = load_registry()
    base = os.path.join(_PKG, "era1", "canon")
    files = ["Part1_Qubit_era.md","Part2_Bosonic_era.md","Part3_Fermion_era.md",
             "Part4_Baryomesonic_era.md","Census.md"]
    seen = set()
    for fn in files:
        ch = parse_file(os.path.join(base, fn), reg)
        kinds = {}
        tags = []
        for c in ch:
            kinds[c["kind"]] = kinds.get(c["kind"], 0) + 1
            if c["kind"] == "tagblock":
                tags.append(c["tag"]); seen.add(c["tag"])
                for s in c["segs"]:
                    if s[0] == "cor": seen.add(s[1]); tags.append("(cor)" + s[1])
            elif c["kind"] == "paratag":
                seen.add(c["tag"]); tags.append("(para)" + c["tag"])
        print(fn, kinds, f"tags={len(tags)}")
    # registry coverage
    missing = [t for t in reg if t not in seen]
    extra = [t for t in seen if t not in reg]
    print("registry tags:", len(reg), "| parsed:", len(seen & set(reg)))
    print("MISSING from parse:", sorted(missing))
    print("EXTRA (not in registry):", sorted(extra))
