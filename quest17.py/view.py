class EmployeeView:

    def show_menu(self):
        print("\n===== Employee Management System =====")
        print("1. Add Employee")
        print("2. Display All Employees")
        print("3. Search Employee")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Exit")

    def get_employee_details(self):
        employee_id = int(input("Enter Employee ID: "))
        name = input("Enter Name: ")
        designation = input("Enter Designation: ")
        department = input("Enter Department: ")
        salary = float(input("Enter Salary: "))

        return employee_id, name, designation, department, salary

    def get_update_details(self):
        name = input("Enter New Name: ")
        designation = input("Enter New Designation: ")
        department = input("Enter New Department: ")
        salary = float(input("Enter New Salary: "))

        return name, designation, department, salary

    def get_employee_id(self):
        return int(input("Enter Employee ID: "))

    def display_employees(self, employees):
        if not employees:
            print("\nNo employee records found.")
            return

        print("\n" + "-" * 85)
        print(
            f"{'ID':<8}"
            f"{'Name':<18}"
            f"{'Designation':<20}"
            f"{'Department':<20}"
            f"{'Salary':<12}"
        )
        print("-" * 85)

        for emp in employees:
            print(
                f"{emp[0]:<8}"
                f"{emp[1]:<18}"
                f"{emp[2]:<20}"
                f"{emp[3]:<20}"
                f"{emp[4]:<12.2f}"
            )

        print("-" * 85)

    def display_employee(self, employee):
        if employee:
            print("\nEmployee Details")
            print("-------------------------")
            print("Employee ID :", employee[0])
            print("Name        :", employee[1])
            print("Designation :", employee[2])
            print("Department  :", employee[3])
            print("Salary      :", employee[4])
        else:
            print("\nEmployee not found.")

    def show_message(self, message):
        print("\n" + message)
