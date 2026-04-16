from pyspark.sql import SparkSession
from pyspark.sql.functions import to_timestamp, to_date
import os

# Créer le dossier staging à la racine du projet
os.makedirs("data/staging", exist_ok=True)

# Session Spark
spark = SparkSession.builder.appName("Cleaning").getOrCreate()

# Chargement
df = spark.read.csv("data/raw/DataCoSupplyChainDataset.csv", header=True, inferSchema=True)

# Suppression des colonnes
drop_cols = [
    'Product Description', 'Order Zipcode', 'Customer Email', 'Customer Password',
    'Product Status', 'Order Customer Id', 'Order Item Cardprod Id', 'Product Category Id',
    'Sales', 'Order Item Total', 'Order Profit Per Order', 'Benefit per order', 'Sales per customer'
]
df = df.drop(*drop_cols)

# Conversion des dates
df = df.withColumn("order_date_typed", to_date(to_timestamp("order date (DateOrders)", "M/d/yyyy H:mm"))) \
       .withColumn("shipping_date_typed", to_date(to_timestamp("shipping date (DateOrders)", "M/d/yyyy H:mm")))

# Suppression des lignes avec nulls
df = df.filter(df["Customer Zipcode"].isNotNull() & df["Customer Lname"].isNotNull())

# Conversion en Pandas
df_pandas = df.toPandas()

# Sauvegarde en Parquet (chemin correct)
try:
    df_pandas.to_parquet("data/staging/cleaned.parquet", index=False)
    print(" Nettoyage terminé – Parquet : data/staging/cleaned.parquet")
except Exception as e:
    print(f" Erreur Parquet : {e}")
    df_pandas.to_csv("data/staging/cleaned.csv", index=False)
    print(" Nettoyage terminé – CSV : data/staging/cleaned.csv")