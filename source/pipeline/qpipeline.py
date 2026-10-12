#!/usr/bin/env python3
"""qpipeline.py — sanitization + restructuring + LaTeX pipeline for the
Qubitick corpus publication package (qubitick_corpus_v1.0).

Stages:
  1. parse the five canon files (+ HistLog §IV) with qparse
  2. sanitize: move adjudications/no-gos/traps/refutations to the Addendum data,
     strip provenance sentences, transform colloquial Phys phrasing, insert
     cross-reference stubs, log every operation
  3. number: Theorem P.N / Definition P.N / Axiom P.N / Convention P.N / Corollary P.N
  4. texify: markdown -> LaTeX via the corpus's own render_paper converter
  5. assemble source/main.tex, source/parts/*.tex, source/addendum.tex,
     source/calibration.tex and the tag index

Nothing here modifies the archive (working_markdowns/); all edits apply to
copies in memory and are written to source/.
"""
import datetime
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PKG = os.path.dirname(os.path.dirname(HERE))          # source/pipeline -> package root
SRC = os.path.join(PKG, "era1", "canon")             # the living revised canon (era-1 half)
OUT = os.path.join(PKG, "source")
TOOLS = os.path.join(PKG, "working_markdowns", "tools")

sys.path.insert(0, HERE)
sys.path.insert(0, TOOLS)
import qparse
import render_paper as rp

REG = qparse.load_registry()

CANON = ["Part1_Qubit_era.md", "Part2_Bosonic_era.md", "Part3_Fermion_era.md",
         "Part4_Baryomesonic_era.md"]
PARTNO = {f: i + 1 for i, f in enumerate(CANON)}
PARTNO["Census.md"] = 5   # appendix A

LOG = []          # sanitization log rows
def log(kind, where, detail):
    LOG.append((kind, where, detail))

# ---------------------------------------------------------------- move registry
# whole-block moves: tag -> addendum section
MOVE = {
    # B.1 category errors and status adjudications
    "FT.89": "B1", "FT.160": "B1",
    "BM.12": "B1", "BM.18": "B1", "BM.24": "B1", "BM.29": "B1", "BM.33": "B1",
    "BM.38": "B1", "BM.50": "B1", "BM.56": "B1", "BM.64": "B1", "BM.72": "B1",
    "BM.78": "B1", "BM.86": "B1", "BM.87": "B1", "BM.93": "B1", "BM.100": "B1",
    "BM.107": "B1", "BM.118": "B1", "BM.119": "B1", "BM.130": "B1", "BM.144": "B1",
    "BM.152": "B1",
    # B.2 refuted hypotheses
    "FT.73": "B2", "FT.77": "B2", "FT.87": "B2", "FT.90": "B2", "FT.94": "B2",
    "BM.126": "B2", "BM.140": "B2",
    # B.3 no-go theorems
    "CT4.4a": "B3", "FT.59": "B3", "FT.117": "B3", "FT.124": "B3", "BM.10": "B3",
    # B.4 traps and phantom gaps
    "BM.143": "B4",
    # revision 1: the deficit registers themselves leave the main corpus
    "FT.84": "B4",
    "FT.125": "B4",
}
assert all(t in REG for t in MOVE), [t for t in MOVE if t not in REG]

# catalog entries: (section, tag or None, quote-search key or None, note)
CATALOG = [
    ("B1", "BM.30",  "the status of the adjudication:", None),
    ("B1", "BM.31",  "the verdict on the extended ensemble:", None),
    ("B1", "BM.45",  "the adjudication", None),
    ("B1", "BM.49",  "remains what the Tier BM.8 adjudication made it", None),
    ("B1", "BM.63",  "the no-opening theorem survives", None),
    ("B1", "BM.94",  "category error", None),
    ("B1", "BM.97",  "the rest mass is the pole mass", None),
    ("B1", "BM.117", "octet adjudication", None),
    ("B1", "BM.141", "width adjudication", None),
    ("B2", "FT.68",  "Verdict on", None),
    ("B2", "FT.79",  "cover hypothesis fails", None),
    ("B2", "BM.57",  "splits nothing", None),
    ("B3", "FT.55",  "no-go", None),
    ("B3", "FT.66",  "absolute index-0 rules are inadmissible for closed chains", None),
    ("B3", "FT.82",  "particle–boson picture is not reproduced", None),
    ("B3", "BM.61",  "the strength bar", None),
    ("B4", "BM.37",  "counting trap", None),
    ("B4", "BM.36",  "capacity ratio", None),
]

