
SELECT 
    COLUMN_NAME AS 'Column',
    COLUMN_TYPE AS 'Type',
    IS_NULLABLE AS 'Null',
    COLUMN_KEY AS 'Key',
    COLUMN_DEFAULT AS 'Default',
    EXTRA AS 'Extra'
FROM information_schema.COLUMNS
WHERE TABLE_SCHEMA = DATABASE()  -- the database passed as argument
  AND TABLE_NAME = 'Books';
