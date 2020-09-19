import os
import pytest

import pytransferwise

pytransferwise.api_key = os.getenv('TRANSFERWISE_API_KEY')
# print('Get value of TRANSFERWISE_API_KEY: {}'.format(pytransferwise.api_key))

client = pytransferwise.Client()


@pytest.fixture()
def interval_start():
    return '2020-08-01T00:00:00.000Z'


@pytest.fixture()
def interval_end():
    return '2020-08-01T23:59:59.999Z'


def test_get_statement_with_default_type_compact(interval_start, interval_end):
    """
    This is the smoke test of passing the optional parameter type 'COMPACT'
    The test does not check the logic of passed type value.
    """
    statements = []
    for profile in client.profiles.list():
        accounts = client.borderless_accounts.list(profile_id=profile.id)
        for account in accounts:
            currencies = [balance.currency for balance in account.balances]
            print(f"AccountID={account.id}, Currencies={currencies}")
            for currency in currencies:
                statement = client.borderless_accounts.statement(profile_id=profile.id,
                                                                 account_id=account.id,
                                                                 currency=currency,
                                                                 interval_start=interval_start,
                                                                 interval_end=interval_end)
                statements.append(statement)
    assert statements  # after the test execution we expect have {statements} as non empty list


def test_get_statement_with_type_flat(interval_start, interval_end):
    """
    This is the smoke test of passing the optional parameter type or 'FLAT'
    The test does not check the logic of passed type value.
    """
    statements = []
    for profile in client.profiles.list():
        accounts = client.borderless_accounts.list(profile_id=profile.id)
        for account in accounts:
            currencies = [balance.currency for balance in account.balances]
            print(f"AccountID={account.id}, Currencies={currencies}")
            for currency in currencies:
                statement = client.borderless_accounts.statement(profile_id=profile.id,
                                                                 account_id=account.id,
                                                                 currency=currency,
                                                                 interval_start=interval_start,
                                                                 interval_end=interval_end,
                                                                 statement_type='FLAT')
                statements.append(statement)
    assert statements  # after the test execution we expect have {statements} as non empty list
