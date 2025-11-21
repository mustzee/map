"""
Step 1: Python 리스트와 배열 기초 연습문제

각 함수를 완성하세요. 함수 내부의 pass를 지우고 코드를 작성하면 됩니다.
"""


def create_number_list(n):
    """
    1부터 n까지의 숫자를 포함하는 리스트를 반환하세요.

    예시:
        create_number_list(5) -> [1, 2, 3, 4, 5]
        create_number_list(3) -> [1, 2, 3]

    Args:
        n (int): 마지막 숫자

    Returns:
        list: 1부터 n까지의 숫자 리스트
    """
    pass


def get_first_and_last(lst):
    """
    리스트의 첫 번째와 마지막 요소를 튜플로 반환하세요.

    예시:
        get_first_and_last([1, 2, 3, 4, 5]) -> (1, 5)
        get_first_and_last(['a', 'b', 'c']) -> ('a', 'c')

    Args:
        lst (list): 입력 리스트

    Returns:
        tuple: (첫 번째 요소, 마지막 요소)
    """
    pass


def get_middle_elements(lst):
    """
    리스트의 첫 번째와 마지막 요소를 제외한 중간 요소들을 반환하세요.

    예시:
        get_middle_elements([1, 2, 3, 4, 5]) -> [2, 3, 4]
        get_middle_elements([10, 20, 30]) -> [20]

    Args:
        lst (list): 입력 리스트

    Returns:
        list: 중간 요소들의 리스트
    """
    pass


def reverse_list(lst):
    """
    리스트를 역순으로 반환하세요. (원본 리스트는 변경하지 않음)

    예시:
        reverse_list([1, 2, 3, 4, 5]) -> [5, 4, 3, 2, 1]
        reverse_list(['a', 'b', 'c']) -> ['c', 'b', 'a']

    Args:
        lst (list): 입력 리스트

    Returns:
        list: 역순 리스트
    """
    pass


def get_even_numbers(lst):
    """
    리스트에서 짝수만 추출하여 반환하세요.

    예시:
        get_even_numbers([1, 2, 3, 4, 5, 6]) -> [2, 4, 6]
        get_even_numbers([10, 15, 20, 25]) -> [10, 20]

    Args:
        lst (list): 숫자 리스트

    Returns:
        list: 짝수만 포함된 리스트
    """
    pass


def square_numbers(lst):
    """
    리스트의 모든 숫자를 제곱한 리스트를 반환하세요.

    예시:
        square_numbers([1, 2, 3, 4]) -> [1, 4, 9, 16]
        square_numbers([5, 10]) -> [25, 100]

    Args:
        lst (list): 숫자 리스트

    Returns:
        list: 제곱된 숫자 리스트
    """
    pass


def count_occurrence(lst, value):
    """
    리스트에서 특정 값이 몇 번 나타나는지 세어 반환하세요.

    예시:
        count_occurrence([1, 2, 3, 2, 2, 4], 2) -> 3
        count_occurrence(['a', 'b', 'a', 'c'], 'a') -> 2

    Args:
        lst (list): 입력 리스트
        value: 찾을 값

    Returns:
        int: 값의 출현 횟수
    """
    pass


def merge_and_sort(list1, list2):
    """
    두 리스트를 합치고 오름차순으로 정렬하여 반환하세요.

    예시:
        merge_and_sort([3, 1, 4], [2, 5]) -> [1, 2, 3, 4, 5]
        merge_and_sort([10, 30], [20, 40]) -> [10, 20, 30, 40]

    Args:
        list1 (list): 첫 번째 리스트
        list2 (list): 두 번째 리스트

    Returns:
        list: 합쳐서 정렬된 리스트
    """
    pass


def remove_duplicates(lst):
    """
    리스트에서 중복을 제거하고 원래 순서를 유지한 리스트를 반환하세요.

    예시:
        remove_duplicates([1, 2, 2, 3, 4, 3, 5]) -> [1, 2, 3, 4, 5]
        remove_duplicates(['a', 'b', 'a', 'c']) -> ['a', 'b', 'c']

    Args:
        lst (list): 입력 리스트

    Returns:
        list: 중복이 제거된 리스트
    """
    pass


def flatten_matrix(matrix):
    """
    2차원 리스트(행렬)를 1차원 리스트로 평탄화하세요.

    예시:
        flatten_matrix([[1, 2], [3, 4], [5, 6]]) -> [1, 2, 3, 4, 5, 6]
        flatten_matrix([[10, 20, 30], [40, 50, 60]]) -> [10, 20, 30, 40, 50, 60]

    Args:
        matrix (list): 2차원 리스트

    Returns:
        list: 1차원 리스트
    """
    pass
