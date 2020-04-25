from vetmanager.domain import DomainTest
from vetmanager.token import Token

domain = DomainTest('one')
token = Token(
    login='komap16',
    password='123456AA',
    domain=domain,
    app_name='test'
)
token.auth()

