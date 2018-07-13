DROP procedure gethospitaldonorlist; 

DELIMITER $$

CREATE PROCEDURE gethospitaldonorlist(IN P_name VARCHAR(50))
BEGIN
	SELECT  * FROM user where donationType='d' AND hospital=P_name;
END $$

DELIMITER ;
