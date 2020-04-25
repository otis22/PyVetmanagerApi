import requests

from vetmanager.domain import Domain
#TODO: write https://stackoverflow.com/questions/15753390/how-can-i-mock-requests-and-the-response test

class Token:
    domain: Domain
    login: str
    password: str
    app_name: str

    response: str
    def __init__(self, domain: Domain, login: str, password: str, app_name: str):
        self.domain = domain
        self.login = login
        self.password = password
        self.app_name = app_name
        pass

    def _get_auth_data(self):
        return {
            'login': self.login,
            'password': self.password,
            'app_name': self.app_name
        }

    def auth(self):
        try :
            response = requests.post(self.domain.url() +  '/token_auth.php', data = self._get_auth_data())
            response_json = response.json()
        except Exception:
            raise ExecutionError("Unknown Error")

        if response.status_code == 401:
            raise WrongAuthentificationException(response_json['title'])
        if response.status_code == 500:
            raise ExecutionError(response_json['title'])


