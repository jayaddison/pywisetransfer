"""This contains the endpoints for the accounts.

An account can be a
- (Recipient) Account
- Refund Account

Attributes:
    ACCEPT_MINOR_VERSION_1: Please note that to use v1.1 Accept-Minor-Version: 1 request header must be set.
"""

from typing import List, Optional
from pywisetransfer.base import Base
from pywisetransfer.client import Client
from pywisetransfer.endpoint import JsonEndpoint
from pywisetransfer.model.account import (
    RecipientAccountList,
    RecipientAccountRequest,
    RecipientAccountResponse,
    RecipientAccountRequirement,
)
from pywisetransfer.model.currency import Currency
from pywisetransfer.model.enum import StrEnum
from pywisetransfer.model.quote import QuoteResponse


ACCEPT_MINOR_VERSION_1 = {"Accept-Minor-Version": "1"}


class RecipientAccountService(Base):
    list = JsonEndpoint(path="/v2/accounts")  # ?profileId={{profileId}}&currency={{currency}}
    create_recipient = JsonEndpoint(default_method="POST", path="/v1/accounts")
    get = JsonEndpoint(path="/v2/accounts/{account_id}")
    get_quote_requirements = JsonEndpoint(
        path="/v1/quotes/{quote_id}/account-requirements", additional_headers=ACCEPT_MINOR_VERSION_1
    )
    get_requirements = JsonEndpoint(
        path="/v1/account-requirements",
        required_params=["source", "target", "sourceAmount"],
        additional_headers=ACCEPT_MINOR_VERSION_1,
    )


class SortRecipientAccounts(StrEnum):
    """Sorting options for recipient accounts.

    Attributes:
        ID_ASC: Sort by ID ascending
        ID_DESC: Sort by ID descending
        CURRENCY_ASC: Sort by currency ascending
        CURRENCY_DESC: Sort by currency descending
    """

    ID_ASC = "id,asc"
    ID_DESC = "id,desc"
    CURRENCY_ASC = "currency,asc"
    CURRENCY_DESC = "currency,desc"


class RecipientAccount:
    def __init__(self, client: Client):
        self.service = RecipientAccountService(client=client)

    def list(
        self,
        *,
        size: Optional[int] = None,
        seek_position: Optional[int] = None,
        sort: Optional[SortRecipientAccounts] = None,
        profile: Optional[int] = None,
        currency: Optional[str] = None,
        creator: Optional[int] = None,
        active: Optional[bool] = None,
        type: Optional[str] = None,
        owned_by_customer: Optional[bool] = None
    ) -> RecipientAccountList:
        """List existing recipient accounts.

        Args:
            creator: Creator id of the account.
            profile: Profile id of the account.
            currency: Currency of the account.
            active: Filter by whether this profile is active. Defaults to true.
            type: Filter responses by account type, comma separated values are supported (e.g. "iban,swift_code").
            owned_by_customer: Filter to get accounts owned by the customer or not, leave out to get all accounts.
            size: Page size of the response. Defaults to a maximum of 20.
            seek_position: Account ID to start the page of responses from in the response. null if no more pages.
            sort: Sorting strategy for the response. Comma separated options: firstly either id or currency, followed by asc or desc for direction.

        """
        params = self.service.get_params_for_endpoint(
            profile_id=profile,
            currency=currency,
            size=size,
            seek_position=seek_position,
            sort=sort,
            creator_id=creator,
            type=type,
            owned_by_customer=owned_by_customer,
            active=active,
        )
        response = self.service.list(params=params)
        return RecipientAccountList(**response)

    def create_recipient(
        self, recipient_account: RecipientAccountRequest
    ) -> RecipientAccountResponse:
        return RecipientAccountResponse(**self.service.create_recipient(json=recipient_account))

    def get(self, account_id: int) -> RecipientAccountResponse:
        return RecipientAccountResponse(**self.service.get(account_id=account_id))

    def get_requirements_for_quote(
        self, quote: int | QuoteResponse
    ) -> List[RecipientAccountRequirement]:
        """Get the requirements for a recipient account.

        Args:
            quote: The quote id
        """
        return [
            RecipientAccountRequirement(**requirement)
            for requirement in self.service.get_quote_requirements(quote_id=quote)
        ]

    def get_requirements_for_currency(
        self,
        source: str | Currency,
        target: str | Currency,
        source_amount=float | int,
    ) -> List[RecipientAccountRequirement]:
        params = self.service.get_params_for_endpoint(
            source=source,
            target=target,
            source_amount=source_amount,
        )
        """Get the requirements for a recipient account.
        
        Args:
            quote: The quote id
            source: The source currency (3 letters)
            target: The target currency (3 letters)
            source_amount: The source amount
        """
        response = self.service.get_requirements(params=params)
        return [RecipientAccountRequirement(**requirement) for requirement in response]


__all__ = ["RecipientAccount", "SortRecipientAccounts"]
