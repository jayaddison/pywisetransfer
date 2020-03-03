from apiron import JsonEndpoint

from pytransferwise.base import Base


class Profile(Base):
    list = JsonEndpoint(path="/v1/profiles")
    get = JsonEndpoint(path="/v1/profiles/{profileId}")
