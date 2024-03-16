from __future__ import annotations

from typing import Any

from apiron import Service

from pywisetransfer import Client


class Base(Service):

    client: Client | None = None

    def __init__(self, *args: Any, **kwargs: Any):
        # TODO: It would be nice to make 'client' a required argument here
        # Currently apiron performs a zero-argument constructor call to the
        # service base class to retrieve the 'required_headers' property,
        # so we cater for empty arguments here
        # https://github.com/ithaka/apiron/blob/v5.1.0/src/apiron/service/base.py#L7
        if "client" in kwargs and Base.client != kwargs["client"]:
            Base.client = kwargs["client"]
        if Base.client and Base.client.environment == "live":
            Base.domain = "https://api.transferwise.com"
        else:
            Base.domain = "https://api.sandbox.transferwise.tech"

    @property
    def required_headers(self) -> dict[str, str]:  # type: ignore[override]
        if self.client:
            return {"Authorization": f"Bearer {self.client.api_key}"}
        return {}
