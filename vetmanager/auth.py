from vetmanager.domain import DomainTest
from vetmanager.token import Token

def test():
    return 1


def test2():
    return 2

def auth():
    domain = DomainTest('one')
    token = Token(
        login='komap16',
        password='123456AA',
        domain = domain,
        app_name='test'
    )
    token.auth()

