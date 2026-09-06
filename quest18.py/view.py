class SalaryReportView:

    def get_department(self):
        return input("Enter Department Name: ")

    def display_report(self, department, employees, summary):

        print("\n==============================================")
        print("       DEPARTMENT-WISE SALARY REPORT")
        print("==============================================")
        print("Department:", department)

        if not employees:
            print("\nNo employees found in this department.")
            return

        print("\n" + "-" * 70)
        print(
            f"{'ID':<8}"
            f"{'Name':<18}"
            f"{'Designation':<20}"
            f"{'Salary':<12}"
        )
        print("-" * 70)

        for employee in employees:
            print(
                f"{employee[0]:<8}"
                f"{employee[1]:<18}"
                f"{employee[2]:<20}"
                f"{employee[3]:<12.2f}"
            )

        print("-" * 70)

        count, total, average, maximum, minimum = summary

        print("Number of Employees :", count)
        print("Total Salary        :", total)
        print("Average Salary      :", round(average, 2))
        print("Highest Salary      :", maximum)
        print("Lowest Salary       :", minimum)

        print("=" * 70)

    def show_message(self, message):
        print("\n" + message)
