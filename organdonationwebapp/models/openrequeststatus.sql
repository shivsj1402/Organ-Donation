DROP procedure openrequeststatus; 

DELIMITER $$

CREATE PROCEDURE openrequeststatus(IN p_recipientID VARCHAR(45))
BEGIN
	SELECT * FROM requestdata WHERE recipientID=p_recipientID;
END $$

DELIMITER ;