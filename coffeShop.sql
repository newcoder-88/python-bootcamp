
--CREATE DATABASE CoffeeShop;

--USE CoffeeShop;

--SELECT DATABASE();
CREATE TABLE Products (
    ProductID INT PRIMARY KEY,
    Name VARCHAR(100),
    Price DECIMAL(10,2));
INSERT INTO Products (ProductID, Name, Price)
VALUES(1, 'MATCHA' , 25);
INSERT INTO Products (ProductID, Name, Price)
VALUES(2, 'LATTE' , 15);
INSERT INTO Products (ProductID, Name, Price)
VALUES(3, 'ORANGE JUICE' , 30);

SELECT * FROM Members;
CREATE TABLE Members ( 
    MemberID INT PRIMARY KEY ,
    Name VARCHAR(50) ,
    Email VARCHAR(50) ,
    JoinDate DATE);
INSERT INTO Members (MemberID, Name, Email, JoinDate )
VALUES (1, 'Sarah', 'sarah@example.com', '2026-08-03');
INSERT INTO Members (MemberID, Name, Email, JoinDate)
VALUES (2, 'Ahmed', 'ahmed@example.com', '2026-08-02');


CREATE TABLE Customer(
    CustomerID INT PRIMARY KEY , 
    Name VARCHAR(100),
    Email VARCHAR(100)
);
INSERT INTO Customer (CustomerID , Name , Email)
VALUES(1 , 'Sarah' , 'sarah@example.com');

CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    CustomerID INT ,
    OrderDate DATE ,
    FOREIGN KEY(CustomerID) REFERENCES Customer(CustomerID) 
);
INSERT INTO Orders (OrderID , CustomerID , OrderDate)
VALUES(1 , 1 , '2026-08-19');

CREATE TABLE OrderItems (
    OrderItemID INT PRIMARY KEY,
    OrderID INT,
    ProductID INT,
    quantity INT,
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID), 
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);
 INSERT INTO OrderItems ( OrderItemID , OrderID , ProductID , quantity) 
 VALUES ( 1 , 1 , 1 , 2 );

--SHOW TABLES;


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
SELECT Price , SUM(Price) FROM Products WHERE Price>10 GROUP BY Price HAVING SUM(Price) > 30;

SELECT Price , AVG(Price) FROM Products GROUP BY Price HAVING AVG(Price)>20;
SELECT Name , AVG(Price) FROM Products WHERE Price > 10 GROUP BY Name HAVING AVG(Price) > 20 ;

SELECT Price , COUNT(*) FROM Products GROUP BY Price HAVING COUNT(*) > 1 ORDER BY COUNT(*) DESC ;
SELECT Price , SUM(Price) FROM Products GROUP BY Price HAVING SUM(Price) > 30 ORDER BY SUM(price) DESC;

SELECT DISTINCT Price FROM Products WHERE Price > 10 ORDER BY Price DESC;
SELECT  Price , COUNT(Price) FROM Products WHERE Price > 10 GROUP BY Price HAVING COUNT(Price) > 1 ORDER BY Price DESC;

SELECT OrderItems.OrderItemID , Products.Name , OrderItems.quantity FROM OrderItems JOIN Products ON OrderItems.ProductID = Products.ProductID; 

SELECT Orders.OrderID , Products.Name , OrderItems.quantity 
FROM Orders 
JOIN OrderItems ON OrderItems.OrderID = Orders.OrderID  
JOIN Products ON  Products.ProductID = OrderItems.ProductID ; 

SELECT Customer.Name , Orders.OrderID , Products.Name , OrderItems.quantity 
FROM Customer
JOIN Orders ON Customer.CustomerID = Orders.CustomerID  
JOIN OrderItems ON Orders.OrderID = OrderItems.OrderID  
JOIN Products ON OrderItems.ProductID = Products.ProductID 
WHERE Customer.Name = 'Sarah' AND OrderItems.quantity > 1 ;


