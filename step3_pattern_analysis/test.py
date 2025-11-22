#!/usr/bin/env python3
"""Step 3 자동 채점: 패턴 분석"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

try:
    from logmaster import LogMaster
except ImportError:
    print("❌ logmaster.py import 실패! Step 2 코드를 복사했나요?")
    sys.exit(1)

def test_count_error_messages():
    """에러 메시지 카운트 테스트"""
    print("Testing count_error_messages()...")
    test_file = 'test.log'
    with open(test_file, 'w') as f:
        f.write("2024-01-15 08:00:00 ERROR Connection timeout\n")
        f.write("2024-01-15 08:01:00 ERROR File not found\n")
        f.write("2024-01-15 08:02:00 ERROR Connection timeout\n")
        f.write("2024-01-15 08:03:00 INFO Normal log\n")
        f.write("2024-01-15 08:04:00 ERROR Connection timeout\n")
    
    try:
        lm = LogMaster()
        lm.load(test_file)
        
        if not hasattr(lm, 'count_error_messages'):
            print("  ❌ count_error_messages 메서드가 없습니다")
            return False
        
        counts = lm.count_error_messages()
        assert counts['Connection timeout'] == 3, "❌ 'Connection timeout' 카운트 오류"
        assert counts['File not found'] == 1, "❌ 'File not found' 카운트 오류"
        
        print("  ✅ 에러 메시지 카운트 성공")
        os.remove(test_file)
        return True
    except Exception as e:
        print(f"  ❌ 실패: {e}")
        if os.path.exists(test_file):
            os.remove(test_file)
        return False

def test_hourly_distribution():
    """시간대별 분포 테스트"""
    print("\nTesting hourly_distribution()...")
    test_file = 'test.log'
    with open(test_file, 'w') as f:
        f.write("2024-01-15 08:00:00 INFO Log 1\n")
        f.write("2024-01-15 08:15:00 ERROR Error 1\n")
        f.write("2024-01-15 09:00:00 INFO Log 2\n")
        f.write("2024-01-15 09:30:00 WARN Warn 1\n")
        f.write("2024-01-15 09:45:00 ERROR Error 2\n")
    
    try:
        lm = LogMaster()
        lm.load(test_file)
        
        if not hasattr(lm, 'hourly_distribution'):
            print("  ❌ hourly_distribution 메서드가 없습니다")
            return False
        
        dist = lm.hourly_distribution()
        assert 8 in dist, "❌ 8시 데이터가 없습니다"
        assert 9 in dist, "❌ 9시 데이터가 없습니다"
        assert dist[8]['INFO'] == 1, "❌ 8시 INFO 카운트 오류"
        assert dist[8]['ERROR'] == 1, "❌ 8시 ERROR 카운트 오류"
        assert dist[9]['INFO'] == 1, "❌ 9시 INFO 카운트 오류"
        assert dist[9]['WARN'] == 1, "❌ 9시 WARN 카운트 오류"
        assert dist[9]['ERROR'] == 1, "❌ 9시 ERROR 카운트 오류"
        
        print("  ✅ 시간대별 분포 성공")
        os.remove(test_file)
        return True
    except Exception as e:
        print(f"  ❌ 실패: {e}")
        if os.path.exists(test_file):
            os.remove(test_file)
        return False

def test_draw_bar_chart():
    """ASCII 차트 테스트"""
    print("\nTesting draw_bar_chart()...")
    try:
        lm = LogMaster()
        
        if not hasattr(lm, 'draw_bar_chart'):
            print("  ❌ draw_bar_chart 메서드가 없습니다")
            return False
        
        chart = lm.draw_bar_chart(5, 10, 10)
        assert len(chart) == 10, "❌ 차트 길이가 10이어야 합니다"
        assert '█' in chart or '░' in chart, "❌ 차트에 막대가 없습니다"
        
        full_chart = lm.draw_bar_chart(10, 10, 10)
        assert full_chart.count('█') == 10, "❌ 최대값일 때 모두 채워져야 합니다"
        
        print("  ✅ ASCII 차트 성공")
        return True
    except Exception as e:
        print(f"  ❌ 실패: {e}")
        return False

def main():
    print("=" * 60)
    print("  Step 3: 자동 채점 - 패턴 분석")
    print("=" * 60)
    
    results = [
        ("에러 메시지 카운트", test_count_error_messages()),
        ("시간대별 분포", test_hourly_distribution()),
        ("ASCII 차트", test_draw_bar_chart()),
    ]
    
    print("\n" + "=" * 60)
    print("  테스트 결과")
    print("=" * 60)
    
    passed = sum(1 for _, r in results if r)
    total = len(results)
    
    for name, result in results:
        print(f"{'✅ PASS' if result else '❌ FAIL'}: {name}")
    
    print("=" * 60)
    print(f"  {passed}/{total} 테스트 통과 ({passed/total*100:.0f}%)")
    print("=" * 60)
    
    if passed == total:
        print("\n🎉 Step 3 완료! Step 4로 넘어가세요!\n")
        return 0
    else:
        print(f"\n💪 {total-passed}개 실패. 다시 도전!\n")
        return 1

if __name__ == '__main__':
    sys.exit(main())
