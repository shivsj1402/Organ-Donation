DROP procedure getreceiverlist; 

DELIMITER $$

CREATE PROCEDURE getreceiverlist()
BEGIN
	SELECT  * FROM user where donationType='d';
END $$

DELIMITER ;