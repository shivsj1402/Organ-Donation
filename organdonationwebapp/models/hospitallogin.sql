DROP procedure hospitallogin; 

DELIMITER $$

CREATE PROCEDURE hospitallogin(IN p_emailID VARCHAR(45), p_password VARCHAR(45), OUT p_emailOUT VARCHAR(45))
BEGIN
	SELECT emailID INTO p_emailOUT FROM hospital where emailID=p_emailID and password= p_password;
END $$

DELIMITER ;