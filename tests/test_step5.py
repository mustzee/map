"""
Step 5: SQLite 데이터베이스 기초 자동 채점 테스트
"""
import pytest
import sqlite3
import os
import sys
sys.path.insert(0, '/home/user/map')

from exercises.step5_exercises import (
    create_database,
    create_table,
    insert_student,
    insert_multiple_students,
    get_all_students,
    get_students_by_age,
    get_student_count,
    update_student_grade,
    delete_student,
    get_average_grade
)


class TestStep5:
    """Step 5 테스트 클래스"""

    @pytest.fixture
    def test_db(self):
        """테스트용 데이터베이스 fixture"""
        db_path = ':memory:'
        conn = sqlite3.connect(db_path)
        yield conn
        conn.close()

    def test_create_database(self, tmp_path):
        """create_database 함수 테스트"""
        db_path = tmp_path / "test.db"
        conn = create_database(str(db_path))

        assert conn is not None
        assert isinstance(conn, sqlite3.Connection)
        assert os.path.exists(db_path)

        conn.close()

    def test_create_table(self, test_db):
        """create_table 함수 테스트"""
        create_table(test_db)

        # 테이블이 생성되었는지 확인
        cursor = test_db.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='students'")
        result = cursor.fetchone()

        assert result is not None
        assert result[0] == 'students'

        # 테이블 구조 확인
        cursor.execute("PRAGMA table_info(students)")
        columns = cursor.fetchall()
        column_names = [col[1] for col in columns]

        assert 'id' in column_names
        assert 'name' in column_names
        assert 'age' in column_names
        assert 'grade' in column_names

    def test_insert_student(self, test_db):
        """insert_student 함수 테스트"""
        create_table(test_db)
        insert_student(test_db, 'Alice', 20, 85.5)

        cursor = test_db.cursor()
        cursor.execute('SELECT * FROM students')
        result = cursor.fetchone()

        assert result is not None
        assert result[1] == 'Alice'
        assert result[2] == 20
        assert result[3] == 85.5

    def test_insert_multiple_students(self, test_db):
        """insert_multiple_students 함수 테스트"""
        create_table(test_db)
        students = [
            ('Alice', 20, 85.5),
            ('Bob', 22, 90.0),
            ('Charlie', 21, 88.5)
        ]
        insert_multiple_students(test_db, students)

        cursor = test_db.cursor()
        cursor.execute('SELECT COUNT(*) FROM students')
        count = cursor.fetchone()[0]

        assert count == 3

    def test_get_all_students(self, test_db):
        """get_all_students 함수 테스트"""
        create_table(test_db)
        insert_student(test_db, 'Alice', 20, 85.5)
        insert_student(test_db, 'Bob', 22, 90.0)

        result = get_all_students(test_db)

        assert len(result) == 2
        assert result[0][1] == 'Alice'
        assert result[1][1] == 'Bob'

    def test_get_students_by_age(self, test_db):
        """get_students_by_age 함수 테스트"""
        create_table(test_db)
        students = [
            ('Alice', 20, 85.5),
            ('Bob', 22, 90.0),
            ('Charlie', 25, 88.5)
        ]
        insert_multiple_students(test_db, students)

        result = get_students_by_age(test_db, 22)

        assert len(result) == 2
        assert all(student[2] >= 22 for student in result)

    def test_get_student_count(self, test_db):
        """get_student_count 함수 테스트"""
        create_table(test_db)

        assert get_student_count(test_db) == 0

        students = [
            ('Alice', 20, 85.5),
            ('Bob', 22, 90.0),
            ('Charlie', 21, 88.5)
        ]
        insert_multiple_students(test_db, students)

        assert get_student_count(test_db) == 3

    def test_update_student_grade(self, test_db):
        """update_student_grade 함수 테스트"""
        create_table(test_db)
        insert_student(test_db, 'Alice', 20, 85.5)

        # ID는 1부터 시작
        update_student_grade(test_db, 1, 95.0)

        cursor = test_db.cursor()
        cursor.execute('SELECT grade FROM students WHERE id = 1')
        grade = cursor.fetchone()[0]

        assert grade == 95.0

    def test_delete_student(self, test_db):
        """delete_student 함수 테스트"""
        create_table(test_db)
        students = [
            ('Alice', 20, 85.5),
            ('Bob', 22, 90.0)
        ]
        insert_multiple_students(test_db, students)

        delete_student(test_db, 1)

        assert get_student_count(test_db) == 1

        cursor = test_db.cursor()
        cursor.execute('SELECT name FROM students')
        result = cursor.fetchone()
        assert result[0] == 'Bob'

    def test_get_average_grade(self, test_db):
        """get_average_grade 함수 테스트"""
        create_table(test_db)

        # 학생이 없을 때
        assert get_average_grade(test_db) == 0.0

        students = [
            ('Alice', 20, 80.0),
            ('Bob', 22, 90.0),
            ('Charlie', 21, 85.0)
        ]
        insert_multiple_students(test_db, students)

        avg = get_average_grade(test_db)
        assert abs(avg - 85.0) < 0.01


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
