.. currentmodule:: mashov

.. Mashov.py documentation master file, created by
   sphinx-quickstart on Sat Sep 14 18:19:45 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Mashov.py documentation
=======================

To use the library, you need to create a client: you can use a :class:`~UsernamePasswordClient` or a :class:`~TokenClient`

.. toctree::
   :maxdepth: 2
   :caption: Contents:


Client
======
.. autoclass:: Client
   :members:

.. autoclass:: UsernamePasswordClient
   :members:
   :inherited-members:

.. autoclass:: TokenClient
   :members:


Models
======
.. autoclass:: Grade
   :members: from_dict

.. autoclass:: School
   :members: from_params

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
