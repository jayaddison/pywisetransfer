from typing import Any

from munch import munchify

from pywisetransfer import Client
from pywisetransfer.base import Base
from pywisetransfer.endpoint import WiseEndpoint


class AccountDetailsService(Base):
    list = WiseEndpoint(path="/v1/profiles/{profile_id}/account-details")


class AccountDetails:
    def __init__(self, client: Client):
        self.service = AccountDetailsService(client=client)

    def list(self, profile_id: str) -> list[Any]:
        return munchify(self.service.list(profile_id=profile_id))
