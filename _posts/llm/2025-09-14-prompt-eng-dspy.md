---
layout: post
title: DSPy와 함께하는 체계적인 프롬프트 엔지니어링
image:
  path: https://miro.medium.com/v2/resize:fit:2000/1*5bWUR3N5ki5mE5D6aGZLQA.png
description: >
  Metric을 사용한 체계적인 프롬프트 관리
categories: llm
sitemap:
  changefreq: weekly
comments: true
---

* this list will be replaced by the table of contents
{:toc}

최근 대형 언어 모델(LLM: Large Language Model)의 활용이 급격히 확대되면서, 단순히 “어떤 지시(prompt)를 넣느냐”보다 “어떻게 프롬프트를 설계하고 관리하느냐”가 모델의 성능, 안정성, 유지보수성 등에 큰 영향을 미치게 되었습니다. 이런 맥락에서 **DSPy(Declarative Self-improving Python)**는 프롬프트 엔지니어링의 새로운 패러다임을 제시하며 주목받고 있습니다. 이 글에서는 DSPy가 프롬프트 엔지니어링 환경에서 왜 필요한지, 어떤 동기가 있는지 정리해보겠습니다.

## 기존 프롬프트 엔지니어링의 문제점

많은 사람들이 쳇지피티를 사용하면서 프롬프트를 자주 수정하고 프롬프트 엔지니어링 기법에 대해 찾아보곤 합니다. 개인적인 작업을 하기 위한 수작업 프롬프트 엔지니어링은 크게 문제가 안되지만, LLM을 활용한 실제 서비스를 개발하는 경우에는 이야기가 조금 다릅니다. 실제 서비스에 적용할 때 기존 프롬프트 엔지니어링의 한계부터 살펴보겠습니다.

### 1. 불안정성 / 재현성의 부족

동일한 프롬프트라도 실행 시점, 맥락, 모델 종류, 설정 등에 따라 결과가 달라질 수 있습니다. 약간의 어휘 변화, 문장의 순서 변화만으로도 출력이 크게 달라지는 경우도 많습니다. 이는 시스템으로써 예측 가능하고 안정적인 동작을 기대하기 어렵게 만듭니다.

### 2. 수작업 중심 / 반복적 튜닝 비용이 높음

좋은 프롬프트를 찾기 위해 많은 시간이 소요됩니다. 시행착오(trial-and-error)가 많고, 사람의 직관이나 감에 의존하는 부분이 큽니다. 특히 복잡한 태스크일수록, 모델이 바뀌거나 요구사항이 미세하게 바뀔 때마다 프롬프트를 재작성하거나 튜닝해야 할 수 있습니다.

### 3. 확장성과 유지보수의 어려움

여러 모델을 사용하거나 여러 use case가 있을 경우, 각 케이스마다 프롬프트를 관리해야 하고, 버전 관리, 테스트, 최적화 등이 수작업이 많습니다. 따라서, 기존 프롬프트 엔지니어링 프로세스는 환경 변화(예: 새로운 LLM 출시)에 대응하기가 쉽지 않습니다.

### 4. 최적화가 제한적임

몇 개의 예제(few-shot)나 지침(instruction)을 수작업으로 고르는 방식으로만 최적화를 시도하는 경우가 많습니다. 예제의 선택, 지침의 표현 방식, 프롬프트 내 구조 등이 모델의 출력 품질에 미치는 영향은 크지만, 인간이 모든 조합을 실험하는 데는 한계가 있습니다.

## DSPy가 제안하는 프롬프트 엔지니어링 방향성

위에서 나열한 프롬프트 엔지니어링의 단점들을 해결하기 위해 DSPy는 기존 수작업에 의지하는 프로세스 대신 코드와 프로그래밍에 기반한 프롬프트 엔지니어링 방법을 새롭게 제시합니다.

## DSPy의 구성

DSPy API는 여러 컴포넌트가 준비되어 있지만, 가장 중요한 3가지 컴포넌트에 대해 알아보겠습니다. 각 컴포넌트를 설명하기 위해 문장이 감정을 판단하는 태스크를 예시로 설명해보겠습니다.

### LM

DSPy 프로그램이 실제 언어 모델(LLM)을 호출하는 기본 엔진입니다.￼ 여러 제공자(provider)를 지원하고, (OpenAI, Anthropic, ollama 로컬 모델 등)￼
기본적으로 캐싱(caching) 기능을 제공하여 동일한 호출(prompt)에 대해 재사용이 가능합니다.

```python

import dspy
lm = dspy.LM('openai/gpt-4o-mini', temperature=0.0, max_tokens=256)

dspy.configure(lm=lm)

```

### Signature

