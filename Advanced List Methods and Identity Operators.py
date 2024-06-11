# Objective:
# The aim of this assignment is to delve deeper into list methods and understand the nuances of identity operators.
# Problem Statement:
# You have two lists of student names. One list contains the names of students who have submitted their assignments, and the other list contains the names of students who attended the last class.

# Task 1: Given the two lists:

# submitted = ["Alice", "Bob", "Charlie", "David"]
# attended = ["Charlie", "Eve", "Alice", "Frank"]
# Find out which students both submitted their assignments and attended the class.

sudmitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]
common_students = []
for student in sudmitted:
    if student in attended:
        common_students.append(student)
print(common_students)

# Task 2: Check if the two lists are identical in terms of their content, regardless of order.

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]
if (submitted) == (attended):
    print("The two lists are identical.")
else:
    print("The two lists are not identical.")

# Task 3: Using list methods, remove any student from the attended list who did not submit their assignment. 

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]
for student in attended:
    if student not in submitted:
        attended.remove(student)
print(attended)

    