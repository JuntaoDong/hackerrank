SELECT T.X, T.Y FROM
(SELECT F1.X, F1.Y 
FROM (FUNCTIONS F1 JOIN FUNCTIONS F2 ON F1.X=F2.Y AND F1.Y=F2.X AND F1.X<>F1.Y)
WHERE F1.X<F1.Y
UNION
SELECT F1.X, F1.Y
FROM (FUNCTIONS F1 JOIN FUNCTIONS F2 ON F1.X=F2.Y AND F1.Y=F2.X AND F1.X=F1.Y)
GROUP BY 1, 2
HAVING COUNT(F1.X) > 1) AS T
ORDER BY 1;