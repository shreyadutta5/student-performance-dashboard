-- Show all data
SELECT * FROM marks;

-- Show only Math marks
SELECT * FROM marks WHERE subject = 'Math';

-- Average marks of all students
SELECT AVG(marks) AS average_marks FROM marks;

-- Highest marks
SELECT MAX(marks) AS highest_marks FROM marks;

-- Average marks per student
SELECT student_id, AVG(markss) AS avg_marks
FROM marks
GROUP BY student_id;

-- Count number of subjects per students
SELECT student_id, COUNT(subject) AS subject_count
FROM marks
GROUP BY student_id;