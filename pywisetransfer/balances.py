from typing import Any

from apiron import JsonEndpoint
from munch import munchify

from pywisetransfer import Client
from pywisetransfer.base import Base


class BalancesService(Base):
    list = JsonEndpoint(path="/v4/profiles/{profile_id}/balances", required_params=["type"])
    get = JsonEndpoint(path="/v4/profiles/{profile_id}/balances/{balance_id}")


class Balances:
    def __init__(self, client: Client):
        self.service = BalancesService(client=client)

    def list(self, profile_id: str, type: str = "STANDARD") -> Any:
        valid_types = ["STANDARD", "SAVINGS"]
        assert type in valid_types, f"Invalid type '{type}'; value values are: {valid_types}"
        return munchify(self.service.list(profile_id=profile_id, type=type))

    def get(self, profile_id: str, balance_id: str) -> Any:
        return munchify(self.service.get(profile_id=profile_id, balance_id=balance_id))
