from typing import Any

from apiron import JsonEndpoint
from munch import munchify

from pywisetransfer import Client
from pywisetransfer.base import Base


class UserService(Base):
    me = JsonEndpoint(path="/v1/me")
    get = JsonEndpoint(path="/v1/users/{userId}")


class User(object):
    def __init__(self, client: Client):
        self.service = UserService(client=client)

    def me(self) -> Any:
        return munchify(self.service.me())

    def get(self, user_id: str) -> Any:
        return munchify(self.service.get(user_id=user_id))
