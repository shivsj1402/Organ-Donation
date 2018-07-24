DROP procedure gethospitalreceiverlist; 

DELIMITER $$

CREATE PROCEDURE gethospitalreceiverlist(IN P_name VARCHAR(50))
BEGIN
	select userFirstName, userLastName, emailID, city, province,
	group_concat(organ) as organ, requestdate
	from user where donationType='r'
	group by emailID;
END $$

DELIMITER ;