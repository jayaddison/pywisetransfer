from __future__ import annotations


class Client:
    def add_resources(self) -> None:
        from pywisetransfer.account_details import AccountDetails
        from pywisetransfer.balance_statements import BalanceStatements
        from pywisetransfer.balances import Balances
        from pywisetransfer.borderless_account import BorderlessAccount
        from pywisetransfer.currency import Currency
        from pywisetransfer.multi_currency_account import MultiCurrencyAccount
        from pywisetransfer.profile import Profile
        from pywisetransfer.subscription import Subscription
        from pywisetransfer.transfer import Transfer
        from pywisetransfer.user import User
        

        self.account_details = AccountDetails(client=self)
        self.balance_statements = BalanceStatements(client=self)
        self.balances = Balances(client=self)
        self.borderless_accounts = BorderlessAccount(client=self)
        self.currencies = Currency(client=self)
        self.multi_currency_account = MultiCurrencyAccount(client=self)
        self.profiles = Profile(client=self)
        self.subscriptions = Subscription(client=self)
        self.transfers = Transfer(client=self)
        self.users = User(client=self)

    def __init__(
        self,
        api_key: str,
        environment: str = "sandbox",
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
