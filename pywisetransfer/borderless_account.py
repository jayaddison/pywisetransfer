from apiron import JsonEndpoint
from munch import munchify

from pywisetransfer.base import Base
from pywisetransfer.endpoint import JsonEndpointWithSCA


class BorderlessAccountService(Base):
    list = JsonEndpoint(path="/v1/borderless-accounts", required_params=["profileId"])
    statement = JsonEndpointWithSCA(
        path="/v3/profiles/{profile_id}/borderless-accounts/{account_id}/statement.json",
        required_params=["currency", "intervalStart", "intervalEnd"],
    )


class BorderlessAccount(object):
    def __init__(self, client):
        self.service = BorderlessAccountService(client=client)

    def list(self, profile_id):
        return munchify(self.service.list(params={"profileId": profile_id}))

    def statement(self, profile_id, account_id, currency, interval_start, interval_end):
        return munchify(
            self.service.statement(
                profile_id=profile_id,
                account_id=account_id,
                params={
                    "currency": currency,
                    "intervalStart": interval_start,
                    "intervalEnd": interval_end,
                },
            )
        )
