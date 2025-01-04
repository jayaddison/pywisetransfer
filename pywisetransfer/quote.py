"""In order to create transfers, you have to create a quote.

See https://docs.wise.com/api-docs/api-reference/quote

> The quote resource defines the basic information required for a Wise transfer - the currencies to send between, the amount to send and the profile who is sending the money. The profile must be included when creating a quote.
> Quote is one of the required resources to create a transfer, along with the recipient who is to receive the funds.
> The quote response contains other information such as the exchange rate, the estimated delivery time and the methods the user can pay for the transfer. Not all of this information may apply to your use case.
> Upon creating a quote the current mid-market exchange rate is locked and will be used for the transfer that is created from the quote. The rate will be locked for 30 minutes to give a user time to complete the transfer creation flow.
"""

from __future__ import annotations

from pprint import pprint
from typing import Any, Optional

from pywisetransfer.model.account import FilledInRecipientAccountRequest, RecipientAccountResponse
from pywisetransfer.model.profile import Profile

from .endpoint import JsonEndpoint
from munch import munchify

from pywisetransfer import Client
from pywisetransfer.base import Base
from pywisetransfer.model.quote import QuoteRequest, QuoteResponse, ExampleQuoteRequest, QuoteUpdate


class QuoteService(Base):
    example = JsonEndpoint(
        default_method="POST",
        path="/v3/quotes",
    )
    create = JsonEndpoint(
        default_method="POST",
        path="/v3/profiles/{profile_id}/quotes",
    )
    patch = JsonEndpoint(
        default_method="PATCH",
        additional_headers={"Content-Type": "application/merge-patch+json"},
        path="/v3/profiles/{profile_id}/quotes/{quote_id}",
    )
    get = JsonEndpoint(
        default_method="GET",
        path="/v3/profiles/{profile_id}/quotes/{quote_id}",
    )


class Quote:
    def __init__(self, client: Client):
        self.service = QuoteService(client=client)

    def example(self, quote: ExampleQuoteRequest) -> QuoteResponse:
        """Create an un-authenticated quote.

        This quote cannot be used to create a transfer.

        Use this endpoint to get example quotes for people to see the exchange
        rate and fees Wise offers before a user has created or linked an account.
        This can drive a version of the quote screen that shows the user what Wise
        offers before they sign up. Note that this endpoint does not require a
        token to create the resource, however, since it is just an example,
        the returned quote has no ID so can't be used later to create a transfer.

        See https://docs.wise.com/api-docs/api-reference/quote#create-not-authenticated
        """
        response = self.service.example(json=quote)
        pprint(response)
        return QuoteResponse(**response)

    def create(self, quote: QuoteRequest, profile: int | Profile) -> QuoteResponse:
        """Create an authenticated quote.

        This quote can be used to create a transfer.

        https://docs.wise.com/api-docs/api-reference/quote#create-authenticated
        """
        response = self.service.create(json=quote, profile_id=profile)
        return QuoteResponse(**response)

    def update(
        self,
        quote_update: QuoteUpdate | FilledInRecipientAccountRequest | RecipientAccountResponse,
        quote: int | QuoteResponse,
        profile: int | Profile | None = None,
    ) -> QuoteResponse:
        """Update a quote.

        See https://docs.wise.com/api-docs/api-reference/quote#update

        Args:
            quote_update: An update to the quote.
                This can be a QuoteUpdate or a recipient account.
            quote: The quote to update. If you provie the id only, also provide the profile.
            profile: The profile to update the quote for.
                This is not required if the quote provides the profile id.
        """
        if isinstance(quote_update, (RecipientAccountResponse, FilledInRecipientAccountRequest)):
            quote_update = QuoteUpdate(targetAccount=quote_update.id)
        if not profile and isinstance(quote, QuoteResponse):
            profile = quote.profile
        response = self.service.patch(json=quote_update, profile_id=profile, quote_id=quote)
        pprint(response)
        print("targetAccount" in response)
        return QuoteResponse(**response)

    def get(self, quote: int | QuoteResponse, profile: Optional[int | Profile] = None):
        """Get an existing quote.

        Get quote info by ID. If the quote has expired (not used to create a transfer
        within 30 minutes of quote creation), it will only be accessible for
        approximately 48 hours via this endpoint.

        Args:
            quote: The quote to get. If you provie the id only, also provide the profile.
            profile: The profile to get the quote for. This is not required if the quote response provides the profile id.

        Returns:
            QuoteResponse: The quote
        """
        if not profile and isinstance(quote, QuoteResponse):
            profile = quote.profile
        response = self.service.get(quote_id=quote, profile_id=profile)
        return QuoteResponse(**response)


__all__ = ["Quote", "QuoteService", "ExampleQuoteRequest", "QuoteResponse"]
