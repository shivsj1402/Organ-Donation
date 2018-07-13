DROP procedure validatehospital; 

DELIMITER $$

CREATE PROCEDURE validatehospital( IN P_hname VARCHAR(45))
BEGIN
	UPDATE hospital SET validate=true WHERE hospitalName=P_hname;
    
END $$

DELIMITER ;