[DSPy의 공식 문서](https://dspy.ai/learn/programming/signatures/)에서 Signature를 다음과 같이 설명합니다

> Signatures allow you to tell the LM **what** it needs to do, rather than specify **how** we should ask the LM to do it.
>
> Signatures는 LLM에게 **어떻게** 요청해야 하는지 명시하는 대신, LLM이 **무엇을** 수행해야 하는지 지시할 수 있습니다.
> {:.lead}

Signatures는 prompt 그 자체가 아니라, DSPy가 내부적으로 LM 호출을 구성(prompt 생성, few-shot 예제 등)할 때 지켜야할 형식을 지정하는 역할을 합니다. 즉, 어떻게 LM에 질의할지를 직접 쓰는 것이 아니라 “무엇이 필요하다”(입력 → 출력)만 선언하게 됩니다.

기존 프롬프트 엔지니어링을 할 떄는 아래와 같이 프롬프트를 구성하여 LLM의 입력값으로 넣어줍니다

```python
"""
당신은 문장이 긍정적인지 부정적인지 판단하는 감별사입니다.
아래 문장을 보고, 문장이 어떤 감정을 내포하고 있는지 판단하세요

user_input: {user_input}

response:
"""
```

DSPy의 Signature를 사용하면, 아래와 같이 input과 output 목적으로 좀 더 명확히 할 수 있습니다

```python
from typing import Literal

class Emotion(dspy.Signature):
    """Classify emotion."""

    sentence: str = dspy.InputField()
    sentiment: Literal['sadness', 'joy', 'love', 'anger', 'fear', 'surprise'] = dspy.OutputField()

```

위 예시와 같이 Signature에 출력 타입이나 출력 옵션들을 명시함으로써 LM의 출력 범위를 제한할 수 있고, 잘못된 레이블 예측을 줄일 수 있습니다.

### Modules

Module은 DSPy에서 실제로 입력을 받아 Signature가 정의한 출력 형태로 LM을 호출하는 방식/전략를 파이썬 클래스 형식으로 정의한 컴포넌트입니다. 즉, “어떤 프럼프팅 스타일,추론 방식,코드 실행,도구 등을 쓸 것인가”를 정하는 컴포넌트입니다. DSPy에는 아래 예시를 포함한 다양한 Module들을 제공합니다.

- Predict: 가장 기본 형태, LM에게 그냥 입력 주고 바로 출력 예측함
- ChainOfThought: LM이 내부 사고 과정을(step-by-step) 써가며 추론한 뒤 최종 레이블 출력함
- ProgramOfThought: LM에게 코드를 생성하게 하고, 그 코드 실행 결과로 레이블을 정함. 예: 감정 분석 코드를 생성 → 실행 → 결과 얻음
- ReAct: reasoning + 도구(tool) 사용하여 결과 도출

Module은 아래 코드와 같이 사용할 수 있습니다.

```python
classify = dspy.Predict(Emotion)
result = classify(sentence="I’m so happy to see you!")

result.sentiment
>>>'joy'
```

```python
classify_cot = dspy.ChainOfThought(Emotion)
result2 = classify_cot(sentence="I’m so happy to see you!")
result.sentiment
>>>'joy'
```

### Optimizers

Optimizer는 DSPy 프로그램(module + signature 설정 등)의 프롬프트 (혹은 LM 가중치)를 조정해서 주어진 metric (예: 정확도, F1 등)을 최대화 하도록 자동으로 개선해 주는 최적화 알고리즘 클래스입니다.

Optimizer를 사용하기 위해서는 아래 컴포넌트들이 필요합니다.

- 태스크 목적에 맞는 데이터셋 준비 (LLM으로 생성 또는 직접 생성)

```python
examples = [
  {
    "sentence": "I'm happy",
    "sentiment": "joy"
  },
  {
    "sentence": "I'm sad",
    "sentiment": "sadness"
  },
  {
    "sentence": "I'm scared!",
    "sentiment": "fear"
  },...
]

dspy_data = list()

for example in examples:
    dspy_data.append(dspy.Example(**example).with_inputs('sentence'))
```

- 프롬프트의 성능을 비교할 수 있는 평가 지표 설정 (ex: F1, Accuracy, precision, etc)

```python
def accuracy(example, prediction, trace=None) -> bool:
    return example.label == prediction.label
```

- 프롬프트가 포함된 모듈 (위 Module 섹션 참조)
- 원하는 Optimizer 선정 후 프롬프트 최적화 진행 (사용 가능한 optimizer들은 [여기](https://dspy.ai/learn/optimization/optimizers/#what-dspy-optimizers-are-currently-available)에서 확인하세요)

```python
tp = dspy.MIPROv2(metric=validate_category, auto="light")
optimzed_classify = tp.compile(
  classify,
  trainset=dspy_data,
  max_labeled_demos=0,
  max_bootstrapped_demos=0
)
```

위 단계별로 프로세스를 진행하면, 매 최적화 스텝마다 프롬프트가 평가지표가 나아지는 방향으로 최적화가 자동으로 진행됩니다.

## 결론

프롬프트 엔지니어링은 단순한 기술적 기법을 넘어, LLM을 실제 서비스에 안정적으로 활용하기 위한 핵심 과제로 자리잡고 있습니다. DSPy는 이러한 흐름 속에서 수작업 중심의 프롬프트 설계를 넘어, 코드 기반·자동 최적화 중심의 새로운 패러다임을 제시합니다.

앞으로 더 많은 모델과 Agent 응용 사례가 등장할수록, 프롬프트의 프로그래밍적 접근과 체계적인 최적화의 중요성은 더욱 커질 것으로 보입니다. DSPy가 제공하는 코드 베이스 프롬프트 엔지니어링 방식은 개발자가 프롬프트 엔지니어링을 더 예측 가능하고, 더 확장 가능하며, 더 유지보수하기 좋은 프로세스로 만들어 줄 수 있습니다.
