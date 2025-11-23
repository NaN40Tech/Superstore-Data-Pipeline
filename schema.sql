-- Superstore Database Schema
-- Created for Data Pipeline & Analytics Project

-- Drop table if exists
DROP TABLE IF EXISTS sales;

-- Create sales table
CREATE TABLE sales (
    Row_ID INT PRIMARY KEY,
    Order_ID VARCHAR(50) NOT NULL,
    Order_Date DATE NOT NULL,
    Ship_Date DATE NOT NULL,
    Ship_Mode VARCHAR(50),
    Customer_ID VARCHAR(50) NOT NULL,
    Customer_Name VARCHAR(100),
    Segment VARCHAR(50),
    Country VARCHAR(50),
    City VARCHAR(100),
    State VARCHAR(100),
    Postal_Code VARCHAR(20),
    Region VARCHAR(50),
    Product_ID VARCHAR(50) NOT NULL,
    Category VARCHAR(50),
    Sub_Category VARCHAR(50),
    Product_Name VARCHAR(255),
    Sales DECIMAL(10, 4),
    Quantity INT,
    Discount DECIMAL(5, 2),
    Profit DECIMAL(10, 4),
    INDEX idx_order_date (Order_Date),
    INDEX idx_category (Category),
    INDEX idx_region (Region),
    INDEX idx_customer (Customer_ID)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
