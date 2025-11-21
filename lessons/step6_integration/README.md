# Step 6: Pandas와 데이터베이스 연동

## 학습 목표
- DataFrame을 데이터베이스에 저장
- SQL 쿼리 결과를 DataFrame으로 불러오기
- Pandas와 SQLite를 활용한 데이터 파이프라인 구축

## 1. DataFrame을 SQL 테이블로 저장

Pandas는 DataFrame을 SQL 테이블로 쉽게 저장할 수 있는 기능을 제공합니다.

```python
import pandas as pd
import sqlite3

# DataFrame 생성
df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'score': [85.5, 90.0, 88.5]
})

# 데이터베이스 연결
conn = sqlite3.connect('example.db')

# DataFrame을 테이블로 저장
df.to_sql('students', conn, if_exists='replace', index=False)

conn.close()
```

### to_sql 파라미터

- `name`: 테이블 이름
- `con`: 데이터베이스 연결
- `if_exists`: 테이블이 이미 있을 때 동작
  - `'fail'`: 에러 발생 (기본값)
  - `'replace'`: 기존 테이블 삭제 후 새로 생성
  - `'append'`: 기존 테이블에 데이터 추가
- `index`: 인덱스를 열로 저장할지 여부

```python
# 데이터 추가 (append)
df_new = pd.DataFrame({
    'name': ['David'],
    'age': [28],
    'score': [92.0]
})
df_new.to_sql('students', conn, if_exists='append', index=False)
```

## 2. SQL 테이블을 DataFrame으로 읽기

```python
import pandas as pd
import sqlite3

conn = sqlite3.connect('example.db')

# 전체 테이블 읽기
df = pd.read_sql('SELECT * FROM students', conn)
print(df)

# SQL 쿼리로 읽기
df = pd.read_sql('SELECT name, age FROM students WHERE age > 25', conn)
print(df)

# 테이블 이름만으로 읽기
df = pd.read_sql_table('students', conn)

# SQL 쿼리로 읽기 (별칭)
df = pd.read_sql_query('SELECT * FROM students', conn)

conn.close()
```

## 3. 실전 데이터 파이프라인

### 예제 1: CSV → DataFrame → Database

```python
import pandas as pd
import sqlite3

# 1. CSV 파일 읽기
df = pd.read_csv('data/sales.csv')

# 2. 데이터 정제
df = df.dropna()  # 결측치 제거
df['total'] = df['price'] * df['quantity']  # 새 열 추가

# 3. 데이터베이스에 저장
conn = sqlite3.connect('sales.db')
df.to_sql('sales', conn, if_exists='replace', index=False)

# 4. 확인
result = pd.read_sql('SELECT * FROM sales LIMIT 5', conn)
print(result)

conn.close()
```

### 예제 2: Database → DataFrame → 분석 → Database

```python
import pandas as pd
import sqlite3

conn = sqlite3.connect('sales.db')

# 1. 데이터베이스에서 읽기
df = pd.read_sql('SELECT * FROM sales', conn)

# 2. 데이터 분석
monthly_summary = df.groupby('month').agg({
    'total': ['sum', 'mean'],
    'quantity': 'sum'
})

# 3. 분석 결과를 새 테이블로 저장
monthly_summary.to_sql('monthly_summary', conn, if_exists='replace')

conn.close()
```

## 4. 조건부 데이터 처리

```python
import pandas as pd
import sqlite3

conn = sqlite3.connect('example.db')

# 1. 조건에 맞는 데이터 읽기
df = pd.read_sql('''
    SELECT * FROM students
    WHERE age > 25
    ORDER BY score DESC
''', conn)

# 2. Pandas에서 추가 처리
df['grade'] = pd.cut(df['score'],
                     bins=[0, 60, 80, 100],
                     labels=['C', 'B', 'A'])

# 3. 처리된 데이터를 새 테이블로 저장
df.to_sql('students_graded', conn, if_exists='replace', index=False)

conn.close()
```

