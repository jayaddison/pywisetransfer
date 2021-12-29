from base64 import b64encode
from typing import Dict, Optional

import apiron
from apiron.endpoint import JsonEndpoint
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from functools import partial, update_wrapper, wraps
from requests.exceptions import HTTPError


class JsonEndpointWithSCA(JsonEndpoint):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sca_headers = {}

    # apiron's required_headers should be called override_headers
    @property
    def required_headers(self) -> Dict[str, str]:
        # It looks like 2FA only needs to be performed every few minutes,
        # but there seems to be no harm in re-sending the signature.
        return {**super().required_headers, **self.sca_headers}

    def __get__(self, instance: Optional[JsonEndpoint], owner: JsonEndpoint):
        caller = partial(apiron.client.call, owner, self)
        update_wrapper(caller, apiron.client.call)

        @wraps(apiron.client.call)
        def perform_2fa_if_needed(*args, **kwargs):
            try:
                return caller(*args, **kwargs)
            except HTTPError as e:
                resp = e.response
                if (
                    resp.status_code == 403
                    and resp.headers["X-2FA-Approval-Result"] == "REJECTED"
                ):
                    challenge = resp.headers["X-2FA-Approval"]
                    if owner.client.private_key is None:
                        raise Exception(
                            f"Please provide pytransferwise.private_key_file or private_key to perform SCA authentication"
                        ) from e
                    signature = owner.client.private_key.sign(
                        challenge.encode("ascii"), padding.PKCS1v15(), hashes.SHA256()
                    )
                    self.sca_headers["X-Signature"] = b64encode(signature).decode(
                        "ascii"
                    )
                    self.sca_headers["X-2FA-Approval"] = challenge
                    return caller(*args, **kwargs)
                raise

        return perform_2fa_if_needed
