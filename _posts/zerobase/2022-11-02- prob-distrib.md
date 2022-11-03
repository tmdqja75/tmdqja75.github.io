---
layout: post
title: 통계 - 확률분포
description: >
    
image: https://images.unsplash.com/photo-1609017909889-d7b582c072f7?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1469&q=80
sitemap: false
categories:
  - zerobase
---

* toctoc
{:toc}

## 이산형 확률분포 (Discrete Probability Distribution)

### 이산형 균등분포 (Discrete Uniform Distibution)
- 확률 변수 X가 유한개이고 모든 확률 변수들이 균일한 확률을 갖는 분포입니다.
- $$X \sim U(a, b)$$로 표현하기도 합니다.

$$f_x(X) = P(X=x) = \frac{1}{N}, \; x=1, 2, ..., N$$


- 기대값: $$E[X] = {(n+1)}/{2}$$
- 분산: $${(n^2-1)}/{12}$$

{% include uniform.html %}

### 베르누이 분포 (Bernoulli Distribution)

#### 베르누이 시행 (Bernoulli Trial)
- 베르누이 시행은 실행의 결과가 성공과 실패, 동전의 앞뒷면과 같이 두 가지 결과만 존재하는 시행을 베르누이 시행이라고 합니다.

$$
\begin{equation}
  X =
    \begin{cases}
      1 & \text{성공}\\
      0 & \text{실패}\\
    \end{cases}       
\end{equation},\; X\sim  Bernoulli(p)
$$

{% include bernoulli.html %}

- 기대값: $$E[X] = p$$
- 분산 $$Var[X] = p(1-p)$$

### 이항분포 (Binomial Distribution)
- 이항분포는 **서로 독립적인** 베르누이 실행을 $$n$$번 반복하여 실행했을 때 성공한 횟수 X의 확률 분포를 나타냅니다.

여기서 **서로 독립적인 실행**이란, 각각의 사건이 이전이나 이후의 사건에 영향을 미치지 않는다는 것을 의미합니다. 예를 들어, 10개의 공에서 공 하나를 빼고, 공을 다시 넣지 않고 다음 공을 빼면, 공을 빼는 행위가 다음 사건의 확률에 영향을 끼쳐서 $$(1/10 \rightarrow 1/9)$$ 독립적인 실행이 되지 않습니다. 하지만, 공을 다시 넣고 다른 공을 뽑는다면, 다음 공의 확률이 유지됨으로, 처음 공과 다음 공을 뽑는 행위는 서로 독립적인 실행이 됩니다. 
{:.note}

$$f_x(X) = P(X=x) = \binom{n}{x}p^x(1-p)^{n-x}\; X\sim  B(n, p)$$

- 예를 들어, 동전을 10번$$(n)$$ 던졌을 때, 동전의 앞면이 나올 횟수 $$(x)$$의 확률을 구하는 식은 다음과 같습니다.

$$P(x) = \binom{10}{x}0.5^x(0.5)^{10-x}$$

- 기대값: $$E[X]=np$$
- 분산: $$Var[X]=np(1-p)$$

### 포아송 분포(Poisson Distribution)
- 포아송 분포는 일정한 시간대에 특정 사건이 발생할 확률 분포입니다.

$$P(X=x) = \frac{e^{-\lambda}\lambda^x}{x!},\; x=0, 1, 2, ...\; X \sim poisson(\lambda)$$

- 기대값: $$E[X]=\lambda$$
- 분산: $$Var[X]=\lambda$$

#### 이항분포와 포아송 근사
- $$X$$의 확률분포가 이항 분포 $$X \sim B(n,p)$$를 따를 때, n이 충분히 크고, p가 아주 작을 때 (),$$X$$의 분포는 $$\lambda=np$$인 포아송 분포와 근사해집니다.
- n이 클 때 $$(n \geq 30)$$ 보통 $$np < 5$$를 만족하게 $$p$$가 작으면 근사도가 높아집니다.
- 아래 그래프는 $$n=100, p=0.01$$일 때의 이항분포와 $$\lambda=np=(100)(0.01)=1$$을 사용한 포아송 분포를 같이 그려놓은 그래프입니다. 보시다시피 두 그래프가 근사하게 겹치는 것을 확인할 수 있습니다. (마우스를 각 점에 올려놓으면 값을 확인할 수 있습니다.)

{% include poisson_n_binom.html %}

### 기하분포 (Geometric Distribution)
- 어떤 

$$
P(X=x) = (1-p)^{x-1}p, \; x=1, 2,... \; X \sim Geometric(p) 
$$

{% include geometric.html %}

### 음이항분포 (Negative Binomial Distribution)
- 성공확률이 p일 때, r번의 실패가 나올 때 까지 발생한 성공 횟수 X의 확률 분포

$$
P(X=x) = \binom{x+r-1}{x}p^x(1-p)^r, \; x=1, 2, ...\; X \sim NB(r, p)
$$

## 연속형 확률분포 (Continuous Probability Distribution)

### PDF와 CDF
#### 확률밀도함수 (PDF: Probability Distribution Function)

##### 확률 밀도 함수의 특징
  - 모든 $$X$$에 대해 확률은 0이거나 0보다 큽니다
  
    $$f(X) \geq 0$$

  - 확률밀도함수에 포함되에 있는 모든 값들을 더하면 1이 됩니다.

  $$P(x \in (-\infty, \infty))= \int_{-\infty}^{\infty} f(x)dx = 1 $$

  - 확률 변수 $$X$$가 $$a$$와 $$b$$ 사이에 있을 확률은 $$a$$와 $$b$$ 사이에 있는 모든 확률밀도를 더한 (적분)한 값입니다.
 
  $$P(a \leq X \leq b) = \int_{a}^{b} f(x)dx$$

##### 확률밀도함수의 평균과 분산

$$E(X) = \int_{-\infty}^{\infty} xf(x)dx$$

$$Var(X) = E(X-\mu)^2 = \int_{-\infty}^{\infty} (x-\mu)^2f(x)dx$$

#### 누적분포함수 (CDF: Cumulative Density Funcntion)


### 정규분포

$$
f(x) = \frac{1}{\sqrt{2\pi\sigma}}e^{-\frac{1}{2\sigma^2}(x-\mu)^2},\; -\infty < x < \infty,\; -\infty < \mu < \infty
$$