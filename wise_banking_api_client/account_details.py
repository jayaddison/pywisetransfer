from typing import Any

from apiron import JsonEndpoint
from munch import munchify

from wise_banking_api_client import Client
from wise_banking_api_client.base import Base


class AccountDetailsService(Base):
    list = JsonEndpoint(path="/v1/profiles/{profile_id}/account-details")


class AccountDetails:
    def __init__(self, client: Client):
        self.service = AccountDetailsService(client=client)

    def list(self, profile_id: str) -> list[Any]:
        return munchify(self.service.list(profile_id=profile_id))
