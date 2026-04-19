import pandas as pd

#Read
students = pd.read_csv('../data/students.csv')
marks = pd.read_csv('../data/marks.csv')

#Display
print("Students Data:")
print(students)
print("\nMarks Data:")
print(marks)
