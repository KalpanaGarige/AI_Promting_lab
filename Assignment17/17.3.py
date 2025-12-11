"""
Write a Python script to clean and preprocess IoT temperature and humidity logs.
Use the following requirements:
1. Handle missing values using **forward fill**.
2. Remove sensor drift using a **rolling mean** (window=3).
3. Normalize temperature and humidity using **StandardScaler**.
4. Encode categorical sensor IDs using **LabelEncoder**.
5. Load data from iot_sensor.csv and output the cleaned dataset.
Also print the first 10 cleaned records.
"""

import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder

# Load dataset (use your uploaded file)
df = pd.read_csv("iot_sensor.csv")

print("\n📌 Original Data:")
print(df.head())

# 1. HANDLE MISSING VALUES – forward fill
df = df.ffill()

# 2. REMOVE SENSOR DRIFT – rolling mean
# (smooth sudden jumps)
df["temperature_smooth"] = df["temperature"].rolling(window=3, min_periods=1).mean()
df["humidity_smooth"] = df["humidity"].rolling(window=3, min_periods=1).mean()

# 3. NORMALIZE VALUES (Standard Scaling)

scaler = StandardScaler()
df[["temp_scaled", "humidity_scaled"]] = scaler.fit_transform(
    df[["temperature_smooth", "humidity_smooth"]]
)

# 4. ENCODE SENSOR ID (categorical → numeric)
encoder = LabelEncoder()
df["sensor_encoded"] = encoder.fit_transform(df["sensor_id"])


# FINAL CLEANED DATA
print("\n✅ CLEANED IoT SENSOR DATA:")
print(df.head(10))

# Save cleaned version
df.to_csv("iot_sensor_cleaned.csv", index=False)
print("\n💾 Saved cleaned file as: iot_sensor_cleaned.csv")
