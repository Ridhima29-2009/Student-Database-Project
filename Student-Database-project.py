CREATE TABLE Students (
    Student_ID INTEGER PRIMARY KEY,
    Name VARCHAR(50),
    Age INTEGER,
    Gender VARCHAR(10),
    City VARCHAR(30),
    Course VARCHAR(30),
    Marks INTEGER
);

INSERT INTO Students VALUES
(101,'Aman',20,'Male','Delhi','BCA',92),
(102,'Riya',21,'Female','Mumbai','BSc',95),
(103,'Rahul',19,'Male','Lucknow','BCom',80),
(104,'Priya',22,'Female','Delhi','BSc',88),
(105,'Arjun',20,'Male','Kanpur','BCA',90),
(106,'Sneha',21,'Female','Jaipur','BSc',85),
(107,'Karan',22,'Male','Delhi','BTech',78),
(108,'Anjali',20,'Female','Lucknow','BCA',91),
(109,'Vikas',23,'Male','Patna','BCom',75),
(110,'Pooja',21,'Female','Mumbai','BSc',89),
(111,'Rohit',20,'Male','Delhi','BTech',94),
(112,'Neha',19,'Female','Kanpur','BCA',87),
(113,'Akash',22,'Male','Jaipur','BSc',82),
(114,'Simran',21,'Female','Delhi','BCom',90),
(115,'Mohit',20,'Male','Lucknow','BCA',79);

SELECT * FROM Students;

SELECT Name, Marks
FROM Students;

SELECT Name, City
FROM Students;

SELECT *
FROM Students
WHERE Marks > 90;

SELECT *
FROM Students
WHERE City='Delhi';

SELECT *
FROM Students
WHERE Age BETWEEN 20 AND 22;

SELECT *
FROM Students
WHERE Name LIKE 'A%';

SELECT *
FROM Students
WHERE Name LIKE '%a';

SELECT *
FROM Students
WHERE Name LIKE '%i%';

SELECT *
FROM Students
ORDER BY Marks DESC;

SELECT *
FROM Students
ORDER BY City ASC;

SELECT *
FROM Students
ORDER BY City ASC, Marks DESC;

SELECT COUNT(*) AS Total_Students
FROM Students;

SELECT MAX(Marks) AS Highest_Marks
FROM Students;

SELECT MIN(Marks) AS Lowest_Marks
FROM Students;

SELECT AVG(Marks) AS Average_Marks
FROM Students;

SELECT SUM(Marks) AS Total_Marks
FROM Students;

SELECT City, COUNT(*)
FROM Students
GROUP BY City;

SELECT Course, COUNT(*)
FROM Students
GROUP BY Course;

SELECT City, AVG(Marks)
FROM Students
GROUP BY City;

SELECT Course, AVG(Marks)
FROM Students
GROUP BY Course;

SELECT City, COUNT(*)
FROM Students
GROUP BY City
HAVING COUNT(*) > 1;

SELECT Course, AVG(Marks)
FROM Students
GROUP BY Course
HAVING AVG(Marks) > 85;

SELECT DISTINCT City
FROM Students;

SELECT DISTINCT Course
FROM Students;

SELECT UPPER(Name)
FROM Students;

SELECT LOWER(Name)
FROM Students;

SELECT LENGTH(Name)
FROM Students;

SELECT ROUND(AVG(Marks),2)
FROM Students;

SELECT Name, Marks
FROM Students
WHERE Marks >
(
SELECT AVG(Marks)
FROM Students
);

SELECT Name, Marks
FROM Students
WHERE Marks=
(
SELECT MAX(Marks)
FROM Students
);

SELECT Name, Marks
FROM Students
WHERE Marks=
(
SELECT MIN(Marks)
FROM Students
);

UPDATE Students
SET Marks=85
WHERE Student_ID=103;

UPDATE Students
SET City='Noida'
WHERE Student_ID=105;

DELETE FROM Students
WHERE Student_ID=115;

ALTER TABLE Students
ADD Email VARCHAR(100);

