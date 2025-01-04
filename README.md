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
>>> from pywisetransfer import Client

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
    >>> client = Client(api_key="your-api-key-here", environment="live")

    ```

- Create a `Client` object with your API key for the `sandbox` environment:

    ```python
    >>> client = Client(api_key="your-api-key-here")

    ```

- Create a `Client` object which interacts with the recorded API which is used for the tests:

    ```python
    >>> from pywisetransfer.test import TestClient
    >>> client = TestClient()

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
...     print(f"name: {profile.details.name}")
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
...     print(f"type: {profile.type}")
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
>>> profiles = client.profiles.list()
>>> for profile in profiles:
...     print(f"type: {profile.type} {', '.join(f'{balance.totalWorth.value}{balance.totalWorth.currency}' for balance in client.balances.list(profile=profile))}")
... 
type: personal 1000000.0GBP, 1000000.0EUR, 1000000.0USD, 1000000.0AUD
type: business 1000000.0GBP, 1000000.0EUR, 1000000.0USD, 1000000.0AUD

```

### Currencies

Wise supports many [currencies](https://docs.wise.com/api-docs/api-reference/currencies).

```python
>>> currencies = client.currencies.list()
>>> AED = currencies[0]
>>> AED.code
'AED'
>>> AED.name
'United Arab Emirates dirham'
>>> AED.symbol
'د.إ'

```

Above are the up-to-date currencies.
You can also use those in the package.

```python
>>> from pywisetransfer import Currency
>>> Currency.AED.code
'AED'
>>> Currency.AED.name
'United Arab Emirates dirham'
>>> Currency.AED.symbol
'د.إ'

```

### Recipient Account Requirements

In this example, we get the requirements for a recipient account that should receive 100 GBP from us.

```python
>>> requirements = client.recipient_accounts.get_requirements_for_currency(source=Currency.GBP, target=Currency.GBP, source_amount=100)
>>> list(sorted([requirement.type for requirement in requirements]))
['email', 'iban', 'sort_code']

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
The example quote requires less information than a real quote.

```python
>>> from pywisetransfer import ExampleQuoteRequest
>>> quote_request = ExampleQuoteRequest(
...     sourceCurrency="GBP",
...     targetCurrency="USD",
...     sourceAmount=None,
...     targetAmount=110,
... )
>>> example_quote = client.quotes.example(quote_request)
>>> example_quote.rate
1.25155
>>> example_quote.rateExpirationTime
datetime.datetime(2024, 12, 31, 19, 21, 44, tzinfo=datetime.timezone.utc)
>>> example_quote.profile == None  # Example quotes are not bound to a profile
True
>>> example_quote.rateType
'FIXED'

```

### Create a Recipient of a Transfer

### Request a Quote

To create a transfer, you first need a quote.
You can read on how to create [Create an authenticated quote](https://docs.wise.com/api-docs/api-reference/quote#create-authenticated).

In this example, we create a quote for the personal account. This is the same quote as the one above.
We also provide pay-out and pay-in information.
The `targetAccount` is None because we don't know the recipient yet.

```python
>>> from pywisetransfer import QuoteRequest, PaymentMethod
>>> quote_request = QuoteRequest(
...        sourceCurrency="GBP",
...        targetCurrency="USD",
...        sourceAmount=None,
...        targetAmount=110,
...        targetAccount=None,
...        payOut=PaymentMethod.BANK_TRANSFER,
...        preferredPayIn=PaymentMethod.BANK_TRANSFER,
...    )
>>> quote = client.quotes.create(quote_request, profile=profiles.personal[0])
>>> quote.user
12970746
>>> quote.status
'PENDING'
>>> quote.sourceCurrency
'GBP'
>>> quote.targetCurrency 
'USD'
>>> quote.sourceAmount is None  # the source amount depends on the payment option
True
>>> quote.targetAmount
110.0
>>> quote.rate
1.24232
>>> quote.rateType
'FIXED'
>>> quote.payOut
'BANK_TRANSFER'
>>> len(quote.paymentOptions)  # we have many payment options
20

```

### Get Recipient Requirements

The quote above lacks the recipient information.
The reason is that there are requirements to the recipient account that
depend on the quote.
We can get these requirements using `get_requirements_for_quote`.

```python
>>> requirements = client.recipient_accounts.get_requirements_for_quote(quote.id)
>>> [requirement.type for requirement in requirements]
['aba', 'fedwire_local', 'swift_code', 'email']

```

In the example above, we see different requirements for transferring money to a bank account
in the USA. We can use `aba`, `fedwire_local`, `swift_code` and `email`.

If we look at the first requirement, we see that we require 10 fields.

```python
>>> ach = requirements[0]
>>> ach.title
'ACH'
>>> len(requirements[0].fields)
10
>>> ach.fields[0].name
'Recipient type'
>>> ach.fields[0].group[0].required
True
>>> ach.fields[0].group[0].type  # the fields are grouped and this is a select with values
'select'
>>> [v.key for v in ach.fields[0].group[0].valuesAllowed]  # the JSON value for the details
['PRIVATE', 'BUSINESS']
>>> [v.name for v in ach.fields[0].group[0].valuesAllowed]  # what to show to the user
['Person', 'Business']

```

### Create an Email Recipient

> Wise: Please contact us before attempting to use email recipients. We do not recommend using this feature except for certain uses cases.

Because `email` is` in the requirements, we can create an email recipient for the quote.

```pyton
>>> email = requirements[-1]
>>> len(email.required_fields)
2
>>> email.required_fields[0].group[0].key
'email'
>>> email.required_fields[0].group[0].name
'Email (Optional)'
>>> email.required_fields[1].group[0].key
'accountHolderName'
>>> email.required_fields[1].group[0].name
'Full name of the account holder'

```

Below, we create the recipient and get a response.
The response includes all the data that we sent and optional fields.

```python
>>> from pywisetransfer import Recipient, RecipientDetails, CurrencyCode, RequirementType
>>> email_recipient = Recipient(
...     currency=CurrencyCode.EUR,
...     type=RequirementType.email,
...     profile=profiles.personal[0].id,
...     accountHolderName="John Doe",
...     ownedByCustomer=False,
...     details=RecipientDetails(email="john@doe.com")
... )
>>> created_response = client.recipient_accounts.create_recipient(email_recipient)
>>> created_response.id  # the response has an id
700614969

```

In the following, we get the actual recipient account as the user sees it e.g. in the app.

```python
>>> recipient = client.recipient_accounts.get(created_response)
>>> recipient.id
700614969
>>> recipient.accountSummary
'john@doe.com'
>>> recipient.currency
'EUR'
>>> recipient.email
'john@doe.com'
>>> recipient.legalEntityType
'PERSON'
>>> recipient.ownedByCustomer
False

```


## Run tests

```bash
# Within the pywisetransfer working directory
pip install .[dev]
pytest
```
