DROP procedure gethospitalname; 

DELIMITER $$

CREATE PROCEDURE gethospitalname(IN P_emailID VARCHAR(50))
BEGIN
	SELECT  * FROM hospital where emailID=P_emailID;
END $$

DELIMITER ;
