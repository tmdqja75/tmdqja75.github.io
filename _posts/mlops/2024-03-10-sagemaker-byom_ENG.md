---
layout: post
title: How to Use Sagemaker for Beginners (2) | Using Custom Models in Sagemaker
description: >
  A guide on how to deploy Custom models in Sagemaker.
image: /assets/post_banner/aws-sagemaker.png
categories: mlops
sitemap:
    changefreq : weekly
comments: true
---

* this list will be replaced by the table of contents
{:toc}

# Deploying Custom Models in Sagemaker

## Sagemaker 🩵 Docker Container
- Before diving into how to deploy a custom model in the Sagemaker environment, it’s important to understand how Sagemaker utilizes Docker Containers during model deployment.
- Below is a flowchart illustrating how the Sagemaker Endpoint leverages Docker containers.

![sm-endpoint](/assets/img/blog/sm-endpoint-docker.jpeg)

1. The Sagemaker Endpoint retrieves a Docker Container from ECR where the model is running.
2. It fetches files related to the model from S3.
3. When an API or user calls the Endpoint, it receives input in the REST API format, processes it within the container, and returns the output.

- In this blog post, we will cover how to save your model to S3, create a container, and finally generate a Sagemaker Endpoint.
- All the code snippets provided can be easily executed in the Sagemaker Notebook environment using Jupyter Notebook.

## When to Deploy a Custom Model 🤷🏻‍♂️
- While working within the AWS Sagemaker environment, there may be instances where deploying a model using only the resources provided by Sagemaker is not feasible.
- For instance, if you wish to use packages not available in the Sagemaker environment alongside your commonly used Tensorflow, Pytorch, or XGBoost packages, you may need to create a custom Docker container for deployment.
- The process of deploying a customized model in Sagemaker follows these steps:
  
1. Write a Sagemaker model serving script
2. Upload the model to S3
3. Upload a custom Docker image to AWS ECR
4. Create the model in SageMaker
5. Create an Endpoint Configuration
6. Create an Endpoint
7. Invoke the Endpoint

## 1. Write a Sagemaker Model Serving Script (`inference.py`)

- First, you need to write the Python code that will handle the model and input/output data processing within the Sagemaker Endpoint.
- The `inference.py` script includes the code for preprocessing the input request, running inference, and postprocessing the inferred results.
    - `model_fn`: This function takes the path where the model is saved as input, reconstructs the model, and returns both the model and related information.
    - `input_fn`: This function receives raw input data and returns it formatted for the model.
    - `predict_fn`: This function takes the transformed data from `input_fn` and the model as input, processes the data, and returns the final results.
    - `output_fn`: This function receives the final processed results and converts them to JSON format before returning the output.

- The `inference.py` can be structured as follows. You are welcome to customize the internal logic of each function as needed.

```python
# inference.py

def model_fn(model_dir):
    ...
    return model, transform
 
def input_fn(request_body, request_content_type):
    ...
    return inputs

def predict_fn(input_data, model):
    ...
    return processed_data

def output_fn(prediction, accept):
    ...
    return json.dumps(prediction), accept

```

- To debug and ensure that `inference.py` functions correctly, you can verify the output with simple test code like the one below:

```python
import json
from inference import model_fn, predict_fn, input_fn, output_fn

response, accept = output_fn(
    predict_fn(
        input_fn(payload, "text/csv"),
        model_fn("./")
    ),
    "application/json"
)

json.loads(response)
```

## 2. Upload the Model to S3

- Once you have verified that `inference.py` works correctly, it's time to save the model to S3.
- Before uploading, compress the model files along with `inference.py` into a single archive.
  - Sagemaker typically uses the `tar.gz` format for compression.

```bash
tar -czvf ./model.tar.gz -C ./ model.joblib inference.py
```

- After compressing the model, use boto3 to upload it to S3.

```python
import boto3
from datetime import datetime
bucket = "bucket_name"
object_key = f"model_function/model.tar.gz"

s3 = boto3.resource('s3')
s3.meta.client.upload_file("./model.tar.gz", bucket, object_key)

```

## 3. Upload Custom Docker Image to AWS ECR

- With the trained model now uploaded to S3, it’s time to configure the environment where the model will run.
- First, log into the AWS ECR registry from the Sagemaker environment.

