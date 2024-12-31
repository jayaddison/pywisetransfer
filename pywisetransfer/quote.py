"""In order to create transfers, you have to create a quote.

See https://docs.wise.com/api-docs/api-reference/quote

> The quote resource defines the basic information required for a Wise transfer - the currencies to send between, the amount to send and the profile who is sending the money. The profile must be included when creating a quote.
> Quote is one of the required resources to create a transfer, along with the recipient who is to receive the funds.
> The quote response contains other information such as the exchange rate, the estimated delivery time and the methods the user can pay for the transfer. Not all of this information may apply to your use case.
> Upon creating a quote the current mid-market exchange rate is locked and will be used for the transfer that is created from the quote. The rate will be locked for 30 minutes to give a user time to complete the transfer creation flow.
"""

from __future__ import annotations

from pprint import pprint
from typing import Any

from .endpoint import JsonEndpoint
from munch import munchify

from pywisetransfer import Client
from pywisetransfer.base import Base
from pywisetransfer.model.quote import QuoteResponse, QuoteRequest


class QuoteService(Base):
    example = JsonEndpoint(
        default_method="POST",
        path="/v3/quotes",
    )


class Quote:
    def __init__(self, client: Client):
        self.service = QuoteService(client=client)

    def example(self, quote: QuoteRequest) -> QuoteResponse:
        response = self.service.example(json=quote.model_dump())
        # pprint(response)
        return QuoteResponse(**response)


__all__ = ["Quote", "QuoteService", "QuoteRequest", "QuoteResponse"]
