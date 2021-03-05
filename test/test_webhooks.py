import pytest

from pywisetransfer.webhooks import verify_signature


@pytest.fixture
def valid_payload():
    return b'{"data":{"resource":{"id":0,"profile_id":0,"type":"balance-account"},"amount":0.01,"currency":"EUR","post_transaction_balance_amount":0.01,"occurred_at":"2020-03-02T14:30:03Z","transaction_type":"credit"},"subscription_id":"00000000-0000-0000-0000-000000000000","event_type":"balances#credit","schema_version":"2.0.0","sent_at":"2020-03-02T14:30:03Z"}'


@pytest.fixture
def corrupt_payload():
    return b'{"data":{"resource":{"id":0,"profile_id":0,"type":"balance-account"},"amount":0.02,"currency":"EUR","post_transaction_balance_amount":0.01,"occurred_at":"2020-03-02T14:30:03Z","transaction_type":"credit"},"subscription_id":"00000000-0000-0000-0000-000000000000","event_type":"balances#credit","schema_version":"2.0.0","sent_at":"2020-03-02T14:30:03Z"}'


@pytest.fixture
def valid_signature():
    return "eZsnoryOFBa9lNT2rR0cLU18P84M1SQP7p+tru5f+5KJHnx8yL6nM3jHbSs03ah3Eh/nOsLCD4FjSi7nsQD1p3wboxAuOA7lyXEI4nxTPcYyxeAG9M4pT2eyDDl4kG/npbV7QuWpFoWDhtDoz33OvJS0Sy7tU1v0WigeuxJxHoV44/g9+ERF4I13Jl6vF0CMk9o/911Sc4z0NgRgZFR2MTRpKJHXLm8OsRXWJeZy86XgOvNSj52DB2WugtPfE4kYIt65d/Hod3XlWgJknx5O/IYKjaPl17+rXxkn/loWsy/DITy9y443D1hOLA/ohgGH4tTsljizGTykdFJxoD4CNA=="


@pytest.fixture
def corrupt_signature():
    return "eZsnoryOFBa9lNT2rR0cLU18P84M1SQP7p+tru6f+5KJHnx8yL6nM3jHbSs03ah3Eh/nOsLCD4FjSi7nsQD1p3wboxAuOA7lyXEI4nxTPcYyxeAG9M4pT2eyDDl4kG/npbV7QuWpFoWDhtDoz33OvJS0Sy7tU1v0WigeuxJxHoV44/g9+ERF4I13Jl6vF0CMk9o/911Sc4z0NgRgZFR2MTRpKJHXLm8OsRXWJeZy86XgOvNSj52DB2WugtPfE4kYIt65d/Hod3XlWgJknx5O/IYKjaPl17+rXxkn/loWsy/DITy9y443D1hOLA/ohgGH4tTsljizGTykdFJxoD4CNA=="


def test_correct_signature(valid_payload, valid_signature):
    result = verify_signature(valid_payload, valid_signature)
    assert result is True


def test_corrupt_payload(corrupt_payload, valid_signature):
    result = verify_signature(corrupt_payload, valid_signature)
    assert result is False


def test_corrupt_signature(valid_payload, corrupt_signature):
    result = verify_signature(valid_payload, corrupt_signature)
    assert result is False
