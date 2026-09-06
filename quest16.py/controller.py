class StudentController:

    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_student(self):
        try:
            roll_no, name, department, cgpa = \
                self.view.get_student_details()

            if cgpa < 0 or cgpa > 10:
                self.view.show_message(
                    "CGPA must be between 0 and 10."
                )
                return

            if self.model.add_student(
                roll_no, name, department, cgpa
            ):
                self.view.show_message(
                    "Student added successfully."
                )
            else:
                self.view.show_message(
                    "Roll number already exists."
                )

        except ValueError:
            self.view.show_message(
                "Invalid input. Please enter valid values."
            )

    def display_students(self):
        students = self.model.get_students()
        self.view.display_students(students)

    def search_student(self):
        try:
            roll_no = self.view.get_roll_no()
            student = self.model.get_student(roll_no)
            self.view.display_student(student)

        except ValueError:
            self.view.show_message(
                "Invalid roll number."
            )

    def delete_student(self):
        try:
            roll_no = self.view.get_roll_no()

            if self.model.delete_student(roll_no):
                self.view.show_message(
                    "Student deleted successfully."
                )
            else:
                self.view.show_message(
                    "Student not found."
                )

        except ValueError:
            self.view.show_message(
                "Invalid roll number."
            )

    def run(self):
        while True:
            self.view.show_menu()

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_student()

            elif choice == "2":
                self.display_students()

            elif choice == "3":
                self.search_student()

            elif choice == "4":
                self.delete_student()

            elif choice == "5":
                self.view.show_message(
                    "Thank you for using the system."
                )
                self.model.close()
                break

            else:
                self.view.show_message(
                    "Invalid choice. Please try again."
                )
