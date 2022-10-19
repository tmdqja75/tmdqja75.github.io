---
layout: post
title: 파이썬 - 자료구조 1
description: >
    
# image: 
sitemap: false
categories:
---

* 
{:toc}

## 파이썬의 자료구조
- 컨테이너 자료형: 여러 데이터가 묶여 있는 자료형
- 데이터 구조: 각 자료들을 묶어서 관리할 수 있습니다

### 파이썬 자료구조 종류
  - 리스트 (list)
  - 튜플 (tuple)
  - 딕셔너리 (dictionary)
  - 세트 (set)

## 리스트 (List)
- `[ ]`를 이용해 선언합니다
- 리스트 내에는 서로 다른 자료 타입을 저장할 수 있습니다.
- 리스트에 또 다른 컨테이너 자료형을 저장할 수도 있습니다
- 리스트 내에 자료들을 삽입, 삭제, 또는 수정할 수 있습니다. (Mutable)

### 리스트 요소 조회
- 리스트 내 요소(element)를 조회할 떄는 인덱스(index)를 사용하여 조회합니다
  - 인덱스는 리스트가 생성되면 각 요소에 자동으로 부여되는 자리 번호입니다.
  - 인덱스는 항상 0에서 시작합니다.
```python
lst = ['cat', 'dog', 'mouse', 'snake']
print(f'first element: {lst[0]}')
print(f'third element: {lst[2]}')
print(f'fifth element: {lst[4]}')
```
```zsh
first element: cat
third element: mouse
IndexError: list index out of range!
```

### 리스트 길이
- 리스트의 길이는 `len()`함수를 이용하여 구합니다.
```python
lst = ['cat', 'dog', 'mouse', 'snake']
print(f'length of list: {len(lst)}')
```
```bash
length of list: 4
```
- `len()`함수로 문자열의 길이도 구할 수 있습니다.


### `enumerate()`함수
- `enumerate()`함수는 인덱스와 요소를 한번에 조회할 수 있습니다.
```python
lst = ['cat', 'dog', 'mouse', 'snake']
for idx, value in enumerate(lst):
    print(f'{idx}: {value}')
```
```bash
0: cat
1: dog
2: mouse
3: snake
```

### 리스트에 요소 추가/삭제
- 리스트 끝에 요소 추가는 `append()`함수를 사용합니다
- 리스트 중간에 요소 추가는 `insert(idx)`함수를 사용합니다.
  - 삽입하고 싶은 자리의 인덱스 값을 `idx`에 넣어줍니다.
  - 삽입한 인덱수 뒤에 있는 값들을 한 인덱스씩 밀려납니다.
- 리스트에서 마지막 인덱스에 있는 값을 삭제하려면 `pop()`를 사용합니다.
  - `pop()`에 인덱스 값을 넣어주면 (`pop(2)`) 삽입된 인덱스 값에 있는 요소가 삭제됩니다. 
- 리스트의 특정 요소를 삭제하려면, `remove(element)`함수를 사용하여 특정 요소를 삭제합니다
  - `remove(element)`는 리스트에서 처음 나오는 `element`만 지울 수 있습니다. 모든 특정 요소를 지우려면, while 문을 활용하여 지울 수 있습니다.
    ```python
    lst = ['cat', 'dog', 'mouse', 'dog', 'snake']
    while 'dog' in lst:
        lst.remove('dog')
    print(lst)
    ```
    ```bash
    ['cat', 'mouse', 'snake']
    ```

### 리스트에 다른 리스트 연결하기
- 덧셈 연산을 이용하여 리스트를 연결하면, 기존 리스트는 변하지 않고 연결된 리스트는 새 리스트로 생성됩니다.
```python
lst1 = ['cat', 'dog', 'mouse']
lst2 = ['dog', 'mouse', 'snake']
result = lst1 + lst2
print(result)
print(lst1)
print(lst2)
```
```bash
['cat', 'dog', 'mouse', 'dog', 'mouse', 'snake']
['cat', 'dog', 'mouse']
['dog', 'mouse', 'snake']
```
- `extend()`를 활용하면, 함수를 적용하는 리스트 자체를 변형시킵니다.
```python
lst1 = ['cat', 'dog', 'mouse']
lst2 = ['dog', 'mouse', 'snake']
lst1.extend(lst2)
print(lst1)
print(lst2)
```
```bash
['cat', 'dog', 'mouse', 'dog', 'mouse', 'snake']
['dog', 'mouse', 'snake']
```

