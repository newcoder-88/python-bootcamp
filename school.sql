CREATE DATABASE school; 

USE school;

CREATE TABLE Students (
    id INT PRIMARY KEY,
    name VARCHAR(100)
);
CREATE TABLE Courses (
    id INT PRIMARY KEY,
    student_id INT,
    course VARCHAR(100)
);

INSERT INTO Students (id, name) VALUES
(1, 'Sarah'),
(2, 'Ali'),
(3, 'John'),
(4, 'Maya');
INSERT INTO Courses (id, student_id, course) VALUES
(1, 1, 'Python'),
(2, 1, 'SQL'),
(3, 2, 'Database Management'),
(4, 2, 'Power BI'),
(5, 3, 'Web Development');

SELECT name , course FROM Students  INNER JOIN Courses ON Students.id = Courses.student_id;
SELECT Students.name , Courses.course FROM Students INNER JOIN Courses ON Students.id = Courses.student_id where Students.name = 'sarah';
SELECT Students.name , Courses.course FROM Students INNER JOIN Courses ON Students.id = Courses.student_id ORDER BY Students.name ; 

SELECT Students.name , Courses.course FROM Students LEFT JOIN Courses ON Students.id = Courses.student_id;
SELECT Students.name , Courses.course FROM Students LEFT JOIN Courses ON Students.id = Courses.student_id WHERE Courses.course IS NULL;

SELECT Students.name , Courses.course FROM Students RIGHT JOIN Courses ON Students.id = Courses.student_id;
SELECT Students.name , Courses.course FROM Students RIGHT JOIN Courses ON Students.id = Courses.student_id WHERE Students.name = 'Sarah';