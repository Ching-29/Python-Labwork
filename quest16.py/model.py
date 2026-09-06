import sqlite3


class StudentModel:
    def __init__(self):
        self.connection = sqlite3.connect("students.db")
        self.create_table()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS students (
            roll_no INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            department TEXT NOT NULL,
            cgpa REAL NOT NULL
        )
        """
        self.connection.execute(query)
        self.connection.commit()

    def add_student(self, roll_no, name, department, cgpa):
        try:
            query = """
            INSERT INTO students (roll_no, name, department, cgpa)
            VALUES (?, ?, ?, ?)
            """
            self.connection.execute(
                query, (roll_no, name, department, cgpa)
            )
            self.connection.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def get_students(self):
        query = "SELECT roll_no, name, department, cgpa FROM students"
        cursor = self.connection.execute(query)
        return cursor.fetchall()

    def get_student(self, roll_no):
        query = """
        SELECT roll_no, name, department, cgpa
        FROM students
        WHERE roll_no = ?
        """
        cursor = self.connection.execute(query, (roll_no,))
        return cursor.fetchone()

    def delete_student(self, roll_no):
        query = "DELETE FROM students WHERE roll_no = ?"
        cursor = self.connection.execute(query, (roll_no,))
        self.connection.commit()
        return cursor.rowcount > 0

    def close(self):
        self.connection.close()
