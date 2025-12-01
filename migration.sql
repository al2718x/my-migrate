DROP DATABASE IF EXISTS `test`;

CREATE DATABASE IF NOT EXISTS `test` COLLATE 'utf8mb4_unicode_ci';

USE `test`;

CREATE TABLE IF NOT EXISTS `user` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(255)
);

INSERT INTO
    `user` (`name`)
VALUES
    ('John'),
    ('Doe');