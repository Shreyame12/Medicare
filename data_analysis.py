
import pandas as pd
import matplotlib.pyplot as plt

# Load the exported dataset
df = pd.read_csv("medication_history.csv")

print("Original dataset:")
print(df)

# 1. Check missing values
print("\nMissing values:")
print(df.isnull().sum())

# 2. Check duplicate records
print("\nDuplicate records:", df.duplicated().sum())

# 3. Remove duplicate records
df = df.drop_duplicates()

# 4. Convert scheduled datetime
df["scheduled_datetime"] = pd.to_datetime(
    df["scheduled_datetime"],
    errors="coerce"
)

# 5. Remove records with invalid scheduled dates
df = df.dropna(subset=["scheduled_datetime"])

# 6. Standardize status values
df["status"] = df["status"].str.strip().str.lower()

# Save cleaned data
df.to_csv("cleaned_medication_data.csv", index=False)

print("\nCleaned dataset:")
print(df)

# 7. Visualize dose status
status_counts = df["status"].value_counts()

status_counts.plot(kind="bar")

plt.title("Medication Dose Status")
plt.xlabel("Dose Status")
plt.ylabel("Number of Doses")
plt.tight_layout()
plt.savefig("dose_status_chart.png")
plt.show()

# 8. Visualize missed doses by weekday
missed = df[df["status"] == "missed"]

weekday_counts = missed["day_of_week"].value_counts()

weekday_counts.plot(kind="bar")

plt.title("Missed Doses by Weekday")
plt.xlabel("Day of Week")
plt.ylabel("Number of Missed Doses")
plt.tight_layout()
plt.savefig("missed_doses_weekday.png")
plt.show()

print("\nData cleaning and visualization completed!")
