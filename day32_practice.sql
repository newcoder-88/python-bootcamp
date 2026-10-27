USE CoffeeShop;
SHOW CREATE TABLE Orders;

SELECT Status, COUNT(*) AS total_orders
FROM Orders
GROUP BY Status;

ALTER TABLE Orders
ADD CONSTRAINT chk_order_status
CHECK (Status IN ('Pending', 'Completed', 'Cancelled'));

START TRANSACTION;
UPDATE Orders
SET Status = 'Banana'
WHERE OrderID = 1;
ROLLBACK;

SELECT OrderID, Status
FROM Orders
WHERE OrderID = 1;


SHOW CREATE TABLE Customer;
SELECT
    Email,
    COUNT(*) AS total
FROM Customer
WHERE Email IS NOT NULL
GROUP BY Email
HAVING COUNT(*) > 1;

ALTER TABLE Customer
ADD CONSTRAINT uq_customer_email UNIQUE (Email);

SELECT CustomerID, Name, Email
FROM Customer
WHERE Email IS NOT NULL;

START TRANSACTION;
INSERT INTO Customer (CustomerID, Name, Email)
VALUES (999, 'Test Customer', 'sarah@example.com');
ROLLBACK;

SELECT CustomerID, Name, Email
FROM Customer
WHERE Email IS NULL;
ALTER TABLE Customer
MODIFY COLUMN Email VARCHAR(100) NOT NULL;


START TRANSACTION;
INSERT INTO Orders (OrderID, CustomerID, OrderDate)
VALUES (999, 500, '2026-10-22');
ROLLBACK;

START TRANSACTION;
INSERT INTO Orders (OrderID, CustomerID, OrderDate)
VALUES (999, NULL, '2026-10-22');
SELECT OrderID, CustomerID, OrderDate, Status
FROM Orders
WHERE OrderID = 999;
ROLLBACk;

START TRANSACTION;
INSERT INTO Orders (OrderID, CustomerID, OrderDate)
VALUES (999, NULL, '2026-10-22');

SELECT OrderID, CustomerID, OrderDate, Status
FROM Orders
WHERE OrderID = 999;
ROLLBACK;

SELECT *
FROM Orders
WHERE OrderID = 999;