DROP procedure gethospitalreceiverlist; 

DELIMITER $$

CREATE PROCEDURE gethospitalreceiverlist(IN P_name VARCHAR(50))
BEGIN
	SELECT  * FROM user where donationType='r' AND hospital=P_name;
END $$

DELIMITER ;
