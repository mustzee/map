#!/usr/bin/env python3
"""
LogMaster Step 3: 패턴 분석 & 집계 - 정답 예시
"""
import argparse
from datetime import datetime
from collections import Counter, defaultdict

class LogEntry:
    def __init__(self, line):
        self.raw = line.strip()
        parts = self.raw.split(' ', 3)
        if len(parts) < 4:
            raise ValueError(f"Invalid log format: {line}")
        date_str, time_str, self.level, self.message = parts
        timestamp_str = f"{date_str} {time_str}"
        self.timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
    
    def __repr__(self):
        return f"<LogEntry {self.level} at {self.timestamp}>"

class LogMaster:
    def __init__(self):
        self.logs = []
        self.filename = None

    def load(self, filename):
        self.logs = []
        self.filename = filename
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    self.logs.append(LogEntry(line))
                except ValueError as e:
                    print(f"Warning: {e}")
        print(f"✓ Loaded {len(self.logs)} log entries")

    def show_stats(self):
        if not self.logs:
            print("No logs loaded. Use 'load' command first.")
            return
        print("\n" + "=" * 50)
        print("📊 Log Statistics")
        print("=" * 50)
        total = len(self.logs)
        print(f"Total entries: {total}")
        level_counts = Counter(log.level for log in self.logs)
        print("\nLog Levels:")
        for level in ['INFO', 'WARN', 'ERROR']:
            count = level_counts.get(level, 0)
            percent = (count / total * 100) if total > 0 else 0
            print(f"  {level:5s}: {count:3d} ({percent:5.1f}%)")
        if self.logs:
            first_time, last_time = self.logs[0].timestamp, self.logs[-1].timestamp
            duration = last_time - first_time
            print("\nTime Range:")
            print(f"  First: {first_time}")
            print(f"  Last:  {last_time}")
            minutes = duration.total_seconds() / 60
            if minutes < 60:
                print(f"  Span:  {int(minutes)} minutes")
            else:
                hours, mins = int(minutes // 60), int(minutes % 60)
                print(f"  Span:  {hours}h {mins}m")
        print("=" * 50 + "\n")

    def filter_logs(self, level=None, after=None, before=None):
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

    def search(self, keyword):
        keyword_lower = keyword.lower()
        return [log for log in self.logs if keyword_lower in log.message.lower()]

    def save_logs(self, logs, filename):
        with open(filename, 'w', encoding='utf-8') as f:
            for log in logs:
                f.write(log.raw + '\n')

    # ============ Step 3: 패턴 분석 ============
    
    def count_error_messages(self):
        """ERROR 로그의 메시지별 카운트"""
        errors = [log for log in self.logs if log.level == 'ERROR']
        messages = [log.message for log in errors]
        return Counter(messages)
    
    def hourly_distribution(self):
        """시간대별 로그 레벨 분포"""
        dist = defaultdict(lambda: {'INFO': 0, 'WARN': 0, 'ERROR': 0})
        for log in self.logs:
            hour = log.timestamp.hour
            dist[hour][log.level] += 1
        return dict(dist)
    
    def draw_bar_chart(self, value, max_value, width=10):
        """ASCII 막대 차트"""
        if max_value == 0:
            return '░' * width
        filled = int((value / max_value) * width)
        return '█' * filled + '░' * (width - filled)
    
    def analyze(self):
        """패턴 분석 출력"""
        print("\n" + "=" * 60)
        print("📊 Pattern Analysis")
        print("=" * 60)
        
        # Top 5 에러 메시지
        error_counts = self.count_error_messages()
        print("\nTop 5 Error Messages:")
        for i, (msg, count) in enumerate(error_counts.most_common(5), 1):
            print(f"  {i}. {msg[:50]} ({count} times)")
        
        # 시간대별 분포
        hourly = self.hourly_distribution()
        if hourly:
            print("\nHourly Distribution:")
            print(f"{'Hour':<6} {'INFO':<6} {'WARN':<6} {'ERROR':<6} {'Total':<6} Chart")
            print("-" * 60)
            
            max_total = max(sum(counts.values()) for counts in hourly.values())
            for hour in sorted(hourly.keys()):
                counts = hourly[hour]
                total = sum(counts.values())
                chart = self.draw_bar_chart(total, max_total, 12)
                print(f"{hour:02d}-{hour+1:02d}  {counts['INFO']:<6} {counts['WARN']:<6} {counts['ERROR']:<6} {total:<6} {chart}")
        
        print("=" * 60 + "\n")

def main():
    parser = argparse.ArgumentParser(description="LogMaster - 로그 분석 도구 (Step 3)")
    parser.add_argument('command', choices=['load', 'stats', 'filter', 'search', 'analyze'], help='실행할 명령')
    parser.add_argument('args', nargs='*', help='명령 인자')
    parser.add_argument('--level', help='로그 레벨')
    parser.add_argument('--after', help='이 시간 이후')
    parser.add_argument('--before', help='이 시간 이전')
    parser.add_argument('--save', help='결과 저장')
    
    args = parser.parse_args()
    
    import pickle, os
    STATE_FILE = '.logmaster_state.pkl'
    
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, 'rb') as f:
            logmaster = pickle.load(f)
    else:
        logmaster = LogMaster()
    
    if args.command == 'load':
        if not args.args:
            print("Error: 파일명을 지정하세요")
            return
        logmaster.load(args.args[0])
        with open(STATE_FILE, 'wb') as f:
            pickle.dump(logmaster, f)
    
    elif args.command == 'stats':
        logmaster.show_stats()
    
    elif args.command == 'filter':
        filtered = logmaster.filter_logs(level=args.level, after=args.after, before=args.before)
        print(f"✓ Filtered to {len(filtered)} entries")
        if args.save:
            logmaster.save_logs(filtered, args.save)
            print(f"✓ Saved to {args.save}")
    
    elif args.command == 'search':
        if not args.args:
            print("Error: 검색 키워드를 지정하세요")
            return
        matches = logmaster.search(args.args[0])
        print(f"✓ Found {len(matches)} matches")
        for log in matches[:10]:
            print(log.raw)
    
    elif args.command == 'analyze':
        logmaster.analyze()

if __name__ == '__main__':
    main()
