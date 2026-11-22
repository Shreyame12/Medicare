
import pandas as pd

# Load cleaned historical data
df = pd.read_csv("cleaned_medication_data.csv")

# Convert date column
df["scheduled_datetime"] = pd.to_datetime(
    df["scheduled_datetime"],
    errors="coerce"
)

# Remove invalid records
df = df.dropna(subset=["scheduled_datetime", "status"])

# Keep only verified outcomes
df = df[df["status"].isin(["taken", "missed"])].copy()

# Extract features
df["day_number"] = df["scheduled_datetime"].dt.day_of_week

df["is_weekend"] = (
    df["day_number"] >= 5
).astype(int)

df["scheduled_hour"] = (
    df["scheduled_datetime"].dt.hour
)

# Create target variable
df["missed_target"] = (
    df["status"] == "missed"
).astype(int)

# Calculate previous missed doses
df = df.sort_values(
    ["patient_id", "medicine_name", "scheduled_datetime"]
)

df["previous_missed_doses"] = (
    df.groupby(["patient_id", "medicine_name"])
    ["missed_target"]
    .transform(lambda x: x.shift(1).rolling(7, min_periods=1).sum())
    .fillna(0)
)

# Export prediction dataset
df.to_csv("prediction_dataset.csv", index=False)

print("Prediction dataset created!")
print(df.head())
print("Total records:", len(df))