# ---------------------------------------------------------------- strips / transforms
# (file, old, new, expected_count) — applied to main-text chunks only.
STRIPS = [
    ("Part1_Qubit_era.md",
     " carry their own non-derived clauses explicitly; their disposition ledger is HistLog §I.",
     " carry their own non-derived clauses explicitly.", 1),
    ("Part1_Qubit_era.md",
     " D0.8. Provenance of the axiom set: HistLog §0.",
     " D0.8.", 1),
    ("Part1_Qubit_era.md",
     " the baryomesonic era introduces none (Part 4 §Cal-BM). The former declared-choice registry is fully dispositioned: HistLog §I.3.",
     " the baryomesonic era introduces none (Part 4 §Cal-BM).", 1),
    ("Part3_Fermion_era.md",
     "that identification is the declared content of Def-H.37(2) (HistLog §I), and",
     "that identification is the declared content of Def-H.37(2), and", 1),
    ("Part3_Fermion_era.md",
     " (retirement record: HistLog §I)", "", 2),
    ("Part3_Fermion_era.md",
     "(retired candidate; HistLog §I)", "(retired candidate)", 1),
    ("Part3_Fermion_era.md",
     "**Rmk (interface definition Def-H.42, logged in HistLog §I).**",
     "**Rmk (interface definition Def-H.42).**", 1),
    ("Part3_Fermion_era.md",
     "**Rmk (interface definition Def-H.34, logged in HistLog §I).**",
     "**Rmk (interface definition Def-H.34).**", 1),
]
TRANSFORMS = [
    ("Part2_Bosonic_era.md",
     "everything the corpus says is either a fixed number",
     "every quantity the corpus derives is either a fixed number", 1),
    ("Part4_Baryomesonic_era.md",
     "the fourth is not, and the corpus says why",
     "the fourth is not, and the structure yields why", 1),
    ("Part4_Baryomesonic_era.md",
     "Where the machinery has no domain the corpus says so instead:",
     "Where the machinery has no domain, the structure yields the obstruction instead:", 1),
    ("Part4_Baryomesonic_era.md",
     "Add the edges and you get six; add the masses and you get nothing.",
     "Adding the edges yields six; adding the masses yields nothing.", 1),
]
MAP_REWRITES = [
    ("Part1_Qubit_era.md",
     "**Census.md** (the computed data cells, cited row-wise by tag)",
     "**the Census annex** (Appendix A of this volume; the computed data cells, cited row-wise by tag)", 1),
    ("Part1_Qubit_era.md",
     "**HistLog.md** (the historical and open ledger; citations are pointers, $\\neg$premises)",
     "**the archival HistLog** (working_markdowns/HistLog.md; the historical and open ledger; citations are pointers, $\\neg$premises)", 1),
    ("Part1_Qubit_era.md", "Part 1 (this file):", "Part 1 (this chapter):", 1),
    ("Part1_Qubit_era.md",
     "Part 3: Def-H.1–Def-H.43, FT.1–FT.145 (structural tags), FT.153–FT.155.",
     "Part 3: Def-H.1–Def-H.43, FT.1–FT.114, FT.116–FT.131, FT.133–FT.139, FT.141–FT.145 (structural tags), FT.153–FT.160.", 1),
    ("Part1_Qubit_era.md",
     "Part 4: Def-BM.1–Def-BM.2, BM.1–BM.6.",
     "Part 4: Def-BM.1–Def-BM.20, BM.1–BM.152.", 1),
    ("Part3_Fermion_era.md",
     "**Census.md** (the computed data cells:",
     "**the Census annex** (Appendix A of this volume; the computed data cells:", 1),
    ("Part3_Fermion_era.md",
     "**HistLog.md** (§I declaration dispositions, §II open ledger — pointers, $\\neg$premises)",
     "**the archival HistLog** (working_markdowns/HistLog.md: §I declaration dispositions, §II open ledger — pointers, $\\neg$premises)", 1),
    ("Part4_Baryomesonic_era.md",
     "**Census.md** (the computed cells",
     "**the Census annex** (Appendix A of this volume; the computed cells", 1),
]

