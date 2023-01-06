# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'ACP2docs_en'
copyright = '2022, Ying Cheng Su'
author = 'Ying Cheng Su'
release = '2.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []

language = 'en'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'alabaster'
# html_static_path = ['_static']
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static', 'images']
html_logo = 'images/ACPainter_logo_text.png'
html_theme_options = {
    'logo_only': True,
    'display_version': True,
}
numfig = True
