---
layout: post
title: 통계 - 추정
description: >
    
image: https://images.unsplash.com/photo-1609017909889-d7b582c072f7?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1469&q=80
sitemap: false
categories:
  - zerobase
---

* toc
{:toc}

## 모집단의 모수 추정
- 모집단의 모수란, 모집단의 평균과 분산을 나타내는 모평균과 모분산을 의미하는 단어입니다.
- 모수를 추정하는 방법은 크게 두 가지 방법이 있습니다
  - 점추정(Point Estimation): 모수를 하나의 특정 값으로 추청하는 것입니다.
  - 구간 추정(Interval Estimation): 모수가 포함될 수 있는 구간을 추정하는 방식입니다.

### 점추정
- 점추정의 성질
  - 일치성(Consistency): 표본의 크기가 클수록 표본에서 계산된 추정량이 모수와 근접해집니다.
  - 불편성(Unbiased Estimator): 표본에서의 추정량이 모수와 일치해야 됩니다.
    - 모수가 $$\theta$$이고 추정량이 $$\hat{\theta}$$일때, $$E[\hat{\theta}] = \theta$$이면, $$\hat{\theta}$$는 **불편추정량**이 됩니다.
    - 추정량이 같지 않다면, 편의(Bias)가 있다고 합니다. 
  - 유효성(Efficiency): 추정량의 분산이 최소값이어야 합니다.
    - 예를 들어 모수에 관해 두 추정량이 있고, $$(\hat{\theta}_1, \hat{\theta}_2)$$, 한 추정량의 분산값이 다른 추정량의 분산값보다 작으면 $$(Var[\hat{\theta}_1]\geq Var[\hat{\theta}_2])$$, 작은 분산값을 가진 추정량이 더 유효하다고 볼 수 있습니다.
  - 평균오차제곱(Mean Squared Error, MSE):평균오차제곱이 최소값이 되어야 합니다.

    $$MSE = E[(\hat{\theta} - \theta)^2]$$

### 구간추정
#### 신뢰수준 (Confidence Level)
- 구간추정에서 신뢰수준은 주어진 구간에 모수가 존재할 확률을 나타내는 수준입니다.
- 예를 들어, 신뢰 수준이 95%라면, 모수가 구간 추정내에 존재할 확률이 95%이고 5%의 확률로 존재하지 않을 가능성이 있다는 것입니다.
  - 이 오차 확률을 유의 수준(Significant Level)라고도 합니다. $$(\alpha=1-0.95 = 0.05)$$
- 신뢰구간은 아래과 같이 신뢰 상한 $$(U(\hat{\theta}))$$과 신뢰 하한 $$(L(\hat{\theta}))$$ 으로 표시합니다. ($$\theta$$는 추청하고자 하는 모수입니다.)

$$P[L(\hat{\theta}) \leq \theta \leq U(\hat{\theta})] = 1-\alpha$$

- 예를 들어, 모평균 $$\mu$$를 추정할 때, 표본평균이 $$\bar{x}$$이고, 표준오차가 s이면, 신뢰구간은 다음가 같이 표현할 수 있습니다.

$$\bar{x}-z\cdot s \leq \mu \leq \bar{x}+z\cdot s$$

- 아래 도표는 신뢰구간에 따라 달라지는 $$z$$값을 나타내는 도표입니다. 예를 들어, 신뢰구간(CI)가 0.95일때, $$z=1.96$$인 것을 확인할 수 있습니다.

![conf_level](https://d37djvu3ytnwxt.cloudfront.net/assets/courseware/v1/3c2230f2c98f3c61fcb4a4884ba96f84/asset-v1:DelftX+OT.1x+3T2016+type@asset+block/Normal_critical_values.png){:.centered width="500"}
출저: [TUDelft](https://ocw.tudelft.nl/course-readings/note-interpretation-confidence-interval/)
{:.figcaption}

#### 모평균의 구간추정 두가지 케이스
##### 모집단의 분산을 아는 경우

$$\bar{x}-z_{\alpha/2}\cdot\frac{\sigma}{\sqrt{n}} \leq \mu \leq \bar{x}+z_{\alpha/2}\cdot\frac{\sigma}{\sqrt{n}} $$

##### 모집단의 분산을 모르는 경우
  - 모평균의 분산을 모르는 경우, t-분포를 사용합니다.
    - $$\sigma$$ 대신 $$s$$를 사용
    - t분포의 자유도는 $$n-1$$입니다.

$$\bar{x}-t_{\alpha/2, n-1}\cdot\frac{s}{\sqrt{n}} \leq \mu \leq \bar{x}+z_{\alpha/2, n-1}\cdot\frac{s}{\sqrt{n}} $$

### 표본의 크기 결정
- 허용오차
- 
$$$$
## 모비율 추정
- 모비율은 모집단 내에 특정 클래스나 속성이 차지하는 비율을 의미합니다. 
- 관심 있는 특성의 개수
### 모비율의 점추정
### 모비율의 구간 추정
