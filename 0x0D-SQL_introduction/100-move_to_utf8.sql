-- Convert a database to utf-8
-- Convert database to utf8mb4
ALTER DATABASE `hbtn_0c_0`
CHARACTER SET = utf8mb4
COLLATE = utf8mb4_unicode_ci;

-- Convert table to utf8mb4
ALTER TABLE `hbtn_0c_0`.`first_table`
CONVERT TO CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

-- Convert column to utf8mb4
ALTER TABLE `hbtn_0c_0`.`first_table`
CHANGE `name` `name` VARCHAR(100)
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

