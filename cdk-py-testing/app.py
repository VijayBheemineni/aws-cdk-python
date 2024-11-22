#!/usr/bin/env python3
import os

import aws_cdk as cdk

from cdk_py_testing.cdk_py_testing_stack import CdkPyTestingStack


app = cdk.App()
CdkPyTestingStack(app, "CdkPyTestingStack")

app.synth()
