---
layout: post
title: Python 중급 - 예외 처리
description: >
    
# image: 
sitemap: false
categories:
---

* 
{:toc}

## 예외
- 예외는 문법적으로는 문제가 없으나 코드 실행 중에 발생하는 예상하지 못한 문제가 발생했을 때 나타납니다.
- 다음 리스트는 파이썬에서 가능한 예외들을 나열한 리스트입니다.
- **모든 예외 클래스는 파이썬의 기본 Exception클래스를 상속합니다.**

![](../assets/img/zerobase/exceptionclass.png)
출저:[연오의 파이썬](https://python.bakyeono.net/chapter-9-4.html)

## 예외처리
- 코드 실행 중 예외가 발생하게 되면, 파이썬은 코드 전체를 중단시킵니다.
- 코드에 예외가 생겨도 코드가 계속 작동하게 하도록 **예외처리**를 해주는 것이 중요합니다.

### `try`, `except`
- 예외처리는 `try` 와 `except`구문을 사용합니다.
```python
n1 = 10
n2 = 0

try:
    print(n1/n2)
except:
    print("Can't divide by 0!")
```
```
>>> Can't divide by 0!
```

### `else`
- `try, except`다음에 오는 구절이며, `try, except`에서 예외가 발생하지 않으면 실행됩니다.
```python

try:
    num = int(input("Enter number!: "))
except:
    print("Number not entered!")
else:
    print(num)
```
```
>>> "Enter number!: 5 
>>> 5
```

### `finally`
- 전 코드에서 예외가 발생 유무에 상관 없이 `finally`에 속해있는 코드 블록은 무조건 실행됩니다. 

### 예외처리 요약
![tryexcept](../assets/img/zerobase/tryexcept.png){:.centered}

### `raise`
- raise는 코드 중간에 예외를 생성할 때 사용됩니다.
- `try, except`구절 내에서도 사용가능하며, `try`내에서 `raise`로 예외를 생성하면, except에서 그 예외에 맞춰 예외처리를 실행할 수 있습니다.
```python
try:
    if s == 0:
        raise 
except ValueError:
    raise ValueError("String can't be changed into integer")
```

## 사용자 지정 예외클래스
```python
class NotUseZeroException(Exception)
    def __init__(self, n):
        super().__init__(f"{n}은 사용불가합니다!")
```
- 위 코드처럼, 사용자 지정 예외클래스를 만들기 위해서는 파이썬 기본 `Exception`클래스를 상속해야 합니다. 
- `super().__init__`를 통해 예외가 생겼을 때 출력하는 string을 수정할 수정할 수 있습니다.
- 
