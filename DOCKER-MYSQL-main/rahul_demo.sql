CREATE DATABASE rahul;
USE rahul;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100),
    age INT
);

INSERT INTO users (username, age) VALUES ('Rahul', 21), ('xyz', 21);
