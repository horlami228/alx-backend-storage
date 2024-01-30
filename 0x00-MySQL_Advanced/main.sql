-- USE testing;
-- DROP TABLE users;

-- INSERT INTO users(email, name, country) VALUES
--     ('akintolaolamielakn@gmail.com', 'Olamilekan', 'US'),
--     ('akintola51@gmail.com', 'Akintola', 'CO'),
--     ('lazycoding@gmail.com', 'Damien', 'TN');

-- INSERT INTO users(email, name) VALUES ('davigguetta@gmail.com', 'david');

-- SELECT * FROM metal_bands WHERE style LIKE '%Glam rock%'\G;


SELECT * FROM need_meeting;
UPDATE students SET last_meeting = ADDDATE(CURDATE(), INTERVAL -2 MONTH) WHERE name = 'Jean';
UPDATE students SET score = 40 WHERE name = 'Bob';
SELECT * FROM students;

SELECT * FROM need_meeting;