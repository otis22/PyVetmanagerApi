# py-vetmanager-api

![](https://github.com/otis22/PyVetmanagerApi/workflows/Python package/badge.svg)

Python library for work with vetmanager api

# Examples

```
try:
    domain = DomainProd('tests')
    client = VetmanagerClient('test_app', domain)
    token = client.token('admin', 'mypassword')
catch  Exception as err: 
    print(str(err))
```


# For contributor

## Run tests

```python -m unittest discover tests```

## For publish package

```
twine upload dist/* -r testpypi
twine upload dist/*
```