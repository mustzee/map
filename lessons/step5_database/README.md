# Step 5: SQLite 데이터베이스 기초

## 학습 목표
- SQLite 데이터베이스의 기본 개념 이해
- 데이터베이스 연결 및 관리
- SQL 쿼리 작성 (CRUD: Create, Read, Update, Delete)
- 테이블 생성 및 관리

## 1. SQLite란?

SQLite는 서버가 필요 없는 경량 데이터베이스입니다.
- 파일 기반 데이터베이스
- Python 표준 라이브러리에 포함
- 모바일 앱, 소규모 애플리케이션에 적합

```python
import sqlite3
```

## 2. 데이터베이스 연결

```python
import sqlite3

# 데이터베이스 연결 (파일이 없으면 생성)
conn = sqlite3.connect('example.db')

# 메모리 데이터베이스 (임시)
conn = sqlite3.connect(':memory:')

# 커서 생성 (쿼리 실행용)
cursor = conn.cursor()

# 작업 완료 후 닫기
conn.close()
```

## 3. 테이블 생성

```python
import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# 테이블 생성
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        email TEXT UNIQUE
    )
''')

# 변경사항 저장
conn.commit()
conn.close()
```

### 데이터 타입

- `INTEGER`: 정수
- `REAL`: 실수
- `TEXT`: 문자열
- `BLOB`: 바이너리 데이터
- `NULL`: NULL 값

### 제약조건

- `PRIMARY KEY`: 기본 키
- `AUTOINCREMENT`: 자동 증가
- `NOT NULL`: NULL 불가
- `UNIQUE`: 중복 불가
- `DEFAULT`: 기본값

## 4. 데이터 삽입 (INSERT)

```python
import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# 단일 데이터 삽입
cursor.execute('''
    INSERT INTO users (name, age, email)
    VALUES ('Alice', 25, 'alice@example.com')
''')

# 파라미터 사용 (SQL 인젝션 방지)
cursor.execute('''
    INSERT INTO users (name, age, email)
    VALUES (?, ?, ?)
''', ('Bob', 30, 'bob@example.com'))

# 여러 데이터 삽입
users_data = [
    ('Charlie', 35, 'charlie@example.com'),
    ('David', 28, 'david@example.com')
]
cursor.executemany('''
    INSERT INTO users (name, age, email)
    VALUES (?, ?, ?)
''', users_data)

conn.commit()
conn.close()
```

## 5. 데이터 조회 (SELECT)

```python
import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# 모든 데이터 조회
cursor.execute('SELECT * FROM users')
rows = cursor.fetchall()
for row in rows:
    print(row)

# 특정 열만 조회
cursor.execute('SELECT name, age FROM users')
rows = cursor.fetchall()

# 조건 조회
cursor.execute('SELECT * FROM users WHERE age > ?', (25,))
rows = cursor.fetchall()

# 정렬
cursor.execute('SELECT * FROM users ORDER BY age DESC')

# 제한
cursor.execute('SELECT * FROM users LIMIT 5')

# 단일 결과
cursor.execute('SELECT * FROM users WHERE id = ?', (1,))
row = cursor.fetchone()

conn.close()
```

### 유용한 SELECT 문

```sql
-- WHERE: 조건 필터링
SELECT * FROM users WHERE age > 25

-- AND, OR: 여러 조건
SELECT * FROM users WHERE age > 25 AND name LIKE 'A%'

-- ORDER BY: 정렬
SELECT * FROM users ORDER BY age DESC

-- LIMIT: 개수 제한
SELECT * FROM users LIMIT 10

-- COUNT: 개수 세기
SELECT COUNT(*) FROM users

-- AVG, SUM, MAX, MIN: 집계
SELECT AVG(age) FROM users
SELECT MAX(age) FROM users
```

## 6. 데이터 수정 (UPDATE)

```python
import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# 데이터 수정
cursor.execute('''
    UPDATE users
    SET age = ?
    WHERE name = ?
''', (26, 'Alice'))

# 여러 열 수정
cursor.execute('''
    UPDATE users
    SET age = ?, email = ?
    WHERE id = ?
''', (31, 'bob_new@example.com', 2))

conn.commit()
conn.close()
```

## 7. 데이터 삭제 (DELETE)

```python
import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# 조건에 맞는 데이터 삭제
cursor.execute('DELETE FROM users WHERE age < ?', (20,))

# 특정 ID 삭제
cursor.execute('DELETE FROM users WHERE id = ?', (1,))

# 모든 데이터 삭제 (주의!)
cursor.execute('DELETE FROM users')

conn.commit()
conn.close()
```

## 8. 트랜잭션

```python
import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()

try:
    # 여러 쿼리 실행
    cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', ('Eve', 22))
    cursor.execute('UPDATE users SET age = ? WHERE name = ?', (23, 'Eve'))

    # 성공 시 커밋
    conn.commit()
except Exception as e:
    # 실패 시 롤백
    conn.rollback()
    print(f"Error: {e}")
finally:
    conn.close()
```

## 9. 테이블 정보 확인

```python
import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# 테이블 목록 조회
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = cursor.fetchall()
print(tables)

# 테이블 구조 확인
cursor.execute("PRAGMA table_info(users)")
columns = cursor.fetchall()
print(columns)

conn.close()
```

## 10. 컨텍스트 매니저 사용

```python
import sqlite3

# 자동으로 commit과 close 처리
with sqlite3.connect('example.db') as conn:
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    rows = cursor.fetchall()
```

## 연습 문제

이제 `exercises/step5_exercises.py` 파일을 열어 연습 문제를 풀어보세요!

다음 명령어로 채점할 수 있습니다:
```bash
pytest tests/test_step5.py -v
```
