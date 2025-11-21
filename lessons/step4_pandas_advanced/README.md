# Step 4: Pandas 데이터 처리

## 학습 목표
- 결측치(missing values) 처리
- 데이터 그룹화 및 집계
- 데이터 병합 및 조인
- 데이터 변환 및 정제

## 1. 결측치 처리

### 결측치 확인

```python
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'A': [1, 2, np.nan, 4],
    'B': [5, np.nan, np.nan, 8],
    'C': [9, 10, 11, 12]
})

# 결측치 확인
print(df.isnull())       # True/False로 표시
print(df.isnull().sum()) # 각 열의 결측치 개수
print(df.notnull())      # 결측치가 아닌 것
```

### 결측치 처리

```python
# 결측치 제거
df_dropped = df.dropna()           # 결측치가 있는 행 제거
df_dropped = df.dropna(axis=1)     # 결측치가 있는 열 제거

# 결측치 채우기
df_filled = df.fillna(0)           # 0으로 채우기
df_filled = df.fillna(df.mean())   # 평균으로 채우기
df_filled = df.fillna(method='ffill')  # 앞의 값으로 채우기
df_filled = df.fillna(method='bfill')  # 뒤의 값으로 채우기

# 특정 열만 채우기
df['A'] = df['A'].fillna(0)
```

## 2. 중복 데이터 처리

```python
df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Alice', 'Charlie'],
    'age': [25, 30, 25, 35]
})

# 중복 확인
print(df.duplicated())         # 중복 여부 (True/False)
print(df.duplicated().sum())   # 중복 개수

# 중복 제거
df_unique = df.drop_duplicates()
df_unique = df.drop_duplicates(subset=['name'])  # 특정 열 기준
```

## 3. 그룹화 (GroupBy)

그룹화는 데이터를 특정 기준으로 나누고 각 그룹별로 연산을 수행합니다.

```python
df = pd.DataFrame({
    'team': ['A', 'A', 'B', 'B', 'A'],
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'score': [80, 90, 85, 95, 88]
})

# 그룹별 평균
print(df.groupby('team')['score'].mean())
# team
# A    86.0
# B    90.0

# 그룹별 합계
print(df.groupby('team')['score'].sum())

# 그룹별 여러 통계량
print(df.groupby('team').agg({
    'score': ['mean', 'sum', 'max', 'min', 'count']
}))

# 여러 열로 그룹화
df = pd.DataFrame({
    'team': ['A', 'A', 'B', 'B'],
    'position': ['F', 'D', 'F', 'D'],
    'score': [80, 90, 85, 95]
})
print(df.groupby(['team', 'position'])['score'].mean())
```

## 4. 데이터 병합

### concat: 데이터 연결

```python
df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})

# 수직 연결 (행 추가)
result = pd.concat([df1, df2])
#    A  B
# 0  1  3
# 1  2  4
# 0  5  7
# 1  6  8

# 수평 연결 (열 추가)
result = pd.concat([df1, df2], axis=1)
```

### merge: SQL 스타일 조인

```python
left = pd.DataFrame({
    'key': ['A', 'B', 'C'],
    'value': [1, 2, 3]
})

right = pd.DataFrame({
    'key': ['A', 'B', 'D'],
    'score': [90, 80, 70]
})

# Inner join (교집합)
result = pd.merge(left, right, on='key')
#   key  value  score
# 0   A      1     90
# 1   B      2     80

# Left join
result = pd.merge(left, right, on='key', how='left')

# Right join
result = pd.merge(left, right, on='key', how='right')

# Outer join (합집합)
result = pd.merge(left, right, on='key', how='outer')
```

## 5. 데이터 변환

### apply: 함수 적용

```python
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
})

# 열에 함수 적용
df['A_squared'] = df['A'].apply(lambda x: x ** 2)

# 여러 열에 함수 적용
def custom_func(row):
    return row['A'] + row['B']

df['sum'] = df.apply(custom_func, axis=1)
```

### map: Series 변환

```python
df = pd.DataFrame({
    'grade': ['A', 'B', 'C', 'A']
})

# 딕셔너리로 매핑
grade_map = {'A': 90, 'B': 80, 'C': 70}
df['score'] = df['grade'].map(grade_map)
```

### replace: 값 치환

```python
df = pd.DataFrame({
    'A': [1, 2, 3, 1, 2]
})

# 특정 값 치환
df['A'] = df['A'].replace(1, 10)

# 여러 값 치환
df['A'] = df['A'].replace({1: 10, 2: 20})
```

## 6. 문자열 처리

```python
df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie']
})

# 대소문자 변환
df['upper'] = df['name'].str.upper()
df['lower'] = df['name'].str.lower()

# 문자열 포함 확인
mask = df['name'].str.contains('li')

# 문자열 길이
df['length'] = df['name'].str.len()

# 문자열 분할
df['first_char'] = df['name'].str[0]
```

## 7. 피벗 테이블

```python
df = pd.DataFrame({
    'date': ['2024-01', '2024-01', '2024-02', '2024-02'],
    'team': ['A', 'B', 'A', 'B'],
    'score': [80, 90, 85, 95]
})

# 피벗 테이블
pivot = df.pivot_table(
    values='score',
    index='date',
    columns='team',
    aggfunc='mean'
)
```

## 연습 문제

이제 `exercises/step4_exercises.py` 파일을 열어 연습 문제를 풀어보세요!

다음 명령어로 채점할 수 있습니다:
```bash
pytest tests/test_step4.py -v
```