GEN_RMK_KEY = "**Rmk (the generator program's two distance claims, resolved).**"

# ---------------------------------------------------------------- helpers
def read(fn):
    return open(os.path.join(SRC, fn), encoding="utf-8").read()

def chunk_text(c):
    if c["kind"] in ("h1", "h2", "h3"):
        return c["text"]
    if c["kind"] == "raw":
        return c["text"]
    if c["kind"] == "paratag":
        return "\n".join(c["lines"])
    if c["kind"] == "tagblock":
        parts = []
        for kind, tag, title, lines in c["segs"]:
            parts.append("\n".join(lines))
        return c.get("headtext", "") + "\n" + "\n".join(parts)
    return ""

def set_chunk_text(c, new):
    """Write sanitized text back into a chunk (paragraph-shaped chunks only)."""
    if c["kind"] in ("raw", "h1", "h2", "h3"):
        c["text"] = new
    elif c["kind"] == "paratag":
        c["lines"] = new.split("\n")
    elif c["kind"] == "tagblock":
        # only valid when segs == [("main", ...)]
        assert len(c["segs"]) == 1 and c["segs"][0][0] == "main", c["tag"]
        c["segs"] = [("main", None, None, new.split("\n"))]

def apply_edits(chunks, fname, edits, kindname):
    for f, old, new, cnt in edits:
        if f != fname:
            continue
        hits = 0
        for c in chunks:
            if c["kind"] == "hr":
                continue
            t = chunk_text(c)
            if old in t:
                k = t.count(old)
                t = t.replace(old, new)
                set_chunk_text(c, t)
                hits += k
        if hits != cnt:
            log(kindname, fname, f"[canon-pre-applied or obsolete ({hits}/{cnt}) - skipped] `{old[:60]}`")
            continue
        for c in chunks:
            pass
        log(kindname, fname, f"[{hits}x] `{old[:90]}` -> `{new[:90]}`")

# ---------------------------------------------------------------- stage 1: parse
def stage_parse():
    docs = {}
    for fn in CANON + ["Census.md"]:
        docs[fn] = qparse.parse_file(os.path.join(SRC, fn), REG)
    return docs

# ---------------------------------------------------------------- stage 2: sanitize
def stage_sanitize(docs):
    # 2a. strips / transforms / map rewrites (main text only)
    for fn in CANON + ["Census.md"]:
        apply_edits(docs[fn], fn, STRIPS, "STRIP")
        apply_edits(docs[fn], fn, TRANSFORMS, "TRANSFORM")
        apply_edits(docs[fn], fn, MAP_REWRITES, "MAP-REWRITE")

    # 2b. passage move: the FT.48 generator-claims Rmk -> B.2 entry
    rmk_text = None
    for c in docs["Part3_Fermion_era.md"]:
        if c["kind"] == "tagblock" and c["tag"] == "FT.48":
            segs = []
            for kind, tag, title, lines in c["segs"]:
                keep = []
                for ln in lines:
                    if ln.startswith(GEN_RMK_KEY):
                        assert rmk_text is None
                        rmk_text = ln
                        keep.append("[[MOVEDSTUB:B2RMK]]")
                    else:
                        keep.append(ln)
                segs.append((kind, tag, title, keep))
            c["segs"] = segs
    assert rmk_text is not None, "FT.48 generator-claims Rmk not found"
    log("PASSAGE-MOVE", "Part3/FT.48",
        "Rmk (the generator program's two distance claims, resolved) -> Addendum B.2.1; "
        "cross-reference stub left in place")

    # 2c. whole-block moves -> stubs
    moved = {}     # tag -> (file, title, body-markdown, doc-position)
    for fn in CANON + ["Census.md"]:
        for pos, c in enumerate(docs[fn]):
            if c["kind"] == "tagblock" and c["tag"] in MOVE:
                body = []
                for kind, tag, title, lines in c["segs"]:
                    body.extend(lines)
                moved[c["tag"]] = (fn, c["title"], "\n".join(body), pos)
                c["kind"] = "stub"
                c["moved_to"] = None   # filled after B-id assignment
                log("BLOCK-MOVE", f"{fn}/{c['tag']}",
                    f"`{c['tag']} — {c['title'][:70]}` -> Addendum ({MOVE[c['tag']]})")
    missing = set(MOVE) - set(moved)
    assert not missing, missing
    return moved, rmk_text

