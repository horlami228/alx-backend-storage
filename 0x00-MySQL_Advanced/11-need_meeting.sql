-- CREATE A VIEW THAT LIST ALL STUDENTS UNDER A SCORE OF 80
-- AND NO LAST MEETING OR NOT MORE THAN A MONTH

DROP VIEW IF EXISTS need_meeting;

CREATE VIEW need_meeting AS
SELECT name FROM students WHERE score < 80
AND (last_meeting IS NULL
OR last_meeting < DATE_SUB(CURDATE(), INTERVAL 1 MONTH));
