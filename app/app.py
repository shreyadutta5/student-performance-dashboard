from flask import Flask, render_template
import sqlite3
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    conn = sqlite3.connect('../data/student.db')

    df = pd.read_sql("""
                     SELECT s.name, s.department, m.subject, m.marks
                     FROM students s
                     JOIN marks m ON s.student_id = m.student_id
                     """, conn)
    
    avg_marks = pd.read_sql("SELECT AVG(marks) AS avg_marks FROM marks", conn)
    max_marks = pd.read_sql("SELECT MAX(marks) AS max_marks FROM marks", conn)
    total_students = pd.read_sql("SELECT COUNT(DISTINCT student_id) AS total_students FROM students", conn)

    chart_df = pd.read_sql("""
                           SELECT s.name, AVG(m.marks) AS avg_marks
                           FROM students s
                           JOIN marks m ON s.student_id = m.student_id
                           GROUP BY s.name
                           ORDER BY s.name
                           """, conn)

    avg_value = round(avg_marks['avg_marks'][0], 2)
    max_value = max_marks['max_marks'][0]
    total_value = total_students['total_students'][0]

    chart_labels = chart_df['name'].tolist()
    chart_values = [round(x, 2) for x in chart_df['avg_marks'].tolist()]

    conn.close()

    return render_template(
        'index.html', 
        tables=df.to_dict(orient='records'),
        avg=avg_value,
        max=max_value,
        total=total_value,
        chart_labels=chart_labels,
        chart_values=chart_values
    )

if __name__ == '__main__':
    app.run(debug=True)

