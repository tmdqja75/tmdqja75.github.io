---
layout: post
title: 편집중-DSPy로 해보는 체계적인 프롬프트 엔지니어링
image: 
  path: https://miro.medium.com/v2/resize:fit:2000/1*5bWUR3N5ki5mE5D6aGZLQA.png
description: >
  Metric을 사용한 체계적인 프롬프트 관리
categories: llm
sitemap:
    changefreq : weekly
---

* this list will be replaced by the table of contents
{:toc}

최근 대형 언어 모델(LLM: Large Language Model)의 활용이 급격히 확대되면서, 단순히 “어떤 지시(prompt)를 넣느냐”보다 “어떻게 프롬프트를 설계하고 관리하느냐”가 모델의 성능, 안정성, 유지보수성 등에 큰 영향을 미치게 되었습니다. 이런 맥락에서 **DSPy(Declarative Self-improving Python)**는 프롬프트 엔지니어링의 새로운 패러다임을 제시하며 주목받고 있습니다. 이 글에서는 DSPy가 프롬프트 엔지니어링 환경에서 왜 필요한지, 어떤 동기(motivation)가 있는지 정리해보겠습니다.

## 기존 프롬프트 엔지니어링의 문제점

먼저 기존 프롬프트 엔지니어링의 한계부터 살펴보겠습니다.

### 1.	불안정성 / 재현성의 부족

동일한 프롬프트라도 실행 시점, 맥락, 모델 종류, 설정 등에 따라 결과가 달라질 수 있습니다. 약간의 어휘 변화, 문장의 순서 변화만으로도 출력이 크게 달라지는 경우도 많습니다. 이는 시스템으로써 예측 가능하고 안정적인 동작을 기대하기 어렵게 만듭니다.

### 2.	수작업 중심 / 반복적 튜닝 비용이 높음

좋은 프롬프트를 찾기 위해 많은 시간이 소요됩니다. 시행착오(trial-and-error)가 많고, 사람의 직관이나 감에 의존하는 부분이 큽니다. 특히 복잡한 태스크일수록, 모델이 바뀌거나 요구사항이 미세하게 바뀔 때마다 프롬프트를 재작성하거나 튜닝해야 할 수 있습니다.

### 3.	확장성과 유지보수의 어려움

여러 모델을 사용하거나 여러 use case가 있을 경우, 각 케이스마다 프롬프트를 관리해야 하고, 버전 관리, 테스트, 최적화 등이 수작업이 많습니다. 따라서, 기존 프롬프트 엔지니어링 프로세스는 환경 변화(예: 새로운 LLM 출시)에 대응하기가 쉽지 않습니다.

### 4.	최적화가 제한적임

“몇 개의 예제(few-shot 사례)”나 “지침(instruction)”을 수작업으로 고르는 방식으로만 최적화를 시도하는 경우가 많습니다. 예제의 선택, 지침의 표현 방식, 프롬프트 내 구조 등이 모델의 출력 품질에 미치는 영향은 크지만, 인간이 모든 조합을 실험하는 데는 한계가 있습니다.

## DSPy가 제안하는 프롬프트 엔지니어링 방향성

위에서 나열한 프롬프트 엔지니어링의 단점들을 해결하기 위해 DSPy는 기존 수작업에 의지하는 프로세스 대신 코드와 프로그래밍에 기반한 프롬프트 엔지니어링 방법을 새롭게 제시합니다. 

## DSPy의 구성

DSPy API는 크게 4가지 컴포넌트롤 구성되어 있습니다.

### Signature

[DSPy의 공식 문서](https://dspy.ai/learn/programming/signatures/)에서 Signature를 다음과 같이 설명합니다

> Signatures allow you to tell the LM **what** it needs to do, rather than specify **how** we should ask the LM to do it.
> 
> Signatures는 LLM에게 **어떻게** 요청해야 하는지 명시하는 대신, LLM이 **무엇을** 수행해야 하는지 지시할 수 있습니다.
{:.lead}

원하는 출력 결과를 얻기 위해 프롬프트를 작성하기 보다, Signature는 LLM 모델에 입력할 형식과 출력 결과 형식을 미리 지정해주는 컴포넌트입니다.
문장이 긍정적인지 부정적인지 판단하는 태스크로 예시를 들어 보겠습니다.

기존 프롬프트 엔지니어링을 할 떄는 아래와 같이 프롬프트를 구성하여 LLM의 입력값으로 넣어줍니다

```python
"""
당신은 문장이 긍정적인지 부정적인지 판단하는 감별사입니다.
아래 문장을 보고, 문장이 긍정적인지, 부정적인지 판단하세요

user_input: {user_input}

response:
"""
```

DSPy에선,ㄴ 


### Modules

### Adapters

### Optimizers




