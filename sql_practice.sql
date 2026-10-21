
---SQL Practice Exercises

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

UPDATE Orders SET Status ='completed' WHERE OrderID = 1;



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

SELECT OrderItems.OrderItemID , Products.Name , OrderItems.Quantity FROM OrderItems JOIN Products ON OrderItems.ProductID = Products.ProductID; 

SELECT Orders.OrderID , Products.Name , OrderItems.Quantity 
FROM Orders 
JOIN OrderItems ON OrderItems.OrderID = Orders.OrderID  
JOIN Products ON  Products.ProductID = OrderItems.ProductID ; 

SELECT Customer.Name , Orders.OrderID , Products.Name , OrderItems.Quantity 
FROM Customer
JOIN Orders ON Customer.CustomerID = Orders.CustomerID  
JOIN OrderItems ON Orders.OrderID = OrderItems.OrderID  
JOIN Products ON OrderItems.ProductID = Products.ProductID 
WHERE Customer.Name = 'Sarah' AND OrderItems.Quantity > 1 ;


SELECT Products.Name , SUM(OrderItems.Quantity) AS TotalSold FROM Products JOIN OrderItems ON OrderItems.ProductID = Products.ProductID  GROUP BY Products.Name HAVING SUM(OrderItems.Quantity) > 2;
SELECT Products.Name , SUM(OrderItems.Quantity) AS TotalSold FROM Products JOIN OrderItems ON OrderItems.ProductID = Products.ProductID  GROUP BY Products.Name ORDER BY SUM(OrderItems.Quantity) DESC;

SELECT Products.Name , SUM(OrderItems.Quantity) AS TotalSold 
FROM Products 
JOIN OrderItems ON OrderItems.ProductID = Products.ProductID  
GROUP BY Products.Name HAVING SUM(OrderItems.Quantity) > 2 ;


SELECT Products.Name , SUM(Products.price * OrderItems.Quantity) AS TotalRevenue FROM Products JOIN OrderItems ON OrderItems.ProductID = Products.ProductID  GROUP BY Products.Name;
SELECT Products.Name , SUM(Products.price * OrderItems.Quantity) AS TotalRevenue FROM Products JOIN OrderItems ON OrderItems.ProductID = Products.ProductID  GROUP BY Products.Name HAVING SUM(Products.price * OrderItems.Quantity) > 50 ; 
SELECT Products.Name , SUM(Products.price * OrderItems.Quantity) AS TotalRevenue FROM Products JOIN OrderItems ON OrderItems.ProductID = Products.ProductID  GROUP BY Products.Name HAVING SUM(Products.price * OrderItems.Quantity) > 50 ORDER BY SUM(Products.price * OrderItems.Quantity) DESC; 
SELECT Customer.Name , SUM(Products.price * OrderItems.Quantity) AS Total FROM Customer 
JOIN Orders ON Orders.CustomerID = Customer.CustomerID 
JOIN OrderItems ON OrderItems.OrderID = Orders.OrderID
JOIN Products ON Products.ProductID = OrderItems.ProductID
GROUP BY Customer.Name;


SELECT Customer.Name , COUNT(Orders.OrderID) AS totalOrders FROM Customer LEFT JOIN Orders ON Customer.CustomerID = Orders.CustomerID GROUP BY Customer.Name;
SELECT Customer.Name , COUNT(Orders.OrderID) AS totalOrders FROM Customer LEFT JOIN Orders ON Customer.CustomerID = Orders.CustomerID GROUP BY Customer.Name HAVING COUNT(Orders.OrderID) > 1;
SELECT Customer.Name , COUNT(Orders.OrderID) AS totalOrders FROM Customer LEFT JOIN Orders ON Customer.CustomerID = Orders.CustomerID GROUP BY Customer.Name ORDER BY COUNT(Orders.OrderID) DESC;
SELECT Customer.Name , COUNT(Orders.OrderID) AS totalOrders FROM Customer LEFT JOIN Orders ON Customer.CustomerID = Orders.CustomerID GROUP BY Customer.Name HAVING COUNT(Orders.OrderID) > 1 ORDER BY COUNT(Orders.OrderID) DESC;


