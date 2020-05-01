import requests
from interface import implements, Interface


class HostInterface(Interface):
    pass


class Host(implements(HostInterface)):

    billing_url: str
    domain: str

    def __init__(self, billing_url: str, domain: str):
        self.billing_url = billing_url
        self.domain = domain

    def __str__(self) -> str:
        token_auth_url = self.billing_url + '/host/' + self.domain
        response = requests.get(token_auth_url)
        response_json = response.json()
        if response_json['success'] is False:
            raise Exception("Domain is not exist")
        return response_json['url']


class CachedHost(implements(HostInterface)):

    __host: HostInterface
    __url: str

    def __init__(self, host: HostInterface):
        self.__host = host
        self.__url = None

    def __str__(self):
        if not self.__url:
            self.__url = str(self.__host)
        return self.__url


class FakeHost(implements(HostInterface)):

    increment = 0

    def __init__(self):
        pass

    def __str__(self):
        self.increment = self.increment + 1
        return 'host' + str(self.increment)
