# pytransferwise

An experimental Python client library for the [TransferWise Payouts API](https://api-docs.transferwise.com).

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

pytransferwise.api_key = 'your-api-key-here'
# pytransferwise.environment = 'live'

client = pytransferwise.Client()

for profile in client.profiles.list():
    accounts = client.borderless_accounts.list(profile_id=profile.id)
    for account in accounts:
        currencies = [balance.currency for balance in account.balances]
        print(f"AccountID={account.id}, Currencies={currencies}")
```

### Webhook signature verification

```python
# Signature retrieved from x-signature header in webhook request
import pytransferwise
from pytransferwise.webhooks import verify_signature

# pytransferwise.environment = 'live'

payload = b'webhook-request-body-here'
signature = 'webhook-signature-data-here'

valid = verify_signature(payload, signature)
print(f"Valid webhook signature: {valid}")

```

## Run tests

```bash
# Within the pytransferwise working directory
poetry install
poetry run pytest --forked
```
