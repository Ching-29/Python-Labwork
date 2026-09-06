import sqlite3


class SalaryReportModel:

    def __init__(self):
        self.conn = sqlite3.connect("employees.db")
        self.create_table()
        self.insert_sample_data()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS employees (
            employee_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            designation TEXT NOT NULL,
            department TEXT NOT NULL,
            salary REAL NOT NULL
        )
        """
        self.conn.execute(query)
        self.conn.commit()

    def insert_sample_data(self):
        query = """
        INSERT OR IGNORE INTO employees
        (employee_id, name, designation, department, salary)
        VALUES (?, ?, ?, ?, ?)
        """

        data = [
            (101, "Rahul", "Manager", "HR", 55000),
            (102, "Anita", "Developer", "IT", 60000),
            (103, "Amit", "Tester", "IT", 45000),
            (104, "Priya", "Accountant", "Finance", 50000),
            (105, "Ravi", "Developer", "IT", 65000),
            (106, "Sneha", "Executive", "HR", 40000)
        ]

        self.conn.executemany(query, data)
        self.conn.commit()

    def get_department_report(self, department):
        # Parameterized SQL query
        query = """
        SELECT employee_id, name, designation, salary
        FROM employees
        WHERE department = ?
        ORDER BY salary DESC
        """

        cursor = self.conn.execute(query, (department,))
        return cursor.fetchall()

    def get_department_summary(self, department):
        query = """
        SELECT
            COUNT(*),
            SUM(salary),
            AVG(salary),
            MAX(salary),
            MIN(salary)
        FROM employees
        WHERE department = ?
        """

        cursor = self.conn.execute(query, (department,))
        return cursor.fetchone()

    def close(self):
        self.conn.close()
