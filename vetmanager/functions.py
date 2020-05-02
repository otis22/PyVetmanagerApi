from .domain import UrlInterface, Url
from .url.host import Host
from .url.protocol import HTTPS
from .billing import BillingApiUrlProduction


def url(domain) -> UrlInterface:

    return Url(HTTPS(), Host(
            billing_url=BillingApiUrlProduction(),
            domain=domain
        ))
