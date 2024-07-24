# Calculating Grades (ok, let me think about this one)

# Write a program that will average 3 numeric exam grades, return an average test score, a corresponding letter grade, and a message stating whether the student is passing.

# Average	Grade
# 90+	A
# 80-89	B
# 70-79	C
# 60-69	D
# 0-59	F

# Exams: 89, 90, 90
# Average: 90
# Grade: A
# Student is passing.

# Exams: 50, 51, 0
# Average: 33
# Grade: F
# Student is failing.

# Prompt user to input three exam grades and convert them to integers
exam_one = int(input("Input exam grade one: "))
exam_two = int(input("Input exam grade two: "))
exam_three = int(input("Input exam grade three: "))

# Store grades in a list
grades = [exam_one, exam_two, exam_three]

# Initialize the sum variable to 0
sum = 0

# Loop through the grades list to calculate the total sum of grades
for grade in grades: 
    sum += grade

# Calculate the average grade
avg = sum / len(grades)

# Determine the letter grade based on the average
if avg >= 90:
    letter_grade = "A"
elif avg >= 80:
    letter_grade = "B"
elif avg >= 70:
    letter_grade = "C"
elif avg >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"

# Print each exam grade
for grade in grades:
    print("Exam: " + str(grade))

# Print the average grade
print("Average: " + str(avg))

# Print the corresponding letter grade
print("Grade: " + letter_grade)

# Print whether the student is passing or failing based on the letter grade
if letter_grade == "F":
    print("Student is failing.")
else:
    print("Student is passing.")

    
