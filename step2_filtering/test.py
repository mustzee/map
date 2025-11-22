#!/usr/bin/env python3
"""
Step 2 자동 채점 시스템: 필터링 & 검색
"""
import sys
import os
from datetime import datetime

sys.path.insert(0, os.path.dirname(__file__))

try:
    from logmaster import LogEntry, LogMaster
except ImportError:
    print("❌ logmaster.py를 찾을 수 없거나 import할 수 없습니다!")
    print("Step 1의 코드를 복사하고 새 기능을 추가했나요?")
    sys.exit(1)


def test_filter_by_level():
    """레벨별 필터링 테스트"""
    print("Testing filter_logs(level=...)...")
    
    # 테스트 로그 파일 생성
    test_file = 'test_filter.log'
    with open(test_file, 'w') as f:
        f.write("2024-01-15 08:00:00 INFO First log\n")
        f.write("2024-01-15 08:01:00 ERROR Error log 1\n")
        f.write("2024-01-15 08:02:00 WARN Warning log\n")
        f.write("2024-01-15 08:03:00 ERROR Error log 2\n")
        f.write("2024-01-15 08:04:00 INFO Second log\n")
    
    try:
        logmaster = LogMaster()
        logmaster.load(test_file)
        
        # filter_logs 메서드가 있는지 확인
        if not hasattr(logmaster, 'filter_logs'):
            print("  ❌ LogMaster에 filter_logs 메서드가 없습니다")
            return False
        
        # ERROR만 필터링
        errors = logmaster.filter_logs(level='ERROR')
        assert len(errors) == 2, f"❌ ERROR 로그가 2개여야 하는데 {len(errors)}개입니다"
        assert all(log.level == 'ERROR' for log in errors), "❌ 모든 로그가 ERROR여야 합니다"
        
        # INFO만 필터링
        infos = logmaster.filter_logs(level='INFO')
        assert len(infos) == 2, f"❌ INFO 로그가 2개여야 하는데 {len(infos)}개입니다"
        
        # WARN만 필터링
        warns = logmaster.filter_logs(level='WARN')
        assert len(warns) == 1, f"❌ WARN 로그가 1개여야 하는데 {len(warns)}개입니다"
        
        print("  ✅ 레벨별 필터링 성공")
        os.remove(test_file)
        return True
        
    except Exception as e:
        print(f"  ❌ 레벨별 필터링 실패: {e}")
        if os.path.exists(test_file):
            os.remove(test_file)
        return False


def test_filter_by_time():
    """시간 범위 필터링 테스트"""
    print("\nTesting filter_logs(after=..., before=...)...")
    
    test_file = 'test_time_filter.log'
    with open(test_file, 'w') as f:
        f.write("2024-01-15 08:00:00 INFO Log at 8:00\n")
        f.write("2024-01-15 09:00:00 INFO Log at 9:00\n")
        f.write("2024-01-15 10:00:00 INFO Log at 10:00\n")
        f.write("2024-01-15 11:00:00 INFO Log at 11:00\n")
        f.write("2024-01-15 12:00:00 INFO Log at 12:00\n")
    
    try:
        logmaster = LogMaster()
        logmaster.load(test_file)
        
        # after 필터링
        after_10 = logmaster.filter_logs(after="2024-01-15 10:00:00")
        assert len(after_10) == 3, f"❌ 10:00 이후 로그가 3개여야 하는데 {len(after_10)}개입니다"
        
        # before 필터링
        before_10 = logmaster.filter_logs(before="2024-01-15 10:00:00")
        assert len(before_10) == 3, f"❌ 10:00 이전 로그가 3개여야 하는데 {len(before_10)}개입니다"
        
        # after + before 조합
        range_logs = logmaster.filter_logs(
            after="2024-01-15 09:00:00",
            before="2024-01-15 11:00:00"
        )
        assert len(range_logs) == 3, f"❌ 9:00~11:00 로그가 3개여야 하는데 {len(range_logs)}개입니다"
        
        print("  ✅ 시간 범위 필터링 성공")
        os.remove(test_file)
        return True
        
    except Exception as e:
        print(f"  ❌ 시간 범위 필터링 실패: {e}")
        if os.path.exists(test_file):
            os.remove(test_file)
        return False


def test_combined_filters():
    """복합 필터링 테스트"""
    print("\nTesting combined filters...")
    
    test_file = 'test_combined.log'
    with open(test_file, 'w') as f:
        f.write("2024-01-15 08:00:00 INFO Info at 8\n")
        f.write("2024-01-15 09:00:00 ERROR Error at 9\n")
        f.write("2024-01-15 10:00:00 INFO Info at 10\n")
        f.write("2024-01-15 11:00:00 ERROR Error at 11\n")
        f.write("2024-01-15 12:00:00 INFO Info at 12\n")
    
    try:
        logmaster = LogMaster()
        logmaster.load(test_file)
        
        # ERROR + after 10:00
        result = logmaster.filter_logs(
            level='ERROR',
            after="2024-01-15 10:00:00"
        )
        assert len(result) == 1, f"❌ 10:00 이후 ERROR가 1개여야 하는데 {len(result)}개입니다"
        assert result[0].timestamp.hour == 11, "❌ 11시 로그여야 합니다"
        
        print("  ✅ 복합 필터링 성공")
        os.remove(test_file)
        return True
        
    except Exception as e:
        print(f"  ❌ 복합 필터링 실패: {e}")
        if os.path.exists(test_file):
            os.remove(test_file)
        return False


