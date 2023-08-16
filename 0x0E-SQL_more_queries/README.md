# 0x0E. SQL - More queries

![A SQL Query](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/66988091.jpg)

## Resources

- [How To Create a New User and Grant Permissions in MySQL](https://intranet.alxswe.com/rltoken/RniBKj48bnIN8xpXhGl1yA)
- [How To Use MySQL GRANT Statement To Grant Privileges To a User](https://intranet.alxswe.com/rltoken/FIiEIvA6IN_hSKM5TvgyxQ)
- [MySQL constraints](https://intranet.alxswe.com/rltoken/LrovGa6N-OE2ID_tpWZRaQ)
- [SQL technique: subqueries](https://intranet.alxswe.com/rltoken/kR71h5zjkPtx4kBoVf7q0g)
- [Basic query operation: the join](https://intranet.alxswe.com/rltoken/rNMJeQ1jbNTCljbvCSjf6w)
- [SQL technique: multiple joins and the distinct keyword](https://intranet.alxswe.com/rltoken/HhZ6TJ1q5S0aR4lhfpKdOQ)
- [SQL technique: join types](https://intranet.alxswe.com/rltoken/T6FZUQdsMzr8hgNInBzudA)
- [SQL technique: union and minus](https://intranet.alxswe.com/rltoken/Nd-sdM8QUpf0YKIlXzVv4w)
- [MySQL Cheat Sheet](https://intranet.alxswe.com/rltoken/iSNyinU6SPWTGDUWMmcRkg)
- [The Seven Types of SQL Joins](https://intranet.alxswe.com/rltoken/-plhBsra0N7BOuFoEg--zg)
- [MySQL Tutorial](https://intranet.alxswe.com/rltoken/I4Lws_eQrIrNTbkZvvk-oQ)
- [SQL Style Guide](https://intranet.alxswe.com/rltoken/051eAEP_rePBU7jeh879GA)
- [MySQL 8.0 SQL Statement Syntax](https://intranet.alxswe.com/rltoken/YavbYiraYFr8oTukT_N6eQ)

#####Extra resources around relational database model design:

- [Design](https://intranet.alxswe.com/rltoken/EWLRPeqr5sQ9AqfoG_KXxw)
- [Normalization](https://intranet.alxswe.com/rltoken/mqBhYoSYbhH5ZZrhDcY0kA)
- [ER Modeling](https://intranet.alxswe.com/rltoken/R0exkJmf-2ddKjGfa8D0dA)

## Learning Objectives

### General
- How to create a new MySQL user
- How to manage privileges for a user to a database or table
- What’s a PRIMARY KEY
- What’s a FOREIGN KEY
- How to use NOT NULL and UNIQUE constraints
- How to retrieve datas from multiple tables in one request
- What are subqueries
- What are JOIN and UNION
## Requirements
### General
- Allowed editors: vi, vim, emacs
- All files will be executed on Ubuntu 20.04 LTS using MySQL 8.0 (version 8.0.25)
- All files should end with a new line
- All SQL queries should have a comment just before (i.e. syntax above)
- All files should start by a comment describing the task
- All SQL keywords should be in uppercase (SELECT, WHERE…)
- The length of your files will be tested using wc

## More Info
### Comments for your SQL file:  
  
$ cat my_script.sql  
-- 3 first students in the Batch ID=3  
-- because Batch 3 is the best!  
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;  
$  
  
### Use "container-on-demand" to run MySQL
  
##### In the container, credentials are root/root

- Ask for container Ubuntu 20.04
- Connect via SSH
- OR connect via the Web terminal
- In the container, you should start MySQL before playing with it:  
$ service mysql start  
 * Starting MySQL database server mysqld  
$  
$ cat 0-list_databases.sql | mysql -uroot -p  
Database  
information_schema  
mysql  
performance_schema  
sys  
$  

##### In the container, credentials are root/root

### How to import a SQL dump  
  
$ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p  
Enter password:  
$ curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows  
Enter password:  
$ echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows  
Enter password:  
id  name  
1   Drama  
2   Mystery  
3   Adventure  
4   Fantasy  
5   Comedy  
6   Crime  
7   Suspense  
8   Thriller  
$  

![SQL](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/3/bc2575fee3303b731031.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230816%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230816T165435Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=c6101e2f29aee51a490a5f84611369d79857caf58008365e7d6f176ae25bb345)
