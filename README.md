# py-vetmanager-api

![Build Status](https://github.com/otis22/PyVetmanagerApi/workflows/Python%20package/badge.svg)

Python library for work with vetmanager api

# Examples

```
try:
    url = url('domain_name')
    client = VetmanagerClient('test_app', url)
    token = client.token('admin', 'mypassword')
catch  Exception as err: 
    print(str(err))
```


# For contributor

## Check codestyle

```
flake8 vetmanager --count --show-source --statistics && flake8 tests --count --show-source --statistics
```

## Run tests

```pytest --cov=vetmanager --cov-fail-under 90 tests/```

## For publish package

```
python setup.py sdist
twine upload --skip-existing dist/* -r testpypi
twine upload --skip-existing dist/*
```