### 리스트 요소 정렬
- `sort()`함수로 간단히 리스트를 정렬할 수 있습니다.
  - 기본적으로 오름차순으로 정렬하지만, `sort(reverse=True)`를 쓰면, 내림차순으로 정렬할 수 있습니다.
```python
lst = ['cat', 'dog', 'mouse', 'dog', 'mouse', 'snake']
print(f'unsorted list: {lst}') 
lst.sort()
print(f'sorted list: {lst}') 
lst.sort(reverse=True)
print(f'reversed sorted list: {lst})
```
```bash
unsorted list: ['cat', 'dog', 'mouse', 'dog', 'mouse', 'snake']
sorted list: ['cat', 'dog', 'dog', 'mouse', 'mouse', 'snake']
reversed sorted list: ['snake', 'mouse', 'mouse', 'dog', 'dog', 'cat']
```
- 리스트 요소의 순서를 (정렬하지 않고) 뒤집으려면 `reverse()`를 사용하면 됩니다.
```python
lst = ['cat', 'dog', 'mouse', 'dog', 'mouse', 'snake']
lst.reverse()
print(f'reversed list: {lst}')
```
```bash
reversed list: ['snake', 'mouse', 'dog', 'mouse', 'dog', 'cat']
```
### 리스트 슬라이싱
- `lst[n:m]`을 사용하면, 인덱스 n에 있는 요소부터 인덱스 m-1까지 사이에 있는 요소들을 슬라이싱 할 수 있습니다.
- 슬라이싱 인덱스에서 앞 숫자나 뒷 숫자를 생략할 수 있습니다.
  - 앞 숫자를 생략하면(`lst[:m]`), 리스트 맨 처음부터 m-1까지 슬라이싱 합니다.
  - 뒷 숫자를 생략하면(`lst[n:]`), n부터 리스트 끝까지 슬라이싱 합니다.
- n과 m에 음수를 넣을 수도 있습니다.
  - 음수를 넣으면 리스트의 마지막 부터 인덱스를 셉니다.

## 튜플
- `( )`를 사용하여 선언합니다.
- 튜플은 한번 생성되면, 리스트처럼 요소 수정, 삭제가 불가능합니다. (Immutable)
- 리스트와 비슷한 점이 많습니다.
  - 서로 다른 자료 타입을 저장할 수 있고, 또 다른 컨테이너 자료형을 저장할 수도 있습니다
  - 인덱싱도 리스트와 같이 0에서 시작하고, `tup[n]`로 인덱싱을 합니다.
  - `len()`로 튜플의 길이를 구할 수 있습니다
  - 

### `in`, `not in`
- 튜플에 특정 요소가 존재하는지 확인하는 키워드입니다.
```python
animalTuple = ('cat', 'dog', 'mouse', 'snake')
print('cat' in animalTuple)
print('fish' in animalTuple)
``` 
```bash
True
False
```
- 두 키워드는 문자열에도 적용이 가능합니다.
```python
sentence = 'the quick fox jumped over the brown box'
print('fox' in sentence)
print('over' not in sentence)
```
```bash
True
False
```

### 튜플 결합
- 리스트와 같이 덧셈 연산을 활용하여 두 튜플을 결합하여 새 튜플을 만들 수 있습니다.
- 하지만 리스트와 다르게 튜플에서는 `extend()`를 사용해서 튜플을 결합할 수 없습니다.
  - 튜플은 한번 생성되면 수정될 수 없기 떄문에, extend()를 사용하면 튜플에서는 쓸 수 없다는 에러가 발생합니다.

### 튜플 슬라이싱
- 리스트와 같은 방식으로 슬라이싱이 가능합니다. (참조: [리스트 슬라이싱](###리스트-슬라이싱))
- 슬라이싱한 결과는 튜플 형식으로 반환됩니다.
- 