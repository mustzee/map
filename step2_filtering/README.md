# Step 2: 필터링 & 검색

## 🎯 목표

Step 1의 코드에 **필터링과 검색 기능**을 추가합니다.

## 🚀 완성 후 할 수 있는 것

```bash
# 에러만 필터링
$ python logmaster.py filter --level ERROR
✓ Filtered to 5 ERROR entries

# 필터링 결과 저장
$ python logmaster.py filter --level ERROR --save errors.log
✓ Saved 5 entries to errors.log

# 키워드 검색
$ python logmaster.py search "database"
2024-01-15 08:15:24 INFO Database connection established
2024-01-15 08:19:02 ERROR Database connection timeout
2024-01-15 08:19:11 INFO Database connection re-established
✓ Found 3 matches

# 시간 범위 필터링
$ python logmaster.py filter --after "2024-01-15 08:30:00"
✓ Filtered to 12 entries after 2024-01-15 08:30:00

$ python logmaster.py filter --before "2024-01-15 08:20:00"
✓ Filtered to 15 entries before 2024-01-15 08:20:00

# 복합 필터링
$ python logmaster.py filter --level ERROR --after "2024-01-15 08:20:00"
✓ Filtered to 3 ERROR entries after 2024-01-15 08:20:00
```

## 📝 구현할 기능

### 1. filter 명령 추가
```python
# filter_logs() 메서드 추가
def filter_logs(self, level=None, after=None, before=None):
    """
    조건에 맞는 로그만 필터링하여 반환
    
    Args:
        level: 로그 레벨 (INFO, WARN, ERROR)
        after: 이 시간 이후의 로그
        before: 이 시간 이전의 로그
    
    Returns:
        필터링된 LogEntry 리스트
    """
    filtered = self.logs
    
    if level:
        filtered = [log for log in filtered if log.level == level]
    
    if after:
        after_dt = datetime.strptime(after, "%Y-%m-%d %H:%M:%S")
        filtered = [log for log in filtered if log.timestamp >= after_dt]
    
    if before:
        before_dt = datetime.strptime(before, "%Y-%m-%d %H:%M:%S")
        filtered = [log for log in filtered if log.timestamp <= before_dt]
    
    return filtered
```

### 2. search 명령 추가
```python
def search(self, keyword):
    """키워드가 포함된 로그 검색"""
    matches = [log for log in self.logs if keyword.lower() in log.message.lower()]
    return matches
```

### 3. save 기능 추가
```python
def save_logs(self, logs, filename):
    """로그를 파일로 저장"""
    with open(filename, 'w') as f:
        for log in logs:
            f.write(log.raw + '\n')
```

## 🔧 시작하기

1. **Step 1 코드 복사**:
```bash
cp ../step1_basic_reader/logmaster.py .
```

2. **기능 추가**:
- `filter_logs()` 메서드 추가
- `search()` 메서드 추가
- `save_logs()` 메서드 추가
- CLI에 `filter`, `search` 명령 추가

3. **테스트**:
```bash
python test.py
```

## 💡 힌트

### 리스트 컴프리헨션
```python
# 레벨로 필터링
errors = [log for log in self.logs if log.level == 'ERROR']

# 시간으로 필터링
recent = [log for log in self.logs if log.timestamp >= cutoff_time]

# 키워드 검색 (대소문자 무시)
matches = [log for log in self.logs if 'database' in log.message.lower()]
```

### 여러 조건 조합
```python
filtered = self.logs

# 조건 1 적용
if condition1:
    filtered = [log for log in filtered if check1(log)]

# 조건 2 적용
if condition2:
    filtered = [log for log in filtered if check2(log)]
```

## ✅ 체크리스트

- [ ] `filter --level ERROR` 동작
- [ ] `filter --after "<시간>"` 동작
- [ ] `filter --before "<시간>"` 동작
- [ ] 여러 조건 조합 동작
- [ ] `search "<키워드>"` 동작
- [ ] `--save` 옵션으로 파일 저장 동작

---

**다음 단계**: Step 3에서는 패턴 분석 기능 (Top 에러, 시간대별 분포)을 추가합니다!
