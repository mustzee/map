#!/usr/bin/env python3
"""
Step 1 자동 채점 시스템
"""
import sys
import os

# logmaster 모듈을 import할 수 있도록 경로 추가
sys.path.insert(0, os.path.dirname(__file__))

try:
    from logmaster import LogEntry, LogMaster
except ImportError:
    print("❌ logmaster.py를 찾을 수 없습니다!")
    print("현재 디렉토리에 logmaster.py가 있는지 확인하세요.")
    sys.exit(1)

from datetime import datetime
from collections import Counter


def test_log_entry():
    """LogEntry 클래스 테스트"""
    print("Testing LogEntry class...")

    # 테스트 1: 기본 파싱
    line = "2024-01-15 08:15:23 INFO Application started"
    try:
        entry = LogEntry(line)

        assert hasattr(entry, 'timestamp'), "❌ LogEntry에 timestamp 속성이 없습니다"
        assert hasattr(entry, 'level'), "❌ LogEntry에 level 속성이 없습니다"
        assert hasattr(entry, 'message'), "❌ LogEntry에 message 속성이 없습니다"

        assert entry.level == "INFO", f"❌ level이 'INFO'여야 하는데 '{entry.level}'입니다"
        assert entry.message == "Application started", f"❌ message가 잘못되었습니다: {entry.message}"
        assert isinstance(entry.timestamp, datetime), "❌ timestamp가 datetime 객체가 아닙니다"

        print("  ✅ 기본 파싱 성공")

    except Exception as e:
        print(f"  ❌ 기본 파싱 실패: {e}")
        return False

    # 테스트 2: 다양한 레벨
    test_cases = [
        ("2024-01-15 08:15:23 ERROR Database connection failed", "ERROR"),
        ("2024-01-15 08:15:23 WARN Memory usage high", "WARN"),
    ]

    for line, expected_level in test_cases:
        try:
            entry = LogEntry(line)
            assert entry.level == expected_level, f"❌ level이 '{expected_level}'여야 하는데 '{entry.level}'입니다"
        except Exception as e:
            print(f"  ❌ {expected_level} 파싱 실패: {e}")
            return False

    print("  ✅ 다양한 레벨 파싱 성공")

    # 테스트 3: 긴 메시지 (공백 포함)
    line = "2024-01-15 08:15:23 INFO This is a long message with many words"
    try:
        entry = LogEntry(line)
        expected_message = "This is a long message with many words"
        assert entry.message == expected_message, f"❌ 긴 메시지 파싱 실패: {entry.message}"
        print("  ✅ 긴 메시지 파싱 성공")
    except Exception as e:
        print(f"  ❌ 긴 메시지 파싱 실패: {e}")
        return False

    return True


def test_logmaster_load():
    """LogMaster load 메서드 테스트"""
    print("\nTesting LogMaster.load()...")

    # 임시 로그 파일 생성
    test_file = 'test_sample.log'
    with open(test_file, 'w') as f:
        f.write("2024-01-15 08:15:23 INFO First log\n")
        f.write("2024-01-15 08:15:24 WARN Second log\n")
        f.write("2024-01-15 08:15:25 ERROR Third log\n")
        f.write("\n")  # 빈 줄
        f.write("2024-01-15 08:15:26 INFO Fourth log\n")

    try:
        logmaster = LogMaster()
        logmaster.load(test_file)

        assert len(logmaster.logs) == 4, f"❌ 4개 로그를 읽어야 하는데 {len(logmaster.logs)}개입니다"
        assert logmaster.logs[0].level == "INFO", "❌ 첫 번째 로그 레벨이 INFO가 아닙니다"
        assert logmaster.logs[1].level == "WARN", "❌ 두 번째 로그 레벨이 WARN이 아닙니다"
        assert logmaster.logs[2].level == "ERROR", "❌ 세 번째 로그 레벨이 ERROR가 아닙니다"

        print("  ✅ 파일 로딩 성공")

        # 정리
        os.remove(test_file)
        return True

    except Exception as e:
        print(f"  ❌ 파일 로딩 실패: {e}")
        if os.path.exists(test_file):
            os.remove(test_file)
        return False


def test_logmaster_stats():
    """LogMaster show_stats 메서드 테스트"""
    print("\nTesting LogMaster.show_stats()...")

    # 임시 로그 파일 생성
    test_file = 'test_sample.log'
    with open(test_file, 'w') as f:
        # INFO 3개, WARN 2개, ERROR 1개
        f.write("2024-01-15 08:15:23 INFO Log 1\n")
        f.write("2024-01-15 08:15:24 INFO Log 2\n")
        f.write("2024-01-15 08:15:25 INFO Log 3\n")
        f.write("2024-01-15 08:15:26 WARN Log 4\n")
        f.write("2024-01-15 08:15:27 WARN Log 5\n")
        f.write("2024-01-15 08:15:28 ERROR Log 6\n")

    try:
        logmaster = LogMaster()
        logmaster.load(test_file)

        # show_stats는 출력 함수이므로, logs 내용이 올바른지 확인
        assert len(logmaster.logs) == 6, "❌ 로그 개수가 6개가 아닙니다"

        level_counts = Counter(log.level for log in logmaster.logs)
        assert level_counts['INFO'] == 3, f"❌ INFO 개수가 3개가 아닙니다: {level_counts['INFO']}"
        assert level_counts['WARN'] == 2, f"❌ WARN 개수가 2개가 아닙니다: {level_counts['WARN']}"
        assert level_counts['ERROR'] == 1, f"❌ ERROR 개수가 1개가 아닙니다: {level_counts['ERROR']}"

        # 시간 범위 확인
        first_time = logmaster.logs[0].timestamp
        last_time = logmaster.logs[-1].timestamp
        duration = last_time - first_time
        assert duration.total_seconds() == 5, "❌ 시간 범위가 5초가 아닙니다"

        print("  ✅ 통계 계산 성공")

        # 실제 출력 테스트 (에러 없이 실행되는지만 확인)
        print("\n  실제 출력 테스트:")
        logmaster.show_stats()

        # 정리
        os.remove(test_file)
        return True

    except Exception as e:
        print(f"  ❌ 통계 계산 실패: {e}")
        if os.path.exists(test_file):
            os.remove(test_file)
        return False


def main():
    """메인 테스트 실행"""
    print("=" * 60)
    print("  Step 1: 자동 채점 시스템")
    print("=" * 60)

    results = []

    # 테스트 실행
    results.append(("LogEntry 클래스", test_log_entry()))
    results.append(("LogMaster.load()", test_logmaster_load()))
    results.append(("LogMaster.show_stats()", test_logmaster_stats()))

    # 결과 요약
    print("\n" + "=" * 60)
    print("  테스트 결과")
    print("=" * 60)

    passed = 0
    for name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status}: {name}")
        if result:
            passed += 1

    total = len(results)
    print("=" * 60)
    print(f"  {passed}/{total} 테스트 통과 ({passed/total*100:.0f}%)")
    print("=" * 60)

    if passed == total:
        print("\n🎉 축하합니다! Step 1을 완료했습니다!")
        print("다음은 Step 2: 필터링 & 검색으로 넘어가세요!\n")
        return 0
    else:
        print(f"\n💪 {total - passed}개 테스트가 실패했습니다. 다시 시도해보세요!\n")
        return 1


if __name__ == '__main__':
    sys.exit(main())
