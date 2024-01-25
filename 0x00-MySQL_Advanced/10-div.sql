-- A function that divides two numbers and returns a zero if
-- second operand is equal to zero
DROP FUNCTION IF EXISTS SafeDiv;

DELIMITER //

CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS FLOAT NO SQL

BEGIN
    DECLARE result FLOAT DEFAULT 0;

    IF b = 0
    THEN
        RETURN result;
    ELSE
        SET result = (a / b);
        RETURN result;
    END IF;

END//

DELIMITER ;
