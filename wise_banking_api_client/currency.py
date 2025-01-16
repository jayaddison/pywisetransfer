"""The currency endpoint.

See https://docs.wise.com/api-docs/api-reference/currencies
"""

from typing import Any

from apiron import JsonEndpoint
from munch import munchify

from wise_banking_api_client import Client
from wise_banking_api_client.base import Base
from wise_banking_api_client.model.currency import Currency as CurrencyModel


class CurrencyService(Base):
    list = JsonEndpoint(path="/v1/currencies")


class Currency:
    def __init__(self, client: Client):
        self.service = CurrencyService(client=client)

    def list(self) -> list[CurrencyModel]:
        """Get a list of currencies.

        See https://docs.wise.com/api-docs/api-reference/currencies

        Returns:
            List of currencies.
        """
        return [CurrencyModel(**c) for c in self.service.list()]


__all__ = ["Currency"]
