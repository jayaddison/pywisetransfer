from typing import Any

from apiron import JsonEndpoint
from munch import munchify

from pywisetransfer import Client
from pywisetransfer.base import Base


class MultiCurrencyAccountService(Base):
    available_currencies = JsonEndpoint(path="/v2/borderless-accounts-configuration/profiles/{profile_id}/available-currencies")
    get = JsonEndpoint(path="/v4/profiles/{profile_id}/multi-currency-account")


class MultiCurrencyAccount:
    def __init__(self, client: Client):
        self.service = MultiCurrencyAccountService(client=client)

    def available_currencies(self, profile_id: str) -> Any:
        return munchify(self.service.available_currencies(profile_id=profile_id))

    def get(self, profile_id: str) -> Any:
        return munchify(self.service.get(profile_id=profile_id))
