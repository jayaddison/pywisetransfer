import logging

logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True

print(
    f"""Getting started:

> client = pywisetransfer.Client(api_key)
> client.profiles.list()
> client.borderless_accounts.list(profile_id)"""
)

import pywisetransfer  # noqa: E402,F401
