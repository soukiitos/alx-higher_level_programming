-- Import in hbtn_0c_0 database
SELECT `city`, AVG(`value`) OVER(PARTITION BY `city`) AS `avg_temp` FROM `temperatures` ORDER BY `avg_temp` DESC;
