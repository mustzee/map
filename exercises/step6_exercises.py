"""
Step 6: Pandas와 데이터베이스 연동 연습문제

각 함수를 완성하세요. Pandas와 SQLite를 함께 활용하세요.
"""
import pandas as pd
import sqlite3


def save_dataframe_to_db(df, db_path, table_name):
    """
    DataFrame을 SQLite 데이터베이스의 테이블로 저장하세요.
    기존 테이블이 있으면 교체하고, 인덱스는 저장하지 마세요.

    Args:
        df (pd.DataFrame): 저장할 DataFrame
        db_path (str): 데이터베이스 파일 경로
        table_name (str): 테이블 이름
    """
    pass


def load_table_to_dataframe(db_path, table_name):
    """
    SQLite 데이터베이스의 테이블을 DataFrame으로 읽어오세요.

    Args:
        db_path (str): 데이터베이스 파일 경로
        table_name (str): 테이블 이름

    Returns:
        pd.DataFrame: 읽어온 DataFrame
    """
    pass


def query_to_dataframe(db_path, sql_query):
    """
    SQL 쿼리를 실행하고 결과를 DataFrame으로 반환하세요.

    Args:
        db_path (str): 데이터베이스 파일 경로
        sql_query (str): 실행할 SQL 쿼리

    Returns:
        pd.DataFrame: 쿼리 결과 DataFrame
    """
    pass


def filter_and_save(db_path, source_table, dest_table, column, threshold):
    """
    source_table에서 특정 열의 값이 threshold보다 큰 행들만 필터링하여
    dest_table로 저장하세요.

    Args:
        db_path (str): 데이터베이스 파일 경로
        source_table (str): 원본 테이블 이름
        dest_table (str): 대상 테이블 이름
        column (str): 필터링할 열 이름
        threshold: 임계값
    """
    pass


def aggregate_and_save(db_path, source_table, dest_table, group_column, agg_column):
    """
    source_table의 데이터를 group_column으로 그룹화하고
    agg_column의 평균과 합계를 계산하여 dest_table로 저장하세요.

    결과 DataFrame의 열 이름:
    - group_column: 그룹 열
    - 'mean': 평균
    - 'sum': 합계

    Args:
        db_path (str): 데이터베이스 파일 경로
        source_table (str): 원본 테이블 이름
        dest_table (str): 대상 테이블 이름
        group_column (str): 그룹화할 열
        agg_column (str): 집계할 열
    """
    pass


def merge_tables(db_path, table1, table2, key_column, output_table):
    """
    두 테이블을 key_column 기준으로 inner join하여 output_table로 저장하세요.

    Args:
        db_path (str): 데이터베이스 파일 경로
        table1 (str): 첫 번째 테이블 이름
        table2 (str): 두 번째 테이블 이름
        key_column (str): 조인 키 열
        output_table (str): 출력 테이블 이름
    """
    pass


def add_calculated_column(db_path, table_name, col1, col2, new_col_name):
    """
    테이블을 읽어서 col1과 col2의 합을 new_col_name이라는 새 열로 추가하고
    같은 테이블로 다시 저장하세요 (기존 테이블 교체).

    Args:
        db_path (str): 데이터베이스 파일 경로
        table_name (str): 테이블 이름
        col1 (str): 첫 번째 열 이름
        col2 (str): 두 번째 열 이름
        new_col_name (str): 새로운 열 이름
    """
    pass


def get_top_n_records(db_path, table_name, sort_column, n):
    """
    테이블에서 sort_column 기준으로 내림차순 정렬한 후
    상위 n개 레코드를 DataFrame으로 반환하세요.

    Args:
        db_path (str): 데이터베이스 파일 경로
        table_name (str): 테이블 이름
        sort_column (str): 정렬 기준 열
        n (int): 가져올 레코드 수

    Returns:
        pd.DataFrame: 상위 n개 레코드
    """
    pass


def calculate_statistics(db_path, table_name, column):
    """
    테이블의 특정 열에 대한 통계를 계산하여 딕셔너리로 반환하세요.
    통계: mean, median, std, min, max

    Args:
        db_path (str): 데이터베이스 파일 경로
        table_name (str): 테이블 이름
        column (str): 통계를 계산할 열

    Returns:
        dict: {'mean': ..., 'median': ..., 'std': ..., 'min': ..., 'max': ...}
    """
    pass


def pivot_and_save(db_path, source_table, dest_table, index_col, columns_col, values_col):
    """
    source_table의 데이터를 피벗하여 dest_table로 저장하세요.

    Args:
        db_path (str): 데이터베이스 파일 경로
        source_table (str): 원본 테이블 이름
        dest_table (str): 대상 테이블 이름
        index_col (str): 피벗 인덱스로 사용할 열
        columns_col (str): 피벗 컬럼으로 사용할 열
        values_col (str): 피벗 값으로 사용할 열
    """
    pass
