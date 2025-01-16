from typing import Any

from munch import munchify

from wise_banking_api_client import Client
from wise_banking_api_client.base import Base
from wise_banking_api_client.endpoint import JsonEndpointWithSCA


class BalanceStatementsService(Base):
    statement = JsonEndpointWithSCA(
        path="/v1/profiles/{profile_id}/balance-statements/{balance_id}/statement.json",
        required_params=["currency", "intervalStart", "intervalEnd"],
    )


class BalanceStatements:
    def __init__(self, client: Client):
        self.service = BalanceStatementsService(client=client)

    def statement(
        self,
        profile_id: str,
        balance_id: str,
        currency: str,
        interval_start: str,
        interval_end: str,
        type: str = "COMPACT",
    ) -> Any:
        valid_types = ["COMPACT", "FLAT"]
        if type not in valid_types:
            raise ValueError(f"Invalid type '{type}'; value values are: {valid_types}")

        return munchify(
            self.service.statement(
                profile_id=profile_id,
                balance_id=balance_id,
                params={
                    "currency": currency,
                    "intervalStart": interval_start,
                    "intervalEnd": interval_end,
                    "type": type,
                },
            )
        )
