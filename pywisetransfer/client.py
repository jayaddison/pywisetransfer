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
from typing import Optional

from pywisetransfer.model.enum import StrEnum

HERE = Path(__file__).parent
DEFAULT_PRIVATE_KEY = HERE / "test" / "private.pem"
DEFAULT_PUBLIC_KEY = HERE / "test" / "public.pem"


def generate_key_pair(
    *,
    private_key: Path | str = "wise.com.private.pem",
    public_key: Optional[Path | str] = "wise.com.public.pem",
):
    """Generate a key public and private key pair.

    This uses openssl to generate the key pair.
    The key pair is stored in the specified location.

    You can then upload the public key to your business account.
    https://sandbox.transferwise.tech/settings/public-keys

    Args:
        private_key: The name of the private key.
            If the file exists, it will not be deleted or overwritten.
        public_key_name: The name of the public key.
            If this is None, the key will not be generated.
    """
    import subprocess

    private_path = Path(private_key)
    if not private_path.exists():
        subprocess.check_call(["openssl", "genrsa", "-out", private_path, "2048"])
    if public_key is not None:
        public_path = Path(public_key)
        subprocess.check_call(
            ["openssl", "rsa", "-pubout", "-in", private_path, "-out", public_path]
        )


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

    Generate the key, either by command line below or using generate_key_pair().

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
        if private_key_data == DEFAULT_PRIVATE_KEY.read_bytes() and environment == "live":
            raise ValueError(
                "Do not use the private key provided for this package on the live environment. "
                "Read on how to create your own: "
                "https://docs.wise.com/api-docs/features/strong-customer-authentication-2fa/personal-token-sca"
            )

        self.api_key = api_key
        self.environment = environment
        self.private_key_file = private_key_file
        self.private_key_data = private_key_data
        self.add_resources()

    def can_read(self) -> bool:
        """Wether or not we can read the API.
        
        We request information on us.
        """
        from pywisetransfer.endpoint import WiseAPIError
        try:
            self.users.me()
        except WiseAPIError:
            return False
        return True

    def can_write(self) -> bool:
        """Wether or not we can write to the API.
        
        We try to create a quote.
        """
        from pywisetransfer.quote import QuoteRequest
        from pywisetransfer.endpoint import WiseAPIError
        try:
            self.quotes.create(
                QuoteRequest(
                    sourceCurrency="EUR",
                    targetCurrency="USD",
                    sourceAmount=100,
                ),
                self.profiles.list()[0]
            )
        except WiseAPIError:
            return False
        return True

    def can_sca(self) -> bool:
        """Wether we can authenticate with SCA.
        
        We try to fund a non-existing transfer.
        """
        from pywisetransfer.endpoint import WiseAPIError
        try:
            if not self.profiles.business:
                return False
            self.transfers.fund(0, self.profiles.business[0])
        except WiseAPIError as e:
            if e.json.status == 401:
                # We are not authorized, the transfer id was not checked.
                return False
        return True
    
__all__ = ["Client", "DEFAULT_PRIVATE_KEY", "DEFAULT_PUBLIC_KEY", "Environment"]
