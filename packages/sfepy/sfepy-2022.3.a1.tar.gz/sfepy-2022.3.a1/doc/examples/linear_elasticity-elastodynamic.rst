.. _linear_elasticity-elastodynamic:

linear_elasticity/elastodynamic.py
==================================

**Description**


The linear elastodynamics solution of an iron plate impact problem.

Find :math:`\ul{u}` such that:

.. math::
    \int_{\Omega} \rho \ul{v} \pddiff{\ul{u}}{t}
    + \int_{\Omega} D_{ijkl}\ e_{ij}(\ul{v}) e_{kl}(\ul{u})
    = 0
    \;, \quad \forall \ul{v} \;,

where

.. math::
    D_{ijkl} = \mu (\delta_{ik} \delta_{jl}+\delta_{il} \delta_{jk}) +
    \lambda \ \delta_{ij} \delta_{kl}
    \;.

Notes
-----

The used elastodynamics solvers expect that the total vector of DOFs contains
three blocks in this order: the displacements, the velocities, and the
accelerations. This is achieved by defining three unknown variables ``'u'``,
``'du'``, ``'ddu'`` and the corresponding test variables, see the `variables`
definition. Then the solver can automatically extract the mass, damping (zero
here), and stiffness matrices as diagonal blocks of the global matrix. Note
also the use of the ``'dw_zero'`` (do-nothing) term that prevents the
velocity-related variables to be removed from the equations in the absence of a
damping term.

Usage Examples
--------------

Run with the default settings (the Newmark method, 3D problem, results stored
in ``output/ed/``)::

  python simple.py sfepy/examples/linear_elasticity/elastodynamic.py

Solve using the Bathe method::

  python simple.py sfepy/examples/linear_elasticity/elastodynamic.py -O "ts='tsb'"

View the resulting deformation using:

  python resview.py output/ed/user_block.h5 -f u:wu:p0 1:vw:p0 cauchy_strain:p1 cauchy_stress:p2 -s 18


.. image:: /../doc/images/gallery/linear_elasticity-elastodynamic.png


:download:`source code </../sfepy/examples/linear_elasticity/elastodynamic.py>`

.. literalinclude:: /../sfepy/examples/linear_elasticity/elastodynamic.py

