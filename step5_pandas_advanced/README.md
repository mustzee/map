# Step 5: Pandas 고급 분석

## 🎯 목표

Pandas DataFrame을 활용한 고급 데이터 분석 및 리포트 생성 기능을 추가합니다.

## 🚀 완성 후 할 수 있는 것

```bash
$ python logmaster.py report
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 Comprehensive Report
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Level Summary:
       Count  Percentage
INFO      28       70.0%
WARN       7       17.5%
ERROR      5       12.5%

Hourly Pivot Table:
        ERROR  INFO  WARN
Hour                     
8          3    15     2
9          2    13     5

Generated report.html ✓

$ python logmaster.py compare logs/week1.log logs/week2.log
Week 1 vs Week 2:
                Week 1  Week 2  Change
Total Errors        12      23  +91.7% ⚠️
Avg per Hour       2.0     3.8  +90.0% ⚠️

$ python logmaster.py timeseries --resample 1H
Creating hourly timeseries analysis...
✓ Saved timeseries.png
```

## 📝 구현할 기능

### 1. DataFrame 변환
```python
import pandas as pd

def to_dataframe(self):
    """LogEntry 리스트를 DataFrame으로 변환"""
    data = {
        'timestamp': [log.timestamp for log in self.logs],
        'level': [log.level for log in self.logs],
        'message': [log.message for log in self.logs]
    }
    df = pd.DataFrame(data)
    df.set_index('timestamp', inplace=True)
    return df
```

### 2. 피벗 테이블
```python
def create_pivot_table(self):
    """시간대별 레벨 피벗 테이블"""
    df = self.to_dataframe()
    df['hour'] = df.index.hour
    
    pivot = df.pivot_table(
        values='message',
        index='hour',
        columns='level',
        aggfunc='count',
        fill_value=0
    )
    return pivot
```

### 3. 시계열 리샘플링
```python
def resample_timeseries(self, rule='1H'):
    """시계열 데이터 리샘플링"""
    df = self.to_dataframe()
    resampled = df.groupby('level').resample(rule).size()
    return resampled
```

### 4. HTML 리포트 생성
```python
def generate_html_report(self, filename='report.html'):
    """HTML 리포트 생성"""
    df = self.to_dataframe()
    
    html = f"""
    <html>
    <head><title>Log Analysis Report</title></head>
    <body>
        <h1>Log Analysis Report</h1>
        <h2>Summary</h2>
        {df.describe().to_html()}
        
        <h2>Level Distribution</h2>
        {df['level'].value_counts().to_frame().to_html()}
    </body>
    </html>
    """
    
    with open(filename, 'w') as f:
        f.write(html)
```

---

**시작하기**: Step 4 코드를 복사하고 Pandas 분석 기능을 추가하세요!
