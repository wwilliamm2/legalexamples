# ~/lx/lx14/public/file_uploader.py

'''
Practices operation of s3 compatible upload.

ref:
https://minio-py.min.io/#file_uploaderpy
pip3 install minio
'''

# file_uploader.py MinIO Python SDK example
from minio import Minio
from minio.error import S3Error
import os


os.environ["RABATASK"]
os.environ["RABATAKEY10"]
os.environ["RABATABUCKET"]

def main():
    # Create a client with the MinIO server playground, its access key
    # and secret key.
    client = Minio("s3.rcs.rabata.io",
                   access_key=os.environ["RABATAKEY10"],
                   secret_key=os.environ["RABATASK"]
    )

    # The file to upload, change this path if needed
    source_file = "upload.tar.gz"
    destination_file = "upload.tar.gz"

    # The destination bucket
    bucket_name = os.environ["RABATABUCKET"]

    # Make the bucket if it doesn't exist.
    found = client.bucket_exists(bucket_name)
    if not found:
        client.make_bucket(bucket_name)
        print("Created bucket", bucket_name)
    else:
        print("Bucket", bucket_name, "already exists")

    # Upload the file, renaming it in the process
    client.fput_object(
        bucket_name, destination_file, source_file,
    )
    print(
        source_file, "successfully uploaded as object",
        destination_file, "to bucket", bucket_name,
    )

if __name__ == "__main__":
    try:
        main()
    except S3Error as exc:
        print("error occurred.", exc)

1
'''
(lx12) lc11@d81:~/lx/lx14/public$ python -i file_uploader.py
error occurred. S3 operation failed; code: MethodNotAllowed, message: The specified method is not allowed against this resource, resource: /legex20240531, request_id: A8B5A4916E714FAC, host_id: None, bucket_name: legex20240531
>>> 
'''
