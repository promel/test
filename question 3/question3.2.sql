SELECT TranTypeId ,SUM(Amount) AS Sum
FROM acctran 
GROUP BY TranTypeId