# py-vetmanager-api

![Build Status](https://github.com/otis22/PyVetmanagerApi/workflows/Python%20package/badge.svg)
![Publish Status](https://github.com/otis22/PyVetmanagerApi/workflows/Publish%20to%20PyPi/badge.svg)


[![Run in Postman](https://run.pstmn.io/button.svg)](https://god.postman.co/run-collection/64d692ca1ea129218ccb)

Python library for work with vetmanager api

[Vetmanager](https://vetmanager.ru) - CRM for veterinary business. 

All CRM account has unique domain name, url address can changes:

* {$domainName}.vetmanager.ru
* {$domainName}.vetmanager2.ru
* {$domainName}.ru.vetmanager.cloud
* {$domainName}.eu.vetmanager.cloud

# Examples

```
# For get full url by domain name
from vetmanager.functions import url

clinic_url = url('mydomain')
print(clinic_url)
```

```

# For get auth token
from vetmanager.functions import url, token, token_credentials

try:
    user_token = token(
        url(domain='domain'),
        token_credentials(
            login='test',
            password='test',
            app_name='test'
        )
    )
    print(user_token)
except Exception as err: 
    print(err)
```

```
#For work with dev enviroments

from vetmanager.url import UrlFromGateway, HostGatewayUrl, BillingApiUrl,\
        Domain
from vetmanager.token import Token, Credentials
from vetmanager.token import Login, Password, AppName

try: 
    clinic_url = UrlFromGateway(
        HostGatewayUrl(
            BillingApiUrl("https://billing-api-test.kube-dev.vetmanager.cloud/"),
            Domain(domain)
        )
    )
    
    credentials = Credentials(
        Login('login'),
        Password('password'),
        AppName('app_name')
    )
    
    token_url = Token(
        clinic_url,
        credentials
    )
except Exception as e:
    print(e)
```

# For contributor

## Install test requirements 

```
pipenv install -d
```

## Run check
```
flake8 --count --show-source --statistics vetmanager tests
pytest --cov=vetmanager --cov-fail-under 90 tests/
```
or with pipenv `pipenv run check`

## For publish package

```
python setup.py sdist
twine upload --skip-existing dist/* -r testpypi
twine upload --skip-existing dist/*
```

```buildoutcfg

```
