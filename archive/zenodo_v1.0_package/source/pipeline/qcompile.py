import sys, os, re, shutil
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(ROOT, "qubitick_corpus_v1.0", "working_markdowns", "tools"))
import rp_patched as rp

PKG = os.path.dirname(os.path.dirname(HERE))
OUT = os.path.join(PKG, "source")
DOCS = os.path.join(PKG, "docs")
FLAT = os.path.join(PKG, "build")

def find_engine():
    for cand in (os.path.join(PKG, "tools", "tectonic"),
                 os.path.join(os.path.expanduser("~"), "tools", "tectonic"),
                 shutil.which("tectonic"), shutil.which("xelatex"),
                 shutil.which("lualatex")):
        if cand and os.path.exists(cand) and os.access(cand, os.X_OK):
            return [cand]
    return None

def fetch_engine():
    import tarfile, tempfile, urllib.request
    dst = os.path.join(PKG, "tools")
    os.makedirs(dst, exist_ok=True)
    print("fetching tectonic ...")
    data = urllib.request.urlopen(rp.TECTONIC_URL, timeout=300).read()
    with tempfile.NamedTemporaryFile(suffix=".tar.gz", delete=False) as f:
        f.write(data); tmp = f.name
    with tarfile.open(tmp) as t:
        t.extractall(dst)
    os.remove(tmp)
    os.chmod(os.path.join(dst, "tectonic"), 0o755)
    return [os.path.join(dst, "tectonic")]

ENGINE = None   # resolved in build_all()/main

def flatten(tex_path, out_path):
    src = open(tex_path, encoding="utf-8").read()
    base = os.path.dirname(tex_path)
    def repl(m):
        inc = os.path.join(base, m.group(1))
        if not inc.endswith(".tex"):
            inc += ".tex"
        return open(inc, encoding="utf-8").read()
    flat = re.sub(r"\\input\{([^}]+)\}", repl, src)
    open(out_path, "w", encoding="utf-8").write(flat)
    return out_path

def compile_doc(tex_path, outdir, pdf_name, rounds=8):
    ok = rp.compile_and_repair(tex_path, outdir, ENGINE, rounds=rounds)
    base = os.path.splitext(os.path.basename(tex_path))[0]
    pdf = os.path.join(outdir, base + ".pdf")
    if ok and os.path.exists(pdf):
        shutil.copy(pdf, os.path.join(DOCS, pdf_name))
        print(f"PDF -> docs/{pdf_name} ({os.path.getsize(pdf)/1e6:.1f} MB)")
        return True
    print("FAILED:", tex_path)
    return False

def build_all(which="all"):
    global ENGINE
    if ENGINE is None:
        ENGINE = find_engine() or fetch_engine()
    print("engine:", ENGINE[0])
    os.makedirs(FLAT, exist_ok=True); os.makedirs(DOCS, exist_ok=True)
    if which in ("all", "main"):
        flat = flatten(os.path.join(OUT, "main.tex"), os.path.join(FLAT, "main_flat.tex"))
        compile_doc(flat, FLAT, "Qubitick_Corpus.pdf")
    if which in ("all", "addendum"):
        shutil.copy(os.path.join(OUT, "addendum.tex"), os.path.join(FLAT, "addendum_build.tex"))
        compile_doc(os.path.join(FLAT, "addendum_build.tex"), FLAT, "Addendum_Refutations.pdf")
    if which in ("all", "calib"):
        shutil.copy(os.path.join(OUT, "calibration.tex"), os.path.join(FLAT, "calibration_build.tex"))
        compile_doc(os.path.join(FLAT, "calibration_build.tex"), FLAT, "Calibration_Policy.pdf")

if __name__ == "__main__":
    build_all(sys.argv[1] if len(sys.argv) > 1 else "all")
