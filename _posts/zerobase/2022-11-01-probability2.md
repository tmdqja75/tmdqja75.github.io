---
layout: post
title: 통계 - 확률
description: >
    
image: https://images.unsplash.com/photo-1609017909889-d7b582c072f7?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1469&q=80
sitemap: false
categories:
  - zerobase
---

* tableofcontents
{:toc}


## 확률
- 확률은 모든 경우에서 특정 사건이 발생하는 비율을 의미합니다. 
### 표본공간 (Sample Space)
- 표본공간은 어떤 상황에서 발생할 수 있는 모든 결과들의 집합을 뜻합니다. 
	- 예를 들어 동전 던지기의 표본 공간은 $$S=\{\text{앞면, 뒷면}\}$$이 되고, 주사위 던지기의 경우, 표본 공간은 $$S=\{1, 2, 3, 4, 5, 6\}$$이 됩니다.
- 표본 공간이 주어졌고, 표본 공간 내에 모든 원소들이 일어날 확률이 동일하다면, 사건 A가 일어날 확률은 다음과 같이 표현할 수 있습니다.


$$
P(A)=\frac{\text{사건 $A$가 일어날 원소의 수}}{\text{표본공간 $S$의 원소의 수} }
$$

### 통계적 확률

$$
\lim_{n\rightarrow\infty}\frac{r}{N}
$$

### 확률의 성질
#### 합사건(Union) $$A\cup B$$
- 합사건은 사건 A 또는 사건 B가 일어나는 경우의 집합입니다.

#### 곱사건(Intersection) $$A\cap B$$
- 곱사건은 사건 A와 사건 B가 동시에 일어나는 경우의 집합입니다.

#### 배반사건(Mutually Exclusive Event) $$A\cap B=\emptyset$$
- 배반사건은 사건 A와 사건 B가 동시에 일어날 수 없는 경우를 설명합니다.

#### 여사건(Complement) $$A^c$$
- 여사건은 표본집합에서 사건 A가 일어나지 않는 경우의 사건의 집합입니다.

#### 확률의 법칙
1) 확률의 덧셈법칙

$$
P(A\cup B) = P(A)+P(B)-P(A\cap B)
$$

2) A와 B의 배반사건

$$
P(A\cap B) = P(\emptyset) = 0
$$

3) 여사건

$$
P(A)+P(A^c)=1
$$

### 조건부 확률 (Conditional Probability)

$$
P(B|A) = \frac{P(A \cap B)}{P(A)},\; P(A)\neq 0
$$


