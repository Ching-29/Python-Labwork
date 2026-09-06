# Program to read student marks from a text file,
# calculate total, average and grade,
# and write results to an output file.

def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


input_file = "students.txt"
output_file = "results.txt"

with open(input_file, "r") as file:
    students = file.readlines()


with open(output_file, "w") as file:

    file.write("Student Results\n")
    file.write("-----------------------------\n")

    for line in students:
        data = line.split()

        roll = data[0]
        name = data[1]

        mark1 = float(data[2])
        mark2 = float(data[3])
        mark3 = float(data[4])

        total = mark1 + mark2 + mark3
        average = total / 3

        grade = calculate_grade(average)

        file.write("Roll Number: " + roll + "\n")
        file.write("Name: " + name + "\n")
        file.write("Total: " + str(total) + "\n")
        file.write("Average: " + str(round(average, 2)) + "\n")
        file.write("Grade: " + grade + "\n")
        file.write("-----------------------------\n")


print("Results calculated successfully.")
print("Results have been written to", output_file)
