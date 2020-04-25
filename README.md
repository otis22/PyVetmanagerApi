# PyVetmanagerApi
Python library for work with vetmanager api

# Examples

```
try:
    domain = DomainTest('tests')
    client = VetmanagerClient('test_app', domain)
catch  Exception as err: 
    print(str(err))
```


# For contributor

## Run tests

```python -m unittest discover tests```

## Publish

```
twine upload dist/* -r testpypi
twine upload dist/*
```