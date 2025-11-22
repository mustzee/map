#!/usr/bin/env python3
"""
LogMaster Step 2: 필터링 & 검색 - 정답 예시
"""
import argparse
from datetime import datetime
from collections import Counter


class LogEntry:
    """로그 한 줄을 나타내는 클래스"""

    def __init__(self, line):
        self.raw = line.strip()
        parts = self.raw.split(' ', 3)

        if len(parts) < 4:
            raise ValueError(f"Invalid log format: {line}")

        date_str = parts[0]
        time_str = parts[1]
        self.level = parts[2]
        self.message = parts[3]

        timestamp_str = f"{date_str} {time_str}"
        self.timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")

    def __repr__(self):
        return f"<LogEntry {self.level} at {self.timestamp}>"


class LogMaster:
    """로그 관리 메인 클래스"""

    def __init__(self):
        self.logs = []
        self.filename = None

    def load(self, filename):
        """로그 파일을 읽어서 self.logs에 저장"""
        self.logs = []
        self.filename = filename

        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue

                try:
                    log_entry = LogEntry(line)
                    self.logs.append(log_entry)
                except ValueError as e:
                    print(f"Warning: {e}")

        print(f"✓ Loaded {len(self.logs)} log entries")

    def show_stats(self):
        """로그 통계 출력"""
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
            first_time = self.logs[0].timestamp
            last_time = self.logs[-1].timestamp
            duration = last_time - first_time

            print("\nTime Range:")
            print(f"  First: {first_time}")
            print(f"  Last:  {last_time}")

            minutes = duration.total_seconds() / 60
            if minutes < 60:
                print(f"  Span:  {int(minutes)} minutes")
            else:
                hours = int(minutes // 60)
                mins = int(minutes % 60)
                print(f"  Span:  {hours}h {mins}m")

        print("=" * 50 + "\n")

    # ============ Step 2: 새로운 기능 ============

    def filter_logs(self, level=None, after=None, before=None):
        """
        조건에 맞는 로그 필터링

        Args:
            level: 로그 레벨 (INFO, WARN, ERROR)
            after: 이 시간 이후 (문자열: "YYYY-MM-DD HH:MM:SS")
            before: 이 시간 이전 (문자열: "YYYY-MM-DD HH:MM:SS")

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

    def search(self, keyword):
        """
        키워드가 포함된 로그 검색 (대소문자 무시)

        Args:
            keyword: 검색할 키워드

        Returns:
            매칭되는 LogEntry 리스트
        """
        keyword_lower = keyword.lower()
        matches = [log for log in self.logs 
                   if keyword_lower in log.message.lower()]
        return matches

    def save_logs(self, logs, filename):
        """
        로그를 파일로 저장

        Args:
            logs: LogEntry 리스트
            filename: 저장할 파일명
        """
        with open(filename, 'w', encoding='utf-8') as f:
            for log in logs:
                f.write(log.raw + '\n')


def main():
    """CLI 메인 함수"""
    parser = argparse.ArgumentParser(
        description="LogMaster - 로그 분석 도구 (Step 2)",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument('command', 
                        choices=['load', 'stats', 'filter', 'search'],
                        help='실행할 명령')
    parser.add_argument('args', nargs='*', help='명령 인자')
    parser.add_argument('--level', help='로그 레벨 (INFO, WARN, ERROR)')
    parser.add_argument('--after', help='이 시간 이후 (YYYY-MM-DD HH:MM:SS)')
    parser.add_argument('--before', help='이 시간 이전 (YYYY-MM-DD HH:MM:SS)')
    parser.add_argument('--save', help='결과를 파일로 저장')

    args = parser.parse_args()

    import pickle
    import os

    STATE_FILE = '.logmaster_state.pkl'

    # 상태 로드
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, 'rb') as f:
            logmaster = pickle.load(f)
    else:
        logmaster = LogMaster()

    # 명령 실행
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
        filtered = logmaster.filter_logs(
            level=args.level,
            after=args.after,
            before=args.before
        )
        
        print(f"✓ Filtered to {len(filtered)} entries")
        
        if args.save:
            logmaster.save_logs(filtered, args.save)
            print(f"✓ Saved to {args.save}")
        else:
            for log in filtered[:10]:  # 처음 10개만 출력
                print(log.raw)
            if len(filtered) > 10:
                print(f"... and {len(filtered) - 10} more")

    elif args.command == 'search':
        if not args.args:
            print("Error: 검색 키워드를 지정하세요")
            return
        
        keyword = args.args[0]
        matches = logmaster.search(keyword)
        
        print(f"✓ Found {len(matches)} matches for '{keyword}'")
        for log in matches[:10]:
            print(log.raw)
        if len(matches) > 10:
            print(f"... and {len(matches) - 10} more")


if __name__ == '__main__':
    main()
