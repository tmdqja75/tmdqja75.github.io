---
layout: post
title: 통계 - 가설 검증
description: >
    
image: https://images.unsplash.com/photo-1609017909889-d7b582c072f7?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1469&q=80
sitemap: false
categories:
  - zerobase
---

* toc
{:toc}

## 가설 검정 (Hypothesis Testing)
- 가설(Hypothesis)은 주어진 사실이나 연구하고자 하는 대상에 대한 주장 또는 추측을 의미합니다.

- 귀무 가설 (Null Hypothesis $$H_0$$)
  - 기존의 사실; 연구 하고자 하는 가설 (대립 가설)과 반대되는 가설 입니다.
- 대립 가설 (Alternative Hypothesis $$H_1$$)
  - 대립 가설은 주장하고자 하는 가설/연구하고자 하는 목적으로 귀무가설과 반대됩니다.

## 오류의 종류
- 제 1종 오류 (Type I Error)
  - 귀무가설을 채택해야 하지만, 귀무가설을 기각하는 오류
  - 제 1종 오류를 범할 확률의 최대허용 한계를 유의수준이라 하고, $$\alpha$$라고 표시합니다.
- 제 2종 오류 (Type II Error)
  - 귀무가설을 기각해야 하지만, 귀무가설을 채택하는 오류
- 검정 통계량
  - 귀무가설이 참이라는 가정하에 얻은 통계량
- P-value
  - 귀무가설이 참일 확률
  - 0-1사이 표준화된 지표
  - 귀무가설이 참이라는 가정하에 통계량이 귀무가설을 얼마나 지지하는지를 나타내는 확률입니다.
- 기각역(reject region)
  - 귀무가설을 기각시키는 검정통계량의 관측값의 영역

## 가설 검정의 절차
1. 가설 수립 ($$H_0,\; H_1$$)
2. 유의수준($$\alpha$$) 정의
3. 기각역 설정
4. 검정통계량 계산
5. 의사 결정
  
## 양측검정과 단측검정
- 양측 검정(two-side test)
  - 대립 가설($$H_1$$)의 내용이 차이가 있다는 주장을 할 때 쓰는 검정 방식입니다.
    - 예를 들어, A회사와 B회사의 연봉에는 차이가 있는지 없는지를 확인할 때 양측검증을 활용할 수 있겠습니다.
- 단측 검정(one-side test)
  - 대립가설의 내용의 크고 작음을 비교할 때는 단측 검증을 활용합니다.
    - 예를 들어, A회사의 연봉이 B회사의 연봉보다 크다/작다를 검정할때는 단축 검정을 쓸 수 있습니다.
- 

![side test](http://www.mathnstuff.com/math/spoken/here/2class/90/htest2.gif)
출저: [Middle Ground](http://www.mathnstuff.com/math/spoken/here/2class/90/htest2.gif)

## 단일 표본에 대한 가설 검정
