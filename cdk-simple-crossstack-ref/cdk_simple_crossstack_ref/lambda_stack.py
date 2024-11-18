from aws_cdk import (
    # Duration,
    Stack,
    aws_s3 as s3,
    aws_lambda,
)
from constructs import Construct


class CdkSimpleCrossstackLambdaStack(Stack):

    def __init__(
        self, scope: Construct, construct_id: str, bucket: s3.Bucket, **kwargs
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        aws_lambda.Function(
            self,
            "VijayCDKLambdaDelete",
            code=aws_lambda.Code.from_inline(
                "import os\ndef handler(event, context):\n print(os.environ['COOL_BUCKET_ARN'])"
            ),
            handler="index.handler",
            runtime=aws_lambda.Runtime.PYTHON_3_13,
            environment={"BUCKET_ARN": bucket.bucket_arn},
        )
