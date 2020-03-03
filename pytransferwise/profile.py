from apiron import JsonEndpoint

from pytransferwise.base import Base


class ProfileService(Base):
    list = JsonEndpoint(path="/v1/profiles")
    get = JsonEndpoint(path="/v1/profiles/{profile_id}")


class Profile(object):
    service = ProfileService()

    def list(self):
        return self.service.list()

    def get(self, profile_id):
        return self.service.get(profile_id=profile_id)
