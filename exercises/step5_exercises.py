"""
Step 5: SQLite 데이터베이스 기초 연습문제

각 함수를 완성하세요. SQLite를 활용하세요.
"""
import sqlite3


def create_database(db_path):
    """
    데이터베이스 파일을 생성하고 연결을 반환하세요.

    Args:
        db_path (str): 데이터베이스 파일 경로

    Returns:
        sqlite3.Connection: 데이터베이스 연결 객체
    """
    pass


def create_table(conn):
    """
    'students' 테이블을 생성하세요.
    컬럼: id (INTEGER PRIMARY KEY), name (TEXT), age (INTEGER), grade (REAL)

    Args:
        conn (sqlite3.Connection): 데이터베이스 연결
    """
    pass


def insert_student(conn, name, age, grade):
    """
    students 테이블에 학생 데이터를 삽입하세요.

    Args:
        conn (sqlite3.Connection): 데이터베이스 연결
        name (str): 학생 이름
        age (int): 학생 나이
        grade (float): 학생 성적
    """
    pass


def insert_multiple_students(conn, students_list):
    """
    여러 학생 데이터를 한 번에 삽입하세요.

    Args:
        conn (sqlite3.Connection): 데이터베이스 연결
        students_list (list): [(name, age, grade), ...] 형태의 리스트
    """
    pass


def get_all_students(conn):
    """
    students 테이블의 모든 데이터를 조회하세요.

    Args:
        conn (sqlite3.Connection): 데이터베이스 연결

    Returns:
        list: 모든 학생 데이터 (튜플의 리스트)
    """
    pass


def get_students_by_age(conn, min_age):
    """
    나이가 min_age 이상인 학생들을 조회하세요.

    Args:
        conn (sqlite3.Connection): 데이터베이스 연결
        min_age (int): 최소 나이

    Returns:
        list: 조건에 맞는 학생 데이터
    """
    pass


def get_student_count(conn):
    """
    students 테이블의 전체 학생 수를 반환하세요.

    Args:
        conn (sqlite3.Connection): 데이터베이스 연결

    Returns:
        int: 학생 수
    """
    pass


def update_student_grade(conn, student_id, new_grade):
    """
    특정 학생의 성적을 업데이트하세요.

    Args:
        conn (sqlite3.Connection): 데이터베이스 연결
        student_id (int): 학생 ID
        new_grade (float): 새로운 성적
    """
    pass


def delete_student(conn, student_id):
    """
    특정 ID의 학생을 삭제하세요.

    Args:
        conn (sqlite3.Connection): 데이터베이스 연결
        student_id (int): 삭제할 학생 ID
    """
    pass


def get_average_grade(conn):
    """
    students 테이블의 평균 성적을 계산하세요.

    Args:
        conn (sqlite3.Connection): 데이터베이스 연결

    Returns:
        float: 평균 성적 (학생이 없으면 0.0)
    """
    pass
