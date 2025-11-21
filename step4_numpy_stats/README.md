# Step 4: NumPy 통계 분석

## 🎯 목표

NumPy를 활용한 고급 통계 분석 및 이상치 탐지 기능을 추가합니다.

## 🚀 완성 후 할 수 있는 것

```bash
$ python logmaster.py trends
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📈 Trend Analysis
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Hourly Error Rate:
Hour    Errors  Rate    Status
─────────────────────────────────
08:00   2       normal  ✓
09:00   15      high    ⚠️
10:00   3       normal  ✓

Statistical Summary:
  Mean errors/hour: 6.7
  Std deviation: 5.2
  Max: 15
  Anomalies detected: 1

⚠️  Spike detected at 09:00 (15 errors, 1.6σ above mean)

$ python logmaster.py detect-anomalies --threshold 2.0
$ python logmaster.py predict --next 6h
Predicted error count (next 6h): 35-45 errors
```

## 📝 구현할 기능

### 1. 시계열 데이터 생성
```python
import numpy as np

def get_hourly_error_counts(self):
    """시간대별 에러 카운트를 NumPy 배열로 반환"""
    # 시간대별 카운트
    hourly = {}
    for log in self.logs:
        if log.level == 'ERROR':
            hour = log.timestamp.hour
            hourly[hour] = hourly.get(hour, 0) + 1
    
    # NumPy 배열로 변환
    hours = sorted(hourly.keys())
    counts = np.array([hourly[h] for h in hours])
    return hours, counts
```

### 2. 이상치 탐지
```python
def detect_anomalies(self, threshold=2.0):
    """Z-score 기반 이상치 탐지"""
    hours, counts = self.get_hourly_error_counts()
    
    mean = np.mean(counts)
    std = np.std(counts)
    
    anomalies = []
    for i, count in enumerate(counts):
        z_score = (count - mean) / std if std > 0 else 0
        if abs(z_score) > threshold:
            anomalies.append((hours[i], count, z_score))
    
    return anomalies
```

### 3. 이동 평균 & 트렌드
```python
def moving_average(self, window=3):
    """이동 평균 계산"""
    hours, counts = self.get_hourly_error_counts()
    ma = np.convolve(counts, np.ones(window)/window, mode='valid')
    return ma
```

---

**시작하기**: Step 3 코드를 복사하고 NumPy 분석 기능을 추가하세요!
