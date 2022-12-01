---
layout: post
title: 통계 - 회귀분석
description: >
    
image: https://images.unsplash.com/photo-1609017909889-d7b582c072f7?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1469&q=80
sitemap: false
categories:
  - zerobase
---

* toc
{:toc}

# 회귀분석 (Regression Analysis)
- 회귀분석은 여러 변수들의 함수적인 관계를 찾아내는 통계적 분석 방법으로, 독립변수를 통해 종속변수를 예측하는 방법이기도 합니다.
  - 종속변수(Dependent Variable)는 다른 변수에 영향을 받는 변수로, 예측하고자 하는 변수를 칭합니다. 회귀분석에서 출력값으로 지정되는 변수입니다.
  - 독립변수(Independent Variable)는 종속변수에 영향을 주는 변수로, 회귀분석에 입력값으로 지정되는 변수입니다.
- 데이터의 특성에 따라, 함수가 직선 형태인 선형회귀(Linear Regression), 또는 함수가 직선이 아닌 비선형회귀(Nonlinear Regression)를 사용할 수도 있습니다.

![](https://miro.medium.com/max/1400/1*HbFXVWyvwaoRpTHP2n_deQ.png){:.centered width="500"}
출저: [Medium Post](https://medium.com/@toprak.mhmt/non-linear-regression-4de80afca347)
{:.figcaption}

## 회귀분석 종류
- 회귀분석은 단순 회귀분석과 다중 회귀분석으로 나눌 수 있습니다.
### 단순 회귀분석 (Simple Regression Analysis)
- 하나의 독립변수로 종속변수를 예측하는 회귀 모형(함수)를 찾아내는 분석을 단순회귀분석이라 합니다.
- 단순 회귀분석으로 찾은 함수는 다음과 같은 형태로, 하나의 독립변수 입력값$$(X)$$으로 하나의 종속변수 $$(Y)$$ 출력값을 반환합니다.

$$Y=\beta_0 + \beta_1 X + \epsilon_i$$

### 다중 회귀분석 (Multiple Regression Analysis)
- 여러 개의 독립 변수로 하나의 결과값(종속변수)를 예측하는 분석 방법입니다. 
- 다중 회귀분석에 사용되는 함수는 다음과 같이 여려 독립변수$$(X_1, X_2, ...)$$를 품고 있습니다. 

$$Y=\beta_0 + \beta_1 X_1 + \beta_2 X_2 + ... +\beta_i X_i + \epsilon_i$$
