---
layout: post
title: How to Use Sagemaker for Beginners (1) | Basic Structure of Pipelines
description: >
  Advantages, disadvantages, and how to use Sagemaker Pipelines
image: /assets/post_banner/aws-sagemaker.png
categories: mlops
sitemap:
    changefreq : weekly
comments: true
---

* this list will be replaced by the table of contents
{:toc}

# Advantages and Disadvantages of Sagemaker Pipelines

## Advantages

- Automated Workflows: SageMaker Pipelines automate machine learning workflows, saving time and yielding consistent results.
- Modular Design: Each step can be modularized, enabling the construction of flexible workflows.
- Visualization and Monitoring: Workflows can be represented visually, and the performance of each step can be monitored effectively.

## Disadvantages
- Cost: As with other AWS services, costs may accrue based on usage.

- Learning Curve: New users may encounter a learning curve, which could take time to optimize workflows.

# Role and Usage of Each Step in Sagemaker Pipelines

When using Sagemaker Pipelines, the creation process involves two main steps:

- Designing each Sagemaker Pipeline Step
- Connecting the designed Pipeline Steps

## Designing Sagemaker Pipeline Steps

1. Data Preprocessing Step (Processing Step):
In this step, data is loaded and preprocessed to convert it into a usable format for model training. This may involve data cleaning, feature engineering, scaling, etc. The Processing Step can also be used in the pipeline to handle other elements using separate Python scripts.

```python
from sagemaker.workflow.steps import ProcessingStep, ProcessingInput, ProcessingOutput
from sagemaker.processing import ScriptProcessor

# Preprocessing script
preprocessing_script = "preprocessing.py"

# Create ProcessingStep
preprocessing_step = ProcessingStep(
    name="DataPreprocessing",
    processor=ScriptProcessor(
        image_uri=image_uri,
        command=["python3"],
        instance_type="ml.m5.large",
        instance_count=1,
        base_job_name="data-preprocessing-job",
    ),
    inputs=[
        ProcessingInput(
            source=input_data_uri,
            destination="/opt/ml/processing/input",
            input_name="input-1"
        )
    ],
    outputs=[
        ProcessingOutput(output_name="output-1", source="/opt/ml/processing/output")
    ],
    code=preprocessing_script,
)
```

2. Model Training Step (Model Training Step):
This step uses training data to train a machine learning model. You can use either built-in algorithms from SageMaker or custom algorithms. There are various ways to utilize the model within Sagemaker. Below is an example using TrainingStep.

```python
from sagemaker.workflow.steps import TrainingStep
from sagemaker.estimator import Estimator

# Training script and hyperparameters
training_script = "train.py"
hyperparameters = {"epochs": 10, "batch-size": 64}

# Create TrainingStep
training_step = TrainingStep(
    name="ModelTraining",
    estimator=Estimator(
        image_uri=image_uri,
        role=role,
        instance_count=1,
        instance_type="ml.m5.xlarge",
        base_job_name="model-training-job",
    ),
    inputs={"train": train_data},
    outputs={"model": model_artifacts},
    code=training_script,
    hyperparameters=hyperparameters,
)
```

3. Model Evaluation Step (Evaluation Step):
In this step, the performance of the trained model is assessed, and feedback is provided for model improvement.

```python
from sagemaker.workflow.steps import ProcessingStep

# Evaluation script
evaluation_script = "evaluate.py"

# Create ProcessingStep
evaluation_step = ProcessingStep(
    name="ModelEvaluation",
    processor=ScriptProcessor(
        image_uri=image_uri,
        command=["python3"],
        instance_type="ml.m5.large",
        instance_count=1,
        base_job_name="model-evaluation-job",
    ),
    inputs=[
        ProcessingInput(
            source=model_artifacts,
            destination="/opt/ml/processing/model",
            input_name="input-1"
        ),
        ProcessingInput(
            source=test_data,
            destination="/opt/ml/processing/test",
            input_name="input-2"
        )
    ],
    outputs=[
        ProcessingOutput(output_name="output-1", source="/opt/ml/processing/output")
    ],
    code=evaluation_script,
)
```

4. Model Deployment Step (Model Deployment Step):
This step deploys the trained model to a SageMaker endpoint, allowing for inference.

```python
from sagemaker.model import Model
from sagemaker.inputs import CreateModelInput
from sagemaker.workflow.steps import CreateModelStep

# Create model
model = Model(
    image_uri=image_uri,
    model_data=model_artifacts,
    role=role,
    sagemaker_session=sagemaker_session
)

# Create CreateModelStep
create_model_step = CreateModelStep(
    name="ModelDeployment",
    model=model,
    inputs=CreateModelInput(instance_type="ml.m5.large"),
)
```

## Defining and Running the Sagemaker Pipeline

Once you have prepared all the steps you want to include in your Sagemaker Pipeline, you will write the final code to deploy all the steps and related variables to Sagemaker. The following code defines the pipeline and sets related parameters using the Pipeline class.

```python
from sagemaker.workflow.pipeline import Pipeline

# Define Pipeline
pipeline = Pipeline(
    name="MySageMakerPipeline",
    parameters=[
        input_data_uri,
        train_data,
        test_data,
        model_artifacts
    ],
    steps=[preprocessing_step, training_step, evaluation_step, create_model_step],
    sagemaker_session=sagemaker_session,
)

# Execute Pipeline
pipeline.upsert(role_arn=role)
```

In the next post, we will explore how to write the Python code to insert into each pipeline step and how the variables and data communicate between the steps!