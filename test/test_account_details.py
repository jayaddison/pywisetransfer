import pytest
import responses

from pywisetransfer import Client
from pywisetransfer.exceptions import WiseAccessDeniedException


@pytest.fixture
def mocked_responses():
    with responses.RequestsMock() as r:
        yield r


@pytest.fixture
def account_details_url():
    return "https://api.sandbox.transferwise.tech/v1/profiles/0/account-details"


@pytest.fixture
def account_details_forbidden(account_details_url, mocked_responses):
    mocked_responses.add(
        responses.GET,
        account_details_url,
        status=403,
        json={
            "code": "access.denied",
            "message": "No message",
            "timestamp": "2026-03-10T20:52:09.513439090Z",
        },
    )


def test_account_details_access_forbidden(account_details_forbidden):
    client = Client(api_key="test-key")
    with pytest.raises(WiseAccessDeniedException):
        client.account_details.list(profile_id=0)
