# Program to analyse student course enrolments
# using set operations and tuples

# Student details stored as tuples
student1 = (101, "Rahul", "Computer Science")
student2 = (102, "Priya", "Information Technology")

# Courses enrolled by students
courses_student1 = {"Python", "Java", "Database", "Web Development"}
courses_student2 = {"Python", "Database", "Networking", "Cloud Computing"}

print("Student 1 Details:", student1)
print("Student 2 Details:", student2)

print("\nCourses of Student 1:")
print(courses_student1)

print("\nCourses of Student 2:")
print(courses_student2)

# Union
print("\nAll Unique Courses:")
print(courses_student1.union(courses_student2))

# Intersection
print("\nCommon Courses:")
print(courses_student1.intersection(courses_student2))

# Difference
print("\nCourses only in Student 1:")
print(courses_student1.difference(courses_student2))

print("\nCourses only in Student 2:")
print(courses_student2.difference(courses_student1))

