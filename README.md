# Anbox Cloud documentation

This repository hosts a copy of the documentation maintained on the [Ubuntu discourse](https://discourse.ubuntu.com) under the [Anbox Cloud > Documentation](https://discourse.ubuntu.com/c/anbox-cloud/documentation/50) category. This is predominantly the source for updating Anbox Cloud documentation and is published to Anbox Cloud documentation via discourse to enable community feedback and engagement.

## Pre-commit checks
* The following checks are run automatically before every commit:
  - Inclusive language checks (`woke`)
  - Spellcheck (`spellcheck`)
  - Link checker that verifies if discourse links are used for all internal links (`anbox-cloud-docs-links-checker`)

### Running pre-commit checks

* Install the `pre-commit` package from the Ubuntu repositories.
* Install the `aspell` and `aspell-en` packages from the Ubuntu repositories. This is required by the spellchecker.
* Navigate to the top-level directory of this repository and run `pre-commit install --install-hooks`.

### Overriding pre-commit checks

* To disable the pre-commit hook, use `--no-verify` when running `git commit`.
* To skip a particular pre-commit check, prefix `SKIP=<pre-commit-hook-name>` when running `git commit`.
* To allow a valid word that is regularly used in the documentation but is flagged by `spellcheck`, add the word to `.wordlist.txt`.
* In special cases, there are ways to avoid a particular file or text from being flagged by `woke`. See [woke user guide](https://docs.getwoke.tech/ignore/).
