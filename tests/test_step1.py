"""
Step 1: Python 리스트와 배열 기초 자동 채점 테스트
"""
import pytest
import sys
sys.path.insert(0, '/home/user/map')

from exercises.step1_exercises import (
    create_number_list,
    get_first_and_last,
    get_middle_elements,
    reverse_list,
    get_even_numbers,
    square_numbers,
    count_occurrence,
    merge_and_sort,
    remove_duplicates,
    flatten_matrix
)


class TestStep1:
    """Step 1 테스트 클래스"""

    def test_create_number_list(self):
        """create_number_list 함수 테스트"""
        assert create_number_list(5) == [1, 2, 3, 4, 5]
        assert create_number_list(3) == [1, 2, 3]
        assert create_number_list(10) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        assert create_number_list(1) == [1]

    def test_get_first_and_last(self):
        """get_first_and_last 함수 테스트"""
        assert get_first_and_last([1, 2, 3, 4, 5]) == (1, 5)
        assert get_first_and_last(['a', 'b', 'c']) == ('a', 'c')
        assert get_first_and_last([10, 20]) == (10, 20)
        assert get_first_and_last([100]) == (100, 100)

    def test_get_middle_elements(self):
        """get_middle_elements 함수 테스트"""
        assert get_middle_elements([1, 2, 3, 4, 5]) == [2, 3, 4]
        assert get_middle_elements([10, 20, 30]) == [20]
        assert get_middle_elements([1, 2, 3, 4]) == [2, 3]
        assert get_middle_elements(['a', 'b', 'c', 'd', 'e']) == ['b', 'c', 'd']

    def test_reverse_list(self):
        """reverse_list 함수 테스트"""
        assert reverse_list([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]
        assert reverse_list(['a', 'b', 'c']) == ['c', 'b', 'a']
        assert reverse_list([10]) == [10]
        assert reverse_list([1, 2]) == [2, 1]

        # 원본 리스트가 변경되지 않았는지 확인
        original = [1, 2, 3]
        reversed_list = reverse_list(original)
        assert original == [1, 2, 3]

    def test_get_even_numbers(self):
        """get_even_numbers 함수 테스트"""
        assert get_even_numbers([1, 2, 3, 4, 5, 6]) == [2, 4, 6]
        assert get_even_numbers([10, 15, 20, 25]) == [10, 20]
        assert get_even_numbers([1, 3, 5, 7]) == []
        assert get_even_numbers([2, 4, 6, 8]) == [2, 4, 6, 8]

    def test_square_numbers(self):
        """square_numbers 함수 테스트"""
        assert square_numbers([1, 2, 3, 4]) == [1, 4, 9, 16]
        assert square_numbers([5, 10]) == [25, 100]
        assert square_numbers([0, 1]) == [0, 1]
        assert square_numbers([10, 20, 30]) == [100, 400, 900]

    def test_count_occurrence(self):
        """count_occurrence 함수 테스트"""
        assert count_occurrence([1, 2, 3, 2, 2, 4], 2) == 3
        assert count_occurrence(['a', 'b', 'a', 'c'], 'a') == 2
        assert count_occurrence([1, 2, 3], 5) == 0
        assert count_occurrence([7, 7, 7, 7], 7) == 4

    def test_merge_and_sort(self):
        """merge_and_sort 함수 테스트"""
        assert merge_and_sort([3, 1, 4], [2, 5]) == [1, 2, 3, 4, 5]
        assert merge_and_sort([10, 30], [20, 40]) == [10, 20, 30, 40]
        assert merge_and_sort([5, 1], [3, 2, 4]) == [1, 2, 3, 4, 5]
        assert merge_and_sort([], [1, 2, 3]) == [1, 2, 3]

    def test_remove_duplicates(self):
        """remove_duplicates 함수 테스트"""
        assert remove_duplicates([1, 2, 2, 3, 4, 3, 5]) == [1, 2, 3, 4, 5]
        assert remove_duplicates(['a', 'b', 'a', 'c']) == ['a', 'b', 'c']
        assert remove_duplicates([1, 1, 1]) == [1]
        assert remove_duplicates([1, 2, 3]) == [1, 2, 3]

    def test_flatten_matrix(self):
        """flatten_matrix 함수 테스트"""
        assert flatten_matrix([[1, 2], [3, 4], [5, 6]]) == [1, 2, 3, 4, 5, 6]
        assert flatten_matrix([[10, 20, 30], [40, 50, 60]]) == [10, 20, 30, 40, 50, 60]
        assert flatten_matrix([[1], [2], [3]]) == [1, 2, 3]
        assert flatten_matrix([[1, 2, 3]]) == [1, 2, 3]


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
