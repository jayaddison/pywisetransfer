import pytransferwise


def setup_function(method):
    pytransferwise.api_key = None
    pytransferwise.environment = "sandbox"


def test_client_live_environment():
    pytransferwise.api_key = "live-key"
    pytransferwise.environment = "live"
    client = pytransferwise.Client()

    domain = client.borderless_accounts.domain
    assert "api.sandbox.transferwise" not in domain
    assert "api.transferwise" in domain
