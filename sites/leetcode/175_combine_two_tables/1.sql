# Write your MySQL query statement below
SELECT firstName, lastName, Address.city as city, Address.state as state
FROM Person
LEFT OUTER JOIN Address
ON Person.personId=Address.personId;