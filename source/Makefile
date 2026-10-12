# Makefile — rebuild the Qubitick corpus v1.0 publication package.
#
#   make          # regenerate the .tex sources and compile the PDFs into ../docs
#   make tex      # regenerate the .tex sources only
#   make verify   # run the full machine-verification suite (expect 79/79 green)
#   make clean    # remove the disposable build/ intermediates
#
# Engine: tectonic (auto-fetched by the pipeline when absent) or xelatex.

PYTHON ?= python3

.PHONY: all tex verify clean

all:
	$(PYTHON) pipeline/build_all.py

tex:
	$(PYTHON) pipeline/build_all.py --tex-only

verify:
	cd ../era1/verification && $(PYTHON) run_all.py

clean:
	rm -rf ../build
