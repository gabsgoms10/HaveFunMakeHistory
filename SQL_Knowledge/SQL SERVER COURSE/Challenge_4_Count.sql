-- Challenge 1: How many products there is on our products table
SELECT COUNT(*) as Products_Count FROM AdventureWorks2017.Production.Product

--Challenge 2: How many products lenght there is on our products table
SELECT Count( Size) as Size_Count FROM AdventureWorks2017.Production.Product

--Challenge 3: How many different product lenght there is on our products table
SELECT Count(Distinct Size) as DifferentSize_Count FROM AdventureWorks2017.Production.Product


;