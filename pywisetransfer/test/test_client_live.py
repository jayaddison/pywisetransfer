import pytest
import responses

from pywisetransfer.client import DEFAULT_PRIVATE_KEY, Client


@pytest.fixture
def me_response():
    return {
        "id": 101,
        "name": "Example Person",
        "email": "person@example.com",
        "active": True,
        "details": {
            "firstName": "Example",
            "lastName": "Person",
            "phoneNumber": "+37111111111",
            "occupation": "",
            "address": {
                "city": "Tallinn",
                "countryCode": "EE",
                "postCode": "11111",
                "state": "",
                "firstLine": "Road 123",
            },
            "dateOfBirth": "1977-01-01",
            "avatar": "https://lh6.googleusercontent.com/photo.jpg",
            "primaryAddress": 111,
        },
    }


@responses.activate
def test_client_live_environment(me_response):
    responses.add(
        responses.GET,
        "https://api.transferwise.com/v1/me",
        json=me_response,
    )
    import pywisetransfer

    client = pywisetransfer.Client(api_key="live-key", environment="live")
    client.users.me()  # retrieve authenticated user details

    domain = client.borderless_accounts.service.domain
    assert "api.sandbox.transferwise" not in domain
    assert "api.transferwise" in domain


def test_cannot_create_live_client_with_default_key():
    """Check we create an error for the default key."""
    with pytest.raises(ValueError):
        Client(
            api_key="live-key",
            private_key_data=DEFAULT_PRIVATE_KEY.read_bytes(),
            environment="live",
        )
    with pytest.raises(ValueError):
        Client(api_key="live-key", private_key_file=DEFAULT_PRIVATE_KEY, environment="live")
