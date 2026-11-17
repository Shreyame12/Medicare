
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

BASE_DIR = Path(__file__).parent

# Load cleaned dataset
df = pd.read_csv(BASE_DIR / "cleaned_dataset.csv")

# Create folder to save graphs
GRAPH_DIR = BASE_DIR / "graphs"
GRAPH_DIR.mkdir(exist_ok=True)

sns.set_theme(style="whitegrid")

# 1. Taken vs Missed Doses
plt.figure(figsize=(7, 5))
sns.countplot(data=df, x="dose_missed")
plt.title("Taken vs Missed Doses")
plt.xlabel("Dose Status (0 = Taken, 1 = Missed)")
plt.ylabel("Number of Doses")
plt.savefig(GRAPH_DIR / "taken_vs_missed.png")
plt.show()
plt.close()

# 2. Medication Adherence Distribution
plt.figure(figsize=(7, 5))
status_counts = df["dose_missed"].value_counts()
plt.pie(
    [status_counts.get(0, 0), status_counts.get(1, 0)],
    labels=["Taken", "Missed"],
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Medication Adherence Distribution")
plt.savefig(GRAPH_DIR / "adherence_distribution.png")
plt.show()
plt.close()

# 3. Missed Doses by Time of Day
plt.figure(figsize=(7, 5))
sns.countplot(
    data=df[df["dose_missed"] == 1],
    x="time_of_day",
    order=["Morning", "Afternoon", "Night"]
)
plt.title("Missed Doses by Time of Day")
plt.xlabel("Time of Day")
plt.ylabel("Number of Missed Doses")
plt.savefig(GRAPH_DIR / "missed_by_time.png")
plt.show()
plt.close()

# 4. Missed Doses by Day of Week
plt.figure(figsize=(9, 5))
sns.countplot(
    data=df[df["dose_missed"] == 1],
    x="day_of_week",
    order=[
        "Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday"
    ]
)
plt.title("Missed Doses by Day of Week")
plt.xlabel("Day")
plt.ylabel("Number of Missed Doses")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig(GRAPH_DIR / "missed_by_day.png")
plt.show()
plt.close()

# 5. Medication Adherence Overview
plt.figure(figsize=(7, 5))
adherence = (df["dose_missed"] == 0).mean() * 100
missed = (df["dose_missed"] == 1).mean() * 100

plt.bar(
    ["Taken", "Missed"],
    [adherence, missed]
)
plt.title("Medication Adherence Overview")
plt.ylabel("Percentage of Doses")
plt.ylim(0, 100)
plt.savefig(GRAPH_DIR / "adherence_overview.png")
plt.show()
plt.close()

print("All graphs generated successfully!")
print("Graphs saved in:", GRAPH_DIR)
