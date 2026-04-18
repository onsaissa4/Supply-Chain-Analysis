import pandas as pd
import os

# Créer le dossier staging s'il n'existe pas
os.makedirs("data/staging", exist_ok=True)

# Lire le fichier nettoyé (Parquet)
df = pd.read_parquet("data/staging/cleaned.parquet")

# ------------------------------------------------------------
# 1. Table Customer
customer_cols = [
    'Customer Id', 'Customer Fname', 'Customer Lname', 'Customer Segment',
    'Customer City', 'Customer State', 'Customer Country', 'Customer Zipcode',
    'Customer Street', 'Latitude', 'Longitude'
]
customer = df[customer_cols].drop_duplicates(subset=['Customer Id'])
customer.to_parquet("data/staging/customer.parquet", index=False)

# ------------------------------------------------------------
# 2. Table Department
dept_cols = ['Department Id', 'Department Name']
department = df[dept_cols].drop_duplicates(subset=['Department Id'])
department.to_parquet("data/staging/department.parquet", index=False)

# ------------------------------------------------------------
# 3. Table Category
category_cols = ['Category Id', 'Category Name', 'Department Id']
category = df[category_cols].drop_duplicates(subset=['Category Id'])
category.to_parquet("data/staging/category.parquet", index=False)

# ------------------------------------------------------------
# 4. Table Product
product_cols = [
    'Product Card Id', 'Product Name', 'Product Price', 'Product Image', 'Category Id'
]
product = df[product_cols].drop_duplicates(subset=['Product Card Id'])
product.to_parquet("data/staging/product.parquet", index=False)

# ------------------------------------------------------------
# 5. Table Order
order_cols = [
    'Order Id', 'order_date_typed', 'Order Status', 'Market', 'Order Region',
    'Order City', 'Order State', 'Order Country', 'Customer Id'
]
order = df[order_cols].drop_duplicates(subset=['Order Id'])
order.to_parquet("data/staging/order.parquet", index=False)

# ------------------------------------------------------------
# 6. Table Order_Details
details_cols = [
    'Order Item Id', 'Order Id', 'Product Card Id', 'Order Item Quantity',
    'Order Item Discount', 'Order Item Discount Rate', 'Order Item Product Price',
    'Order Item Profit Ratio'
]
order_details = df[details_cols].drop_duplicates(subset=['Order Item Id'])
order_details.to_parquet("data/staging/order_details.parquet", index=False)

# ------------------------------------------------------------
# 7. Table Shipment
shipment_cols = [
    'Order Id', 'Shipping Mode', 'Delivery Status', 'Late_delivery_risk',
    'Days for shipping (real)', 'Days for shipment (scheduled)', 'shipping_date_typed'
]
shipment = df[shipment_cols].drop_duplicates(subset=['Order Id'])
shipment.to_parquet("data/staging/shipment.parquet", index=False)

print(" Split terminé. Tables sauvegardées dans data/staging/")