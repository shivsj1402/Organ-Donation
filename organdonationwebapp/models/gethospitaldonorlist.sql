DROP procedure gethospitaldonorlist; 

DELIMITER $$

CREATE PROCEDURE gethospitaldonorlist(IN P_name VARCHAR(50))
BEGIN
	select userFirstName, userLastName, emailID, city, province,
	group_concat(organ) as organ, requestdate
	from user
	group by  emailID;
END $$

DELIMITER ;