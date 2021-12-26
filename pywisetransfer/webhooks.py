from base64 import b64decode

from pywisetransfer.keys import (
    WEBHOOK_SIGNATURE_PUBLIC_KEY_LIVE,
    WEBHOOK_SIGNATURE_PUBLIC_KEY_SANDBOX,
)

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding, utils
from cryptography.hazmat.primitives.serialization import load_pem_public_key


def verify_signature(payload, signature, environment="sandbox"):
    signature = b64decode(signature)
    key_data = (
        WEBHOOK_SIGNATURE_PUBLIC_KEY_LIVE
        if environment == "live"
        else WEBHOOK_SIGNATURE_PUBLIC_KEY_SANDBOX
    )
    public_key = load_pem_public_key(key_data, backend=default_backend())
    try:
        public_key.verify(signature, payload, padding.PKCS1v15(), hashes.SHA1())
        return True
    except InvalidSignature:
        return False
