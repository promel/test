SELECT PolicyType ,SUM(Balance) AS SUM 
FROM policy 
GROUP BY PolicyType