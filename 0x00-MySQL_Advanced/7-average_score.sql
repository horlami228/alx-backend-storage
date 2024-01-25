-- A stored procedure that computes and return the average score

DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;

DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
-- BODY OF THE PROCEDURE

BEGIN
    DECLARE avg_score DECIMAL(10, 2);

    -- GET THE AVERAGE SCORE
    SET avg_score = (SELECT AVG(score) FROM corrections AS cor WHERE cor.user_id = user_id);

    -- Update the score in the users table

    UPDATE users SET average_score = avg_score WHERE id = user_id;
END //
