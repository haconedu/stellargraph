# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

import urllib.parse
import docutils
import sphinx

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
import re

sys.path.insert(0, os.path.abspath(".."))

version = {}
with open(os.path.abspath("../stellargraph/version.py"), "r") as fh:
    exec(fh.read(), version)

# -- Project information -----------------------------------------------------

project = "StellarGraph"
copyright = "2018-2020, Data61, CSIRO"
author = "Data61, CSIRO"

# Get global version
# see: https://packaging.python.org/guides/single-sourcing-package-version/
release = version["__version__"]

# The short X.Y version
m = re.match("^(\d+.\d+)", version["__version__"])
if m is None:
    raise RuntimeError("Couldn't parse version")
version = m.group()

# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.doctest",
    "sphinx.ext.todo",
    "sphinx.ext.coverage",
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
    "sphinx.ext.intersphinx",
    "recommonmark",
    "sphinx_markdown_tables",
    "nbsphinx",
    "nbsphinx_link",
    "notfound.extension",
    "sphinxcontrib.spelling",
]

# Add mappings
intersphinx_mapping = {
    "python": ("http://docs.python.org/3", None),
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
source_suffix = [".rst", ".md"]

# The master toctree document.
master_doc = "index"

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    "requirements.txt",
    "demos/community_detection/*",
    "demos/use-cases/*",
    "demos/interpretability/hateful-twitters-interpretability.nblink",
]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}

html_logo = "banner.png"

# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "StellarGraphdoc"


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',
    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (
        master_doc,
        "StellarGraph.tex",
        "StellarGraph Documentation",
        "Data61, CSIRO",
        "manual",
    ),
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(master_doc, "stellargraph", "StellarGraph Documentation", [author], 1)]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        "StellarGraph",
        "StellarGraph Documentation",
        author,
        "StellarGraph",
        "StellarGraph is a graph machine learning library for Python.",
        "Miscellaneous",
    ),
]

# -- Extension configuration -------------------------------------------------

# This is processed by Jinja2 and inserted before each notebook
# We use internal readthedocs variables to get the git version if available. Note that this is undocumented, however it
# is shown in our readthedocs build logs, and is generated from a template:
# https://github.com/readthedocs/readthedocs.org/blob/master/readthedocs/doc_builder/templates/doc_builder/conf.py.tmpl
nbsphinx_prolog = r"""
{% if env.config.html_context.github_version is defined and env.config.html_context.current_version != "stable" %}
    {% set git_revision = env.config.html_context.github_version %}
{% else %}
    {% set git_revision = "master" %}
{% endif %}

.. raw:: html

    <div class="admonition info">
      <p>
        Execute this notebook:
        <a href="https://mybinder.org/v2/gh/stellargraph/stellargraph/{{ git_revision }}?urlpath=lab/tree/{{ env.docname }}.ipynb" alt="Open In Binder"><img src="https://mybinder.org/badge_logo.svg"/></a>
        <a href="https://colab.research.google.com/github/stellargraph/stellargraph/blob/{{ git_revision }}/{{ env.docname }}.ipynb" alt="Open In Colab"><img src="https://colab.research.google.com/assets/colab-badge.svg"/></a>
        <a href="{{ env.docname.rsplit('/', 1).pop() }}.ipynb" class="btn">Download locally</a>
      </p>
    </div>
"""

nbsphinx_epilog = nbsphinx_prolog  # also insert after each notebook

# -- Options for todo extension ----------------------------------------------

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

# -- Options for spelling extension ------------------------------------------

spelling_lang = "en_AU"
tokenizer_lang = "en_AU"

# -- StellarGraph customisation ----------------------------------------------


class RewriteLinks(docutils.transforms.Transform):
    # before NBSphinx's link processing
    default_priority = 300

    RTD_PATH_RE = re.compile("^/(?P<lang>[^/]*)/(?P<version>[^/]*)/(?P<rest>.*)$")

    def _rewrite_rtd_link(self, node, refuri, parsed):
        """
        Rewrite deep links to the Read the Docs documentation to point to the relevant page in this
        build.

        Having full URLs is good when viewing the docs without rendering, such as with `help(...)`
        or `?...`, but internal links make for a more consistent experience (no jumping from
        .../1.2/ or .../latest/ to .../stable/) as well as allowing checks for validity. The
        rewriting done here gives the best of both worlds: full URLs without rendering, internal
        links within Sphinx.
        """
        env = self.document.settings.env
        match = self.RTD_PATH_RE.match(parsed.path)
        if not match:
            return

        lang = match["lang"]
        version = match["version"]
        rest = match["rest"]
        fragment = parsed.fragment

        # validate that the links all have the same basic structure:
        if lang != "en" or version != "stable" or not rest.endswith(".html"):
            self.document.reporter.warning(
                f"Links to stellargraph.readthedocs.io should always be to the stable english form <https://stellargraph.readthedocs.io/en/stable/...> and have the path end with a .html file extension, found language {lang!r}, version {version!r} and path ending with {rest[-8:]!r} in <{refuri}>"
            )
            return

        if rest == "api.html" and fragment:
            # a link to a Python element in the API: infer which one from the fragment. Examples:
            # - https://stellargraph.readthedocs.io/en/stable/api.html#module-stellargraph
            # - https://stellargraph.readthedocs.io/en/stable/api.html#stellargraph.StellarGraph
            # - https://stellargraph.readthedocs.io/en/stable/api.html#stellargraph.StellarGraph.to_networkx
            new_domain = "py"

            module_prefix = "module-"
            if fragment.startswith(module_prefix):
                new_type = "mod"
                new_target = fragment[len(module_prefix) :]
            else:
                new_type = "any"
                new_target = fragment
        else:
            # a link to a file (e.g. a demo)
            if fragment:
                self.document.reporter.warning(
                    f"Link <{refuri}> to stellargraph.readthedocs.io has a fragment {fragment!r} after #, which isn't yet supported for rewriting; remove the fragment, or search for this message in conf.py and extend it"
                )
                return

            html_suffix = ".html"
            new_domain = "std"
            new_type = "doc"
            new_target = "/" + rest[: -len(html_suffix)]

        xref = sphinx.addnodes.pending_xref(
            refdomain=new_domain,
            reftype=new_type,
            reftarget=new_target,
            refwarn=True,
            refexplicit=True,
            refdoc=env.docname,
        )

        linktext = node.astext()
        xref += docutils.nodes.Text(linktext, linktext)

        node.replace_self(xref)

    def apply(self):
        env = self.document.settings.env

        for node in self.document.traverse(docutils.nodes.reference):
            refuri = node.get("refuri")
            parsed = urllib.parse.urlparse(refuri)

            if parsed.netloc == "" and parsed.path.endswith("README.md"):
                # the notebooks include links to READMEs so that the links work locally and on
                # GitHub, but on Read the Docs, the equivalent files are 'index', not 'README'.
                new_path = parsed.path.replace("README.md", "index.rst")
                new_components = (
                    parsed.scheme,
                    parsed.netloc,
                    new_path,
                    parsed.params,
                    parsed.query,
                    parsed.fragment,
                )
                node["refuri"] = urllib.parse.urlunparse(new_components)

            elif parsed.netloc == "stellargraph.readthedocs.io":
                self._rewrite_rtd_link(node, refuri, parsed)


def setup(app):
    app.add_transform(RewriteLinks)

    app.add_stylesheet("custom.css")
