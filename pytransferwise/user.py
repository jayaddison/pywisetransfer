from apiron import JsonEndpoint

from pytransferwise.base import Base


class User(Base):
    me = JsonEndpoint(path="/v1/me")
    get = JsonEndpoint(path="/v1/users/{userId}")
