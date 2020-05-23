from interface import implements, Interface


class BillingApiUrlInterface(Interface):
    pass


class BillingApiUrlProduction(implements(BillingApiUrlInterface)):

    def __str__(self):
        return 'https://billing-api.vetmanager.cloud/'


class BillingApiUrlTest(implements(BillingApiUrlInterface)):

    def __str__(self):
        return 'https://billing-api.vetmanager.cloud/'
