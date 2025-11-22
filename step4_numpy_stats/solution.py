#!/usr/bin/env python3
"""LogMaster Step 4: NumPy 통계 분석 - 정답 예시"""
# Step 3의 모든 코드 + NumPy 기능
from step3_pattern_analysis.solution import *
import numpy as np

class LogMaster(LogMaster):  # Step 3 확장
    def get_hourly_error_counts(self):
        """시간대별 에러 카운트를 NumPy 배열로 반환"""
        hourly = {}
        for log in self.logs:
            if log.level == 'ERROR':
                hour = log.timestamp.hour
                hourly[hour] = hourly.get(hour, 0) + 1
        
        hours = sorted(hourly.keys())
        counts = np.array([hourly[h] for h in hours])
        return hours, counts
    
    def detect_anomalies(self, threshold=2.0):
        """Z-score 기반 이상치 탐지"""
        hours, counts = self.get_hourly_error_counts()
        if len(counts) == 0:
            return []
        
        mean = np.mean(counts)
        std = np.std(counts)
        
        anomalies = []
        for i, count in enumerate(counts):
            z_score = (count - mean) / std if std > 0 else 0
            if abs(z_score) > threshold:
                anomalies.append((hours[i], count, z_score))
        
        return anomalies
    
    def moving_average(self, window=3):
        """이동 평균 계산"""
        hours, counts = self.get_hourly_error_counts()
        if len(counts) < window:
            return counts
        ma = np.convolve(counts, np.ones(window)/window, mode='valid')
        return ma

if __name__ == '__main__':
    main()
