from apiron import JsonEndpoint
from munch import munchify

from pywisetransfer.base import Base


class UserService(Base):
    me = JsonEndpoint(path="/v1/me")
    get = JsonEndpoint(path="/v1/users/{userId}")


class User(object):
    def __init__(self, client):
        self.service = UserService(client=client)

    def me(self):
        return munchify(self.service.me())

    def get(self, user_id):
        return munchify(self.service.get(user_id=user_id))
