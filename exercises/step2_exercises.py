"""
Step 2: NumPy 배열 연습문제

각 함수를 완성하세요. NumPy 배열 연산을 활용하세요.
"""
import numpy as np


def create_array_from_range(start, end, step):
    """
    start부터 end까지 step 간격의 NumPy 배열을 생성하세요.

    예시:
        create_array_from_range(0, 10, 2) -> array([0, 2, 4, 6, 8])
        create_array_from_range(5, 15, 3) -> array([5, 8, 11, 14])

    Args:
        start (int): 시작 값
        end (int): 끝 값 (포함 안 됨)
        step (int): 간격

    Returns:
        numpy.ndarray: 생성된 배열
    """
    pass


def create_zero_matrix(rows, cols):
    """
    rows x cols 크기의 0으로 채워진 2차원 배열을 생성하세요.

    예시:
        create_zero_matrix(2, 3) -> array([[0., 0., 0.], [0., 0., 0.]])

    Args:
        rows (int): 행 수
        cols (int): 열 수

    Returns:
        numpy.ndarray: 0으로 채워진 배열
    """
    pass


def get_array_stats(arr):
    """
    배열의 통계값(평균, 최솟값, 최댓값, 표준편차)을 딕셔너리로 반환하세요.

    예시:
        get_array_stats(np.array([1, 2, 3, 4, 5]))
        -> {'mean': 3.0, 'min': 1, 'max': 5, 'std': 1.414...}

    Args:
        arr (numpy.ndarray): 입력 배열

    Returns:
        dict: {'mean': 평균, 'min': 최솟값, 'max': 최댓값, 'std': 표준편차}
    """
    pass


def filter_greater_than(arr, threshold):
    """
    배열에서 threshold보다 큰 값들만 반환하세요.

    예시:
        filter_greater_than(np.array([1, 5, 3, 8, 2]), 3) -> array([5, 8])

    Args:
        arr (numpy.ndarray): 입력 배열
        threshold: 임계값

    Returns:
        numpy.ndarray: threshold보다 큰 값들
    """
    pass


def normalize_array(arr):
    """
    배열을 0-1 범위로 정규화하세요.
    공식: (x - min) / (max - min)

    예시:
        normalize_array(np.array([10, 20, 30, 40, 50]))
        -> array([0., 0.25, 0.5, 0.75, 1.])

    Args:
        arr (numpy.ndarray): 입력 배열

    Returns:
        numpy.ndarray: 정규화된 배열
    """
    pass


def multiply_matrices(matrix1, matrix2):
    """
    두 행렬을 요소별로 곱하세요. (행렬 곱셈이 아님)

    예시:
        multiply_matrices(
            np.array([[1, 2], [3, 4]]),
            np.array([[5, 6], [7, 8]])
        ) -> array([[5, 12], [21, 32]])

    Args:
        matrix1 (numpy.ndarray): 첫 번째 행렬
        matrix2 (numpy.ndarray): 두 번째 행렬

    Returns:
        numpy.ndarray: 요소별 곱셈 결과
    """
    pass


def sum_rows(matrix):
    """
    2차원 배열의 각 행의 합을 계산하여 1차원 배열로 반환하세요.

    예시:
        sum_rows(np.array([[1, 2, 3], [4, 5, 6]]))
        -> array([6, 15])

    Args:
        matrix (numpy.ndarray): 2차원 배열

    Returns:
        numpy.ndarray: 각 행의 합
    """
    pass


def sum_columns(matrix):
    """
    2차원 배열의 각 열의 합을 계산하여 1차원 배열로 반환하세요.

    예시:
        sum_columns(np.array([[1, 2, 3], [4, 5, 6]]))
        -> array([5, 7, 9])

    Args:
        matrix (numpy.ndarray): 2차원 배열

    Returns:
        numpy.ndarray: 각 열의 합
    """
    pass


def replace_negatives_with_zero(arr):
    """
    배열의 음수를 모두 0으로 바꾸세요.

    예시:
        replace_negatives_with_zero(np.array([1, -2, 3, -4, 5]))
        -> array([1, 0, 3, 0, 5])

    Args:
        arr (numpy.ndarray): 입력 배열

    Returns:
        numpy.ndarray: 음수가 0으로 바뀐 배열
    """
    pass


def reshape_to_matrix(arr, rows, cols):
    """
    1차원 배열을 rows x cols 크기의 2차원 배열로 변환하세요.

    예시:
        reshape_to_matrix(np.array([1, 2, 3, 4, 5, 6]), 2, 3)
        -> array([[1, 2, 3], [4, 5, 6]])

    Args:
        arr (numpy.ndarray): 1차원 배열
        rows (int): 행 수
        cols (int): 열 수

    Returns:
        numpy.ndarray: 2차원 배열
    """
    pass
