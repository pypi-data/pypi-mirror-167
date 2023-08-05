.. _dg-advection_1D:

dg/advection_1D.py
==================

**Description**


Transient advection equation in 1D solved using discontinous galerkin method.

.. math:: \frac{dp}{dt} + a \cdot dp/dx = 0

    p(t,0) = p(t,1)


Usage Examples
--------------
Run with simple.py script::

    python simple.py sfepy/examples/dg/advection_1D.py

To view animated results use ``script/dg_plot_1D.py`` specifing name of the
output in ``output/`` folder, default is ``dg/advection_1D``::

    python simple.py script/dg_plot_1D.py dg/advection_1D

``script/dg_plot_1D.py`` also accepts full and relative paths::

    python ./script/dg_plot_1D.py output/dg/advection_1D




.. image:: /../doc/images/gallery/dg-advection_1D.png


:download:`source code </../sfepy/examples/dg/advection_1D.py>`

.. literalinclude:: /../sfepy/examples/dg/advection_1D.py

