-- creates a trigger that resets the attribute `valid_email` 
-- only when the email has been changed
DELIMITER $$
CREATE TRIGGER email_validity
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
	-- check if email column is updated
	IF NEW.email <> OLD.email THEN
		-- reset valid email to 0
		SET NEW.valid_email = 0;
	END IF;
END;
$$
DELIMITER ;
