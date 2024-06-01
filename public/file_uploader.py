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

