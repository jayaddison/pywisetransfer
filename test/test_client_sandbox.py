import pytest

import pywisetransfer


def setup_function(method):
    pywisetransfer.api_key = None
    pywisetransfer.environment = "sandbox"


def test_client_missing_key():
    with pytest.raises(KeyError, match="pywisetransfer.api_key"):
        pywisetransfer.Client()


def test_client_invalid_environment():
    pywisetransfer.api_key = "test-key"
    pywisetransfer.environment = "test-environment"
    with pytest.raises(KeyError, match="pywisetransfer.environment"):
        pywisetransfer.Client()


def test_client_default_environment():
    pywisetransfer.api_key = "test-key"
    client = pywisetransfer.Client()

    domain = client.borderless_accounts.service.domain
    assert "api.sandbox.transferwise" in domain
    assert "api.transferwise" not in domain


def test_client_domain_immutable():
    assert pywisetransfer.environment == "sandbox"

    pywisetransfer.api_key = "test-key"
    client = pywisetransfer.Client()

    domain = client.borderless_accounts.service.domain
    assert "api.sandbox.transferwise" in domain
    assert "api.transferwise" not in domain

    # Should not happen: modify the environment config after creating a client
    pywisetransfer.environment = "live"

    domain = client.borderless_accounts.service.domain
    assert "api.sandbox.transferwise" in domain
    assert "api.transferwise" not in domain
