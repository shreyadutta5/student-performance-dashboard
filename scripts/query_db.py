import sqlite3
import pandas as pd
conn = sqlite3.connect('../data/student.db')

# Query 1: Show all data
df = pd.read_sql("SELECT * FROM marks", conn)
print("\nAll Data:")
print(df)

# Query 2: Average marks
avg = pd.read_sql("SELECT AVG(marks) AS avg_marks FROM marks", conn)
print("\nAverage Marks:")
print(avg)

# Query 3: Average per student
grouped = pd.read_sql("""
                      SELECT student_id, AVG(marks) AS avg_marks
                      FROM marks
                      GROUP BY student_id
                      """, conn)

print("\nAverage Marks per Students:")
print(grouped)

# JOIN query: Combine student name with marks
join_query = pd.read_sql("""
                         SELECT s.name, s.department, m.subject, m.marks
                         FROM students s
                         JOIN marks m
                         ON s.student_id = m.student_id
                         """, conn)

print("\nJoined Data (Student + Marks):")
print(join_query)

# ADVANCE QUERIES:
# 1. Top performing student
top_student = pd.read_sql("""
                          SELECT s.name, AVG(m.marks) AS avg_marks
                          FROM students s
                          JOIN marks m ON s.student_id = m.student_id
                          GROUP BY s.name
                          ORDER BY avg_marks DESC
                          LIMIT 1
                          """, conn)
print("\nTop Performing Student:")
print(top_student)

# 2. Subject-wise average
subject_avg = pd.read_sql("""
                          SELECT subject, AVG(marks) AS avg_marks
                          FROM marks
                          GROUP BY subject
                          """, conn)

print("\nSubject-wise Average:")
print(subject_avg)

conn.close()
