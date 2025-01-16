import pytest

import wise_banking_api_client


def test_client_missing_key():
    with pytest.raises(KeyError, match="wise_banking_api_client.api_key"):
        wise_banking_api_client.Client(api_key=None)


def test_client_invalid_environment():
    with pytest.raises(KeyError, match="wise_banking_api_client.environment"):
        wise_banking_api_client.Client(api_key="test-key", environment="test-environment")


def test_client_default_environment():
    client = wise_banking_api_client.Client(api_key="test-key")

    domain = client.borderless_accounts.service.domain
    assert "api.sandbox.transferwise" in domain
    assert "api.transferwise" not in domain


def test_client_domain_immutable():
    client = wise_banking_api_client.Client(api_key="test-key", environment="sandbox")

    domain = client.borderless_accounts.service.domain
    assert "api.sandbox.transferwise" in domain
    assert "api.transferwise" not in domain

    # Should not happen: modify the environment config after creating a client
    wise_banking_api_client.environment = "live"

    domain = client.borderless_accounts.service.domain
    assert "api.sandbox.transferwise" in domain
    assert "api.transferwise" not in domain
