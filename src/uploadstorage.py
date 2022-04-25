import os
from google.cloud import storage


CREDENTIALS_PATH = "C:/Users/JADER NETO/Downloads/teste-credentials.json"

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = CREDENTIALS_PATH

# FILE = "C:/PROJETOS/APIextractor/src/teste.txt"


def createbucket(bucket_name):
    try:
        client = storage.Client()
        bucket = client.bucket(bucket_name)
        client.create_bucket(bucket)
        return True
    except Exception as e:
        print(e)
        return False


def uploadtobucket(blob_name, filepath, bucket_name):
    try:
        client = storage.Client()
        bucket = client.bucket(bucket_name)
        blob = bucket.blob(blob_name)
        blob.upload_from_filename(filepath)
        return True
    except Exception as e:
        print(e)
        return False


def downloadfrombucket(blob_name, filepath, bucket_name):
    try:
        client = storage.Client()
        bucket = client.get_bucket(bucket_name)
        blob = bucket.blob(blob_name)
        with open(filepath, 'wb') as f:
            client.download_blob_to_file(blob, f)
        return True
    except Exception as e:
        print(e)
        return False

