---
layout: post
title: How to Use Sagemaker for AWS Beginners (1) | Pipeline Basic Structure
description: >
  Advantages, disadvantages, and usage methods of Sagemaker Pipeline
image: /assets/post_banner/aws-sagemaker.png
categories: mlops
sitemap:
    changefreq : weekly
comments: true
---

* this list will be replaced by the table of contents
{:toc}

# Advantages and Disadvantages of Sagemaker Pipeline

## Advantages

- **Automated Workflows**: SageMaker Pipeline automates machine learning workflows, saving time and delivering consistent results.
- **Modular Design**: Each step can be modularized to build flexible workflows that adapt to your specific needs.
- **Visualization and Monitoring**: You can visually represent workflows and monitor the performance of each step in real-time.

## Disadvantages
- **Cost**: Like other AWS services, costs can accumulate based on usage, so careful resource management is essential.

- **Learning Curve**: First-time users may face a learning curve, and optimizing workflows can require significant time investment.

# Role and Usage of Each Sagemaker Pipeline Step

When using Sagemaker Pipeline, you'll typically go through two main processes to build your pipeline:

- Design each Sagemaker Pipeline Step
- Connect the designed Pipeline Steps

## Designing Sagemaker Pipeline Steps

1. **Data Preprocessing Step (Processing Step)**:
This step loads and preprocesses data, transforming it into a format suitable for model training. This includes data cleaning, feature engineering, scaling, and more. Processing Steps aren't limited to data preprocessing—they can also be used to handle other pipeline components using custom Python scripts.

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

2. **Model Training Step**:
This step trains machine learning models using your training data. You can use SageMaker's built-in algorithms or custom algorithms. SageMaker offers multiple ways to utilize models. Below is an example using TrainingStep:

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

3. **Model Evaluation Step**:
This step evaluates the performance of your trained model and provides feedback for model improvement. This is where you assess model quality and make data-driven decisions about deployment.

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

4. **Model Deployment Step**:
This step deploys your trained model to a SageMaker endpoint, making it ready for inference and real-world predictions.

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

## Defining and Executing Sagemaker Pipeline

Once you've prepared all the steps you want to use in your Sagemaker Pipeline, you'll write code to deploy all steps and related variables to SageMaker. In the code below, the Pipeline class combines pipeline parameters and steps into a cohesive workflow:

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

In the next post, I'll dive deeper into how to write the Python code that goes into each pipeline step and explore how variables and data communicate between steps. Stay tuned for more exciting insights into SageMaker Pipeline development!