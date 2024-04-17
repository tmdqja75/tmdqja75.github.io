---
layout: post
title: 시계열 데이터 패키지 - Darts
description: >
  
image: /assets/post_banner/darts.png
categories: mldl
sitemap: false
---

{:.toc}

# Darts: 시계열 데이터를 다루는 원툴

- 오늘은 현업에서 발견한 좋은 시계열 데이터 툴을 소개해 드리겠습니다.
- 바로 Darts라는 python 패키지 입니다.

## 설치

- Darts는 여려 설치 옵션을 제공합니다. Darts는 딥러닝을 포함한 다양한 모델을 지원하기 떄문에, 패키지에 필요한 모든 dependencies들을 설치하면, 지정된 환경에 필요 이상으로 많은 용량을 차치할 수 있습니다. 이를 방지하기 위해, Darts는 여려 설치 옵션을 제공합니다.

![darts-install](/assets/img/blog/darts-install.png)

- 모든 모델 설치 : `pip install "u8darts[all]`
- 필수 패기지만 설치 (neural networks, Prophet, LightGBM, Catboost 제외): `pip install u8darts`
필수 + Prophet + LightGBM + CatBoost: `pip install "u8darts[notorch]"`
필수 + PyTorch 패키지 설치: `pip install "u8darts[torch]"` (`pip install darts`와 동일)

- 실제 배포환경 / 모델 실험 환경에서 요구사항에 맞게 패키지를 설치하면 됩니다.

## 예시 데이터
- 시계열 데이터 문제에 자주 사용되는 Benchmark 데이터를 포함한 여례 예시 데이터를 제공합니다. 
- Darts가 제공하는 모든 데이터 리스트는 다음 링크에서 확인할 수 있습니다.
  - [Darts 시계열 예시 시계열 데이터 리스트](https://unit8co.github.io/darts/generated_api/darts.datasets.html?highlight=darts+datasets#module-darts.datasets)

## 데이터 input 구조
- Darts는 모든 시계열 입력을 크게 `target`과 `covariates`로 나눕니다.
### Target
- **target**은 우리가 예측하고자 하는 시계열을 의미합니다. Darts에서는 univariate time series와 multivariate time series 데이터를 모두 다룰 수 있습니다.
### Covariates
- **covariates**는 모델 예측에 도움을 줄 수 있는 target 데이터와 관련이 있는 시계열 데이터를 의미합니다.
  - covariates 데이터는 다음과 같이 세 가지 부류로 나뉩니다. 
### Past Covariates
- past covairates는 오직 과거에만 알려진 covariate 시계열 데이터입니다.
### Future Covariates
- future covairates는 미래에 이미 알 수 있는 데이터들을 의미합니다.
### Static Covariates
- static covairates는 시간이 변해도 유지되는 데이터를 의미합니다.

```python


```
## 모델 

## 모델 검증

## 