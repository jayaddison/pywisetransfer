from base64 import b64decode, b64encode

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.serialization import (
    load_pem_private_key,
    load_pem_public_key,
)


def sign_sca_challenge(challenge, private_key_data):
    private_key = load_pem_private_key(private_key_data, None)
    signature = private_key.sign(
        challenge.encode("ascii"), padding.PKCS1v15(), hashes.SHA256()
    )
    return b64encode(signature).decode("ascii")


def validate_sha1_signature(signature, payload, key_data):
    public_key = load_pem_public_key(key_data)
    public_key.verify(b64decode(signature), payload, padding.PKCS1v15(), hashes.SHA1())


def validate_sha256_signature(signature, payload, key_data):
    public_key = load_pem_public_key(key_data)
    public_key.verify(
        b64decode(signature), payload, padding.PKCS1v15(), hashes.SHA256()
    )
