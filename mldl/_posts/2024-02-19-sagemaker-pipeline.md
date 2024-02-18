---
layout: post
title: AWS 초보를 위한 Sagemaker Pipeline 사용법 (1) - Pipeline 기본 구조
description: >
  Sagemaker Pipeline의 장단점과 사용방법
image: /assets/img/blog/example-content-ii.jpg
categories: mldl
sitemap: false

---

{:toc}

# Sagemaker Pipeline의 장단점

## 장점

- 자동화된 워크플로우: SageMaker Pipeline은 머신러닝 워크플로우를 자동화하여 시간을 절약하고 일관된 결과를 얻을 수 있습니다.
- 모듈화된 설계: 각 단계를 모듈화하여 유연한 워크플로우를 구축할 수 있습니다.
- 시각화 및 모니터링: 워크플로우를 시각적으로 표현하고 각 단계의 성능을 모니터링할 수 있습니다.

## 단점
- 비용: 다른 AWS 서비스와 마찬가지로 사용량에 따라 비용이 발생할 수 있습니다.

- 러닝 커브: 처음 사용자들에게는 학습 곡선이 있을 수 있으며, 워크플로우를 최적화하는 데 시간이 소요될 수 있습니다.

# Sagemaker Pipeline의 각 Step 역할과 사용방법

Sagemaker Pipeline을 사용할 때는 크게 두 과정을 거쳐서 만들게 됩니다.

- 각 Sagemaker Pipeline Step 설계
- 설계한 Pipeline Step 연결

## Sagemaker Pipeline Step 설계

1. 데이터 전처리 단계 (Processing Step):
이 단계에서는 데이터를 불러오고 전처리하여 모델 학습에 사용할 수 있는 형식으로 변환합니다. 예를 들어 데이터 정제, 특성 엔지니어링, 스케일링 등이 이루어집니다. Processing Step는 데이터 전처리 뿐만 아니라 별도의 python script를 사용하여 Pipeline내 다른 요소들을 처리할 경우에도 사용될 수 있습니다.

```python
from sagemaker.workflow.steps import ProcessingStep, ProcessingInput, ProcessingOutput
from sagemaker.processing import ScriptProcessor

# 전처리 스크립트
preprocessing_script = "preprocessing.py"

# ProcessingStep 생성
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

2. 모델 학습 단계 (Model Training Step):
학습 데이터를 사용하여 머신러닝 모델을 학습합니다. SageMaker의 내장 알고리즘 또는 사용자 지정 알고리즘을 사용할 수 있습니다. Sagemaker에서 모델을 활용할 수 있는 방법은 여러가지 방법 있습니다. 아래는 TrainingStep을 활용하여 

```python
from sagemaker.workflow.steps import TrainingStep
from sagemaker.estimator import Estimator

# 학습 스크립트와 하이퍼파라미터
training_script = "train.py"
hyperparameters = {"epochs": 10, "batch-size": 64}

# TrainingStep 생성
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

3. 모델 평가 단계 (Evaluation Step):
학습된 모델의 성능을 평가하고 모델을 개선하기 위한 피드백을 제공합니다. 이 단계에서 

```python
from sagemaker.workflow.steps import ProcessingStep

# 평가 스크립트
evaluation_script = "evaluate.py"

# ProcessingStep 생성
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

4. 모델 배포 단계 (Model Deployment Step):
학습된 모델을 SageMaker 엔드포인트로 배포하여 추론을 수행할 수 있도록 합니다.

```python
from sagemaker.model import Model
from sagemaker.inputs import CreateModelInput
from sagemaker.workflow.steps import CreateModelStep

# 모델 생성
model = Model(
    image_uri=image_uri,
    model_data=model_artifacts,
    role=role,
    sagemaker_session=sagemaker_session
)

# CreateModelStep 생성
create_model_step = CreateModelStep(
    name="ModelDeployment",
    model=model,
    inputs=CreateModelInput(instance_type="ml.m5.large"),
)

```

## Sagemaker Pipeline 정의 및 실행

Sagemaker Pipeline에 사용하고 싶은 모든 step 준비가 완료되면, 최종적으로 모든 step과 관련 변수들을 Sagemaker에 배포하는 코드를 작성합니다. 아래 코드에서 Pipeline 클래스로 pipeline 관련 파라미터와 

```python
from sagemaker.workflow.pipeline import Pipeline

# Pipeline 정의
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

# Pipeline 실행
pipeline.upsert(role_arn=role)

```



다음 포스팅에서는 각 pipeline step에 삽입하는 python코드를 어떤 식으로 작성해야 하는지와 각 변수와 데이터들이 step간 어떤 식으로 통신되는지에 대한 포스팅을 올려보겠습니다!