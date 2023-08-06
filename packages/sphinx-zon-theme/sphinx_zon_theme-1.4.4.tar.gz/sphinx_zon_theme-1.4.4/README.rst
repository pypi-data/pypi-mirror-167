============================
Sphinx Theme for ZEIT ONLINE
============================

Based on the fabulous `Read the Docs`_ theme.

.. _`Read the Docs`: https://github.com/rtfd/sphinx_rtd_theme


Usage
=====

Install the package, e.g. ``pip install sphinx_zon_theme``, and then set
``html_theme = 'sphinx_zon_theme'`` in your Sphinx ``conf.py``.


Features
========

* Automatically uses the ZON logo.
* Adds an "edit this page" link to the sidebar. To customize how this link is
  created, you can set the following::

    html_theme_options = {
        'editme_link': (
            'https://github.com/zeitonline/{project}/edit/master/{page}')
    }

  (This is the default value, it supports two variables, ``project`` is taken
   directly from ``conf.py``, and ``page`` evaluates to
   ``path/to/current/page.suffix``)
