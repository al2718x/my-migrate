DROP DATABASE IF EXISTS `test-my`;

CREATE DATABASE IF NOT EXISTS `test-my` COLLATE 'utf8mb4_unicode_ci';

USE `test-my`;

CREATE TABLE IF NOT EXISTS `user` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(255)
);

INSERT INTO
    `user` (`name`)
VALUES
    ('John'),
    ('Doe');