## 5. 대용량 데이터 처리

대용량 데이터는 청크(chunk) 단위로 처리합니다.

```python
import pandas as pd
import sqlite3

conn = sqlite3.connect('large_data.db')

# CSV를 청크로 읽어서 데이터베이스에 저장
chunk_size = 1000
for chunk in pd.read_csv('large_file.csv', chunksize=chunk_size):
    # 각 청크를 처리
    chunk = chunk.dropna()

    # 데이터베이스에 추가
    chunk.to_sql('large_table', conn, if_exists='append', index=False)

conn.close()
```

## 6. JOIN 연산

```python
import pandas as pd
import sqlite3

conn = sqlite3.connect('school.db')

# SQL JOIN
df = pd.read_sql('''
    SELECT s.name, s.age, c.course_name, c.grade
    FROM students s
    JOIN courses c ON s.id = c.student_id
''', conn)

# 또는 Pandas merge 사용
students = pd.read_sql('SELECT * FROM students', conn)
courses = pd.read_sql('SELECT * FROM courses', conn)
df = pd.merge(students, courses, left_on='id', right_on='student_id')

conn.close()
```

## 7. 트랜잭션 관리

```python
import pandas as pd
import sqlite3

conn = sqlite3.connect('example.db')

try:
    # 여러 DataFrame 저장
    df1.to_sql('table1', conn, if_exists='replace', index=False)
    df2.to_sql('table2', conn, if_exists='replace', index=False)

    # 성공 시 커밋
    conn.commit()
except Exception as e:
    # 실패 시 롤백
    conn.rollback()
    print(f"Error: {e}")
finally:
    conn.close()
```

## 8. 실전 예제: 데이터 분석 워크플로우

```python
import pandas as pd
import sqlite3
import numpy as np

# 1. 데이터베이스 연결
conn = sqlite3.connect('analytics.db')

# 2. 여러 테이블 읽기
orders = pd.read_sql('SELECT * FROM orders', conn)
customers = pd.read_sql('SELECT * FROM customers', conn)

# 3. 데이터 병합
df = pd.merge(orders, customers, on='customer_id')

# 4. 데이터 정제
df = df.dropna()
df['order_date'] = pd.to_datetime(df['order_date'])

# 5. 분석: 월별 고객별 구매 금액
monthly_customer = df.groupby([
    df['order_date'].dt.to_period('M'),
    'customer_id'
]).agg({
    'amount': 'sum',
    'order_id': 'count'
}).reset_index()

# 6. 결과 저장
monthly_customer.to_sql(
    'monthly_customer_analysis',
    conn,
    if_exists='replace',
    index=False
)

# 7. 요약 통계
summary = pd.read_sql('''
    SELECT *
    FROM monthly_customer_analysis
    ORDER BY amount DESC
    LIMIT 10
''', conn)

print("Top 10 customers by monthly spending:")
print(summary)

conn.close()
```

## 9. 성능 최적화 팁

```python
import pandas as pd
import sqlite3

conn = sqlite3.connect('example.db')

# 1. 필요한 열만 선택
df = pd.read_sql('SELECT name, age FROM students', conn)  # 전체보다 빠름

# 2. WHERE 절로 필터링
df = pd.read_sql('SELECT * FROM students WHERE age > 25', conn)

# 3. 인덱스 활용 (데이터베이스에서)
cursor = conn.cursor()
cursor.execute('CREATE INDEX idx_age ON students(age)')
conn.commit()

# 4. 청크 단위 처리
for chunk in pd.read_sql('SELECT * FROM large_table', conn, chunksize=1000):
    # 청크 처리
    process(chunk)

conn.close()
```

## 연습 문제

이제 `exercises/step6_exercises.py` 파일을 열어 연습 문제를 풀어보세요!

다음 명령어로 채점할 수 있습니다:
```bash
pytest tests/test_step6.py -v
```
