#!/usr/bin/env python3
import os

import aws_cdk as cdk

from cdk_simple_crossstack_ref.cdk_simple_crossstack_ref_stack import (
    CdkSimpleCrossstackRefStack,
)
from cdk_simple_crossstack_ref.lambda_stack import CdkSimpleCrossstackLambdaStack


app = cdk.App()
cdk_simple_crossstack_ref = CdkSimpleCrossstackRefStack(
    app,
    "CdkSimpleCrossstackRefStack",
)
CdkSimpleCrossstackLambdaStack(
    app, "CdkSimpleCrossstackLambdaStack", cdk_simple_crossstack_ref.my_s3_bucket
)

app.synth()
