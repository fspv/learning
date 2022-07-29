SELECT
    b.name
FROM
    Employee a
    JOIN Employee b ON a.managerId = b.id
GROUP BY
    a.managerId
HAVING
    count(*) >= 5