# ---------------------------------------------------------------- HistLog §IV
def stage_histlog():
    src = read("HistLog.md")
    m = re.search(r"^## §IV — The adjudication record \(historical\)$", src, re.M)
    m2 = re.search(r"^## §V — Verification history$", src, re.M)
    assert m and m2 and m.start() < m2.start()
    sec = src[m.end():m2.start()]
    # split into §IV.0 note / §IV.1 / §IV.2 / §IV.3 at the bolded section leads
    iv0 = sec.split("**§IV.1")[0]
    rest = "**§IV.1" + sec.split("**§IV.1", 1)[1]
    iv1 = rest.split("**§IV.2")[0]
    rest2 = "**§IV.2" + rest.split("**§IV.2", 1)[1]
    iv2 = rest2.split("**§IV.3")[0]
    iv3 = "**§IV.3" + rest2.split("**§IV.3", 1)[1]
    # split §IV.1 into the four tag sections; §IV.3 into FT.146-152 sections
    def split_tags(text, tags):
        out = {}
        marks = []
        for t in tags:
            mm = re.search(r"(?m)^### " + re.escape(t) + r" — (.*)$", text)
            assert mm, (t, text[:200])
            marks.append((mm.start(), t, mm.group(1).strip(), mm.end()))
        marks.sort()
        for k, (pos, t, title, head_end) in enumerate(marks):
            end = marks[k + 1][0] if k + 1 < len(marks) else len(text)
            out[t] = (title, text[head_end:end].strip())
        return out
    iv1_tags = split_tags(re.sub(r"(?m)^\*\*§IV\.1[^\n]*\n", "", iv1), ["FT.115", "FT.121", "FT.132", "FT.140"])
    iv3_tags = split_tags(re.sub(r"(?m)^\*\*§IV\.3[^\n]*\n", "", iv3),
                          ["FT.146", "FT.147", "FT.148", "FT.149", "FT.150", "FT.151", "FT.152"])
    iv0_note = re.sub(r"(?m)^\*\*§IV\.0 Note\.\*\*", "**Note (HistLog §IV.0).**", iv0.strip())
    iv2_body = re.sub(r"(?m)^\*\*§IV\.2[^\n]*\n", "", iv2).strip()
    log("HISTLOG-EXTRACT", "HistLog.md §IV",
        "FT.115/FT.121/FT.132/FT.140 (§IV.1), §IV.2 closure exports, FT.146–FT.152 (§IV.3) "
        "-> Addendum B.1.1–B.1.12 (verbatim)")
    return iv0_note, iv1_tags, iv2_body, iv3_tags

