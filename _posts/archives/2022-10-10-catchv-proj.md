---
layout: post
title: 딥러닝 Embedding을 이용한 디지털 성범죄 피해자 지원 프로그램
description: >

image: https://arsfutura-production.s3.us-east-1.amazonaws.com/magazine/2019/10/face_recognition/facenet-brki.png
sitemap: false
categories:
    - projects
---

* tableofcontents
{:toc}

## 목적
- 인터넷에 불법으로 배포된 피해자의 영상의 주소 색출해내기

## 주요 업무
- 동영상에 있는 얼굴들을 추출 후 사용자의 얼굴이 있는지를 확인하는 방법 연구
- 얼굴 인식 결과 배포할 REST API 만들기

## 과정
1. 모델
   1. 다양한 얼굴 인식 모델을 손쉽게 활용할 수 있는 [DeepFace](https://github.com/serengil/deepface) 라이브러리를 이용한 얼굴 인식
2. 효율성
   1. 기존 방식 (for문으로 각 얼굴의 cosine distance 비교)대신 numpy를 활용한 병렬적 처리로 얼굴 인식 속도 개선

## 개발 일지
- [노션 개발일지](https://temporal-willow-a60.notion.site/Final-Project-df6eb6baf8eb408ea54451401dbedcaa)

## 결과

{% include youtubePlayer.html id="7mfoPNcYGiA" %}{:.centered}
<p align = "center">
프로젝트 결과물
</p>

<object data="/assets/1_catchv.pdf" width="1000" height="1000" type='application/pdf'></object>