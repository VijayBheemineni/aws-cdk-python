from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
    aws_s3 as s3,
    Duration,
    CfnOutput,
    RemovalPolicy,
)
from constructs import Construct


class CdkHelloworldStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create S3 bucket
        s3_bucket = s3.Bucket(
            self,
            "VijayCDKStackNameS3",
            bucket_name="vijaycdktests3delete",
            lifecycle_rules=[s3.LifecycleRule(expiration=Duration.days(3))],
            removal_policy=RemovalPolicy.DESTROY,
        )

        CfnOutput(self, "VijayCDKBucketName", value=s3_bucket.bucket_name)
