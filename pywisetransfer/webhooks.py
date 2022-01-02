from cryptography.exceptions import InvalidSignature

from .exceptions import InvalidWebhookHeader, InvalidWebhookRequest, InvalidWebhookSignature
from .keys import get_key_data
from .signing import validate_sha1_signature, validate_sha256_signature


def verify_signature(payload, signature, environment="sandbox"):
    try:
        validate_sha1_signature(signature, payload, get_key_data(environment))
        return True
    except InvalidSignature:
        return False


def validate_request(request, environment="sandbox"):
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
        validate_sha256_signature(signature, payload, get_key_data(environment))
    except InvalidSignature as e:
        raise InvalidWebhookSignature("Invalid webhook signature") from e
