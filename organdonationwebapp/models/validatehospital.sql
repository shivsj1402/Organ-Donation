DROP procedure validatehospital; 

DELIMITER $$

CREATE PROCEDURE validatehospital( IN P_emailID VARCHAR(45))
BEGIN
	UPDATE hospital SET validate=true WHERE emailID=P_emailID;
    
END $$

DELIMITER ;