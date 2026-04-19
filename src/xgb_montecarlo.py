import pandas as pd
import numpy as np
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error
import joblib
from sqlalchemy import create_engine

# PostgreSQL connection (change password!)
DB_USER = "postgres"
DB_PASSWORD = "123456"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "supply_chain"
engine = create_engine(f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

# Load features
df = pd.read_parquet("data/staging/features.parquet")
print(f"Loaded {len(df)} rows")

# Prepare features and target
feature_cols = ["lag_7", "lag_14", "rolling_mean_7", "rolling_std_7",
                "day_of_week", "month", "is_weekend", "product_category"]
X = df[feature_cols].copy()
y = df["demand_next_7"]

# One-hot encode product_category
X = pd.get_dummies(X, columns=["product_category"])

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train XGBoost
model = xgb.XGBRegressor(n_estimators=100, learning_rate=0.1, max_depth=5, random_state=42)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print(f"MAE: {mae:.2f}, RMSE: {rmse:.2f}")

# Save model
joblib.dump(model, "models/xgboost_demand_model.pkl")
print("Model saved to models/xgboost_demand_model.pkl")

# Monte Carlo simulation
errors = y_test - y_pred
error_mean = errors.mean()
error_std = errors.std()
print(f"Forecast error distribution: mean={error_mean:.2f}, std={error_std:.2f}")

# Forecast for all rows
forecast = model.predict(X)

# Stockout probability (example inventory = 50)
inventory_level = 50
n_simulations = 10000
stockout_probs = []
for f in forecast:
    simulated = np.random.normal(f + error_mean, error_std, size=n_simulations)
    prob = (simulated > inventory_level).mean()
    stockout_probs.append(prob)

# Build forecast table
forecast_df = pd.DataFrame()
cat_cols = [c for c in X.columns if c.startswith("product_category_")]
forecast_df['product_category'] = X[cat_cols].idxmax(axis=1).str.replace("product_category_", "")
forecast_df['forecast_demand'] = forecast
forecast_df['stockout_probability'] = stockout_probs
forecast_df['forecast_week_start'] = pd.Timestamp.today().normalize() + pd.DateOffset(days=7)


# Calculate average demand and relative error to test the model's performance
mean_demand = y.mean()
mae_percent = (mae / mean_demand) * 100

print(f"Average actual demand (next 7 days): {mean_demand:.2f}")
print(f"MAE percentage: {mae_percent:.2f}%")
if mae_percent < 30:
    print(" Relative error < 30% → model acceptable for demonstration.")
else:
    print(" Relative error > 30% → model needs improvement.")

# Save to PostgreSQL
forecast_df.to_sql("demand_forecast", engine, if_exists="replace", index=False)
print("demand_forecast table created in PostgreSQL")