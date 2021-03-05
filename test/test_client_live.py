def test_client_live_environment():
    import pywisetransfer

    pywisetransfer.api_key = "live-key"
    pywisetransfer.environment = "live"
    client = pywisetransfer.Client()

    domain = client.borderless_accounts.service.domain
    assert "api.sandbox.transferwise" not in domain
    assert "api.transferwise" in domain
