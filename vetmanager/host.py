import requests


class Domain:

    __domain: str

    def __init__(self, domain: str):
        self.__domain = domain

    def __str__(self) -> str:
        return self.__domain

    def __add__(self, other) -> str:
        return str(self) + other


class HostGatewayUrl:

    __url: str
    __domain: Domain

    def __init__(self, url: str, domain: Domain):
        self.__url = url
        self.__domain = domain

    def __str__(self) -> str:
        return self.__url + '/host/' + str(self.__domain)


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

    def __add__(self, other) -> str:
        return str(self) + other


class HostNameFromHostGateway(HostName):

    __host_gateway_url: HostGatewayUrl

    def __init__(self, host_gateway_url: HostGatewayUrl):
        self.__host_gateway_url = host_gateway_url

    def __invalid_response(self, response_json):
        return 'success' not in response_json \
            or 'url' not in response_json \
            or response_json['success'] is False

    def __str__(self) -> str:
        response = requests.get(str(self.__host_gateway_url))
        response_json = response.json()
        if self.__invalid_response(response_json):
            raise Exception(
                'Invalid response from Host Gateway : {}'.format(response.text)
            )
        return response_json['url']

    def __add__(self, other) -> str:
        return str(self) + other
