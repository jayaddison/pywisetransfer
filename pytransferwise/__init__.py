api_key = None
environment = "sandbox"


class Client(object):
    def add_resources(self):
        from pytransferwise.borderless_account import BorderlessAccount
        from pytransferwise.profile import Profile
        from pytransferwise.subscription import Subscription
        from pytransferwise.user import User
        from pytransferwise.rates import Rates

        self.borderless_accounts = BorderlessAccount()
        self.profiles = Profile()
        self.subscriptions = Subscription()
        self.users = User()
        self.rates = Rates()

    def __init__(self):
        if api_key is None:
            raise KeyError("You must provide a value for pytransferwise.api_key")

        if environment not in ("sandbox", "live"):
            raise KeyError("pytransferwise.environment must be 'sandbox' or 'live'")

        self.add_resources()
