# pywisetransfer

An unofficial, experimental Python client library for the [TransferWise API](https://api-docs.transferwise.com).

:warning: The classes, functions and interfaces that this library provides are very much in-development and prone to change.

## Installation

```bash
# Within your project directory
pip install pywisetransfer
```
After installation, you should be able to import the package.

```python
import pywisetransfer
```

## Usage

Wise provides [two APIs](https://docs.wise.com/api-docs/api-reference#environments): `live` and `sandbox`.
You can use either of these environments with this library.

### API Key

In order to use the API, you need to obtain an API key.
This key looks like this: `12345678-1234-1234-1234-123456789abcde`

To use the sandbox API, log into [sandbox.transferwise.tech].
Then, go to Settings 🠚 Developer Tools 🠚 API-Tokens.
Create and copy a new API key.

To use your own account, log into [wise.com](https://wise.com).
Then click on your account at the top right 🠚 Integrations and Tools 🠚 Developer Tools 🠚 API Tokens and add a new token.

[sandbox.transferwise.tech]: https://sandbox.transferwise.tech

### API Requests

The API requests are made using the [requests](https://requests.readthedocs.io/en/latest/) library.
First of all, you create a `Client` object:

- Create a `Client` object with your API key for the `live` environment:

    ```python
    client = pywisetransfer.Client(api_key="your-api-key-here", environment="live")
    ```

- Create a `Client` object with your API key for the `sandbox` environment:

    ```python
    client = pywisetransfer.Client(api_key="your-api-key-here")
    ```

- Create a `Client` object which interacts with the recorded API which is used for the tests:

    ```python
    from pywisetransfer.test import TestClient
    client = pywisetransfer.TestClient()
    ```

    After this, all calls to the real Wise API are blocked by the `responses` library.
    To stop using the recorded API:

    ```python
    client.stop()
    ```

## Examples

This section provides a few examples of how to use this package.

### Profiles

This library follows the **[Wise API Reference]**.
So, if you find e.g. profile here, you can look up all the values of it in the [Wise API Reference].

If you create a sandbox account, you should have two profiles: `business` and `personal`.

```python
>>> for profile in client.profiles.list():
...     print(f"id: {profile.id}")
...     print(f"type: {profile.type}")
...     if profile.type == "personal":
...         print(f"name: {profile.details.firstName} {profile.details.lastName}")
...     else:
...         print(f"name: {profile.details.name}")
...     print()
... 
id: 28577318
type: personal
name: Teresa Adams

id: 28577319
type: business
name: Law and Daughters 6423
```

### Receive Money

One profile can have several accounts in different currencies.
This shows which currencies are accepted and how to receive money.

```python
>>> for profile in client.profiles.list():
...     accounts = client.account_details.list(profile_id=profile.id)
...     print(f"\ntype: {profile.type}")
...     for account in accounts:
...         print(
...             f"    currency: {account.currency.code}"
...             f" receive with: {', '.join(feature.title for feature in account.bankFeatures if feature.supported)}")
... 

type: personal
    currency: EUR receive with: Receive locally, Receive internationally (Swift), Set up Direct Debits, Receive from PayPal and Stripe
    currency: GBP receive with: Receive locally, Receive internationally (Swift), Set up Direct Debits, Receive from PayPal and Stripe
    currency: USD receive with: Receive locally, Receive internationally (Swift), Set up Direct Debits, Receive from PayPal and Stripe
    currency: AUD receive with: Receive locally, Set up Direct Debits
    currency: NZD receive with: Receive locally
    currency: CAD receive with: Receive locally, Set up Direct Debits
    currency: HUF receive with: Receive locally
    currency: MYR receive with: 
    currency: RON receive with: Receive locally
    currency: SGD receive with: Receive locally
    currency: TRY receive with: Receive locally

type: business
    currency: EUR receive with: Receive locally, Receive internationally (Swift), Set up Direct Debits, Receive from PayPal and Stripe
    currency: GBP receive with: Receive locally, Receive internationally (Swift), Set up Direct Debits, Receive from PayPal and Stripe
    currency: USD receive with: Receive locally, Receive internationally (Swift), Set up Direct Debits, Receive from PayPal and Stripe
    currency: AUD receive with: Receive locally, Set up Direct Debits
    currency: NZD receive with: Receive locally
    currency: CAD receive with: Receive locally, Set up Direct Debits
    currency: HUF receive with: Receive locally
    currency: MYR receive with: 
    currency: RON receive with: Receive locally
    currency: SGD receive with: Receive locally
    currency: TRY receive with: Receive locally

```

[Wise API Reference]: https://docs.wise.com/api-docs/api-reference

### Balance

This code retrieves the balance for each currency in each account.

```python
>>> for profile in client.profiles.list():
...     print(f"type: {profile.type} {', '.join(f'{balance.totalWorth.value}{balance.totalWorth.currency}' for balance in client.balances.list(profile_id=profile.id))}")
... 
type: personal 1000000.0GBP, 1000000.0EUR, 1000000.0USD, 1000000.0AUD
type: business 1000000.0GBP, 1000000.0EUR, 1000000.0USD, 1000000.0AUD

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

### Request an Example Quote

You can request quote examples as stated in [Create an un-authenticated quote](https://docs.wise.com/api-docs/api-reference/quote#create-not-authenticated).

In this example, we want to transfer `GBP` to `USD` and make sure we have `110USD` in the end.

```python
from pywisetransfer import *
from pywisetransfer.test import *
client = TestClient()
qr = QuoteRequest(
    sourceCurrency="GBP",
    targetCurrency="USD",
    sourceAmount=None,
    targetAmount=110,
)
example_quotes = client.quotes.example(qr)
```

## Run tests

```bash
# Within the pywisetransfer working directory
pip install .[dev]
pytest
```
