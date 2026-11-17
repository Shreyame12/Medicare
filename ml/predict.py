
import pandas as pd
from pathlib import Path
import joblib

BASE_DIR = Path(__file__).parent

# Load the trained model
model = joblib.load(BASE_DIR / "medication_model.pkl")

# Get medication details from the user
print("===== MediCare: Missed Dose Prediction =====")

previous_missed_doses = int(input("Enter previous missed doses: "))
doses_taken_last_7_days = int(input("Enter doses taken in last 7 days: "))
medication_count = int(input("Enter number of medications: "))
scheduled_hour = int(input("Enter scheduled hour (0-23): "))

day = input("Enter day (Monday-Sunday): ").capitalize()
time_of_day = input("Enter time (Morning/Afternoon/Night): ").capitalize()

# Prepare input data
input_data = pd.DataFrame([{
    "previous_missed_doses": previous_missed_doses,
    "doses_taken_last_7_days": doses_taken_last_7_days,
    "medication_count": medication_count,
    "scheduled_hour": scheduled_hour,
    "day_of_week_Friday": int(day == "Friday"),
    "day_of_week_Monday": int(day == "Monday"),
    "day_of_week_Saturday": int(day == "Saturday"),
    "day_of_week_Sunday": int(day == "Sunday"),
    "day_of_week_Thursday": int(day == "Thursday"),
    "day_of_week_Tuesday": int(day == "Tuesday"),
    "day_of_week_Wednesday": int(day == "Wednesday"),
    "time_of_day_Afternoon": int(time_of_day == "Afternoon"),
    "time_of_day_Morning": int(time_of_day == "Morning"),
    "time_of_day_Night": int(time_of_day == "Night")
}])

# Predict missed-dose risk
prediction = model.predict(input_data)[0]
probability = model.predict_proba(input_data)[0][1]

print("\n===== Prediction Result =====")

if prediction == 1:
    print("Higher risk of missing this dose.")
else:
    print("Lower risk of missing this dose.")

print(f"Estimated missed-dose risk: {probability * 100:.2f}%")
