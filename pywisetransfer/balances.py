from typing import Any

from apiron import JsonEndpoint
from munch import munchify

from pywisetransfer import Client
from pywisetransfer.base import Base


class BalancesService(Base):
    list = JsonEndpoint(path="/v4/profiles/{profile_id}/balances", required_params=["types"])
    get = JsonEndpoint(path="/v4/profiles/{profile_id}/balances/{balance_id}")


class Balances:
    def __init__(self, client: Client):
        self.service = BalancesService(client=client)

    def list(self, profile_id: str, types: str | list[str] = "STANDARD") -> Any:
        if not isinstance(types, list):
            assert isinstance(types, str)
            types = [types]

        valid_types = ["STANDARD", "SAVINGS"]
        for value in types:
            assert isinstance(value, str)
            if value not in valid_types:
                raise ValueError(f"Invalid type '{type}'; value values are: {valid_types}")

        params = {"types": ",".join(types)}
        return munchify(self.service.list(profile_id=profile_id, params=params))

    def get(self, profile_id: str, balance_id: str) -> Any:
        return munchify(self.service.get(profile_id=profile_id, balance_id=balance_id))
