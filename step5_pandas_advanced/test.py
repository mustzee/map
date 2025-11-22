#!/usr/bin/env python3
"""Step 5 자동 채점: Pandas"""
import sys, os, pandas as pd
sys.path.insert(0, os.path.dirname(__file__))

try:
    from logmaster import LogMaster
except ImportError:
    print("❌ logmaster.py import 실패!")
    sys.exit(1)

def test_to_dataframe():
    print("Testing to_dataframe()...")
    test_file = 'test.log'
    with open(test_file, 'w') as f:
        f.write("2024-01-15 08:00:00 INFO Log 1\n")
        f.write("2024-01-15 09:00:00 ERROR Log 2\n")
    
    try:
        lm = LogMaster()
        lm.load(test_file)
        
        if not hasattr(lm, 'to_dataframe'):
            print("  ❌ to_dataframe 메서드가 없습니다")
            return False
        
        df = lm.to_dataframe()
        assert isinstance(df, pd.DataFrame), "❌ DataFrame이 아닙니다"
        assert len(df) == 2, "❌ 2개 행이어야 합니다"
        assert 'level' in df.columns, "❌ level 열이 없습니다"
        assert 'message' in df.columns, "❌ message 열이 없습니다"
        
        print("  ✅ DataFrame 변환 성공")
        os.remove(test_file)
        return True
    except Exception as e:
        print(f"  ❌ 실패: {e}")
        if os.path.exists(test_file):
            os.remove(test_file)
        return False

def test_create_pivot_table():
    print("\nTesting create_pivot_table()...")
    test_file = 'test.log'
    with open(test_file, 'w') as f:
        f.write("2024-01-15 08:00:00 INFO I1\n")
        f.write("2024-01-15 08:15:00 ERROR E1\n")
        f.write("2024-01-15 09:00:00 INFO I2\n")
    
    try:
        lm = LogMaster()
        lm.load(test_file)
        
        if not hasattr(lm, 'create_pivot_table'):
            print("  ❌ create_pivot_table 메서드가 없습니다")
            return False
        
        pivot = lm.create_pivot_table()
        assert isinstance(pivot, pd.DataFrame), "❌ DataFrame이 아닙니다"
        assert 8 in pivot.index, "❌ 8시 데이터가 없습니다"
        
        print("  ✅ 피벗 테이블 성공")
        os.remove(test_file)
        return True
    except Exception as e:
        print(f"  ❌ 실패: {e}")
        if os.path.exists(test_file):
            os.remove(test_file)
        return False

def test_generate_html_report():
    print("\nTesting generate_html_report()...")
    test_file = 'test.log'
    html_file = 'test_report.html'
    
    with open(test_file, 'w') as f:
        f.write("2024-01-15 08:00:00 INFO Test\n")
    
    try:
        lm = LogMaster()
        lm.load(test_file)
        
        if not hasattr(lm, 'generate_html_report'):
            print("  ❌ generate_html_report 메서드가 없습니다")
            return False
        
        lm.generate_html_report(html_file)
        assert os.path.exists(html_file), "❌ HTML 파일이 생성되지 않았습니다"
        
        with open(html_file, 'r') as f:
            content = f.read()
            assert '<html>' in content, "❌ HTML 형식이 아닙니다"
            assert 'Log Analysis' in content, "❌ 제목이 없습니다"
        
        print("  ✅ HTML 리포트 생성 성공")
        os.remove(test_file)
        os.remove(html_file)
        return True
    except Exception as e:
        print(f"  ❌ 실패: {e}")
        for f in [test_file, html_file]:
            if os.path.exists(f):
                os.remove(f)
        return False

def main():
    print("=" * 60)
    print("  Step 5: 자동 채점 - Pandas 고급")
    print("=" * 60)
    
    results = [
        ("DataFrame 변환", test_to_dataframe()),
        ("피벗 테이블", test_create_pivot_table()),
        ("HTML 리포트", test_generate_html_report()),
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
        print("\n🎉 Step 5 완료! 마지막 Step 6로!\n")
        return 0
    return 1

if __name__ == '__main__':
    sys.exit(main())
