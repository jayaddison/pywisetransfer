from apiron import JsonEndpoint

from pytransferwise.base import Base


class UserService(Base):
    me = JsonEndpoint(path="/v1/me")
    get = JsonEndpoint(path="/v1/users/{userId}")


class User(object):
    service = UserService()

    def me(self):
        return self.service.me()

    def get(self, user_id):
        return self.service.get(user_id=user_id)
