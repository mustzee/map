# Step 3: 패턴 분석 & 집계

## 🎯 목표

로그 패턴을 분석하고 통계를 집계하는 기능을 추가합니다.

## 🚀 완성 후 할 수 있는 것

```bash
$ python logmaster.py analyze
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 Pattern Analysis
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Top 5 Error Messages:
  1. Database connection timeout (3 times)
  2. Permission denied (2 times)
  3. File not found (1 time)
  4. Invalid API key (1 time)
  5. File size exceeds limit (1 time)

Hourly Distribution:
Hour    INFO    WARN    ERROR   Total   Chart
────────────────────────────────────────────────
08-09   10      2       2       14      ██████████░░
09-10   8       1       1       10      ████████░░░░
10-11   10      4       2       16      ████████████

$ python logmaster.py top-errors 10
$ python logmaster.py hourly-chart
$ python logmaster.py export-report analysis.txt
```

## 📝 구현할 기능

### 1. 에러 메시지 집계
```python
def count_error_messages(self):
    """ERROR 로그의 메시지별 카운트"""
    errors = [log for log in self.logs if log.level == 'ERROR']
    messages = [log.message for log in errors]
    return Counter(messages)
```

### 2. 시간대별 분포
```python
def hourly_distribution(self):
    """시간대별 로그 레벨 분포"""
    from collections import defaultdict
    
    dist = defaultdict(lambda: {'INFO': 0, 'WARN': 0, 'ERROR': 0})
    
    for log in self.logs:
        hour = log.timestamp.hour
        dist[hour][log.level] += 1
    
    return dist
```

### 3. ASCII 차트
```python
def draw_bar_chart(value, max_value, width=10):
    """ASCII 막대 차트"""
    filled = int((value / max_value) * width)
    return '█' * filled + '░' * (width - filled)
```

---

**시작하기**: Step 2 코드를 복사하고 분석 기능을 추가하세요!
