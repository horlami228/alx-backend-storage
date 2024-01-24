-- Resets the valid_email attribute only when the email is updated

DELIMITER // ;

CREATE TRIGGER reset_valid_email
BEFORE UPDATE ON users FOR EACH ROW

-- BODY OF THE TRIGGER
BEGIN
    IF NEW.email != OLD.email
    THEN
        IF OLD.valid_email = 0
        THEN
           SET NEW.valid_email = 1;
        ELSE
            SET NEW.valid_email = 0;
        END IF;
    END IF;
END//
