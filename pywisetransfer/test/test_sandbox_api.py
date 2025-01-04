"""This runs tests with the sandbox API.

In order to run these tests, you need to pass a token.

pytest --api_token <token>

The tests here run on the sandbox API on the web.
They make sure that we can actually deal with the data that is
up-to-date.

"""

from enum import IntEnum
from typing import Annotated

import pytest
from pywisetransfer.client import Client
from pywisetransfer.model.account import (
    LegalEntityType,
    AccountRequirement,
    RecipientAccountRequirements,
    RecipientAccountResponse,
    AccountRequirementType,
)
from pywisetransfer.model.currency import Currency, CurrencyCode
from pywisetransfer.model.profile import Profile, Profiles
from pywisetransfer.model.quote import ExampleQuoteRequest, PaymentMethod, QuoteRequest, QuoteResponse, QuoteStatus
from pywisetransfer.model.recipient import Recipient
from pywisetransfer.model.requirements import TransferRequirements
from pywisetransfer.model.transfer import TransferRequest, TransferResponse


class Order(IntEnum):
    """The order of tests."""
    
    GET_ACCOUNT_DATA = 1
    CREATE_ENTRIES = 2
    CREATE_QUOTE = 3
    CREATE_RECIPIENT = 4
    UPDATE_QUOTE = 5
    CREATE_TRANSFER = 6
    FUND_TRANSFER = 7
    SIMULATE_TRANSFER = 8


# ------------------- 1 - GET_ACCOUNT_DATA -------------------

@pytest.mark.order(Order.GET_ACCOUNT_DATA)
def test_1_1_two_profile_types(sandbox_profiles: Profiles):
    """Check the types of profiles we have."""
    assert len(sandbox_profiles) >= 2
    assert len(sandbox_profiles.business) >= 1
    assert len(sandbox_profiles.personal) >= 1

    assert sandbox_profiles.business[0].type == "business"
    assert sandbox_profiles.personal[0].type == "personal"

    assert sandbox_profiles.business[0].is_business()
    assert sandbox_profiles.personal[0].is_personal()

    assert not sandbox_profiles.personal[0].is_business()
    assert not sandbox_profiles.business[0].is_personal()

@pytest.mark.order(Order.GET_ACCOUNT_DATA)
def test_1_2_list_currencies(sandbox_currencies: list[Currency]):
    """Check the list of currencies."""
    assert len(sandbox_currencies) >= 1
    codes = [c.code for c in sandbox_currencies]
    assert "EUR" in codes
    assert "USD" in codes
    assert "GBP" in codes
    assert "AUD" in codes

@pytest.mark.order(Order.GET_ACCOUNT_DATA)
def test_1_3_list_balance(sandbox_personal_balances):
    """Check the list of currencies."""
    assert len(sandbox_personal_balances) >= 1
    currencies = [b.currency for b in sandbox_personal_balances]
    assert "EUR" in currencies
    assert "USD" in currencies
    assert "GBP" in currencies
    assert "AUD" in currencies

@pytest.mark.order(Order.GET_ACCOUNT_DATA)
def test_1_4_requirements(sandbox_requirements_gbp: list[AccountRequirement]):
    """Check that we can create the right requirements.

    We make sure that GBP sort code is in the requirements.
    """
    assert len(sandbox_requirements_gbp) > 0
    assert any(
        requirement.type == AccountRequirementType.sort_code
        for requirement in sandbox_requirements_gbp
    )

# ------------------- 2 - CREATE_ENTRIES -------------------


@pytest.mark.order(Order.CREATE_ENTRIES)
def test_2_1_example_quote(
    sandbox_example_quote: QuoteResponse, example_quote_request: ExampleQuoteRequest
):
    """Check that the example quote matches the request."""
    assert sandbox_example_quote.sourceCurrency == example_quote_request.sourceCurrency
    assert sandbox_example_quote.targetCurrency == example_quote_request.targetCurrency
    assert sandbox_example_quote.sourceAmount == example_quote_request.sourceAmount
    assert sandbox_example_quote.targetAmount == example_quote_request.targetAmount
    print(sandbox_example_quote.id)
    assert sandbox_example_quote.status == QuoteStatus.PENDING

@pytest.mark.order(Order.CREATE_ENTRIES)
def test__2_2_get_the_quote_again(
    sandbox_client: Client, sandbox_example_quote: QuoteResponse, sandbox_business_profile: Profile
):
    """Get the quote again and see if it changed."""
    quote: QuoteResponse = sandbox_client.quotes.get(
        sandbox_example_quote, sandbox_business_profile
    )
    assert quote.id == sandbox_example_quote.id

