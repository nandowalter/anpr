#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# -- PROJECT Variables ----------------------------------------------------
settings_project_name = 'ANPR'
settings_copyright_year = '2017'
settings_copyright_name = 'Team per la Trasformazione Digitale'
settings_doc_version = ''
settings_doc_release = ''
settings_basename = 'ANPRdoc'
settings_file_name = 'ANPRdoc'

import sys
import os

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.ifconfig',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'
source_encoding = 'utf-8'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = settings_project_name
copyright = settings_copyright_year + ', ' + settings_copyright_name

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = settings_doc_version
# The full version, including alpha/beta/rc tags.
release = settings_doc_release

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None
language = 'it'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['.DS_Store', ]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# -- Options for HTML output ----------------------------------------------
html_theme = 'sphinx_italia_theme'

html_theme_path = ["_themes", ]

# -- ReadTheDoc requirements and local template generation---------------------

# on_rtd is whether we are on readthedocs.org, this line of code grabbed from docs.readthedocs.org
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

if not on_rtd:  # only import and set the theme if we're building docs locally
    html_theme = 'sphinx_italia_theme'
    html_theme_path = ["_themes", ]
else:
    # Override default css to get a larger width for ReadTheDoc build
    html_context = {
        'css_files': [
            'https://media.readthedocs.org/css/sphinx_rtd_theme.css',
            'https://media.readthedocs.org/css/readthedocs-doc-embed.css',
            '_static/css/theme.css',
        ],
    }

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%d/%m/%Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
html_use_smartypants = True

# Output file base name for HTML help builder.
htmlhelp_basename = settings_basename + 'doc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'a4paper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
#'preamble': '',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
  ('index', settings_file_name + '.tex', settings_project_name,
   settings_copyright_year + ', ' + settings_copyright_name, 'manual'),
]

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', settings_file_name, settings_project_name,
     [settings_copyright_name], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  ('index', settings_file_name, settings_project_name,
   settings_copyright_year + ', ' + settings_copyright_name, settings_project_name, settings_project_name,
   'Miscellaneous'),
]
