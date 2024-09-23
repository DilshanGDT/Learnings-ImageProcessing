
# An empty list to store marks
marks = []

file = open("marks.txt", "r")

# a. Read ten marks of a student and store it in to an empty list called ‘marks’
for line in file:
    marks.extend([float(mark.strip()) for mark in line.split(',')])
print('Student Marks List = ', marks)

# b. Sort the ‘marks’ list in ascending order
print('Sorted Student Marks = ', sorted(marks))

# c. Print the total, mean, median and mode element of the ‘marks’ list
import statistics

def meanMedMode(dataSet):
    total = sum(dataSet)
    mean = statistics.mean(dataSet)
    median = statistics.median(dataSet)
    mode = statistics.mode(dataSet)

    print(f'Student Marks : Mean = {mean}, Median = {median}, Mode = {mode}, Total = {total}')

meanMedMode(marks)

# d.  find the grade for each mark and insert into ‘grade’ list
def gradeAssign(marks):
    if marks>=80:
        return 'A'
    elif marks>=60:
        return 'B'
    elif marks>=50:
        return 'C'
    elif marks>=30:
        return 'D'
    elif marks>=0:
        return 'E'
    else:
        return 0

grades = []

for mark in sorted(marks):
    grades.append(gradeAssign(mark))

print('Student Grades List : ', grades)

file.close