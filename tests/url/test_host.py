import unittest
from unittest import mock
from vetmanager.url.host import Host, FakeHost


class MockResponse:

    def __init__(self, json_data):
        self.json_data = json_data

    def json(self):
        return self.json_data


class TestHost(unittest.TestCase):

    def test_cached_property_host(self):
        host = FakeHost()
        self.assertEqual(str(host), 'host')

    @mock.patch('vetmanager.url.host.requests.get')
    def test_host_all_is_ok(self, mock):
        mock.return_value = MockResponse({
            "success": True,
            "host": ".testhost.test",
            "url": "test.testhost.test"
        })

        host = Host(billing_url='test', domain='test')
        self.assertEqual(str(host), 'test.testhost.test')

    @mock.patch('vetmanager.url.host.requests.get')
    def test_host_all_is_ok(self, mock):
        mock.return_value = MockResponse({
            "success": False,
            "message": 'some error message'
        })
        host = Host(billing_url='test', domain='test')
        with self.assertRaises(Exception):
            str(host)


if __name__ == '__main__':
    unittest.main()
