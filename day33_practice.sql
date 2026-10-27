SELECT
    o.OrderID,
    o.CustomerID
FROM Orders o
LEFT JOIN Customer c
    ON o.CustomerID = c.CustomerID
WHERE c.CustomerID IS NULL;

SELECT *
FROM Orders
WHERE CustomerID IS NULL;



SELECT *
FROM Customer;

SELECT
    Email,
    COUNT(*) AS EmailCount
FROM Customer
GROUP BY Email
HAVING COUNT(*) > 1;


SELECT OrderID, Status
FROM Orders
WHERE Status NOT IN ('Pending', 'Completed', 'Cancelled');

SELECT OrderID, Status
FROM Orders;





START TRANSACTION;

UPDATE Orders
SET Status = 'Pending'
WHERE OrderID = 1;

SELECT OrderID, Status
FROM Orders
WHERE OrderID = 1;

ROLLBACK;

SELECT OrderID, Status
FROM Orders
WHERE OrderID = 1;

UPDATE Orders
SET Status = 'Banana'
WHERE OrderID = 1;


SELECT OrderID , Status 
FROM Orders
where Status = 'Completed'
ORDER BY OrderID desc;

SELECT CustomerID , COUNT(OrderID) AS orderCount
FROM Orders
GROUP BY CustomerID
HAVING COUNT(OrderID) > 2 ;

