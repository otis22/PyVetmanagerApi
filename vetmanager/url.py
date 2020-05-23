from .host import HostName


class Protocol:

    protocol: str

    def __init__(self, protocol: str):
        self.protocol = protocol

    def __str__(self) -> str:
        return self.protocol + '://'


class Url:

    protocol: Protocol
    host_name: HostName

    def __init__(self, protocol: Protocol, host_name: HostName):
        self.protocol = protocol
        self.host_name = host_name

    def __str__(self):
        return str(self.protocol) + str(self.host_name)
