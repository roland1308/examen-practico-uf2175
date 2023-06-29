DROP DATABASE IF EXISTS `gri`;
CREATE DATABASE IF NOT EXISTS `gri`;

USE `gri`;

CREATE TABLE `users` (
    id INT,
    name VARCHAR(20)
);

INSERT INTO users (id, name) VALUES (1, 'Merlin');
INSERT INTO users (id, name) VALUES (2, 'Ginger');
INSERT INTO users (id, name) VALUES (3, 'Nata');