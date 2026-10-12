#!/usr/bin/env python3
"""build_all.py — regenerate every LaTeX source from the archived canon and
compile the three publication PDFs into docs/.

Usage:
    python3 build_all.py            # tex + pdf (main, addendum, calibration)
    python3 build_all.py --tex-only # regenerate the .tex sources only

Reads:  ../../working_markdowns/   (the byte-identical canon archive; never written)
Writes: ../ (source/*.tex, source/parts/*.tex, source/CONVERSION_LOG.md)
        ../../docs/*.pdf
        ../../build/               (flattened compile copies; disposable)

Engine: tectonic (discovered at ../../tools/tectonic, ~/tools/tectonic or on
PATH; auto-fetched when absent and the network allows) or a local
xelatex/lualatex. The preamble uses fontspec, so a XeLaTeX-family engine is
required.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import qtexify
import qcompile


def main(argv):
    tex_only = "--tex-only" in argv
    qtexify.main()
    if tex_only:
        print("--tex-only: skipping compilation")
        return 0
    qcompile.build_all("all")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
