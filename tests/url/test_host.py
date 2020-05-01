import unittest
from unittest import mock
from vetmanager.url.host import Host, CachedHost, FakeHost


class MockResponse:

    def __init__(self, json_data):
        self.json_data = json_data

    def json(self):
        return self.json_data


class TestHost(unittest.TestCase):

    def test_cached_host(self):
        host = CachedHost(FakeHost())
        self.assertEqual(str(host), 'host1')
        self.assertEqual(str(host), 'host1')

    @mock.patch('vetmanager.url.host.requests.get')
    def test_host(self, mock):
        mock.return_value = MockResponse({
            "success": True,
            "host": ".testhost.test",
            "url": "test.testhost.test"
        })

        host = Host(billing_url='test', domain='test')
        self.assertEqual(str(host), 'test.testhost.test')


if __name__ == '__main__':
    unittest.main()
