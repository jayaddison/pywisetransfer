"""This runs tests with the sandbox API.

In order to run these tests, you need to pass a token.

pytest --api_token <token>

"""

from pywisetransfer.model.currency import Currency
from pywisetransfer.model.profile import Profile, Profiles

def test_two_profile_types(sandbox_profiles:Profiles):
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


def test_list_currencies(sandbox_currencies:list[Currency]):
    """Check the list of currencies."""
    assert len(sandbox_currencies) >= 1
    codes = [c.code for c in sandbox_currencies]
    assert "EUR" in codes
    assert "USD" in codes
    assert "GBP" in codes
    assert "AUD" in codes


def test_list_balance(sandbox_personal_balances):
    """Check the list of currencies."""
    assert len(sandbox_personal_balances) >= 1
    currencies = [b.currency for b in sandbox_personal_balances]
    assert "EUR" in currencies
    assert "USD" in currencies
    assert "GBP" in currencies
    assert "AUD" in currencies