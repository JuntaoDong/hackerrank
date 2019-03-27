/* 
1. Offset should be constant so one can't directly pass count(*)/2 to offset. However a workaround could be using prepared statement. 
2. Count of rows can be even or odd, if it's odd then select the middle one row, else select the middle two rows.
3. Round and AVG functions will be implemented before LIMIT function. So one needs to create a new table to make AVG function implemented after LIMIT. 
*/

SET @total_rows := (SELECT COUNT(*) FROM STATION);
SET @limit_rows := IF(@total_rows MOD 2 = 0, 2, 1);
SET @offset_rows := FLOOR(@total_rows/2-0.5);
PREPARE STMT FROM 'SELECT ROUND(AVG(LAT_N), 4)
FROM (SELECT LAT_N FROM STATION ORDER BY LAT_N LIMIT ? OFFSET ?) AS T;';
EXECUTE STMT USING @limit_rows, @offset_rows;
DEALLOCATE PREPARE STMT;
