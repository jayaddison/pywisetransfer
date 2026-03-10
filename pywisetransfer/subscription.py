from typing import Any

from munch import munchify

from pywisetransfer import Client
from pywisetransfer.base import Base
from pywisetransfer.endpoint import WiseEndpoint


class SubscriptionService(Base):
    list = WiseEndpoint(path="/v3/profiles/{profile_id}/subscriptions")
    get = WiseEndpoint(path="/v3/profiles/{profile_id}/subscriptions/{subscription_id}")


class Subscription:
    def __init__(self, client: Client):
        self.service = SubscriptionService(client=client)

    def list(self, profile_id: str) -> Any:
        return munchify(self.service.list(profile_id=profile_id))

    def get(self, profile_id: str, subscription_id: str) -> Any:
        return munchify(self.service.get(profile_id=profile_id, subscription_id=subscription_id))
