import requests


class Domain:

    protocol = 'https://'

    def url(self):
        return self.protocol + self.domain + self.server


class DomainProd(Domain):

    def __init__(self, domain):
        self.domain = domain

    def url(self):
        host = CachedHost(
            Host(
                billing_url="https://billing-api.vetmanager.cloud/",
                domain=self.domain
            )
        )
        return self.protocol + host.url()


class DomainTest(Domain):

    def __init__(self, domain):
        self.domain = domain

    def url(self):
        host = CachedHost(
            Host(
                billing_url="https://billing-api-test.kube-dev.vetmanager.cloud/",
                domain=self.domain
            )
        )
        return self.protocol + host.url()


class DomainLocal(Domain):

    protocol = 'http://'
    server = '.localhost:8080'

    def __init__(self, domain):
        self.domain = domain


class Host:

    billing_url: str
    domain: str

    def __init__(self, billing_url: str, domain: str):
        self.billing_url = billing_url
        self.domain = domain

    def url(self) -> str:
        token_auth_url = self.billing_url + '/host/' + self.domain
        response = requests.get(token_auth_url)
        response_json = response.json()
        if response_json['success'] is False:
            raise Exception("Domain is not exist")
        return response_json['url']


class CachedHost:

    host: Host
    _url: str

    def __init__(self, host: Host):
        self.host = host
        self._url = None

    def url(self):
        if not self._url:
            self._url = self.host.url()
        return self._url
