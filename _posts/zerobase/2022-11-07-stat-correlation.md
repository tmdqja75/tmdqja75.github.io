---
layout: post
title: 통계 - 상관관계
description: >
    
image: https://images.unsplash.com/photo-1609017909889-d7b582c072f7?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1469&q=80
sitemap: false
categories:
  - zerobase
---

* toc
{:toc}

## 상관관계 (Correlation Coefficient)
- 두 변수간의 선형적인 관계의 정도를 나타내는 수치입니다.
- 상관관계는 상관계수 $$(\rho)$$로 나타낼 수 있습니다.
- 
$$\rho = Corr(X, Y) = \frac{Cov(X, Y)}{\sqrt{Var(X)}\sqrt{Var(Y)}}$$

- 상관계수는 $$-1 \leq \rho \leq 1$$의 범위를 가집니다.
  - $$\rho$$가 1에 가까울수록 양의 상관관계, -1에 가까울수록, 음의 상관관계가 뚜렷이 나타납니다.
- 상관계수가 0이라고 아예 관계가 존재하지 않는다는 것은 아닙니다.
  - 아래와 같이 상관계수가 0이여도 세번째 줄과 같이 비선형 관계가 존재할 수도 있습니다.
- 상관관계는 두 변수의 인과관계를 나타내지는 않습니다. 상관관계는 그저 두 변수의 관계만을 나타냅니다. 

![corr](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Correlation_examples2.svg/800px-Correlation_examples2.svg.png){:centered width="500"}
출저: [Wikipedia](https://en.wikipedia.org/wiki/Correlation)
{:.figcaption}

## 표본 상관관계 (Sample Correlation Coefficient)
- 표본 상관관계는 모집단에서 표본을 뽑고 표본데이터에 대해 상관관계를 구하는 것입니다.
- 데이터가 $$(x_1, y_1), (x_2, y_2),..., (x_i, y_i)$$ 형태로 주어진다면, 표본상관관계는 다음과 같이 계산할 수 있습니다.

$$r = \frac{\sum(x_i-\bar{x})(y_i-\bar{y})}{\sqrt{\sum{(x_i-\bar{x})^2}}\sqrt{\sum{(y_i-\bar{y})^2}}} = \frac{S_{xy}}{\sqrt{S_{xx}}\sqrt{S_{yy}}}$$


