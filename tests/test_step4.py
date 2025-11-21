"""
Step 4: Pandas 데이터 처리 자동 채점 테스트
"""
import pytest
import pandas as pd
import numpy as np
import sys
sys.path.insert(0, '/home/user/map')

from exercises.step4_exercises import (
    count_missing_values,
    fill_missing_with_mean,
    remove_duplicates,
    group_and_calculate_mean,
    merge_dataframes,
    concatenate_dataframes,
    apply_function_to_column,
    create_age_group,
    filter_and_sort,
    pivot_table_summary
)


class TestStep4:
    """Step 4 테스트 클래스"""

    def test_count_missing_values(self):
        """count_missing_values 함수 테스트"""
        df = pd.DataFrame({
            'A': [1, 2, np.nan, 4],
            'B': [5, np.nan, np.nan, 8],
            'C': [9, 10, 11, 12]
        })
        result = count_missing_values(df)
        expected = pd.Series({'A': 1, 'B': 2, 'C': 0})

        pd.testing.assert_series_equal(result, expected)

    def test_fill_missing_with_mean(self):
        """fill_missing_with_mean 함수 테스트"""
        df = pd.DataFrame({
            'A': [1, 2, np.nan, 4],
            'B': [5, 6, 7, 8]
        })
        result = fill_missing_with_mean(df, 'A')

        # 평균은 (1+2+4)/3 = 2.333...
        assert pd.isna(result['A']).sum() == 0
        assert abs(result['A'].iloc[2] - 2.333333) < 0.001

        # 원본이 변경되지 않았는지 확인
        assert pd.isna(df['A'].iloc[2])

    def test_remove_duplicates(self):
        """remove_duplicates 함수 테스트"""
        df = pd.DataFrame({
            'A': [1, 2, 1, 3],
            'B': [4, 5, 4, 6]
        })
        result = remove_duplicates(df)

        assert len(result) == 3
        assert result.duplicated().sum() == 0

    def test_group_and_calculate_mean(self):
        """group_and_calculate_mean 함수 테스트"""
        df = pd.DataFrame({
            'team': ['A', 'A', 'B', 'B'],
            'score': [80, 90, 85, 95]
        })
        result = group_and_calculate_mean(df, 'team', 'score')

        assert result['A'] == 85.0
        assert result['B'] == 90.0

    def test_merge_dataframes(self):
        """merge_dataframes 함수 테스트"""
        df1 = pd.DataFrame({
            'key': ['A', 'B', 'C'],
            'value1': [1, 2, 3]
        })
        df2 = pd.DataFrame({
            'key': ['A', 'B', 'D'],
            'value2': [10, 20, 30]
        })
        result = merge_dataframes(df1, df2, 'key')

        # Inner join이므로 A와 B만 남음
        assert len(result) == 2
        assert 'value1' in result.columns
        assert 'value2' in result.columns

    def test_concatenate_dataframes(self):
        """concatenate_dataframes 함수 테스트"""
        df1 = pd.DataFrame({'A': [1, 2]})
        df2 = pd.DataFrame({'A': [3, 4]})
        result = concatenate_dataframes(df1, df2)

        assert len(result) == 4
        assert list(result['A']) == [1, 2, 3, 4]
        # 인덱스가 리셋되었는지 확인
        assert list(result.index) == [0, 1, 2, 3]

    def test_apply_function_to_column(self):
        """apply_function_to_column 함수 테스트"""
        df = pd.DataFrame({'A': [1, 2, 3]})
        result = apply_function_to_column(df, 'A', lambda x: x * 2)

        expected = pd.Series([2, 4, 6], name='A')
        pd.testing.assert_series_equal(result, expected)

    def test_create_age_group(self):
        """create_age_group 함수 테스트"""
        df = pd.DataFrame({'age': [25, 32, 48, 19, 55]})
        result = create_age_group(df, 'age')

        assert result.iloc[0] == '20대'
        assert result.iloc[1] == '30대'
        assert result.iloc[2] == '40대'
        assert result.iloc[3] == '10대'
        assert result.iloc[4] == '50대'

    def test_filter_and_sort(self):
        """filter_and_sort 함수 테스트"""
        df = pd.DataFrame({
            'score': [80, 90, 70, 95],
            'age': [25, 30, 28, 22]
        })
        result = filter_and_sort(df, 'score', 75, 'age')

        # score > 75인 행들만 있어야 함
        assert len(result) == 3
        assert all(result['score'] > 75)

        # age로 정렬되어 있어야 함
        assert list(result['age']) == [22, 25, 30]

    def test_pivot_table_summary(self):
        """pivot_table_summary 함수 테스트"""
        df = pd.DataFrame({
            'date': ['2024-01', '2024-01', '2024-02', '2024-02'],
            'team': ['A', 'B', 'A', 'B'],
            'score': [80, 90, 85, 95]
        })
        result = pivot_table_summary(df, 'date', 'team', 'score')

        # 결과가 DataFrame인지 확인
        assert isinstance(result, pd.DataFrame)

        # 피벗 테이블의 값 확인
        assert result.loc['2024-01', 'A'] == 80
        assert result.loc['2024-01', 'B'] == 90
        assert result.loc['2024-02', 'A'] == 85
        assert result.loc['2024-02', 'B'] == 95


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
