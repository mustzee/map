"""
Step 2: NumPy 배열 자동 채점 테스트
"""
import pytest
import numpy as np
import sys
sys.path.insert(0, '/home/user/map')

from exercises.step2_exercises import (
    create_array_from_range,
    create_zero_matrix,
    get_array_stats,
    filter_greater_than,
    normalize_array,
    multiply_matrices,
    sum_rows,
    sum_columns,
    replace_negatives_with_zero,
    reshape_to_matrix
)


class TestStep2:
    """Step 2 테스트 클래스"""

    def test_create_array_from_range(self):
        """create_array_from_range 함수 테스트"""
        result = create_array_from_range(0, 10, 2)
        expected = np.array([0, 2, 4, 6, 8])
        np.testing.assert_array_equal(result, expected)

        result = create_array_from_range(5, 15, 3)
        expected = np.array([5, 8, 11, 14])
        np.testing.assert_array_equal(result, expected)

    def test_create_zero_matrix(self):
        """create_zero_matrix 함수 테스트"""
        result = create_zero_matrix(2, 3)
        expected = np.zeros((2, 3))
        np.testing.assert_array_equal(result, expected)
        assert result.shape == (2, 3)

        result = create_zero_matrix(3, 4)
        assert result.shape == (3, 4)
        assert np.all(result == 0)

    def test_get_array_stats(self):
        """get_array_stats 함수 테스트"""
        arr = np.array([1, 2, 3, 4, 5])
        result = get_array_stats(arr)

        assert 'mean' in result
        assert 'min' in result
        assert 'max' in result
        assert 'std' in result

        assert result['mean'] == 3.0
        assert result['min'] == 1
        assert result['max'] == 5
        np.testing.assert_almost_equal(result['std'], 1.4142, decimal=4)

    def test_filter_greater_than(self):
        """filter_greater_than 함수 테스트"""
        arr = np.array([1, 5, 3, 8, 2])
        result = filter_greater_than(arr, 3)
        expected = np.array([5, 8])
        np.testing.assert_array_equal(result, expected)

        arr = np.array([10, 15, 20, 25])
        result = filter_greater_than(arr, 15)
        expected = np.array([20, 25])
        np.testing.assert_array_equal(result, expected)

    def test_normalize_array(self):
        """normalize_array 함수 테스트"""
        arr = np.array([10, 20, 30, 40, 50])
        result = normalize_array(arr)
        expected = np.array([0., 0.25, 0.5, 0.75, 1.])
        np.testing.assert_array_almost_equal(result, expected)

        # 결과가 0-1 범위인지 확인
        assert result.min() == 0.0
        assert result.max() == 1.0

    def test_multiply_matrices(self):
        """multiply_matrices 함수 테스트"""
        matrix1 = np.array([[1, 2], [3, 4]])
        matrix2 = np.array([[5, 6], [7, 8]])
        result = multiply_matrices(matrix1, matrix2)
        expected = np.array([[5, 12], [21, 32]])
        np.testing.assert_array_equal(result, expected)

    def test_sum_rows(self):
        """sum_rows 함수 테스트"""
        matrix = np.array([[1, 2, 3], [4, 5, 6]])
        result = sum_rows(matrix)
        expected = np.array([6, 15])
        np.testing.assert_array_equal(result, expected)

        matrix = np.array([[10, 20], [30, 40], [50, 60]])
        result = sum_rows(matrix)
        expected = np.array([30, 70, 110])
        np.testing.assert_array_equal(result, expected)

    def test_sum_columns(self):
        """sum_columns 함수 테스트"""
        matrix = np.array([[1, 2, 3], [4, 5, 6]])
        result = sum_columns(matrix)
        expected = np.array([5, 7, 9])
        np.testing.assert_array_equal(result, expected)

        matrix = np.array([[10, 20], [30, 40], [50, 60]])
        result = sum_columns(matrix)
        expected = np.array([90, 120])
        np.testing.assert_array_equal(result, expected)

    def test_replace_negatives_with_zero(self):
        """replace_negatives_with_zero 함수 테스트"""
        arr = np.array([1, -2, 3, -4, 5])
        result = replace_negatives_with_zero(arr)
        expected = np.array([1, 0, 3, 0, 5])
        np.testing.assert_array_equal(result, expected)

        arr = np.array([-1, -2, -3])
        result = replace_negatives_with_zero(arr)
        expected = np.array([0, 0, 0])
        np.testing.assert_array_equal(result, expected)

    def test_reshape_to_matrix(self):
        """reshape_to_matrix 함수 테스트"""
        arr = np.array([1, 2, 3, 4, 5, 6])
        result = reshape_to_matrix(arr, 2, 3)
        expected = np.array([[1, 2, 3], [4, 5, 6]])
        np.testing.assert_array_equal(result, expected)
        assert result.shape == (2, 3)

        arr = np.array([1, 2, 3, 4])
        result = reshape_to_matrix(arr, 4, 1)
        assert result.shape == (4, 1)


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
