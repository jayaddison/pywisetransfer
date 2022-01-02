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

    def __init__(self, api_key, environment="sandbox"):
        if api_key is None:
            raise KeyError("You must provide a value for pywisetransfer.api_key")

        if environment not in ("sandbox", "live"):
            raise KeyError("pywisetransfer.environment must be 'sandbox' or 'live'")

        self.api_key = api_key
        self.environment = environment
        self.add_resources()
