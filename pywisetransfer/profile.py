from apiron import JsonEndpoint
from munch import munchify

from pywisetransfer.base import Base


class ProfileService(Base):
    list = JsonEndpoint(path="/v1/profiles")
    get = JsonEndpoint(path="/v1/profiles/{profile_id}")


class Profile(object):
    service = ProfileService()

    def list(self, type=None):
        profiles = munchify(self.service.list())
        if type is None:
            return profiles
        return [p for p in profiles if p.type == type]

    def get(self, profile_id):
        return munchify(self.service.get(profile_id=profile_id))
