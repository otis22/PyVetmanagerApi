from interface import implements, Interface


class ProtocolInterface(Interface):

    pass


class HTTPS(implements(ProtocolInterface)):

    def __str__(self):
        return 'https://'


class HTTP(implements(ProtocolInterface)):

    def __str__(self):
        return 'http://'
