DROP procedure donorhospitalshowreceiverprofile; 

DELIMITER $$

CREATE PROCEDURE donorhospitalshowreceiverprofile(IN p_emailID VARCHAR(45))
BEGIN
	SELECT userFirstName, userLastName, emailID, dob, sex, organ FROM user WHERE emailID=p_emailID AND donationType='r';
END $$

DELIMITER ;