DROP procedure getdonorlist; 

DELIMITER $$

CREATE PROCEDURE getdonorlist()
BEGIN
	SELECT  * FROM user where donationType='d';
END $$

DELIMITER ;