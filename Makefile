# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = .
BUILDDIR      = _build
VENV = .venv/bin/activate
PORT = 8001

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: html doc-incremental
html doc-incremental:
	. $(VENV); $(SPHINXBUILD) -b dirhtml . _build/html -w warnings.txt

.PHONY: doc
doc: install html

run:
	. $(VENV); sphinx-autobuild $(ALLSPHINXOPTS) --ignore ".git/*" --ignore "*.scss" . -b dirhtml -a _build/html --host 0.0.0.0 --port $(PORT)

spelling:
	sphinx-build -b spelling "$(SOURCEDIR)" "$(BUILDDIR)"

.PHONY: install
install:
	@echo "... setting up virtualenv"
	python3 -m venv .venv
	. $(VENV); pip install --upgrade -r requirements.txt
	@echo "\n" \
	  "--------------------------------------------------------------- \n" \
      "* watch, build and serve the documentation on port $(PORT): make run \n" \
	  "* check spelling: make spelling \n" \
	  "\n" \
      "enchant must be installed in order for pyenchant (and therefore \n" \
	  "spelling checks) to work. \n" \
	  "--------------------------------------------------------------- \n"

clean:
	rm -rf _build
	rm -rf .theme-repo
	rm -rf .venv
	rm -f vanilla
	rm -f warnings.txt

.PHONY: serve doc-serve
serve doc-serve:
	cd _build/html; python3 -m http.server $(PORT)

linkcheck:
	. $(VENV); $(SPHINXBUILD) -b linkcheck . _build/html
