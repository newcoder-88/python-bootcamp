WITH CompletedOrders AS (
    SELECT OrderID, CustomerID, Status
    FROM Orders
    WHERE Status = 'Completed'
)
SELECT *
FROM CompletedOrders ;


DESCRIBE orders;

WITH CompletedOrders AS (
    SELECT Orders.OrderID,  Orders.CustomerID,  Orders.Status
    FROM Orders
    WHERE Status = 'Completed'
)
SELECT CompletedOrders.OrderID, Customer.NAME, CompletedOrders.Status
FROM CompletedOrders
JOIN Customer
ON CompletedOrders.CustomerID = Customer.CustomerID;

WITH OrderCounts AS (
    SELECT CustomerID, COUNT(*) AS TotalOrders
    FROM Orders
    GROUP BY CustomerID
)
SELECT Customer.Name, OrderCounts.TotalOrders
FROM OrderCounts
JOIN Customer
ON OrderCounts.CustomerID = Customer.CustomerID;

WITH CompletedOrders AS (
    SELECT Orders.OrderID
    FROM Orders
    WHERE Status = 'Completed'
),
PendingOrders AS (
    SELECT Orders.OrderID
    FROM Orders
    WHERE Status = 'Pending'
)
SELECT
    (SELECT COUNT(*) FROM CompletedOrders) AS CompletedCount,
    (SELECT COUNT(*) FROM PendingOrders) AS PendingCount;
