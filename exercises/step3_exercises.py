"""
Step 3: Pandas 기초 연습문제

각 함수를 완성하세요. Pandas의 Series와 DataFrame을 활용하세요.
"""
import pandas as pd


def create_series_from_dict(data_dict):
    """
    딕셔너리로부터 Pandas Series를 생성하세요.

    예시:
        create_series_from_dict({'a': 10, 'b': 20, 'c': 30})
        -> Series with index ['a', 'b', 'c'] and values [10, 20, 30]

    Args:
        data_dict (dict): 입력 딕셔너리

    Returns:
        pd.Series: 생성된 Series
    """
    pass


def create_dataframe_from_dict(data_dict):
    """
    딕셔너리로부터 Pandas DataFrame을 생성하세요.

    예시:
        create_dataframe_from_dict({
            'name': ['Alice', 'Bob'],
            'age': [25, 30]
        })

    Args:
        data_dict (dict): 입력 딕셔너리

    Returns:
        pd.DataFrame: 생성된 DataFrame
    """
    pass


def get_column(df, column_name):
    """
    DataFrame에서 특정 열을 Series로 반환하세요.

    예시:
        df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
        get_column(df, 'A') -> Series([1, 2])

    Args:
        df (pd.DataFrame): 입력 DataFrame
        column_name (str): 열 이름

    Returns:
        pd.Series: 선택된 열
    """
    pass


def get_first_n_rows(df, n):
    """
    DataFrame의 처음 n개 행을 반환하세요.

    예시:
        get_first_n_rows(df, 3) -> 처음 3개 행

    Args:
        df (pd.DataFrame): 입력 DataFrame
        n (int): 행 개수

    Returns:
        pd.DataFrame: 처음 n개 행
    """
    pass


def filter_by_condition(df, column_name, threshold):
    """
    특정 열의 값이 threshold보다 큰 행들만 반환하세요.

    예시:
        df = pd.DataFrame({'age': [25, 30, 35]})
        filter_by_condition(df, 'age', 28)
        -> DataFrame with rows where age > 28

    Args:
        df (pd.DataFrame): 입력 DataFrame
        column_name (str): 필터링할 열 이름
        threshold: 임계값

    Returns:
        pd.DataFrame: 필터링된 DataFrame
    """
    pass


def add_new_column(df, column_name, values):
    """
    DataFrame에 새로운 열을 추가하세요. (원본 수정하지 않고 복사본 반환)

    예시:
        df = pd.DataFrame({'A': [1, 2]})
        add_new_column(df, 'B', [3, 4])
        -> DataFrame with columns 'A' and 'B'

    Args:
        df (pd.DataFrame): 입력 DataFrame
        column_name (str): 새 열 이름
        values (list): 새 열의 값

    Returns:
        pd.DataFrame: 새 열이 추가된 DataFrame
    """
    pass


def calculate_column_mean(df, column_name):
    """
    특정 열의 평균을 계산하세요.

    예시:
        df = pd.DataFrame({'score': [80, 90, 100]})
        calculate_column_mean(df, 'score') -> 90.0

    Args:
        df (pd.DataFrame): 입력 DataFrame
        column_name (str): 열 이름

    Returns:
        float: 평균값
    """
    pass


def sort_by_column(df, column_name, ascending=True):
    """
    DataFrame을 특정 열 기준으로 정렬하세요.

    예시:
        df = pd.DataFrame({'age': [30, 25, 35]})
        sort_by_column(df, 'age') -> age가 오름차순으로 정렬됨

    Args:
        df (pd.DataFrame): 입력 DataFrame
        column_name (str): 정렬 기준 열
        ascending (bool): True면 오름차순, False면 내림차순

    Returns:
        pd.DataFrame: 정렬된 DataFrame
    """
    pass


def get_dataframe_shape(df):
    """
    DataFrame의 형태(행 수, 열 수)를 튜플로 반환하세요.

    예시:
        df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        get_dataframe_shape(df) -> (3, 2)

    Args:
        df (pd.DataFrame): 입력 DataFrame

    Returns:
        tuple: (행 수, 열 수)
    """
    pass


def select_multiple_columns(df, column_list):
    """
    DataFrame에서 여러 열을 선택하여 반환하세요.

    예시:
        df = pd.DataFrame({'A': [1, 2], 'B': [3, 4], 'C': [5, 6]})
        select_multiple_columns(df, ['A', 'C'])
        -> DataFrame with only columns 'A' and 'C'

    Args:
        df (pd.DataFrame): 입력 DataFrame
        column_list (list): 선택할 열 이름 리스트

    Returns:
        pd.DataFrame: 선택된 열들만 포함된 DataFrame
    """
    pass
