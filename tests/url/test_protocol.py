import unittest
from vetmanager.url.protocol import HTTP, HTTPS


class TestProtocol(unittest.TestCase):

    def test_http(self):
        self.assertEqual(str(HTTP()), 'http://')

    def test_https(self):
        self.assertEqual(str(HTTPS()), 'https://')


if __name__ == '__main__':
    unittest.main()
