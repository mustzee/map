#!/usr/bin/env python3
"""Step 4 자동 채점: NumPy 통계"""
import sys, os, numpy as np
sys.path.insert(0, os.path.dirname(__file__))

try:
    from logmaster import LogMaster
except ImportError:
    print("❌ logmaster.py import 실패!")
    sys.exit(1)

def test_get_hourly_error_counts():
    print("Testing get_hourly_error_counts()...")
    test_file = 'test.log'
    with open(test_file, 'w') as f:
        f.write("2024-01-15 08:00:00 ERROR E1\n")
        f.write("2024-01-15 08:15:00 ERROR E2\n")
        f.write("2024-01-15 09:00:00 INFO I1\n")
        f.write("2024-01-15 10:00:00 ERROR E3\n")
    
    try:
        lm = LogMaster()
        lm.load(test_file)
        
        if not hasattr(lm, 'get_hourly_error_counts'):
            print("  ❌ get_hourly_error_counts 메서드가 없습니다")
            return False
        
        hours, counts = lm.get_hourly_error_counts()
        assert isinstance(counts, np.ndarray), "❌ counts가 NumPy 배열이어야 합니다"
        assert len(hours) == 2, f"❌ 시간대가 2개여야 하는데 {len(hours)}개입니다"
        assert counts[0] == 2, "❌ 8시 에러가 2개여야 합니다"
        assert counts[1] == 1, "❌ 10시 에러가 1개여야 합니다"
        
        print("  ✅ NumPy 배열 변환 성공")
        os.remove(test_file)
        return True
    except Exception as e:
        print(f"  ❌ 실패: {e}")
        if os.path.exists(test_file):
            os.remove(test_file)
        return False

def test_detect_anomalies():
    print("\nTesting detect_anomalies()...")
    test_file = 'test.log'
    with open(test_file, 'w') as f:
        # 정상: 1개씩, 이상: 10개
        for hour in range(8, 13):
            count = 10 if hour == 10 else 1
            for i in range(count):
                f.write(f"2024-01-15 {hour:02d}:00:00 ERROR E\n")
    
    try:
        lm = LogMaster()
        lm.load(test_file)
        
        if not hasattr(lm, 'detect_anomalies'):
            print("  ❌ detect_anomalies 메서드가 없습니다")
            return False
        
        anomalies = lm.detect_anomalies(threshold=2.0)
        assert len(anomalies) > 0, "❌ 이상치가 탐지되어야 합니다"
        
        # 10시에 이상치가 있어야 함
        anomaly_hours = [a[0] for a in anomalies]
        assert 10 in anomaly_hours, "❌ 10시가 이상치로 탐지되어야 합니다"
        
        print("  ✅ 이상치 탐지 성공")
        os.remove(test_file)
        return True
    except Exception as e:
        print(f"  ❌ 실패: {e}")
        if os.path.exists(test_file):
            os.remove(test_file)
        return False

def main():
    print("=" * 60)
    print("  Step 4: 자동 채점 - NumPy 통계")
    print("=" * 60)
    
    results = [
        ("NumPy 배열 변환", test_get_hourly_error_counts()),
        ("이상치 탐지", test_detect_anomalies()),
    ]
    
    print("\n" + "=" * 60)
    passed = sum(1 for _, r in results if r)
    total = len(results)
    
    for name, result in results:
        print(f"{'✅ PASS' if result else '❌ FAIL'}: {name}")
    
    print("=" * 60)
    print(f"  {passed}/{total} 테스트 통과")
    print("=" * 60)
    
    if passed == total:
        print("\n🎉 Step 4 완료! Step 5로!\n")
        return 0
    return 1

if __name__ == '__main__':
    sys.exit(main())
