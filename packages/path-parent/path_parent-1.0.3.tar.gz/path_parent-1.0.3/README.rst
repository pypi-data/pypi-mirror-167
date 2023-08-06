path_parent
===========

Append ‘..’ to path setting.

This package append string ‘..’ to the path setting when being imported.

Install
=======

::

   pip install path_parent

Usage
=====

.. code:: python

   import path_parent.p        # append '..' to path setting;

   import path_parent.pp       # append '../..' to path setting;

   import path_parent.ppp      # append '../../..' to path setting;

   import path_parent          # nothing happen;

   path_parent.clear("../..")          # remove only '../..';

   path_parent.clear("..\..\..")       # nothing removed, not backslash;

   path_parent.clear()                 # remove all '..', '../..' and '../../..';
