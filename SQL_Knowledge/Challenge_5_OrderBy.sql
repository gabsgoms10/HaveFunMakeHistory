--Challenge 1: Get the 10 most expensive productID, from the expensive to the cheaper
SELECT TOP(10) ProductID as TenMostExpensive
FROM AdventureWorks2017.Production.Product 
ORDER BY StandardCost desc


--Challenge 2: Get the name and number of the products that have the productID between 1 and 4
SELECT TOP(4) Name, ProductNumber
FROM AdventureWorks2017.Production.Product 
ORDER BY ProductID asc;

--Challenge 3: 