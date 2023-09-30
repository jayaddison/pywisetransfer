# pywisetransfer

An unofficial, experimental Python client library for the [TransferWise API](https://api-docs.transferwise.com).

:warning: The classes, functions and interfaces that this library provides are very much in-development and prone to change.

## Installation

```bash
# Within your project directory
pip install pywisetransfer
```

## Usage

### API Requests

```python
import pywisetransfer

client = pywisetransfer.Client(api_key="your-api-key-here")

for profile in client.profiles.list():
    accounts = client.borderless_accounts.list(profile_id=profile.id)
    for account in accounts:
        currencies = [balance.currency for balance in account.balances]
        print(f"AccountID={account.id}, Currencies={currencies}")
```

### Webhook signature verification

```python
from flask import abort, request
from pywisetransfer.webhooks import validate_request

@app.route("/payments/wise/webhooks")
def handle_wise_webhook():
    try:
        validate_request(request)
    except Exception as e:
        logger.error(f"Wise webhook request validation failed: {e}")
        abort(400)

    ...
```

## Run tests

```bash
# Within the pywisetransfer working directory
pip install .[dev]
pytest
```
