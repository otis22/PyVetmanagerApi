import unittest
from vetmanager.billing import BillingApiUrlProduction, BillingApiUrlTest


class TestBilling(unittest.TestCase):

    def test_billing_api_url_production(self):
        self.assertEqual(
            str(BillingApiUrlProduction()),
            'https://billing-api.vetmanager.cloud/'
        )

    def test_billing_api_url_test(self):
        self.assertEqual(
            str(BillingApiUrlTest()),
            'https://billing-api.vetmanager.cloud/'
        )


if __name__ == '__main__':
    unittest.main()
