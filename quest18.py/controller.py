class SalaryReportController:

    def __init__(self, model, view):
        self.model = model
        self.view = view

    def generate_report(self):
        department = self.view.get_department()

        employees = self.model.get_department_report(
            department
        )

        summary = self.model.get_department_summary(
            department
        )

        self.view.display_report(
            department,
            employees,
            summary
        )

    def run(self):
        while True:
            print("\n===== Salary Report System =====")
            print("1. Generate Department Salary Report")
            print("2. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.generate_report()

            elif choice == "2":
                self.view.show_message(
                    "Exiting application..."
                )
                self.model.close()
                break

            else:
                self.view.show_message(
                    "Invalid choice."
                )
