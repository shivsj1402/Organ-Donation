DROP procedure requestlistprofile; 

DELIMITER $$

CREATE PROCEDURE requestlistprofile(IN p_emailID VARCHAR(45), P_hospitalName VARCHAR(55))
BEGIN
	SELECT DISTINCT emailID , userFirstName, userLastName FROM user WHERE emailID = p_emailID AND donationType='d' and hospital=P_hospitalName;
END $$

DELIMITER ;