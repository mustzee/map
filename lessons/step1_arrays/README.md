# Step 1: Python 리스트와 배열 기초

## 학습 목표
- Python 리스트의 기본 개념 이해
- 리스트 생성, 인덱싱, 슬라이싱 방법 학습
- 리스트 메서드 활용
- 리스트 컴프리헨션 이해

## 1. 리스트 생성

Python의 리스트는 대괄호 `[]`를 사용하여 생성합니다.

```python
# 빈 리스트
empty_list = []

# 숫자 리스트
numbers = [1, 2, 3, 4, 5]

# 문자열 리스트
fruits = ['apple', 'banana', 'cherry']

# 혼합 타입 리스트
mixed = [1, 'hello', 3.14, True]

# range를 사용한 리스트
numbers = list(range(1, 11))  # [1, 2, 3, ..., 10]
```

## 2. 인덱싱 (Indexing)

리스트의 각 요소는 인덱스로 접근할 수 있습니다. 인덱스는 0부터 시작합니다.

```python
fruits = ['apple', 'banana', 'cherry', 'date']

# 양수 인덱스 (앞에서부터)
print(fruits[0])   # 'apple'
print(fruits[1])   # 'banana'

# 음수 인덱스 (뒤에서부터)
print(fruits[-1])  # 'date' (마지막 요소)
print(fruits[-2])  # 'cherry' (뒤에서 두 번째)
```

## 3. 슬라이싱 (Slicing)

슬라이싱은 리스트의 일부분을 추출하는 방법입니다.

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 기본 슬라이싱: [시작:끝]
print(numbers[2:5])    # [2, 3, 4] (5는 포함 안 됨)
print(numbers[:3])     # [0, 1, 2] (처음부터 3까지)
print(numbers[7:])     # [7, 8, 9] (7부터 끝까지)

# 스텝을 포함한 슬라이싱: [시작:끝:스텝]
print(numbers[::2])    # [0, 2, 4, 6, 8] (2칸씩)
print(numbers[1::2])   # [1, 3, 5, 7, 9] (홀수만)
print(numbers[::-1])   # [9, 8, 7, ..., 0] (역순)
```

## 4. 리스트 메서드

```python
numbers = [1, 2, 3]

# 요소 추가
numbers.append(4)        # [1, 2, 3, 4]
numbers.extend([5, 6])   # [1, 2, 3, 4, 5, 6]
numbers.insert(0, 0)     # [0, 1, 2, 3, 4, 5, 6]

# 요소 제거
numbers.remove(0)        # 첫 번째 0 제거
last = numbers.pop()     # 마지막 요소 제거 및 반환
numbers.pop(0)           # 인덱스 0 요소 제거

# 정렬
numbers.sort()           # 오름차순 정렬
numbers.sort(reverse=True)  # 내림차순 정렬
numbers.reverse()        # 순서 뒤집기

# 기타
count = numbers.count(3)     # 3의 개수
index = numbers.index(5)     # 5의 인덱스
numbers.clear()              # 모든 요소 제거
```

## 5. 리스트 연산

```python
# 리스트 합치기
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2  # [1, 2, 3, 4, 5, 6]

# 리스트 반복
repeated = [1, 2] * 3     # [1, 2, 1, 2, 1, 2]

# 길이
length = len(list1)       # 3

# 최대/최소/합계
numbers = [1, 5, 3, 9, 2]
print(max(numbers))       # 9
print(min(numbers))       # 1
print(sum(numbers))       # 20
```

## 6. 리스트 컴프리헨션

리스트 컴프리헨션은 간결하게 리스트를 생성하는 방법입니다.

```python
# 기본 형태
squares = [x**2 for x in range(10)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 조건 포함
evens = [x for x in range(20) if x % 2 == 0]
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# 변환
fruits = ['apple', 'banana', 'cherry']
upper_fruits = [fruit.upper() for fruit in fruits]
# ['APPLE', 'BANANA', 'CHERRY']

# 중첩 리스트 평탄화
matrix = [[1, 2], [3, 4], [5, 6]]
flat = [num for row in matrix for num in row]
# [1, 2, 3, 4, 5, 6]
```

## 7. 2차원 리스트 (행렬)

```python
# 2차원 리스트 생성
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# 접근
print(matrix[0][0])  # 1
print(matrix[1][2])  # 6

# 반복문으로 순회
for row in matrix:
    for element in row:
        print(element, end=' ')
    print()
```

## 연습 문제

이제 `exercises/step1_exercises.py` 파일을 열어 연습 문제를 풀어보세요!

다음 명령어로 채점할 수 있습니다:
```bash
pytest tests/test_step1.py -v
```
