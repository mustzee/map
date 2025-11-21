# 🔍 LogMaster - 점진적 로그 분석 도구 만들기

실제로 작동하는 CLI 로그 분석 도구를 **처음부터 끝까지 점진적으로 완성**하는 프로젝트입니다.

## 🎯 프로젝트 컨셉

단순히 빈칸 채우기가 아닙니다! 각 단계마다 **실제로 동작하는 CLI 도구**를 만들고, 점점 기능을 추가하면서 완전한 로그 분석 시스템으로 성장시킵니다.

### 성장 과정

```
Step 1: 기본 리더     →  python logmaster.py stats
Step 2: 필터링 추가    →  python logmaster.py filter --level ERROR
Step 3: 패턴 분석     →  python logmaster.py analyze --top-errors 10
Step 4: 통계 분석     →  python logmaster.py trends --detect-anomalies
Step 5: 고급 분석     →  python logmaster.py report --format html
Step 6: DB 연동       →  python logmaster.py query "errors last 24h"
```

## 📊 각 단계별 기능

### Step 1: 기본 로그 파일 리더
**학습 내용**: Python 파일 I/O, 리스트, 딕셔너리

**완성 후 할 수 있는 것**:
```bash
$ python logmaster.py load logs/app.log
✓ Loaded 1,524 log entries

$ python logmaster.py stats
Total lines: 1,524
Log levels:
  INFO:  1,120 (73.5%)
  WARN:    245 (16.1%)
  ERROR:   159 (10.4%)
Time range: 2024-01-01 00:00:00 to 2024-01-15 23:59:59
```

**추가되는 코드**: `logmaster.py` 기본 구조
- `LogEntry` 클래스 (로그 파싱)
- `load_logs()` 함수
- `show_stats()` 함수
- CLI 기본 구조

---

### Step 2: 필터링 & 검색
**학습 내용**: 리스트 컴프리헨션, 정규표현식

**완성 후 할 수 있는 것**:
```bash
$ python logmaster.py filter --level ERROR
✓ Found 159 ERROR entries

$ python logmaster.py filter --level ERROR --save errors.log
✓ Saved 159 entries to errors.log

$ python logmaster.py search "database connection"
2024-01-05 14:23:45 ERROR database connection timeout
2024-01-08 09:12:33 ERROR database connection refused
✓ Found 2 matches

$ python logmaster.py filter --after "2024-01-10" --before "2024-01-15"
✓ Found 478 entries in date range
```

**추가되는 코드**: `logmaster.py`에 추가
- `filter_by_level()` 함수
- `filter_by_time()` 함수
- `search_logs()` 함수
- `save_logs()` 함수

---

### Step 3: 패턴 분석 & 집계
**학습 내용**: Counter, defaultdict, 데이터 집계

**완성 후 할 수 있는 것**:
```bash
$ python logmaster.py analyze
Top 5 Error Messages:
  1. Connection timeout (45 times)
  2. File not found (23 times)
  3. Permission denied (18 times)
  4. Invalid input (12 times)
  5. Out of memory (8 times)

Hourly Distribution:
  00-06: ███░░░░░░░ 234 (15.4%)
  06-12: ████████░░ 567 (37.2%)
  12-18: ██████████ 623 (40.9%)
  18-24: ██░░░░░░░░ 100 (6.6%)

$ python logmaster.py analyze --group-by hour --show-chart
$ python logmaster.py analyze --top-errors 10 --export errors-report.txt
```

**추가되는 코드**: `logmaster.py`에 추가
- `count_by_message()` 함수
- `hourly_distribution()` 함수
- `analyze_patterns()` 함수
- `draw_chart()` 함수

---

### Step 4: NumPy 통계 분석
**학습 내용**: NumPy 배열, 통계 함수, 이상치 탐지

**완성 후 할 수 있는 것**:
```bash
$ python logmaster.py trends
Error Rate Trend:
  Week 1: 12.5 errors/hour (normal)
  Week 2: 45.3 errors/hour ⚠️  SPIKE DETECTED!
  Week 3: 11.8 errors/hour (normal)

Statistical Summary:
  Mean: 23.2 errors/hour
  Std Dev: 15.7
  Anomalies detected: 3 time periods

$ python logmaster.py trends --detect-anomalies --threshold 2.5
⚠️  Anomaly: 2024-01-08 14:00 - 15:00 (78 errors, 3.2σ)
⚠️  Anomaly: 2024-01-12 09:00 - 10:00 (92 errors, 4.1σ)

$ python logmaster.py predict --next 24h
Predicted error count (next 24h): 15-25 errors
Confidence: 85%
```

**추가되는 코드**: `logmaster.py`에 추가
- `calculate_trends()` 함수 (NumPy)
- `detect_anomalies()` 함수
- `predict_future()` 함수
- `statistical_summary()` 함수

---

### Step 5: Pandas 고급 분석
**학습 내용**: DataFrame, 그룹화, 피벗, 시계열

