---
layout: post
title: 통계 - 모집단과 표본 분포
description: >
    
image: https://images.unsplash.com/photo-1609017909889-d7b582c072f7?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1469&q=80
sitemap: false
categories:
  - zerobase
---

* tableofcontent
{:toc}

## 모집단과 표본의 정의
- 모집단은 통계를 내는 모든 
- 표본은

||모집단(Population)|표본(Sample)|
|--|:--:|:--:|
|평균|$$\mu$$|$$\bar{X}$$|
|분산|$$\sigma^2$$|$$s^2$$|

### 표본 추출 (Sampling)
- 모집단으로부터 표본을 추출하는 것을 sampling이라고 부릅니다. 표본 추출로 모집단의 특성을 추론할 수 있습니다.
- 모집단에서 데이터를 추출하는 방법은 두 가지가 있습니다.
  - 복원 추출 (Sampling with replacement): 모집단에서 데이터를 추출한 후 추출한 데이터를 다시 모집단에 넣고 다음 데이터를 추출하는 방식입니다.
  - 비복원 추출 (Sampling without replacement): 모집단에서 데이터를 추출한 뒤 추출된 데이터를 다시 모집단으로 넣지 않고 다음 데이터를 추출하는 방식입니다. 

### 불균형 데이터(Imbalanced Data)의 문제
- 모집단 데이터 내에 관심 있는 데이터들이 불균형하게 분산되어 있다면, 데이터를 샘플링할 때 표본이 모집단의 특성을 잘 반영하지 않을 수도 있습니다.
- 예를 들어 아래 도표가 공장에서 생성하는 물품들 중 불랑품들을 빨간색으로 표시해둔 데이터라 가정합시다. 이 데이터를 가지고 표본 추출을 통해 불량률을 구하려고 할 떄, 데이터의 중심에서 표본 추출을 하게 된다면, 불량률이 0%라는 정확하지 않은 결과가 나옵니다. 

![imbalanced](https://miro.medium.com/max/1146/1*kVUSNSaF3KFp1ZsGahxBBA.png){:.centered width="400"}
출저: [Dinesh Yadav](https://towardsdatascience.com/weighted-logistic-regression-for-imbalanced-dataset-9a5cd88e68b)
{:.figcaption}

- 이처럼, 불균형한 데이터에서는 표본 추출(Sampling)하는 방식도 데이터 분석에 큰 영향을 미칩니다.

#### Sampling 기법
- Over Sampling
  - Over Sampling은 데이터량이 적은 타겟 클래스를 데이터량이 많은 클래스의 데이터량만큼 샘플링을 하는 방식입니다 (복원 추출).
  - 과도적합(Overfit)문제가 발생할 수 있습니다.
- Under Sampling
  - Under Sampling은 데이터량이 많은 클래스 데이터 추출 수를 데이터량이 적은 클래스의 데이터량 만큼만 샘플링을 하는 방식입니다.
  - 데이터가 편향될 수 있고, 모형의 성능을 떨어뜨릴 수 있습니다.


![Overunder](https://i.stack.imgur.com/FEOjd.jpg){:.centered width="400"}
출저: [Cross Validated](hhttps://stats.stackexchange.com/questions/351638/random-sampling-methods-for-handling-class-imbalance)
{:.figcaption}

## 표본분포 (Sampling Distribution)
- 표본분포는 통계량들이 이루는 분포를 의미합니다.
### 통계량 (Statistic)
- 통계량은 표본을 바탕으로 계산되는 평균, 분산등을 의미합니다.
- 표본의 평균$$(\bar{X})$$과 분산$$(s^2)$$은 다음과 같이 계산됩니다.

$$\bar{X} = \frac{x_1+x_2 + ...+x_n}{n},\; s^2 = \frac{1}{n-1}\sum_{i=1}^{n} (x_i-\bar{x})^2$$

### 표본 평균 ($$\bar{X}$$)의 기대값과 분산
- 특정 모집단에서 여러 개의 표본들을 추출하여 각 표본들의 평균을 계산했을 때 그 평균의 기대값을 계산하면 다음과 같이 계산할 수 있습니다.

$$E[\bar{X}] = E[\frac{1}{n}(x_1+x_2+...+x_n)] = \frac{1}{n}(E[x_1]+E[x_2]+...E[x_n]) = \frac{1}{n}(\mu+\mu+ ...+\mu) =\mu$$

- 표본 평균의 분산은 다음과 같이 계산할 수 있습니다.

$$Var[\bar{X}] = Var[\frac{1}{n}(x_1+x_2+...+x_n)] = \frac{1}{n^2}(Var[x_1]+Var[x_2]+...Var[x_n]) = \frac{1}{n^2}(\sigma^2+\sigma^2+...+\sigma^2) = \frac{\sigma^2}{n}$$


### 중심 극한 정리 (Central Limit Theorem)
- 평균이 $$\mu$$이고 분산이 $$\sigma^2$$인 임의의 모집단에서 크기가 충분히 큰 표본울 추출할 때, 표본 평균 $$\bar{X}$$는 근사적으로 정규분포 $$(\bar{X} \sim N(\mu, \sigma^2/n))$$ 를 따르게 됩니다.

### 카이제곱 분포 ($$\chi-$$square Distribution)
- $$Z \sim \chi^2(\nu)$$.
- 표준 정규분포의 합
- 범주형 자료 분석에 활용함
$$f(x:\nu) = \frac{1}{2^{\frac{\nu}{2}}\Gamma(\frac{\nu}{2})}x^{\frac{\nu}{2}-1}e^{-\frac{x}{2}},\; x > 0$$

#### 자유도

### t-분포 (t-Distribution)

### F-분포 (F-distribution)
- 분산분석에 활용
- 