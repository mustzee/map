"""
Step 3: Pandas 기초 자동 채점 테스트
"""
import pytest
import pandas as pd
import sys
sys.path.insert(0, '/home/user/map')

from exercises.step3_exercises import (
    create_series_from_dict,
    create_dataframe_from_dict,
    get_column,
    get_first_n_rows,
    filter_by_condition,
    add_new_column,
    calculate_column_mean,
    sort_by_column,
    get_dataframe_shape,
    select_multiple_columns
)


class TestStep3:
    """Step 3 테스트 클래스"""

    def test_create_series_from_dict(self):
        """create_series_from_dict 함수 테스트"""
        data = {'a': 10, 'b': 20, 'c': 30}
        result = create_series_from_dict(data)
        expected = pd.Series(data)

        assert isinstance(result, pd.Series)
        pd.testing.assert_series_equal(result, expected)

    def test_create_dataframe_from_dict(self):
        """create_dataframe_from_dict 함수 테스트"""
        data = {
            'name': ['Alice', 'Bob'],
            'age': [25, 30]
        }
        result = create_dataframe_from_dict(data)
        expected = pd.DataFrame(data)

        assert isinstance(result, pd.DataFrame)
        pd.testing.assert_frame_equal(result, expected)

    def test_get_column(self):
        """get_column 함수 테스트"""
        df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        result = get_column(df, 'A')
        expected = pd.Series([1, 2, 3], name='A')

        assert isinstance(result, pd.Series)
        pd.testing.assert_series_equal(result, expected)

    def test_get_first_n_rows(self):
        """get_first_n_rows 함수 테스트"""
        df = pd.DataFrame({'A': [1, 2, 3, 4, 5]})
        result = get_first_n_rows(df, 3)
        expected = pd.DataFrame({'A': [1, 2, 3]})

        pd.testing.assert_frame_equal(result, expected)

    def test_filter_by_condition(self):
        """filter_by_condition 함수 테스트"""
        df = pd.DataFrame({'age': [25, 30, 35, 28]})
        result = filter_by_condition(df, 'age', 28)
        expected = pd.DataFrame({'age': [30, 35]}, index=[1, 2])

        pd.testing.assert_frame_equal(result, expected)

    def test_add_new_column(self):
        """add_new_column 함수 테스트"""
        df = pd.DataFrame({'A': [1, 2]})
        result = add_new_column(df, 'B', [3, 4])
        expected = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})

        pd.testing.assert_frame_equal(result, expected)
        # 원본이 변경되지 않았는지 확인
        assert 'B' not in df.columns

    def test_calculate_column_mean(self):
        """calculate_column_mean 함수 테스트"""
        df = pd.DataFrame({'score': [80, 90, 100]})
        result = calculate_column_mean(df, 'score')

        assert result == 90.0

    def test_sort_by_column(self):
        """sort_by_column 함수 테스트"""
        df = pd.DataFrame({'age': [30, 25, 35]})

        # 오름차순
        result = sort_by_column(df, 'age')
        expected = pd.DataFrame({'age': [25, 30, 35]}, index=[1, 0, 2])
        pd.testing.assert_frame_equal(result, expected)

        # 내림차순
        result = sort_by_column(df, 'age', ascending=False)
        expected = pd.DataFrame({'age': [35, 30, 25]}, index=[2, 0, 1])
        pd.testing.assert_frame_equal(result, expected)

    def test_get_dataframe_shape(self):
        """get_dataframe_shape 함수 테스트"""
        df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        result = get_dataframe_shape(df)

        assert result == (3, 2)

        df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [1, 2, 3, 4, 5], 'C': [1, 2, 3, 4, 5]})
        result = get_dataframe_shape(df)
        assert result == (5, 3)

    def test_select_multiple_columns(self):
        """select_multiple_columns 함수 테스트"""
        df = pd.DataFrame({'A': [1, 2], 'B': [3, 4], 'C': [5, 6]})
        result = select_multiple_columns(df, ['A', 'C'])
        expected = pd.DataFrame({'A': [1, 2], 'C': [5, 6]})

        pd.testing.assert_frame_equal(result, expected)


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
