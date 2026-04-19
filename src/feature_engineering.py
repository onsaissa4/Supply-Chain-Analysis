from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum as _sum, lag, avg, stddev, dayofweek, month, when
from pyspark.sql.window import Window

spark = SparkSession.builder.appName("FeatureEngineering").getOrCreate()

# Load Parquet files (rename columns to remove spaces)
details = spark.read.parquet("data/staging/order_details.parquet") \
    .withColumnRenamed("Order Item Id", "order_item_id") \
    .withColumnRenamed("Order Id", "order_id") \
    .withColumnRenamed("Product Card Id", "product_card_id") \
    .withColumnRenamed("Order Item Quantity", "quantity") \
    .withColumnRenamed("Order Item Discount", "discount") \
    .withColumnRenamed("Order Item Discount Rate", "discount_rate") \
    .withColumnRenamed("Order Item Product Price", "unit_price") \
    .withColumnRenamed("Order Item Profit Ratio", "profit_ratio")

orders = spark.read.parquet("data/staging/order.parquet") \
    .withColumnRenamed("Order Id", "order_id") \
    .withColumnRenamed("order_date_typed", "order_date") \
    .withColumnRenamed("Order Status", "order_status") \
    .withColumnRenamed("Market", "market") \
    .withColumnRenamed("Order Region", "order_region") \
    .withColumnRenamed("Order City", "order_city") \
    .withColumnRenamed("Order State", "order_state") \
    .withColumnRenamed("Order Country", "order_country") \
    .withColumnRenamed("Customer Id", "customer_id")

product = spark.read.parquet("data/staging/product.parquet") \
    .withColumnRenamed("Product Card Id", "product_card_id") \
    .withColumnRenamed("Product Name", "product_name") \
    .withColumnRenamed("Product Price", "product_price") \
    .withColumnRenamed("Product Image", "product_image") \
    .withColumnRenamed("Category Id", "category_id")

category = spark.read.parquet("data/staging/category.parquet") \
    .withColumnRenamed("Category Id", "category_id") \
    .withColumnRenamed("Category Name", "category_name") \
    .withColumnRenamed("Department Id", "department_id")

# Join to get date per order line
df = details.join(orders, on="order_id", how="inner")

# Aggregate daily demand per product
daily_demand = df.groupBy("product_card_id", "order_date") \
    .agg(_sum("quantity").alias("demand"))

daily_demand = daily_demand.orderBy("product_card_id", "order_date")

# Window per product
window_spec = Window.partitionBy("product_card_id").orderBy("order_date")

# Lags
daily_demand = daily_demand.withColumn("lag_7", lag("demand", 7).over(window_spec))
daily_demand = daily_demand.withColumn("lag_14", lag("demand", 14).over(window_spec))

# Rolling statistics (previous 7 days)
window_7 = window_spec.rowsBetween(-7, -1)
daily_demand = daily_demand.withColumn("rolling_mean_7", avg("demand").over(window_7))
daily_demand = daily_demand.withColumn("rolling_std_7", stddev("demand").over(window_7))

# Calendar features
daily_demand = daily_demand.withColumn("day_of_week", dayofweek(col("order_date")))
daily_demand = daily_demand.withColumn("month", month(col("order_date")))
daily_demand = daily_demand.withColumn("is_weekend", when(col("day_of_week").isin([6,7]), 1).otherwise(0))

# Add product category name (via join with category)
product_with_cat = product.join(category, on="category_id", how="left")
daily_demand = daily_demand.join(product_with_cat, on="product_card_id", how="left")
daily_demand = daily_demand.withColumnRenamed("category_name", "product_category")

# Target: sum of demand over next 7 days
window_forward = window_spec.rowsBetween(1, 7)
daily_demand = daily_demand.withColumn("demand_next_7", _sum("demand").over(window_forward))

# Drop nulls
daily_demand = daily_demand.dropna()

# Convert to Pandas and save (workaround for Hadoop native library issue)
pandas_df = daily_demand.toPandas()
pandas_df.to_parquet("data/staging/features.parquet", index=False)
print("✅ features.parquet generated using pandas")
spark.stop()