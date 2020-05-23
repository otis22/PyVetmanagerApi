import requests


class Domain:

    domain: str

    def __init__(self, domain: str):
        self.domain = domain

    def __str__(self) -> str:
        return self.domain


class HostGatewayUrl:

    url: str
    domain: Domain

    def __init__(self, url: str, domain: Domain):
        self.url = url
        self.domain = domain

    def __str__(self) -> str:
        return self.url + '/host/' + str(self.domain)


class HostName:
    """Type for declarations of various ways to obtain a host name"""

    def __init__(self):
        raise NotImplementedError


class FakeHost(HostName):
    """class for testing, in a string it is 'fake.host' """

    def __init__(self):
        pass

    def __str__(self) -> str:
        return 'fake.host'


class HostNameFromHostGateway(HostName):

    host_gateway_url: HostGatewayUrl

    def __init__(self, host_gateway_url: HostGatewayUrl):
        self.host_gateway_url = host_gateway_url

    def __str__(self) -> str:
        response = requests.get(str(self.host_gateway_url))
        response_json = response.json()
        if 'success' not in response_json and 'url' not in response_json:
            raise Exception(
                'Invalid response from Host Gateway : {}'.format(response.text)
            )
        if response_json['success'] is False:
            raise Exception("Domain is not exist")
        return response_json['url']