def test_search():
    """키워드 검색 테스트"""
    print("\nTesting search()...")
    
    test_file = 'test_search.log'
    with open(test_file, 'w') as f:
        f.write("2024-01-15 08:00:00 INFO Database connection established\n")
        f.write("2024-01-15 08:01:00 ERROR Database connection failed\n")
        f.write("2024-01-15 08:02:00 INFO User login successful\n")
        f.write("2024-01-15 08:03:00 ERROR File not found\n")
        f.write("2024-01-15 08:04:00 INFO Database query completed\n")
    
    try:
        logmaster = LogMaster()
        logmaster.load(test_file)
        
        if not hasattr(logmaster, 'search'):
            print("  ❌ LogMaster에 search 메서드가 없습니다")
            return False
        
        # "database" 검색
        results = logmaster.search("database")
        assert len(results) == 3, f"❌ 'database' 검색 결과가 3개여야 하는데 {len(results)}개입니다"
        
        # "connection" 검색
        results = logmaster.search("connection")
        assert len(results) == 2, f"❌ 'connection' 검색 결과가 2개여야 하는데 {len(results)}개입니다"
        
        # 대소문자 무시 확인
        results_upper = logmaster.search("DATABASE")
        assert len(results_upper) == 3, "❌ 대소문자 구분 없이 검색되어야 합니다"
        
        # 없는 키워드
        results = logmaster.search("nonexistent")
        assert len(results) == 0, "❌ 없는 키워드는 결과가 0개여야 합니다"
        
        print("  ✅ 키워드 검색 성공")
        os.remove(test_file)
        return True
        
    except Exception as e:
        print(f"  ❌ 키워드 검색 실패: {e}")
        if os.path.exists(test_file):
            os.remove(test_file)
        return False


def test_save_logs():
    """로그 저장 기능 테스트"""
    print("\nTesting save_logs()...")
    
    test_file = 'test_save_input.log'
    output_file = 'test_save_output.log'
    
    with open(test_file, 'w') as f:
        f.write("2024-01-15 08:00:00 ERROR Error 1\n")
        f.write("2024-01-15 08:01:00 INFO Info 1\n")
        f.write("2024-01-15 08:02:00 ERROR Error 2\n")
    
    try:
        logmaster = LogMaster()
        logmaster.load(test_file)
        
        if not hasattr(logmaster, 'save_logs'):
            print("  ❌ LogMaster에 save_logs 메서드가 없습니다")
            return False
        
        # ERROR만 필터링해서 저장
        errors = logmaster.filter_logs(level='ERROR')
        logmaster.save_logs(errors, output_file)
        
        # 저장된 파일 확인
        assert os.path.exists(output_file), "❌ 파일이 저장되지 않았습니다"
        
        with open(output_file, 'r') as f:
            lines = [line.strip() for line in f if line.strip()]
        
        assert len(lines) == 2, f"❌ 저장된 로그가 2개여야 하는데 {len(lines)}개입니다"
        assert 'ERROR' in lines[0], "❌ 첫 번째 줄에 ERROR가 있어야 합니다"
        assert 'ERROR' in lines[1], "❌ 두 번째 줄에 ERROR가 있어야 합니다"
        
        print("  ✅ 로그 저장 성공")
        
        os.remove(test_file)
        os.remove(output_file)
        return True
        
    except Exception as e:
        print(f"  ❌ 로그 저장 실패: {e}")
        for f in [test_file, output_file]:
            if os.path.exists(f):
                os.remove(f)
        return False


def main():
    """메인 테스트 실행"""
    print("=" * 60)
    print("  Step 2: 자동 채점 시스템 - 필터링 & 검색")
    print("=" * 60)
    
    results = []
    
    # 테스트 실행
    results.append(("레벨별 필터링", test_filter_by_level()))
    results.append(("시간 범위 필터링", test_filter_by_time()))
    results.append(("복합 필터링", test_combined_filters()))
    results.append(("키워드 검색", test_search()))
    results.append(("로그 저장", test_save_logs()))
    
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
        print("\n🎉 축하합니다! Step 2를 완료했습니다!")
        print("다음은 Step 3: 패턴 분석으로 넘어가세요!\n")
        return 0
    else:
        print(f"\n💪 {total - passed}개 테스트가 실패했습니다. 다시 시도해보세요!")
        print("힌트: solution.py를 참고하세요.\n")
        return 1


if __name__ == '__main__':
    sys.exit(main())
