---
layout: post
title: Python 중급
description: >
    
# image: 
sitemap: false
categories:
  - zerobase
---

* 
{:toc}

## 컴파일러와 인터프리터
- 컴파일러: 개발자가 작성한 코드를 컴퓨터가 이해할 수 있는 실팽파일(기계어)로 바꿔주는 것
	- 소스파일 -> 기계어
- 인터프리터: 실행파일을 만들지 않고 실행할 때 소스 코드를 바로 기계어로 번역함

## 데이터와 메모리
- 데이터: 숫자, 문자, 이미지, 동영상, 등 -> 데이터를 수집, 가공하면 정보로 변환됨
- 메모리: 데이터를 탑재
- 실행

## 변수 (Variable)
## 인수와 매개변수
- 인수 (parameter)
- 매개변수 (arguement): 호출과 선언부의 관계를 맺어주는 변수
- 인수와 매개변수의 갯수는 일치해야 한다
- 매개변수의 개수가 정해지지 않았으면 `*`을 사용해 매개변수를 선언한다.

## 함수

### 중첩함수
- 파이썬에서는 함수 내부에 필요한 함수를 따로 선언할 수 있다.
- 함수 내어세 선언된 중첩함수는 함수 밖에서 사용할 수 없다.
```python
def out_func():
    print('outfunc')

    def in_func():
        print('a')
    in_func()
out_func()
in_func()
```
```
>>> outfunc
>>> a
>>> NameError: name 'in_func' is not defined.
```

### lambda 함수
- 간단한 함수는 lambda함수를 활용하면 더 간결히 선언할 수 있다.
```python
def addition(a, b):
    return a + b
```

- 두 수를 더해주는 `addition`이라는 함수를 다음과 같이 lambda 함수로 나타낼 수 있다.
```python
addition = lambda a, b: a + b
```

- lambda 함수를 호출할 땐 일반 함수를 불러올 때와 같은 방식으로 호출할 수 있다.
```python
addition(2, 3)
>>> 5
``` 

## 모듈
- 모듈은 파이썬에서 자주 쓰이는 함수들을 손쉽게 사용하도록 미리 설계되어 있는 코드들이다.
- 3가지 모듈 구분
    1. 내부 모듈: 파이썬 내부에 내장되어 있는 모듈
    2. 외부 모듈: 외부 다른 개발자가 미리 만들어 놓은 모듈 (개인 코드에 가져와서 사용 가능)
    3. 사용자 모듈: 사용자가 직접 설계해서 사용하는 모듈
- 주요 문법
    - `import`: 모듈을 불러옴
    ```python
    import numpy
    ```
    - `as`: 모듈 이름을 변형해서 불러올 수 있다
    ```python
    import numpy as np
    ```
    - `from ~ import`: 모듈에서 특정 기능이나 함수를 불러올 때 사용
    ```python
    from numpy import array
    ```

## `__name__` 전역변수
- `__name__`은 사용자가 지정하는 변수가 아니라 파이썬에서 기본적으로 탑재되에 있는 전역변수
- 해당 모듈의 파일명이 `__name__`변수에 저장됨
- 단 직접 실행되는 파일에는 `__name__`에 `__main__`이라는 값이 저장된다.

    - 실행파일이란?
      - 다음과 같은 파일구조가 있다면, 
        ![filestruct](/mygitblog/assets/img/filestruct.jpeg)

