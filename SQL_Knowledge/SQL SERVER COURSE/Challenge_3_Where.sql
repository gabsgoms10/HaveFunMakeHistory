		
-- Challenge 1: Production team asked for produtcts that the weight is higher than 500kg but less than 700kg
SELECT * FROM AdventureWorks2017.Production.Product
WHERE Weight > 500 and Weight<700


-- Challenge 2: Marketing department asked a list of married and salaried employees
SELECT TOP(10) * FROM AdventureWorks2017.HumanResources.Employee
WHERE MaritalStatus = 'M' and SalariedFlag = 1


-- Challenge 3: We need to send a payment remember to Peter Krebs, find his email.
DECLARE @EntityIDPeter int = (SELECT BusinessEntityID 
											FROM AdventureWorks2017.Person.Person
											WHERE FirstName = 'Peter' and LastName='Krebs')

SELECT EmailAddress as PeterKrebs_Email FROM AdventureWorks2017.Person.EmailAddress WHERE BusinessEntityID = @EntityIDPeter;

/* 
Operator/Description
=   EQUAL
>   HIGHER
<   LESS
>=  HIGHER OR EQUAL TO
<=  LESS OR EQUAL TO
<>  DIFFERENT
AND LOGICAL OPERATOR, BOTH ARGUMENTS MUST BE TRUE FOR A TRUE
OR  LOGICAL OPERATOR, ONE ARGUMENT MUST BE TRUE FOR A TRUE
*/