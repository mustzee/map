"""
Step 4: Pandas 데이터 처리 연습문제

각 함수를 완성하세요. Pandas의 고급 기능을 활용하세요.
"""
import pandas as pd
import numpy as np


def count_missing_values(df):
    """
    DataFrame의 각 열별 결측치 개수를 Series로 반환하세요.

    Args:
        df (pd.DataFrame): 입력 DataFrame

    Returns:
        pd.Series: 각 열의 결측치 개수
    """
    pass


def fill_missing_with_mean(df, column_name):
    """
    특정 열의 결측치를 해당 열의 평균값으로 채우세요.
    원본은 수정하지 않고 복사본을 반환하세요.

    Args:
        df (pd.DataFrame): 입력 DataFrame
        column_name (str): 결측치를 채울 열 이름

    Returns:
        pd.DataFrame: 결측치가 채워진 DataFrame
    """
    pass


def remove_duplicates(df):
    """
    DataFrame에서 중복된 행을 제거하세요.

    Args:
        df (pd.DataFrame): 입력 DataFrame

    Returns:
        pd.DataFrame: 중복이 제거된 DataFrame
    """
    pass


def group_and_calculate_mean(df, group_column, value_column):
    """
    특정 열로 그룹화하고 다른 열의 평균을 계산하세요.

    예시:
        df = pd.DataFrame({
            'team': ['A', 'A', 'B', 'B'],
            'score': [80, 90, 85, 95]
        })
        group_and_calculate_mean(df, 'team', 'score')
        -> Series: A: 85.0, B: 90.0

    Args:
        df (pd.DataFrame): 입력 DataFrame
        group_column (str): 그룹화할 열
        value_column (str): 평균을 계산할 열

    Returns:
        pd.Series: 그룹별 평균
    """
    pass


def merge_dataframes(df1, df2, key_column):
    """
    두 DataFrame을 특정 열을 기준으로 inner join하세요.

    Args:
        df1 (pd.DataFrame): 첫 번째 DataFrame
        df2 (pd.DataFrame): 두 번째 DataFrame
        key_column (str): 조인 키 열

    Returns:
        pd.DataFrame: 병합된 DataFrame
    """
    pass


def concatenate_dataframes(df1, df2):
    """
    두 DataFrame을 수직으로 연결하세요 (행 추가).
    인덱스는 리셋하세요.

    Args:
        df1 (pd.DataFrame): 첫 번째 DataFrame
        df2 (pd.DataFrame): 두 번째 DataFrame

    Returns:
        pd.DataFrame: 연결된 DataFrame
    """
    pass


def apply_function_to_column(df, column_name, func):
    """
    특정 열에 함수를 적용하여 새로운 Series를 반환하세요.

    예시:
        df = pd.DataFrame({'A': [1, 2, 3]})
        apply_function_to_column(df, 'A', lambda x: x * 2)
        -> Series([2, 4, 6])

    Args:
        df (pd.DataFrame): 입력 DataFrame
        column_name (str): 함수를 적용할 열
        func: 적용할 함수

    Returns:
        pd.Series: 함수가 적용된 Series
    """
    pass


def create_age_group(df, age_column):
    """
    나이 열을 기반으로 연령대 그룹을 생성하세요.
    - 20대: 20-29
    - 30대: 30-39
    - 40대: 40-49
    등등...

    예시:
        df = pd.DataFrame({'age': [25, 32, 48]})
        create_age_group(df, 'age')
        -> Series(['20대', '30대', '40대'])

    Args:
        df (pd.DataFrame): 입력 DataFrame
        age_column (str): 나이 열 이름

    Returns:
        pd.Series: 연령대 그룹
    """
    pass


def filter_and_sort(df, filter_column, threshold, sort_column):
    """
    특정 열의 값이 threshold보다 큰 행만 필터링하고,
    다른 열을 기준으로 오름차순 정렬하세요.

    Args:
        df (pd.DataFrame): 입력 DataFrame
        filter_column (str): 필터링할 열
        threshold: 임계값
        sort_column (str): 정렬 기준 열

    Returns:
        pd.DataFrame: 필터링 및 정렬된 DataFrame
    """
    pass


def pivot_table_summary(df, index_col, columns_col, values_col):
    """
    피벗 테이블을 생성하여 데이터를 요약하세요.
    집계 함수는 평균(mean)을 사용하세요.

    Args:
        df (pd.DataFrame): 입력 DataFrame
        index_col (str): 행 인덱스로 사용할 열
        columns_col (str): 열로 사용할 열
        values_col (str): 값으로 사용할 열

    Returns:
        pd.DataFrame: 피벗 테이블
    """
    pass
