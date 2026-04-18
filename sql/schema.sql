TRUNCATE TABLE shipment, order_details, order_table, product, category, department, customer CASCADE;
-- customer table
CREATE TABLE IF NOT EXISTS customer (
    Customer_Id INT PRIMARY KEY,
    Customer_Fname VARCHAR(50),
    Customer_Lname VARCHAR(50),
    Customer_Segment VARCHAR(50),
    Customer_City VARCHAR(100),
    Customer_State VARCHAR(50),
    Customer_Country VARCHAR(50),
    Customer_Zipcode VARCHAR(20),
    Customer_Street VARCHAR(255),
    Latitude DECIMAL(10,6),
    Longitude DECIMAL(10,6)
);

-- department table
CREATE TABLE IF NOT EXISTS department (
    Department_Id INT PRIMARY KEY,
    Department_Name VARCHAR(100)
);

-- category table
CREATE TABLE IF NOT EXISTS category (
    Category_Id INT PRIMARY KEY,
    Category_Name VARCHAR(100),
    Department_Id INT REFERENCES department(Department_Id)
);

-- product table
CREATE TABLE IF NOT EXISTS product (
    Product_Card_Id INT PRIMARY KEY,
    Product_Name VARCHAR(255),
    Product_Price DECIMAL(10,2),
    Product_Image TEXT,
    Category_Id INT REFERENCES category(Category_Id)
);

-- order table (renamed because ORDER is a reserved keyword)
CREATE TABLE IF NOT EXISTS order_table (
    Order_Id INT PRIMARY KEY,
    order_date_typed DATE,
    Order_Status VARCHAR(50),
    Market VARCHAR(50),
    Order_Region VARCHAR(50),
    Order_City VARCHAR(100),
    Order_State VARCHAR(50),
    Order_Country VARCHAR(50),
    Customer_Id INT REFERENCES customer(Customer_Id)
);

-- order_details table
CREATE TABLE IF NOT EXISTS order_details (
    Order_Item_Id INT PRIMARY KEY,
    Order_Id INT REFERENCES order_table(Order_Id),
    Product_Card_Id INT REFERENCES product(Product_Card_Id),
    Order_Item_Quantity INT,
    Order_Item_Discount DECIMAL(10,2),
    Order_Item_Discount_Rate DECIMAL(5,4),
    Order_Item_Product_Price DECIMAL(10,2),
    Order_Item_Profit_Ratio DECIMAL(5,4)
);

-- shipment table
CREATE TABLE IF NOT EXISTS shipment (
    Order_Id INT PRIMARY KEY REFERENCES order_table(Order_Id),
    Shipping_Mode VARCHAR(50),
    Delivery_Status VARCHAR(50),
    Late_delivery_risk INT,
    Days_for_shipping_real INT,
    Days_for_shipment_scheduled INT,
    shipping_date_typed DATE
);

SELECT column_name, data_type 
FROM information_schema.columns 
WHERE table_name = 'customer';
SELECT column_name 
FROM information_schema.columns 
WHERE table_name = 'shipment';


SELECT 'customer' AS table_name, COUNT(*) FROM customer
UNION ALL
SELECT 'department', COUNT(*) FROM department
UNION ALL
SELECT 'category', COUNT(*) FROM category
UNION ALL
SELECT 'product', COUNT(*) FROM product
UNION ALL
SELECT 'order_table', COUNT(*) FROM order_table
UNION ALL
SELECT 'order_details', COUNT(*) FROM order_details
UNION ALL
SELECT 'shipment', COUNT(*) FROM shipment;

-- 1. Customer sample
SELECT * FROM customer LIMIT 100;

-- 2. Department sample
SELECT * FROM department LIMIT 100;

-- 3. Category sample
SELECT * FROM category LIMIT 100;

-- 4. Product sample
SELECT * FROM product LIMIT 100;

-- 5. Order (order_table) sample
SELECT * FROM order_table LIMIT 100;

-- 6. Order details sample
SELECT * FROM order_details LIMIT 100;

-- 7. Shipment sample
SELECT * FROM shipment LIMIT 100;