# ---------------------------------------------------------------- B-id assignment
def assign_ids(moved, hist):
    iv0_note, iv1_tags, iv2_body, iv3_tags = hist
    entries = {"B1": [], "B2": [], "B3": [], "B4": []}
    # B.1: HistLog record first
    for t in ("FT.115", "FT.121", "FT.132", "FT.140"):
        title, body = iv1_tags[t]
        entries["B1"].append({"type": "histlog", "tag": t,
                              "title": title, "body": body,
                              "src": "HistLog §IV.1"})
    entries["B1"].append({"type": "histlog", "tag": None,
                          "title": "Tier closure exports and ledger updates (Q/R tiers)",
                          "body": iv2_body, "src": "HistLog §IV.2"})
    for t in ("FT.146", "FT.147", "FT.148", "FT.149", "FT.150", "FT.151", "FT.152"):
        title, body = iv3_tags[t]
        entries["B1"].append({"type": "histlog", "tag": t,
                              "title": title, "body": body,
                              "src": "HistLog §IV.3 (the closure tier F.43)"})
    # moved blocks in era order
    def sortkey(t):
        return (PARTNO[moved[t][0]], moved[t][3])
    for t in sorted([x for x in moved if MOVE[x] == "B1"], key=sortkey):
        fn, title, body = moved[t][0], moved[t][1], moved[t][2]
        entries["B1"].append({"type": "block", "tag": t, "title": title, "body": body,
                              "src": f"Part {PARTNO[fn]} ({fn})"})
    # B.2: the FT.48 Rmk passage first
    entries["B2"].append({"type": "rmk", "tag": "FT.48 (Rmk)",
                          "title": "The two distance claims of the derivation record, resolved",
                          "body": None, "src": "Part 3 (FT.48 block)"})
    for t in sorted([x for x in moved if MOVE[x] == "B2"], key=sortkey):
        fn, title, body = moved[t][0], moved[t][1], moved[t][2]
        entries["B2"].append({"type": "block", "tag": t, "title": title, "body": body,
                              "src": f"Part {PARTNO[fn]} ({fn})"})
    for t in sorted([x for x in moved if MOVE[x] == "B3"], key=sortkey):
        fn, title, body = moved[t][0], moved[t][1], moved[t][2]
        entries["B3"].append({"type": "block", "tag": t, "title": title, "body": body,
                              "src": f"Part {PARTNO[fn]} ({fn})"})
    for t in sorted([x for x in moved if MOVE[x] == "B4"], key=sortkey):
        fn, title, body = moved[t][0], moved[t][1], moved[t][2]
        entries["B4"].append({"type": "block", "tag": t, "title": title, "body": body,
                              "src": f"Part {PARTNO[fn]} ({fn})"})
    # assign ids
    ids = {}
    for sec in ("B1", "B2", "B3", "B4"):
        for k, e in enumerate(entries[sec], 1):
            e["id"] = f"B.{sec[1]}.{k}"
            if e["type"] == "block":
                ids[e["tag"]] = e["id"]
            elif e["type"] == "histlog" and e["tag"]:
                ids[e["tag"]] = e["id"]
    ids["B2RMK"] = ids.get("FT.48-RMK", entries["B2"][0]["id"])
    return entries, ids

def hist_title(tag, text):
    m = re.match(r"\*\*" + re.escape(tag) + r"\.\*\*\s*([^\n]*)", text)
    first = m.group(1).strip() if m else ""
    # take up to first sentence-ish boundary, strip markdown bold
    first = re.sub(r"\*\*", "", first)
    return (tag + (" — " + first[:110] if first else ""))

# ---------------------------------------------------------------- catalog entries
def build_catalog(docs, entries, ids, numbers):
    """Append catalog entries (kept-in-main rulings) to the section entry lists."""
    blocks = {}   # tag -> body markdown (from main docs, post-sanitize)
    for fn in CANON + ["Census.md"]:
        for c in docs[fn]:
            if c["kind"] == "tagblock":
                body = []
                for kind, tag, title, lines in c["segs"]:
                    body.extend(lines)
                blocks[c["tag"]] = (fn, c["title"], "\n".join(body))
    cat_log = []
    for sec, tag, key, _ in CATALOG:
        assert tag in blocks, f"catalog tag {tag} not found in main docs"
        fn, title, body = blocks[tag]
        quote = extract_quote(body, key)
        assert quote, f"catalog key {key!r} not found in {tag}"
        srcname = ("the Census annex (Appendix A)" if fn == "Census.md"
                   else f"Part {PARTNO[fn]}")
        e = {"type": "catalog", "tag": tag, "title": title, "quote": quote,
             "src": srcname, "mainref": numbers.get(tag, "?")}
        entries[sec].append(e)
        cat_log.append((sec, tag, e))
    # assign catalog ids (continue numbering)
    for sec in ("B1", "B2", "B3", "B4"):
        k = 0
        for e in entries[sec]:
            k += 1
            e["id"] = f"B.{sec[1]}.{k}"
    # pointer-only entries for B.4 (traps recorded inside moved/kept blocks)
    ptr = [
        ("FT.73(5)", "The standing trap pattern — comparing a derived pure number with a "
         "measured coupling constant (the $\\pi$-against-$1/137$ species) — is recorded at "
         "FT.73(5), reproduced in full at {ft73}."),
        ("FT.77(3),(5)", "The dimension-trap disclosures (comparing $m^2$-ratios to measured "
         "mass ratios; the amplitude-span near-coincidences) travel with the full audit at {ft77}."),
        ("FT.89(2)", "The Koide category trap (reading the derived rational $\\tfrac23$ as a "
         "measured mass-ratio datum) is adjudicated at {ft89}; the supersession of its "
         "classification clause by FT.158(5) is recorded there and at Theorem 3.94."),
        ("Census FT.99(6)", "The unreduced-versus-lowest-terms comparison trap is recorded, "
         "with its integrity ledger, in the Census annex (Appendix A, cell FT.99(6)(b))."),
    ]
    for tagref, text in ptr:
        entries["B4"].append({"type": "pointer", "tag": tagref, "title": None,
                              "text": text, "src": None})
    for sec in ("B1", "B2", "B3", "B4"):
        k = 0
        for e in entries[sec]:
            k += 1
            e["id"] = f"B.{sec[1]}.{k}"
    return cat_log

