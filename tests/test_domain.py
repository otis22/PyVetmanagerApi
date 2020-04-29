import unittest
from unittest import mock
from vetmanager.domain import DomainProd, DomainLocal,\
    DomainTest, Host, CachedHost


class MockResponse:

    def __init__(self, json_data):
        self.json_data = json_data

    def json(self):
        return self.json_data


class FakeHost(Host):

    increment = 0

    def __init__(self):
        pass

    def url(self):
        self.increment = self.increment + 1
        return 'url' + str(self.increment)


class TestDomain(unittest.TestCase):

    @mock.patch('vetmanager.domain.requests.get')
    def test_prod_url(self, mock):
        mock.return_value = MockResponse({
            "success": True,
            "host": "vetmanager.ru",
            "url": "tests.vetmanager.ru"
        })
        domain = DomainProd('tests')

        self.assertEqual(
            domain.url(),
            'https://tests.vetmanager.ru'
        )

    @mock.patch('vetmanager.domain.requests.get')
    def test_test_url(self, mock):
        mock.return_value = MockResponse({
            "success": True,
            "host": ".tests.kube-dev.vetmanager.cloud",
            "url": "tests.tests.kube-dev.vetmanager.cloud"
        })
        domain = DomainTest('tests')
        self.assertEqual(
            domain.url(),
            'https://tests.tests.kube-dev.vetmanager.cloud'
        )

    def test_local_url(self):
        domain = DomainLocal('tests')
        self.assertEqual(domain.url(), 'http://tests.localhost:8080')


class TestCachedHost(unittest.TestCase):

    def test_cached_host(self):
        host = CachedHost(FakeHost())
        self.assertEqual(host.url(), 'url1')
        self.assertEqual(host.url(), 'url1')


if __name__ == '__main__':
    unittest.main()
