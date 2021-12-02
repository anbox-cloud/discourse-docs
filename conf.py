# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
from git import Repo

if not os.path.isdir('.theme-repo'):
    Repo.clone_from('https://github.com/evildmp/vanilla-sphinx-test', '.theme-repo')
if not os.path.islink('vanilla'):
    os.symlink('.theme-repo/vanilla', 'vanilla')

# -- Project information -----------------------------------------------------

project = 'Anbox Cloud documentation'
copyright = '2021, Canonical Ltd.'
author = 'Canonical Ltd.'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.intersphinx",
    "sphinx_tabs.tabs",
    "sphinx_reredirects"
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '.venv', '.theme-repo']

rst_epilog = """
.. include:: /reuse/substitutions.txt
"""

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme_path = ['.']
html_theme = 'vanilla'

html_show_sphinx = False
html_last_updated_fmt = ""

html_static_path = ['_static']
html_css_files = ['custom.css']

# Uses global TOC for side nav instead of default local TOC
html_sidebars = {
    '**': [
        'globaltoc.html',
    ]
}

# -- Redirects ---------------------------------------------------------------

redirects = {
    "component-versions/index": "../anbox/component-versions/",
    "supported-versions/index": "../anbox/supported-versions/",
    "roadmap/index": "../anbox/roadmap/",
    "changelog/index": "../anbox/release-notes/",
    "requirements/index": "../anbox/requirements/",
}
