
import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split

# Locate the ML folder
BASE_DIR = Path(__file__).parent

# Load cleaned dataset
df = pd.read_csv(BASE_DIR / "cleaned_dataset.csv")

# Remove user ID because it is an identifier, not a useful prediction feature
df = df.drop(columns=["user_id"])

# Convert scheduled time into hour
df["scheduled_hour"] = pd.to_datetime(
    df["scheduled_time"], format="%H:%M"
).dt.hour

df = df.drop(columns=["scheduled_time"])

# Convert categorical columns into numerical values
df = pd.get_dummies(
    df,
    columns=["day_of_week", "time_of_day"],
    dtype=int
)

# Separate input features and target
X = df.drop(columns=["dose_missed"])
y = df["dose_missed"]

# Check dataset size and class distribution
print("Dataset size:", len(df))
print("\nTarget distribution:")
print(y.value_counts())

# A reliable train/test split needs enough examples of each class.
# For this small starter dataset, keep all records for initial model development.
if y.value_counts().min() >= 2 and len(df) >= 10:
    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=0.25,
        random_state=42,
        stratify=y
    )

    print("\nTraining and testing split completed.")
else:
    X_train, X_test, y_train, y_test = X, X, y, y
    print("\nDataset is too small for a reliable split yet.")

# Save prepared datasets
X_train.to_csv(BASE_DIR / "X_train.csv", index=False)
X_test.to_csv(BASE_DIR / "X_test.csv", index=False)
y_train.to_csv(BASE_DIR / "y_train.csv", index=False)
y_test.to_csv(BASE_DIR / "y_test.csv", index=False)

print("\nPreprocessing completed successfully!")
print("Training records:", len(X_train))
print("Testing records:", len(X_test))
print("\nFeatures used:")
print(list(X.columns))