SELECT Customer.Name , COALESCE(SUM(Products.price * OrderItems.Quantity) , 0) AS  totalPrice FROM customer LEFT JOIN Orders ON customer.CustomerID = Orders.CustomerID LEFT JOIN OrderItems ON Orders.OrderID = OrderItems.OrderID LEFT JOIN Products ON OrderItems.ProductID = Products.ProductID GROUP BY Customer.Name ORDER BY COALESCE(SUM(Products.price * OrderItems.Quantity) , 0) DESC ; 


SELECT Customer.Name ,COUNT(DISTINCT Orders.OrderID) AS totalOrders , COALESCE(SUM(Products.PRICE * OrderItems.Quantity) , 0) AS TotalSpent FROM Customer LEFT JOIN Orders ON  Customer.CustomerID = Orders.CustomerID LEFT JOIN OrderItems ON Orders.OrderID = OrderItems.OrderID LEFT JOIN Products ON OrderItems.ProductID = Products.ProductID GROUP BY Customer.Name ORDER BY TotalSpent DESC LIMIT 1 ;

SELECT Products.Name ,COALESCE(SUM(OrderItems.Quantity), 0) AS totalQuantitySold , COALESCE(SUM(OrderItems.Quantity * Products.price), 0) AS Revenue FROM Products LEFT JOIN  OrderItems ON Products.ProductID = OrderItems.ProductID GROUP BY Products.Name ORDER BY totalQuantitySold DESC;
SELECT Products.Name ,COALESCE(SUM(OrderItems.Quantity), 0) AS totalQuantitySold , COALESCE(SUM(OrderItems.Quantity * Products.price), 0) AS Revenue FROM Products LEFT JOIN  OrderItems ON Products.ProductID = OrderItems.ProductID GROUP BY Products.Name ORDER BY Revenue DESC;

UPDATE Orders SET Status ='Preparing' WHERE OrderID= 3 ;
SELECT COUNT(*) from Orders WHERE Status = 'Completed';
SELECT COALESCE(SUM(OrderItems.Quantity * Products.price), 0) AS Revenue FROM Products LEFT JOIN  OrderItems ON Products.ProductID = OrderItems.ProductID LEFT JOIN Orders ON Orders.OrderID = OrderItems.OrderID WHERE Status = 'Completed';
SELECT Status , count(*) FROM Orders GROUP BY Status;


SELECT COUNT(*) AS totalCustomers FROM Customer;
SELECT COUNT(*) AS totalOrders FROM Orders;
SELECT COALESCE(SUM(OrderItems.Quantity * Products.price),0) FROM Products JOIN OrderItems ON Products.ProductID = OrderItems.ProductID JOIN Orders ON OrderItems.OrderID = Orders.OrderID WHERE Status = 'Completed';
SELECT AVG(ordersTotal) AS averageOrderValue FROM (SELECT SUM(OrderItems.Quantity * Products.price) AS orderTotal FROM  Products JOIN OrderItems ON Products.ProductID = OrderItems.ProductID JOIN Orders ON OrderItems.OrderID = Orders.OrderID WHERE Status = 'Completed' GROUP BY Orders.OrderID) AS completedOrder; 
SELECT Customer.Name , SUM(Products.Price * OrderItems.Quantity)AS totalspent FROM Customer JOIN Orders ON Customer.CustomerID = Orders.CustomerID JOIN OrderItems ON Orders.OrderID= OrderItems.OrderID JOIN Products ON OrderItems.ProductID = Products.ProductID  GROUP BY Customer.Name ORDER BY totalspent DESC limit 1 ;  
SELECT Products.Name , SUM(OrderItems.Quantity) AS QuantitySold FROM Products JOIN OrderItems ON Products.ProductID = OrderItems.ProductID GROUP BY Products.Name ORDER BY QuantitySold DESC LIMIT 1 ;
SELECT Products.Name , SUM(OrderItems.Quantity * Products.Price) AS Revenue FROM Products JOIN OrderItems ON Products.ProductID = OrderItems.ProductID GROUP BY Products.Name ORDER BY Revenue DESC LIMIT 1 ; 
SELECT Status , COUNT(*) FROM Orders GROUP BY Status; 