def extract_quote(body, key):
    """Verbatim quote: the display line or sentence containing key."""
    i = body.find(key)
    if i < 0:
        return None
    # display-line context?
    ls = body.rfind("$$", 0, i)
    le = body.find("$$", i)
    if ls >= 0 and le >= 0 and body.count("$", ls, i) % 2 == 1:
        seg = body[ls + 2:le].strip()
        seg = seg.replace("$", "").strip()
        assert len(seg) <= 900, f"display quote too long ({len(seg)}); pick a narrower key"
        return ("display", seg)
    # sentence context (never cross a display or line boundary)
    start = max(body.rfind(". ", 0, i), body.rfind("\n", 0, i)) + 1
    end = body.find(". ", i)
    end = end + 1 if end >= 0 else min(len(body), i + 400)
    seg = body[start:end + 1].strip()
    for stop in ("$", "\n"):
        k = seg.find(stop)
        if k >= 0:
            seg = seg[:k].strip()
    if len(seg) > 520:
        seg = seg[:520].rsplit(";", 1)[0] + "; \u2026"
    return ("text", seg)

# ---------------------------------------------------------------- numbering
def stage_number(docs, ids):
    """Assign presentation numbers to every tag occurrence in the main docs."""
    numbers = {}     # tag -> label string, e.g. "Theorem 1.3"
    counters = {}
    ENVNAME = {"theorem": "Theorem", "definition": "Definition", "axiom": "Axiom",
               "convention": "Convention", "corollary": "Corollary"}
    def bump(chap, cls):
        key = (chap, cls)
        counters[key] = counters.get(key, 0) + 1
        return counters[key]
    for fn in CANON + ["Census.md"]:
        chap = PARTNO[fn]
        chapletter = str(chap) if chap <= 4 else "A"
        for c in docs[fn]:
            if c["kind"] == "tagblock":
                cls = qparse.tag_class(c["tag"])
                if cls == "policy":
                    numbers[c["tag"]] = c["tag"]
                    continue
                k = bump(chap, "corollary" if False else cls)
                numbers[c["tag"]] = f"{ENVNAME[cls]} {chapletter}.{k}"
                for kind, tag, title, lines in c["segs"]:
                    if kind == "cor":
                        k2 = bump(chap, "corollary")
                        numbers[tag] = f"Corollary {chapletter}.{k2}"
            elif c["kind"] == "paratag":
                cls = "corollary" if c["is_cor"] else qparse.tag_class(c["tag"])
                if cls == "policy":
                    numbers[c["tag"]] = c["tag"]
                    continue
                k = bump(chap, cls)
                numbers[c["tag"]] = f"{ENVNAME[cls]} {chapletter}.{k}"
    # moved tags -> appendix ids
    for t, bid in ids.items():
        if t == "B2RMK":
            continue
        numbers[t] = f"Appendix {bid}"
    return numbers

if __name__ == "__main__":
    docs = stage_parse()
    moved, rmk = stage_sanitize(docs)
    hist = stage_histlog()
    entries, ids = assign_ids(moved, hist)
    numbers = stage_number(docs, ids)
    print("moved blocks:", len(moved), "| B entries:", {s: len(entries[s]) for s in entries})
    print("numbers assigned:", len(numbers))
    for t in ("CT0.1", "FT.1", "BM.1", "BM.152", "FT.77", "CT4.4a", "A1", "D0.1", "CT0.7a", "FT.28"):
        print(f"  {t:9s} -> {numbers.get(t)}")
