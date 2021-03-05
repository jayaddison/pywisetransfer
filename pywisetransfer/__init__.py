api_key = None
environment = "sandbox"


class Client(object):
    def add_resources(self):
        from pywisetransfer.borderless_account import BorderlessAccount
        from pywisetransfer.profile import Profile
        from pywisetransfer.subscription import Subscription
        from pywisetransfer.user import User

        self.borderless_accounts = BorderlessAccount()
        self.profiles = Profile()
        self.subscriptions = Subscription()
        self.users = User()

    def __init__(self):
        if api_key is None:
            raise KeyError("You must provide a value for pywisetransfer.api_key")

        if environment not in ("sandbox", "live"):
            raise KeyError("pywisetransfer.environment must be 'sandbox' or 'live'")

        self.add_resources()
