import sqlite3


class EmployeeModel:
    def __init__(self):
        self.conn = sqlite3.connect("employees.db")
        self.create_table()

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

    # CREATE
    def add_employee(self, employee_id, name, designation,
                     department, salary):
        try:
            query = """
            INSERT INTO employees
            (employee_id, name, designation, department, salary)
            VALUES (?, ?, ?, ?, ?)
            """
            self.conn.execute(
                query,
                (employee_id, name, designation, department, salary)
            )
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    # READ
    def get_all_employees(self):
        query = "SELECT * FROM employees"
        cursor = self.conn.execute(query)
        return cursor.fetchall()

    def get_employee(self, employee_id):
        query = "SELECT * FROM employees WHERE employee_id = ?"
        cursor = self.conn.execute(query, (employee_id,))
        return cursor.fetchone()

    # UPDATE
    def update_employee(self, employee_id, name, designation,
                        department, salary):
        query = """
        UPDATE employees
        SET name = ?, designation = ?, department = ?, salary = ?
        WHERE employee_id = ?
        """
        cursor = self.conn.execute(
            query,
            (name, designation, department, salary, employee_id)
        )
        self.conn.commit()
        return cursor.rowcount > 0

    # DELETE
    def delete_employee(self, employee_id):
        query = "DELETE FROM employees WHERE employee_id = ?"
        cursor = self.conn.execute(query, (employee_id,))
        self.conn.commit()
        return cursor.rowcount > 0

    def close(self):
        self.conn.close()
