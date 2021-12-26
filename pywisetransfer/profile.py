from apiron import JsonEndpoint
from munch import munchify

from pywisetransfer.base import Base


class ProfileService(Base):
    list = JsonEndpoint(path="/v1/profiles")
    get = JsonEndpoint(path="/v1/profiles/{profile_id}")


class Profile(object):
    def __init__(self, client):
        self.service = ProfileService(client=client)

    def list(self, type=None):
        profiles = munchify(self.service.list())
        return filter(lambda p: type is None or p.type == type, profiles)

    def get(self, profile_id):
        return munchify(self.service.get(profile_id=profile_id))
