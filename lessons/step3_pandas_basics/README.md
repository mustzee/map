# Step 3: Pandas 기초

## 학습 목표
- Pandas 라이브러리의 기본 개념 이해
- Series와 DataFrame 생성 및 조작
- 데이터 선택 및 필터링
- 기본 통계 함수 활용

## 1. Pandas란?

Pandas는 데이터 분석을 위한 Python 라이브러리입니다.
- Series: 1차원 데이터 구조
- DataFrame: 2차원 테이블 데이터 구조

```python
import pandas as pd
```

## 2. Series 생성 및 활용

Series는 인덱스가 있는 1차원 배열입니다.

```python
# 리스트로 생성
s = pd.Series([1, 2, 3, 4, 5])
print(s)
# 0    1
# 1    2
# 2    3
# 3    4
# 4    5

# 인덱스 지정
s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print(s)
# a    10
# b    20
# c    30

# 딕셔너리로 생성
data = {'apple': 100, 'banana': 200, 'cherry': 300}
s = pd.Series(data)
print(s)
# apple     100
# banana    200
# cherry    300
```

### Series 접근

```python
s = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])

# 인덱스로 접근
print(s['a'])        # 10
print(s[['a', 'c']]) # 여러 개 선택

# 위치로 접근
print(s[0])          # 10
print(s[1:3])        # b와 c

# 조건으로 필터링
print(s[s > 20])     # 20보다 큰 값들
```

### Series 연산

```python
s = pd.Series([1, 2, 3, 4])

print(s + 10)        # 모든 값에 10 더하기
print(s * 2)         # 모든 값에 2 곱하기
print(s ** 2)        # 제곱

# 통계 함수
print(s.sum())       # 합계
print(s.mean())      # 평균
print(s.max())       # 최댓값
print(s.min())       # 최솟값
print(s.std())       # 표준편차
```

## 3. DataFrame 생성

DataFrame은 행과 열이 있는 2차원 테이블입니다.

```python
# 딕셔너리로 생성
data = {
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'city': ['Seoul', 'Busan', 'Daegu']
}
df = pd.DataFrame(data)
print(df)
#       name  age   city
# 0    Alice   25  Seoul
# 1      Bob   30  Busan
# 2  Charlie   35  Daegu

# 리스트의 리스트로 생성
data = [
    ['Alice', 25, 'Seoul'],
    ['Bob', 30, 'Busan'],
    ['Charlie', 35, 'Daegu']
]
df = pd.DataFrame(data, columns=['name', 'age', 'city'])

# CSV 파일에서 읽기
df = pd.read_csv('data.csv')
```

## 4. DataFrame 기본 정보

```python
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
})

# 기본 정보
print(df.shape)      # (3, 3) - 행, 열 개수
print(df.columns)    # Index(['A', 'B', 'C']) - 열 이름
print(df.index)      # RangeIndex(start=0, stop=3, step=1)
print(df.dtypes)     # 각 열의 데이터 타입

# 데이터 미리보기
print(df.head())     # 처음 5개 행
print(df.tail())     # 마지막 5개 행

# 통계 요약
print(df.describe()) # 수치형 열의 통계 요약
print(df.info())     # DataFrame 정보
```

## 5. 데이터 선택

### 열 선택

```python
df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'city': ['Seoul', 'Busan', 'Daegu']
})

# 단일 열 (Series 반환)
print(df['name'])

# 여러 열 (DataFrame 반환)
print(df[['name', 'age']])
```

### 행 선택

```python
# 인덱스로 선택 (iloc: 위치 기반)
print(df.iloc[0])        # 첫 번째 행
print(df.iloc[0:2])      # 첫 두 행
print(df.iloc[[0, 2]])   # 첫 번째와 세 번째 행

# 레이블로 선택 (loc: 레이블 기반)
print(df.loc[0])         # 인덱스 0인 행
print(df.loc[0:1])       # 인덱스 0부터 1까지
```

### 특정 값 선택

```python
# 행, 열 모두 지정
print(df.loc[0, 'name'])      # 'Alice'
print(df.iloc[0, 0])          # 'Alice'
print(df.loc[0:1, ['name', 'age']])  # 여러 행과 열
```

## 6. 조건 필터링

```python
df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie', 'David'],
    'age': [25, 30, 35, 28],
    'score': [85, 90, 75, 95]
})

# 단일 조건
print(df[df['age'] > 28])

# 여러 조건 (AND: &, OR: |)
print(df[(df['age'] > 25) & (df['score'] >= 85)])
print(df[(df['age'] < 30) | (df['score'] > 90)])

# isin: 특정 값들 포함 여부
print(df[df['name'].isin(['Alice', 'Charlie'])])
```

## 7. 새 열 추가 및 수정

```python
df = pd.DataFrame({
    'name': ['Alice', 'Bob'],
    'age': [25, 30]
})

# 새 열 추가
df['city'] = ['Seoul', 'Busan']
df['score'] = [85, 90]

# 계산으로 새 열 추가
df['age_plus_10'] = df['age'] + 10

# 조건으로 새 열 추가
df['adult'] = df['age'] >= 20

print(df)
```

## 8. 정렬

```python
df = pd.DataFrame({
    'name': ['Charlie', 'Alice', 'Bob'],
    'age': [35, 25, 30],
    'score': [75, 85, 90]
})

# 단일 열로 정렬
df_sorted = df.sort_values('age')
df_sorted = df.sort_values('age', ascending=False)  # 내림차순

# 여러 열로 정렬
df_sorted = df.sort_values(['age', 'score'])

# 인덱스로 정렬
df_sorted = df.sort_index()
```

## 9. 기본 통계 함수

```python
df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [10, 20, 30, 40, 50]
})

# 열별 통계
print(df['A'].sum())      # A 열의 합
print(df['A'].mean())     # A 열의 평균
print(df['A'].max())      # A 열의 최댓값

# 전체 DataFrame 통계
print(df.sum())           # 각 열의 합
print(df.mean())          # 각 열의 평균
print(df.describe())      # 통계 요약

# 행별 연산 (axis=1)
print(df.sum(axis=1))     # 각 행의 합
print(df.mean(axis=1))    # 각 행의 평균
```

## 연습 문제

이제 `exercises/step3_exercises.py` 파일을 열어 연습 문제를 풀어보세요!

다음 명령어로 채점할 수 있습니다:
```bash
pytest tests/test_step3.py -v
```
