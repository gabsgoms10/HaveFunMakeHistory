-- Challenge 1: We need to identify the stateProvinceID that occurs most on our system, we'll query the ones that appears more than 1000 times
SELECT StateProvinceID, COUNT(StateProvinceID) AS CountProvince
FROM AdventureWorks2017.Person.Address
GROUP BY StateProvinceID
HAVING COUNT(StateProvinceID) > 1000



--Challenge 2: We want to identify the products that selled 1 million dolar
SELECT ProductID, SUM(LineTotal) as totalSelled
FROM AdventureWorks2017.Sales.SalesOrderDetail
GROUP BY ProductID
HAVING SUM(LineTotal) > 1000000

;