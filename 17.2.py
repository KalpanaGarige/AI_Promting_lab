"""
Write Python code to preprocess a financial dataset (financial_data.csv) with the following steps:
1. Handle missing values in closing_price and volume.
2. Create lag features: 1-day return and 7-day return.
3. Normalize volume using log-scaling.
4. Detect and remove outliers in closing_price using the IQR method.
5. Output the cleaned dataset.
"""

import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("financial_data.csv")   # your file name

print("✅ Original Data Loaded")
print(df.head())

# 1️⃣ HANDLE MISSING VALUES (closing_price, volume)
df["closing_price"] = df["closing_price"].fillna(df["closing_price"].median())
df["volume"] = df["volume"].fillna(df["volume"].median())

# 2️⃣ CREATE LAG FEATURES (1-day return, 7-day return)

df = df.sort_values("date")  # ensure sorted by date

df["return_1d"] = df["closing_price"].pct_change(1)
df["return_7d"] = df["closing_price"].pct_change(7)

# Replace NA returns at start with 0
df["return_1d"] = df["return_1d"].fillna(0)
df["return_7d"] = df["return_7d"].fillna(0)

# 3️⃣ NORMALIZE VOLUME (Log Scaling)

df["volume_log"] = np.log1p(df["volume"])  # log(1+volume)

# 4️⃣ OUTLIER DETECTION (closing_price) using IQR

Q1 = df["closing_price"].quantile(0.25)
Q3 = df["closing_price"].quantile(0.75)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

df_clean = df[(df["closing_price"] >= lower) & (df["closing_price"] <= upper)]

print("🔍 Outliers removed:", len(df) - len(df_clean))

# 5️⃣ OUTPUT CLEANED DATASET

df_clean.to_csv("financial_data_cleaned.csv", index=False)

print("\n🎉 Preprocessing Completed!")
print("📁 Cleaned file saved as: financial_data_cleaned.csv")
print("\n🔎 Preview:")
print(df_clean.head())
