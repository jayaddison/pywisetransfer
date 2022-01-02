from base64 import b64encode

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.serialization import load_pem_private_key


def sign_sca_challenge(challenge, private_key_data):
    private_key = load_pem_private_key(private_key_data, None)
    signature = private_key.sign(
        challenge.encode("ascii"), padding.PKCS1v15(), hashes.SHA256()
    )
    return b64encode(signature).decode("ascii")
