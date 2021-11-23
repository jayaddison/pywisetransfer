from config import BUCKET
from google.cloud import storage

storage_client = storage.Client()
bucket = storage_client.get_bucket(BUCKET)


def download_blob(source_blob_name, destination_file_name):
    """Downloads a blob from the bucket."""
    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(destination_file_name)

    print('Blob {} downloaded to {}'.format(
        source_blob_name,
        destination_file_name))


