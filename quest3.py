# Program to manage student records
# using lists and dictionaries

students = []


def insert_student():
    roll = int(input("Enter Roll Number: "))
    name = input("Enter Name: ")
    marks = float(input("Enter Marks: "))

    student = {
        "roll": roll,
        "name": name,
        "marks": marks
    }

    students.append(student)
    print("Student record inserted successfully.")


def delete_student():
    roll = int(input("Enter Roll Number to delete: "))

    for student in students:
        if student["roll"] == roll:
            students.remove(student)
            print("Student record deleted successfully.")
            return

    print("Student not found.")


def search_student():
    roll = int(input("Enter Roll Number to search: "))

    for student in students:
        if student["roll"] == roll:
            print("Student Found")
            print("Roll Number:", student["roll"])
            print("Name:", student["name"])
            print("Marks:", student["marks"])
            return

    print("Student not found.")


def display_students():
    if len(students) == 0:
        print("No student records available.")
    else:
        print("\nStudent Records:")
        for student in students:
            print(
                "Roll:", student["roll"],
                "| Name:", student["name"],
                "| Marks:", student["marks"]
            )


# Main menu
while True:
    print("\n--- Student Record Management ---")
    print("1. Insert Student")
    print("2. Delete Student")
    print("3. Search Student")
    print("4. Display Students")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        insert_student()

    elif choice == 2:
        delete_student()

    elif choice == 3:
        search_student()

    elif choice == 4:
        display_students()

    elif choice == 5:
        print("Program terminated.")
        break

    else:
        print("Invalid choice.")
