from typing import Any, List, Optional

from apiron import JsonEndpoint
from munch import munchify

from pywisetransfer import Client
from pywisetransfer.base import Base


class ProfileService(Base):
    list = JsonEndpoint(path="/v1/profiles")
    get = JsonEndpoint(path="/v1/profiles/{profile_id}")


class Profile:
    def __init__(self, client: Client):
        self.service = ProfileService(client=client)

    def list(self, type: Optional[str] = None) -> list[Any]:
        profiles: list[Any] = munchify(self.service.list())
        if type is None:
            return profiles
        return [p for p in profiles if p.type == type]

    def get(self, profile_id: str) -> Any:
        return munchify(self.service.get(profile_id=profile_id))
