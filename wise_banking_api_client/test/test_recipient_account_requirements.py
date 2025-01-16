"""Test the requirements for a recipient account."""

import pytest
from wise_banking_api_client.client import Client
from wise_banking_api_client.model.currency import Currency


def test_requirements_can_be_parsed(client: Client, currency: Currency):
    """Test the requirements for a recipient account.

    Here, we validate that all results can be parsed.
    """
    if currency in [
        Currency.ZMW,
        Currency.ZWG,
        Currency.UYW,
        Currency.STD,
        Currency.SSP,
        Currency.CNH,
    ]:
        pytest.skip("Not recorded yet.")
    requirements = client.recipient_accounts.get_requirements_for_currency(
        source=currency, target=currency, source_amount=100
    )
    assert True
