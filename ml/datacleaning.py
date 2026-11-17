import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).parent
df = pd.read_csv(BASE_DIR / "dataset.csv")

print("Original Dataset:")
print(df.head())

# Display dataset information
print("\nMissing values before cleaning:")
print(df.isnull().sum())

# Remove duplicate records
df = df.drop_duplicates()

# Remove records where the target value is missing
df = df.dropna(subset=["dose_missed"])

# Convert numerical columns into numeric format
numeric_columns = [
    "previous_missed_doses",
    "doses_taken_last_7_days",
    "medication_count"
]

for column in numeric_columns:
    df[column] = pd.to_numeric(df[column], errors="coerce")
    df[column] = df[column].fillna(df[column].median())

# Fill missing categorical values
categorical_columns = [
    "user_id",
    "scheduled_time",
    "day_of_week",
    "time_of_day"
]

for column in categorical_columns:
    df[column] = df[column].fillna(df[column].mode()[0])

# Remove invalid target values
df["dose_missed"] = pd.to_numeric(
    df["dose_missed"], errors="coerce"
)

df = df[df["dose_missed"].isin([0, 1])]

# Display cleaned dataset
print("\nCleaned Dataset:")
print(df.head())

print("\nMissing values after cleaning:")
print(df.isnull().sum())

# Save cleaned dataset
df.to_csv(BASE_DIR / "cleaned_dataset.csv", index=False)

print("\nData cleaning completed successfully!")
