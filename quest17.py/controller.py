class EmployeeController:

    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_employee(self):
        try:
            details = self.view.get_employee_details()

            if self.model.add_employee(*details):
                self.view.show_message(
                    "Employee added successfully."
                )
            else:
                self.view.show_message(
                    "Employee ID already exists."
                )

        except ValueError:
            self.view.show_message("Invalid input.")

    def display_employees(self):
        employees = self.model.get_all_employees()
        self.view.display_employees(employees)

    def search_employee(self):
        try:
            employee_id = self.view.get_employee_id()
            employee = self.model.get_employee(employee_id)
            self.view.display_employee(employee)

        except ValueError:
            self.view.show_message("Invalid Employee ID.")

    def update_employee(self):
        try:
            employee_id = self.view.get_employee_id()

            employee = self.model.get_employee(employee_id)

            if not employee:
                self.view.show_message("Employee not found.")
                return

            details = self.view.get_update_details()

            if self.model.update_employee(employee_id, *details):
                self.view.show_message(
                    "Employee updated successfully."
                )

        except ValueError:
            self.view.show_message("Invalid input.")

    def delete_employee(self):
        try:
            employee_id = self.view.get_employee_id()

            if self.model.delete_employee(employee_id):
                self.view.show_message(
                    "Employee deleted successfully."
                )
            else:
                self.view.show_message(
                    "Employee not found."
                )

        except ValueError:
            self.view.show_message("Invalid Employee ID.")

    def run(self):
        while True:
            self.view.show_menu()
            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_employee()

            elif choice == "2":
                self.display_employees()

            elif choice == "3":
                self.search_employee()

            elif choice == "4":
                self.update_employee()

            elif choice == "5":
                self.delete_employee()

            elif choice == "6":
                self.view.show_message("Exiting application...")
                self.model.close()
                break

            else:
                self.view.show_message(
                    "Invalid choice. Please try again."
                )
