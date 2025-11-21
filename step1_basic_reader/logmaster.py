#!/usr/bin/env python3
"""
LogMaster Step 1: 기본 로그 파일 리더

이 파일을 완성하세요!
"""
import argparse
from datetime import datetime
from collections import Counter


class LogEntry:
    """로그 한 줄을 나타내는 클래스"""

    def __init__(self, line):
        """
        로그 라인을 파싱합니다.

        입력 예: "2024-01-15 08:15:23 INFO Application started"

        TODO: 다음 속성들을 파싱하여 저장하세요
        - self.timestamp: datetime 객체
        - self.level: 문자열 (INFO, WARN, ERROR)
        - self.message: 문자열
        - self.raw: 원본 라인 (strip된 상태)
        """
        self.raw = line.strip()

        # TODO: 라인을 파싱하여 timestamp, level, message 추출
        # 힌트: split(' ', 3)을 사용하면 날짜, 시간, 레벨, 메시지로 분리됩니다
        pass

    def __repr__(self):
        return f"<LogEntry {self.level} at {self.timestamp}>"


class LogMaster:
    """로그 관리 메인 클래스"""

    def __init__(self):
        self.logs = []
        self.filename = None

    def load(self, filename):
        """
        로그 파일을 읽어서 self.logs에 저장합니다.

        TODO:
        1. 파일을 열어서 모든 줄을 읽기
        2. 빈 줄은 건너뛰기
        3. 각 줄을 LogEntry로 변환
        4. self.logs 리스트에 추가
        5. self.filename 저장
        """
        self.logs = []
        self.filename = filename

        # TODO: 파일 읽기 및 파싱
        pass

        print(f"✓ Loaded {len(self.logs)} log entries")

    def show_stats(self):
        """
        로그 통계를 보기 좋게 출력합니다.

        TODO:
        1. 총 로그 개수 출력
        2. 레벨별 카운트 및 퍼센트 출력 (INFO, WARN, ERROR)
        3. 시간 범위 출력 (첫 로그 ~ 마지막 로그, 시간 차이)
        """
        if not self.logs:
            print("No logs loaded. Use 'load' command first.")
            return

        print("\n" + "=" * 50)
        print("📊 Log Statistics")
        print("=" * 50)

        # TODO: 총 개수
        print(f"Total entries: ???")

        print("\nLog Levels:")
        # TODO: 레벨별 카운트
        # 힌트: Counter를 사용하면 편리합니다
        pass

        print("\nTime Range:")
        # TODO: 첫 로그와 마지막 로그의 시간, 시간 차이
        pass

        print("=" * 50 + "\n")


def main():
    """CLI 메인 함수"""
    parser = argparse.ArgumentParser(
        description="LogMaster - 로그 분석 도구 (Step 1)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
예제:
  로그 파일 읽기:
    python logmaster.py load ../logs/sample.log

  통계 보기:
    python logmaster.py stats
        """
    )

    parser.add_argument('command', choices=['load', 'stats'],
                        help='실행할 명령')
    parser.add_argument('args', nargs='*', help='명령 인자')

    args = parser.parse_args()

    # 전역 LogMaster 인스턴스 (간단히 하기 위해)
    # 실전에서는 파일에 저장하거나 DB를 사용합니다
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
            print("사용법: python logmaster.py load <파일명>")
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
