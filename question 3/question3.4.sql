SELECT * FROM account a
JOIN policy p
ON p.AccountId = a.Id
JOIN acctran ac
ON ac.PolicyId = PolicyId
ORDER BY a.Name Asc