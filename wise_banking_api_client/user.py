from typing import Any

from munch import munchify

from wise_banking_api_client import Client
from wise_banking_api_client.base import Base
from wise_banking_api_client.endpoint import JsonEndpoint


class UserService(Base):
    me = JsonEndpoint(path="/v1/me")
    get = JsonEndpoint(path="/v1/users/{userId}")


class User:
    def __init__(self, client: Client):
        self.service = UserService(client=client)

    def me(self) -> Any:
        return munchify(self.service.me())

    def get(self, user_id: str) -> Any:
        return munchify(self.service.get(user_id=user_id))
