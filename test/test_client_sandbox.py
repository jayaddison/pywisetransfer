import pytest

import pytransferwise


def setup_function(method):
    pytransferwise.api_key = None
    pytransferwise.environment = "sandbox"


def test_client_missing_key():
    with pytest.raises(KeyError, match="pytransferwise.api_key"):
        pytransferwise.Client()


def test_client_invalid_environment():
    pytransferwise.api_key = "test-key"
    pytransferwise.environment = "test-environment"
    with pytest.raises(KeyError, match="pytransferwise.environment"):
        pytransferwise.Client()


def test_client_default_environment():
    pytransferwise.api_key = "test-key"
    client = pytransferwise.Client()

    domain = client.borderless_accounts.service.domain
    assert "api.sandbox.transferwise" in domain
    assert "api.transferwise" not in domain
