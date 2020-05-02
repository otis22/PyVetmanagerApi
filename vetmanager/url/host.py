import requests
from vetmanager.decorators import only_once
from interface import implements, Interface


class HostInterface(Interface):
    pass


class Host(implements(HostInterface)):

    billing_url: str
    domain: str

    def __init__(self, billing_url: str, domain: str):
        self.billing_url = billing_url
        self.domain = domain

    @only_once
    def __str__(self) -> str:
        token_auth_url = self.billing_url + '/host/' + self.domain
        response = requests.get(token_auth_url)
        response_json = response.json()
        if response_json['success'] is False:
            raise Exception("Domain is not exist")
        return response_json['url']


class FakeHost(implements(HostInterface)):

    def __str__(self) -> str:
        return 'host'