```bash
# Authenticate Docker to Amazon ECR registry
aws ecr get-login-password --region $REGION | docker login --username AWS --password-stdin <docker_registry_url>.dkr.ecr.$REGION.amazonaws.com

# Log into Amazon ECR registry
aws ecr get-login-password --region $REGION | docker login --username AWS --password-stdin $ACCOUNT.dkr.ecr.$REGION.amazonaws.com
```

- After logging into ECR, create a Dockerfile to build the container to be pushed to ECR. Depending on your project, you can use images from AWS’s provided registry as the base and configure the necessary environment.
- You can search for images available in the AWS Seoul Region at the following link: 

[AWS Seoul Region Docker Registry URLs](https://docs.aws.amazon.com/sagemaker/latest/dg-ecr-paths/ecr-ap-northeast-2.html)

```dockerfile
# Base image
FROM <docker_registry_url>.dkr.ecr.<my_aws_region>.amazonaws.com/pytorch-inference:2.0.0-gpu-py310

# Install additional required packages / configure environment
RUN pip install workalendar
...
```

- Once the Dockerfile is complete, build the Docker image using the build command.

```bash
docker build -t model-project .
```

- After building, create a repository in ECR and push the image to the newly created repository.

```bash
# Create AWS ECR repository
aws ecr create-repository --repository-name model-project

docker tag model-project:latest $ACCOUNT.dkr.ecr.$REGION.amazonaws.com/model-project:latest

# Push tagged image to the repository
docker push $ACCOUNT.dkr.ecr.$REGION.amazonaws.com/model-project:latest
```

- With this step completed, you have set up everything necessary for deployment, including the model and the Docker-based environment.
- Now, let’s deploy the created model and container to Sagemaker.

## 4. Create the Model in SageMaker

- Initially, you need to register the model in the Sagemaker Model Registry.
- Model registration can be done using the following Python code.
- At this stage, you will use the S3 URI where your model is stored and the ECR URL where the Docker container resides.

```python
import boto3
import sagemaker

sagemaker_client = boto3.client(service_name="sagemaker")
role = sagemaker.get_execution_role()

bucket = "bucket_name"
object_key = f"model_function/model.tar.gz"

model_name = f"model-test"

primary_container = {
    "Image": f"{my_aws_account}.dkr.ecr.{my_aws_region}.amazonaws.com/model-project:latest",
    "ModelDataUrl": f"s3://{bucket}/{object_key}"
}

create_model_response = sagemaker_client.create_model(
    ModelName=model_name,
    ExecutionRoleArn=role,
    PrimaryContainer=primary_container)
```

## 5. Create Endpoint Configuration

- With the model registered, the next step is to create an Endpoint Configuration using the registered model.
- The Endpoint Configuration sets up the model and the environment where the container will run.

```python
endpoint_config_name = f"ai-vad-model-config"

sagemaker_client.create_endpoint_config(
    EndpointConfigName=endpoint_config_name,
    ProductionVariants=[{
        "InstanceType": "ml.g5.xlarge",
        "InitialVariantWeight": 1,
        "InitialInstanceCount": 1,
        "ModelName": model_name,
        "VariantName": "AllTraffic"}])
```

## 6. Create Endpoint

- Finally, create the Sagemaker Endpoint that can be directly invoked by users or APIs.

```python
endpoint_name = f"ai-vad-model-endpoint-{current_datetime}"

sagemaker_client.create_endpoint(
    EndpointName=endpoint_name,
    EndpointConfigName=endpoint_config_name)
```

- Note that it may take some time for the Endpoint to be created. You can check the creation status using the code below. If the status is `InService`, you can confirm that the model Endpoint has been successfully created.

```python
response = sagemaker_client.describe_endpoint(EndpointName=endpoint_name)
print(response["EndpointStatus"])
```

## 7. Invoke the Endpoint

- Once the Sagemaker Endpoint has been successfully created, your custom model is finally deployed. To test the created Endpoint, you can use the code below to invoke it.

```python
payload = "1.0,2.0,3.2,2.2,1.23,11.5"

sagemaker_runtime = boto3.client("runtime.sagemaker")
response = sagemaker_runtime.invoke_endpoint(
    EndpointName=endpoint_name,
    ContentType="text/csv",
    Body=payload
)

response = json.loads(response["Body"].read().decode())
```

With this, you have successfully navigated the process of deploying a custom model in Sagemaker! Time to unleash the power of your machine learning models in the cloud!