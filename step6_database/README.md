# Step 6: 데이터베이스 연동

## 🎯 목표

SQLite 데이터베이스에 로그를 저장하고 SQL 쿼리로 분석하는 기능을 추가합니다.

## 🚀 완성 후 할 수 있는 것

```bash
$ python logmaster.py import ../logs/sample.log
✓ Imported 40 log entries to database

$ python logmaster.py query "SELECT level, COUNT(*) FROM logs GROUP BY level"
┌─────────┬──────────┐
│ level   │ COUNT(*) │
├─────────┼──────────┤
│ INFO    │ 28       │
│ WARN    │ 7        │
│ ERROR   │ 5        │
└─────────┴──────────┘

$ python logmaster.py query "SELECT * FROM logs WHERE level='ERROR' AND timestamp > datetime('now', '-1 hour')"

$ python logmaster.py export-db --format csv
✓ Exported 40 entries to logs_export.csv

$ python logmaster.py history --last 7days
Showing log history for last 7 days...

$ python logmaster.py dashboard
Starting live monitoring dashboard...
Press Ctrl+C to stop
```

## 📝 구현할 기능

### 1. 데이터베이스 초기화
```python
import sqlite3
import pandas as pd

def init_database(self, db_path='logs.db'):
    """데이터베이스 초기화"""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME,
            level TEXT,
            message TEXT,
            imported_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()
```

### 2. 로그 임포트
```python
def import_to_db(self, db_path='logs.db'):
    """현재 로드된 로그를 DB에 저장"""
    conn = sqlite3.connect(db_path)
    
    df = self.to_dataframe()
    df.to_sql('logs', conn, if_exists='append', index=True)
    
    conn.close()
    print(f"✓ Imported {len(self.logs)} entries")
```

### 3. SQL 쿼리 실행
```python
def query_db(self, sql, db_path='logs.db'):
    """SQL 쿼리 실행 및 결과 반환"""
    conn = sqlite3.connect(db_path)
    df = pd.read_sql_query(sql, conn)
    conn.close()
    return df
```

### 4. 알림 규칙 설정
```python
def setup_alert_rule(self, condition, action):
    """
    알림 규칙 설정
    예: "ERROR count > 10 per hour" -> Slack 알림
    """
    # 규칙을 DB에 저장
    # 실시간 모니터링 시 체크
    pass
```

### 5. 라이브 대시보드 (선택)
```python
def live_dashboard(self):
    """실시간 로그 모니터링 대시보드"""
    import time
    
    while True:
        # DB에서 최근 로그 조회
        recent = self.query_db(
            "SELECT * FROM logs WHERE timestamp > datetime('now', '-5 minutes')"
        )
        
        # 통계 계산 및 출력
        print(f"\rLive: {len(recent)} logs in last 5 min", end='')
        
        time.sleep(5)
```

---

**시작하기**: Step 5 코드를 복사하고 데이터베이스 기능을 추가하세요!

**🎉 Step 6를 완료하면 완전한 로그 분석 시스템이 완성됩니다!**
