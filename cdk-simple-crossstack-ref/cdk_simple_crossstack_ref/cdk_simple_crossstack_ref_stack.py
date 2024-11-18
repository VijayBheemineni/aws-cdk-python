from aws_cdk import (
    # Duration,
    Stack,
    aws_s3 as s3,
    Duration,
    RemovalPolicy,
    Fn,
    CfnOutput,
)
from constructs import Construct


class CdkSimpleCrossstackRefStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        suffix = self.__initialize_suffix()

        # Create S3 bucket
        self.s3_bucket = s3.Bucket(
            self,
            "VijayCDKStackNameS3",
            bucket_name=f"vijaycdkcrossstackdelete-{suffix}",
            lifecycle_rules=[s3.LifecycleRule(expiration=Duration.days(3))],
            removal_policy=RemovalPolicy.DESTROY,
        )

        CfnOutput(self, "VijayCDKBucketName", value=self.s3_bucket.bucket_name)

    def __initialize_suffix(self):
        short_stack_id = Fn.select(2, Fn.split("/", self.stack_id))
        suffix = Fn.select(4, Fn.split("-", short_stack_id))
        return suffix

    @property
    def my_s3_bucket(self):
        return self.s3_bucket
