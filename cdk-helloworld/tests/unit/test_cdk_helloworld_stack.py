import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_helloworld.cdk_helloworld_stack import CdkHelloworldStack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_helloworld/cdk_helloworld_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CdkHelloworldStack(app, "cdk-helloworld")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
