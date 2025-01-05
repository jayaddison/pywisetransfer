from __future__ import annotations

import functools
from typing import Any

from apiron import JsonEndpoint

from pywisetransfer import Client
from pywisetransfer.base import Base
from pywisetransfer.model.profile import Profiles, profile_type, Profile as ProfileModel


class ProfileService(Base):
    list = JsonEndpoint(path="/v1/profiles")
    get = JsonEndpoint(path="/v1/profiles/{profile_id}")


class Profile:
    def __init__(self, client: Client):
        self.service = ProfileService(client=client)

    def list(self, type: profile_type | None = None) -> Profiles:
        """List all the profiles.

        Args:
            type: Filter by type.
        """
        profiles = Profiles(ProfileModel(**p) for p in self.service.list())
        if type is None:
            return profiles
        return Profiles([p for p in profiles if p.type == type])

    def get(self, profile_id: int) -> Any:
        """Get a profile by id."""
        return ProfileModel(**self.service.get(profile_id=profile_id))

    @property
    @functools.cache
    def business(self) -> list[Profile]:
        """Business profiles.

        This is a shortcut for listing them.
        The result is also cached for fast access.
        """
        return self.list(type=profile_type.business).business

    @property
    @functools.cache
    def personal(self) -> Profile:
        """Return the one personal profile.

        This is a shortcut for listing them.
        The result is also cached for fast access.

        Raises:
            IndexError: If there is no personal profile (unlikely)
        """
        return self.list(type=profile_type.personal).personal[0]


__all__ = ["Profile"]
