from apiron import JsonEndpoint
from munch import munchify

from pytransferwise.base import Base


class ProfileService(Base):
    list = JsonEndpoint(path="/v1/profiles")
    get = JsonEndpoint(path="/v1/profiles/{profile_id}")


class Profile(object):
    service = ProfileService()

    def list(self):
        return munchify(self.service.list())

    def get(self, profile_id):
        return munchify(self.service.get(profile_id=profile_id))
