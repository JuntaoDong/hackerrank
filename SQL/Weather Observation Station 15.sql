SELECT ROUND(LONG_W,4)
FROM (SELECT LONG_W, LAT_N
    FROM STATION
    WHERE LAT_N < 137.2345
    ORDER BY 2 DESC LIMIT 1) AS MAXLATN; 