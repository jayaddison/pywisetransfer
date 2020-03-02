from apiron import JsonEndpoint

from pytransferwise.base import Base


class BorderlessAccount(Base):
    account_list = JsonEndpoint(
        path="/v1/borderless-accounts", required_params=["profileId"]
    )
    statement = JsonEndpoint(
        path="/v3/profiles/{profileId}/borderless-accounts/{borderlessAccountId}/statement.json",
        required_params=["currency", "intervalStart", "intervalEnd"],
    )
