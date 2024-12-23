import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_cloudfront_s3.cdk_cloudfront_s3_stack import CdkCloudfrontS3Stack


# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_cloudfront_s3/cdk_cloudfront_s3_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CdkCloudfrontS3Stack(app, "cdk-cloudfront-s3")
    template = assertions.Template.from_stack(stack)
