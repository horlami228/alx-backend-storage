# MySQL Advanced

```SQL
-- Create a stored procedure AddBonus that adds a new correction for a student

DELIMITER // ;
DROP PROCEDURE IF EXISTS AddBonus;

CREATE PROCEDURE AddBonus(
    IN user_id INT, 
    IN project_name VARCHAR(255), 
    IN score float)
    
-- BODY OF THE PROCEDURE
BEGIN
    DECLARE count_row INT;
    DECLARE project_id INT;

    SELECT COUNT(*) INTO count_row FROM
    projects WHERE name = project_name;

    -- Check if the project_name exist in the projects table
    IF count_row = 0
    THEN
        -- Insert into projects table
        INSERT INTO projects (name) VALUES (project_name);
    END IF;

    -- Get ID associated with the project name
    SELECT id INTO project_id FROM projects
    WHERE name = project_name;

    -- Insert the new correction
    INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, project_id, score);

END//

```