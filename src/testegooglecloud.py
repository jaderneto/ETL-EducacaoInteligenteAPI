import os
from google.cloud import storage

CREDENTIALS_PATH = "C:/Users/JADER NETO/Downloads/teste-credentials.json"

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = CREDENTIALS_PATH

storage_client = storage.Client()

# Create a New Bucket
# bucket_name = "24042022_jader"
# bucket = storage_client.bucket(bucket_name)
# bucket = storage_client.create_bucket(bucket)

# print Bucket Details
# vars(bucket)

# Accessing a specific bucket
my_bucket = storage_client.get_bucket('24042022_jader')
print(vars(my_bucket))


# Upload Files

def upload_to_bucket(blob_name, file_path, bucket_name):
    try:
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(blob_name)
        blob.upload_from_filename(file_path)
        return True
    except Exception as e:
        print(e)
        return False


file_path = "C:/PROJETOS/APIextractor/src/teste.txt"

# upload_to_bucket('JADER/teste_24042022', file_path, '24042022_jader')

# Download Files


def download_from_bucket(blob_name, file_path, bucket_name):
    try:
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(blob_name)
        with open(file_path, 'wb') as f:
            storage_client.download_blob_to_file(blob, f)
        return True
    except Exception as e:
        print(e)
        return False


download_from_bucket('JADER/teste_24042022', os.path.join(os.getcwd(), 'file1.csv'), '24042022_jader')