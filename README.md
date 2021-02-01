# FitnessCloudFormation Overview
This is a repository to launch and deploy a application on AWS that will allow you to upload any raw ".fit" activity file into an S3 Bucket and process the data to provide a CSV document. This will allow users to import the data and perform various analytics and visualizations. **Currently, this CloudFormation stack is only supported in AWS us-west-1**.   

# Building Layers and Lambda Function
* You can find the Lambda Function in the lambdaFunctionFit directory
* To build the layer on your own, you can use the Dockerfile to deploy a **amazonlinux** image and generate a layer that will be compatable with the Python 3.8 runtime. 
```
docker build . -t lamdalayer:latest
docker run --name <Name_Container> lamdalayer:latest 
docker cp <Name_Container>:python.zip .
docker rm <Name_Container>
```