-- Import in hbtn_0c_0 database
SELECT `city`, AVG(`value`) AS `avg_temp` FROM `temperatures` WHERE `month` IN (7, 8) GROUP BY `city` ORDER BY `avg_temp` DESC LIMIT 3;
