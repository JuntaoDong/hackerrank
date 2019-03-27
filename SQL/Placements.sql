SELECT S.NAME
FROM (Students S JOIN Friends F ON S.ID=F.ID
    JOIN Packages P1 on S.ID=P1.ID
    JOIN Packages P2 on F.Friend_ID=P2.ID)
WHERE P2.Salary > P1.Salary
ORDER BY P2.Salary;