UPDATE Students
SET Email='aman@gmail.com'
WHERE Student_ID=101;

UPDATE Students
SET Email='riya@gmail.com'
WHERE Student_ID=102;

UPDATE Students
SET Email='rahul@gmail.com'
WHERE Student_ID=103;

UPDATE Students
SET Email='priya@gmail.com'
WHERE Student_ID=104;

UPDATE Students
SET Email='arjun@gmail.com'
WHERE Student_ID=105;

SELECT *
FROM Students;

CREATE VIEW Top_Students AS
SELECT Student_ID, Name, City, Course, Marks
FROM Students
WHERE Marks >= 90;

SELECT * FROM Top_Students;

CREATE VIEW Delhi_Students AS
SELECT Student_ID, Name, City, Marks
FROM Students
WHERE City = 'Delhi';

SELECT * FROM Delhi_Students;

SELECT Name,
Marks,
ROW_NUMBER() OVER(ORDER BY Marks DESC) AS Row_Number
FROM Students;

SELECT Name,
Marks,
RANK() OVER(ORDER BY Marks DESC) AS Student_Rank
FROM Students;

SELECT Name,
Marks,
DENSE_RANK() OVER(ORDER BY Marks DESC) AS Dense_Rank
FROM Students;

SELECT Name,
Marks,
NTILE(2) OVER(ORDER BY Marks DESC) AS Group_No
FROM Students;

SELECT Name, Marks
FROM Students
LIMIT 5;

SELECT *
FROM Students
WHERE Course='BCA'
ORDER BY Marks DESC;

SELECT *
FROM Students
WHERE Course='BSc'
ORDER BY Marks DESC;

SELECT Name, Course, Marks
FROM Students
WHERE Marks BETWEEN 80 AND 90;

SELECT Name, City
FROM Students
WHERE City IN ('Delhi','Mumbai');

SELECT Name
FROM Students
WHERE City NOT IN ('Delhi');

SELECT COUNT(*) AS Delhi_Students
FROM Students
WHERE City='Delhi';

SELECT COUNT(*) AS Female_Students
FROM Students
WHERE Gender='Female';

SELECT COUNT(*) AS Male_Students
FROM Students
WHERE Gender='Male';

SELECT Course,
MAX(Marks) AS Highest_Marks
FROM Students
GROUP BY Course;

SELECT Course,
MIN(Marks) AS Lowest_Marks
FROM Students
GROUP BY Course;

SELECT Course,
ROUND(AVG(Marks),2) AS Average_Marks
FROM Students
GROUP BY Course;

SELECT City,
MAX(Marks)
FROM Students
GROUP BY City;

SELECT City,
MIN(Marks)
FROM Students
GROUP BY City;

SELECT City,
SUM(Marks)
FROM Students
GROUP BY City;

SELECT *
FROM Students
WHERE Marks >= 85
AND City='Delhi';

SELECT *
FROM Students
WHERE Marks >= 90
OR City='Mumbai';

SELECT *
FROM Students
WHERE NOT City='Delhi';

SELECT Name,
Marks,
CASE
WHEN Marks>=90 THEN 'Excellent'
WHEN Marks>=80 THEN 'Good'
WHEN Marks>=70 THEN 'Average'
ELSE 'Needs Improvement'
END AS Grade
FROM Students;

SELECT Name,
Marks
FROM Students
ORDER BY Marks DESC
LIMIT 3;

SELECT Name,
Marks
FROM Students
ORDER BY Marks ASC
LIMIT 3;

SELECT *
FROM Students
WHERE Marks >
(
SELECT AVG(Marks)
FROM Students
);

SELECT *
FROM Students
WHERE Marks <
(
SELECT AVG(Marks)
FROM Students
);

SELECT Name,
City,
Marks
FROM Students
ORDER BY City, Marks DESC;

SELECT Name,
Email
FROM Students
WHERE Email IS NOT NULL;

DROP VIEW Delhi_Students;

DROP VIEW Top_Students;

SELECT * FROM Students;