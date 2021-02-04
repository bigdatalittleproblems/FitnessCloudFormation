# FitnessCloudFormation Overview
This is a repository to launch and deploy a application on AWS that will allow you to upload any raw ".fit" activity file into an S3 Bucket and process the data to provide a CSV document. This will allow you to import the data and perform various analytics and visualizations. **Currently, this CloudFormation stack is only supported in AWS us-west-1 region.**   

# Building Layers and Lambda Function
You can make changes to the stack and even add layers 
* You can find the Lambda Function in the lambdaFunctionFit directory
* To build the layer on your own, you can use the Dockerfile to deploy a **amazonlinux** image and generate a layer that will be compatable with the Python 3.8 runtime. Below are the commands to run to build the layers Zip file using Dockers. Be sure to be in the root directory of this project to be able to run it, and replace <Name_Container> with whatever name you want to give the container.
```
docker build . -t lamdalayer:latest
docker run --name Name_Layer_Container lamdalayer:latest 
docker cp Name_Layer_Container:/home/python.zip .
docker rm Name_Layer_Container
```
## AWS CLI Deployment
Deploy the CloudFormation Stack: 
```
aws cloudformation create-stack --stack-name demostack --template-url https://fitcfproject.s3-us-west-1.amazonaws.com/cloudformation.json  --region us-west-1 --capabilities CAPABILITY_IAM --parameters ParameterKey=setBucketPublic,ParameterValue=<select True or False>
```

Delete the CloudFormation Stack: 
```
aws cloudformation delete-stack --stack-name demostack --region us-west-1 
```


## Resources
You can dowload the Lambda Layers here and also the lambda_function 
* [Download Layers](https://fitcfproject.s3-us-west-1.amazonaws.com/layers/python.zip)
* [Download lambda_function](https://fitcfproject.s3-us-west-1.amazonaws.com/fitparse/lambda_function.zip)
