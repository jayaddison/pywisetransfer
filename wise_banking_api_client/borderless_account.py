from typing import Any

from apiron import JsonEndpoint
from munch import munchify

from wise_banking_api_client import Client
from wise_banking_api_client.base import Base
from wise_banking_api_client.deprecation import deprecated
from wise_banking_api_client.endpoint import JsonEndpointWithSCA


class BorderlessAccountService(Base):
    list = JsonEndpoint(path="/v1/borderless-accounts", required_params=["profileId"])
    statement = JsonEndpointWithSCA(
        path="/v3/profiles/{profile_id}/borderless-accounts/{account_id}/statement.json",
        required_params=["currency", "intervalStart", "intervalEnd"],
    )


class BorderlessAccount:
    def __init__(self, client: Client):
        self.service = BorderlessAccountService(client=client)

    @deprecated(
        message="The borderless-accounts endpoint is deprecated; please use account-details instead"
    )
    def list(self, profile_id: str) -> list[Any]:
        accounts: list[Any] = self.service.list(params={"profileId": profile_id})
        return munchify(accounts)

    @deprecated(
        message="The borderless-accounts statement endpoint is deprecated; please use balance-statements instead"
    )
    def statement(
        self,
        profile_id: str,
        account_id: str,
        currency: str,
        interval_start: str,
        interval_end: str,
    ) -> Any:
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
