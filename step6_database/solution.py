#!/usr/bin/env python3
"""LogMaster Step 6: 데이터베이스 연동 - 정답 예시"""
from step5_pandas_advanced.solution import *
import sqlite3

class LogMaster(LogMaster):  # Step 5 확장
    def init_database(self, db_path='logs.db'):
        """데이터베이스 초기화"""
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME,
                level TEXT,
                message TEXT,
                imported_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        conn.commit()
        conn.close()
        print(f"✓ Database initialized at {db_path}")
    
    def import_to_db(self, db_path='logs.db'):
        """현재 로드된 로그를 DB에 저장"""
        self.init_database(db_path)
        conn = sqlite3.connect(db_path)
        
        df = self.to_dataframe()
        df.to_sql('logs', conn, if_exists='append', index=True, index_label='timestamp')
        
        conn.close()
        print(f"✓ Imported {len(self.logs)} entries to database")
    
    def query_db(self, sql, db_path='logs.db'):
        """SQL 쿼리 실행 및 결과 반환"""
        conn = sqlite3.connect(db_path)
        df = pd.read_sql_query(sql, conn)
        conn.close()
        return df
    
    def export_from_db(self, db_path='logs.db', output_file='export.csv'):
        """DB의 모든 로그를 CSV로 내보내기"""
        df = self.query_db("SELECT * FROM logs", db_path)
        df.to_csv(output_file, index=False)
        print(f"✓ Exported {len(df)} entries to {output_file}")

if __name__ == '__main__':
    main()
