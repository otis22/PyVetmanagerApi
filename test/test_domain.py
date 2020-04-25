import unittest
from vetmanager.domain import DomainProd, DomainLocal, DomainTest


class TestDomain(unittest.TestCase):
    def test_prod_url(self):
        domain = DomainProd('test')
        self.assertEqual(domain.url(), 'https://test.vetmanager.ru')

    def test_test_url(self):
        domain = DomainTest('test')
        self.assertEqual(domain.url(), 'https://test.test.kube-dev.vetmanager.cloud')

    def test_local_url(self):
        domain = DomainLocal('test')
        self.assertEqual(domain.url(), 'http://test.localhost:8080')


if __name__ == '__main__':
    unittest.main()



