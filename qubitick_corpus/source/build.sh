#!/usr/bin/env bash
# build.sh — regenerate the LaTeX sources from the archived canon and compile
# the three publication PDFs into docs/.
#
#   ./build.sh              # full build (tex + pdf)
#   ./build.sh --tex-only   # regenerate the .tex sources only
#
# Engine: tectonic (auto-fetched to ../tools/ when absent and the network
# allows) or a local xelatex/lualatex. The preamble uses fontspec, so a
# XeLaTeX-family engine is required; pdflatex alone will not compile it
# without removing the fontspec block.
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
exec python3 "$HERE/pipeline/build_all.py" "$@"
