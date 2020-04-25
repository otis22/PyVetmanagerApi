PyVetmanagerApi
=======

Python library for work with vetmanager api

Examples
=======

.. code-block:: python
    try:
        domain = DomainTest('tests')
        client = VetmanagerClient('test_app', domain)
    catch  Exception as err:
        print(str(err))



For contributor
=======
Run tests
=======

.. code-block:: python
    python -m unittest discover tests

