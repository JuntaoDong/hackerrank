/* Round, Ceiling and Floor
 https://www.mssqltips.com/sqlservertip/1589/sql-server-rounding-functions--round-ceiling-and-floor/ */

SELECT CEIL(AVG(Salary)-AVG(REPLACE(Salary,'0',''))) FROM EMPLOYEES;
