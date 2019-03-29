SELECT 
    s.submission_date, uniquesub, h.hacker_id, name
FROM
    Hackers h,
    (SELECT 
        submission_date,
            hacker_id,
            totalsub,
            CASE submission_date
                WHEN @curDate THEN @curRow:=@curRow + 1
                ELSE @curRow:=1
            END AS rowgroup,
            @curDate:=submission_date AS subDate
    FROM
        (SELECT 
        submission_date, hacker_id, COUNT(submission_id) AS totalsub
    FROM
        Submissions s
    GROUP BY hacker_id , submission_date
    ORDER BY submission_date , totalsub DESC , hacker_id ASC) dd
    JOIN (SELECT @curRow:=0, @curDate:='') r) s,
    (SELECT 
        submission_date, COUNT(*) as uniquesub
    FROM
        (SELECT 
        submission_date,
            hacker_id,
            totalsub,
            CASE hacker_id
                WHEN @curHacker THEN @curRow:=@curRow + 1
                ELSE @curRow:=1
            END AS continuesub,
            @curHacker:=hacker_id AS hackerid
    FROM
        (SELECT 
        submission_date, hacker_id, COUNT(submission_id) AS totalsub
    FROM
        Submissions s
    GROUP BY hacker_id , submission_date
    ORDER BY hacker_id , submission_date) dd
    JOIN (SELECT @curRow:=0, @curHacker:=0) r) x, (SELECT 
        MIN(submission_date) AS startdate
    FROM
        Submissions) y
    WHERE
        continuesub = DATEDIFF(submission_date, startdate) + 1
    GROUP BY submission_date) x
WHERE
    s.rowgroup = 1
        AND h.hacker_id = s.hacker_id
        AND x.submission_date = s.submission_date
ORDER BY s.submission_date