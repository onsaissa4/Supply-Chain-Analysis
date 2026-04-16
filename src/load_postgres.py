import pandas as pd
import re
from sqlalchemy import create_engine, text

# PostgreSQL connection settings

DB_USER = "postgres"
DB_PASSWORD = "ons"   
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "supply_chain"

DB_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(DB_URL)


# function to clean column names
# This function converts column names to lowercase, replaces non-alphanumeric characters with underscores, collapses multiple underscores, and strips leading/trailing underscores.
def clean_columns(df):
    df.columns = df.columns.str.lower()
    df.columns = [re.sub(r'[^a-z0-9_]', '_', col) for col in df.columns]
    df.columns = [re.sub(r'_+', '_', col) for col in df.columns]
    df.columns = [col.strip('_') for col in df.columns]
    return df


# Load Parquet files
customer = pd.read_parquet("data/staging/customer.parquet")
department = pd.read_parquet("data/staging/department.parquet")
category = pd.read_parquet("data/staging/category.parquet")
product = pd.read_parquet("data/staging/product.parquet")
order = pd.read_parquet("data/staging/order.parquet")
order_details = pd.read_parquet("data/staging/order_details.parquet")
shipment = pd.read_parquet("data/staging/shipment.parquet")

# Clean column names
customer = clean_columns(customer)
department = clean_columns(department)
category = clean_columns(category)
product = clean_columns(product)
order = clean_columns(order)
order_details = clean_columns(order_details)
shipment = clean_columns(shipment)

# Truncate all tables before loading new data 

with engine.connect() as conn:
    print("Truncating existing tables...")
    conn.execute(text("TRUNCATE TABLE customer CASCADE"))
    conn.execute(text("TRUNCATE TABLE department CASCADE"))
    conn.execute(text("TRUNCATE TABLE category CASCADE"))
    conn.execute(text("TRUNCATE TABLE product CASCADE"))
    conn.execute(text("TRUNCATE TABLE order_table CASCADE"))
    conn.execute(text("TRUNCATE TABLE order_details CASCADE"))
    conn.execute(text("TRUNCATE TABLE shipment CASCADE"))
    conn.commit()
    print("Tables truncated.")


# Load data in correct order (append mode)
print("Loading customer...")
customer.to_sql("customer", engine, if_exists="append", index=False)

print("Loading department...")
department.to_sql("department", engine, if_exists="append", index=False)

print("Loading category...")
category.to_sql("category", engine, if_exists="append", index=False)

print("Loading product...")
product.to_sql("product", engine, if_exists="append", index=False)

print("Loading order_table...")
order.to_sql("order_table", engine, if_exists="append", index=False)

print("Loading order_details...")
order_details.to_sql("order_details", engine, if_exists="append", index=False)

print("Loading shipment...")
shipment.to_sql("shipment", engine, if_exists="append", index=False)

print(" All tables loaded successfully")