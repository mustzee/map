# Step 2: NumPy 배열

## 학습 목표
- NumPy 라이브러리의 기본 개념 이해
- NumPy 배열 생성 및 조작
- 배열 연산 및 브로드캐스팅
- 배열 인덱싱 및 슬라이싱
- 통계 함수 활용

## 1. NumPy란?

NumPy(Numerical Python)는 Python에서 수치 계산을 위한 핵심 라이브러리입니다.
- 강력한 N차원 배열 객체
- 빠른 배열 연산
- 선형대수, 통계 함수 제공

```python
import numpy as np
```

## 2. NumPy 배열 생성

```python
# 리스트에서 생성
arr1 = np.array([1, 2, 3, 4, 5])
print(arr1)  # [1 2 3 4 5]

# 2차원 배열
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2d)
# [[1 2 3]
#  [4 5 6]]

# 특수 배열 생성
zeros = np.zeros((3, 4))        # 0으로 채워진 3x4 배열
ones = np.ones((2, 3))          # 1로 채워진 2x3 배열
full = np.full((2, 2), 7)       # 7로 채워진 2x2 배열
identity = np.eye(3)            # 3x3 단위 행렬

# 범위 배열
range_arr = np.arange(0, 10, 2)    # [0 2 4 6 8]
linspace = np.linspace(0, 1, 5)    # [0. 0.25 0.5 0.75 1.]

# 랜덤 배열
random_arr = np.random.rand(3, 3)        # 0~1 사이 난수
random_int = np.random.randint(0, 10, 5) # 0~9 사이 정수 5개
```

## 3. 배열 속성

```python
arr = np.array([[1, 2, 3], [4, 5, 6]])

print(arr.shape)      # (2, 3) - 배열의 형태
print(arr.size)       # 6 - 전체 요소 개수
print(arr.ndim)       # 2 - 차원 수
print(arr.dtype)      # int64 - 데이터 타입
```

## 4. 배열 인덱싱과 슬라이싱

```python
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# 인덱싱
print(arr[0])      # 0
print(arr[-1])     # 9

# 슬라이싱
print(arr[2:5])    # [2 3 4]
print(arr[::2])    # [0 2 4 6 8]
print(arr[::-1])   # [9 8 7 6 5 4 3 2 1 0]

# 2차원 배열 인덱싱
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2d[0, 0])     # 1
print(arr2d[1, 2])     # 6
print(arr2d[:2, :2])   # [[1 2] [4 5]]

# 불린 인덱싱
arr = np.array([1, 2, 3, 4, 5])
mask = arr > 3
print(arr[mask])       # [4 5]
print(arr[arr % 2 == 0])  # [2 4]
```

## 5. 배열 연산

```python
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# 기본 연산 (요소별)
print(arr1 + arr2)    # [5 7 9]
print(arr1 - arr2)    # [-3 -3 -3]
print(arr1 * arr2)    # [4 10 18]
print(arr1 / arr2)    # [0.25 0.4 0.5]
print(arr1 ** 2)      # [1 4 9]

# 스칼라 연산
print(arr1 + 10)      # [11 12 13]
print(arr1 * 2)       # [2 4 6]

# 배열 간 비교
print(arr1 > 2)       # [False False True]
print(arr1 == arr2)   # [False False False]
```

## 6. 브로드캐스팅

크기가 다른 배열 간의 연산을 자동으로 처리합니다.

```python
# 1차원 배열과 스칼라
arr = np.array([1, 2, 3])
print(arr + 10)  # [11 12 13]

# 2차원과 1차원
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
arr1d = np.array([10, 20, 30])
print(arr2d + arr1d)
# [[11 22 33]
#  [14 25 36]]
```

## 7. 유용한 배열 함수

```python
arr = np.array([3, 1, 4, 1, 5, 9, 2, 6])

# 통계 함수
print(np.sum(arr))      # 31 - 합계
print(np.mean(arr))     # 3.875 - 평균
print(np.median(arr))   # 3.5 - 중앙값
print(np.std(arr))      # 2.52 - 표준편차
print(np.min(arr))      # 1 - 최솟값
print(np.max(arr))      # 9 - 최댓값

# 정렬
sorted_arr = np.sort(arr)        # [1 1 2 3 4 5 6 9]
indices = np.argsort(arr)        # 정렬된 인덱스

# 집계
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print(np.sum(arr2d, axis=0))     # [5 7 9] - 열 합계
print(np.sum(arr2d, axis=1))     # [6 15] - 행 합계

# 배열 형태 변경
arr = np.array([1, 2, 3, 4, 5, 6])
reshaped = arr.reshape(2, 3)     # 2x3으로 변경
flattened = reshaped.flatten()   # 1차원으로 평탄화
```

## 8. 배열 결합

```python
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# 수평 결합
hstack = np.hstack([arr1, arr2])  # [1 2 3 4 5 6]
concatenate = np.concatenate([arr1, arr2])  # [1 2 3 4 5 6]

# 수직 결합
vstack = np.vstack([arr1, arr2])
# [[1 2 3]
#  [4 5 6]]
```

## 9. 조건 연산

```python
arr = np.array([1, 2, 3, 4, 5])

# where: 조건에 따라 값 선택
result = np.where(arr > 3, 'big', 'small')
# ['small' 'small' 'small' 'big' 'big']

# 숫자 선택
result = np.where(arr > 3, arr * 2, arr)
# [1 2 3 8 10]
```

## 연습 문제

이제 `exercises/step2_exercises.py` 파일을 열어 연습 문제를 풀어보세요!

다음 명령어로 채점할 수 있습니다:
```bash
pytest tests/test_step2.py -v
```
