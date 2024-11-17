# Steps
- Create 'cdk-helloworld' folder.
- cd to 'cdk-helloworld' folder
- execute below command
```sh
cdk init app --language python
```
- Python setup 
```sh
# python -m venv .venv # This is already installed by 'cdk init' command.
source ./venv/bin/activate
pip install --upgrade pip
pip list # will contain only 2 packages
pip install -r requirements.txt # It will install 'aws-cdk-lib' and 'constructs' and all required packages
```
- CDK Synth. This step creates 'cdk.out' which contains 'CdkHelloworldStack.template' file.
```sh
cdk synth
```
- CDK Deploy. Deploy the CloudFormation Stack to AWS Account. Make sure `cdk bootstrap <accountnumber>\<region>` had been executed on the AWS account.

```sh
cdk deploy
```


*** Note :- Event after installing packages Visual Studio code will be showing errors that package is not installed. In order for these errors not to show execute below steps. Couldn't find better solution. ***
- Close the Visual Studio Code.
- From Terminal go the folder 'cdk-helloworld'
- Execute `source .venv/bin/activate`.
- Open the Visual Studio Code using `code .`

# Understanding the folder structure
## Important Files
- README.md
- .gitignore
- cdk.json :- contains information for CDK. Most important entry 'app' entry. It contains the executable which needs to be called. For example 'python app.py'
- requirements.txt
- requirements-dev.txt
- app.py