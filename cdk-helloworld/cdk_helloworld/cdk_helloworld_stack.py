from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
    aws_s3 as s3,
    Duration,
    CfnOutput,
    RemovalPolicy,
    Fn,
)
from constructs import Construct


class CdkHelloworldStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        suffix = self.__initialize_suffix()

        # Create S3 bucket
        s3_bucket = s3.Bucket(
            self,
            "VijayCDKStackNameS3",
            bucket_name=f"vijaycdktests3delete-{suffix}",
            lifecycle_rules=[s3.LifecycleRule(expiration=Duration.days(3))],
            removal_policy=RemovalPolicy.DESTROY,
        )

        CfnOutput(self, "VijayCDKBucketName", value=s3_bucket.bucket_name)

    def __initialize_suffix(self):
        short_stack_id = Fn.select(2, Fn.split("/", self.stack_id))
        suffix = Fn.select(4, Fn.split("-", short_stack_id))
        return suffix
