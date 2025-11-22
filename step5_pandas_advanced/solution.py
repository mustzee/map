#!/usr/bin/env python3
"""LogMaster Step 5: Pandas 고급 분석 - 정답 예시"""
from step4_numpy_stats.solution import *
import pandas as pd

class LogMaster(LogMaster):  # Step 4 확장
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
    
    def resample_timeseries(self, rule='1H'):
        """시계열 데이터 리샘플링"""
        df = self.to_dataframe()
        resampled = df.groupby('level').resample(rule).size()
        return resampled
    
    def generate_html_report(self, filename='report.html'):
        """HTML 리포트 생성"""
        df = self.to_dataframe()
        
        html = f"""<html>
<head><title>Log Analysis Report</title>
<style>
body {{ font-family: Arial, sans-serif; margin: 20px; }}
table {{ border-collapse: collapse; width: 100%; margin: 20px 0; }}
th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
th {{ background-color: #4CAF50; color: white; }}
</style>
</head>
<body>
<h1>📊 Log Analysis Report</h1>
<h2>Summary</h2>
<p>Total logs: {len(df)}</p>
<h2>Level Distribution</h2>
{df['level'].value_counts().to_frame().to_html()}
<h2>Hourly Pivot</h2>
{self.create_pivot_table().to_html()}
</body>
</html>"""
        
        with open(filename, 'w') as f:
            f.write(html)
        
        print(f"✓ Generated {filename}")

if __name__ == '__main__':
    main()
