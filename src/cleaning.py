from pyspark.sql import SparkSession
from pyspark.sql.functions import to_timestamp, to_date
import os

# Create the staging folder at the project root
os.makedirs("data/staging", exist_ok=True)

# Spark Session
spark = SparkSession.builder.appName("Cleaning").getOrCreate()

# Loading
df = spark.read.csv("data/raw/DataCoSupplyChainDataset.csv", header=True, inferSchema=True)

# Drop columns
drop_cols = [
    'Product Description', 'Order Zipcode', 'Customer Email', 'Customer Password',
    'Product Status', 'Order Customer Id', 'Order Item Cardprod Id', 'Product Category Id',
    'Sales', 'Order Item Total', 'Order Profit Per Order', 'Benefit per order', 'Sales per customer'
]
df = df.drop(*drop_cols)

# Date conversions
df = df.withColumn("order_date_typed", to_date(to_timestamp("order date (DateOrders)", "M/d/yyyy H:mm"))) \
       .withColumn("shipping_date_typed", to_date(to_timestamp("shipping date (DateOrders)", "M/d/yyyy H:mm")))

# Drop rows with nulls
df = df.filter(df["Customer Zipcode"].isNotNull() & df["Customer Lname"].isNotNull())

# Convert to Pandas
df_pandas = df.toPandas()

# Save as Parquet (or CSV if Parquet fails , just to ensure the cleaning was done right)
try:
    df_pandas.to_parquet("data/staging/cleaned.parquet", index=False)
    print("Cleaning completed – Parquet: data/staging/cleaned.parquet")
except Exception as e:
    print(f"Parquet error: {e}")
    df_pandas.to_csv("data/staging/cleaned.csv", index=False)
    print("Cleaning completed – CSV: data/staging/cleaned.csv")