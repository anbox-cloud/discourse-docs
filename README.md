# Overview

Copy of the documentation maintained on
https://discourse.ubuntu.com/c/anbox-cloud/documentation/50 to apply a regular git base
review workflow on top.

# Running pre-commit checks
* Install the `pre-commit` package from the Ubuntu repositories.
* Install the `aspell` and `aspell-en` packages from the Ubuntu repositories. This is required by
  the spellchecker.
* Navigate to the top-level directory of this repository and run `pre-commit install --install-hooks`.
* The following checks are run automatically before every commit.
  - Inclusive naming checks (`woke`)
  - Spellcheck (`spellcheck`)
  - Docs links checker (`anbox-cloud-docs-links-checker`)
