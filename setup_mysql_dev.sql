CREATE DATABASE IF NOT EXISTS in_person_db;
CREATE USER IF NOT EXISTS 'inperson'@'localhost' IDENTIFIED BY 'Development_200';
GRANT ALL PRIVILEGES ON `in_person_db`.* TO 'inperson'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'inperson'@'localhost';
FLUSH PRIVILEGES;
