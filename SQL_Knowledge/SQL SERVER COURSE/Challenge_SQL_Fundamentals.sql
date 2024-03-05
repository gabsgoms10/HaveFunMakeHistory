-- Challenge 1: How many products in the system are more expensive than 1500?
SELECT COUNT(ListPrice) as MoreThan1500 
FROM AdventureWorks2017.Production.Product 
WHERE ListPrice > 1500

--Challenge 2: How many people the FirstName starts with P?
SELECT COUNT(FirstName) as StartWithP
FROM AdventureWorks2017.Person.Person 
WHERE FirstName LIKE 'P%'

--Challenge 3: From how many cities are your customers?
SELECT COUNT(DISTINCT(CITY)) as UniqueCustomersCity
FROM AdventureWorks2017.Person.Address

--Challenge 4: Wich cities our customers live in?
SELECT DISTINCT City AS CustomersCiry
FROM AdventureWorks2017.Person.Address

--Challenge 5: How many red products cost between 500 and 1000?
SELECT COUNT(ProductID) as RedProductsbet500and1000
FROM AdventureWorks2017.Production.Product
WHERE COLOR = 'RED' and ListPrice between 500 and 1000

--Challenge 6: How many products have 'road' in their names?
SELECT count(ProductID) as roadOnProduct
FROM AdventureWorks2017.Production.Product
WHERE Name LIKE '%road%';