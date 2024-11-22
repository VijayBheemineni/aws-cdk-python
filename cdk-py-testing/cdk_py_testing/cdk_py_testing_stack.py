from aws_cdk import Stack, aws_lambda, aws_s3, RemovalPolicy
from constructs import Construct


class CdkPyTestingStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        cdk_lambda = aws_lambda.Function(
            self,
            "VijayCDKLambda",
            handler="index.handler",
            code=aws_lambda.Code.from_inline("print()"),
            runtime=aws_lambda.Runtime.PYTHON_3_11,
        )

        bucket = aws_s3.Bucket(
            self, "VijayCDKBucket", versioned=True, removal_policy=RemovalPolicy.DESTROY
        )

        bucket.grant_read(cdk_lambda)
