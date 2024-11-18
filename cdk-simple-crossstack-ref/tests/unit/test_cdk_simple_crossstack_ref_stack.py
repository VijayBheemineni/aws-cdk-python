import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_simple_crossstack_ref.cdk_simple_crossstack_ref_stack import CdkSimpleCrossstackRefStack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_simple_crossstack_ref/cdk_simple_crossstack_ref_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CdkSimpleCrossstackRefStack(app, "cdk-simple-crossstack-ref")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
