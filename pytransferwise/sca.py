import os
import base64
import rsa
import googleapi.cloud_storage_api as gcsapi

# TODO: implement storing/loading private key from more secret place like Google KMS
def download_key_file():
    cloud_storage_tw_key_dir = os.environ['TW_KEY_DIR']
    _key_fname = os.environ['TW_KEY_NAME'] + '.pem'

    # export_dir = './tmp/' # Only windows env debug
    export_dir = os.environ['TW_KEY_EXPORT_DIR']

    _key_path = export_dir + _key_fname

    gcsapi.download_blob(cloud_storage_tw_key_dir + _key_fname, _key_path)
    # print(f'{_key_fname} has been downloaded to {_key_path}')
    return _key_path

private_key_path = download_key_file()
# private_key_path = './e_tw_sca_rsa_private.pem' # Only debug option

if os.path.exists(private_key_path) is False:
    print(f'Private key file not found in {private_key_path}, please check ENV configuration')

# Read the private key file as bytes.
with open(private_key_path, 'rb') as f:
    private_key_data = f.read()

private_key = rsa.PrivateKey.load_pkcs1(private_key_data, 'PEM')


def add_sca_headers(service, one_time_token):
    signature = do_sca_challenge(one_time_token)
    sca_headers = {
        'x-2fa-approval': one_time_token,
        'X-Signature': signature
    }
    service.required_headers.update(sca_headers)
    return service


def do_sca_challenge(one_time_token):
    print('doing sca challenge')

    # Use the private key to sign the one-time-token that was returned
    # in the x-2fa-approval header of the HTTP 403.
    signed_token = rsa.sign(
        one_time_token.encode('ascii'),
        private_key,
        'SHA-256')

    # Encode the signed message as friendly base64 format for HTTP
    # headers.
    signature = base64.b64encode(signed_token).decode('ascii')

    return signature
