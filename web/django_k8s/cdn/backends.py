from storages.backends.s3boto3 import S3Boto3Storage, S3StaticStorage


class StaticRootS3BotoStorage(S3StaticStorage):
    location = "static"


class MediaRootS3Boto3Storage(S3Boto3Storage):
    location = "media"
