"""The client to access the Wise API.

Attributes:
    DEFAULT_PRIVATE_KEY: The default private key to use for SCA protected endpoints.
    DEFAULT_PUBLIC_KEY: The default public key to use for SCA protected endpoints.

If you wish to give the whole world access to a test account on the Wise Sandbox API,
you can upload the contents of the DEFAULT_PUBLIC_KEY to your account.

>>> from pywisetransfer import DEFAULT_PUBLIC_KEY
>>> print(DEFAULT_PUBLIC_KEY.read_text())
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAyMyEEbVf3dyP57TdjXOg
2HNpjq74qEoWTewFtQMeaUYuO41jSq3SC69g7Mf6OHMC0wqNY2Eso0q1bXHf6Eym
yR5qFJjzVHFcWmjivJ9jDd+8NzJm+ZsEe18HycCepNvcjSQefgqmMl/A6r83o5Q+
R4rCqemAQLZNTmj+WaZK4m+0tFwTnT6K1Hp2t3pkcpUUG3yJNOB5w3FUY8LQtv8I
m+WePMqkYYT6sn7uGpikvC8SEje0R8IGc2SItvhkRZ1CULGm8weEY68aGjkRb7LE
OJ+iEyzI7IuA2SA64+xhGfg+EEBp569zeYNuuwm9Uqx9O5hExuqgi7ENyHbVOJ4K
VwIDAQAB
-----END PUBLIC KEY-----

Read more on SCA protection here:
https://docs.wise.com/api-docs/features/strong-customer-authentication-2fa/personal-token-sca

Upload the public key to your business account:
https://sandbox.transferwise.tech/settings/public-keys

"""
from pathlib import Path

from pywisetransfer.model.enum import StrEnum

HERE = Path(__file__).parent
DEFAULT_PRIVATE_KEY = HERE / "test" / "private.pem"
DEFAULT_PUBLIC_KEY = HERE / "test" / "public.pem"


class Environment(StrEnum):
    """The different environments that we can access.
    
    Attributes:
        sandbox: The sandbox environment.
        live: The live environment.
    """
    
    sandbox = "sandbox"
    live = "live"


class Client:
    """The client class to access the Wise API.
    
    In order to use the API you need to provide an API key.
    Please have a look in the project documentation for more information.
    
    In order to use SCA protected endpoints, you need to generate a key.
    See https://docs.wise.com/api-docs/features/strong-customer-authentication-2fa/personal-token-sca
    
    Generate the key:
    
        openssl genrsa -out wise.pem 2048
        
    Get the public key:
    
        openssl rsa -pubout -in wise.pem -out wise.pub
    
    Then, upload the public key to your account.
    
    """

    def add_resources(self) -> None:
        from pywisetransfer.account_details import AccountDetails
        from pywisetransfer.balance_statements import BalanceStatements
        from pywisetransfer.balances import Balances
        from pywisetransfer.borderless_account import BorderlessAccount
        from pywisetransfer.currency import Currency
        from pywisetransfer.multi_currency_account import MultiCurrencyAccount
        from pywisetransfer.profile import Profile
        from pywisetransfer.quote import Quote
        from pywisetransfer.recipient_account import RecipientAccount
        from pywisetransfer.subscription import Subscription
        from pywisetransfer.transfer import Transfer
        from pywisetransfer.user import User
        from pywisetransfer.sandbox_simulation import TransferSimulation

        self.account_details = AccountDetails(client=self)
        self.balance_statements = BalanceStatements(client=self)
        self.balances = Balances(client=self)
        self.borderless_accounts = BorderlessAccount(client=self)
        self.currencies = Currency(client=self)
        self.multi_currency_account = MultiCurrencyAccount(client=self)
        self.profiles = Profile(client=self)
        self.quotes = Quote(client=self)
        self.recipient_accounts = RecipientAccount(client=self)
        self.simulate_transfer = TransferSimulation(client=self)
        self.subscriptions = Subscription(client=self)
        self.transfers = Transfer(client=self)
        self.users = User(client=self)

    def __init__(
        self,
        api_key: str,
        environment: Environment = Environment.sandbox,
        private_key_file: str | None = None,
        private_key_data: bytes | None = None,
    ):
        if api_key is None:
            raise KeyError("You must provide a value for pywisetransfer.api_key")

        if environment not in ("sandbox", "live"):
            raise KeyError("pywisetransfer.environment must be 'sandbox' or 'live'")

        if private_key_file is not None:
            if private_key_data is not None:
                raise ValueError(
                    "Please provide only one of pywisetransfer.private_key_file or private_key_data"
                )
            with open(private_key_file, "rb") as f:
                private_key_data = f.read()

        self.api_key = api_key
        self.environment = environment
        self.private_key_file = private_key_file
        self.private_key_data = private_key_data
        self.add_resources()


__all__ = ["Client", "DEFAULT_PRIVATE_KEY", "DEFAULT_PUBLIC_KEY", "Environment"]
