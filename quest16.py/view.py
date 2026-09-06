class StudentView:

    def show_menu(self):
        print("\n===== Student Information Management System =====")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

    def get_student_details(self):
        roll_no = int(input("Enter Roll Number: "))
        name = input("Enter Name: ")
        department = input("Enter Department: ")
        cgpa = float(input("Enter CGPA: "))

        return roll_no, name, department, cgpa

    def get_roll_no(self):
        return int(input("Enter Roll Number: "))

    def display_students(self, students):
        if not students:
            print("\nNo student records found.")
            return

        print("\n" + "-" * 65)
        print(
            f"{'Roll No':<10}"
            f"{'Name':<20}"
            f"{'Department':<20}"
            f"{'CGPA':<10}"
        )
        print("-" * 65)

        for student in students:
            print(
                f"{student[0]:<10}"
                f"{student[1]:<20}"
                f"{student[2]:<20}"
                f"{student[3]:<10.2f}"
            )

        print("-" * 65)

    def display_student(self, student):
        if student:
            print("\nStudent Details")
            print("-------------------------")
            print("Roll Number :", student[0])
            print("Name        :", student[1])
            print("Department  :", student[2])
            print("CGPA        :", student[3])
        else:
            print("\nStudent not found.")

    def show_message(self, message):
        print("\n" + message)
