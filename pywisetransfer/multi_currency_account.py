from typing import Any

from munch import munchify

from pywisetransfer import Client
from pywisetransfer.base import Base
from pywisetransfer.endpoint import WiseEndpoint


class MultiCurrencyAccountService(Base):
    available_currencies = WiseEndpoint(
        path="/v2/borderless-accounts-configuration/profiles/{profile_id}/available-currencies"
    )
    get = WiseEndpoint(path="/v4/profiles/{profile_id}/multi-currency-account")


class MultiCurrencyAccount:
    def __init__(self, client: Client):
        self.service = MultiCurrencyAccountService(client=client)

    def available_currencies(self, profile_id: str) -> Any:
        return munchify(self.service.available_currencies(profile_id=profile_id))

    def get(self, profile_id: str) -> Any:
        return munchify(self.service.get(profile_id=profile_id))
