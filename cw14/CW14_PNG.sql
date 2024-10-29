-- CREATE TABLE patient (
-- id INT PRIMARY KEY,
-- first_name VARCHAR(50),
-- last_name VARCHAR(50),
-- phone VARCHAR(20) UNIQUE,
-- national_id VARCHAR(20) UNIQUE);

select * from patient;

-- INSERT INTO patient (blood_type,age) VALUES
-- (1, 'Akbar', 'Babaii', '09123456789', '0123456784'),
-- (2, 'Asqer', 'Mamadi', '09373456788', '0123456782'),
-- (3, 'Reza', 'Babaii', '09373456787', '0123456787'),
-- (4, 'Reza', 'Akbari', '09363456786', '0123456786'),
-- (5, 'Akbar', 'Akbari', '09123456785', '0123456785'),
-- (6, 'Mamad', 'Babaii', '09123456784', '0123456783'),
-- (7, 'Akbar', 'Salari', '09373456783', '0123456781')

-- alter table patient add age int;


-- ALTER TABLE patient ADD COLUMN age INT;

-- UPDATE patient SET blood_type = 'B+' WHERE id = 1;
-- UPDATE patient SET blood_type = 'O-' WHERE id = 2;
-- UPDATE patient SET blood_type = 'AB-' WHERE id = 3;
-- UPDATE patient SET blood_type = 'AB+' WHERE id = 4;
-- UPDATE patient SET blood_type = 'A+' WHERE id = 5;
-- UPDATE patient SET blood_type = 'B-' WHERE id = 6;
-- UPDATE patient SET blood_type = 'B-' WHERE id = 7;

-- SELECT * FROM patient ORDER BY age LIMIT 4 OFFSET 3; --6


-- SELECT * FROM patient WHERE blood_type LIKE 'AB%'; --7

-- select * FROM patient WHERE first_name LIKE 'A%' and age > 40; --8


-- select * FROM patient WHERE last_name like 'Ba%' and phone LIKE '0912%' ; --9

--10
-- UPDATE patient
-- SET phone = REPLACE(phone, '09', '+98')

