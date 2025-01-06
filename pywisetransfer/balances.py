from typing import Any

from apiron import JsonEndpoint
from munch import Munch, munchify

from pywisetransfer import Client
from pywisetransfer.base import Base
from pywisetransfer.model.profile import Profile


class BalancesService(Base):
    list = JsonEndpoint(path="/v4/profiles/{profileId}/balances", required_params=["types"])
    get = JsonEndpoint(path="/v4/profiles/{profileId}/balances/{balanceId}")


class Balances:
    def __init__(self, client: Client):
        self.service = BalancesService(client=client)

    def list(self, profile: int | Profile, types: str | list[str] = "STANDARD") -> list[Munch]:
        params = self.service.get_params_for_endpoint(types=types)
        kw = self.service.get_params_for_endpoint(profile_id=profile)
        return munchify(self.service.list(params=params, **kw))

    def get(self, profile: str, balance: str) -> Any:
        kw = self.service.get_params_for_endpoint(profile_id=profile, balance_id=balance)
        return munchify(self.service.get(**kw))
