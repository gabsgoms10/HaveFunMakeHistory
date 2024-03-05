-- BETWEEN STATEMENT (WORKS WITH NUMBERS, DATES)

SELECT *
FROM AdventureWorks2017.HumanResources.Employee
WHERE HireDate between '2009/01/01' and '2010/04/05'
ORDER BY HireDate asc



SELECT *
FROM AdventureWorks2017.Production.Product
WHERE ListPrice between 500 and 1000

-- LIKE STATEMENT (COMPLETE WHAT YOU HAVE WITH SOMETHING ELSE)


-- Any lastname that starts with mi
SELECT *
FROM AdventureWorks2017.PERSON.PERSON
WHERE LastName LIKE 'mi%'

--Any Firstname that starts with Lo
SELECT *
FROM AdventureWorks2017.Person.Person
WHERE FirstName LIKE 'Lo%'

--Anythin in the middle that have essa
SELECT *
FROM AdventureWorks2017.Person.Person
WHERE FirstName LIKE '%essa%'

-- Character limitation with _
SELECT *
FROM AdventureWorks2017.Person.Person
WHERE FirstName LIKE '%r_';
