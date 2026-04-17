-- INDEXES SCRIPT
-- Add indexes for performance optimization

-- Indexes on foreign keys (for faster joins)
CREATE INDEX IF NOT EXISTS idx_order_customer ON order_table(customer_id);
CREATE INDEX IF NOT EXISTS idx_order_details_order ON order_details(order_id);
CREATE INDEX IF NOT EXISTS idx_order_details_product ON order_details(product_card_id);
CREATE INDEX IF NOT EXISTS idx_shipment_order ON shipment(order_id);
CREATE INDEX IF NOT EXISTS idx_product_category ON product(category_id);
CREATE INDEX IF NOT EXISTS idx_category_department ON category(department_id);

-- Indexes on frequently searched columns
CREATE INDEX IF NOT EXISTS idx_order_date ON order_table(order_date_typed);
CREATE INDEX IF NOT EXISTS idx_shipment_date ON shipment(shipping_date_typed);
CREATE INDEX IF NOT EXISTS idx_order_status ON order_table(order_status);

-- Composite index for common join + filter pattern
CREATE INDEX IF NOT EXISTS idx_order_customer_date ON order_table(customer_id, order_date_typed);