@pytest.mark.order(Order.CREATE_ENTRIES)
def test_2_3_email_recipient(
    sandbox_email_recipient: RecipientAccountResponse, 
):
    """Check the data matches."""
    print(sandbox_email_recipient.model_dump_json(indent=4))
    assert sandbox_email_recipient.currency == CurrencyCode.EUR
    assert sandbox_email_recipient.type == AccountRequirementType.email
    assert sandbox_email_recipient.legalEntityType == LegalEntityType.PERSON
    assert sandbox_email_recipient.email == "john@doe.com"

# ------------------- 3 - CREATE_QUOTE -------------------

@pytest.mark.order(Order.CREATE_QUOTE)
def test_3_1_create_quote(sandbox_quote_request: QuoteRequest, sandbox_quote: QuoteResponse):
    """Check that the request and the quote match."""
    assert sandbox_quote.id is not None
    assert sandbox_quote.sourceCurrency == sandbox_quote_request.sourceCurrency
    assert sandbox_quote.targetCurrency == sandbox_quote_request.targetCurrency
    assert sandbox_quote.sourceAmount == sandbox_quote_request.sourceAmount
    assert sandbox_quote.payOut == PaymentMethod.BANK_TRANSFER
    assert any(option.payIn == PaymentMethod.BANK_TRANSFER for option in sandbox_quote.paymentOptions)

@pytest.mark.order(Order.CREATE_QUOTE)
def test_3_2_quote_does_not_have_a_target_account(sandbox_quote_request: QuoteRequest):
    """Check that we can create a quote without targetAccount."""
    assert sandbox_quote_request.targetAccount is None

# ------------------- 4 - CREATE_RECIPIENT -------------------


@pytest.mark.order(Order.CREATE_RECIPIENT)
def test_4_1_iban_recipient(
    sandbox_iban_recipient: RecipientAccountResponse, sandbox_iban_recipient_request: Recipient
):
    """Check tha the data matches."""
    assert sandbox_iban_recipient.email == "max@mustermann.de"
    assert sandbox_iban_recipient.type == AccountRequirementType.iban
    assert not sandbox_iban_recipient.ownedByCustomer
    assert sandbox_iban_recipient.currency == sandbox_iban_recipient_request.currency

@pytest.mark.order(Order.CREATE_RECIPIENT)
def test_4_2_iban_is_a_requirement(sandbox_quote_requirements:RecipientAccountRequirements, sandbox_iban_recipient_request: Recipient):
    """Check that we can use iban"""
    assert sandbox_quote_requirements.iban is not None
    assert sandbox_quote_requirements.iban.required_keys == ["IBAN", "accountHolderName", "legalType"]
    assert sandbox_iban_recipient_request.accountHolderName is not None
    assert sandbox_iban_recipient_request.details.IBAN is not None
    assert sandbox_iban_recipient_request.details.legalType is not None

# ------------------- 5 - UPDATE_QUOTE -------------------

@pytest.mark.order(Order.UPDATE_QUOTE)
def test_5_1_updated_quote_matches_old_quote(sandbox_quote_updated:QuoteResponse, sandbox_quote :QuoteResponse):
    """Check the data macthes."""
    assert sandbox_quote_updated.id == sandbox_quote.id
    
@pytest.mark.order(Order.UPDATE_QUOTE)
def test_5_2_update_has_target(sandbox_quote_updated:QuoteResponse, sandbox_quote: QuoteResponse):
    """Check the data macthes."""
    # we seem not to know the target account
    assert sandbox_quote_updated.id == sandbox_quote.id

# ------------------- 6 - CREATE_TRANSFER -------------------


@pytest.mark.order(Order.CREATE_TRANSFER)
def test_6_1_requirements_include_reference(sandbox_transfer_requirements:TransferRequirements):
    """Check the requirements."""
    assert sandbox_transfer_requirements.transfer is not None
    assert sandbox_transfer_requirements.transfer.keys == ['reference']

@pytest.mark.order(Order.CREATE_TRANSFER)
def test_6_2_details_include_reference(sandbox_transfer_request:TransferRequest):
    """Check the details."""
    assert sandbox_transfer_request.details.reference == "Geschenk"


@pytest.mark.order(Order.CREATE_TRANSFER)
def test_6_3_transfer_matches(sandbox_transfer:TransferResponse, sandbox_transfer_request:TransferRequest):
    """Check the data macthes."""
    assert sandbox_transfer.id is not None
    assert sandbox_transfer.details.reference == sandbox_transfer_request.details.reference
    assert sandbox_transfer.targetAccount == sandbox_transfer_request.targetAccount
    assert sandbox_transfer.quoteUuid == sandbox_transfer_request.quoteUuid

# ------------------- 7 - FUND_TRANSFER -------------------





# ------------------- 8 - SIMULATE_TRANSFER -------------------
