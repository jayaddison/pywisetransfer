from cryptography.hazmat.primitives.serialization import load_pem_private_key


class Client(object):
    def add_resources(self):
        from pywisetransfer.borderless_account import BorderlessAccount
        from pywisetransfer.profile import Profile
        from pywisetransfer.subscription import Subscription
        from pywisetransfer.user import User

        self.borderless_accounts = BorderlessAccount(client=self)
        self.profiles = Profile(client=self)
        self.subscriptions = Subscription(client=self)
        self.users = User(client=self)

    def __init__(
        self, api_key, environment="sandbox", private_key_file=None, private_key=None
    ):
        if api_key is None:
            raise KeyError("You must provide a value for pywisetransfer.api_key")

        if environment not in ("sandbox", "live"):
            raise KeyError("pywisetransfer.environment must be 'sandbox' or 'live'")

        if private_key_file is not None:
            if private_key is not None:
                raise ValueError(
                    "Please provide only one of pywisetransfer.private_key_file or private_key"
                )
            key_file = open(private_key_file, "rb")
            private_key = load_pem_private_key(key_file.read(), None)

        self.api_key = api_key
        self.environment = environment
        self.private_key_file = private_key_file
        self.private_key = private_key
        self.add_resources()
