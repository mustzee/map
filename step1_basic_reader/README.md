# Step 1: 기본 로그 파일 리더

## 🎯 목표

첫 번째 단계에서는 **로그 파일을 읽고 기본 통계를 보여주는** CLI 도구를 만듭니다.

## 💡 학습 내용

- Python 파일 읽기 (`open`, `readlines`)
- 문자열 파싱 (`split`, `strip`)
- 딕셔너리로 카운팅
- CLI 인터페이스 (`argparse`)
- 클래스 기본 (`LogEntry`)

## 🚀 완성 후 할 수 있는 것

```bash
$ python logmaster.py load ../logs/sample.log
✓ Loaded 40 log entries

$ python logmaster.py stats
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 Log Statistics
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Total entries: 40

Log Levels:
  INFO:  28 (70.0%)
  WARN:   7 (17.5%)
  ERROR:  5 (12.5%)

Time Range:
  First: 2024-01-15 08:15:23
  Last:  2024-01-15 08:40:21
  Span:  25 minutes
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## 📝 구현할 기능

### 1. LogEntry 클래스
로그 한 줄을 파싱하여 객체로 만듭니다.

```python
class LogEntry:
    def __init__(self, line):
        # "2024-01-15 08:15:23 INFO Application started"
        # → timestamp, level, message 분리
        pass
```

### 2. load_logs() 함수
파일에서 로그를 읽어 LogEntry 리스트로 반환합니다.

```python
def load_logs(filename):
    # 파일 열기
    # 각 줄을 LogEntry로 변환
    # 리스트 반환
    pass
```

### 3. show_stats() 함수
로그 통계를 보기 좋게 출력합니다.

```python
def show_stats(logs):
    # 총 개수
    # 레벨별 카운트 (INFO, WARN, ERROR)
    # 시간 범위 (첫 로그 ~ 마지막 로그)
    pass
```

### 4. CLI 인터페이스
argparse로 명령줄 인터페이스를 만듭니다.

```python
# load 명령
python logmaster.py load <파일명>

# stats 명령  
python logmaster.py stats
```

## 📖 로그 포맷

샘플 로그는 다음 형식을 따릅니다:
```
<타임스탬프> <레벨> <메시지>

예: 2024-01-15 08:15:23 INFO Application started
```

- **타임스탬프**: `YYYY-MM-DD HH:MM:SS` 형식
- **레벨**: `INFO`, `WARN`, `ERROR` 중 하나
- **메시지**: 나머지 모든 텍스트

## 🔧 구현 가이드

### 파싱 팁

```python
line = "2024-01-15 08:15:23 INFO Application started successfully"

# 방법 1: split() 사용
parts = line.split(' ', 3)  # 최대 4개로 분리
date = parts[0]             # "2024-01-15"
time = parts[1]             # "08:15:23"
level = parts[2]            # "INFO"
message = parts[3]          # "Application started successfully"

timestamp = f"{date} {time}"

# 방법 2: 정규표현식 (선택사항)
import re
pattern = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) (.+)'
match = re.match(pattern, line)
if match:
    timestamp, level, message = match.groups()
```

### 카운팅 팁

```python
# 레벨별 카운트
level_counts = {}
for log in logs:
    level = log.level
    if level in level_counts:
        level_counts[level] += 1
    else:
        level_counts[level] = 1

# 또는 defaultdict 사용
from collections import defaultdict
level_counts = defaultdict(int)
for log in logs:
    level_counts[log.level] += 1

# 또는 Counter 사용 (가장 간단!)
from collections import Counter
level_counts = Counter(log.level for log in logs)
```

### 시간 계산 팁

```python
from datetime import datetime

# 문자열을 datetime으로 변환
timestamp_str = "2024-01-15 08:15:23"
dt = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")

# 시간 차이 계산
first_time = logs[0].timestamp  # datetime 객체
last_time = logs[-1].timestamp
duration = last_time - first_time
print(f"Span: {duration}")  # "0:25:00" (25분)
```

## ✅ 체크리스트

완성 전에 확인하세요:

- [ ] `LogEntry` 클래스가 timestamp, level, message 속성을 가지는가?
- [ ] `load_logs()`가 파일을 읽고 LogEntry 리스트를 반환하는가?
- [ ] `show_stats()`가 총 개수, 레벨별 카운트, 시간 범위를 출력하는가?
- [ ] CLI에서 `load`와 `stats` 명령이 동작하는가?
- [ ] 샘플 로그로 테스트했는가?

## 🧪 테스트

```bash
# 자동 채점
python test.py

# 직접 실행 테스트
python logmaster.py load ../logs/sample.log
python logmaster.py stats
```

## 🎓 다음 단계

Step 1을 완료하면 **Step 2: 필터링 & 검색**으로 넘어갑니다!

Step 2에서는 이 코드를 그대로 가져가서 필터링 기능을 추가합니다:
- `filter --level ERROR` (에러만 보기)
- `search "database"` (키워드 검색)
- `filter --after "2024-01-15 08:30:00"` (시간 필터링)

---

**힌트**: 막히면 `solution.py`를 참고하세요. 하지만 먼저 직접 시도해보는 것이 중요합니다!
