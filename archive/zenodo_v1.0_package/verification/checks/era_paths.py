"""era_paths.py — legacy filename → era-canon resolver for the checker suite.

The four-era restructure replaced the letter-series files:
  A_axioms.md            -> Part1_Qubit_era.md + Part2_Bosonic_era.md (definitions D2–D4, symbol rows)
  B_foundation.md        -> Part1_Qubit_era.md
  C/D/E/F/G_*.md         -> Part2_Bosonic_era.md
  H,J,K,L,M,N,O,P,Q,R_*.md -> Part3_Fermion_era.md + Census.md (+ HistLog.md for ledger text)
  S_registries_and_gaps.md -> HistLog.md
  T_rung_closure.md      -> HistLog.md + Census.md (§Consumption)
  H_archive/*            -> EXTERNALIZED: the 21 first editions now live in a
                            separate historical-archive repository.  ARCHIVE_PRESENT
                            reports whether they are bundled; read() yields "" for an
                            absent one and records it in ABSENT, so checkers gate
                            their first-edition pins instead of crashing.

`read(name)` returns the concatenation of the mapped canon files (deduplicated),
or the literal file when the name is not a legacy canon file. Content checkers
pin exact substrings; the transplanted theorem mathematics is unmodified, so the
pins resolve against the concatenation.
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.normpath(os.path.join(HERE, ".."))

_P3 = ["Part3_Fermion_era.md", "Census.md", "HistLog.md"]
MAP = {
    "A_axioms.md": ["Part1_Qubit_era.md", "Part2_Bosonic_era.md"],
    "B_foundation.md": ["Part1_Qubit_era.md"],
    "C_geometry.md": ["Part2_Bosonic_era.md"],
    "D_electroweak.md": ["Part2_Bosonic_era.md"],
    "E_electromagnetic.md": ["Part2_Bosonic_era.md"],
    "F_color.md": ["Part2_Bosonic_era.md"],
    "G_saturation.md": ["Part2_Bosonic_era.md"],
    "H_measurement_and_forces.md": _P3,
    "J_floor_families.md": _P3,
    "K_spin_and_stability.md": _P3,
    "L_flicker_and_domains.md": _P3,
    "M_spectra_and_audits.md": _P3,
    "N_clifford_and_branches.md": _P3,
    "O_path_integrals.md": _P3,
    "P_family_channels.md": _P3,
    "Q_carrier_and_parity.md": _P3,
    "R_rung_one.md": _P3,
    "S_registries_and_gaps.md": ["HistLog.md"],
    "T_rung_closure.md": ["HistLog.md", "Census.md"],
}

# ---------------------------------------------------------------------------
#  The bundled first editions (H_archive/H01-H21) were externalized: they now
#  live in a separate historical-archive repository that traces the theory from
#  its roots.  This resolver is the single place that knows whether they are
#  present, so the content checkers can gate their first-edition pins on it
#  instead of crashing.  When the archive IS bundled - in this repo or in the
#  archive repo's own checkout - every gated pin runs again unchanged.
# ---------------------------------------------------------------------------
ARCHIVE_DIR = os.path.join(DOCS, "H_archive")
ARCHIVE_PRESENT = os.path.isdir(ARCHIVE_DIR)
#: archive documents requested while absent, for the skip report
ABSENT = []

def archive_note(checker=""):
    """one-line banner explaining why the first-edition pins were skipped"""
    if ARCHIVE_PRESENT:
        return None
    who = (" (%s)" % checker) if checker else ""
    return ("  SKIP%s: H_archive/ is not bundled - the 21 first editions live in the "
            "external historical-archive repository, so the first-edition identity pins "
            "are gated off (%d archive document(s) requested)." % (who, len(ABSENT)))

_cache = {}

def read(name):
    if name in _cache:
        return _cache[name]
    files = MAP.get(name)
    if files is None:
        path = os.path.join(DOCS, name)
        if not os.path.exists(path):
            alt = os.path.join(DOCS, "H_archive", name)   # bare archive names
            if os.path.exists(alt):
                path = alt
        if not os.path.exists(path):
            # an externalized first edition: report it and yield "" rather than
            # raising, so a checker that forgot to gate degrades visibly instead
            # of dying at import time
            if name.startswith("H_archive/") or os.path.dirname(name) == "":
                ABSENT.append(name)
                _cache[name] = ""
                return ""
        with open(path, encoding="utf-8") as f:
            txt = f.read()
    else:
        seen, chunks = set(), []
        for fn in files:
            with open(os.path.join(DOCS, fn), encoding="utf-8") as f:
                t = f.read()
            if t not in seen:
                seen.add(t)
                chunks.append(t)
        txt = "\n".join(chunks)
    _cache[name] = txt
    return txt
