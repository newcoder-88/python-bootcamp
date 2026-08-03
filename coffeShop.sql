
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