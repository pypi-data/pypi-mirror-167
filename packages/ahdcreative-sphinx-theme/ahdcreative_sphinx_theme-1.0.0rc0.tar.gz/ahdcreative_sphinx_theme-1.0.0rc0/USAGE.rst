=====
Usage
=====

Select the "Sphinx AHD theme" in the ``conf.py`` file of a Sphinx project:

.. code-block:: python

   # include the theme in the list of extensions to be loaded
   extensions = ['sphinx_ahd_theme', ...]

   # select the theme
   html_theme = 'sphinx_ahd_theme'


For developers:

The following snippet should always work if appended at the end of ``conf.py``:

.. code-block:: python

   try:
      extensions
   except NameError:
      extensions = []

   extensions.append('sphinx_ahd_theme')
   html_theme = 'sphinx_ahd_theme'