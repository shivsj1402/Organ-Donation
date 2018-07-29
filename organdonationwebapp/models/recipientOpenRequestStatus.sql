DROP procedure recipientOpenRequestStatus; 

DELIMITER $$

CREATE PROCEDURE recipientOpenRequestStatus(IN p_donorID VARCHAR(45))
BEGIN
	SELECT * FROM requestdata WHERE donorID=p_donorID;
END $$

DELIMITER ;