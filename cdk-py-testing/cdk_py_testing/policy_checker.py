import jsii
from aws_cdk import IAspect, aws_iam, Stack
import json


@jsii.implements(IAspect)
class PolicyChecker:

    def visit(self, node):
        print(f"Visiting {node.__class__.__name__}")

        if isinstance(node, aws_iam.CfnPolicy):
            resolveDoc = Stack.of(node).resolve(node.policy_document)
            resolvedDocJson = json.dumps(resolveDoc)

            print(resolvedDocJson)
