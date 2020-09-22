def test_client_live_environment():
    import pytransferwise

    pytransferwise.api_key = "live-key"
    pytransferwise.environment = "live"
    client = pytransferwise.Client()

    domain = client.borderless_accounts.service.domain
    assert "api.sandbox.transferwise" not in domain
    assert "api.transferwise" in domain
