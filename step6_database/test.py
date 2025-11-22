#!/usr/bin/env python3
"""Step 6 자동 채점: 데이터베이스"""
import sys, os, sqlite3, pandas as pd
sys.path.insert(0, os.path.dirname(__file__))

try:
    from logmaster import LogMaster
except ImportError:
    print("❌ logmaster.py import 실패!")
    sys.exit(1)

def test_init_database():
    print("Testing init_database()...")
    db_file = 'test.db'
    
    try:
        lm = LogMaster()
        
        if not hasattr(lm, 'init_database'):
            print("  ❌ init_database 메서드가 없습니다")
            return False
        
        lm.init_database(db_file)
        assert os.path.exists(db_file), "❌ DB 파일이 생성되지 않았습니다"
        
        # 테이블 확인
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='logs'")
        table = cursor.fetchone()
        conn.close()
        
        assert table is not None, "❌ logs 테이블이 생성되지 않았습니다"
        
        print("  ✅ DB 초기화 성공")
        os.remove(db_file)
        return True
    except Exception as e:
        print(f"  ❌ 실패: {e}")
        if os.path.exists(db_file):
            os.remove(db_file)
        return False

def test_import_to_db():
    print("\nTesting import_to_db()...")
    log_file = 'test.log'
    db_file = 'test.db'
    
    with open(log_file, 'w') as f:
        f.write("2024-01-15 08:00:00 INFO Test 1\n")
        f.write("2024-01-15 09:00:00 ERROR Test 2\n")
    
    try:
        lm = LogMaster()
        lm.load(log_file)
        
        if not hasattr(lm, 'import_to_db'):
            print("  ❌ import_to_db 메서드가 없습니다")
            return False
        
        lm.import_to_db(db_file)
        
        # DB 데이터 확인
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM logs")
        count = cursor.fetchone()[0]
        conn.close()
        
        assert count == 2, f"❌ DB에 2개 로그가 있어야 하는데 {count}개입니다"
        
        print("  ✅ DB 임포트 성공")
        os.remove(log_file)
        os.remove(db_file)
        return True
    except Exception as e:
        print(f"  ❌ 실패: {e}")
        for f in [log_file, db_file]:
            if os.path.exists(f):
                os.remove(f)
        return False

def test_query_db():
    print("\nTesting query_db()...")
    log_file = 'test.log'
    db_file = 'test.db'
    
    with open(log_file, 'w') as f:
        f.write("2024-01-15 08:00:00 INFO Info log\n")
        f.write("2024-01-15 09:00:00 ERROR Error log\n")
        f.write("2024-01-15 10:00:00 ERROR Another error\n")
    
    try:
        lm = LogMaster()
        lm.load(log_file)
        lm.import_to_db(db_file)
        
        if not hasattr(lm, 'query_db'):
            print("  ❌ query_db 메서드가 없습니다")
            return False
        
        # ERROR만 쿼리
        result = lm.query_db("SELECT * FROM logs WHERE level='ERROR'", db_file)
        assert isinstance(result, pd.DataFrame), "❌ DataFrame이 아닙니다"
        assert len(result) == 2, f"❌ ERROR 로그가 2개여야 하는데 {len(result)}개입니다"
        
        print("  ✅ DB 쿼리 성공")
        os.remove(log_file)
        os.remove(db_file)
        return True
    except Exception as e:
        print(f"  ❌ 실패: {e}")
        for f in [log_file, db_file]:
            if os.path.exists(f):
                os.remove(f)
        return False

def test_export_from_db():
    print("\nTesting export_from_db()...")
    log_file = 'test.log'
    db_file = 'test.db'
    csv_file = 'test_export.csv'
    
    with open(log_file, 'w') as f:
        f.write("2024-01-15 08:00:00 INFO Test\n")
    
    try:
        lm = LogMaster()
        lm.load(log_file)
        lm.import_to_db(db_file)
        
        if not hasattr(lm, 'export_from_db'):
            print("  ❌ export_from_db 메서드가 없습니다")
            return False
        
        lm.export_from_db(db_file, csv_file)
        assert os.path.exists(csv_file), "❌ CSV 파일이 생성되지 않았습니다"
        
        df = pd.read_csv(csv_file)
        assert len(df) > 0, "❌ CSV가 비어있습니다"
        
        print("  ✅ DB 내보내기 성공")
        for f in [log_file, db_file, csv_file]:
            if os.path.exists(f):
                os.remove(f)
        return True
    except Exception as e:
        print(f"  ❌ 실패: {e}")
        for f in [log_file, db_file, csv_file]:
            if os.path.exists(f):
                os.remove(f)
        return False

def main():
    print("=" * 60)
    print("  Step 6: 자동 채점 - 데이터베이스")
    print("=" * 60)
    
    results = [
        ("DB 초기화", test_init_database()),
        ("DB 임포트", test_import_to_db()),
        ("DB 쿼리", test_query_db()),
        ("DB 내보내기", test_export_from_db()),
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
        print("\n🎉🎉🎉 축하합니다! 모든 단계 완료! 🎉🎉🎉")
        print("완전한 로그 분석 도구를 만들었습니다!\n")
        return 0
    else:
        print(f"\n💪 {total-passed}개 실패. 다시 도전!\n")
        return 1

if __name__ == '__main__':
    sys.exit(main())
