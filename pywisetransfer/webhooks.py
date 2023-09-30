from base64 import b64decode

from pywisetransfer.exceptions import (
    InvalidWebhookHeader,
    InvalidWebhookRequest,
    InvalidWebhookSignature,
)
from pywisetransfer.keys import get_webhook_public_key

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.serialization import load_pem_public_key


def validate_request(request: "flask.Request", environment: str = "sandbox") -> None:
    if request.json is None:
        raise InvalidWebhookRequest("JSON content not found")

    if "X-Signature-SHA256" not in request.headers:
        raise InvalidWebhookRequest("X-Signature-SHA256 header not found")

    try:
        signature = b64decode(request.headers["X-Signature-SHA256"])
    except Exception:
        raise InvalidWebhookHeader("Failed to decode signature")

    if not verify_signature(
        payload=request.data,
        signature=signature,
        environment=environment,
    ):
        raise InvalidWebhookSignature("Failed to verify signature")


def verify_signature(payload: bytes, signature: bytes, environment: str = "sandbox") -> None:
    key_data = get_webhook_public_key(environment)
    public_key = load_pem_public_key(key_data, backend=default_backend())
    try:
        public_key.verify(signature, payload, padding.PKCS1v15(), hashes.SHA256())
        return True
    except InvalidSignature:
        return False