**완성 후 할 수 있는 것**:
```bash
$ python logmaster.py report
Generating comprehensive report...
✓ Created report.html

$ python logmaster.py compare logs/week1.log logs/week2.log
Comparison Report:
                Week 1    Week 2    Change
Total Errors      234       456    +94.9% ⚠️
Avg Response    125ms     380ms    +204%  ⚠️
Uptime          99.8%     97.2%    -2.6%  ⚠️

$ python logmaster.py timeseries --resample 1H --plot
Creating hourly timeseries plot...
✓ Saved to timeseries.png

$ python logmaster.py pivot --index date --columns level --values count
```

**추가되는 코드**: `logmaster.py`에 추가
- `to_dataframe()` 함수
- `generate_report()` 함수
- `compare_logs()` 함수
- `timeseries_analysis()` 함수
- `create_pivot_table()` 함수

---

### Step 6: 데이터베이스 연동
**학습 내용**: SQLite, Pandas-DB 연동, 영구 저장

**완성 후 할 수 있는 것**:
```bash
$ python logmaster.py import logs/app.log
✓ Imported 1,524 entries to database

$ python logmaster.py query "SELECT * FROM logs WHERE level='ERROR' AND timestamp > datetime('now', '-1 day')"
✓ Found 23 entries

$ python logmaster.py alert-rule "ERROR count > 10 per hour"
✓ Alert rule created

$ python logmaster.py dashboard
Starting live dashboard on http://localhost:8080
Press Ctrl+C to stop...

$ python logmaster.py export-db --format csv
✓ Exported to logs_export.csv

$ python logmaster.py history --show-trends --last 30days
```

**추가되는 코드**: `logmaster.py`에 추가
- `import_to_db()` 함수
- `query_db()` 함수
- `setup_alerts()` 함수
- `live_dashboard()` 함수
- `export_from_db()` 함수

---

## 🚀 시작하기

### 1. 환경 설정
```bash
pip install -r requirements.txt
```

### 2. Step 1부터 시작
```bash
cd step1_basic_reader
cat README.md  # 학습 자료 읽기
```

### 3. 코드 작성
각 단계의 `logmaster.py`를 완성하세요. 주석으로 TODO가 표시되어 있습니다.

### 4. 테스트
```bash
# 직접 실행해보기
python logmaster.py load ../logs/sample.log
python logmaster.py stats

# 자동 채점
python test.py
```

### 5. 다음 단계로
```bash
cd ../step2_filtering
# Step 1의 코드를 복사해서 시작 (점진적 확장!)
```

## 📁 프로젝트 구조

```
logmaster/
├── README.md                    # 이 파일
├── requirements.txt
├── logs/                        # 샘플 로그 파일
│   ├── sample.log              # 기본 샘플
│   ├── sample_large.log        # 대용량 (10,000+ 줄)
│   ├── sample_errors.log       # 에러 많은 로그
│   └── sample_realtime.log     # 실시간 시뮬레이션
├── step1_basic_reader/
│   ├── README.md               # Step 1 학습 자료
│   ├── logmaster.py            # 여기에 코드 작성
│   ├── test.py                 # 자동 채점
│   └── solution.py             # 정답 예시 (막힐 때만!)
├── step2_filtering/
│   ├── README.md
│   ├── logmaster.py            # Step 1 코드 + 새 기능
│   ├── test.py
│   └── solution.py
├── step3_pattern_analysis/
├── step4_numpy_stats/
├── step5_pandas_advanced/
└── step6_database/
```

## 🎯 학습 목표

### 기술 스택
- ✅ Python 기초 (파일 I/O, 리스트, 딕셔너리)
- ✅ 정규표현식 (로그 파싱)
- ✅ NumPy (통계 분석, 이상치 탐지)
- ✅ Pandas (데이터프레임, 시계열)
- ✅ SQLite (데이터 영구 저장)
- ✅ CLI 도구 개발 (argparse)

### 실무 역량
- 🔍 로그 분석 & 디버깅
- 📊 데이터 시각화
- ⚠️ 이상 탐지
- 📈 트렌드 분석
- 🗄️ 데이터베이스 설계
- 🚨 알림 시스템

## 💡 학습 팁

1. **각 단계를 순서대로**: 이전 단계의 코드를 재사용하며 확장합니다
2. **실제로 실행해보기**: 샘플 로그로 직접 테스트하세요
3. **자동 채점 활용**: `python test.py`로 즉시 피드백
4. **실전 응용**: 실제 프로젝트의 로그 파일로 분석해보세요
5. **커스터마이징**: 원하는 기능을 추가해보세요!

## 🎓 완료 후 할 수 있는 것

이 프로젝트를 완료하면:
- ✅ 실제 업무에서 바로 사용할 수 있는 로그 분석 도구 완성
- ✅ Python 데이터 분석 스택 마스터 (Pandas, NumPy, SQLite)
- ✅ CLI 도구 개발 능력 습득
- ✅ 포트폴리오에 추가할 수 있는 실전 프로젝트

## 📚 추가 도전 과제

각 단계를 완료한 후:
- 새로운 로그 포맷 추가 (JSON, syslog 등)
- 웹 대시보드 만들기 (Flask/FastAPI)
- 실시간 로그 스트리밍 처리
- 머신러닝 기반 예측 모델
- Slack/Discord 알림 연동

---

**Let's build something useful! 🚀**
