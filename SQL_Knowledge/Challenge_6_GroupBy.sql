--Challenge 1: I need to know how many people have the same middlename
SELECT MiddleName, COUNT(MiddleName) as MiddlenameCount
FROM AdventureWorks2017.Person.Person
GROUP BY MiddleName


--Challenge 2: I need to know the mean quantity of selled products

SELECT ProductID, avg(OrderQty) as ProductAverageSell	
FROM AdventureWorks2017.Sales.SalesOrderDetail
GROUP BY ProductID

--Challenge 3: The 10 highest value sell per product from highest to lowest
SELECT TOP (10) ProductID, MAX(LineTotal) as MaxSell
FROM AdventureWorks2017.Sales.SalesOrderDetail
GROUP BY ProductID
ORDER BY MaxSell DESC

--Challenge 4: Need to know total products and mean products on work order

SELECT ProductID, SUM(OrderQty) as StockProducts, AVG(OrderQty) as AvgStockProducts
FROM AdventureWorks2017.Production.WorkOrder
GROUP BY ProductID
;