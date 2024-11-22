#!/usr/bin/env python3
import os

import aws_cdk as cdk

from cdk_py_testing.cdk_py_testing_stack import CdkPyTestingStack
from cdk_py_testing.policy_checker import PolicyChecker


app = cdk.App()
stack = CdkPyTestingStack(app, "CdkPyTestingStack")
cdk.Tags.of(stack).add("CreatedBy", "VijayBheemineni")
cdk.Tags.of(stack).add("Description", "Vijay CDK Python Test Concepts")

cdk.Aspects.of(app).add(PolicyChecker())
app.synth()
