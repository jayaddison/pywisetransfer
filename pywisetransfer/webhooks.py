from cryptography.exceptions import InvalidSignature

from .exceptions import InvalidWebhookHeader, InvalidWebhookRequest, InvalidWebhookSignature
from .keys import get_webhook_public_key
from .signing import validate_sha1_signature, validate_sha256_signature


def verify_signature(payload: bytes, signature: str, environment: str ="sandbox") -> bool:
    try:
        validate_sha1_signature(signature, payload, get_webhook_public_key(environment))
        return True
    except InvalidSignature:
        return False


def validate_request(request: "requests.Request", environment: str = "sandbox") -> None:
    if request.json is None:
        raise InvalidWebhookRequest("Webhook request does not contain JSON")

    try:
        signature = request.headers["X-Signature-SHA256"]
    except KeyError:
        raise InvalidWebhookRequest("Webhook request does not include SHA-256 signature")

    try:
        b64decode(signature)
    except Exception as e:
        raise InvalidWebhookHeader("Cannot decode webhook signature") from e

    try:
        validate_sha256_signature(signature, payload, get_webhook_public_key(environment))
    except InvalidSignature as e:
        raise InvalidWebhookSignature("Invalid webhook signature") from e
