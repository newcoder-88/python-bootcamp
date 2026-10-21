USE CoffeeShop;

ALTER TABLE Orders
ADD COLUMN Status VARCHAR(20) NOT NULL DEFAULT 'Pending';

DESCRIBE Orders;
SELECT * FROM Orders;

UPDATE Orders
SET Status = 'Completed'
WHERE OrderID = 1;

SELECT OrderID, CustomerID, Status
FROM Orders
WHERE OrderID = 1;

DESCRIBE Customer;


SELECT Customer.Name ,count(Orders.Status) AS completed_orders 
FROM Customer JOIN Orders ON Customer.CustomerID = Orders.CustomerID 
WHERE Orders.Status = 'Completed' 
GROUP BY Customer.Name ORDER BY completed_orders DESC;
