# This file is placed in the Public Domain.
# -*- coding: utf-8 -*-


import doctest
import sys
import os


curdir = os.getcwd()


sys.path.insert(0, curdir)
sys.path.insert(0, curdir + os.sep + '..' )


__version__ = "161"


needs_sphinx = '1.1'
nitpick_ignore = [
                ('py:class', 'builtins.BaseException'),
               ]


extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.doctest',
    'sphinx.ext.viewcode',
    'sphinx.ext.todo',
    'sphinx.ext.githubpages'
]


project = "BOTLIB"
version = '%s' % __version__
release = '%s' % __version__


html_short_title ="The Python3 ``bot`` Namespace"
html_title = "BOTLIB"
html_style = 'botlib.css'
html_static_path = ["_static"]
html_css_files = ["botlib.css",]
html_theme = "alabaster"
html_theme_options = {
    'github_user': 'bthate',
    'github_repo': 'botlib',
    'github_button': True,
    'github_banner': False,
    'logo': 'botdgreensmile.png',
    'link': '#000',
    'link_hover': '#000',
    'nosidebar': True,
    'show_powered_by': False,
    'show_relbar_top': False,
}
#html_theme_path = []
html_favicon = "botdgreensmile.png"
html_extra_path = []
html_last_updated_fmt = '%Y-%b-%d'
html_additional_pages = {}
html_domain_indices = False
html_sidebars = {
    '**': [
        'about.html',
        'searchbox.html',
        'navigation.html',
        'relations.html',
    ]
}
html_use_index = False
html_split_index = False
html_show_sourcelink = False
html_show_sphinx = False
html_show_copyright = False
html_copy_source = False
html_use_opensearch = 'http://botlib.rtfd.io/'
html_file_suffix = '.html'
htmlhelp_basename = 'pydoc'
templates_path = ['_templates']
source_suffix = '.rst'
source_encoding = 'utf-8-sig'
master_doc = 'index'
language = ''
today = ''
today_fmt = ''
exclude_patterns = ['_build', "_sources", "_templates"]
default_role = ''
add_function_parentheses = True
add_module_names = True
show_authors = True
pygments_style = 'colorful'
modindex_common_prefix = [""]
keep_warnings = True
rst_prolog = '''.. image:: botlib2.jpg
    :width: 100%
    :height: 2.3cm
    :target: index.html

.. raw:: html

    <center><b>

:ref:`home <home>` - :ref:`admin <admin>` - :ref:`programmer <programmer>` - :ref:`source <source>` - `pypi <http://pypi.org/project/botlib>`_ - `github <http://github.com/bthate/botlib>`_ - `sponsor <http://genocide.rtfd.io>`_

.. raw:: html

   </b>
   </center>

'''
autosummary_generate = True
autodoc_default_flags = ['members',
                         'undoc-members',
                         'private-members',
                         "imported-members"]
autodoc_member_order = 'bysource'
autodoc_docstring_signature = False
autoclass_content = "class"
doctest_global_setup = ""
doctest_global_cleanup = ""
doctest_test_doctest_blocks = "default"
trim_doctest_flags = True
doctest_flags = doctest.REPORT_UDIFF
intersphinx_mapping = {
                       'python': ('https://docs.python.org/3', 'objects.inv'),
                       'sphinx': ('http://sphinx.pocoo.org/', None),
                      }
intersphinx_cache_limit = 1
