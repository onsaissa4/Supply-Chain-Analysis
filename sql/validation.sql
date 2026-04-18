-- VALIDATION SCRIPT
-- Check data integrity after loading


-- 1. Count rows per table (compare with Parquet files)
SELECT 'customer' AS table_name, COUNT(*) AS row_count FROM customer
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
SELECT 'shipment', COUNT(*) FROM shipment
ORDER BY row_count DESC;

-- 2. Check foreign key integrity (orphans)
SELECT 'order_table (customer_id)' AS check_name, COUNT(*) AS orphan_count
FROM order_table o LEFT JOIN customer c ON o.customer_id = c.customer_id
WHERE c.customer_id IS NULL
UNION ALL
SELECT 'order_details (order_id)', COUNT(*)
FROM order_details od LEFT JOIN order_table o ON od.order_id = o.order_id
WHERE o.order_id IS NULL
UNION ALL
SELECT 'order_details (product_card_id)', COUNT(*)
FROM order_details od LEFT JOIN product p ON od.product_card_id = p.product_card_id
WHERE p.product_card_id IS NULL
UNION ALL
SELECT 'product (category_id)', COUNT(*)
FROM product p LEFT JOIN category c ON p.category_id = c.category_id
WHERE c.category_id IS NULL
UNION ALL
SELECT 'category (department_id)', COUNT(*)
FROM category c LEFT JOIN department d ON c.department_id = d.department_id
WHERE d.department_id IS NULL
UNION ALL
SELECT 'shipment (order_id)', COUNT(*)
FROM shipment s LEFT JOIN order_table o ON s.order_id = o.order_id
WHERE o.order_id IS NULL;

-- 3. Check duplicate primary keys (should all be 0)
SELECT 'customer' AS table_name, COUNT(*) - COUNT(DISTINCT customer_id) AS duplicate_pk FROM customer
UNION ALL
SELECT 'department', COUNT(*) - COUNT(DISTINCT department_id) FROM department
UNION ALL
SELECT 'category', COUNT(*) - COUNT(DISTINCT category_id) FROM category
UNION ALL
SELECT 'product', COUNT(*) - COUNT(DISTINCT product_card_id) FROM product
UNION ALL
SELECT 'order_table', COUNT(*) - COUNT(DISTINCT order_id) FROM order_table
UNION ALL
SELECT 'order_details', COUNT(*) - COUNT(DISTINCT order_item_id) FROM order_details
UNION ALL
SELECT 'shipment', COUNT(*) - COUNT(DISTINCT order_id) FROM shipment;

-- 4. Check for nulls in mandatory columns (example for order_table)
SELECT 'order_table (order_id nulls)' AS check_name, COUNT(*) AS null_count
FROM order_table WHERE order_id IS NULL
UNION ALL
SELECT 'order_table (order_date_typed nulls)', COUNT(*)
FROM order_table WHERE order_date_typed IS NULL
UNION ALL
SELECT 'customer (customer_id nulls)', COUNT(*)
FROM customer WHERE customer_id IS NULL;