
CREATE DATABASE CoffeeShop;

USE CoffeeShop;

CREATE TABLE Products (
    ProductID INT PRIMARY KEY,
    Name VARCHAR(100),
    Price DECIMAL(10,2)
);

CREATE TABLE Members ( 
    MemberID INT PRIMARY KEY ,
    Name VARCHAR(50) ,
    Email VARCHAR(50) ,
    JoinDate DATE) ;

INSERT INTO Members (MemberID, Name, Email, JoinDate DATE)
VALUES (1, 'Sarah', 'sarah@example.com', '2026-08-03');
INSERT INTO Members (MemberID, Name, Email, JoinDate)
VALUES (2, 'Ahmed', 'ahmed@example.com', '2026-08-02');


INSERT INTO Products (ProductID, Name, Price)
VALUES(1, 'MATCHA' , 25);
INSERT INTO Products (ProductID, Name, Price)
VALUES(2, 'LATTE' , 15);
INSERT INTO Products (ProductID, Name, Price)
VALUES(3, 'ORANGE JUICE' , 30);
SELECT * FROM Products;
SELECT Name FROM Products;
SELECT * FROM Products WHERE ProductID = 2 ;

SELECT * FROM Products where Price = 25 ; 
SELECT Name , Price FROM Products ;
SELECT * FROM Products ORDER BY price DESC; 


UPDATE  Products 
SET Price = 18 
WHERE Name = 'LATTE' ;
DELETE FROM Products 
WHERE Name = 'ORANGE JUICE';

SELECT COUNT(*) FROM Products ; 
SELECT SUM(Price) FROM Products ; 
SELECT AVG(Price) FROM Products ; 
SELECT MIN(Price) FROM Products ; 
SELECT MAX(Price) FROM Products ;




SELECT * FROM Products WHERE Price>15 AND Price<30;
SELECT * FROM Products where Name = 'MATCHA' OR Name = 'LATTE';
SELECT * FROM Products where Price IN (15,25,30);



SELECT * FROM Products WHERE Name LIKE '%a%';
SELECT * FROM Products WHERE Name LIKE 'M%' ; 
SELECT * FROM Products WHERE Name LIKE '%e' ; 



SELECT * FROM Products WHERE Price BETWEEN 15 AND 30 ; 
SELECT * FROM Products WHERE Price BETWEEN 10 AND 25 ; 



SELECT * FROM Products WHERE Price BETWEEN 10 AND 30 AND Name LIKE '%a%' ; 


SELECT Price , count(*) FROM Products GROUP BY Price;
SELECT Price , AVG(Price) FROM Products GROUP BY Price; 
SELECT Price , SUM(Price) FROM Products GROUP BY Price ;


SELECT Price , COUNT(*) FROM Products GROUP BY Price HAVING COUNT(*) > 1;
SELECT Price , AVG(Price) FROM Products GROUP BY Price HAVING AVG(Price) > 20;
SELECT Price , AVG(Price) FROM Products GROUP BY Price HAVING AVG(Price) > 20;

SELECT Price , SUM(Price) FROM Products WHERE Price>10 GROUP BY Price HAVING SUM(Price) > 30;