SELECT Products.Name , SUM(OrderItems.quantity) AS TotalSold FROM Products JOIN OrderItems ON OrderItems.ProductID = Products.ProductID  GROUP BY Products.Name HAVING SUM(OrderItems.quantity) > 2;
SELECT Products.Name , SUM(OrderItems.quantity) AS TotalSold FROM Products JOIN OrderItems ON OrderItems.ProductID = Products.ProductID  GROUP BY Products.Name ORDER BY SUM(OrderItems.quantity) DESC;

SELECT Products.Name , SUM(OrderItems.quantity) AS TotalSold 
FROM Products 
JOIN OrderItems ON OrderItems.ProductID = Products.ProductID  
GROUP BY Products.Name HAVING SUM(OrderItems.quantity) > 2 ;


SELECT Products.Name , SUM(Products.price * OrderItems.quantity) AS TotalRevenue FROM Products JOIN OrderItems ON OrderItems.ProductID = Products.ProductID  GROUP BY Products.Name;
SELECT Products.Name , SUM(Products.price * OrderItems.quantity) AS TotalRevenue FROM Products JOIN OrderItems ON OrderItems.ProductID = Products.ProductID  GROUP BY Products.Name HAVING SUM(Products.price * OrderItems.quantity) > 50 ; 
SELECT Products.Name , SUM(Products.price * OrderItems.quantity) AS TotalRevenue FROM Products JOIN OrderItems ON OrderItems.ProductID = Products.ProductID  GROUP BY Products.Name HAVING SUM(Products.price * OrderItems.quantity) > 50 ORDER BY SUM(Products.price * OrderItems.quantity) DESC; 
SELECT Customer.Name , SUM(Products.price * OrderItems.quantity) AS Total FROM Customer 
JOIN Orders ON Orders.CustomerID = Customer.CustomerID 
JOIN OrderItems ON OrderItems.OrderID = Orders.OrderID
JOIN Products ON Products.ProductID = OrderItems.ProductID
GROUP BY Customer.Name;


SELECT Customer.Name , COUNT(Orders.OrderID) AS totalOrders FROM Customer LEFT JOIN Orders ON Customer.CustomerID = Orders.CustomerID GROUP BY Customer.Name;
SELECT Customer.Name , COUNT(Orders.OrderID) AS totalOrders FROM Customer LEFT JOIN Orders ON Customer.CustomerID = Orders.CustomerID GROUP BY Customer.Name HAVING COUNT(Orders.OrderID) > 1;
SELECT Customer.Name , COUNT(Orders.OrderID) AS totalOrders FROM Customer LEFT JOIN Orders ON Customer.CustomerID = Orders.CustomerID GROUP BY Customer.Name ORDER BY COUNT(Orders.OrderID) DESC;
SELECT Customer.Name , COUNT(Orders.OrderID) AS totalOrders FROM Customer LEFT JOIN Orders ON Customer.CustomerID = Orders.CustomerID GROUP BY Customer.Name HAVING COUNT(Orders.OrderID) > 1 ORDER BY COUNT(Orders.OrderID) DESC;


SELECT Customer.Name , COALESCE(SUM(Products.price * OrderItems.quantity) , 0) AS  totalPrice FROM customer LEFT JOIN Orders ON customer.CustomerID = Orders.CustomerID LEFT JOIN OrderItems ON Orders.OrderID = OrderItems.OrderID LEFT JOIN Products ON OrderItems.ProductID = Products.ProductID GROUP BY Customer.Name ORDER BY COALESCE(SUM(Products.price * OrderItems.quantity) , 0) DESC ; 


SELECT Customer.Name ,COUNT(DISTINCT Orders.OrderID) AS totalOrders , COALESCE(SUM(Products.PRICE * OrderItems.quantity) , 0) AS TotalSpent FROM Customer LEFT JOIN Orders on  Customer.CustomerID = Orders.CustomerID LEFT JOIN OrderItems ON Orders.OrderID = OrderItems.OrderID LEFT JOIN Products ON OrderItems.ProductID = Products.ProductID GROUP BY Customer.Name ORDER BY TotalSpent DESC LIMIT 1 ;