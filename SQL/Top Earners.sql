/* GROUP BY 1 & ORDER BY 1: here 1 is the column number, which means group by or order by the first column from SELECT that is EARNINGS */

SELECT MONTHS*SALARY AS EARNINGS, COUNT(*)
FROM EMPLOYEE
GROUP BY 1
ORDER BY 1 DESC
LIMIT 1;