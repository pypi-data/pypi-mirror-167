mrbob.kita
=================


``mrbob.kita`` is a set of `mr.bob
<https://mrbob.readthedocs.io/en/latest/>`_
templates to use when developing kita addons.


Install
~~~~~~~

  .. code:: shell

    pip install mrbob.kita

Quickstart
~~~~~~~~~~

CAUTION: it is recommanded to backup or vcs commit your current
directory before running these commands, so you can easily see
what has been generated and/or changed.

Create a new addon in the current directory:

  .. code:: shell

    mrbob kita:addon

Now go to the newly created addon directory and run this to
add a new model, with associated views, demo data, and acl:

  .. code:: shell

    mrbob kita:model

Add a test class:

  .. code:: shell

    mrbob kita:test

Add a wizard class:

  .. code:: shell

    mrbob kita:wizard

Tip: read the `mr.bob user guide
<http://mrbob.readthedocs.io/en/latest/userguide.html>`_.
In particular it explains how to set default values to avoid
retyping the same answers at each run (such as the copyright
author).


