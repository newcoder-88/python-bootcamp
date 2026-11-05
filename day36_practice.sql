SELECT OrderID, CustomerID , Status,
ROW_NUMBER() OVER (ORDER BY OrderID ASC) AS OrderNumber
FROM Orders;

WITH SampleOrders AS (
    SELECT 1 AS OrderID, 100 AS Total
    UNION ALL
    SELECT 2, 80
    UNION ALL
    SELECT 3, 80
    UNION ALL
    SELECT 4, 50
)
SELECT OrderID , Total,
RANK() OVER (ORDER BY Total DESC) AS OrderRank,
DENSE_RANK() OVER (ORDER BY Total DESC) AS DenseRank
FROM SampleOrders;


WITH SampleOrders AS (
    SELECT 1 AS OrderID, 1 AS CustomerID, 100 AS Total
    UNION ALL
    SELECT 2, 1, 80
    UNION ALL
    SELECT 3, 1, 80
    UNION ALL
    SELECT 4, 2, 120
    UNION ALL
    SELECT 5, 2, 90
)
SELECT OrderID, CustomerID, Total,
DENSE_RANK() OVER (PARTITION BY CustomerID ORDER BY Total DESC) AS DenseRank
FROM SampleOrders;
