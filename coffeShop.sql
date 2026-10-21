
CREATE DATABASE IF NOT EXISTS CoffeeShop;
USE CoffeeShop;


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
    Status VARCHAR(20) NOT NULL DEFAULT 'Pending',
    FOREIGN KEY(CustomerID) REFERENCES Customer(CustomerID) 
);
INSERT INTO Orders (OrderID , CustomerID , OrderDate)
VALUES(1 , 1 , '2026-08-19');


CREATE TABLE OrderItems (
    OrderItemID INT PRIMARY KEY,
    OrderID INT,
    ProductID INT,
    Quantity INT,
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID), 
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);
 INSERT INTO OrderItems ( OrderItemID , OrderID , ProductID , quantity) 
 VALUES ( 1 , 1 , 1 , 2 );

