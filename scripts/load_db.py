import pandas as pd
import sqlite3

#Read cleaned data
df = pd.read_csv('../data/cleaned_marks.csv')

#Connect to SQLite database
conn = sqlite3.connect('../data/student.db')

#Store data into a table
df.to_sql('marks', conn, if_exists='replace', index=False)
print("Marks table loaded successfully!")

#Read students data
students = pd.read_csv('../data/students.csv')

#Load into database
students.to_sql('students', conn, if_exists='replace', index=False)
print("Students data loaded successfully!")

#Show inserted data (marks table)
result = pd.read_sql("SELECT * FROM marks", conn)
print("\nMarks Table:")
print(result)

#Show inserted data (students table)
students_result = pd.read_sql("SELECT * FROM students", conn)
print("\nStudents Table:")
print(students_result)

#Close connection
conn.close()

