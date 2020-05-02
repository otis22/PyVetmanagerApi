from vetmanager.domain import UrlInterface, Url
from vetmanager.url.host import CachedHost, Host
from vetmanager.url.protocol import HTTPS


def url(domain) -> UrlInterface:
    host = CachedHost(
        Host(
            billing_url="https://billing-api.vetmanager.cloud/",
            domain=domain
        )
    )
    return Url(HTTPS(), host)
