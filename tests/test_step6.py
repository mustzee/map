"""
Step 6: Pandas와 데이터베이스 연동 자동 채점 테스트
"""
import pytest
import pandas as pd
import sqlite3
import os
import sys
sys.path.insert(0, '/home/user/map')

from exercises.step6_exercises import (
    save_dataframe_to_db,
    load_table_to_dataframe,
    query_to_dataframe,
    filter_and_save,
    aggregate_and_save,
    merge_tables,
    add_calculated_column,
    get_top_n_records,
    calculate_statistics,
    pivot_and_save
)


class TestStep6:
    """Step 6 테스트 클래스"""

    @pytest.fixture
    def sample_df(self):
        """샘플 DataFrame"""
        return pd.DataFrame({
            'name': ['Alice', 'Bob', 'Charlie', 'David'],
            'age': [25, 30, 35, 28],
            'score': [85.5, 90.0, 88.5, 92.0]
        })

    @pytest.fixture
    def test_db_path(self, tmp_path):
        """임시 데이터베이스 경로"""
        return str(tmp_path / "test.db")

    def test_save_dataframe_to_db(self, sample_df, test_db_path):
        """save_dataframe_to_db 함수 테스트"""
        save_dataframe_to_db(sample_df, test_db_path, 'students')

        # 데이터베이스에 저장되었는지 확인
        conn = sqlite3.connect(test_db_path)
        df = pd.read_sql('SELECT * FROM students', conn)
        conn.close()

        assert len(df) == 4
        assert list(df.columns) == ['name', 'age', 'score']

    def test_load_table_to_dataframe(self, sample_df, test_db_path):
        """load_table_to_dataframe 함수 테스트"""
        # 먼저 데이터 저장
        conn = sqlite3.connect(test_db_path)
        sample_df.to_sql('students', conn, if_exists='replace', index=False)
        conn.close()

        # 읽기 테스트
        df = load_table_to_dataframe(test_db_path, 'students')

        assert len(df) == 4
        assert list(df.columns) == ['name', 'age', 'score']
        pd.testing.assert_frame_equal(df, sample_df)

    def test_query_to_dataframe(self, sample_df, test_db_path):
        """query_to_dataframe 함수 테스트"""
        # 먼저 데이터 저장
        conn = sqlite3.connect(test_db_path)
        sample_df.to_sql('students', conn, if_exists='replace', index=False)
        conn.close()

        # 쿼리 테스트
        df = query_to_dataframe(test_db_path, 'SELECT * FROM students WHERE age > 28')

        assert len(df) == 2
        assert all(df['age'] > 28)

    def test_filter_and_save(self, sample_df, test_db_path):
        """filter_and_save 함수 테스트"""
        # 먼저 데이터 저장
        conn = sqlite3.connect(test_db_path)
        sample_df.to_sql('students', conn, if_exists='replace', index=False)
        conn.close()

        # 필터링 및 저장
        filter_and_save(test_db_path, 'students', 'filtered_students', 'age', 28)

        # 확인
        conn = sqlite3.connect(test_db_path)
        df = pd.read_sql('SELECT * FROM filtered_students', conn)
        conn.close()

        assert len(df) == 2
        assert all(df['age'] > 28)

    def test_aggregate_and_save(self, test_db_path):
        """aggregate_and_save 함수 테스트"""
        # 테스트 데이터
        df = pd.DataFrame({
            'team': ['A', 'A', 'B', 'B', 'A'],
            'score': [80, 90, 85, 95, 88]
        })

        conn = sqlite3.connect(test_db_path)
        df.to_sql('scores', conn, if_exists='replace', index=False)
        conn.close()

        # 집계 및 저장
        aggregate_and_save(test_db_path, 'scores', 'team_stats', 'team', 'score')

        # 확인
        conn = sqlite3.connect(test_db_path)
        result = pd.read_sql('SELECT * FROM team_stats', conn)
        conn.close()

        assert len(result) == 2
        assert 'mean' in result.columns
        assert 'sum' in result.columns

        # A팀 확인 (80, 90, 88의 평균과 합)
        team_a = result[result['team'] == 'A'].iloc[0]
        assert abs(team_a['mean'] - 86.0) < 0.01
        assert team_a['sum'] == 258

    def test_merge_tables(self, test_db_path):
        """merge_tables 함수 테스트"""
        # 테스트 데이터
        df1 = pd.DataFrame({
            'id': [1, 2, 3],
            'name': ['Alice', 'Bob', 'Charlie']
        })
        df2 = pd.DataFrame({
            'id': [1, 2, 4],
            'score': [85, 90, 95]
        })

        conn = sqlite3.connect(test_db_path)
        df1.to_sql('students', conn, if_exists='replace', index=False)
        df2.to_sql('scores', conn, if_exists='replace', index=False)
        conn.close()

        # 병합
        merge_tables(test_db_path, 'students', 'scores', 'id', 'merged')

        # 확인
        conn = sqlite3.connect(test_db_path)
        result = pd.read_sql('SELECT * FROM merged', conn)
        conn.close()

        # Inner join이므로 id 1, 2만 남음
        assert len(result) == 2
        assert 'name' in result.columns
        assert 'score' in result.columns

    def test_add_calculated_column(self, test_db_path):
        """add_calculated_column 함수 테스트"""
        # 테스트 데이터
        df = pd.DataFrame({
            'A': [1, 2, 3],
            'B': [4, 5, 6]
        })

        conn = sqlite3.connect(test_db_path)
        df.to_sql('numbers', conn, if_exists='replace', index=False)
        conn.close()

        # 계산된 열 추가
        add_calculated_column(test_db_path, 'numbers', 'A', 'B', 'sum')

        # 확인
        conn = sqlite3.connect(test_db_path)
        result = pd.read_sql('SELECT * FROM numbers', conn)
        conn.close()

        assert 'sum' in result.columns
        assert list(result['sum']) == [5, 7, 9]

    def test_get_top_n_records(self, sample_df, test_db_path):
        """get_top_n_records 함수 테스트"""
        # 먼저 데이터 저장
        conn = sqlite3.connect(test_db_path)
        sample_df.to_sql('students', conn, if_exists='replace', index=False)
        conn.close()

        # 상위 2개 조회
        df = get_top_n_records(test_db_path, 'students', 'score', 2)

        assert len(df) == 2
        # 내림차순이므로 첫 번째는 David (92.0)
        assert df.iloc[0]['score'] == 92.0
        assert df.iloc[1]['score'] == 90.0

    def test_calculate_statistics(self, sample_df, test_db_path):
        """calculate_statistics 함수 테스트"""
        # 먼저 데이터 저장
        conn = sqlite3.connect(test_db_path)
        sample_df.to_sql('students', conn, if_exists='replace', index=False)
        conn.close()

        # 통계 계산
        stats = calculate_statistics(test_db_path, 'students', 'score')

        assert 'mean' in stats
        assert 'median' in stats
        assert 'std' in stats
        assert 'min' in stats
        assert 'max' in stats

        assert abs(stats['mean'] - 89.0) < 0.01
        assert stats['min'] == 85.5
        assert stats['max'] == 92.0

    def test_pivot_and_save(self, test_db_path):
        """pivot_and_save 함수 테스트"""
        # 테스트 데이터
        df = pd.DataFrame({
            'date': ['2024-01', '2024-01', '2024-02', '2024-02'],
            'team': ['A', 'B', 'A', 'B'],
            'score': [80, 90, 85, 95]
        })

        conn = sqlite3.connect(test_db_path)
        df.to_sql('scores', conn, if_exists='replace', index=False)
        conn.close()

        # 피벗
        pivot_and_save(test_db_path, 'scores', 'pivot_scores', 'date', 'team', 'score')

        # 확인
        conn = sqlite3.connect(test_db_path)
        result = pd.read_sql('SELECT * FROM pivot_scores', conn)
        conn.close()

        # 피벗 테이블이 생성되었는지 확인
        assert len(result) == 2  # 2개의 날짜


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
