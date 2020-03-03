from apiron import JsonEndpoint
from munch import munchify

from pytransferwise.base import Base


class UserService(Base):
    me = JsonEndpoint(path="/v1/me")
    get = JsonEndpoint(path="/v1/users/{userId}")


class User(object):
    service = UserService()

    def me(self):
        return munchify(self.service.me())

    def get(self, user_id):
        return munchify(self.service.get(user_id=user_id))
