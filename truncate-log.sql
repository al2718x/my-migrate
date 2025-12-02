-- DELETE FROM `log` WHERE `updated_at` < (NOW() - INTERVAL 1 MONTH);
-- DELETE FROM `log` WHERE `updated_at` < (NOW() - INTERVAL 1 WEEK);
DELETE FROM `log` WHERE `updated_at` < (NOW() - INTERVAL 3 DAY);
-- DELETE FROM `log` WHERE `updated_at` < (NOW() - INTERVAL 1 DAY);
