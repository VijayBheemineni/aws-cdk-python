from aws_cdk import (
    # Duration,
    Stack,
    aws_cloudfront,
    aws_cloudfront_origins,
    aws_s3,
    aws_s3_deployment,
    CfnOutput,
    RemovalPolicy,
)
from constructs import Construct
import os


class CdkCloudfrontS3Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        deployment_bucket = aws_s3.Bucket(
            self, "VijayDeploymentBucket", removal_policy=RemovalPolicy.DESTROY
        )

        ui_dir = os.path.join(
            os.path.dirname(__file__), "..", "..", "npm-vite-web-cloudfornt-s3", "dist"
        )

        if not os.path.exists(ui_dir):
            print(f"Web code directory not found : {ui_dir}")
            return

        origin_identity = aws_cloudfront.OriginAccessIdentity(
            self, "VijayOriginIdentityDeploymentBucket"
        )
        deployment_bucket.grant_read(origin_identity)

        distribution = aws_cloudfront.Distribution(
            self,
            "VijayCDKCloudfrontS3",
            default_root_object="index.html",
            default_behavior=aws_cloudfront.BehaviorOptions(
                origin=aws_cloudfront_origins.S3Origin(
                    deployment_bucket, origin_access_identity=origin_identity
                )
            ),
        )

        aws_s3_deployment.BucketDeployment(
            self,
            "VijayAWSS3Deployment",
            destination_bucket=deployment_bucket,
            sources=[aws_s3_deployment.Source.asset(ui_dir)],
            distribution=distribution,
        )

        CfnOutput(
            self, "VijayCloudfrontS3URl", value=distribution.distribution_domain_name
        )
