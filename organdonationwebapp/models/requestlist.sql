DROP procedure requestlist; 

DELIMITER $$

CREATE PROCEDURE requestlist(IN p_emailID VARCHAR(45))
BEGIN
    SELECT * FROM requestdata where hospitalID=p_emailID;
END $$

DELIMITER ;