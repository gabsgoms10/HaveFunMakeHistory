--InnerJoin

SELECT TOP(10) * 
FROM AdventureWorks2017.Person.Person

SELECT TOP(10) * 
FROM AdventureWorks2017.Person.EmailAddress

SELECT p.FirstName, P.LastName, EA.EmailAddress, EA.EmailAddressID
FROM AdventureWorks2017.Person.Person P
INNER JOIN AdventureWorks2017.Person.EmailAddress EA
ON P.BusinessEntityID = EA.BusinessEntityID


;
