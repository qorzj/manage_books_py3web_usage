CREATE DATABASE bookstore;
USE bookstore;

DROP TABLE IF EXISTS `tbl_book`;

CREATE TABLE `tbl_book` (
    `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
    `name` varchar(128) DEFAULT NULL,
    `author` varchar(128) DEFAULT NULL,
    `press` varchar(128) DEFAULT NULL,
    `create_at` datetime DEFAULT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
