# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = '学习笔记'
copyright = 'Wang Shun'
author = '王顺'
release = '2024.01'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extension = [
   "sphinxawesome.highlighting",
   # To help you with the upgrade to version 5:
   # "sphinxawesome.deprecated",
]
needs_sphinx = '' # minimum supported version of Sphinx required for this project
templates_path = ['_templates']
exclude_patterns = []

language = 'zh_CN'

numfig = True
numfig_format = {
        'code-block': '代码 %s',
        'figure': '图 %s',
        'table': '表 %s',
        }
# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
html_favicon = 'media/favicon.ico'
html_theme = 'furo' #'sphinxawesome_theme'
html_static_path = ['_static']
rst_prolog = """
.. role:: raw-html(raw)
    :format: html

"""

