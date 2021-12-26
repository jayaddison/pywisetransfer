def test_client_live_environment():
    import pywisetransfer

    client = pywisetransfer.Client(api_key="live-key", environment="live")

    domain = client.borderless_accounts.service.domain
    assert "api.sandbox.transferwise" not in domain
    assert "api.transferwise" in domain
