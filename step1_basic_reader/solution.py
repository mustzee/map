#!/usr/bin/env python3
"""
LogMaster Step 1: 정답 예시

막힐 때만 참고하세요!
"""
import argparse
from datetime import datetime
from collections import Counter


class LogEntry:
    """로그 한 줄을 나타내는 클래스"""

    def __init__(self, line):
        self.raw = line.strip()

        # 라인 파싱: "2024-01-15 08:15:23 INFO Application started"
        parts = self.raw.split(' ', 3)

        if len(parts) < 4:
            raise ValueError(f"Invalid log format: {line}")

        date_str = parts[0]
        time_str = parts[1]
        self.level = parts[2]
        self.message = parts[3]

        # timestamp를 datetime 객체로 변환
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
                if not line:  # 빈 줄 건너뛰기
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

        # 총 개수
        total = len(self.logs)
        print(f"Total entries: {total}")

        # 레벨별 카운트
        level_counts = Counter(log.level for log in self.logs)
        print("\nLog Levels:")
        for level in ['INFO', 'WARN', 'ERROR']:
            count = level_counts.get(level, 0)
            percent = (count / total * 100) if total > 0 else 0
            print(f"  {level:5s}: {count:3d} ({percent:5.1f}%)")

        # 시간 범위
        if self.logs:
            first_time = self.logs[0].timestamp
            last_time = self.logs[-1].timestamp
            duration = last_time - first_time

            print("\nTime Range:")
            print(f"  First: {first_time}")
            print(f"  Last:  {last_time}")

            # 시간 차이를 분으로 변환
            minutes = duration.total_seconds() / 60
            if minutes < 60:
                print(f"  Span:  {int(minutes)} minutes")
            else:
                hours = int(minutes // 60)
                mins = int(minutes % 60)
                print(f"  Span:  {hours}h {mins}m")

        print("=" * 50 + "\n")


def main():
    """CLI 메인 함수"""
    parser = argparse.ArgumentParser(
        description="LogMaster - 로그 분석 도구 (Step 1)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
예제:
  로그 파일 읽기:
    python solution.py load ../logs/sample.log

  통계 보기:
    python solution.py stats
        """
    )

    parser.add_argument('command', choices=['load', 'stats'],
                        help='실행할 명령')
    parser.add_argument('args', nargs='*', help='명령 인자')

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
            print("사용법: python solution.py load <파일명>")
            return

        filename = args.args[0]
        logmaster.load(filename)

        # 상태 저장
        with open(STATE_FILE, 'wb') as f:
            pickle.dump(logmaster, f)

    elif args.command == 'stats':
        logmaster.show_stats()


if __name__ == '__main__':
    main()
