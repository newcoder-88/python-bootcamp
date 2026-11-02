SELECT Name, CustomerID
FROM Customer 
WHERE CustomerID NOT IN(
    SELECT CustomerID
    FROM Orders
);


SELECT OrderID, OrderDate
FROM Orders
WHERE OrderDate > (
    select MIN(OrderDate)
    FROM Orders
);


SELECT OrderID, OrderDate
FROM Orders
WHERE OrderDate < (
    select MAX(OrderDate)
    FROM Orders
);


SELECT CustomerID , Name
FROM Customer AS c 
where EXISTS(
    SELECT 1
    FROM Orders AS o 
    WHERE o.CustomerID = c.CustomerID
); 

SELECT DISTINCT Customer.CustomerID , Customer.Name
FROM Customer
INNER JOIN Orders
ON Customer.CustomerID = orders.CustomerID;

SELECT DISTINCT Customer.CustomerID , Customer.Name
FROM Customer
LEFT JOIN Orders
ON Customer.CustomerID =orders.CustomerID 
WHERE Orders.OrderID IS NULL;


SELECT CustomerID, Name
FROM Customer;
SELECT OrderID, CustomerID
FROM Orders;

show tables ;
describe Orders;
