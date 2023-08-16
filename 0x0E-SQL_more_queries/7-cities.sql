-- Create the database hbtn_0d_usa and the table cities on MYSQL server
-- cities description:
-- id INT unique, auto generated, can’t be null and is a primary key
-- state_id INT, can’t be null and must be a FOREIGN KEY that references to id of the states table
-- name VARCHAR(256) can’t be null
-- If the database hbtn_0d_usa already exists, the script should not fail
-- If the table cities already exists, your script should not fail

CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
USE `hbtn_0d_usa`;
CREATE TABLE IF NOT EXISTS `states` (`id` INT AUTO_INCREMENT PRIMARY KEY, `name` VARCHAR(256) NOT NULL);
