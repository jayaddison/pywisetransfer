# pytransferwise

An experimental Python client library for the [TransferWise Payouts API](https://api-docs.transferwise.com).

:warning: The classes, functions and interfaces that this library provides are very much in-development and prone to change.

## Installation

```bash
# Within your project directory
poetry add pytransferwise
```

## Usage

```python
import pytransferwise

pytransferwise.api_key = 'your-api-key-here'
# pytransferwise.environment = 'live'

client = pytransferwise.Client()

for profile in client.profiles.list():
    accounts = client.borderless_accounts.list(profile_id=profile.id)
    for account in accounts:
        currencies = [balance.currency for balance in account.balances]
        print(f"AccountID={account.id}, Currencies={currencies}")
```

## Run tests

```bash
# Within the pytransferwise working directory
poetry install
poetry run pytest --forked
```
