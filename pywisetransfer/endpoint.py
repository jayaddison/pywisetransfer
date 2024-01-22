from typing import Any, Callable, Optional

import apiron
from apiron.endpoint import JsonEndpoint
from functools import partial, update_wrapper, wraps
from requests.exceptions import HTTPError

from pywisetransfer.base import Base
from pywisetransfer.signing import sign_sca_challenge


class JsonEndpointWithSCA(JsonEndpoint):
    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(*args, **kwargs)
        self.sca_headers: dict[str, str] = {}

    # apiron's required_headers should be called override_headers
    @property
    def required_headers(self) -> dict[str, str]:
        # It looks like 2FA only needs to be performed every few minutes,
        # but there seems to be no harm in re-sending the signature.
        return {**super().required_headers, **self.sca_headers}

    def __get__(self, instance: Optional[Base], owner: type[Base]) -> Callable[..., Any]:
        caller = partial(apiron.client.call, owner, self)
        update_wrapper(caller, apiron.client.call)

        @wraps(apiron.client.call)
        def perform_2fa_if_needed(*args: Any, **kwargs: Any) -> Any:
            try:
                return caller(*args, **kwargs)
            except HTTPError as e:
                resp = e.response
                if (
                    resp.status_code == 403
                    and resp.headers["X-2FA-Approval-Result"] == "REJECTED"
                ):
                    challenge = resp.headers["X-2FA-Approval"]
                    if owner.client.private_key_data is None:  # type: ignore[union-attr]
                        raise Exception(
                            "Please provide pytransferwise.private_key_file or private_key_data to perform SCA authentication"
                        ) from e

                    self.sca_headers["X-Signature"] = sign_sca_challenge(
                        challenge, owner.client.private_key_data  # type: ignore[union-attr]
                    )
                    self.sca_headers["X-2FA-Approval"] = challenge
                    return caller(*args, **kwargs)
                raise

        return perform_2fa_if_needed
