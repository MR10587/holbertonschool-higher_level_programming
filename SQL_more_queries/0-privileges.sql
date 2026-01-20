-- GRANT ACCESS
CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY 'password';
CREATE USER 'user_0d_2'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_2'@'localhost' WITH GRANT OPTION;
