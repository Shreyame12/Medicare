

from pathlib import Path
import joblib
import pandas as pd


# Get the ML folder path
BASE_DIR = Path(__file__).resolve().parent

# Load the trained model
MODEL_PATH = BASE_DIR / "medication_model.pkl"
model = joblib.load(MODEL_PATH)


def predict_missed_dose(input_data):
    """
    Predict whether a user is likely to miss a scheduled dose.

    Required input:
    {
        "previous_missed_doses": 3,
        "doses_taken_last_7_days": 4,
        "medication_count": 3,
        "scheduled_hour": 8,
        "day_of_week": "Monday",
        "time_of_day": "Morning"
    }
    """

    required_fields = [
        "previous_missed_doses",
        "doses_taken_last_7_days",
        "medication_count",
        "scheduled_hour",
        "day_of_week",
        "time_of_day"
    ]

    # Check whether all inputs are provided
    if not isinstance(input_data, dict):
        raise ValueError("Input must be a dictionary")

    for field in required_fields:
        if field not in input_data or input_data[field] is None:
            raise ValueError(f"Missing input: {field}")

    # Validate numerical inputs
    numeric_fields = [
        "previous_missed_doses",
        "doses_taken_last_7_days",
        "medication_count",
        "scheduled_hour"
    ]

    values = {}

    for field in numeric_fields:
        try:
            value = float(input_data[field])
        except (TypeError, ValueError):
            raise ValueError(f"{field} must be a number")

        if not value.is_integer():
            raise ValueError(f"{field} must be a whole number")

        if value < 0:
            raise ValueError(f"{field} cannot be negative")

        values[field] = int(value)

    if values["scheduled_hour"] > 23:
        raise ValueError("scheduled_hour must be between 0 and 23")

    # Get feature names used during model training
    feature_names = list(model.feature_names_in_)

    # Initialize all features with zero
    data = {feature: 0 for feature in feature_names}

    # Add numerical features
    for field, value in values.items():
        if field not in data:
            raise ValueError(f"Model does not contain feature: {field}")

        data[field] = value

    # Find the matching day-of-week feature
    day = str(input_data["day_of_week"]).strip().lower()

    day_feature = next(
        (
            feature for feature in feature_names
            if feature.startswith("day_of_week_")
            and feature[len("day_of_week_"):].lower() == day
        ),
        None
    )

    if day_feature is None:
        raise ValueError("Invalid day_of_week value")

    data[day_feature] = 1

    # Find the matching time-of-day feature
    time = str(input_data["time_of_day"]).strip().lower()

    time_feature = next(
        (
            feature for feature in feature_names
            if feature.startswith("time_of_day_")
            and feature[len("time_of_day_"):].lower() == time
        ),
        None
    )

    if time_feature is None:
        raise ValueError("Invalid time_of_day value")

    data[time_feature] = 1

    # Arrange input features in training order
    input_df = pd.DataFrame([data], columns=feature_names)

    # Make prediction
    prediction = int(model.predict(input_df)[0])

    # Get probability of missing the dose (class 1)
    classes = list(model.classes_)
    missed_index = classes.index(1)

    risk = model.predict_proba(input_df)[0][missed_index]

    # Return result to backend
    return {
        "missed_dose_prediction": prediction,
        "missed_dose_risk_percent": round(float(risk) * 100, 2)
    }
