# About MYSQL REGEXP: https://dev.mysql.com/doc/refman/5.5/en/regexp.html

SELECT DISTINCT CITY
FROM STATION
WHERE CITY
REGEXP '^[^AEIOU]';