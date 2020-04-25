import unittest
from vetmanager import auth


class TestAuth(unittest.TestCase):
    def test_test(self):
        self.assertEqual(auth.test(), 1, "Should be 1")

    def test_test2(self):
        self.assertEqual(auth.test2(), 2, "Should be 2")

    def test_auth(self):
        auth.auth()
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()
