import boto3


def get_bronze_bucket_name(environment: str, company: str, site: str) -> str:
    return f'{environment}-etl-bronze-{company}-{site}'


def get_silver_bucket_name(environment: str, company: str, site: str) -> str:
    return f'{environment}-etl-silver-{company}-{site}'


class S3Client:
    def __init__(
        self,
        s3_access_key: str,
        s3_secret_key: str
    ):
        session = boto3.Session(
            aws_access_key_id=s3_access_key,
            aws_secret_access_key=s3_secret_key
        )
        self.s3 = session.resource('s3')

    def put(self, bucket_name: str, filename: str, document: str) -> bool:
        self.s3.Object(bucket_name, filename).put(Body=document)

        return True
