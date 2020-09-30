# pytransferwise

An experimental Python client library for the [TransferWise API](https://api-docs.transferwise.com).

:warning: The classes, functions and interfaces that this library provides are very much in-development and prone to change.

## Installation

```bash
# Within your project directory
poetry add pytransferwise
```

## Usage

### API Requests

```python
import pytransferwise

pytransferwise.api_key = "your-api-key-here"
# pytransferwise.environment = "live"

client = pytransferwise.Client()

for profile in client.profiles.list():
    accounts = client.borderless_accounts.list(profile_id=profile.id)
    for account in accounts:
        currencies = [balance.currency for balance in account.balances]
        print(f"AccountID={account.id}, Currencies={currencies}")
```

### Webhook signature verification

```python
import pytransferwise
from pytransferwise.webhooks import verify_signature

# pytransferwise.environment = "live"

payload = b"webhook-request-body-here"
signature = "webhook-signature-data-here"

valid = verify_signature(payload, signature)
print(f"Valid webhook signature: {valid}")

```

## Run tests

Before run integration tests:
- test/test_get_account_statement.py

please perform the steps:
1. Get sandbox api key according [the docs here](https://api-docs.transferwise.com/#payouts-guide-api-access)
2. Set an environment variable 'TRANSFERWISE_API_KEY' with a value of your sandbox api key. 
```bash
# Within the pytransferwise working directory
poetry install
poetry run pytest --forked
```
