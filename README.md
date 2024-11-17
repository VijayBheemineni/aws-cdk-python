# Urls
- https://docs.aws.amazon.com/cdk/api/v2/docs/aws-construct-library.html

# Setup of CDK

## Prerequisites for CDK installation
https://docs.aws.amazon.com/cdk/v2/guide/prerequisites.html

- node.js :- Install Node.js or later.
- npm :- 

## Installation of CDK 
https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html

```sh
npm install -g aws-cdk
cdk --version # Verifying the version
```

## Optional AWS CDK Tools
https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html
- Installing the AWS Toolkit for Visual Studio Code.
- AWS CDK for VS Code.

# CDK Architecture
- CDK App(Main Container). `app = cdk.App()`. Creates the 'app' container.
- CDK stack :- We can create multiple stacks. All stacks can be part of 'App'. This is defined using 'Stack' construct parameter 'scope'.

## CDK Constructs
- Construct provides 'abstact' over AWS resources. Most AWS services have their own 'Construct'.
- Properties of 'Construct'.
    - scope(stack)
    - id 
    - required/optional parameters
- 


# How CDK works
Me --Write--> Python Code --JSII Compiler--> TypeScript --Execute-->CloudFormation --Deploy--> AWS 

- Synthetize :- Python Code to CloudFormation

## What is CDK Bootstrapping?
- This is one time step per account. 
- Within our AWS Account, CDK needs to install 'CDK ToolKit Stack' which contains resources 'IAM Role for CDK' and 'S3 Bucket'.
- Execute below command
```sh
# cdk bootstrap <accountNumber>/<region>
cdk bootstrap 193229017848/us-west-2
```

# What happens when we execute `cdk init`
- Inside the folder 'cdk-helloworld' when we execute `cdk init app --language python`. CDK will create 'cdk_helloworld'(Only '-' replaced with '_') which is same as folder we created 'cdk-helloworld'.
- With 'cdk_helloworld' folder it creates 'CDK stack' file which has same name as 'cdk_helloworld'(Only '-' replaced with '_'). For example in this case 'cdk_helloworld_stack.py'.
- With this file 'cdk_helloworld_stack.py' it create Python class 'CdkHelloworldStack'.
- 'app.py' initializes the CDK app and then intializes 'CdkHelloworldStack' class.

# What happens when we execute `cdk deploy`
- CloudFormation stack with the name 'CdkHelloworldStack' is created.

# What happens in 'cdk_helloworld_stack.py'.
- This code defines the resources we need to create for our application.
- Our CloudFormation stack extends Base class 'Stack' `class CdkHelloworldStack(Stack)`.
- Then we initialize our stack `def __init__(self, scope: Construct, construct_id: str, **kwargs)`
    - First parameter 'self' is the object itself.
    - Second parameter 'scope'. Whose is the parent of this stack. In our case we are saying 'app' is parent of our stack.
    - Third parameter 'construct_id' is the name or id we are giving to identify our stack'. This name is used to create 'CloudFormation' stack name too.
    - **kwargs :- additional arguments we need to pass to constructor.
- 

# CDK commands
```sh
cdk list # List all stacks in this app.
cdk diff # See the diff between current changes and stack which is deployed
cdk destroy # Destroy the stack
cdk deploy <stack_name> # If multiple stack are deployed, list stack_name
```

# Errors
## CDK bootstrap error 
cdk bootstrap error Resource handler returned message: "The repository with name 'cdk-hnb659fds-container-assets--us-west-2' does not exist in the registry with id ''

Steps
- Get the S3 bucket from CloudFormation Output. Empty the S3 bucket and delete.
- Delete the 'CDKToolKit' CloudFormation stack.

Solution
- After deleting above resources, again execute bootstrap command `cdk bootstrap 193229017848/us-west-2`

