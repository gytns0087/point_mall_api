from storages.backends.s3boto3 import S3Boto3Storage
import boto3

from . import settings


class StaticStorage(S3Boto3Storage):

    location = settings.STATIC_ROOT