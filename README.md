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
client.borderless_accounts.account_list(params={'profileId': '9129'})
```

## Run tests

```bash
# Within the pytransferwise working directory
poetry install
poetry run pytest --forked
```
