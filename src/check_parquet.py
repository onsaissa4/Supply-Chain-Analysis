import pandas as pd
df = pd.read_parquet("data/staging/category.parquet")
print(df.columns.tolist())